# SYNTHESIS — EXP-101 T-Cell Targeted Expansion (Series 100 Closure)

**Date**: 2026-06-13
**Commit chain**: EXP-001 → EXP-002 → EXP-003 → EXP-004 → EXP-005 → EXP-101
**Primary outcome**: INCONCLUSIVE

---

## 1. Result

EXP-101 primary test (E-008, preregistered HYPOTHESIS_exp101.md commit 5864fb2):

| pool | n | k_DETECTED | rate | Wilson 95% CI | outcome |
|---|---|---|---|---|---|
| A + C_T (primary) | 20 | 8 | 0.400 | [0.219, 0.613] | **INCONCLUSIVE** |

Success condition: k/n >= 0.60 AND Wilson_upper > 0.40.
INCONCLUSIVE rule: point < 0.60 AND Wilson_upper >= 0.60 — insufficient n to decide.

The Wilson upper (0.613) crosses the 0.60 threshold, so the hypothesis that the true
detection rate in T-cell repos is >= 0.60 cannot be rejected. But the point estimate
(0.400) is well below it. The test is underpowered.

---

## 2. Population accounting

- Component A: 11 EXP-002 T-cell repos (EXP-004, committed 659bb06)
- Component C declared: 22 repos (REPO_DECLARATION_exp101.json)
  - Slug errors resolved via errata E-017, E-019–E-023 (7 total, all pre-clone)
  - C_T (T-cell by M1^M2): 9/22
- Combined A + C_T: n = 20 (minimum interpretable; target was >= 33)
- Component B: 7 wave-1 T-cells, excluded from primary (incorporation bias)

---

## 3. Campaign summary (Series 100)

| study | population | n | k | rate | outcome |
|---|---|---|---|---|---|
| EXP-001 | wave-1 repos (general) | 20 | 12 | 0.600 | VALIDATED |
| EXP-002 | EXP-002 general | 50 | ~18 | ~0.360 | REJECTED |
| EXP-003 | EXP-002 (Ld/Ls families) | 50 | -- | -- | REJECTED_CONDITIONAL |
| EXP-004 | EXP-002 T-cell subset | 11 | 5 | 0.455 | INCONCLUSIVE |
| EXP-005 | wave-1 T-cell enrichment | 20 | -- | -- | NOT_CONFIRMED |
| EXP-101 | combined T-cell A+C | 20 | 8 | 0.400 | INCONCLUSIVE |

The campaign has consistently produced INCONCLUSIVE results at T-cell scale. Two
consecutive INCONCLUSIVE outcomes (EXP-004 and EXP-101) at n=11 and n=20 indicate
that the true detection rate in the M1^M2 T-cell space is in the range 0.30–0.61,
with the Wilson upper repeatedly threading just above the 0.60 threshold.

---

## 4. Component B post-primary signal (informational only)

Per HYPOTHESIS_exp101.md, Component B (wave-1 T-cell, n=7) was examined after the
primary outcome was committed and is informational only — it does not alter the
primary INCONCLUSIVE result.

| pool | n | k | rate | CI |
|---|---|---|---|---|
| B wave-1 T-cell | 7 | 5 | 0.714 | [0.359, 0.918] |

Component B rate (0.714) is substantially higher than Component A (0.455) or C_T (0.333).
This is consistent with EXP-001's VALIDATED result, which was entirely wave-1.
The B cohort was not used for any primary test in this series due to incorporation bias
(these repos contributed to EXP-001 VALIDATED).

---

## 5. M3 (Galois closure diameter) — observational metadata (E-018)

compute_moderators_exp101.py (E-018, E-024) computed M3 for all Component C repos.
M3 is NOT a T-cell classification criterion in EXP-101; it is observational metadata
for EXP-102 preregistration.

| component | n_tcell | n_pseudo_T (M3>0.4) | n_pure_T (M3<=0.4) |
|---|---|---|---|
| C | 9 | 8 | 1 |

The sole pure T-cell in Component C is C019 docutils/docutils (M3=0.2129).
M3 distribution across all 22 C repos: mean=0.850, min=0.213, max=0.975.

Detection rate decomposition by cohort:

| cohort | n | rate | M3 profile |
|---|---|---|---|
| B wave-1 T-cell (post-primary) | 7 | 0.714 | M3 not computed |
| A EXP-002 T-cell | 11 | 0.455 | M3 not computed |
| C_T EXP-101 T-cell | 9 | 0.333 | 8/9 pseudo-T (M3>0.4) |

The descending detection rate (0.714 > 0.455 > 0.333) as cohorts expand away from
the wave-1 population is consistent with the hypothesis that M3 contaminates the
M1^M2 T-cell gate: the wave-1 cohort likely contains more structurally exclusive
(low M3) repos than the EXP-002 or EXP-101 C populations.

This cannot be confirmed without computing M3 for Components A and B. That computation
is a preregistration target for EXP-102.

---

## 6. Interpretation constraints

Per E-005, per-repo classifications are intermediate data only. AGGREGATE_exp101.md
contains the intermediate table for audit purposes; the rates reported above are the
only interpretable aggregate quantities.

Forbidden interpretations (per HYPOTHESIS_exp101.md and REPO_DECLARATION_exp101.json):
- post_hoc_threshold_shift (M3 threshold not preregistered for EXP-101)
- component_b_in_primary
- non_tcell_inflation
- cherry_picked_subsets

---

## 7. EXP-102 design brief (Series 300 opening)

The M3 evidence motivates a Pure T-cell test:

**Proposed T-cell definition for EXP-102**:
  Pure T-cell: M1 > 0.858675 AND M2 < 7.702891 AND M3 < threshold_102

**Threshold for M3**: to be preregistered based on EXP-101 M3 distribution.
Candidate: M3 < 0.40 (which would select C019 docutils from Component C, and
potentially ~25-35% of wave-1 repos if they follow a similar distribution).

**Population requirement**: n_pure_T >= 33 (same power target as EXP-101).
This requires new candidate repos with low-M3 ownership structure — typically
single-author tools, domain-specific libraries, or small-team projects where
one contributor holds clear majority ownership across uncontested file domains.

**Key preregistration gates for EXP-102**:
1. M3 threshold fixed from EXP-101 distribution (M3 mean=0.850, min=0.213)
2. M3 computed for Components A and B (retrospective, informational)
3. Declaration committed before any new clone

---

## 8. Commitment chain

EXP-001 VALIDATED (wave-1, n=20)
  -> EXP-002 REJECTED (general pop, n=50)
  -> EXP-003 REJECTED_CONDITIONAL (Ld/Ls families)
  -> EXP-004 INCONCLUSIVE (T-cell, n=11)
  -> EXP-005 NOT_CONFIRMED (wave-1 enrichment, p=0.204)
  -> EXP-101 INCONCLUSIVE (T-cell A+C, n=20)
  -> EXP-102 [Pure T-cell, M1^M2^M3, n>=33] (Series 300, to be preregistered)

The Series 100 campaign closes INCONCLUSIVE. The instrument is not falsified.
The M1^M2 T-cell gate is insufficient at n=20. The M3 moderator is the highest-
information next test for isolating the structural signature the instrument is
detecting.
