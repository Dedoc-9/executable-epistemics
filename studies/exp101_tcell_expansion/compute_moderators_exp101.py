"""
compute_moderators_exp101.py — EXP-101 Component C moderator computation.

Reads REPO_DECLARATION_exp101.json, runs git log against clones in
tests_epi/exp101/ to compute M₁ (Gini) and M₂ (density) for each repo.

Does NOT read any score_ownership.json — moderator computation is score-blind.

Inputs:
  studies/exp101_tcell_expansion/REPO_DECLARATION_exp101.json
  results_exp101/{repo_name}/ground_truth.json   (written by run_study.py)
  tests_epi/exp101/{repo_name}/                  (git clone)

Output:
  studies/exp101_tcell_expansion/moderators_exp101.json

Execution order (per HYPOTHESIS_exp101.md §7):
  compute_moderators_exp101.py  →  run_batch_exp101.ps1  →  analyze_exp101.py

Run from MCL_OBS2 root:
  python studies\\exp101_tcell_expansion\\compute_moderators_exp101.py

Protocol: script hash must match HYPOTHESIS_exp101.md before execution.
Modify this script only via pre-execution erratum.
"""

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT         = Path(".")
DECL_FILE    = ROOT / "studies/exp101_tcell_expansion/REPO_DECLARATION_exp101.json"
RESULTS_ROOT = ROOT / "results_exp101"
CLONE_ROOT   = Path("C:/Users/dillb_lzxy763/Desktop/tests_epi/exp101")
OUT_FILE     = ROOT / "studies/exp101_tcell_expansion/moderators_exp101.json"

# EXP-003 thresholds — frozen at commit 4e809c8 / moderators_exp003.json
M1_THRESHOLD = 0.858675
M2_THRESHOLD = 7.702891


def gini(counts: list[int]) -> float | None:
    """
    Frozen Gini formula (identical to compute_moderators_exp003.py, commit f3ee2f0):
        (2 * Σ(i+1)*cᵢ) / (n * Σcᵢ) - (n+1)/n   where c sorted ascending
    """
    if not counts or sum(counts) == 0:
        return None
    c = sorted(counts)
    n = len(c)
    numerator   = 2 * sum((i + 1) * v for i, v in enumerate(c))
    denominator = n * sum(c)
    return numerator / denominator - (n + 1) / n


def resolve_clone(slug: str) -> Path | None:
    """Try slug-tail, then full-slug path under CLONE_ROOT."""
    tail = slug.split("/")[1]
    for candidate in [CLONE_ROOT / tail, CLONE_ROOT / slug]:
        if (candidate / ".git").exists():
            return candidate
    return None


def git_author_commit_counts(clone_path: Path, after_ts: int, before_ts: int) -> list[int]:
    """
    Run git log filtered by observation_window; return per-author commit counts.
    Identical filter logic to compute_moderators_exp003.py.
    """
    after_dt  = datetime.fromtimestamp(after_ts,  tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    before_dt = datetime.fromtimestamp(before_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    result = subprocess.run(
        ["git", "-C", str(clone_path), "log",
         f"--after={after_dt}", f"--before={before_dt}",
         "--format=%ae"],
        capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=120
    )
    if result.returncode != 0 or result.stdout is None:
        return []
    return list(Counter(
        e.strip().lower() for e in result.stdout.splitlines() if e.strip()
    ).values())


def main() -> None:
    decl  = json.loads(DECL_FILE.read_text(encoding="utf-8"))
    repos = [r for r in decl["repos"]
             if r["eligibility"] in ("CONFIRMED", "REPLACEMENT")]

    print(f"EXP-101 Component C: {len(repos)} repos declared")
    print(f"M1_threshold={M1_THRESHOLD}  M2_threshold={M2_THRESHOLD}")
    print(f"Clone root: {CLONE_ROOT}\n")

    records      = []
    missing      = []

    for r in repos:
        slug      = r["slug"]
        repo_id   = r["id"]
        repo_name = slug.split("/")[1]

        gt_path = RESULTS_ROOT / repo_name / "ground_truth.json"
        if not gt_path.exists():
            print(f"[SKIP] {repo_id} {slug}: ground_truth.json missing — score first",
                  file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                            "m1_gini": None, "m2_density": None,
                            "note": "ground_truth_missing_score_first"})
            continue

        gt = json.loads(gt_path.read_text(encoding="utf-8"))
        ow = gt["data"]["observation_window"]
        n_commits = ow["n_commits_used"]
        n_files   = ow["n_files"]
        after_ts  = ow["first_commit_ts"]
        before_ts = ow["last_commit_ts"]

        m2 = n_commits / n_files if n_files > 0 else None

        clone = resolve_clone(slug)
        if clone is None:
            missing.append(slug)
            print(f"[SKIP] {repo_id} {slug}: clone not found under {CLONE_ROOT}",
                  file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                            "m1_gini": None,
                            "m2_density": round(m2, 6) if m2 else None,
                            "note": "clone_missing"})
            continue

        counts = git_author_commit_counts(clone, after_ts, before_ts)
        m1 = gini(counts) if counts else None

        t_cell = (m1 is not None and m1 > M1_THRESHOLD and
                  m2 is not None and m2 < M2_THRESHOLD)
        m1_s = f"{m1:.4f}" if m1 is not None else "N/A"
        m2_s = f"{m2:.2f}"  if m2 is not None else "N/A"
        print(f"  {repo_id:6s} {slug:40s}  M1={m1_s}  M2={m2_s}  "
              f"{'T-CELL' if t_cell else 'non-T'}")

        records.append({
            "id":              repo_id,
            "slug":            slug,
            "m1_gini":         round(m1, 6) if m1 is not None else None,
            "m2_density":      round(m2, 6) if m2 is not None else None,
            "n_authors":       len(counts),
            "n_commits_git":   sum(counts),
            "n_commits_gt":    n_commits,
            "n_files":         n_files,
            "note":            r.get("notes", "")
        })

    valid   = [r for r in records if r["m1_gini"] is not None and r["m2_density"] is not None]
    t_cells = [r for r in valid
               if r["m1_gini"] > M1_THRESHOLD and r["m2_density"] < M2_THRESHOLD]

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps({
        "study":        "EXP-101",
        "component":    "C",
        "source":       "studies/exp101_tcell_expansion/REPO_DECLARATION_exp101.json",
        "n_declared":   len(repos),
        "n_computed":   len(valid),
        "n_tcell_c":    len(t_cells),
        "m1_threshold": M1_THRESHOLD,
        "m2_threshold": M2_THRESHOLD,
        "moderators":   records
    }, indent=2), encoding="utf-8")

    print(f"\nWritten: {OUT_FILE}")
    print(f"n_declared={len(repos)}  n_computed={len(valid)}  "
          f"T-cell(C)={len(t_cells)}/{len(valid)}")
    print(f"Component A T-cell: 11 (EXP-004, committed 659bb06)")
    print(f"Combined A+C_T (projected): {11 + len(t_cells)}")
    if missing:
        print(f"Missing clones ({len(missing)}): {missing}", file=sys.stderr)


if __name__ == "__main__":
    main()
