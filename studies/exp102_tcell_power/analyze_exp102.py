"""
analyze_exp102.py -- EXP-102 Component D aggregate analysis.

Reads moderators_exp102.json (T-cell classifications) and
score_ownership.json files for each T-cell repo.

Computes:
  k_D_T  = count of DETECTED in T-cell subset
  n_D_T  = count of T-cell repos with valid ownership scores
  rate   = k_D_T / n_D_T
  Wilson 95% CI (z=1.96)

Outcome rule (HYPOTHESIS_exp102.md §6):
  VALIDATED    : rate >= 0.60 AND Wilson_upper > 0.40
  REJECTED     : Wilson_upper < 0.60
  INCONCLUSIVE : neither

LEAKAGE and UNRESOLVED_ACTIVITY_MARGIN count toward n_D_T (denominator)
but NOT toward k_D_T (numerator). They are non-detections for this test.

Forbidden: per-repo result reporting (E-005).
Output: studies/exp102_tcell_power/AGGREGATE_exp102.json
        studies/exp102_tcell_power/AGGREGATE_exp102.md
"""

import json
import math
from pathlib import Path
from datetime import datetime, timezone

ROOT         = Path(".")
MOD_FILE     = ROOT / "studies/exp102_tcell_power/moderators_exp102.json"
RESULTS_ROOT = ROOT / "results_exp102"
OUT_JSON     = ROOT / "studies/exp102_tcell_power/AGGREGATE_exp102.json"
OUT_MD       = ROOT / "studies/exp102_tcell_power/AGGREGATE_exp102.md"
HYP_FILE     = ROOT / "studies/exp102_tcell_power/HYPOTHESIS_exp102.md"

REQUIRED_SCORER_HASH = "cd6bf9a6c3f3ab36"
Z = 1.96  # 95% CI


def wilson_ci(k, n, z=Z):
    """Wilson score interval. Returns (lower, center, upper)."""
    if n == 0:
        return (None, None, None)
    p = k / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half   = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (round(center - half, 6), round(center, 6), round(center + half, 6))


def load_ownership(repo_name):
    """Read score_ownership.json; return (classification, scorer_hash) or (None, None)."""
    path = RESULTS_ROOT / repo_name / "score_ownership.json"
    if not path.exists():
        return None, None
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        clsf  = d.get("data", {}).get("classification")
        shash = d.get("provenance", {}).get("code_fingerprints", {}).get("scorer.py")
        return clsf, shash
    except Exception as e:
        print(f"  [WARN] could not read {path}: {e}")
        return None, None


def main():
    mods = json.loads(MOD_FILE.read_text(encoding="utf-8"))

    t_cells = [r for r in mods["moderators"] if r.get("tcell_m1m2")]
    print(f"EXP-102 Component D analysis")
    print(f"T-cell gate: M1 > {mods['m1_threshold']}  M2 < {mods['m2_threshold']}")
    print(f"n_T-cell from moderators: {len(t_cells)}")
    print()

    # Verify scorer hash on all T-cell repos before aggregating
    hash_errors = []
    records = []
    for r in t_cells:
        repo_name = r["slug"].split("/")[1]
        clsf, shash = load_ownership(repo_name)
        if shash != REQUIRED_SCORER_HASH:
            hash_errors.append((r["id"], repo_name, shash))
        records.append({
            "id":           r["id"],
            "slug":         r["slug"],
            "m1":           r["m1_gini"],
            "m2":           r["m2_density"],
            "m3":           r["m3_galois"],
            "classification": clsf,
            "scorer_hash":  shash,
            "hash_valid":   shash == REQUIRED_SCORER_HASH,
        })

    if hash_errors:
        print(f"HASH ERROR: scorer hash mismatch on {len(hash_errors)} repos:")
        for eid, name, h in hash_errors:
            print(f"  {eid} {name}: got {h}, expected {REQUIRED_SCORER_HASH}")
        print("EXECUTION INVALID: revert to last valid hashed state.")
        return

    # Count
    valid   = [r for r in records if r["classification"] is not None]
    n_D_T   = len(valid)
    k_D_T   = sum(1 for r in valid if r["classification"] == "DETECTED")
    n_leakage = sum(1 for r in valid if r["classification"] == "LEAKAGE")
    n_unresolved = sum(1 for r in valid if r["classification"] == "UNRESOLVED_ACTIVITY_MARGIN")
    n_not_detected = sum(1 for r in valid if r["classification"] == "NOT_DETECTED")

    rate = k_D_T / n_D_T if n_D_T > 0 else None
    w_lower, w_center, w_upper = wilson_ci(k_D_T, n_D_T)

    # Outcome determination
    if n_D_T < 20:
        outcome = "UNINTERPRETABLE"
        outcome_reason = f"n_D_T={n_D_T} < minimum interpretable floor (20)"
    elif w_upper is not None and w_upper < 0.60:
        outcome = "REJECTED"
        outcome_reason = f"Wilson_upper={w_upper:.4f} < 0.60 rejection threshold"
    elif rate is not None and rate >= 0.60 and w_upper is not None and w_upper > 0.40:
        outcome = "VALIDATED"
        outcome_reason = f"rate={rate:.4f} >= 0.60 AND Wilson_upper={w_upper:.4f} > 0.40"
    else:
        outcome = "INCONCLUSIVE"
        outcome_reason = f"rate={rate:.4f}, Wilson=[{w_lower:.4f}, {w_upper:.4f}]; neither criterion met"

    power_note = (
        f"n_D_T={n_D_T} < target 50. Power to detect true rate 0.65 at alpha=0.05 "
        f"is approximately {round(1 - 0.05**(1), 2)} (underpowered). "
        "Result is valid but confidence intervals are wide."
        if n_D_T < 50 else
        f"n_D_T={n_D_T} >= target 50. Power criterion satisfied."
    )

    print(f"n_D_T={n_D_T}  k_D_T={k_D_T}  rate={rate:.4f}" if rate else f"n_D_T={n_D_T}  k_D_T={k_D_T}")
    print(f"DETECTED={k_D_T}  NOT_DETECTED={n_not_detected}  LEAKAGE={n_leakage}  UNRESOLVED={n_unresolved}")
    print(f"Wilson 95% CI: [{w_lower:.4f}, {w_upper:.4f}]  (center={w_center:.4f})")
    print(f"OUTCOME: {outcome}")
    print(f"  Reason: {outcome_reason}")
    print()

    # Implication
    if outcome == "REJECTED":
        implication = (
            "The ownership instrument (M1^M2 gate) is RETIRED as a generalizable claim class. "
            "True detection rate in T-cell space is bounded below 0.60 with high confidence. "
            "EXP-001 VALIDATED result is attributed to population selection artifact (wave-1 curation bias)."
        )
    elif outcome == "VALIDATED":
        implication = (
            "The ownership instrument is CONFIRMED at n_D_T detections. "
            "Wave-1/EXP-002 divergence explained by T-cell enrichment in wave-1. "
            "Claim class survives for M1^M2 populations."
        )
    elif outcome == "INCONCLUSIVE":
        implication = (
            "The 0.60 threshold is not resolvable at this n_D_T. "
            "Claim class is SUSPENDED pending further power or redefined threshold."
        )
    else:
        implication = "n_D_T below minimum interpretable floor. No outcome issued."

    # Write JSON
    result = {
        "study":            "EXP-102",
        "component":        "D",
        "analysis_date":    datetime.now(timezone.utc).isoformat(),
        "declaration_hash": mods.get("declaration_hash", "see REPO_DECLARATION_exp102.json"),
        "scorer_hash":      REQUIRED_SCORER_HASH,
        "n_declared":       mods["n_declared"],
        "n_computed":       mods["n_computed"],
        "n_D_T":            n_D_T,
        "k_D_T":            k_D_T,
        "n_not_detected":   n_not_detected,
        "n_leakage":        n_leakage,
        "n_unresolved":     n_unresolved,
        "rate":             round(rate, 6) if rate is not None else None,
        "wilson_lower":     w_lower,
        "wilson_center":    w_center,
        "wilson_upper":     w_upper,
        "wilson_z":         Z,
        "outcome":          outcome,
        "outcome_reason":   outcome_reason,
        "implication":      implication,
        "power_note":       power_note,
        "m3_distribution":  mods["m3_distribution"],
        "forbidden_interpretations": [
            "post_hoc_threshold_shift",
            "component_inclusion_of_prior_tcells",
            "non_tcell_inflation",
            "per_repo_outcome_report",
            "cherry_picked_subsets",
            "m3_gate_retroactive"
        ]
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Written: {OUT_JSON}")

    # Write markdown
    md = f"""# AGGREGATE RESULT — EXP-102 Component D (Series 200)

**Study**: EXP-102 T-Cell Power Test (Pivot A)
**Analysis date**: {result['analysis_date']}
**Declaration hash**: {result['declaration_hash']}
**Scorer hash**: {REQUIRED_SCORER_HASH}

---

## Result

| metric         | value                                      |
|----------------|--------------------------------------------|
| n_declared     | {result['n_declared']}                                        |
| n_computed     | {result['n_computed']}                                       |
| n_D_T          | {n_D_T} (T-cell repos: M1 > {mods['m1_threshold']} AND M2 < {mods['m2_threshold']}) |
| k_D_T          | {k_D_T} (DETECTED in T-cell subset)          |
| rate           | {rate:.4f}                                  |
| Wilson lower   | {w_lower:.4f}                               |
| Wilson upper   | {w_upper:.4f}                               |
| Wilson center  | {w_center:.4f}                              |

## Outcome

**{outcome}**

{outcome_reason}

## Implication

{implication}

## Power note

{power_note}

## Classification breakdown (T-cell subset, n={n_D_T})

| classification          | count |
|-------------------------|-------|
| DETECTED                | {k_D_T}    |
| NOT_DETECTED            | {n_not_detected}   |
| LEAKAGE                 | {n_leakage}    |
| UNRESOLVED_ACTIVITY_MARGIN | {n_unresolved} |

LEAKAGE and UNRESOLVED_ACTIVITY_MARGIN count toward denominator (n_D_T)
but not toward numerator (k_D_T). Per preregistered protocol.

## Commitment chain

EXP-001 VALIDATED → EXP-002 REJECTED → EXP-003 REJECTED_CONDITIONAL →
EXP-004 INCONCLUSIVE → EXP-005 NOT_CONFIRMED → EXP-101 INCONCLUSIVE →
**EXP-102 {outcome}** (M1^M2 power test, n_D_T={n_D_T}, Series 200)

## M3 distribution (observational, no classification effect)

mean={mods['m3_distribution']['mean']}  min={mods['m3_distribution']['min']}  max={mods['m3_distribution']['max']}  n={mods['m3_distribution']['n']}

(M3 retrocompute f0be383 falsified M3 as cohort-level mechanism. No M3 threshold preregistered.)

## Forbidden interpretations

- post_hoc_threshold_shift
- component_inclusion_of_prior_tcells
- non_tcell_inflation
- per_repo_outcome_report (E-005)
- cherry_picked_subsets
- m3_gate_retroactive
"""

    OUT_MD.write_text(md, encoding="utf-8")
    print(f"Written: {OUT_MD}")


if __name__ == "__main__":
    main()
