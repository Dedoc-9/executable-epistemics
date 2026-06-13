# Run Notes — R006 of 50: psycopg/psycopg2

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 5df4450ef75a878a · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.026847 | 0.050558 | 0.046247 | (not tested EXP-002) |
| ast_metrics | 0.063688 | 0.097394 | 0.046247 | (not tested EXP-002) |
| ownership   | 0.097786 | 0.097786 | 0.046247 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.097786): giant-block discreteness. Not an erratum.
- All capture values extremely low (ownership null_p95=0.097786, activity=0.046247): sparse co-change corpus with E-006 filter=8. Corpus is structurally thin.
- Wall time 0:12.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
