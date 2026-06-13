# Run Notes — R045 of 50: rubik/radon

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 2c89ffdcc9d0ecce · Score chain: 03c52e14cde4e3b2 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=495 · n_commits_dropped_as_bulk=25 · n_files=86 · n_cochange_pairs=90

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.446108 | 0.479042 | 0.404192 | (not tested EXP-002) |
| ast_metrics | 0.266467 | 0.368263 | 0.404192 | (not tested EXP-002) |
| ownership   | 0.479042 | 0.449102 | 0.404192 | UNRESOLVED_ACTIVITY_MARGIN |

E-007: cap > null_p95 but e007_margin=0.074850 ≤ yardstick=0.083833. UNRESOLVED_ACTIVITY_MARGIN. Counts as non-detection.

## Scrutiny items
- UNRESOLVED_ACTIVITY_MARGIN: cap=0.479042 > null_p95=0.449102 (gap=0.029940) but E-007 dual condition fails: e007_margin=(cap−activity)=0.074850 < yardstick=(null_p95−null_median)=0.083833 (deficit=0.008983). Counts as non-detection in E-008 aggregate.
- dep_graph(non-classified) also below null (0.446108 vs 0.479042) — tracks ownership pattern. ast_metrics cap (0.266467) below activity (0.404192).
- Small repo: 86 files, 90 cochange pairs. Marginal result on a near-empty graph.
- Wall time 0:05.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
