# Pre-Run Surprise Priors (recorded before repository 1 executes)

Per protocol discipline: what would genuinely surprise each experimenter,
written down BEFORE first contact. This file is additive precommitment —
it amends nothing and carries no evidentiary weight; it exists so that
surprise cannot be retrofitted.

## Assistant's priors (recorded 2026-06-12, before any real-repo run)

**dep_graph** — Expected: beats the random null but lands LEAKAGE or
UNRESOLVED_ACTIVITY_MARGIN on most repos (import structure plausibly
correlates with co-change, but so does churn). Genuinely surprising:
(a) clean DETECTED with a wide E-007 margin on the first repo — would
suggest structural signal is easy, against the encoder-relativity
pessimism of the prior project; (b) capture BELOW the null median —
systematic anti-correlation would be the strangest possible result.

**ast_metrics** — Expected: NOT_DETECTED or LEAKAGE (the E-003 size
channel). Surprising: clean DETECTED.

**ownership** — Pre-run honesty note, recorded here rather than as an
amendment: this family is derived from commit METADATA (authorship), the
same history that generates the ground truth — pair-blind, like the
activity baseline, but E-003-class ambiguity applies. Expected: high raw
capture that fails the activity baseline or margin. Surprising: ownership
cleanly DETECTED *and* dep_graph not — would suggest social structure
out-predicts technical structure.

**Operational surprises**: E-006 formula filter hitting its cap (50) or
returning < 5; any encoder skip on a major repo; runtime beyond hours on
mid-size repos (pure-Python O(n²) is untested at numpy scale — declared,
not benchmarked).

**Meta-prior**: across 20 repos, modal outcome INCONCLUSIVE under E-008
(point < 0.60, Wilson upper >= 0.60). A clean POSITIVE or clean NEGATIVE
at n=20 would itself be mildly surprising.

## Compressed-prior acknowledgment (secondary_corr.py pair selection)

The six registered pairs in secondary_corr.py (tracked_py_files,
non_merge_commits × per-family E-007 margin) were NOT chosen neutrally.
They encode a prior: E-003/E-004 already identified activity (size, churn)
as the dominant confound threat, so the secondary analysis points at that
threat specifically. Classification: compressed prior injection, declared
pre-observation — not exploratory, not assumption-free. If the confound
operates through a channel other than these two covariates, this analysis
will not see it; that blind spot is accepted and recorded here.

## Operator's priors (Daniel — add before running, then commit)

- dep_graph:
- ast_metrics:
- ownership:
- operational:
- what result would make you distrust the instrument rather than accept it:
