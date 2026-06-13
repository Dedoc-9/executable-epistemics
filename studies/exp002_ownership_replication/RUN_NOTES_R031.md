# Run Notes — R031 of 50: PyCQA/bandit

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 1fd80a3ee0f53515 · Score chain: 462165937ef31013 · E-006 filter = 10
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=1094 · n_commits_dropped_as_bulk=57 · n_files=362 · n_cochange_pairs=572

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.397935 | 0.517597 | 0.590802 | (not tested EXP-002) |
| ast_metrics | 0.590802 | 0.590802 | 0.590802 | (not tested EXP-002) |
| ownership   | 0.589864 | 0.573440 | 0.590802 | LEAKAGE |

E-007 check (ownership): e007_margin=(cap−activity)=−0.000938 < e007_yardstick=(p95−median)=0.043642. cap > null_p95 but cap ≤ activity → LEAKAGE (E-003 channel).

## Scrutiny items
- LEAKAGE classification: second in campaign after pypa/pip in EXP-001. Cap exceeds random null (0.589864 > 0.573440) but does not exceed activity baseline (0.590802). E-003 soft circularity channel (size/frequency co-movement in ownership encoder) confirmed operative on a security-tooling repo.
- ast_metrics triple tie: cap==null_p95==activity=0.590802. Giant-block discreteness. Not an erratum; same mechanism documented throughout campaign.
- dep_graph well below null (0.397935 vs 0.517597); not leakage candidate — below null entirely.
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
