"""
compute_moderators_exp005.py — EXP-005 wave-1 moderator retrocompute.

Reads EXP-001 wave-1 repo list from studies/population/REPO_DECLARATION.json,
computes M₁ (Gini) and M₂ (density) using the identical formulae as
compute_moderators_exp003.py (commit f3ee2f0, hash 41c66d6).

Does NOT read any score_ownership.json — moderator-blind.

Inputs:
  studies/population/REPO_DECLARATION.json  (wave-1 slugs, n=20)
  results/{repo_name}/ground_truth.json     (observation_window, n_commits_used, n_files)
  tests_epi/{repo_name}/  OR  tests_epi/{org}/{repo}/  (git clone for author emails)

Output:
  studies/exp005_wave1_moderators/moderators_exp005.json

Clone path resolution (in order):
  1. CLONE_ROOT / slug.split('/')[1]   (most repos)
  2. CLONE_ROOT / slug                 (e.g. psf/requests)

Run from MCL_OBS2 root:
  python studies/exp005_wave1_moderators/compute_moderators_exp005.py

Protocol: script hash must match HYPOTHESIS_exp005.md before execution.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT        = Path(".")
DECL_FILE   = ROOT / "studies/population/REPO_DECLARATION.json"
RESULTS_ROOT = ROOT / "results"
CLONE_ROOT  = Path("C:/Users/dillb_lzxy763/Desktop/tests_epi")
OUT_FILE    = ROOT / "studies/exp005_wave1_moderators/moderators_exp005.json"

# EXP-003 thresholds (frozen at commit 4e809c8 / HYPOTHESIS_exp005.md)
M1_THRESHOLD = 0.858675   # M₁ median from moderators_exp003.json
M2_THRESHOLD = 7.702891   # M₂ median from moderators_exp003.json


def gini(counts: list[int]) -> float:
    """
    Frozen formula (identical to compute_moderators_exp003.py, commit f3ee2f0):
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
    """Try slug-tail then full-slug path."""
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
        encoding="utf-8", errors="replace"
    )
    if result.returncode != 0 or result.stdout is None:
        return []

    from collections import Counter
    counts_map = Counter(e.strip().lower() for e in result.stdout.splitlines() if e.strip())
    return list(counts_map.values())


def main() -> None:
    decl = json.loads(DECL_FILE.read_text(encoding="utf-8"))
    slugs = decl["data"]["repositories"]
    n_declared = decl["data"]["n_declared"]
    assert len(slugs) == n_declared, f"slug count mismatch: {len(slugs)} vs {n_declared}"

    records = []
    missing_clones = []

    for slug in slugs:
        repo_name = slug.split("/")[1]
        repo_id   = f"W1_{repo_name}"

        # Ground truth
        gt_path = RESULTS_ROOT / repo_name / "ground_truth.json"
        if not gt_path.exists():
            print(f"[WARN] {slug}: ground_truth.json missing at {gt_path}", file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                             "m1_gini": None, "m2_density": None,
                             "note": "ground_truth_missing"})
            continue

        gt = json.loads(gt_path.read_text(encoding="utf-8"))
        ow = gt["data"]["observation_window"]
        n_commits = ow["n_commits_used"]
        n_files   = ow["n_files"]
        after_ts  = ow["first_commit_ts"]
        before_ts = ow["last_commit_ts"]

        # M₂
        m2 = n_commits / n_files if n_files > 0 else None

        # M₁ — needs clone
        clone = resolve_clone(slug)
        if clone is None:
            missing_clones.append(slug)
            print(f"[WARN] {slug}: clone not found under {CLONE_ROOT}", file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                             "m1_gini": None, "m2_density": round(m2, 6) if m2 else None,
                             "note": "clone_missing"})
            continue

        counts = git_author_commit_counts(clone, after_ts, before_ts)
        m1 = gini(counts) if counts else None

        records.append({
            "id":          repo_id,
            "slug":        slug,
            "m1_gini":     round(m1, 6) if m1 is not None else None,
            "m2_density":  round(m2, 6) if m2 is not None else None,
            "n_authors":   len(counts),
            "n_commits_git": sum(counts),
            "n_commits_gt":  n_commits,
            "n_files":      n_files,
            "note":         ""
        })

        t_cell = (m1 is not None and m1 > M1_THRESHOLD and
                  m2 is not None and m2 < M2_THRESHOLD)
        m1_s = f"{m1:.4f}" if m1 is not None else "N/A"
        m2_s = f"{m2:.2f}" if m2 is not None else "N/A"
        print(f"  {repo_id:30s}  M1={m1_s}  M2={m2_s}  {'T-CELL' if t_cell else 'non-T'}")

    # Compute T-cell count for console summary
    valid = [r for r in records if r["m1_gini"] is not None and r["m2_density"] is not None]
    t_cell_repos = [r for r in valid
                    if r["m1_gini"] > M1_THRESHOLD and r["m2_density"] < M2_THRESHOLD]

    OUT_FILE.write_text(json.dumps({
        "study":      "EXP-005",
        "source":     "studies/population/REPO_DECLARATION.json",
        "n_declared": n_declared,
        "n_computed": len(valid),
        "m1_threshold": M1_THRESHOLD,
        "m2_threshold": M2_THRESHOLD,
        "moderators": records
    }, indent=2), encoding="utf-8")

    print(f"\nWritten: {OUT_FILE}")
    print(f"n_declared={n_declared}  n_computed={len(valid)}  T-cell={len(t_cell_repos)}/{len(valid)}")
    if missing_clones:
        print(f"Missing clones ({len(missing_clones)}): {missing_clones}")


if __name__ == "__main__":
    main()
