# Run Notes — R037 of 50: urllib3/urllib3

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 0b28488c003fe315 · Score chain: 5021b2b85d7d4d7b · E-006 filter = 7
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=3516 · n_commits_dropped_as_bulk=130 · n_files=397 · n_cochange_pairs=820

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.099529 | 0.237647 | 0.426353 | (not tested EXP-002) |
| ast_metrics | 0.428235 | 0.508706 | 0.426353 | (not tested EXP-002) |
| ownership   | 0.509176 | 0.509176 | 0.426353 | NOT_DETECTED |

## Scrutiny items
- Ownership cap==null_p95=0.509176: giant-block discreteness. cap > activity (0.426353) but cap does not exceed null_p95 → NOT_DETECTED. Not an erratum.
- dep_graph well below null (0.099529 vs 0.237647) and far below activity (0.426353). Import-graph coupling absent relative to cochange history.
- ast_metrics below null_p95 (0.428235 vs 0.508706), close to activity (0.426353).
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
