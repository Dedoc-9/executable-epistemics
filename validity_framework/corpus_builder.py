# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""
P1-A: Ground-truth construction (co-change coupling from git history).

SEQUENCING CONSTRAINT (protocol-binding): this module contains NOTHING
geometric, spectral, quotient-related, or predictive. It emits a witnessed
historical observation, frozen before any encoder exists. The thing being
predicted is established before the mechanism attempting to predict it.

Outputs (inside one witness Artifact):
    cochange_matrix     {file_a||file_b: weight} over the observation window
    commit_graph        per-commit file lists (hashed ids)
    file_index          stable file id table
    observation_window  declared time bounds + commit count
    exclusion_rules     applied filters, declared not implied
    ground_truth_frozen True + freeze hash

Usage:
    python corpus_builder.py --repo /path/to/repo --output gt.json
        [--max-commit-files 20] [--exclude-glob "vendor/*" ...]
"""
import argparse, json, os, subprocess, sys, fnmatch

_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, _ROOT)
from witness_core import Artifact, Provenance

CLAIM = "historical_cochange_observation_only"
FORBIDDEN = ["predictive_validity", "causal_coupling", "design_quality",
             "geometry_alignment", "future_cochange_inference"]


def git_log(repo):
    """Deterministic commit -> changed-files extraction (oldest first).
    P1-B policy: rename chains followed (-M50); every historical path is
    resolved to its terminal name so coupling survives mass renames."""
    out = subprocess.run(
        ["git", "-C", repo, "log", "--reverse", "--name-status", "-M50",
         "--no-merges", "--pretty=format:@@%H|%at"],
        capture_output=True, text=True, check=True).stdout
    commits, renames = [], {}          # renames: old -> new (chain links)
    for block in out.split("@@"):
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        sha, ts = lines[0].split("|")
        files = set()
        for l in lines[1:]:
            parts = l.strip().split("\t")
            if len(parts) == 2 and parts[0] and parts[0][0] in "AMDT":
                files.add(parts[1])
            elif len(parts) == 3 and parts[0].startswith(("R", "C")):
                old_p, new_p = parts[1], parts[2]
                if parts[0].startswith("R"):
                    renames[old_p] = new_p
                files.add(new_p)
        commits.append({"sha": sha, "timestamp": int(ts),
                        "files": sorted(files)})

    def terminal(p, _guard=0):
        seen = set()
        while p in renames and p not in seen:
            seen.add(p)
            p = renames[p]
        return p

    for c in commits:
        c["files"] = sorted({terminal(f) for f in c["files"]})
    return commits


def build(repo, max_commit_files=20, exclude_globs=(), min_cochange=1,
          window_months=None):
    commits = git_log(repo)
    if window_months:                       # P1-B preregistered secondary analysis
        newest = max(c["timestamp"] for c in commits)
        cutoff = newest - window_months * 30 * 86400
        commits = [c for c in commits if c["timestamp"] >= cutoff]
    exclusions = {"max_commit_files": max_commit_files,
                  "exclude_globs": sorted(exclude_globs),
                  "min_cochange": min_cochange,
                  "window_months": window_months,
                  "merges_excluded": True,
                  "rename_handling": "follow_rename_chains_M50_terminal_name"}

    def keep(f):
        return not any(fnmatch.fnmatch(f, g) for g in exclude_globs)

    graph, dropped_large = [], 0
    for c in commits:
        files = [f for f in c["files"] if keep(f)]
        if len(files) > max_commit_files:      # bulk commits are not coupling signal
            dropped_large += 1
            continue
        if len(files) >= 1:
            graph.append({"sha": c["sha"], "timestamp": c["timestamp"],
                          "files": files})

    all_files = sorted({f for c in graph for f in c["files"]})
    file_index = {f: i for i, f in enumerate(all_files)}
    matrix = {}
    for c in graph:
        fs = c["files"]
        for i, a in enumerate(fs):
            for b in fs[i + 1:]:
                key = "||".join(sorted((a, b)))
                matrix[key] = matrix.get(key, 0) + 1
    matrix = {k: v for k, v in matrix.items() if v >= min_cochange}

    window = {"first_commit_ts": graph[0]["timestamp"] if graph else None,
              "last_commit_ts": graph[-1]["timestamp"] if graph else None,
              "n_commits_used": len(graph),
              "n_commits_dropped_as_bulk": dropped_large,
              "n_files": len(all_files), "n_cochange_pairs": len(matrix)}

    data = {"cochange_matrix": matrix,
            "commit_graph": graph,
            "file_index": file_index,
            "observation_window": window,
            "exclusion_rules": exclusions,
            "ground_truth_frozen": True}
    art = Artifact(
        data=data,
        provenance=Provenance.capture(
            code_files=[os.path.abspath(__file__)],
            extra={"repo_head": subprocess.run(
                ["git", "-C", repo, "rev-parse", "HEAD"],
                capture_output=True, text=True).stdout.strip()}),
        claim_class=CLAIM,
        validity_scope={
            "certifies": "historical co-change counts under declared exclusions",
            "measured_window_only": True,
            "does_not_certify": ["future coupling", "causal relationships",
                                 "module quality", "any geometric structure"]},
        forbidden_interpretations=FORBIDDEN)
    return art


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-commit-files", type=int, default=20)
    ap.add_argument("--exclude-glob", action="append", default=[])
    a = ap.parse_args()
    art = build(a.repo, a.max_commit_files, a.exclude_glob)
    with open(a.output, "w") as fh:
        json.dump(art, fh, indent=2, sort_keys=True)
    w = art["data"]["observation_window"]
    print(f"[P1-A] frozen ground truth: {w['n_files']} files, "
          f"{w['n_commits_used']} commits, {w['n_cochange_pairs']} pairs, "
          f"chain={art['chain_hash']}")
