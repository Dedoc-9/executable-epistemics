# Run Notes — R016 of 50: aio-libs/aiohttp

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 781fba7c93af5d9b · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.030956 | 0.130928 | 0.181738 | (not tested EXP-002) |
| ast_metrics | 0.202568 | 0.235018 | 0.181738 | (not tested EXP-002) |
| ownership   | 0.23517 | 0.235018 | 0.181738 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.000152 (0.23517−0.235018). Thinnest margin in EXP-002 campaign to date. Classification stands per §A (no razor-thin floor defined in protocol).
- activity baseline (0.181738) well below null_p95 (0.235018): E-003 channel not implicated.
- Wall time 1:28.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
