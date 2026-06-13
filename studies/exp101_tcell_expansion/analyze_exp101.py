"""
analyze_exp101.py — EXP-101 primary analysis: combined A+C_T pool test.

Component A: EXP-004 T-cell repos (n=11, committed 659bb06).
             Ownership scores from results_exp002/*/score_ownership.json.
Component C_T: Component C repos where M1 > M1_threshold AND M2 < M2_threshold
               (from moderators_exp101.json). Ownership from results_exp101/*/score_ownership.json.
Component B: EXP-001 wave-1 T-cell repos — confirmatory holdout ONLY, not in primary.

Primary test: k_(A+C_T) / n_(A+C_T) >= 0.60 (E-008 VALIDATED).
Success: VALIDATED if >=0.60 AND Wilson_upper > 0.40.
         REJECTED if Wilson_upper < 0.60.
         INCONCLUSIVE otherwise.

Run from MCL_OBS2 root AFTER compute_moderators_exp101.py has been run:
  python studies\\exp101_tcell_expansion\\analyze_exp101.py

Protocol: run compute_moderators_exp101.py FIRST. Do not review any ownership
scores before this script runs.
"""

import json
import math
from pathlib import Path

ROOT        = Path(".")
MOD_FILE    = ROOT / "studies/exp101_tcell_expansion/moderators_exp101.json"
RES_C       = ROOT / "results_exp101"
RES_A       = ROOT / "results_exp002"
AGG_OUT     = ROOT / "studies/exp101_tcell_expansion/AGGREGATE_exp101.md"

# ── Component A: EXP-004 T-cell repos (source: AGGREGATE_exp004.md, commit 659bb06)
# T-cell confirmed by M1 > 0.858675 AND M2 < 7.702891 in moderators_exp003.json.
COMPONENT_A = [
    {"id": "R004", "slug": "piccolo-orm/piccolo",      "name": "piccolo"},
    {"id": "R036", "slug": "boto/boto3",               "name": "boto3"},
    {"id": "R028", "slug": "agronholm/apscheduler",    "name": "apscheduler"},
    {"id": "R019", "slug": "mitmproxy/mitmproxy",      "name": "mitmproxy"},
    {"id": "R016", "slug": "aio-libs/aiohttp",         "name": "aiohttp"},
    {"id": "R026", "slug": "coleifer/huey",            "name": "huey"},
    {"id": "R020", "slug": "tiangolo/typer",           "name": "typer"},
    {"id": "R033", "slug": "PyCQA/pylint",             "name": "pylint"},
    {"id": "R005", "slug": "python-gino/gino",         "name": "gino"},
    {"id": "R045", "slug": "rubik/radon",              "name": "radon"},
    {"id": "R034", "slug": "pre-commit/pre-commit",    "name": "pre-commit"},
]

# ── Component B: EXP-001 wave-1 T-cell (confirmatory holdout — NOT in primary)
COMPONENT_B = [
    {"id": "W1_scipy",      "slug": "scipy/scipy",                "name": "scipy"},
    {"id": "W1_matplotlib", "slug": "matplotlib/matplotlib",      "name": "matplotlib"},
    {"id": "W1_django",     "slug": "django/django",              "name": "django"},
    {"id": "W1_pytest",     "slug": "pytest-dev/pytest",          "name": "pytest"},
    {"id": "W1_sqlalchemy", "slug": "sqlalchemy/sqlalchemy",      "name": "sqlalchemy"},
    {"id": "W1_mypy",       "slug": "python/mypy",                "name": "mypy"},
    {"id": "W1_pip",        "slug": "pypa/pip",                   "name": "pip"},
]

M1_THRESHOLD = 0.858675
M2_THRESHOLD = 7.702891


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom  = 1 + z**2 / n
    center = (p + z**2 / (2*n)) / denom
    half   = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def e008_outcome(k: int, n: int) -> str:
    if n < 20:
        return "UNDERPOWERED"
    lo, hi = wilson_ci(k, n)
    p = k / n
    if p >= 0.60:
        return "VALIDATED"
    elif hi < 0.60:
        return "REJECTED"
    return "INCONCLUSIVE"


def load_classification(score_path: Path) -> str | None:
    if not score_path.exists():
        return None
    sc = json.loads(score_path.read_text(encoding="utf-8"))
    return sc["data"]["classification"]


def is_detected(cls: str | None) -> int:
    return 1 if cls == "DETECTED" else 0


def main() -> None:
    # ── Load Component C moderators
    mod_data  = json.loads(MOD_FILE.read_text(encoding="utf-8"))
    mod_c_all = {m["id"]: m for m in mod_data["moderators"]}

    # ── Component A rows
    rows_a = []
    for r in COMPONENT_A:
        score_path = RES_A / r["name"] / "score_ownership.json"
        cls = load_classification(score_path)
        rows_a.append({
            "id": r["id"], "slug": r["slug"], "component": "A",
            "cls": cls or "MISSING",
            "detected": is_detected(cls)
        })

    # ── Component C_T rows (T-cell only)
    rows_c_all = []
    rows_c_t   = []
    for repo_id, m in mod_c_all.items():
        m1 = m.get("m1_gini")
        m2 = m.get("m2_density")
        if m1 is None or m2 is None:
            continue
        name = m["slug"].split("/")[1]
        score_path = RES_C / name / "score_ownership.json"
        cls = load_classification(score_path)
        row = {
            "id": repo_id, "slug": m["slug"], "component": "C",
            "m1": m1, "m2": m2,
            "t_cell": m1 > M1_THRESHOLD and m2 < M2_THRESHOLD,
            "cls": cls or "MISSING",
            "detected": is_detected(cls)
        }
        rows_c_all.append(row)
        if row["t_cell"]:
            rows_c_t.append(row)

    # ── Component B (holdout — informational only)
    rows_b = []
    for r in COMPONENT_B:
        score_path = ROOT / "results" / r["name"] / "score_ownership.json"
        cls = load_classification(score_path)
        rows_b.append({
            "id": r["id"], "slug": r["slug"], "component": "B",
            "cls": cls or "MISSING",
            "detected": is_detected(cls)
        })

    # ── Primary test: A + C_T
    combined = rows_a + rows_c_t
    n_comb   = len(combined)
    k_comb   = sum(r["detected"] for r in combined)
    lo, hi   = wilson_ci(k_comb, n_comb)
    outcome  = e008_outcome(k_comb, n_comb)

    if outcome == "VALIDATED" and hi > 0.40:
        primary = "VALIDATED"
    elif outcome == "REJECTED":
        primary = "REJECTED"
    else:
        primary = f"INCONCLUSIVE ({outcome})"

    # ── Write AGGREGATE_exp101.md
    lines = []
    A = lines.append

    A("# EXP-101 Aggregate Result — T-Cell Combined Pool (A + C_T)")
    A("")
    A("**Claim class**: E-008 primary test on preregistered combined T-cell pool.")
    A("Per E-005, per-repo classifications are intermediate data only.")
    A("")
    A("---")
    A("")
    A("## Population")
    A(f"- Component A: n={len(rows_a)} (EXP-004 T-cell, committed 659bb06)")
    A(f"- Component C declared: n={len(mod_c_all)} (REPO_DECLARATION_exp101.json, commit 5864fb2)")
    A(f"- Component C_T (T-cell confirmed): n={len(rows_c_t)} "
      f"(M1 > {M1_THRESHOLD}, M2 < {M2_THRESHOLD})")
    A(f"- Combined A + C_T: n={n_comb}")
    A(f"- Component B (holdout, not in primary): n={len(rows_b)}")
    A("")
    A("## Primary test: k_(A+C_T) / n_(A+C_T) ≥ 0.60")
    A("")
    A(f"| pool | n | k_DETECTED | rate | Wilson 95% CI | E-008 |")
    A(f"|---|---|---|---|---|---|")
    A(f"| A + C_T (primary) | {n_comb} | {k_comb} | {k_comb/n_comb:.4f} "
      f"| [{lo:.4f}, {hi:.4f}] | {outcome} |")

    # A-only and C_T-only for decomposition
    k_a  = sum(r["detected"] for r in rows_a)
    lo_a, hi_a = wilson_ci(k_a, len(rows_a))
    k_ct = sum(r["detected"] for r in rows_c_t)
    lo_ct, hi_ct = wilson_ci(k_ct, len(rows_c_t)) if rows_c_t else (float("nan"), float("nan"))

    A(f"| A only            | {len(rows_a)} | {k_a} | {k_a/len(rows_a):.4f} "
      f"| [{lo_a:.4f}, {hi_a:.4f}] | {e008_outcome(k_a, len(rows_a))} |")
    if rows_c_t:
        A(f"| C_T only          | {len(rows_c_t)} | {k_ct} | {k_ct/len(rows_c_t):.4f} "
          f"| [{lo_ct:.4f}, {hi_ct:.4f}] | {e008_outcome(k_ct, len(rows_c_t))} |")
    A("")
    A(f"**Primary outcome: {primary}**")
    A("")
    A("Success condition: k/n ≥ 0.60 AND Wilson_upper > 0.40")
    A("")
    A("## Component C T-cell classification")
    A("")
    A(f"| id | slug | M1 | M2 | T-cell | classification |")
    A(f"|---|---|---|---|---|---|")
    for r in sorted(rows_c_all, key=lambda x: (-x["m1"], x["m2"])):
        tc = "T" if r["t_cell"] else "non-T"
        A(f"| {r['id']} | {r['slug']} | {r['m1']:.4f} | {r['m2']:.2f} | {tc} | {r['cls']} |")
    A("")
    A("## Component A decomposition (EXP-004 T-cell, for audit)")
    A("")
    A(f"| id | slug | classification |")
    A(f"|---|---|---|")
    for r in rows_a:
        A(f"| {r['id']} | {r['slug']} | {r['cls']} |")
    A("")
    A("## Component B confirmatory holdout (wave-1 T-cell, post-primary only)")
    A("")
    if any(r["cls"] != "MISSING" for r in rows_b):
        k_b  = sum(r["detected"] for r in rows_b)
        lo_b, hi_b = wilson_ci(k_b, len(rows_b))
        A(f"| pool | n | k | rate | CI |")
        A(f"|---|---|---|---|---|")
        A(f"| B (wave-1 T-cell) | {len(rows_b)} | {k_b} | {k_b/len(rows_b):.4f} | [{lo_b:.4f}, {hi_b:.4f}] |")
        A("")
        for r in rows_b:
            A(f"| {r['id']} | {r['slug']} | {r['cls']} |")
    else:
        A("*(Component B scores not yet loaded — examine after primary result committed)*")
    A("")
    A("## Protocol compliance")
    A("- compute_moderators_exp101.py run before any ownership score review.")
    A("- T-cell threshold fixed: M1 > 0.858675 AND M2 < 7.702891 (commit 4e809c8).")
    A("- Component A sourced from AGGREGATE_exp004.md (commit 659bb06), not re-scored.")
    A("- Component B excluded from primary test (incorporation bias prevention).")
    A("- Forbidden interpretations: post_hoc_threshold_shift, component_b_in_primary,")
    A("  non_tcell_inflation, per_repo_outcome_report.")

    AGG_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {AGG_OUT}")
    print(f"\nPrimary outcome: {primary}")
    print(f"  Combined A+C_T: {k_comb}/{n_comb} = {k_comb/n_comb:.3f}  CI [{lo:.3f},{hi:.3f}]  {outcome}")
    print(f"  A only:         {k_a}/{len(rows_a)} = {k_a/len(rows_a):.3f}")
    if rows_c_t:
        print(f"  C_T only:       {k_ct}/{len(rows_c_t)} = {k_ct/len(rows_c_t):.3f}")
    print(f"  C non-T (scored but excluded from primary): {len(rows_c_all) - len(rows_c_t)}")


if __name__ == "__main__":
    main()
