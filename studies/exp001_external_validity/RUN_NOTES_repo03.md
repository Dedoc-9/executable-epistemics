# Run Notes — Repository 3 of 20: pallets/flask

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: a2b6fa8b31ce1c62 · E-006 filter = 7
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.018474 | 0.128119 | 0.220729 | NOT_DETECTED |
| ast_metrics | 0.206334 | 0.263676 | 0.220729 | NOT_DETECTED |
| ownership | 0.263676 | 0.263196 | 0.220729 | DETECTED |

## Scrutiny items
- ownership DETECTED by razor-thin margin (0.000480): classification mechanically valid; margin recorded without interpretation.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 3/20 scored. Erratum budget: 1 of 3 used.
