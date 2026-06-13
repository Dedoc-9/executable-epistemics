# Run Notes — R004 of 50: piccolo-orm/piccolo

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 39379fef0f7014ec · E-006 filter = 11
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.61861 | 0.619081 | 0.544641 | (not tested EXP-002) |
| ast_metrics | 0.545583 | 0.619081 | 0.544641 | (not tested EXP-002) |
| ownership   | 0.619081 | 0.619081 | 0.544641 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.619081): giant-block discreteness. Not an erratum.
- dep_graph capture=0.61861 just below null_p95=0.619081 (margin −0.000471): near-threshold but NOT_DETECTED for dep_graph. Irrelevant to EXP-002 aggregate.
- activity baseline elevated (0.544641): co-change structure is activity-dense; ownership partition at null_p95 ceiling.
- Wall time 1:20.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
