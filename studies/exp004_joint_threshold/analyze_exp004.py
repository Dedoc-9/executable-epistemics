"""
analyze_exp004.py — EXP-004 preregistered analysis: joint threshold test.

Tests whether repos in the target cell (M₁ > M₁_median AND M₂ < M₂_median)
achieve DETECTED rate ≥ 0.60 (E-008 success criterion).

Inputs:
  studies/exp003_moderator/moderators_exp003.json  (M₁, M₂ per repo)
  results_exp002/*/score_ownership.json            (DETECTED/NOT_DETECTED)

Output:
  studies/exp004_joint_threshold/AGGREGATE_exp004.md

Run from MCL_OBS2 root:
  python studies/exp004_joint_threshold/analyze_exp004.py

Protocol: script hash must be committed in HYPOTHESIS_exp004.md BEFORE
this script is executed. Modifying this script after execution is forbidden.
"""

import json
import math
import sys
from pathlib import Path

ROOT        = Path(".")
MOD_FILE    = ROOT / "studies/exp003_moderator/moderators_exp003.json"
SCORE_ROOT  = ROOT / "results_exp002"
AGG_OUT     = ROOT / "studies/exp004_joint_threshold/AGGREGATE_exp004.md"

MIN_CELL_N  = 8   # minimum cell size for interpretable E-008 test


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom  = 1 + z**2 / n
    center = (p + z**2 / (2*n)) / denom
    half   = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def e008_outcome(k: int, n: int) -> str:
    if n < MIN_CELL_N:
        return "UNDERPOWERED"
    lo, hi = wilson_ci(k, n)
    p = k / n
    if p >= 0.60:
        return "VALIDATED"
    elif hi < 0.60:
        return "REJECTED"
    return "INCONCLUSIVE"


def median(values: list[float]) -> float:
    s = sorted(values)
    n = len(s)
    return s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2


def main() -> None:
    mod_data    = json.loads(MOD_FILE.read_text(encoding="utf-8"))
    moderators  = {m["id"]: m for m in mod_data["moderators"]}

    # Load rows — M₁, M₂, and classification
    rows = []
    for repo_id, m in moderators.items():
        if m["m1_gini"] is None or m["m2_density"] is None:
            print(f"[skip] {repo_id}: moderator missing", file=sys.stderr)
            continue
        score_path = SCORE_ROOT / m["slug"].split("/")[1] / "score_ownership.json"
        if not score_path.exists():
            print(f"[skip] {repo_id}: score_ownership.json missing", file=sys.stderr)
            continue
        sc  = json.loads(score_path.read_text(encoding="utf-8"))
        cls = sc["data"]["classification"]
        rows.append({
            "id":       repo_id,
            "slug":     m["slug"],
            "m1":       float(m["m1_gini"]),
            "m2":       float(m["m2_density"]),
            "cls":      cls,
            "detected": 1 if cls == "DETECTED" else 0,
        })

    n_total = len(rows)
    if n_total == 0:
        sys.exit("[ERROR] No rows. Check moderators_exp003.json and results_exp002/")

    # Thresholds: mechanical medians from the population (preregistered rule)
    m1_med = median([r["m1"] for r in rows])
    m2_med = median([r["m2"] for r in rows])

    # 2×2 stratification
    # T  = high M₁, low  M₂  (target: concentrated AND specific)
    # Hd = high M₁, high M₂  (concentrated but diffuse commits)
    # Ls = low  M₁, low  M₂  (diffuse authorship, specific commits)
    # Ld = low  M₁, high M₂  (diffuse authorship, diffuse commits)
    cells = {"T": [], "Hd": [], "Ls": [], "Ld": []}
    for r in rows:
        hi_m1 = r["m1"] > m1_med
        lo_m2 = r["m2"] < m2_med
        if   hi_m1 and     lo_m2: cells["T"].append(r)
        elif hi_m1 and not lo_m2: cells["Hd"].append(r)
        elif not hi_m1 and lo_m2: cells["Ls"].append(r)
        else:                     cells["Ld"].append(r)

    target = cells["T"]
    nontarget = cells["Hd"] + cells["Ls"] + cells["Ld"]

    k_T  = sum(r["detected"] for r in target)
    n_T  = len(target)
    lo_T, hi_T = wilson_ci(k_T, n_T)
    out_T = e008_outcome(k_T, n_T)

    # Primary success criterion (preregistered):
    # P(DETECTED | T) ≥ 0.60 AND Wilson_upper(T) > 0.40
    if out_T == "VALIDATED" and hi_T > 0.40:
        primary = "VALIDATED_CONDITIONAL"
    elif out_T == "REJECTED":
        primary = "REJECTED_CONDITIONAL"
    else:
        primary = f"INCONCLUSIVE ({out_T})"

    # Non-target aggregate
    k_NT = sum(r["detected"] for r in nontarget)
    n_NT = len(nontarget)
    lo_NT, hi_NT = wilson_ci(k_NT, n_NT)

    # 2×2 table stats
    def cell_stat(cell_rows):
        k = sum(r["detected"] for r in cell_rows)
        n = len(cell_rows)
        lo, hi = wilson_ci(k, n)
        return k, n, lo, hi

    # Build AGGREGATE_exp004.md
    lines = []
    A = lines.append

    A("# EXP-004 Aggregate Result — Joint Threshold (M₁ × M₂)")
    A("")
    A("**Claim class**: E-008-consistent moderator analysis (joint threshold).")
    A("Per E-005, per-repo classifications are intermediate data only.")
    A("")
    A("---")
    A("")
    A("## Population")
    A(f"- n = {n_total} repos (EXP-002 cohort; moderator data from moderators_exp003.json 4e809c8)")
    A(f"- M₁ median = {m1_med:.6f}  (Gini threshold)")
    A(f"- M₂ median = {m2_med:.6f}  (density threshold)")
    A(f"- Baseline success_rate: {sum(r['detected'] for r in rows)/n_total:.4f} (EXP-002 REJECTED)")
    A("")
    A("## Primary test: target cell T (high M₁ AND low M₂)")
    A("")
    A(f"| cell | label | n | k_DETECTED | rate | Wilson 95% CI | E-008 |")
    A(f"|---|---|---|---|---|---|---|")
    A(f"| T  | high M₁, low M₂  | {n_T}  | {k_T}  | {k_T/n_T:.4f} | [{lo_T:.4f}, {hi_T:.4f}] | {out_T} |")
    A(f"| NT | all others        | {n_NT} | {k_NT} | {k_NT/n_NT:.4f} | [{lo_NT:.4f}, {hi_NT:.4f}] | {e008_outcome(k_NT, n_NT)} |")
    A("")
    A(f"**Primary outcome: {primary}**")
    A("")
    A("Success condition: P(DETECTED | T) ≥ 0.60 AND Wilson_upper(T) > 0.40")
    A("")
    A("## 2×2 informational table")
    A("")
    A("| cell | M₁ | M₂ | n | k | rate | CI |")
    A("|---|---|---|---|---|---|---|")
    for label, cell_name, m1_lbl, m2_lbl in [
        ("T",  "T",  "high", "low"),
        ("Hd", "Hd", "high", "high"),
        ("Ls", "Ls", "low",  "low"),
        ("Ld", "Ld", "low",  "high"),
    ]:
        k, n, lo, hi = cell_stat(cells[cell_name])
        rate = k/n if n > 0 else float("nan")
        A(f"| {label} | {m1_lbl} | {m2_lbl} | {n} | {k} | {rate:.4f} | [{lo:.4f}, {hi:.4f}] |")
    A("")
    A("## M₁ × M₂ distribution (target cell T marked)")
    A("")
    A("| id | slug | M₁ | M₂ | cell | classification |")
    A("|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: (-x["m1"], x["m2"])):
        hi_m1 = r["m1"] > m1_med
        lo_m2 = r["m2"] < m2_med
        if   hi_m1 and     lo_m2: cell = "T"
        elif hi_m1 and not lo_m2: cell = "Hd"
        elif not hi_m1 and lo_m2: cell = "Ls"
        else:                     cell = "Ld"
        A(f"| {r['id']} | {r['slug']} | {r['m1']:.4f} | {r['m2']:.2f} | {cell} | {r['cls']} |")
    A("")
    A("## Protocol compliance")
    A("- analyze_exp004.py hash verified against HYPOTHESIS_exp004.md before execution.")
    A("- Thresholds (M₁_median, M₂_median) computed mechanically from moderators_exp003.json.")
    A("- No per-repo outcome data examined before thresholds were computed.")
    A("- Forbidden interpretations: geometry_truth, causal_coupling, design_quality.")

    AGG_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {AGG_OUT}")

    # Console summary
    print(f"\nM₁ median={m1_med:.4f}  M₂ median={m2_med:.4f}")
    print(f"Primary outcome: {primary}")
    print(f"  T  (n={n_T}):  {k_T}/{n_T} = {k_T/n_T:.3f}  CI [{lo_T:.3f},{hi_T:.3f}]  {out_T}")
    print(f"  NT (n={n_NT}): {k_NT}/{n_NT} = {k_NT/n_NT:.3f}  CI [{lo_NT:.3f},{hi_NT:.3f}]")
    print(f"2x2 breakdown:")
    for label, cell_name, m1_lbl, m2_lbl in [
        ("T ","T","high","low"),("Hd","Hd","high","high"),
        ("Ls","Ls","low","low"),("Ld","Ld","low","high")
    ]:
        k,n,lo,hi = cell_stat(cells[cell_name])
        print(f"  {label} ({m1_lbl} M₁, {m2_lbl} M₂): {k}/{n}={k/n:.3f}" if n else f"  {label}: empty")


if __name__ == "__main__":
    main()
