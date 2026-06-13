# Run Notes — R039 of 50: HypothesisWorks/hypothesis

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 25b84ceb87e7412e · Score chain: 5d3636cf488a54d0 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=14093 · n_commits_dropped_as_bulk=696 · n_files=1067 · n_cochange_pairs=2521

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.035142 | 0.092838 | 0.318259 | (not tested EXP-002) |
| ast_metrics | 0.255901 | 0.320881 | 0.318259 | (not tested EXP-002) |
| ownership   | 0.321755 | 0.321231 | 0.318259 | DETECTED |

E-007: e007_margin=(cap−activity)=0.003496 > e007_yardstick=(p95−median)=0.003205 → DETECTED.

## Scrutiny items
- Narrowest DETECTED in full campaign: cap − null_p95 = 0.000524; e007_margin − yardstick = 0.000291 (margin barely clears the dual condition). Both conditions strictly satisfied per instrument output.
- Largest commit count in campaign: 14093 used. ast_metrics capture (0.255901) close to activity (0.318259) and null_p95 (0.320881); both below null_p95.
- dep_graph well below null (0.035142 vs 0.092838).
- Wall time 2:51.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
