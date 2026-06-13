# Run Notes — Repository 8 of 20: celery/celery

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: aec2f07216db8040 · E-006 filter = 9
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.407896 | 0.407896 | 0.395586 | NOT_DETECTED |
| ast_metrics | 0.395586 | 0.407896 | 0.395586 | NOT_DETECTED |
| ownership | 0.407896 | 0.394502 | 0.395586 | UNRESOLVED_ACTIVITY_MARGIN |

## Scrutiny items
- dep_graph capture == own null_p95 (0.407896): discreteness artifact.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 8/20 scored. Erratum budget: 1 of 3 used.
