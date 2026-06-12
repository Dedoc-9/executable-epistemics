# Interpretation Rules (binding summary)

1. validity_scope before summary: read `certifies`, `does_not_certify`,
   and `forbidden_interpretations` before describing any result.
2. E-004/E-007 classification: DETECTED requires beating the random null
   AND the activity baseline by more than the null's spread. LEAKAGE means
   churn was rediscovered. UNRESOLVED counts as non-detection.
3. E-005 multiplicity: per-repo outcomes are intermediate data. Only the
   aggregate (>=60% of the declared population) is reportable.
4. E-008 outcomes: VALIDATED (point >= 0.60), REJECTED (Wilson upper < 0.60),
   INCONCLUSIVE (between), INCOMPLETE (population not fully scored).
5. E-009 rendering: no outcome may be displayed without its claim banner.
6. Chain hashes certify integrity (unaltered since compilation), never truth.
7. A negative aggregate is a valid, publishable terminal state, not a
   failure of the framework.
8. Small corpora produce permissive nulls: non-detection at small n is
   uninformative about structure (calibration finding). Report it as-is.
