"""
compute_moderators_exp003.py — EXP-003 gate: blind moderator computation.

Computes M1 (Gini coefficient of per-author commit counts) and M2 (commit
density = n_commits_used / n_files) for every repo in the EXP-002 declared
population. DOES NOT read any score_ownership.json or classification data.

Run from MCL_OBS2 root:
    python studies/exp003_moderator/compute_moderators_exp003.py

Writes: studies/exp003_moderator/moderators_exp003.json

Protocol note: this script must be committed with its SHA-256 hash recorded
in HYPOTHESIS_exp003.md BEFORE it is executed against real data.
"""

import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (relative to MCL_OBS2 root, which must be cwd)
# ---------------------------------------------------------------------------
ROOT          = Path(".")
DECLARATION   = ROOT / "studies/exp002_ownership_replication/REPO_DECLARATION_exp002.json"
GT_ROOT       = ROOT / "results_exp002"
CLONE_ROOT    = Path(r"C:\Users\dillb_lzxy763\Desktop\tests_epi\exp002")
OUT_FILE      = ROOT / "studies/exp003_moderator/moderators_exp003.json"

# ---------------------------------------------------------------------------
# Gini coefficient (frozen formula, preregistered in HYPOTHESIS_exp003.md)
# Formula: Lorenz area, exact for discrete non-negative distributions.
# Edge case: n=1 → G=0 (single-author repos; flagged in output as n_authors=1).
# ---------------------------------------------------------------------------
def gini(counts: list[int]) -> float:
    c = sorted(counts)
    n = len(c)
    total = sum(c)
    if n == 0 or total == 0:
        return float("nan")
    return (2 * sum((i + 1) * v for i, v in enumerate(c))) / (n * total) - (n + 1) / n


# ---------------------------------------------------------------------------
# Git log authorship count within an observation window
# Uses timestamps from ground_truth.json observation_window to bound the
# query to the same period the instrument operated over.
# Counts non-merge commits only (--no-merges), deduplicated by normalised
# author email (lowercased) to handle capitalisation variants.
# ---------------------------------------------------------------------------
def author_commit_counts(clone_path: Path, ts_first: int, ts_last: int) -> dict[str, int]:
    """Returns {email: commit_count} for non-merge commits in [ts_first, ts_last]."""
    # Convert unix timestamps to ISO strings git understands
    def ts_to_iso(ts: int) -> str:
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    cmd = [
        "git", "-C", str(clone_path),
        "log", "--no-merges",
        "--format=%ae",
        f"--after={ts_to_iso(ts_first - 1)}",   # -1s to include first commit
        f"--before={ts_to_iso(ts_last + 1)}",    # +1s to include last commit
    ]
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
        if result.returncode != 0:
            return {}
        counts: dict[str, int] = {}
        for email in result.stdout.splitlines():
            e = email.strip().lower()
            if e:
                counts[e] = counts.get(e, 0) + 1
        return counts
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    decl = json.loads(DECLARATION.read_text(encoding="utf-8"))
    repos = decl["repos"]

    results = []
    for r in repos:
        repo_id   = r["id"]
        slug      = r["slug"]
        name      = slug.split("/")[1]
        clone_path = CLONE_ROOT / name
        gt_path   = GT_ROOT / name / "ground_truth.json"

        record: dict = {"id": repo_id, "slug": slug}

        # --- M2: read from ground_truth.json (no outcome data accessed) ---
        if not gt_path.exists():
            print(f"[WARN] {repo_id}: ground_truth.json missing — skipping", file=sys.stderr)
            record.update({"m1_gini": None, "m2_density": None,
                           "n_authors": None, "n_commits_git": None,
                           "n_commits_used": None, "n_files": None,
                           "notes": "ground_truth_missing"})
            results.append(record)
            continue

        gt = json.loads(gt_path.read_text(encoding="utf-8"))
        ow = gt["data"]["observation_window"]
        n_commits_used = ow["n_commits_used"]
        n_files        = ow["n_files"]
        ts_first       = ow["first_commit_ts"]
        ts_last        = ow["last_commit_ts"]

        m2 = n_commits_used / n_files if n_files > 0 else float("nan")

        # --- M1: git log author counts ---
        if not clone_path.exists():
            print(f"[WARN] {repo_id}: clone missing at {clone_path}", file=sys.stderr)
            record.update({"m1_gini": None, "m2_density": round(m2, 6),
                           "n_authors": None, "n_commits_git": None,
                           "n_commits_used": n_commits_used, "n_files": n_files,
                           "notes": "clone_missing"})
            results.append(record)
            continue

        author_counts = author_commit_counts(clone_path, ts_first, ts_last)
        n_authors     = len(author_counts)
        n_commits_git = sum(author_counts.values())

        if n_authors == 0:
            m1 = float("nan")
            notes = "no_commits_in_window"
        elif n_authors == 1:
            m1 = 0.0
            notes = "single_author_gini_zero"   # declared edge case; see HYPOTHESIS
        else:
            m1    = round(gini(list(author_counts.values())), 6)
            notes = ""

        record.update({
            "m1_gini":       m1,
            "m2_density":    round(m2, 6),
            "n_authors":     n_authors,
            "n_commits_git": n_commits_git,
            "n_commits_used": n_commits_used,
            "n_files":       n_files,
            "notes":         notes,
        })
        results.append(record)
        status = f"G={m1:.4f}" if isinstance(m1, float) and not math.isnan(m1) else "G=nan"
        print(f"[ok] {repo_id:5s} {slug:40s} {status}  D={m2:.2f}  n_authors={n_authors}")

    OUT_FILE.write_text(
        json.dumps({"study": "EXP-003", "moderators": results}, indent=2),
        encoding="utf-8"
    )
    print(f"\nWritten: {OUT_FILE}  ({len(results)} repos)")


if __name__ == "__main__":
    main()
