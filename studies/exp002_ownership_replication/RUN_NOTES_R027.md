# Run Notes — R027 of 50: taskiq-python/taskiq

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: eb6e5cffbd674475 · E-006 filter = 17
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.406905 | 0.474723 | 0.289766 | (not tested EXP-002) |
| ast_metrics | 0.451911 | 0.495068 | 0.289766 | (not tested EXP-002) |
| ownership   | 0.495068 | 0.495068 | 0.289766 | NOT_DETECTED |

## Scrutiny items
- ownership cap==null_p95 (0.495068): giant-block discreteness. Not an erratum.
- E-006 filter=17: highest filter value in the campaign; only commits touching ≤17 files retained. Small filtered corpus.
- Wall time 0:26.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
