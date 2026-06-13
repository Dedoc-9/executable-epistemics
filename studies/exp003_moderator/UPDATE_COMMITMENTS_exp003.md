# Update Commitments — EXP-003

Governs all analysis steps from preregistration to AGGREGATE_exp003.md.

## §A — Script execution discipline

- compute_moderators_exp003.py: run ONCE after preregistration commit.
  Re-runs are permitted only if the repo state (cloned repos) is unchanged;
  the output hash must match. Any deviation triggers a §C erratum.
- analyze_exp003.py: run ONCE after moderators_exp003.json is written and
  before it is committed. The script reads score_ownership.json files;
  those files must not be modified between compute and analyze runs.
- No manual edits to moderators_exp003.json between compute and analyze.

## §B — Outcome reporting

- Primary outcome: VALIDATED_CONDITIONAL, REJECTED_CONDITIONAL, or
  INCONCLUSIVE. Determined mechanically by analyze_exp003.py.
- Secondary outcome: r_pb and one-tailed p-value. Significant at α=0.05.
- Per-repo M₁ values are reported in AGGREGATE_exp003.md as a distribution
  table. They are NOT per-repo results (M₁ is an input variable, not an
  outcome) and are reportable.
- Per-repo DETECTED/NOT_DETECTED classifications appearing in AGGREGATE
  are there for reproducibility. They remain E-005 intermediate data and
  are not individually interpretable as results.

## §C — Erratum budget

EXP-003 shares the MCL_OBS2 §C budget (currently 3/3 remaining post EXP-002).
Any change to compute_moderators_exp003.py or analyze_exp003.py after
preregistration consumes one §C erratum. Erratum must be filed in
studies/errata/ERRATA.json before the modified script is re-run.

## §D — Forbidden procedures

- post_hoc_threshold_selection: choosing M₁_split after examining outcome data.
- script_modification_post_execution: modifying scripts after step 4 commit.
- moderator_dredging: testing additional moderators not in HYPOTHESIS_exp003.md
  and reporting them as confirmatory results.
- cherry_picked_strata: excluding repos from a stratum after seeing the
  stratum's detection rate.
