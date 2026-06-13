# Run Notes — R019 of 50: mitmproxy/mitmproxy

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 5d0e3876a4414869 · E-006 filter = 11
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.315903 | 0.316391 | 0.309311 | (not tested EXP-002) |
| ast_metrics | 0.295068 | 0.316066 | 0.309311 | (not tested EXP-002) |
| ownership   | 0.316391 | 0.315903 | 0.309311 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.000488 (0.316391−0.315903). Razor-thin; classification stands per §A.
- activity baseline (0.309311) close to null_p95 (0.315903) and close to ownership capture (0.316391): gap between capture and activity = 0.007080. NOT LEAKAGE: capture (0.316391) exceeds null_p95 (0.315903); E-007 LEAKAGE condition requires capture ≤ activity baseline, which is not met here (0.316391 > 0.309311). DETECTED classification is correct.
- dep_graph capture=0.315903 just below own null_p95=0.316391; dep_graph would be borderline too, irrelevant to EXP-002.
- Wall time 3:39.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
