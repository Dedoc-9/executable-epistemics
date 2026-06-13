"""
compute_moderators_exp102.py -- EXP-102 Component D moderator computation.

Reads REPO_DECLARATION_exp102.json, runs git log against clones in
tests_epi/exp102/ to compute M1 (Gini), M2 (density), and M3 (Galois
closure diameter) for each repo.

M3 is OBSERVATIONAL METADATA ONLY (E-018 precedent). T-cell classification
uses frozen M1^M2 gate only. M3 retrocompute (m3_retroactive.json,
f0be383) falsified M3 as a cohort-level mechanism. M3 recorded for
longitudinal tracking only. No M3 threshold is preregistered for EXP-102.

T-cell definition (frozen EXP-003, commit 4e809c8):
  M1 > 0.858675 AND M2 < 7.702891

Does NOT read any score_ownership.json -- moderator computation is score-blind.

Inputs:
  studies/exp102_tcell_power/REPO_DECLARATION_exp102.json
  results_exp102/{repo_name}/ground_truth.json   (written by run_study.py)
  tests_epi/exp102/{repo_name}/                  (git clone)

Output:
  studies/exp102_tcell_power/moderators_exp102.json

Execution order (per HYPOTHESIS_exp102.md):
  run_batch_exp102.ps1 --> compute_moderators_exp102.py --> analyze_exp102.py

Run from MCL_OBS2 root:
  python studies\\exp102_tcell_power\\compute_moderators_exp102.py

Protocol: script hash must match HYPOTHESIS_exp102.md before execution.
Modify this script only via pre-execution erratum.
"""

import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT         = Path(".")
DECL_FILE    = ROOT / "studies/exp102_tcell_power/REPO_DECLARATION_exp102.json"
RESULTS_ROOT = ROOT / "results_exp102"
CLONE_ROOT   = Path("C:/Users/dillb_lzxy763/Desktop/tests_epi/exp102")
OUT_FILE     = ROOT / "studies/exp102_tcell_power/moderators_exp102.json"

# EXP-003 thresholds -- frozen at commit 4e809c8 / moderators_exp003.json
M1_THRESHOLD = 0.858675
M2_THRESHOLD = 7.702891
# M3 threshold: NOT preregistered for EXP-102 (null finding, m3_retroactive.json f0be383).


def gini(counts):
    """(2 * sum((i+1)*ci) / (n * sum(ci))) - (n+1)/n  where c sorted ascending."""
    if not counts or sum(counts) == 0:
        return None
    c = sorted(counts)
    n = len(c)
    numerator   = 2 * sum((i + 1) * v for i, v in enumerate(c))
    denominator = n * sum(c)
    return numerator / denominator - (n + 1) / n


def resolve_clone(slug):
    """Try slug-tail, then full-slug path under CLONE_ROOT."""
    tail = slug.split("/")[1]
    for candidate in [CLONE_ROOT / tail, CLONE_ROOT / slug]:
        if (candidate / ".git").exists():
            return candidate
    return None


def git_author_commit_counts(clone_path, after_ts, before_ts):
    """Per-author commit counts in observation window."""
    after_dt  = datetime.fromtimestamp(after_ts,  tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    before_dt = datetime.fromtimestamp(before_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", str(clone_path), "log",
         f"--after={after_dt}", f"--before={before_dt}", "--format=%ae"],
        capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=120
    )
    if result.returncode != 0 or result.stdout is None:
        return []
    return list(Counter(
        e.strip().lower() for e in result.stdout.splitlines() if e.strip()
    ).values())


def git_file_author_matrix(clone_path, after_ts, before_ts):
    """
    {author_email: {filepath: commit_count}} for the observation window.
    Single git log pass using --name-only with NUL-prefixed format line.
    """
    after_dt  = datetime.fromtimestamp(after_ts,  tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    before_dt = datetime.fromtimestamp(before_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", str(clone_path), "log",
         f"--after={after_dt}", f"--before={before_dt}",
         "--format=%x00%ae", "--name-only"],
        capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=180
    )
    if result.returncode != 0 or not result.stdout:
        return {}
    matrix = {}
    current_author = None
    for line in result.stdout.splitlines():
        if line.startswith("\x00"):
            current_author = line[1:].strip().lower()
        elif line.strip() and current_author:
            f = line.strip()
            matrix.setdefault(current_author, {})
            matrix[current_author][f] = matrix[current_author].get(f, 0) + 1
    return matrix


def compute_m3(author_file_matrix):
    """
    Galois closure diameter (observational only, no EXP-102 classification effect).

    alpha_maj(a) = files where author a holds >50% of commits.
    gamma(T)     = all authors with any commit in file set T.
    M3 = mean_a( |gamma(alpha_maj(a))| ) / |Authors|

    Low M3: tight exclusive domain.
    High M3: diffuse closure (Pseudo-T by EXP-101 informal definition).

    Authors with no majority-owned files contribute M3=1.0 (conservative).
    NOT used for T-cell classification in EXP-102.
    """
    if not author_file_matrix:
        return None
    authors = list(author_file_matrix.keys())
    N = len(authors)
    if N == 0:
        return None
    if N == 1:
        return round(1.0 / N, 6)

    file_author = {}
    for author, files in author_file_matrix.items():
        for f, c in files.items():
            file_author.setdefault(f, {})[author] = c

    closure_sizes = []
    for a in authors:
        alpha_a = {
            f for f, counts in file_author.items()
            if counts.get(a, 0) / max(sum(counts.values()), 1) > 0.5
        }
        if not alpha_a:
            closure_sizes.append(1.0)
            continue
        gamma_alpha_a = set()
        for f in alpha_a:
            gamma_alpha_a |= set(file_author[f].keys())
        closure_sizes.append(len(gamma_alpha_a) / N)

    return round(sum(closure_sizes) / len(closure_sizes), 6) if closure_sizes else None


def main():
    decl  = json.loads(DECL_FILE.read_text(encoding="utf-8"))
    repos = [r for r in decl["repos"]
             if r["eligibility"] in ("CONFIRMED", "REPLACEMENT")]

    print(f"EXP-102 Component D: {len(repos)} repos declared")
    print(f"M1_threshold={M1_THRESHOLD}  M2_threshold={M2_THRESHOLD}")
    print(f"M3: observational only -- no EXP-102 classification effect")
    print(f"Clone root: {CLONE_ROOT}\n")

    records = []
    missing = []

    for r in repos:
        slug      = r["slug"]
        repo_id   = r["id"]
        repo_name = slug.split("/")[1]

        gt_path = RESULTS_ROOT / repo_name / "ground_truth.json"
        if not gt_path.exists():
            print(f"[SKIP] {repo_id} {slug}: ground_truth.json missing", file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                            "m1_gini": None, "m2_density": None, "m3_galois": None,
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
            print(f"[SKIP] {repo_id} {slug}: clone not found under {CLONE_ROOT}", file=sys.stderr)
            records.append({"id": repo_id, "slug": slug,
                            "m1_gini": None,
                            "m2_density": round(m2, 6) if m2 else None,
                            "m3_galois": None,
                            "note": "clone_missing"})
            continue

        counts = git_author_commit_counts(clone, after_ts, before_ts)
        m1     = gini(counts) if counts else None

        matrix = git_file_author_matrix(clone, after_ts, before_ts)
        m3     = compute_m3(matrix)

        t_cell = (m1 is not None and m1 > M1_THRESHOLD and
                  m2 is not None and m2 < M2_THRESHOLD)

        m1_s = f"{m1:.4f}" if m1 is not None else "N/A"
        m2_s = f"{m2:.2f}"  if m2 is not None else "N/A"
        m3_s = f"{m3:.4f}" if m3 is not None else "N/A"
        label = "T-CELL" if t_cell else "non-T"
        print(f"  {repo_id:6s} {slug:50s}  M1={m1_s}  M2={m2_s}  M3={m3_s}  {label}")

        records.append({
            "id":            repo_id,
            "slug":          slug,
            "m1_gini":       round(m1, 6) if m1 is not None else None,
            "m2_density":    round(m2, 6) if m2 is not None else None,
            "m3_galois":     m3,
            "n_authors":     len(counts),
            "n_commits_git": sum(counts),
            "n_commits_gt":  n_commits,
            "n_files":       n_files,
            "tcell_m1m2":    t_cell,
            "note":          r.get("notes", "")
        })

    valid   = [r for r in records if r["m1_gini"] is not None and r["m2_density"] is not None]
    t_cells = [r for r in valid if r["tcell_m1m2"]]

    m3_vals = [r["m3_galois"] for r in valid if r["m3_galois"] is not None]
    m3_mean = round(sum(m3_vals) / len(m3_vals), 6) if m3_vals else None
    m3_min  = round(min(m3_vals), 6)               if m3_vals else None
    m3_max  = round(max(m3_vals), 6)               if m3_vals else None

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps({
        "study":        "EXP-102",
        "component":    "D",
        "source":       "studies/exp102_tcell_power/REPO_DECLARATION_exp102.json",
        "n_declared":   len(repos),
        "n_computed":   len(valid),
        "n_tcell_d":    len(t_cells),
        "m1_threshold": M1_THRESHOLD,
        "m2_threshold": M2_THRESHOLD,
        "m3_note":      (
            "Observational only. No threshold preregistered for EXP-102. "
            "M3 retrocompute (f0be383) falsified M3 as cohort-level mechanism."
        ),
        "m3_distribution": {
            "mean": m3_mean, "min": m3_min, "max": m3_max, "n": len(m3_vals)
        },
        "moderators":   records
    }, indent=2), encoding="utf-8")

    print(f"\nWritten: {OUT_FILE}")
    print(f"n_declared={len(repos)}  n_computed={len(valid)}  "
          f"T-cell(M1^M2)={len(t_cells)}/{len(valid)}")
    print(f"M3 distribution: mean={m3_mean}  min={m3_min}  max={m3_max}")
    print(f"Target n_T >= 50; current projected: {len(t_cells)}")
    if missing:
        print(f"Missing clones ({len(missing)}): {missing}", file=sys.stderr)


if __name__ == "__main__":
    main()
