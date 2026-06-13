# Run Notes — R044 of 50: mkdocs/mkdocs

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 826d31026d045e1b · Score chain: cd9566d0694d8b1e · E-006 filter = 13
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1625 · n_commits_dropped_as_bulk=79 · n_files=331 · n_cochange_pairs=1189

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.350062 | 0.351296 | 0.360963 | (not tested EXP-002) |
| ast_metrics | 0.285479 | 0.359934 | 0.360963 | (not tested EXP-002) |
| ownership   | 0.360963 | 0.329905 | 0.360963 | UNRESOLVED_ACTIVITY_MARGIN |

E-007: cap > null_p95 but e007_margin=0.000000 ≤ yardstick=0.050185. UNRESOLVED_ACTIVITY_MARGIN. Counts as non-detection.

## Scrutiny items
- UNRESOLVED_ACTIVITY_MARGIN: cap=0.360963 exceeds null_p95=0.329905 (gap=0.031058) but cap==activity=0.360963 exactly. E-007 dual condition: e007_margin=(cap−activity)=0.000 not > yardstick=0.050185. Counts as non-detection in E-008 aggregate.
- Highest filter in campaign: max_commit_files=13. dep_graph near-tie: cap=0.350062 vs null_p95=0.351296 (gap=0.001234). ast_metrics below null and activity.
- dep_graph(non-classified) also near-tie; consistent with activity-baseline-driven marginal lift across all families.
- Wall time 0:14.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
