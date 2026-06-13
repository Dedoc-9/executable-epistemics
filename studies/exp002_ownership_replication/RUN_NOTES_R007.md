# Run Notes — R007 of 50: redis/redis-py

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 74dff3d23fc48125 · E-006 filter = 9
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.06842 | 0.31702 | 0.58729 | (not tested EXP-002) |
| ast_metrics | 0.58729 | 0.653762 | 0.58729 | (not tested EXP-002) |
| ownership   | 0.653762 | 0.653762 | 0.58729 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.653762): giant-block discreteness. Not an erratum.
- activity baseline very high (0.58729): ownership is at ceiling of null distribution, but activity is also high; the ownership partition is not differentiating beyond the activity baseline at null_p95.
- dep_graph capture very low (0.06842 vs null_p95=0.31702): structural connectivity not driving co-change.
- Wall time 1:18.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
