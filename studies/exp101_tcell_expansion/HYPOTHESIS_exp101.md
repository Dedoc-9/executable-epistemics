# HYPOTHESIS — EXP-101 T-Cell Targeted Expansion (Series 100)

**Preregistration status**: GATE PENDING — commit this file + REPO_DECLARATION_exp101.json + compute_moderators_exp101.py simultaneously before any clone.
**Gate commit must include**: this file, REPO_DECLARATION_exp101.json,
compute_moderators_exp101.py.

---

## 1. Research question

EXP-004 established that the joint threshold (M₁ > 0.858675 AND M₂ < 7.702891)
produces a detection rate of 0.455 (CI [0.213, 0.720], INCONCLUSIVE) in n=11 T-cell
repos from the EXP-002 cohort. EXP-005 found that EXP-001 wave-1 is directionally
T-cell enriched (OR=1.91) but the test was underpowered (p=0.204, n=20).

EXP-101 asks: in a powered T-cell population (n≥33), does the ownership instrument
achieve P(DETECTED | T-cell) ≥ 0.60?

---

## 2. Combined pool design

| component | source | n | ownership scores |
|---|---|---|---|
| A | EXP-004 T-cell repos (committed 659bb06) | 11 | results_exp002/*/score_ownership.json |
| C | EXP-101 new repos (REPO_DECLARATION_exp101.json) | n_C (post-audit) | to be scored |

**Component B exclusion**: EXP-001 wave-1 T-cell repos (n=7, moderators_exp005.json)
are EXCLUDED from the primary test to prevent incorporation bias (wave-1 contributed
to EXP-001 VALIDATED; including known-positive repos would undermine the test).
Component B is reserved as a confirmatory holdout after primary result is known.

Primary test population: A ∪ C, where T-cell membership for C is confirmed by
M₁ > 0.858675 AND M₂ < 7.702891 (computed by compute_moderators_exp101.py,
committed in gate, run before ownership scoring).

---

## 3. Thresholds (frozen from EXP-003, commit 4e809c8)

| symbol | value | provenance |
|---|---|---|
| M₁_threshold | 0.858675 | median of EXP-002 cohort, moderators_exp003.json |
| M₂_threshold | 7.702891 | median of EXP-002 cohort, moderators_exp003.json |

Thresholds are immutable for EXP-101.

---

## 4. Population constraints for Component C

Repos in REPO_DECLARATION_exp101.json must satisfy ALL of:
- Not in EXP-001 wave-1 (studies/population/REPO_DECLARATION.json)
- Not in EXP-002 cohort (studies/exp002_ownership_replication/REPO_DECLARATION_exp002.json)
- GitHub: archived=false, primary_language=Python
- ≥500 commits (total), ≥50 tracked Python files
- Not a monorepo (< 5 distinct top-level packages)
- Scorer hash must equal cd6bf9a6c3f3ab36 (no instrument changes between series)

Component C repos are scored regardless of T-cell outcome. Non-T-cell repos in C are
reported in the campaign record but excluded from the primary test by preregistered rule.

---

## 5. Preregistered hypothesis

**H₁₀₁**: P(DETECTED | M₁ > 0.858675 AND M₂ < 7.702891, A ∪ C_T) ≥ 0.60

Where C_T = {repos in Component C with M₁ > 0.858675 AND M₂ < 7.702891}.

---

## 6. Success criterion

| outcome | condition |
|---|---|
| VALIDATED | k_(A+C_T) / n_(A+C_T) ≥ 0.60 AND Wilson_upper > 0.40 |
| REJECTED | Wilson_upper_(A+C_T) < 0.60 |
| INCONCLUSIVE | neither above |

Minimum interpretable n_(A+C_T): 20.
Target n_(A+C_T): ≥ 33 (sufficient for 80% power at true rate 0.65, α=0.05).

**Aggregate campaign interpretation if VALIDATED**:
The ownership instrument reliably detects concentrated authorship in T-cell repos
(high Gini, low commit density). The EXP-001/EXP-002 divergence is explained by
T-cell enrichment in EXP-001 wave-1. The instrument is a high-fidelity signal
for flagship/dominant-author architectures and is not a general-purpose population metric.

---

## 7. Compute script

- File: studies/exp101_tcell_expansion/compute_moderators_exp101.py
- SHA-256: 8c0d3236490093b9a27dea0c70a2837e013cf23efcf0fd34ba98804415a58547
- Inputs: REPO_DECLARATION_exp101.json, results_exp101/*/ground_truth.json,
          tests_epi/exp101/ clones (for git log)
- Output: studies/exp101_tcell_expansion/moderators_exp101.json
- Must run BEFORE ownership scoring begins

Execution order: compute_moderators_exp101.py → run_batch_exp101.ps1 → analyze_exp101.py

---

## 8. Confirmatory holdout (post-primary)

After primary test result is known and committed, Component B (EXP-001 wave-1 T-cell,
n=7: scipy, matplotlib, django, pytest, sqlalchemy, mypy, pip) may be examined as
a confirmatory holdout. This is informational only and does not alter the primary
outcome. Component B examination requires a separate post-primary commit.

---

## 9. Instrument continuity

scorer.py hash must equal cd6bf9a6c3f3ab36 for all Component C scoring.
Any instrument change requires a new erratum and re-declaration.

---

## 10. Forbidden procedures

- post_hoc_threshold_shift: adjusting M₁/M₂ thresholds after compute_moderators_exp101.py runs
- component_b_in_primary: including wave-1 T-cell repos in k_(A+C_T) / n_(A+C_T)
- non_tcell_inflation: counting repos that fail M₁/M₂ criterion in the primary numerator
- per_repo_outcome_report: E-005 prohibition maintained
- cherry_picked_subsets: any post-hoc sub-cell analysis reported as primary

---

## 11. Commitment chain

EXP-001 VALIDATED → EXP-002 REJECTED → EXP-003 REJECTED_CONDITIONAL →
EXP-004 INCONCLUSIVE → EXP-005 NOT_CONFIRMED → EXP-101 (primary T-cell power test)
