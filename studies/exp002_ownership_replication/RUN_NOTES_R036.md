# Run Notes — R036 of 50: boto/boto3

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis. Only ownership is classified in EXP-002 aggregate.

## Pin
- Ground-truth chain: 6d958da0a19b0238 · Score chain: 4ea0cbb465fad003 · E-006 filter = 15
- Precommitments pushed BEFORE scoring: REPO_DECLARATION_exp002.json at e36d2dd
- n_commits_used=4989 · n_commits_dropped_as_bulk=211 · n_files=11656 · n_cochange_pairs=20489

## Events (UPDATE_COMMITMENTS_exp002.md §A branches exercised)
- Pipeline clean, exit 0. No events. Proceed branch exercised.

## Classifications (ownership only — EXP-002 family; dep_graph/ast_metrics computed but not classified)
| family | capture | null_p95 | activity | classification |
|---|---|---|---|---|
| dep_graph   | 0.047933 | 0.055759 | 0.055891 | (not tested EXP-002) |
| ast_metrics | 0.055023 | 0.056287 | 0.055891 | (not tested EXP-002) |
| ownership   | 0.055891 | 0.056098 | 0.055891 | NOT_DETECTED |

## Scrutiny items
- Genuine gap: ownership cap=0.055891 < null_p95=0.056098 (gap=0.000207). All three families clustered in 0.047–0.056 range — extremely compressed capture distribution across the board.
- ownership cap==activity exactly (0.055891). e007_margin=(cap−activity)=0.000000; NOT_DETECTED regardless of null comparison.
- Largest file count in campaign: 11656 files, 20489 cochange pairs. boto3 is a code-generated SDK; thin per-file ownership coupling is structurally expected (generated files share no committer specialization pattern).
- Wall time not captured in log.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → continue to next repo.
