# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""EXP-001 aggregate conclusion (E-008 rule). Reads per-repo score artifacts,
emits the study's terminal witnessed artifact. Usage:
    python aggregate.py --results-root results/ --output EXP001_CONCLUSION.json
Expects results/<repo_name>/score_<family>.json from run_study.py."""
import argparse, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from witness_core import Artifact, Provenance, ExperimentRegistry

THRESHOLD = 0.60


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-root", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--declared", default=os.path.join(HERE, "..", "studies", "population", "REPO_DECLARATION.json"))
    ap.add_argument("--rehearsal", action="store_true",
                    help="campaign rehearsal: undeclared repos allowed; conclusion "
                         "claim-scoped as rehearsal, NEVER exp001 evidence")
    a = ap.parse_args()
    decl = json.load(open(a.declared))["data"]
    declared = decl["n_declared"]
    declared_names = {r.split("/")[-1].lower() for r in decl["repositories"]}
    per_family = {}
    repo_dirs = sorted(d for d in os.listdir(a.results_root)
                       if os.path.isdir(os.path.join(a.results_root, d)))
    excluded_not_declared = []
    for rd in repo_dirs:
        if not a.rehearsal and rd.lower() not in declared_names:
            excluded_not_declared.append(rd)      # population firewall
            continue
        for f in sorted(os.listdir(os.path.join(a.results_root, rd))):
            if f.startswith("score_"):
                fam = f[len("score_"):-len(".json")]
                s = json.load(open(os.path.join(a.results_root, rd, f)))
                per_family.setdefault(fam, []).append(
                    {"repo": rd, "classification": s["data"]["classification"],
                     "chain": s["chain_hash"]})
    summary = {}
    for fam, rows in sorted(per_family.items()):
        k = sum(1 for r in rows if r["classification"] == "DETECTED")
        n = len(rows)
        lo, hi = wilson(k, n)
        rate = k / n if n else 0.0
        if n < declared:
            outcome = "CAMPAIGN_INCOMPLETE"
        elif rate >= THRESHOLD:
            outcome = "VALIDATED"
        elif hi < THRESHOLD:
            outcome = "REJECTED"
        else:
            outcome = "INCONCLUSIVE"
        summary[fam] = {"detected": k, "scored": n, "declared": declared,
                        "success_rate": round(rate, 4),
                        "wilson_95": [round(lo, 4), round(hi, 4)],
                        "outcome": outcome, "rows": rows}
    if not summary:
        exp001 = "NO_DECLARED_RESULTS"
    else:
        exp001 = None
    exp001 = exp001 or ("POSITIVE" if any(s["outcome"] == "VALIDATED"
                                for s in summary.values())
              else "INCOMPLETE" if any(s["outcome"] == "CAMPAIGN_INCOMPLETE"
                                       for s in summary.values())
              else "NEGATIVE" if all(s["outcome"] == "REJECTED"
                                     for s in summary.values())
              else "INCONCLUSIVE")
    claim = ("campaign_rehearsal_only" if a.rehearsal
             else "exp001_aggregate_conclusion")
    forb = ["geometry_truth", "structure_universality", "per_repo_storytelling"]
    if a.rehearsal:
        forb.append("exp001_evidence")
    art = Artifact(
        data={"per_family": summary, "exp001_outcome": exp001,
              "rehearsal": a.rehearsal,
              "excluded_not_declared": excluded_not_declared,
              "decision_rule": "E-008", "threshold": THRESHOLD},
        provenance=Provenance.capture(code_files=[os.path.abspath(__file__)]),
        claim_class=claim,
        validity_scope={"certifies": "preregistered aggregate over declared population",
                        "does_not_certify": ["generality beyond wave-1 population",
                                             "causal or semantic claims"]},
        forbidden_interpretations=forb)
    json.dump(art, open(a.output, "w"), indent=2, sort_keys=True)
    banner = ("[REHEARSAL — claim_class=campaign_rehearsal_only — "
              "NOT EXP-001 EVIDENCE] " if a.rehearsal else "[EXP-001] ")
    print(f"[aggregate] {banner}outcome: {exp001}")
    for fam, s in summary.items():
        print(f"  {fam:<12} {s['detected']}/{s['scored']} "
              f"rate={s['success_rate']} CI={s['wilson_95']} -> {s['outcome']}")
    print(f"[aggregate] conclusion chain: {art['chain_hash']}")

if __name__ == "__main__":
    main()
