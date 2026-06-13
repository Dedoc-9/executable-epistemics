# Run Notes — R025 of 50: Bogdanp/dramatiq

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 6aff4cf68478b410 · E-006 filter = 7
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.476868 | 0.487544 | 0.160142 | (not tested EXP-002) |
| ast_metrics | 0.326512 | 0.487544 | 0.160142 | (not tested EXP-002) |
| ownership   | 0.487544 | 0.487544 | 0.160142 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.487544): giant-block discreteness. Not an erratum.
- dep_graph capture=0.476868 close to null_p95=0.487544 (gap 0.010676): near-threshold for dep_graph; irrelevant to EXP-002.
- Wall time 0:21.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
