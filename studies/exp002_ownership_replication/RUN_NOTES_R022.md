# Run Notes — R022 of 50: Textualize/rich

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 5610849f732a8e83 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.401364 | 0.543066 | 0.401364 | (not tested EXP-002) |
| ast_metrics | 0.543066 | 0.543066 | 0.401364 | (not tested EXP-002) |
| ownership   | 0.543066 | 0.541298 | 0.401364 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.001768 (0.543066−0.541298). Razor-thin; classification stands per §A.
- ast_metrics cap==null_p95 (0.543066): AST family at giant-block ceiling. dep_graph capture equals activity (0.401364): dep_graph tracks activity baseline exactly, not ownership. The DETECTED ownership signal is above this collapsed floor.
- Wall time 0:44.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
