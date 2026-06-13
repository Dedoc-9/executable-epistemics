# Run Notes — R032 of 50: PyCQA/pycodestyle

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 2effaef9913a0841 · Score chain: ffde2597db3a2bf2 · E-006 filter = 4
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=1117 · n_commits_dropped_as_bulk=46 · n_files=104 · n_cochange_pairs=122

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- SyntaxWarnings emitted during AST scan: 22 warning lines. Source: invalid decimal literals and invalid escape sequences (\.) in pycodestyle source files. Python 3.12 deprecation of these constructs in scanned source code; exit code 0. NOT an instrument erratum — warnings originate in the scanned repository's source, not in instrument code. Same class as R021 (httpie).
- Pipeline clean, exit 0. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.351220 | 0.345122 | 0.045122 | (not tested EXP-002) |
| ast_metrics | 0.045122 | 0.378049 | 0.045122 | (not tested EXP-002) |
| ownership   | 0.031707 | 0.363415 | 0.045122 | NOT_DETECTED |

## Scrutiny items
- Genuine ownership gap: cap=0.031707 is far below null_p95=0.363415. No ambiguity in classification.
- dep_graph (non-classified) exceeds null: cap=0.351220 > null_p95=0.345122 AND > activity=0.045122. Instrument records DETECTED for dep_graph family. This is NOT a classified result in EXP-002 (ownership only) and is intermediate data per E-005. Noted for completeness.
- ast_metrics==activity (0.045122 each): activity-baseline tie, not a scoring issue.
- Small repo: 104 files, filter=4. Thin cochange matrix (122 pairs). Low capture values consistent with tight module structure.
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
