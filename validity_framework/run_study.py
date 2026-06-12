# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""EXP-001 per-repository runner (Python repositories, wave 1).
Mechanical end-to-end: E-006 formula filter -> ground truth -> families ->
E-004/E-007 scoring -> witnessed artifacts. No discretionary choices remain.

Usage: python run_study.py --repo /path/to/python/repo --outdir results/
"""
import argparse, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from corpus_builder import build
from encoders import FAMILIES
from scorer import score_family_v2, formula_filter
from mcl_runtime import analyze, register_encoder

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--exclude-glob", action="append", default=[])
    ap.add_argument("--calibration", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    mcf = formula_filter(a.repo)                       # E-006: mechanical
    gt = build(a.repo, max_commit_files=mcf, exclude_globs=a.exclude_glob,
               min_cochange=2)                         # P1-B threshold
    json.dump(gt, open(os.path.join(a.outdir, "ground_truth.json"), "w"),
              indent=2, sort_keys=True)
    print(f"[runner] E-006 filter={mcf}; ground truth chain={gt['chain_hash']}")
    for fam, builder_fn in sorted(FAMILIES.items()):
        sig = builder_fn(a.repo)
        if len(sig) < 4:
            print(f"[runner] {fam}: <4 files, skipped"); continue
        register_encoder(fam, lambda native, raw, s=sig: s)
        r = analyze(sig, encoders=(fam,))
        P = r["data"]["partition_family"][fam]
        s = score_family_v2(P, gt, a.repo, calibration=a.calibration)
        json.dump(s, open(os.path.join(a.outdir, f"score_{fam}.json"), "w"),
                  indent=2, sort_keys=True)
        d = s["data"]
        print(f"[runner] {fam:<12} capture={d['observed_capture']} "
              f"null_p95={d['null_p95']} activity={d['activity_baseline_capture']} "
              f"-> {d['classification']}")
    print("[runner] per-repo artifacts written. REMINDER (E-005): per-repo "
          "classifications are intermediate data; only the >=60%-of-repos "
          "aggregate is a reportable result.")

if __name__ == "__main__":
    main()
