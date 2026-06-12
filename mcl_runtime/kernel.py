# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""THE single truth kernel (self-contained, including the metric).
No other module in this package may define these functions — enforced
by the firewall test. Numeric contract: VI < TOL is exactly 0.0."""
import math
import random

KERNEL_VERSION = "2.0"
TOL = 1e-12


def euclidean(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def q_tau(sig, idset, tau):
    """Single-linkage partition at tau (strict <). Deterministic."""
    ids = sorted(idset)
    parent = {x: x for x in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if euclidean(sig[a], sig[b]) < tau:
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[max(ra, rb)] = min(ra, rb)
    blocks = {}
    for x in ids:
        blocks.setdefault(find(x), []).append(x)
    return sorted((sorted(v) for v in blocks.values()),
                  key=lambda b: (-len(b), b[0]))


def project(P, V):
    V = set(V)
    return sorted((sorted(set(b) & V) for b in P if set(b) & V),
                  key=lambda b: (-len(b), b[0]))


def vi(P, Q):
    n = sum(len(b) for b in P)
    assert n == sum(len(b) for b in Q), "different universes"
    if n == 0:
        return 0.0
    Ps, Qs = [set(b) for b in P], [set(b) for b in Q]
    H = lambda R: -sum(len(b) / n * math.log(len(b) / n) for b in R if b)
    I = sum(len(b & c) / n * math.log(n * len(b & c) / (len(b) * len(c)))
            for b in Ps for c in Qs if b & c)
    v = H(Ps) + H(Qs) - 2 * I
    return 0.0 if v < TOL else v


def refines(P, Q):
    look = {x: i for i, q in enumerate(Q) for x in q}
    return all(len({look[x] for x in p}) == 1 for p in P)


def merge_heights(sig):
    ids = sorted(sig)
    edges = sorted((euclidean(sig[a], sig[b]), a, b)
                   for i, a in enumerate(ids) for b in ids[i + 1:])
    parent = {x: x for x in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    hs = []
    for d, a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)
            hs.append(d)
    return hs


def perturb(sig, eps, seed):
    """Isotropic perturbation; seed REQUIRED."""
    rng = random.Random(seed)
    out = {}
    for k, v in sorted(sig.items()):
        d = [rng.gauss(0, 1) for _ in v]
        n = math.sqrt(sum(c * c for c in d)) or 1.0
        out[k] = [a + eps * c / n for a, c in zip(v, d)]
    return out


def barcode_tau(sig):
    """tau policy: center of the largest merge-height gap."""
    hs = merge_heights(sig)
    if len(hs) < 2:
        return (hs[0] if hs else 1.0) * 0.99
    a, b = max(zip(hs, hs[1:]), key=lambda g: g[1] - g[0])
    return (a + b) / 2
