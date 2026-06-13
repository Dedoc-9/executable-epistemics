# SYNTHESIS: EXP-003 — Gini Moderator Study

**Claim class**: cross-study synthesis. Characterizes the EXP-003 result and
constrains EXP-004 design. Committed BEFORE any EXP-004 analysis begins.

---

## EXP-003 result summary

| test | result |
|---|---|
| Primary (M₁ stratification, n=25/25) | REJECTED_CONDITIONAL |
| H stratum (M₁ > median) k/n | 10/25 = 0.400, Wilson CI [0.234, 0.593] |
| L stratum (M₁ ≤ median) k/n | 7/25 = 0.280, Wilson CI [0.143, 0.476] |
| Secondary r_pb(M₁, DETECTED) | 0.2182, p=0.0640 (one-tailed, α=0.05) |
| EXP-003 outcome | REJECTED_CONDITIONAL |

M₁ median = 0.858650 (computed from moderators_exp003.json, committed 4e809c8).

---

## What is established

**Established (protocol-valid):**
- M₁ (Gini) has the preregistered directional effect: H stratum detects at
  higher rate than L stratum (0.400 vs 0.280; Δ = 0.120).
- The directional signal is real but sub-threshold: Wilson upper for H
  (0.593) is 0.007 below the 0.600 success criterion.
- Secondary r_pb = 0.218 is positive (correct direction) and marginal
  (p = 0.064, not significant at preregistered α = 0.05).
- REJECTED_CONDITIONAL is not a null result: it rules out Gini alone as a
  sufficient moderator while leaving open the possibility that Gini is a
  necessary component of a sufficient moderator.

**Not established:**
- Gini is irrelevant. (The directional signal is consistent across both tests.)
- Gini is the primary moderator. (Effect size insufficient; REJECTED.)
- Per-repo Gini values predict individual repo outcomes. (E-005 applies.)

---

## Structural observation motivating EXP-004

The following is an aggregate-level observation from the M₁/M₂ distribution
in moderators_exp003.json (committed 4e809c8). It is NOT a moderator test —
it is a description of the data that motivates a new preregistered hypothesis.

Within the H stratum (high Gini), the NOT_DETECTED cases include repos with
notably high M₂ (commit density). The mechanistic account: a dominant author
who changes many files per commit saturates the cochange matrix — every file
pair co-occurs with the dominant author — and the ownership partition cannot
be distinguished from the activity baseline because both reflect the same
dominant change pattern. The ownership encoder requires not just concentrated
authorship (high M₁) but also *specialized* commits (low M₂) where the
dominant author's changes are targeted to specific file clusters.

This motivates a two-dimensional threshold hypothesis: the target cell is
repos with BOTH high M₁ (concentrated authorship) AND low M₂ (commit
specificity). Repos with high M₁ but high M₂ should behave like low-M₁
repos — both flood the cochange matrix, destroying the ownership partition.

This observation is post-hoc relative to EXP-003 in the sense that it uses
EXP-003 moderator values (M₁, M₂) jointly. It is NOT post-hoc relative to
EXP-002 outcome data: M₂ was a declared secondary moderator in EXP-003, and
the joint distribution of M₁ and M₂ was available before any outcome data
was examined. The EXP-004 threshold (M₁ median AND M₂ median from EXP-003)
is mechanical, not outcome-optimized.

---

## Cumulative chain of evidence

| study | population | outcome | interpretation |
|---|---|---|---|
| EXP-001 | n=20 flagships | VALIDATED | ownership detectable on flagship cohort |
| EXP-002 | n=50 general | REJECTED | ownership not universal |
| EXP-003 | n=50 (moderator) | REJECTED_CONDITIONAL | Gini necessary, not sufficient |
| EXP-004 | n=50 (joint) | TBD | joint threshold: high Gini AND low density |

Divergence from EXP-001: the flagship cohort likely occupies the target cell
(high M₁, low M₂) at higher rate than the general EXP-002 cohort. This is
a testable implication of EXP-004 — if VALIDATED_CONDITIONAL holds, the
EXP-001 positive result is explained by population selection into the target
cell, not by a universal property of the ownership metric.

---

## Constraints on EXP-004 design

- Population: EXP-002 cohort (n=50); no new scoring.
- Moderator inputs: moderators_exp003.json (committed, immutable).
- No new compute script required (M₁ and M₂ already available).
- Thresholds: M₁ and M₂ medians computed from moderators_exp003.json;
  both thresholds are mechanical, not outcome-optimized.
- No logistic regression or continuous interaction terms — these introduce
  researcher degrees of freedom not covered by this synthesis.
- A 2×2 table (M₁_high/low × M₂_high/low) is permitted as a secondary
  informational display; only the target-cell E-008 test is the primary outcome.
- HYPOTHESIS_exp004.md and analyze_exp004.py must be committed before
  analyze_exp004.py is run.
