# Run Notes — R040 of 50: joke2k/faker

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 56d90d78f1f96832 · Score chain: 1b164495b5d97ff6 · E-006 filter = 5
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=3469 · n_commits_dropped_as_bulk=167 · n_files=667 · n_cochange_pairs=313

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.224888 | 0.288356 | 0.322589 | (not tested EXP-002) |
| ast_metrics | 0.322589 | 0.322589 | 0.322589 | (not tested EXP-002) |
| ownership   | 0.320590 | 0.314093 | 0.322589 | LEAKAGE |

E-007: cap > null_p95 but cap ≤ activity (e007_margin=-0.001999 < 0). LEAKAGE (E-003 channel).

## Scrutiny items
- LEAKAGE: third in campaign after pip (EXP-001) and bandit (R031). cap=0.32059 exceeds null_p95=0.314093 but does not exceed activity=0.322589. E-003 channel (size/frequency co-movement) operative.
- ast_metrics triple tie: cap==null_p95==activity=0.322589. Giant-block discreteness in all three values. Not an erratum.
- dep_graph below null (0.224888 vs 0.288356).
- Wall time 4:08.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
