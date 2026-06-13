# Run Notes — R003 of 50: ponyorm/pony

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 7cc8a7112127df13 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.517116 | 0.516311 | 0.191301 | (not tested EXP-002) |
| ast_metrics | 0.191301 | 0.517116 | 0.191301 | (not tested EXP-002) |
| ownership   | 0.517116 | 0.517116 | 0.191301 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.517116): giant-block discreteness. Not an erratum.
- dep_graph capture=0.517116 > null_p95=0.516311 (margin 0.000805): would be DETECTED in dep_graph, but dep_graph is not tested in EXP-002. Recorded without interpretation per E-005.
- Wall time 0:36.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
