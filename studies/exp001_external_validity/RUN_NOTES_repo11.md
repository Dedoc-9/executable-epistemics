# Run Notes — Repository 11 of 20: sqlalchemy/sqlalchemy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: 7504c00bab2d0feb · E-006 filter = 12
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.029884 | 0.143179 | 0.543028 | NOT_DETECTED |
| ast_metrics | 0.543028 | 0.583197 | 0.543028 | NOT_DETECTED |
| ownership | 0.583197 | 0.582458 | 0.543028 | DETECTED |

## Scrutiny items
- ownership DETECTED by razor-thin margin (0.000739): classification mechanically valid; margin recorded without interpretation.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 11/20 scored. Erratum budget: 1 of 3 used.
