# Run Notes — R041 of 50: getsentry/responses

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 195d2464dfd16e1a · Score chain: bdfa0b4860c41d32 · E-006 filter = 4
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=630 · n_commits_dropped_as_bulk=26 · n_files=41 · n_cochange_pairs=50

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.000000 | 0.000000 | 0.107595 | (not tested EXP-002) |
| ast_metrics | 0.107595 | 0.424051 | 0.107595 | (not tested EXP-002) |
| ownership   | 0.000000 | 0.025316 | 0.107595 | NOT_DETECTED |

## Scrutiny items
- Ownership and dep_graph both return capture=0.0. dep_graph null_p95=0.0 (empty import graph — instrument emits zero/skip signature per E-011 design). Very small repo: 41 files, 50 cochange pairs.
- ast_metrics cap==activity (0.107595 each); both well below null_p95=0.424051.
- Wall time 0:02 — consistent with minimal file count.
- Wall time 0:02.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
