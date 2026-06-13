# Run Notes — R017 of 50: pallets/werkzeug

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 7661bc9e6eca8810 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.312263 | 0.313745 | 0.205761 | (not tested EXP-002) |
| ast_metrics | 0.304856 | 0.313745 | 0.205761 | (not tested EXP-002) |
| ownership   | 0.313416 | 0.313086 | 0.205761 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.000330 (0.313416−0.313086). Razor-thin; classification stands per §A.
- dep_graph capture=0.312263 just below null_p95=0.313745 (gap 0.001482): near-threshold but NOT_DETECTED. Not relevant to EXP-002.
- Wall time 0:34.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
