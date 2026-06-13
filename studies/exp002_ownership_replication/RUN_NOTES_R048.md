# Run Notes — R048 of 50: elastic/elasticsearch-py

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 0a59205ccaeff5f0 · Score chain: df63c81e3bfcc7f1 · E-006 filter = 21
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1765 · n_commits_dropped_as_bulk=90 · n_files=570 · n_cochange_pairs=1890

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.447109 | 0.603179 | 0.298027 | (not tested EXP-002) |
| ast_metrics | 0.590025 | 0.603179 | 0.298027 | (not tested EXP-002) |
| ownership   | 0.603179 | 0.602220 | 0.298027 | DETECTED |

E-007: e007_margin=(cap−activity)=0.305152 > e007_yardstick=(p95−median)=0.015073 → DETECTED.

## Scrutiny items
- Highest filter in campaign: max_commit_files=21. cap − null_p95 = 0.000959. E-007: margin=0.305152 >> yardstick=0.015073. Very strong E-007 signal despite narrow null exceedance.
- ast_metrics cap (0.590025) near null_p95 (0.603179); dep_graph (0.447109) well below null_p95 (0.603179). Both below null; not classified.
- activity baseline low (0.298027) relative to capture; ownership signal substantially exceeds both null and activity.
- Wall time 1:13.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
