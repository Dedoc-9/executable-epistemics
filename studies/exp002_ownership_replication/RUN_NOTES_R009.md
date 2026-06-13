# Run Notes — R009 of 50: pydantic/pydantic

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: d40621e281748817 · E-006 filter = 15
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.288102 | 0.323505 | 0.275333 | (not tested EXP-002) |
| ast_metrics | 0.296173 | 0.323505 | 0.275333 | (not tested EXP-002) |
| ownership   | 0.323505 | 0.323146 | 0.275333 | DETECTED |

## Scrutiny items
- ownership DETECTED margin=0.000359 (0.323505−0.323146). Razor-thin; classification stands per §A.
- activity baseline well below ownership capture (0.275333 << 0.323505): E-003 channel not implicated.
- Wall time 2:33.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
