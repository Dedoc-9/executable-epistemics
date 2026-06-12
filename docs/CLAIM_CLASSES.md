# Claim Classes

Every artifact carries exactly one claim_class. It defines what the artifact
may be used as — and every human-readable rendering must surface it (E-009).

| claim_class | is | is never |
|---|---|---|
| observer_agreement_only | structural comparison between declared views | a statement about the underlying system |
| historical_cochange_observation_only | frozen ground truth | a quality/architecture judgment |
| preregistered_methodology_only | rules, frozen pre-data | a finding |
| preregistered_study_population_only | the declared sample | a representativeness claim |
| pipeline_calibration_only / campaign_rehearsal_only | mechanics validation | evidence (exp001_evidence is forbidden on these) |
| exp001_scored_observation | one repository's intermediate datum | individually reportable (E-005) |
| exp001_aggregate_conclusion | the study's reportable result | truth about software generally |
| behavioral_equivalence_on_tested_corpora_only | version-equivalence witness | a general correctness proof |

Rule of quotation: a number lifted from an artifact carries its claim_class
with it. If you cannot state the claim_class of a figure you are citing,
you do not yet know what the figure means.
