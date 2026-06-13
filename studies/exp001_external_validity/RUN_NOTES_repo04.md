# Run Notes — Repository 4 of 20: tornadoweb/tornado

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: 535fece73d4ac0f8 · E-006 filter = 7
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.310207 | 0.379351 | 0.577611 | NOT_DETECTED |
| ast_metrics | 0.577611 | 0.708373 | 0.577611 | NOT_DETECTED |
| ownership | 0.708843 | 0.708843 | 0.577611 | NOT_DETECTED |

## Scrutiny items
- ownership capture == own null_p95 (0.708843): single-linkage giant-block discreteness, not defect (cf. repo 1). NOT an erratum.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 4/20 scored. Erratum budget: 1 of 3 used.
