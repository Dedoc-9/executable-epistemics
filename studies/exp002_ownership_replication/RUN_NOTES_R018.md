# Run Notes — R018 of 50: encode/httpx

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: e5c2fa27ec3758ff · E-006 filter = 11
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.06668 | 0.230738 | 0.307989 | (not tested EXP-002) |
| ast_metrics | 0.214271 | 0.402318 | 0.307989 | (not tested EXP-002) |
| ownership   | 0.403131 | 0.403131 | 0.307989 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.403131): giant-block discreteness. Not an erratum.
- activity baseline moderate (0.307989): elevated relative to dep_graph (0.06668), consistent with a project where ownership and activity co-move.
- Wall time 0:13.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
