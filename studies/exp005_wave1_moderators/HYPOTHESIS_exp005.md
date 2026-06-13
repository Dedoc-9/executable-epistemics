# HYPOTHESIS — EXP-005 Wave-1 T-Cell Enrichment Retrocompute

**Preregistration status**: COMMITTED before any execution of compute_moderators_exp005.py.
**Gate commit must include**: this file + compute_moderators_exp005.py.

---

## 1. Research question

EXP-001 (wave-1, n=20) returned VALIDATED. EXP-002 (n=50, broader population) returned
REJECTED. EXP-003 and EXP-004 established that the joint threshold (high M₁ AND low M₂)
is the strongest predictor of DETECTED, but could not clear E-008 at T-cell power.

The remaining open question: is the EXP-001 VALIDATED result explained by the wave-1
cohort being structurally enriched in T-cell repos (high Gini concentration, low commit
density) relative to the EXP-002 general population? If yes, the EXP-001 / EXP-002
divergence is fully accounted for by selection bias in cohort composition — not by any
failure of the instrument in EXP-002 or EXP-003/004.

---

## 2. Population

- EXP-001 wave-1: n=20 repos (studies/population/REPO_DECLARATION.json,
  chain_hash 13076c4084f9d9cb)
- Moderator values computed from: results/{repo}/ground_truth.json (already committed)
  and git log from tests_epi clones (for Gini)
- Does NOT read score_ownership.json — moderator computation is score-blind

---

## 3. Thresholds (frozen from EXP-003 analysis, commit 4e809c8)

| symbol | value | provenance |
|---|---|---|
| M₁_threshold | 0.858675 | median of EXP-002 cohort M₁ values, moderators_exp003.json |
| M₂_threshold | 7.702891 | median of EXP-002 cohort M₂ values, moderators_exp003.json |

T-cell definition: M₁ > 0.858675 AND M₂ < 7.702891 (strictly greater / strictly less).
These thresholds are immutable for EXP-005. No recalibration permitted.

---

## 4. Moderator definitions (identical to EXP-003, frozen at commit f3ee2f0)

| symbol | name | formula |
|---|---|---|
| M₁ | Gini coefficient | (2·Σ(i+1)·cᵢ)/(n·Σcᵢ) − (n+1)/n, c sorted ascending (per-author commit counts within observation_window) |
| M₂ | commit density | n_commits_used / n_files (from ground_truth.json observation_window) |

---

## 5. Preregistered hypothesis

**H₅**: P(T-cell | wave-1) > P(T-cell | EXP-002)

Operationalized:
- EXP-002 T-cell count: 11/50 = 0.22 (fixed, from AGGREGATE_exp004.md, commit 659bb06)
- Wave-1 T-cell count: k₁ / n₁ (to be computed by compute_moderators_exp005.py)
- Test: one-sided Fisher exact test on the 2×2 table:

```
             T-cell    non-T    total
wave-1          k₁    n₁−k₁      n₁
EXP-002         11       39      50
```

One-sided alternative: wave-1 has a higher T-cell proportion than EXP-002.

---

## 6. Success criterion

| outcome | condition |
|---|---|
| CONFIRMED | Fisher exact one-sided p < 0.05 |
| NOT_CONFIRMED | p ≥ 0.05 |

Minimum interpretable n₁: 15 (if any wave-1 repos lack ground_truth or clone,
this threshold applies; n₁ < 15 renders the test UNDERPOWERED).

**Aggregate campaign interpretation if CONFIRMED**:
The EXP-001 VALIDATED result is explained by T-cell enrichment in the wave-1 cohort.
The instrument detects ownership at ≥60% in T-cell space; the EXP-002 general
population is not T-cell enriched (11/50=0.22), which explains the REJECTED result.
The divergence gap Δ=−0.260 is attributed to cohort selection, not instrument failure.

---

## 7. Compute script

- File: studies/exp005_wave1_moderators/compute_moderators_exp005.py
- SHA-256: a09a3ea6a1ec39e7dab8b7d453a32cb24f545911d55fbaeebcb0be92a355dff0
- E-015: display-only syntax fix (pre-execution); §C budget unchanged (3/3)
- Inputs: studies/population/REPO_DECLARATION.json, results/*/ground_truth.json,
          tests_epi/ clones (for git log)
- Output: studies/exp005_wave1_moderators/moderators_exp005.json
- Execution: single script, no analyze step required (Fisher test inline)

No analyze_exp005.py is needed — the primary test (Fisher exact) is self-contained
in the compute script output interpretation. The moderators_exp005.json output plus
the fixed EXP-002 T-cell count (11/50) are sufficient for full audit.

---

## 8. Forbidden procedures

- post_hoc_threshold_shift: any change to M₁_threshold or M₂_threshold after
  compute_moderators_exp005.py is executed
- clone_cherry_pick: excluding any wave-1 repo from the T-cell count without a
  pre-run erratum
- score_consultation: reading score_ownership.json before or during moderator compute
- two_sided_retest: switching to a two-sided test if one-sided p is 0.06–0.10

---

## 9. Commitment chain at EXP-005 gate

EXP-001 (VALIDATED) → EXP-002 (REJECTED) → EXP-003 (REJECTED_CONDITIONAL)
→ EXP-004 (INCONCLUSIVE) → EXP-005 (preregistered: T-cell enrichment test)

This is the final planned study in the campaign. SYNTHESIS_EXP004.md (commit c2ee242)
characterizes the full chain and motivates EXP-005 as the highest-information /
lowest-cost closure test.
