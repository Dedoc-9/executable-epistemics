# Run Notes — R002 of 50: coleifer/peewee

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: cf656d68f081e594 · E-006 filter = 4
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.336591 | 0.46797 | 0.128845 | (not tested EXP-002) |
| ast_metrics | 0.128845 | 0.46797 | 0.128845 | (not tested EXP-002) |
| ownership   | 0.46797 | 0.46797 | 0.128845 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.46797): giant-block discreteness. Single-linkage collapse; cap is at p95 by construction. Same mechanism as EXP-001 repos 1,2,4,8,19,20. Not an erratum.
- E-006 filter=4: low threshold; most files co-change. Consistent with giant-block outcome.
- activity baseline very low (0.128845): activity is not the driver here; structure is collapsed.
- Wall time 0:23.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
