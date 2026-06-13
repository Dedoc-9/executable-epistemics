# Run Notes — R011 of 50: pyeve/cerberus

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: fa5e57f67aa515a0 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.0 | 0.0 | 0.094737 | (not tested EXP-002) |
| ast_metrics | 0.081781 | 0.241296 | 0.094737 | (not tested EXP-002) |
| ownership   | 0.242915 | 0.241296 | 0.094737 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.001619 (0.242915−0.241296). Razor-thin; classification stands per §A.
- dep_graph capture=0.0, null_p95=0.0: degenerate partition (near-empty or disconnected dependency graph at E-006 filter=6). Same degenerate condition as EXP-001 observation on small repos. Not an erratum; dep_graph not tested in EXP-002.
- activity baseline low (0.094737): ownership signal is above baseline by a wide margin.
- Wall time 0:04.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
