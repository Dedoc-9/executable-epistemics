# Run Notes — R012 of 50: python-jsonschema/jsonschema

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 6dfa584b0f310d5a · E-006 filter = 7
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.0 | 0.0 | 0.151694 | (not tested EXP-002) |
| ast_metrics | 0.252332 | 0.405989 | 0.151694 | (not tested EXP-002) |
| ownership   | 0.405989 | 0.405989 | 0.151694 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.405989): giant-block discreteness. Not an erratum.
- dep_graph capture=0.0, null_p95=0.0: degenerate partition; same as R011. Not relevant to EXP-002.
- Wall time 0:09.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
