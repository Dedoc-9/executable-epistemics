# HYPOTHESIS — EXP-004 Joint Threshold Study

**Preregistration status**: COMMITTED before any execution of analyze_exp004.py.
**Gate commit must include**: SYNTHESIS_EXP003.md, this file, analyze_exp004.py.

---

## 1. Research question

EXP-002 (n=50, ownership family) returned REJECTED (17/50=0.340). EXP-003 found Gini
coefficient (M₁) does not moderate DETECTED rate above E-008 threshold
(REJECTED_CONDITIONAL, H-stratum: 10/25=0.400). However, the 2×2 cell breakdown
in EXP-003 reveals that high-M₁ repos with simultaneously high M₂ (commit density)
are overrepresented among NOT_DETECTED cases (peewee M₂=17.10, marshmallow M₂=26.33).

Hypothesis: concentrated authorship (high M₁) predicts DETECTED only when commit
density (M₂ = n_commits_used / n_files) is low. High M₂ saturates the co-change
matrix, making ownership indistinguishable from baseline activity patterns regardless
of Gini concentration. The joint threshold (high M₁ AND low M₂) identifies repos
where concentrated authorship manifests as targeted, specialized file-editing
rather than bulk co-change.

---

## 2. Population

- EXP-002 cohort: n=50 repos (REPO_DECLARATION_exp002.json, declaration_hash
  13ffc9a71c3fda50471592c22c9f209448b7c66082eeeeb76b3ac4e230f68a0e)
- Moderator values: studies/exp003_moderator/moderators_exp003.json (commit 4e809c8)
- Score files: results_exp002/*/score_ownership.json (E-005: per-repo = intermediate data)

---

## 3. Moderator definitions (frozen at commit 4e809c8)

| symbol | name | formula |
|---|---|---|
| M₁ | Gini coefficient | (2·Σ(i+1)·cᵢ)/(n·Σcᵢ) − (n+1)/n, c sorted ascending |
| M₂ | commit density | n_commits_used / n_files (observation_window) |

Medians computed mechanically from moderators_exp003.json (n=50 each):

- M₁_median = 0.858675
- M₂_median = 7.702891

Thresholds are fixed. analyze_exp004.py recomputes them from moderators_exp003.json;
any discrepancy indicates a data integrity violation.

---

## 4. Preregistered hypothesis

**H₄**: P(DETECTED | M₁ > M₁_median AND M₂ < M₂_median) ≥ 0.60

Target cell T = {repos: M₁ > M₁_median AND M₂ < M₂_median}
Expected cell size: n_T ≈ 11–13 (mechanical count from moderators_exp003.json).

---

## 5. Success criterion

| outcome | condition |
|---|---|
| VALIDATED_CONDITIONAL | E-008 on T: k_T/n_T ≥ 0.60 AND Wilson_upper_T > 0.40 |
| REJECTED_CONDITIONAL  | Wilson_upper_T < 0.60 |
| INCONCLUSIVE          | neither above |

Minimum interpretable cell: n_T ≥ 8. If n_T < 8 the primary test is UNDERPOWERED
and no conditional claim is made.

**Aggregate campaign outcome** if VALIDATED_CONDITIONAL:
The joint threshold (concentrated AND sparse) is a candidate moderator explaining
the EXP-001 VALIDATED / EXP-002 REJECTED divergence. This does not retroactively
validate EXP-002; it specifies a substructure of the population where the signal holds.

---

## 6. Analysis script

- File: studies/exp004_joint_threshold/analyze_exp004.py
- SHA-256: 2f115f3c3894f4741e1f7fd5ca422fe293bc7b0f471b16c69791cec8eac5de38
- Inputs: moderators_exp003.json, results_exp002/*/score_ownership.json
- Output: studies/exp004_joint_threshold/AGGREGATE_exp004.md
- No new compute script required (M₁, M₂ already committed at 4e809c8)

Execution order: analyze_exp004.py (single script, reads precommitted data)

---

## 7. Forbidden procedures (UPDATE_COMMITMENTS_exp004.md)

- post_hoc_threshold_shift: adjusting M₁_median or M₂_median after seeing AGGREGATE_exp004.md
- cell_cherry_pick: reporting a 2×2 sub-cell result as the primary outcome
- retroactive_moderator_add: introducing M₃ or M₄ after execution
- verdict_field_in_artifact: no verdict field in any committed file
- per_repo_outcome_report: E-005 prohibition on individual repo classifications

---

## 8. Commitment chain

EXP-001 (VALIDATED) → EXP-002 (REJECTED) → EXP-003 (REJECTED_CONDITIONAL, M₁ alone)
→ EXP-004 (preregistered: joint threshold M₁ × M₂)

SYNTHESIS_EXP003.md characterizes the EXP-003 result and motivates EXP-004.
This file and analyze_exp004.py must be committed before any analysis is run.

---

*Preregistration hash (informational): SHA-256 over this file + analyze_exp004.py
committed simultaneously in EXP-004 gate commit.*
