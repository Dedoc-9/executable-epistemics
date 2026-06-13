# Run Notes — R034 of 50: pre-commit/pre-commit

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: d1bfc465c1a5d5f4 · Score chain: 5808d626164a83c2 · E-006 filter = 10
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=1690 · n_commits_dropped_as_bulk=81 · n_files=346 · n_cochange_pairs=931

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.598272 | 0.601235 | 0.368889 | (not tested EXP-002) |
| ast_metrics | 0.464444 | 0.603457 | 0.368889 | (not tested EXP-002) |
| ownership   | 0.603457 | 0.595556 | 0.368889 | DETECTED |

E-007 check (ownership): cap − null_p95 = 0.007901. e007_margin=(cap−activity)=0.234568 > e007_yardstick=(p95−median)=0.034321. Both conditions satisfied → DETECTED.

## Scrutiny items
- Strong E-007 margin: excess over activity (0.234568) >> null spread (0.034321). DETECTED classification is unambiguous.
- dep_graph (non-classified) just below null: cap=0.598272 vs null_p95=0.601235, gap=0.002963. Very close but below threshold; not a DETECTED result and not classified in EXP-002.
- ast_metrics cap well below null_p95 (0.464444 vs 0.603457).
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
