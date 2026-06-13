# Run Notes — R047 of 50: mongodb/motor

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: bff38d2cc78db25f · Score chain: a9716ae532e14ec2 · E-006 filter = 9
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=1781 · n_commits_dropped_as_bulk=92 · n_files=196 · n_cochange_pairs=603

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.286776 | 0.422535 | 0.313772 | (not tested EXP-002) |
| ast_metrics | 0.237089 | 0.414319 | 0.313772 | (not tested EXP-002) |
| ownership   | 0.427230 | 0.417840 | 0.313772 | DETECTED |

E-007: e007_margin=(cap−activity)=0.113458 > e007_yardstick=(p95−median)=0.039123 → DETECTED.

## Scrutiny items
- cap − null_p95 = 0.009390. E-007: margin=0.113458 >> yardstick=0.039123.
- dep_graph below null (0.286776 vs 0.422535) and below activity (0.313772).
- Wall time 0:15.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
