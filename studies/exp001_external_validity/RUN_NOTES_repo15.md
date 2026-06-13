# Run Notes — Repository 15 of 20: numpy/numpy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: 72f8d3dff4d470a7 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.113149 | 0.137307 | 0.16968 | NOT_DETECTED |
| ast_metrics | 0.184696 | 0.197483 | 0.16968 | NOT_DETECTED |
| ownership | 0.197483 | 0.196094 | 0.16968 | DETECTED |

## Scrutiny items
- ownership DETECTED by razor-thin margin (0.001389): classification mechanically valid; margin recorded without interpretation.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 15/20 scored. Erratum budget: 1 of 3 used.
