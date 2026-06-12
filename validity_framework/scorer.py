# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""EXP-001 scorer. Implements EXACTLY the metric frozen in P1B_POLICY.json:
capture = within-block cochange weight / total weight;
null = 1000 size-matched random partitions (seeded); success mapping
= capture > 95th percentile of null. Nothing else is computed."""
import json, os, random, sys

_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, _ROOT)
from witness_core import Artifact, Provenance

NULL_DRAWS = 1000
NULL_SEED = 0


def capture(partition, matrix):
    look = {x: i for i, blk in enumerate(partition) for x in blk}
    total = sum(matrix.values())
    if total == 0:
        return 0.0
    within = sum(w for pair, w in matrix.items()
                 if (lambda a, b: a in look and b in look
                     and look[a] == look[b])(*pair.split("||")))
    return within / total


def null_distribution(partition, matrix, ids):
    sizes = [len(b) for b in partition]
    rng = random.Random(NULL_SEED)
    vals = []
    for _ in range(NULL_DRAWS):
        pool = list(ids)
        rng.shuffle(pool)
        P, at = [], 0
        for s in sizes:
            P.append(pool[at:at + s]); at += s
        vals.append(capture(P, matrix))
    return sorted(vals)


def score_family(partition, ground_truth, calibration=False):
    matrix = ground_truth["data"]["cochange_matrix"]
    ids = sorted({x for blk in partition for x in blk})
    obs = capture(partition, matrix)
    null = null_distribution(partition, matrix, ids)
    p95 = null[int(0.95 * len(null))]
    exceeds = obs > p95
    data = {"observed_capture": round(obs, 6),
            "null_p95": round(p95, 6),
            "null_median": round(null[len(null) // 2], 6),
            "exceeds_null_p95": exceeds,
            "n_null_draws": NULL_DRAWS,
            "ground_truth_chain": ground_truth["chain_hash"]}
    claim = ("pipeline_calibration_only" if calibration
             else "exp001_scored_observation")
    forbidden = ["geometry_truth", "causal_coupling", "design_quality"]
    if calibration:
        forbidden.append("exp001_evidence")
    return Artifact(
        data=data,
        provenance=Provenance.capture(
            code_files=[os.path.abspath(__file__)],
            seeds={"null_seed": NULL_SEED}),
        claim_class=claim,
        validity_scope={
            "certifies": "frozen-metric score vs preregistered null on one repository",
            "single_repository": True,
            "does_not_certify": ["cross-repository generality",
                                 "EXP-001 success (requires >=60% of >=20 repos)"]},
        forbidden_interpretations=forbidden)


def activity_baseline_partition(repo, files):
    """E-004: pair-blind activity partition (change frequency + size).
    BASELINE ONLY — forbidden as a candidate family."""
    import subprocess
    from mcl_runtime.kernel import q_tau, barcode_tau
    sig = {}
    for f in files:
        n = len(subprocess.run(["git", "-C", repo, "log", "--oneline", "--", f],
                               capture_output=True, text=True).stdout.splitlines())
        try:
            size = len(open(os.path.join(repo, f)).read().splitlines())
        except OSError:
            size = 0
        sig[f] = [n / 50.0, size / 200.0]
    return q_tau(sig, set(sig), barcode_tau(sig))


def score_family_v2(partition, ground_truth, repo, calibration=False):
    """E-004 scoring: detection requires exceeding BOTH random null p95
    AND the activity-baseline capture."""
    base = score_family(partition, ground_truth, calibration=calibration)
    files = sorted({x for blk in partition for x in blk})
    act_p = activity_baseline_partition(repo, files)
    act_capture = capture(act_p, ground_truth["data"]["cochange_matrix"])
    d = dict(base["data"])
    d["activity_baseline_capture"] = round(act_capture, 6)
    d["exceeds_activity_baseline"] = d["observed_capture"] > act_capture
    yardstick = d["null_p95"] - d["null_median"]            # E-007 noise band
    margin = d["observed_capture"] - act_capture
    if d["exceeds_null_p95"] and margin > yardstick:
        d["classification"] = "DETECTED"
    elif d["exceeds_null_p95"] and margin <= 0:
        d["classification"] = "LEAKAGE"
    elif d["exceeds_null_p95"]:
        d["classification"] = "UNRESOLVED_ACTIVITY_MARGIN"
    else:
        d["classification"] = "NOT_DETECTED"
    d["e007_yardstick"] = round(yardstick, 6)
    d["e007_margin"] = round(margin, 6)
    return Artifact(data=d, provenance=base["provenance"],
                    claim_class=base["claim_class"],
                    validity_scope={**base["validity_scope"],
                                    "detection_rule": "E-004_dual_baseline"},
                    forbidden_interpretations=base["forbidden_interpretations"])


def formula_filter(repo):
    """E-006: max_commit_files = min(50, ceil(p95 of non-merge commit sizes))."""
    import math, subprocess
    out = subprocess.run(["git", "-C", repo, "log", "--no-merges",
                          "--name-only", "--pretty=format:@@"],
                         capture_output=True, text=True, check=True).stdout
    counts = [len([l for l in b.strip().split("\n") if l.strip()])
              for b in out.split("@@") if b.strip()]
    if not counts:
        return 50
    counts.sort()
    idx = min(len(counts) - 1, math.ceil(0.95 * len(counts)) - 1)  # E-010 nearest-rank
    return min(50, math.ceil(counts[idx]))
