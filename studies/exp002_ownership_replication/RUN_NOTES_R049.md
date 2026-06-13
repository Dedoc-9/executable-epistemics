# Run Notes — R049 of 50: Pylons/colander

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 7c71fbd027ff2705 · Score chain: e2173a672f63e599 · E-006 filter = 4
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=846 · n_commits_dropped_as_bulk=37 · n_files=87 · n_cochange_pairs=64

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.000000 | 0.000000 | 0.042899 | (not tested EXP-002) |
| ast_metrics | 0.045858 | 0.285503 | 0.042899 | (not tested EXP-002) |
| ownership   | 0.000000 | 0.239645 | 0.042899 | NOT_DETECTED |

## Scrutiny items
- Ownership capture=0.0 and dep_graph capture=0.0, dep_graph p95=0.0 (empty import graph). Small sparse repo: 87 files, 64 cochange pairs.
- ast_metrics cap (0.045858) slightly above activity (0.042899) but far below null_p95 (0.285503).
- Wall time 0:02.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
