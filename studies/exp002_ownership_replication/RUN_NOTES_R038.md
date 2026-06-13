# Run Notes — R038 of 50: pyca/cryptography

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: e0b478eb2a23093d · Score chain: 854211dc1772c996 · E-006 filter = 6
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd (E-014 correction committed prior to this batch)
- n_commits_used=12648 · n_commits_dropped_as_bulk=619 · n_files=1068 · n_cochange_pairs=1897

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.095688 | 0.096363 | 0.226681 | (not tested EXP-002) |
| ast_metrics | 0.226681 | 0.267580 | 0.226681 | (not tested EXP-002) |
| ownership   | 0.267580 | 0.266615 | 0.226681 | DETECTED |

E-007: e007_margin=(cap−activity)=0.040899 > e007_yardstick=(p95−median)=0.006752 → DETECTED.

## Scrutiny items
- cap − null_p95 = 0.000965 (narrow absolute gap). E-007 dual-condition: margin=0.040899 >> yardstick=0.006752. DETECTED classification robust.
- Large repo: 12648 commits used (second-largest in campaign). ast_metrics cap==activity (0.226681 each); giant-block in ast family only.
- dep_graph near-tie: cap=0.095688 vs p95=0.096363 (gap=0.000675). Below null; NOT_DETECTED.
- Wall time 2:05.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
