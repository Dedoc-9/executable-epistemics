# HYPOTHESIS — EXP-102 T-Cell Power Test (Series 200)

**Preregistration status**: GATE PENDING — commit this file + REPO_DECLARATION_exp102.json + compute_moderators_exp102.py simultaneously before any clone.
**Gate commit must include**: this file, REPO_DECLARATION_exp102.json, compute_moderators_exp102.py.

---

## 1. Research question

EXP-101 (n_T=20) produced INCONCLUSIVE: k/n=0.400, CI [0.219, 0.613]. The Wilson upper
(0.613) threads just above 0.60, preventing rejection. EXP-004 (n_T=11) was similarly
INCONCLUSIVE. Two consecutive INCONCLUSIVE outcomes at n=11 and n=20 leave the 0.60
threshold unresolved.

M3 retrocompute (m3_retroactive.json, commit f0be383) falsified the Pseudo-T hypothesis:
cohort-level M3 does not predict detection rate ordering. M3 is not a justified gate for
this experiment. EXP-102 therefore pursues Pivot A: a larger M1^M2 cohort (n_T >= 50)
to force a frequentist resolution.

**H_102**: P(DETECTED | M1 > 0.858675 AND M2 < 7.702891) >= 0.60 in a fresh T-cell cohort
of n_T >= 50, excluding all prior experiment populations.

---

## 2. Design

| parameter        | value                                                    |
|------------------|----------------------------------------------------------|
| gate             | M1 > 0.858675 AND M2 < 7.702891 (frozen from EXP-003)   |
| M3               | computed as observational metadata ONLY; not used in gate|
| n_declared       | 100 (REPO_DECLARATION_exp102.json)                       |
| n_target_tcell   | >= 50                                                    |
| scorer_hash      | cd6bf9a6c3f3ab36                                         |
| population       | fresh repos; none in EXP-001/EXP-002/EXP-101 cohorts    |
| declaration_hash | 970f4c4f330e629e5b18d0d0f5cc68cd738e7bbea8d0bc3aba4e4f54376a25ca |

Component A (EXP-002 T-cells, n=11) and Component B (wave-1 T-cell, n=7) are NOT
included in the primary test — their classifications are known and including them would
constitute cherry-picking.

---

## 3. Thresholds (frozen from EXP-003, commit 4e809c8)

| symbol        | value     | provenance                                     |
|---------------|-----------|------------------------------------------------|
| M1_threshold  | 0.858675  | median of EXP-002 cohort, moderators_exp003.json |
| M2_threshold  | 7.702891  | median of EXP-002 cohort, moderators_exp003.json |

Immutable for EXP-102.

---

## 4. Population constraints

Repos in REPO_DECLARATION_exp102.json must satisfy ALL of:
- Not in EXP-001 wave-1 (studies/population/REPO_DECLARATION.json)
- Not in EXP-002 cohort (studies/exp002_ownership_replication/REPO_DECLARATION_exp002.json)
- Not in EXP-101 Component C (studies/exp101_tcell_expansion/REPO_DECLARATION_exp101.json)
- GitHub: archived=false, primary_language=Python
- >= 500 commits (total), >= 50 tracked Python files
- Not a monorepo (< 5 distinct top-level packages)
- Scorer hash must equal cd6bf9a6c3f3ab36

Repos are scored regardless of T-cell outcome. Non-T-cell repos are excluded from the
primary test by preregistered rule; they are NOT reported individually (E-005).

---

## 5. Preregistered hypothesis

**H_102**: P(DETECTED | M1 > 0.858675 AND M2 < 7.702891, fresh cohort D) >= 0.60

Where D_T = {repos in D with M1 > 0.858675 AND M2 < 7.702891}.

---

## 6. Success criterion

| outcome      | condition                                              |
|--------------|--------------------------------------------------------|
| VALIDATED    | k_D_T / n_D_T >= 0.60 AND Wilson_upper > 0.40         |
| REJECTED     | Wilson_upper_(D_T) < 0.60                             |
| INCONCLUSIVE | neither above                                          |

Minimum interpretable n_D_T: 20.
Target n_D_T: >= 50 (sufficient for ~80% power at true rate 0.65, alpha=0.05).

**If REJECTED**: The ownership instrument (M1^M2 gate) is retired as a generalizable
claim class. The true detection rate in the T-cell space is bounded below 0.60 with
high confidence. The EXP-001 VALIDATED result is attributed to population selection
artifact (wave-1 curation bias).

**If VALIDATED**: The instrument is confirmed at n=50. The wave-1/EXP-002 divergence is
explained by T-cell enrichment in wave-1. The claim class survives for M1^M2 populations.

**If INCONCLUSIVE**: The 0.60 threshold is not resolvable at n=50. The claim class is
suspended pending further power or a redefined threshold.

---

## 7. M3 observational metadata

compute_moderators_exp102.py computes M3 (Galois closure diameter, E-018) for all repos
as longitudinal observational metadata. M3 is NOT used in T-cell classification.
M3 stored in moderators_exp102.json for cross-experiment tracking only.

M3 retrocompute finding (m3_retroactive.json, f0be383):
  B mean M3=0.911, rate=0.714
  A mean M3=0.874, rate=0.455
  C_T mean M3=0.773, rate=0.333
Detection rate and M3 co-vary in the same direction across cohorts. M3-as-mechanism
is falsified. No M3 threshold is preregistered for EXP-102.

---

## 8. Compute script

- File: studies/exp102_tcell_power/compute_moderators_exp102.py
- SHA-256: 0c3974150a22d78253b2863eab29bb4c1cfa91da07065d9ee52d82d645ce89f9
- Inputs: REPO_DECLARATION_exp102.json, results_exp102/*/ground_truth.json, tests_epi/exp102/ clones
- Output: studies/exp102_tcell_power/moderators_exp102.json

Execution order: run_batch_exp102.ps1 -> compute_moderators_exp102.py -> analyze_exp102.py

---

## 9. Forbidden procedures

- post_hoc_threshold_shift: adjusting M1/M2 thresholds after compute_moderators_exp102.py runs
- component_inclusion_of_prior_tcells: including EXP-004/EXP-101 A/B T-cells in k_D_T/n_D_T
- non_tcell_inflation: counting repos that fail M1^M2 in the primary numerator
- per_repo_outcome_report: E-005 prohibition maintained
- cherry_picked_subsets: any post-hoc sub-cell analysis reported as primary
- m3_gate_retroactive: applying any M3 threshold post-hoc to EXP-102 T-cell classification

---

## 10. Commitment chain

EXP-001 VALIDATED -> EXP-002 REJECTED -> EXP-003 REJECTED_CONDITIONAL ->
EXP-004 INCONCLUSIVE -> EXP-005 NOT_CONFIRMED -> EXP-101 INCONCLUSIVE ->
EXP-102 (M1^M2 power test, n_T >= 50, Pivot A, Series 200)
