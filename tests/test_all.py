# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.environ["SOURCE_DATE_EPOCH"] = "0"
import random
from witness_core import (Artifact, WitnessViolation, Provenance,
                          ExperimentRegistry, RegistryViolation)
from mcl_runtime import (q_tau, vi, project, refines, merge_heights, perturb,
                         analyze, detect_divergence, triage_content,
                         analyze_trajectory, ForbiddenTransformation)

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond))); print(("PASS " if cond else "FAIL ") + name)

# --- Layer 0: witness_core ---
P = Provenance.capture()
A = lambda d: Artifact(d, P, "observer_agreement_only",
                       {"certifies": "x"}, ["y"])
check("L0.artifact_roundtrip", A({"k": 1}).verify_chain())
try: A({"valid": True}); check("L0.verdict_firewall", False)
except WitnessViolation: check("L0.verdict_firewall", True)
try: A({"nested": [{"healthy": 1}]}); check("L0.verdict_firewall_nested", False)
except WitnessViolation: check("L0.verdict_firewall_nested", True)
a = A({"k": 1}); a["data"]["k"] = 2
check("L0.tamper_detected", not a.verify_chain())
reg = ExperimentRegistry("/tmp/reg_test.json")
try:
    reg.register("X", hypothesis="h", success_condition="s",
                 failure_condition="", interpretation_limits="l")
    check("L0.registry_requires_failure_condition", False)
except RegistryViolation: check("L0.registry_requires_failure_condition", True)

# --- Layer 1: kernel properties (random spaces) ---
ok = True
for t in range(30):
    rng = random.Random(t)
    sig = {f"x{i}": [rng.uniform(0, 1) for _ in range(5)]
           for i in range(rng.randint(4, 12))}
    t1, t2 = sorted((rng.uniform(0.1, 1.2), rng.uniform(0.1, 1.2)))
    P1, P2 = q_tau(sig, set(sig), t1), q_tau(sig, set(sig), t2)
    V = set(rng.sample(sorted(sig), max(2, len(sig)//2)))
    ok &= (vi(P1, P1) == 0.0 and refines(P1, P2)
           and refines(q_tau(sig, V, t1), project(P1, V))
           and merge_heights(sig) == sorted(merge_heights(sig)))
check("L1.kernel_properties(30)", ok)
check("L1.perturb_seeded", perturb(sig, .01, 7) == perturb(sig, .01, 7))

# --- Layer 1: runtime contract ---
corp = {f"e{i}": [i*0.1, 0.0, 1.0] for i in range(8)}
r = analyze(corp, encoders=("native", "spatial"))
check("L1.artifact_output", isinstance(r, Artifact) and r.verify_chain())
check("L1.scope_fields", r["validity_scope"]["certifies"]
      == "structural_admissibility_only"
      and "single_family_run" in r["validity_scope"])
try: analyze(corp, encoders=("nope",)); check("L1.F1", False)
except ForbiddenTransformation: check("L1.F1", True)
try:
    analyze(corp, encoders=("native", "spatial"), tau_policy="fixed:0.25")
    check("L1.F7", False)
except ForbiddenTransformation: check("L1.F7", True)

# --- tools ---
b = {k: list(v) for k, v in corp.items()}; b["e5"][0] += 0.35
d = detect_divergence(corp, b)
check("tools.divergence", d["data"]["diverged"] and isinstance(d, Artifact))
tr = triage_content(corp)
check("tools.triage_scoped", tr["validity_scope"]["outlier_meaning"]
      == "novel_under_declared_geometry_only")
frames = [corp, b]
check("tools.trajectory", analyze_trajectory(frames)["data"]["drift_ticks"] == [1])

# --- firewall: kernel defined once ---
CANON = re.compile(r"^def (q_tau|vi|project|refines|merge_heights|perturb)\(", re.M)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
dups = []
for sub in ("mcl_runtime", "witness_core"):
    for f in os.listdir(os.path.join(root, sub)):
        if f.endswith(".py") and f != "kernel.py":
            if CANON.search(open(os.path.join(root, sub, f)).read()):
                dups.append(f"{sub}/{f}")
check("firewall.single_kernel", dups == [])

# --- determinism ---
check("determinism", analyze(corp, encoders=("native", "spatial"))
      == analyze(corp, encoders=("native", "spatial")))

n = sum(1 for _, k in PASS if not k)
print(f"\n{len(PASS)-n}/{len(PASS)} passed")
sys.exit(1 if n else 0)
