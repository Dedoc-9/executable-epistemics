# Run Notes — R042 of 50: spulec/freezegun

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: e3b26868c4df1fd3 · Score chain: fe737cace4ce384e · E-006 filter = 4
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=473 · n_commits_dropped_as_bulk=18 · n_files=40 · n_cochange_pairs=52

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.035599 | 0.563107 | 0.158576 | (not tested EXP-002) |
| ast_metrics | 0.158576 | 0.569579 | 0.158576 | (not tested EXP-002) |
| ownership   | 0.569579 | 0.569579 | 0.158576 | NOT_DETECTED |

## Scrutiny items
- Ownership giant-block: cap==null_p95=0.569579. Single-linkage collapse; exceeds_null_p95=false → NOT_DETECTED. Activity=0.158576 (cap >> activity but cap==p95 gate not passed). e007_margin=0.411003 is large but irrelevant — null_p95 condition not met.
- Very small repo: 40 files, 52 cochange pairs. dep_graph far below null (0.035599 vs 0.563107).
- Wall time 0:04.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
