# Run Notes — R020 of 50: tiangolo/typer

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 2b5d1a6d5b61fb5b · E-006 filter = 8
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.020725 | 0.213731 | 0.130829 | (not tested EXP-002) |
| ast_metrics | 0.21114 | 0.233161 | 0.130829 | (not tested EXP-002) |
| ownership   | 0.233161 | 0.224093 | 0.130829 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.009068 (0.233161−0.224093). Widest DETECTED margin in batch 2; comfortable above null_p95.
- activity baseline low (0.130829): ownership signal clearly above activity channel.
- dep_graph very low (0.020725 vs null_p95=0.213731): structural coupling is not driving co-change here.
- Wall time 2:10.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
