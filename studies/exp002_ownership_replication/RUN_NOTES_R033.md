# Run Notes — R033 of 50: PyCQA/pylint

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 866ecbe882ada9ea · Score chain: 3bc5acbf853729e9 · E-006 filter = 12
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=9119 · n_commits_dropped_as_bulk=417 · n_files=4784 · n_cochange_pairs=7152

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- SyntaxWarnings emitted during AST scan: 36 warning lines. Source: invalid escape sequences (\z, \u) in pylint source files. Python 3.12 deprecation; exit code 0. NOT an instrument erratum — warnings originate in scanned repo source. Same class as R021 (httpie) and R032 (pycodestyle).
- Pipeline clean, exit 0. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.145613 | 0.219900 | 0.247797 | (not tested EXP-002) |
| ast_metrics | 0.206979 | 0.275137 | 0.247797 | (not tested EXP-002) |
| ownership   | 0.272873 | 0.269146 | 0.247797 | DETECTED |

E-007 check (ownership): cap − null_p95 = 0.003727. e007_margin=(cap−activity)=0.025076 > e007_yardstick=(p95−median)=0.009299. Both conditions satisfied → DETECTED.

## Scrutiny items
- Narrow cap − null_p95 margin (0.003727) but E-007 dual-condition satisfied: excess over activity (0.025076) comfortably exceeds null spread (0.009299).
- Large repo: 9119 commits used, 4784 files — largest file count scored in campaign so far. Wall time substantial (~30 min prior session estimate).
- dep_graph and ast_metrics both below null_p95 and below activity (well into NOT_DETECTED territory).
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
