# Run Notes — R014 of 50: sanic-org/sanic

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 098431ad97742602 · E-006 filter = 11
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.216116 | 0.493791 | 0.395509 | (not tested EXP-002) |
| ast_metrics | 0.583884 | 0.583884 | 0.395509 | (not tested EXP-002) |
| ownership   | 0.583884 | 0.583884 | 0.395509 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.583884): giant-block discreteness. Not an erratum.
- ast_metrics cap==null_p95 as well (0.583884): double giant-block across ownership and AST families. Both partition families collapse to the same null ceiling.
- Wall time 1:15.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
