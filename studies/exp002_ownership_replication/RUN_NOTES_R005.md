# Run Notes — R005 of 50: python-gino/gino

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 1ea0fbe859475ba2 · E-006 filter = 7
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.020681 | 0.159367 | 0.317518 | (not tested EXP-002) |
| ast_metrics | 0.29927 | 0.465937 | 0.317518 | (not tested EXP-002) |
| ownership   | 0.475669 | 0.475669 | 0.317518 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.475669): giant-block discreteness. Not an erratum.
- Dormant repo (last push 2022-02-12): wall time 0:11 consistent with small/frozen corpus. No mechanical unavailability; scored cleanly.
- dep_graph very low (0.020681 vs null_p95=0.159367): dep_graph partition is much weaker than ownership; not relevant to EXP-002.
- Wall time 0:11.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
