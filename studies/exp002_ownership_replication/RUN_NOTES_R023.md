# Run Notes — R023 of 50: tqdm/tqdm

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 2b1912e50467d0a2 · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.042105 | 0.158596 | 0.126316 | (not tested EXP-002) |
| ast_metrics | 0.230877 | 0.373333 | 0.126316 | (not tested EXP-002) |
| ownership   | 0.289123 | 0.340351 | 0.126316 | NOT_DETECTED |

## Scrutiny items
- ownership capture=0.289123 genuinely below null_p95=0.340351 (gap 0.051228): NOT_DETECTED is not giant-block; ownership partition has real signal but does not clear the null threshold.
- E-006 filter=5: low threshold, co-change corpus is sparse. Ownership is not structurally organizing what little coupling exists.
- Wall time 0:11.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
