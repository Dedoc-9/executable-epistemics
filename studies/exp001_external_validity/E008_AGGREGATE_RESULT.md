# E-008 Aggregate Result — EXP-001 Wave 1

**Claim class**: `exp001_aggregate_result`
**Status**: COMPLETE (20/20 repos scored, 0 substitutions, 1/3 instrument errata used)
**Date**: 2026-06-12

## E-008 Rule (frozen pre-campaign)
VALIDATED if point ≥ 0.60. REJECTED if Wilson_upper(k,n=20,z=1.96) < 0.60.
INCONCLUSIVE otherwise. EXP-001 positive iff any family VALIDATED.

## Per-family counts (denominator = 20, per §E)

| family | DETECTED | UNRESOLVED | LEAKAGE | NOT_DETECTED |
|---|---|---|---|---|
| dep_graph   |  1 | 0 | 0 | 19 |
| ast_metrics |  0 | 0 | 0 | 20 |
| ownership   | 10 | 2 | 1 |  7 |

DETECTED repo by family:
- dep_graph: scikit-learn/scikit-learn only
- ast_metrics: (none)
- ownership: flask, pytest, Pillow, sphinx, sqlalchemy, mypy, matplotlib, numpy, scipy, pandas

## E-008 Verdicts

| family | k/20 | point | Wilson lower | Wilson upper | verdict |
|---|---|---|---|---|---|
| dep_graph   |  1/20 | 0.050 | 0.009 | 0.236 | **REJECTED** |
| ast_metrics |  0/20 | 0.000 | 0.000 | 0.161 | **REJECTED** |
| ownership   | 10/20 | 0.500 | 0.299 | 0.701 | **INCONCLUSIVE** |

**EXP-001 overall: NEGATIVE** (no family VALIDATED; success condition not met).

## Interpretation limits (per REPO_DECLARATION forbidden_interpretations)
- post_hoc_repo_exclusion: forbidden
- cherry_picked_subsets: forbidden
- Per E-005: the per-repo classifications above are INTERMEDIATE DATA used
  solely to compute the aggregate; they are not individually reportable results.

## Validity scope
- Certifies: the E-008 aggregate outcome for the frozen 20-repo wave-1 population
- Does not certify: generality to arbitrary Python repositories, causal claims,
  design-quality claims, or any claim outside the registered success condition

## Publication consequence (UPDATE_COMMITMENTS §B)
- dep_graph, ast_metrics REJECTED: publish null result. Report detection rate and
  Wilson CI. dep_graph: 1/20 [0.009, 0.236]; ast_metrics: 0/20 [0.000, 0.161].
- ownership INCONCLUSIVE: report point 10/20 = 0.50, Wilson [0.299, 0.701].
  Note power limitation: at n=20, a 60%-true instrument has P(k≥12)≈0.26; INCONCLUSIVE
  was the median expected outcome even under the most optimistic plausible model.
  Recommended next step (not preregistered): wave-2 study, ownership only, n≥50,
  new preregistration required before execution.
- No theoretical update is licensed by this result (E-009 lesson).

## Notable campaign observations (recorded without interpretation per E-005)
- Giant-block discreteness: appeared in repos 1,2,4,6,8,10,11,19,20 as cap==p95
  ties; consequence of single-linkage collapse at small n or high connectivity.
- LEAKAGE: 1 instance (pip/ownership). First and only LEAKAGE in campaign.
- UNRESOLVED_ACTIVITY_MARGIN: 2 instances (celery, django). Both ownership.
- Scikit-learn dep_graph: sole dep_graph DETECTED; ownership capture=0.0 (fine-grained
  partition, null_p95 near-zero — both consistent, not contradictory).
- Razor-thin DETECTED margins: flask (0.000480), pytest (0.001428), scipy (0.000183),
  numpy (0.001389), sqlalchemy (0.000739). Mechanically valid; no interpretation.
