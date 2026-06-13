# Run Notes — R026 of 50: coleifer/huey

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 60ec4bfe015bf3fc · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.446849 | 0.449671 | 0.415804 | (not tested EXP-002) |
| ast_metrics | 0.415804 | 0.465663 | 0.415804 | (not tested EXP-002) |
| ownership   | 0.460019 | 0.463782 | 0.415804 | NOT_DETECTED |

## Scrutiny items
- ownership capture=0.460019 genuinely below null_p95=0.463782 (gap 0.003763): NOT_DETECTED is not giant-block. Ownership is close to but does not clear the null threshold.
- activity baseline very high (0.415804); all three family captures are close together and all near null_p95. Repo is activity-dense; partition structure is hard to distinguish from random at this co-change frequency.
- Wall time 0:11.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
