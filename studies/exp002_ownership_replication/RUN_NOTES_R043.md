# Run Notes — R043 of 50: kevin1024/vcrpy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 665a2ccef3ea3656 · Score chain: c6afba9b809ec67a · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1130 · n_commits_dropped_as_bulk=42 · n_files=131 · n_cochange_pairs=252

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.077543 | 0.270896 | 0.257805 | (not tested EXP-002) |
| ast_metrics | 0.404834 | 0.454179 | 0.257805 | (not tested EXP-002) |
| ownership   | 0.454179 | 0.439074 | 0.257805 | DETECTED |

E-007: e007_margin=(cap−activity)=0.196374 > e007_yardstick=(p95−median)=0.035247 → DETECTED.

## Scrutiny items
- Clean DETECTED: cap − null_p95 = 0.015105. e007_margin=0.196374 >> yardstick=0.035247.
- dep_graph well below null (0.077543 vs 0.270896) and below activity (0.257805).
- ast_metrics below null (0.404834 vs 0.454179); cap==ownership_p95 (0.454179) — coincidence of values, not structural.
- Wall time 0:13.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
