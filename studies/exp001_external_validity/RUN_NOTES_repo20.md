# Run Notes — Repository 20 of 20: pypa/pip

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- Ground-truth chain: d06d6be6325110ff · E-006 filter = 8
- Precommitments pushed BEFORE scoring: full campaign precommit batch (see repo 1 RUN_NOTES)
- E-013 applied: --exclude-glob "src/pip/_vendor/*" (b3c1e7f2a904d658, recorded pre-run)

## Events (UPDATE_COMMITMENTS §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (intermediate data, not reportable)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph | 0.703175 | 0.703175 | 0.703175 | NOT_DETECTED |
| ast_metrics | 0.703175 | 0.703175 | 0.703175 | NOT_DETECTED |
| ownership | 0.702673 | 0.679532 | 0.703175 | LEAKAGE |

## Scrutiny items
- dep_graph capture == null_p95 == activity (0.703175): triple tie. dep_graph, ast_metrics, and activity baseline all collapse to the same giant-block partition. First triple-encoder collapse in the campaign. Same single-linkage discreteness mechanism as repos 1, 2, 4, 8, 19; pip's tracked-file graph after _vendor/ exclusion still produces a dominant giant component. NOT an erratum.
- First LEAKAGE classification in the campaign: ownership exceeds null_p95 (0.702673 > 0.679532) but is below activity baseline (0.702673 < 0.703175) by margin 0.000502. Per E-007, LEAKAGE — ownership encoder signal does not exceed what pure activity-based partitioning captures. E-003 channel (size/frequency co-movement) is the pre-registered explanation. No new mechanism asserted.
- E-013 exclusion (src/pip/_vendor/*) applied as recorded. Pre-observation; no discretionary choice at run time.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → run E-008 aggregate.
Campaign: 20/20 scored. Erratum budget: 1 of 3 used.
