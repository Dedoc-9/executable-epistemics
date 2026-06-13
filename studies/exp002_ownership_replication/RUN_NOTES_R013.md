# Run Notes — R013 of 50: encode/starlette

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 767c9bb453b977ee · E-006 filter = 7
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.400481 | 0.534576 | 0.51834 | (not tested EXP-002) |
| ast_metrics | 0.141912 | 0.447986 | 0.51834 | (not tested EXP-002) |
| ownership   | 0.542393 | 0.542393 | 0.51834 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.542393): giant-block discreteness. Not an erratum.
- activity baseline high (0.51834); ownership at null_p95 ceiling, not differentiating beyond activity.
- Wall time 0:15.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
