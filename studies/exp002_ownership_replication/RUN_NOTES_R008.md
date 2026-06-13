# Run Notes — R008 of 50: MagicStack/asyncpg

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: e5112a2fafed7d0c · E-006 filter = 9
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.212775 | 0.269745 | 0.118256 | (not tested EXP-002) |
| ast_metrics | 0.276219 | 0.283988 | 0.118256 | (not tested EXP-002) |
| ownership   | 0.283988 | 0.283988 | 0.118256 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.283988): giant-block discreteness. Not an erratum.
- activity baseline low (0.118256): small focused library with concentrated co-change; giant block at ceiling.
- Wall time 0:10.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
