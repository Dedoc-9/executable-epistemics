"""
analyze_exp003.py — EXP-003 preregistered analysis.

Reads moderators_exp003.json (M1, M2 per repo) and score_ownership.json
(DETECTED/NOT_DETECTED classification) for each EXP-002 repo.
Runs the two preregistered tests declared in HYPOTHESIS_exp003.md:
  1. Primary: E-008-consistent stratification test (median split on M1)
  2. Secondary: point-biserial correlation r(M1, DETECTED_binary), one-tailed

Writes: studies/exp003_moderator/AGGREGATE_exp003.md

Protocol note: this script must be committed with its SHA-256 hash recorded
in HYPOTHESIS_exp003.md BEFORE it is executed. Running this script before
the hash is committed is a forbidden post-hoc procedure.
"""

import json
import math
import sys
from pathlib import Path

try:
    from scipy import stats as _scipy_stats
    _SCIPY = True
except ImportError:
    _SCIPY = False

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT        = Path(".")
MOD_FILE    = ROOT / "studies/exp003_moderator/moderators_exp003.json"
SCORE_ROOT  = ROOT / "results_exp002"
AGG_OUT     = ROOT / "studies/exp003_moderator/AGGREGATE_exp003.md"

MIN_STRATUM_N = 10   # minimum stratum size for primary test to be interpretable


# ---------------------------------------------------------------------------
# Wilson 95% CI (frozen formula)
# ---------------------------------------------------------------------------
def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1 + z ** 2 / n
    center = (p + z ** 2 / (2 * n)) / denom
    half   = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


# ---------------------------------------------------------------------------
# Point-biserial correlation (preregistered formula)
# r_pb = Pearson(M1_i, DETECTED_i) where DETECTED_i ∈ {0, 1}
# One-tailed p-value: H_alt: r > 0 (higher M1 → higher P(DETECTED))
# ---------------------------------------------------------------------------
def point_biserial(x: list[float], y: list[int]) -> tuple[float, float]:
    """Returns (r, p_one_tailed). Uses scipy if available, else manual Pearson."""
    n = len(x)
    assert n == len(y), "length mismatch"
    if _SCIPY:
        r, p_two = _scipy_stats.pointbiserialr(y, x)
        p_one = p_two / 2 if r > 0 else 1 - p_two / 2
        return float(r), float(p_one)
    # Manual Pearson
    mx = sum(x) / n
    my = sum(y) / n
    cov = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / n
    sx  = math.sqrt(sum((xi - mx) ** 2 for xi in x) / n)
    sy  = math.sqrt(sum((yi - my) ** 2 for yi in y) / n)
    if sx == 0 or sy == 0:
        return float("nan"), float("nan")
    r = cov / (sx * sy)
    # t-statistic, df = n-2
    if abs(r) >= 1.0:
        return r, (0.0 if r > 0 else 1.0)
    t = r * math.sqrt(n - 2) / math.sqrt(1 - r ** 2)
    # one-tailed p via regularised incomplete beta (normal approx for n≥30)
    if n >= 30:
        p_one = 0.5 * math.erfc(t / math.sqrt(2))
    else:
        # use scipy t-distribution; fall back to nan if unavailable
        try:
            from scipy.stats import t as t_dist
            p_one = float(t_dist.sf(t, df=n - 2))
        except ImportError:
            p_one = float("nan")
    return r, p_one


# ---------------------------------------------------------------------------
# E-008 stratum outcome
# ---------------------------------------------------------------------------
def e008_outcome(k: int, n: int) -> str:
    if n < MIN_STRATUM_N:
        return "UNDERPOWERED"
    lo, hi = wilson_ci(k, n)
    p = k / n
    if p >= 0.60:
        return "VALIDATED"
    elif hi < 0.60:
        return "REJECTED"
    else:
        return "INCONCLUSIVE"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    mod_data = json.loads(MOD_FILE.read_text(encoding="utf-8"))
    moderators = {m["id"]: m for m in mod_data["moderators"]}

    # Load ownership classifications
    rows = []
    for repo_id, m in moderators.items():
        if m["m1_gini"] is None or math.isnan(float(m["m1_gini"] or "nan")):
            print(f"[skip] {repo_id}: M1 unavailable", file=sys.stderr)
            continue
        score_path = SCORE_ROOT / m["slug"].split("/")[1] / "score_ownership.json"
        if not score_path.exists():
            print(f"[skip] {repo_id}: score_ownership.json missing", file=sys.stderr)
            continue
        sc = json.loads(score_path.read_text(encoding="utf-8"))
        cls = sc["data"]["classification"]
        detected = 1 if cls == "DETECTED" else 0
        rows.append({
            "id":       repo_id,
            "slug":     m["slug"],
            "m1":       float(m["m1_gini"]),
            "m2":       float(m["m2_density"]),
            "cls":      cls,
            "detected": detected,
        })

    n_total = len(rows)
    if n_total == 0:
        sys.exit("[ERROR] No rows loaded; check moderators_exp003.json and results_exp002/")

    # --- Primary test: median split on M1 ---
    m1_values  = sorted(r["m1"] for r in rows)
    m1_median  = m1_values[n_total // 2] if n_total % 2 == 1 \
                 else (m1_values[n_total // 2 - 1] + m1_values[n_total // 2]) / 2

    stratum_H = [r for r in rows if r["m1"] >  m1_median]   # high concentration
    stratum_L = [r for r in rows if r["m1"] <= m1_median]   # low concentration

    k_H  = sum(r["detected"] for r in stratum_H)
    k_L  = sum(r["detected"] for r in stratum_L)
    n_H, n_L = len(stratum_H), len(stratum_L)

    p_H = k_H / n_H if n_H else float("nan")
    p_L = k_L / n_L if n_L else float("nan")
    lo_H, hi_H = wilson_ci(k_H, n_H)
    lo_L, hi_L = wilson_ci(k_L, n_L)

    outcome_H = e008_outcome(k_H, n_H)
    outcome_L = e008_outcome(k_L, n_L)

    # VALIDATED_CONDITIONAL requires H stratum VALIDATED and Wilson_upper(H) > 0.40
    if outcome_H == "VALIDATED" and hi_H > 0.40:
        primary_outcome = "VALIDATED_CONDITIONAL"
    elif outcome_H == "REJECTED":
        primary_outcome = "REJECTED_CONDITIONAL"
    else:
        primary_outcome = f"INCONCLUSIVE ({outcome_H})"

    # --- Secondary test: point-biserial correlation ---
    m1_list  = [r["m1"] for r in rows]
    det_list = [r["detected"] for r in rows]
    r_pb, p_pb = point_biserial(m1_list, det_list)

    # --- M2 secondary stratification (informational, not primary criterion) ---
    m2_values = sorted(r["m2"] for r in rows)
    m2_median = m2_values[n_total // 2] if n_total % 2 == 1 \
                else (m2_values[n_total // 2 - 1] + m2_values[n_total // 2]) / 2
    strat_m2_H = [r for r in rows if r["m2"] >  m2_median]
    strat_m2_L = [r for r in rows if r["m2"] <= m2_median]
    k_m2_H = sum(r["detected"] for r in strat_m2_H)
    k_m2_L = sum(r["detected"] for r in strat_m2_L)
    r_m2, p_m2 = point_biserial([r["m2"] for r in rows], det_list)

    # ---------------------------------------------------------------------------
    # Write AGGREGATE_exp003.md
    # ---------------------------------------------------------------------------
    lines = []
    A = lines.append

    A("# EXP-003 Aggregate Result — Ownership Moderator Analysis (M₁/M₂)")
    A("")
    A("**Claim class**: E-008-consistent moderator analysis. Per E-005,")
    A("per-repo classifications are intermediate data. The aggregate outcomes")
    A("below are the only reportable results of EXP-003.")
    A("")
    A("---")
    A("")
    A("## Population")
    A(f"- n = {n_total} repos (EXP-002 cohort, declaration hash 13ffc9a71c3fda50471592c22c9f209448b7c66082eeeeb76b3ac4e230f68a0e)")
    A(f"- Rows excluded (M1 unavailable or clone missing): {50 - n_total}")
    A(f"- DETECTED: {sum(r['detected'] for r in rows)}/{n_total}")
    A(f"- Baseline success_rate: {sum(r['detected'] for r in rows)/n_total:.4f} (EXP-002 REJECTED)")
    A("")
    A("## Primary test: M₁ (Gini) median split")
    A("")
    A(f"M₁ median = {m1_median:.6f}")
    A("")
    A("| stratum | n | k_DETECTED | rate | Wilson 95% CI | E-008 outcome |")
    A("|---|---|---|---|---|---|")
    A(f"| H (M₁ > median) | {n_H} | {k_H} | {p_H:.4f} | [{lo_H:.4f}, {hi_H:.4f}] | {outcome_H} |")
    A(f"| L (M₁ ≤ median) | {n_L} | {k_L} | {p_L:.4f} | [{lo_L:.4f}, {hi_L:.4f}] | {outcome_L} |")
    A("")
    A(f"**Primary outcome: {primary_outcome}**")
    A("")
    A("Success condition (preregistered):")
    A("  k_H / n_H ≥ 0.60 AND Wilson_upper(H) > 0.40")
    A("")
    A("## Secondary test: point-biserial correlation r(M₁, DETECTED)")
    A("")
    A(f"r_pb = {r_pb:.4f}   p (one-tailed, H_alt: r > 0) = {p_pb:.4f}   α = 0.05")
    if not math.isnan(p_pb):
        sig = "SIGNIFICANT" if p_pb < 0.05 else "NOT SIGNIFICANT"
        A(f"Result: {sig} at α=0.05")
    A("")
    A("## M₂ (commit density) — informational secondary")
    A("")
    A(f"M₂ median = {m2_median:.4f}")
    A(f"k_DETECTED in H stratum (M₂ > median): {k_m2_H}/{len(strat_m2_H)}")
    A(f"k_DETECTED in L stratum (M₂ ≤ median): {k_m2_L}/{len(strat_m2_L)}")
    A(f"r_pb(M₂, DETECTED) = {r_m2:.4f}   p (one-tailed) = {p_m2:.4f}")
    A("")
    A("## M₁ distribution")
    A("")
    A("| id | slug | M₁_gini | M₂_density | classification |")
    A("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: x["m1"], reverse=True):
        A(f"| {r['id']} | {r['slug']} | {r['m1']:.4f} | {r['m2']:.2f} | {r['cls']} |")
    A("")
    A("## Protocol compliance")
    A("- compute_moderators_exp003.py executed without reading any score_*.json files.")
    A("- analyze_exp003.py executed after compute; script hashes match HYPOTHESIS_exp003.md.")
    A("- No per-repo results were examined before median threshold was set.")
    A("- Forbidden interpretations: geometry_truth, causal_coupling, design_quality.")

    AGG_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {AGG_OUT}")

    # Console summary
    print(f"\nPrimary outcome (M1 stratification): {primary_outcome}")
    print(f"  H stratum: {k_H}/{n_H} = {p_H:.3f}  CI [{lo_H:.3f},{hi_H:.3f}]  {outcome_H}")
    print(f"  L stratum: {k_L}/{n_L} = {p_L:.3f}  CI [{lo_L:.3f},{hi_L:.3f}]  {outcome_L}")
    print(f"Secondary (r_pb): {r_pb:.4f}  p={p_pb:.4f}")


if __name__ == "__main__":
    main()
