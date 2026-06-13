# Run Notes — R010 of 50: marshmallow-code/marshmallow

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 3636cec582c52e68 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.344411 | 0.355488 | 0.178499 | (not tested EXP-002) |
| ast_metrics | 0.156093 | 0.355488 | 0.178499 | (not tested EXP-002) |
| ownership   | 0.355488 | 0.355488 | 0.178499 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.355488): giant-block discreteness. Not an erratum.
- dep_graph capture=0.344411 below null_p95=0.355488 (margin −0.011077): NOT_DETECTED for dep_graph as well. Not relevant to EXP-002.
- Wall time 0:09.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
