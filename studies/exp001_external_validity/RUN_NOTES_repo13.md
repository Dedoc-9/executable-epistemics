# Run Notes — Repository 13 of 20: scikit-learn/scikit-learn

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: a926d56f1857f996 · E-006 filter = 8
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.391132 | 0.373052 | 0.359765 | DETECTED |
| ast_metrics | 0.377845 | 0.393026 | 0.359765 | NOT_DETECTED |
| ownership | 0.0 | 0.001521 | 0.359765 | NOT_DETECTED |

## Scrutiny items
- ownership capture=0.0, null_p95=0.001521: null_p95 near-zero confirms null is calibrated to actual partition granularity. scikit-learn ownership is highly distributed (n_files=3055, n_commits=29348); ownership encoder produces fine-grained partition, constraining capture by construction. NOT an erratum.
- dep_graph DETECTED (capture=0.391132, null_p95=0.373052, margin=0.018080): only dep_graph detection in 19 repos at campaign close. Recorded without interpretation (E-005).

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 13/20 scored. Erratum budget: 1 of 3 used.
