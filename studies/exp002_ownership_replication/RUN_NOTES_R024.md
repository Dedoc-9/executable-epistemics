# Run Notes — R024 of 50: rq/rq

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 0fe8492b63e19134 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.218734 | 0.718995 | 0.233909 | (not tested EXP-002) |
| ast_metrics | 0.586604 | 0.720042 | 0.233909 | (not tested EXP-002) |
| ownership   | 0.720042 | 0.720042 | 0.233909 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.720042): giant-block discreteness. Not an erratum.
- Capture value is high (0.720042) but this is the null_p95 ceiling, not a meaningful signal. Giant block.
- Wall time 0:15.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
