# Run Notes — R015 of 50: falconry/falcon

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: e7c86ef089a8ce08 · E-006 filter = 15
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.108289 | 0.285475 | 0.386768 | (not tested EXP-002) |
| ast_metrics | 0.381293 | 0.50251 | 0.386768 | (not tested EXP-002) |
| ownership   | 0.502814 | 0.502205 | 0.386768 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.000609 (0.502814−0.502205). Razor-thin; classification stands per §A.
- activity baseline (0.386768) well below ownership capture (0.502814): E-003 channel not implicated.
- Wall time 1:01.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
