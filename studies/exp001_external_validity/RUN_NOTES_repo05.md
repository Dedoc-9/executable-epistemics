# Run Notes — Repository 5 of 20: psf/black

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: a231b8d86c92e153 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.0625 | 0.269561 | 0.280773 | NOT_DETECTED |
| ast_metrics | 0.280773 | 0.280773 | 0.280773 | NOT_DETECTED |
| ownership | 0.005725 | 0.08063 | 0.280773 | NOT_DETECTED |

## Scrutiny items
- ast_metrics capture == own null_p95 (0.280773): discreteness artifact.
- Pipeline stderr: Python SyntaxWarnings from black's own test files (intentionally invalid escape sequences). Exit 0. Not an erratum.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 5/20 scored. Erratum budget: 1 of 3 used.
