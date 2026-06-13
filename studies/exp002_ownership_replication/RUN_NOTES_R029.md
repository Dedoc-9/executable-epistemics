# Run Notes — R029 of 50: PyCQA/isort

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: fd5859adbf36c446 · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.022399 | 0.286048 | 0.251517 | (not tested EXP-002) |
| ast_metrics | 0.251517 | 0.363509 | 0.251517 | (not tested EXP-002) |
| ownership   | 0.362576 | 0.363509 | 0.251517 | NOT_DETECTED |

## Scrutiny items
- ownership capture=0.362576 genuinely below null_p95=0.363509 (gap 0.000933): NOT_DETECTED is not giant-block but margin is very thin. Ownership is close to null threshold without exceeding it.
- dep_graph very low (0.022399 vs null_p95=0.286048): structural family has negligible signal.
- Wall time 0:23.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
