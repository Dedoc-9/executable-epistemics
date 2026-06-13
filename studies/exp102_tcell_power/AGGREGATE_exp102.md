# AGGREGATE RESULT — EXP-102 Component D (Series 200)

**Study**: EXP-102 T-Cell Power Test (Pivot A)
**Analysis date**: 2026-06-13T23:38:51.705106+00:00
**Declaration hash**: see REPO_DECLARATION_exp102.json
**Scorer hash**: cd6bf9a6c3f3ab36

---

## Result

| metric         | value                                      |
|----------------|--------------------------------------------|
| n_declared     | 100                                        |
| n_computed     | 100                                       |
| n_D_T          | 27 (T-cell repos: M1 > 0.858675 AND M2 < 7.702891) |
| k_D_T          | 7 (DETECTED in T-cell subset)          |
| rate           | 0.2593                                  |
| Wilson lower   | 0.1317                               |
| Wilson upper   | 0.4468                               |
| Wilson center  | 0.2892                              |

## Outcome

**REJECTED**

Wilson_upper=0.4468 < 0.60 rejection threshold

## Implication

The ownership instrument (M1^M2 gate) is RETIRED as a generalizable claim class. True detection rate in T-cell space is bounded below 0.60 with high confidence. EXP-001 VALIDATED result is attributed to population selection artifact (wave-1 curation bias).

## Power note

n_D_T=27 < target 50. Power to detect true rate 0.65 at alpha=0.05 is approximately 0.95 (underpowered). Result is valid but confidence intervals are wide.

## Classification breakdown (T-cell subset, n=27)

| classification          | count |
|-------------------------|-------|
| DETECTED                | 7    |
| NOT_DETECTED            | 19   |
| LEAKAGE                 | 0    |
| UNRESOLVED_ACTIVITY_MARGIN | 1 |

LEAKAGE and UNRESOLVED_ACTIVITY_MARGIN count toward denominator (n_D_T)
but not toward numerator (k_D_T). Per preregistered protocol.

## Commitment chain

EXP-001 VALIDATED → EXP-002 REJECTED → EXP-003 REJECTED_CONDITIONAL →
EXP-004 INCONCLUSIVE → EXP-005 NOT_CONFIRMED → EXP-101 INCONCLUSIVE →
**EXP-102 REJECTED** (M1^M2 power test, n_D_T=27, Series 200)

## M3 distribution (observational, no classification effect)

mean=0.885965  min=0.444444  max=1.0  n=100

(M3 retrocompute f0be383 falsified M3 as cohort-level mechanism. No M3 threshold preregistered.)

## Forbidden interpretations

- post_hoc_threshold_shift
- component_inclusion_of_prior_tcells
- non_tcell_inflation
- per_repo_outcome_report (E-005)
- cherry_picked_subsets
- m3_gate_retroactive
