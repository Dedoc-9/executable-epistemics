# Run Notes — R035 of 50: pypa/setuptools

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 7da2543052b37631 · Score chain: 60dd37ae2b0dc00d · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=13323 · n_commits_dropped_as_bulk=590 · n_files=1392 · n_cochange_pairs=1163

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.015943 | 0.075008 | 0.250835 | (not tested EXP-002) |
| ast_metrics | 0.249165 | 0.250835 | 0.250835 | (not tested EXP-002) |
| ownership   | 0.250835 | 0.250835 | 0.250835 | NOT_DETECTED |

## Scrutiny items
- Ownership triple tie: cap==null_p95==activity=0.250835. Giant-block discreteness (single-linkage collapse). Not an erratum; same mechanism as R031 ast_metrics triple tie and multiple prior repos.
- ast_metrics near-tie: cap=0.249165 vs null_p95=0.250835 (gap=0.001670). Below null_p95; NOT_DETECTED.
- dep_graph far below null (0.015943 vs 0.075008) and below activity (0.250835). Very sparse import coupling relative to cochange.
- Large commit history: 13323 commits used (second-largest in campaign), filter=5 (tight single-linkage produces compressed cochange distribution).
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
