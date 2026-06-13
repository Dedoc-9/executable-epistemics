# Run Notes — R030 of 50: PyCQA/flake8

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 7d4f775d3d2bd29a · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.458675 | 0.469844 | 0.463142 | (not tested EXP-002) |
| ast_metrics | 0.463142 | 0.474311 | 0.463142 | (not tested EXP-002) |
| ownership   | 0.474311 | 0.474311 | 0.463142 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.474311): giant-block discreteness. Not an erratum.
- activity baseline very high (0.463142); dep_graph capture (0.458675) and ast_metrics capture (0.463142) both track activity closely. All families near null_p95 ceiling.
- Wall time 0:14.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
