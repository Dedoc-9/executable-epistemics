# Run Notes — R001 of 50: tortoise/tortoise-orm

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: b866c47c28cd51d3 · E-006 filter = 16
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.318646 | 0.433558 | 0.268553 | (not tested EXP-002) |
| ast_metrics | 0.440863 | 0.457444 | 0.268553 | (not tested EXP-002) |
| ownership   | 0.457444 | 0.456053 | 0.268553 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.001391 (0.457444−0.456053). Razor-thin; classification stands per §A.
- activity baseline well below ownership capture (0.268553 << 0.457444): E-003 channel not implicated.
- Wall time 1:32. Clean.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
