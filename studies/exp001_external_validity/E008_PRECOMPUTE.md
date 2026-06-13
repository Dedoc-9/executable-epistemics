# E-008 Aggregate Pre-computation — status after 19/20 repos

**Claim class**: operational forecast only. E-008 verdict cannot be issued until
all 20 repos are scored. This file records pre-computed Wilson bounds to certify
that the aggregate outcome is ALREADY DETERMINED for dep_graph and ast_metrics.

## Formula
E-008 rule (frozen):
- VALIDATED   if point ≥ 0.60
- REJECTED    if Wilson_upper(k, n=20, z=1.96) < 0.60
- INCONCLUSIVE otherwise

## Counts at n=19 (pip not yet scored)

| family | DETECTED | UNRESOLVED | NOT_DETECTED |
|---|---|---|---|
| dep_graph   | 1  | 0 | 18 |
| ast_metrics | 0  | 0 | 19 |
| ownership   | 10 | 2 | 7  |

## Wilson bounds (denominator always 20)

| family | k_min | k_max | point_min | point_max | Wilson_upper_max | verdict |
|---|---|---|---|---|---|---|
| dep_graph   | 1 | 2 | 0.050 | 0.100 | 0.301 | **REJECTED** (determined) |
| ast_metrics | 0 | 1 | 0.000 | 0.050 | 0.236 | **REJECTED** (determined) |
| ownership   | 10| 11| 0.500 | 0.550 | 0.742 | INCONCLUSIVE (pip cannot change) |

Notes:
- dep_graph: Wilson_upper max = 0.301 < 0.60 even if pip = DETECTED. Verdict locked.
- ast_metrics: Wilson_upper max = 0.236 < 0.60 even if pip = DETECTED. Verdict locked.
- ownership: point = 0.50 or 0.55; Wilson_upper = 0.701 or 0.742 > 0.60; Wilson_lower
  = 0.299 or 0.342 < 0.60. Cannot reach VALIDATED (would need ≥12 DETECTED = impossible).
  Cannot reach REJECTED (Wilson_upper > 0.60 regardless). INCONCLUSIVE is locked.

## Operational consequence (UPDATE_COMMITMENTS §B)
§B rows for dep_graph and ast_metrics: "Wilson_upper < 0.60 → REJECTED → publish
null result; note detection rate and Wilson CI". These rows are now pre-triggered.
Ownership §B row: "INCONCLUSIVE → report point + CI, note power limitations".

## Pip still required
Pip (repo 20) must still be scored:
  (a) completion definition §E requires 20 valid scorings
  (b) E-013 erratum (vendored-tree decision) must precede pip's run
  (c) final ownership k (10 or 11) determines reported CI
  (d) secondary_corr.py requires all 20 rows

## E-013 decision pending
Options recorded in ERRATA.json once operator chooses:
  A: include _vendor/ (score as-is)
  B: --exclude-glob "src/pip/_vendor/*" (exclude vendored tree)
Both options produce valid data; choice must be recorded BEFORE pip scores.
