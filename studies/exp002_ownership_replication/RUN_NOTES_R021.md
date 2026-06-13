# Run Notes — R021 of 50: httpie/httpie

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: afc1c93a30aad2e7 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. Stderr SyntaxWarnings emitted (see scrutiny). Proceed branch exercised — exit 0 is the SUSPEND trigger; warnings are not.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.033537 | 0.12108 | 0.195557 | (not tested EXP-002) |
| ast_metrics | 0.211237 | 0.305749 | 0.195557 | (not tested EXP-002) |
| ownership   | 0.305749 | 0.305749 | 0.195557 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.305749): giant-block discreteness. Not an erratum.
- SyntaxWarnings from httpie source during pipeline execution: Python 3.12 SyntaxWarning on invalid escape sequences (\[, \(, \e) in httpie source files at <unknown>:24-28. These warnings are emitted by the Python interpreter when the instrument's AST encoder parses httpie's source files; they originate in httpie's code (deprecated regex literals), not in the instrument. Exit code 0. Runner produced all output files. NOT an instrument erratum. Recorded for completeness.
- Wall time 0:25.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
