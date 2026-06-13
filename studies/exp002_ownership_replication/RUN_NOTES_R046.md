# Run Notes — R046 of 50: jazzband/pip-tools

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 34232f25902b5c63 · Score chain: f18e05c8f517f601 · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1971 · n_commits_dropped_as_bulk=102 · n_files=251 · n_cochange_pairs=313

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.027995 | 0.401042 | 0.393229 | (not tested EXP-002) |
| ast_metrics | 0.393229 | 0.554688 | 0.393229 | (not tested EXP-002) |
| ownership   | 0.554688 | 0.553385 | 0.393229 | DETECTED |

E-007: e007_margin=(cap−activity)=0.161459 > e007_yardstick=(p95−median)=0.048828 → DETECTED.

## Scrutiny items
- cap − null_p95 = 0.001303 (narrow). E-007: margin=0.161459 >> yardstick=0.048828. DETECTED classification robust.
- ast_metrics cap==activity (0.393229 each); both below null_p95 (0.554688).
- dep_graph very low (0.027995 vs 0.401042) — sparse import coupling.
- Wall time 0:13.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
