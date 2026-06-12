# SPDX-License-Identifier: AGPL-3.0-or-later
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.environ.setdefault("SOURCE_DATE_EPOCH", "0")
from mcl_runtime import detect_divergence

a = {f"e{i}": [i * 0.1, 0.0, 1.0] for i in range(8)}
b = {k: list(v) for k, v in a.items()}; b["e5"][0] += 0.35
r = detect_divergence(a, b)
print("diverged:", r["data"]["diverged"])
print("claim_class:", r["claim_class"])
print("forbidden:", r["forbidden_interpretations"])
print("chain verified:", r.verify_chain())
