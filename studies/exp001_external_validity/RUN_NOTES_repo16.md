# Run Notes — Repository 16 of 20: scipy/scipy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: 262400b9070e44a5 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.492373 | 0.509763 | 0.446672 | NOT_DETECTED |
| ast_metrics | 0.46101 | 0.509763 | 0.446672 | NOT_DETECTED |
| ownership | 0.509702 | 0.509519 | 0.446672 | DETECTED |

## Scrutiny items
- ownership DETECTED by razor-thin margin (0.000183): classification mechanically valid; margin recorded without interpretation.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 16/20 scored. Erratum budget: 1 of 3 used.
