# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""analyze(): observer comparison, emitting witness_core Artifacts."""
import inspect, hashlib, math, os
from witness_core import Artifact, Provenance
from .kernel import (q_tau, vi, merge_heights, barcode_tau, euclidean,
                     KERNEL_VERSION)

HERE = os.path.dirname(os.path.abspath(__file__))
FAMILY_SPEARMAN = 0.6
COINCIDENT_TOL = 1e-9
CLAIM = "observer_agreement_only"
FORBIDDEN = ["semantic_correctness", "legality", "causal_attribution",
             "quality_or_fitness", "encoder_invariant_truth"]


class ForbiddenTransformation(Exception):
    pass


_REGISTRY = {
    "native": lambda native, raw: native,
    "spatial": lambda native, raw: {k: v[:2] for k, v in native.items()},
}


def register_encoder(name, fn):
    _REGISTRY[name] = fn


def _spearman(x, y):
    def rank(v):
        r = [0.0] * len(v)
        for pos, i in enumerate(sorted(range(len(v)), key=lambda i: v[i])):
            r[i] = pos
        return r
    rx, ry = rank(x), rank(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx)
                    * sum((b - my) ** 2 for b in ry))
    return num / den if den else 0.0


def analyze(corpus, encoders=("native",), tau_policy="barcode",
            outputs=("partition_family", "vi_matrix", "consensus")):
    native = dict(corpus)
    for e in encoders:
        if e not in _REGISTRY:
            raise ForbiddenTransformation(f"F1:undeclared_encoder:{e}")
    if tau_policy.startswith("fixed:") and len(encoders) > 1:
        raise ForbiddenTransformation("F7:fixed_tau_multi_encoder")

    names = sorted(encoders)
    sigs, meta, parts = {}, {}, {}
    for e in names:
        s = _REGISTRY[e](native, None)
        if set(s) != set(native):
            raise ForbiddenTransformation(f"F2:encoder_not_total:{e}")
        tau = barcode_tau(s) if tau_policy == "barcode"             else float(tau_policy.split(":")[1])
        sigs[e], parts[e] = s, q_tau(s, set(s), tau)
        try:
            enc_src = inspect.getsource(_REGISTRY[e])
            src_status = "source"
        except (OSError, TypeError):
            enc_src = repr(_REGISTRY[e])          # dynamic encoder: declared, not hidden
            src_status = "source_unavailable_repr_hash"
        meta[e] = {"tau": round(tau, 6),
                   "sizes": [len(b) for b in parts[e]],
                   "source_hash": hashlib.sha256(enc_src.encode()).hexdigest()[:16],
                   "source_hash_basis": src_status}

    ids = sorted(native)
    pairs = [(a, b) for i, a in enumerate(ids) for b in ids[i + 1:]]
    dv = {e: [euclidean(sigs[e][a], sigs[e][b]) for a, b in pairs]
          for e in names}
    fam = {names[0]: 0}
    nxt = 1
    for e in names[1:]:
        for f, fid in list(fam.items()):
            if _spearman(dv[e], dv[f]) >= FAMILY_SPEARMAN:
                fam[e] = fid
                break
        else:
            fam[e] = nxt
            nxt += 1

    data = {"encoders": meta, "families": {e: f"family_{fam[e]}" for e in names}}
    if "partition_family" in outputs:
        data["partition_family"] = {e: parts[e] for e in names}
    if "vi_matrix" in outputs:
        data["vi_matrix"] = [
            {"a": a, "b": b, "vi": round(vi(parts[a], parts[b]), 6),
             "same_family": fam[a] == fam[b]}
            for i, a in enumerate(names) for b in names[i + 1:]]
    if "consensus" in outputs:
        agree = {p: 0 for p in pairs}
        for e in names:
            look = {x: j for j, blk in enumerate(parts[e]) for x in blk}
            for p in pairs:
                if look[p[0]] == look[p[1]]:
                    agree[p] += 1
        C = sorted(list(p) for p, c in agree.items() if c == len(names))
        data["consensus"] = {"C_pairs": C,
                             "U_count": sum(1 for c in agree.values() if c >= 1),
                             "n_pairs": len(pairs)}

    scope = {"certifies": "structural_admissibility_only",
             "geometry_relative": True,
             "single_family_run": len(set(fam.values())) == 1,
             "consensus_meaning": "within_family_only"
             if len(set(fam.values())) == 1 else "cross_family",
             "unmeasured_axes": ["external_validity", "semantic_correctness"]}
    prov = Provenance.capture(
        code_files=[os.path.join(HERE, "kernel.py"),
                    os.path.join(HERE, "runtime.py")],
        seeds={}, extra={"kernel_version": KERNEL_VERSION})
    return Artifact(data=data, provenance=prov, claim_class=CLAIM,
                    validity_scope=scope,
                    forbidden_interpretations=FORBIDDEN)
