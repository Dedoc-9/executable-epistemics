# SYNTHESIS — EXP-102 (Series 200)

**Status**: CLOSED — REJECTED
**Date**: 2026-06-13
**Declaration hash (final)**: bfa3f2a9b15a565cb52c27c888881f9b1e22e7c6ac6afe9c1b68a3301fb850d5 (E-029)

---

## 1. Outcome

| quantity       | value                                   |
|----------------|-----------------------------------------|
| n_declared     | 100                                     |
| n_computed     | 100                                     |
| n_D_T          | 27                                      |
| k_D_T          | 7                                       |
| rate           | 0.2593                                  |
| Wilson_lower   | 0.1317                                  |
| Wilson_upper   | 0.4468                                  |
| z              | 1.96 (95%)                              |
| outcome        | REJECTED                                |

**Rejection condition**: Wilson_upper = 0.4468 < 0.60 threshold (preregistered, HYPOTHESIS_exp102.md §6).

---

## 2. Implication (preregistered)

The ownership instrument (M1 > 0.858675 AND M2 < 7.702891) is retired as a generalizable claim class.

The true detection rate in the T-cell space is bounded below 0.60 with high confidence:
Wilson_upper = 0.447 establishes that, at 95% confidence, the rate does not reach 0.60 in the
Component D population.

The EXP-001 VALIDATED result (wave-1 cohort, k/n = 0.733) is attributed to population selection
artifact: wave-1 curation bias produced a T-cell-enriched cohort unrepresentative of the general
Python open-source population. The instrument does not generalize beyond the wave-1 selection.

---

## 3. Cross-experiment state summary

| experiment | n_T | k_T | rate  | outcome             |
|------------|-----|-----|-------|---------------------|
| EXP-001    | 15  | 11  | 0.733 | VALIDATED           |
| EXP-002    | 11  | 5   | 0.455 | REJECTED            |
| EXP-003    | 11  | —   | —     | REJECTED_CONDITIONAL|
| EXP-004    | 11  | 5   | 0.455 | INCONCLUSIVE        |
| EXP-005    | —   | —   | —     | NOT_CONFIRMED       |
| EXP-101    | 20  | 8   | 0.400 | INCONCLUSIVE        |
| EXP-102    | 27  | 7   | 0.259 | **REJECTED**        |

EXP-001 is the only VALIDATED outcome across all experiments. All subsequent fresh-cohort
tests fall below the 0.60 threshold. The monotone decline from 0.733 → 0.455 → 0.400 → 0.259
across successively fresher populations is consistent with curation bias in wave-1, not
instrument validity.

---

## 4. T-cell gate coverage

n_D_T = 27/100 = 0.27. Target was ≥ 50. The lower-than-expected T-cell yield reflects
the M1∧M2 gate being calibrated on the wave-1 cohort, which over-represented
concentrated-authorship repositories relative to the general Python ecosystem.
This is itself evidence of wave-1 selection bias.

---

## 5. M3 observational note

M3 distribution (Component D, n=100): mean=0.886, min=0.444, max=1.000.
M3 retrocompute (m3_retroactive.json, commit f0be383) falsified M3 as a cohort-level mechanism.
M3 is not a justified gate. No M3 threshold was preregistered for EXP-102. M3 data archived
in moderators_exp102.json for longitudinal tracking only.

---

## 6. Errata log (EXP-102 slug corrections)

| erratum | repo_id | declared               | corrected              |
|---------|---------|------------------------|------------------------|
| E-025   | D009    | pallets/blinker        | pallets-eco/blinker    |
| E-026   | D022    | pypa/pyOpenSSL         | pyca/pyopenssl         |
| E-027   | D061    | bitarray/bitarray      | ilanschnell/bitarray   |
| E-028   | D090    | pyca/pyotp             | pyauth/pyotp           |
| E-029   | D091    | pypa/cachecontrol      | psf/cachecontrol       |

All corrections filed pre-clone. Instrument unaffected. Declaration hash chain maintained.

---

## 7. Commitment chain closed

EXP-001 VALIDATED →
EXP-002 REJECTED →
EXP-003 REJECTED_CONDITIONAL →
EXP-004 INCONCLUSIVE →
EXP-005 NOT_CONFIRMED →
EXP-101 INCONCLUSIVE →
**EXP-102 REJECTED** ← Series 200 terminus

The ownership claim class is retired. No further experiments in this series are warranted
without redefinition of the instrument or population constraints.
