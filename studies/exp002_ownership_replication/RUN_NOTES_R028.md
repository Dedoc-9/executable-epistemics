# Run Notes — R028 of 50: agronholm/apscheduler

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 275c17668d9a42a8 · E-006 filter = 11
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.019906 | 0.086812 | 0.155654 | (not tested EXP-002) |
| ast_metrics | 0.235001 | 0.332596 | 0.155654 | (not tested EXP-002) |
| ownership   | 0.332596 | 0.332596 | 0.155654 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.332596): giant-block discreteness. Not an erratum.
- dep_graph very low (0.019906 vs null_p95=0.086812): structural coupling not driving co-change.
- Wall time 0:13.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
