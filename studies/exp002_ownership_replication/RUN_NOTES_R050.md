# Run Notes — R050 of 50: arrow-py/arrow

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 5ae7a2310edf772b · Score chain: cfa04ff3175d5b6a · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1080 · n_commits_dropped_as_bulk=51 · n_files=76 · n_cochange_pairs=178

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.527344 | 0.540039 | 0.376953 | (not tested EXP-002) |
| ast_metrics | 0.219727 | 0.503906 | 0.376953 | (not tested EXP-002) |
| ownership   | 0.540039 | 0.540039 | 0.376953 | NOT_DETECTED |

## Scrutiny items
- Ownership giant-block: cap==null_p95=0.540039. exceeds_null_p95=false → NOT_DETECTED despite e007_margin=0.163086. Same mechanism as R037 (urllib3) and others.
- dep_graph(non-classified) also near-tie: cap=0.527344 vs null_p95=0.540039 (gap=0.012695). Below null.
- Small repo: 76 files, 178 cochange pairs.
- Wall time 0:04.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
