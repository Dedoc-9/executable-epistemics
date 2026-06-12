# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The three tools, each returning a witness_core Artifact."""
import os
from witness_core import Artifact, Provenance
from .runtime import analyze, CLAIM, FORBIDDEN
from .kernel import vi, q_tau, perturb, barcode_tau

HERE = os.path.dirname(os.path.abspath(__file__))


def _wrap(data, scope, seeds=None):
    return Artifact(
        data=data,
        provenance=Provenance.capture(
            code_files=[os.path.join(HERE, "kernel.py")],
            seeds=seeds or {}),
        claim_class=CLAIM, validity_scope=scope,
        forbidden_interpretations=FORBIDDEN)


def detect_divergence(snapshot_a, snapshot_b, encoders=("native", "spatial")):
    if set(snapshot_a) != set(snapshot_b):
        raise ValueError("universe_mismatch")
    ra = analyze(snapshot_a, encoders=encoders)
    rb = analyze(snapshot_b, encoders=encoders)
    per, implicated = {}, set()
    for e in sorted(encoders):
        v = vi(ra["data"]["partition_family"][e],
               rb["data"]["partition_family"][e])
        per[e] = round(v, 6)
        if v > 0:
            la = {x: i for i, blk in
                  enumerate(ra["data"]["partition_family"][e]) for x in blk}
            lb = {x: i for i, blk in
                  enumerate(rb["data"]["partition_family"][e]) for x in blk}
            implicated |= {x for x in la
                           if {y for y in la if la[y] == la[x]}
                           != {y for y in lb if lb[y] == lb[x]}}
    return _wrap(
        {"diverged": ra["chain_hash"] != rb["chain_hash"],
         "partition_diverged": any(v > 0 for v in per.values()),
         "vi_per_geometry": per, "implicated": sorted(implicated),
         "chain_hashes": [ra["chain_hash"], rb["chain_hash"]]},
        {**ra["validity_scope"],
         "sensitivity": "phase_change_detector_not_error_meter"})


def triage_content(snapshot, encoders=("spatial",), n_directions=30,
                   spectrum_seed=0):
    r = analyze(snapshot, encoders=encoders)
    e = sorted(encoders)[0]
    sig = dict(snapshot) if e == "native" else         {k: v[:2] for k, v in snapshot.items()}
    t = barcode_tau(sig)
    P0 = q_tau(sig, set(sig), t)
    spec = []
    for frac in (0.2, 0.5, 1.0):
        lam = frac * t
        surv = sum(1 for s in range(n_directions)
                   if vi(P0, q_tau(perturb(sig, lam, spectrum_seed + s),
                                   set(sig), t)) == 0.0) / n_directions
        spec.append({"lambda": round(lam, 6), "survival": surv})
    return _wrap(
        {"partition_family": r["data"]["partition_family"],
         "structural_outliers": [b[0] for b in
                                 r["data"]["partition_family"][e]
                                 if len(b) == 1],
         "stability_spectrum": {e: spec}},
        {**r["validity_scope"],
         "outlier_meaning": "novel_under_declared_geometry_only"},
        seeds={"spectrum_seed": spectrum_seed})


def analyze_trajectory(frames, encoders=("native", "spatial")):
    steps, prev = [], None
    for t, frame in enumerate(frames):
        r = analyze(frame, encoders=encoders)
        step = {"t": t, "chain_hash": r["chain_hash"]}
        if prev is not None:
            step["vi_from_prev"] = {
                e: round(vi(prev["data"]["partition_family"][e],
                            r["data"]["partition_family"][e]), 6)
                for e in sorted(encoders)}
        steps.append(step)
        prev = r
    return _wrap(
        {"steps": steps,
         "drift_ticks": [s["t"] for s in steps
                         if any(v > 0 for v in
                                s.get("vi_from_prev", {}).values())]},
        {**prev["validity_scope"],
         "analysis_mode": "post_hoc_only_never_per_action"})
