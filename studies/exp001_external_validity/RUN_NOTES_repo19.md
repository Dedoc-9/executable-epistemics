# Run Notes — Repository 19 of 20: sympy/sympy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: 9e967ca79d8d892d · E-006 filter = 6
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.350852 | 0.55062 | 0.819247 | NOT_DETECTED |
| ast_metrics | 0.836585 | 0.837103 | 0.819247 | NOT_DETECTED |
| ownership | 0.837103 | 0.837103 | 0.819247 | NOT_DETECTED |

## Scrutiny items
- ownership capture == own null_p95 (0.837103): single-linkage giant-block discreteness, not defect (cf. repo 1). NOT an erratum.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 19/20 scored. Erratum budget: 1 of 3 used.
