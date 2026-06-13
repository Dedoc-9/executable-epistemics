# EXP-005 Aggregate Result — Wave-1 T-Cell Enrichment Test

**Claim class**: E-008-consistent retrocompute moderator test.
Per E-005, per-repo classifications are intermediate data only.

---

## Population

- EXP-005 (wave-1): n=20 repos (studies/population/REPO_DECLARATION.json,
  chain_hash 13076c4084f9d9cb)
- EXP-002 (reference): n=50 repos, T-cell count fixed at 11/50=0.22
  (AGGREGATE_exp004.md, commit 659bb06)
- Moderators: studies/exp005_wave1_moderators/moderators_exp005.json (this run,
  script hash c23785200e79467b)
- Thresholds (frozen from EXP-003, commit 4e809c8):
  M₁ > 0.858675 AND M₂ < 7.702891

---

## T-cell classification: wave-1

| id | slug | M₁ | M₂ | cell |
|---|---|---|---|---|
| W1_scipy | scipy/scipy | 0.8937 | 6.98 | T |
| W1_matplotlib | matplotlib/matplotlib | 0.9260 | 7.17 | T |
| W1_django | django/django | 0.8739 | 6.27 | T |
| W1_pytest | pytest-dev/pytest | 0.8976 | 4.61 | T |
| W1_sqlalchemy | sqlalchemy/sqlalchemy | 0.9442 | 4.67 | T |
| W1_mypy | python/mypy | 0.9030 | 7.45 | T |
| W1_pip | pypa/pip | 0.8879 | 4.66 | T |
| W1_numpy | numpy/numpy | 0.9056 | 8.06 | non-T (M₂ > threshold) |
| W1_pandas | pandas-dev/pandas | 0.8616 | 9.79 | non-T (M₂ > threshold) |
| W1_scikit-learn | scikit-learn/scikit-learn | 0.8551 | 9.61 | non-T (M₁ < threshold) |
| W1_sympy | sympy/sympy | 0.8687 | 18.76 | non-T (M₂ > threshold) |
| W1_flask | pallets/flask | 0.8221 | 9.11 | non-T (M₁ < threshold) |
| W1_requests | psf/requests | 0.8356 | 21.71 | non-T (both) |
| W1_click | pallets/click | 0.8225 | 9.83 | non-T (both) |
| W1_sphinx | sphinx-doc/sphinx | 0.9298 | 7.91 | non-T (M₂ > threshold) |
| W1_celery | celery/celery | 0.8646 | 9.40 | non-T (M₂ > threshold) |
| W1_tornado | tornadoweb/tornado | 0.8758 | 10.03 | non-T (M₂ > threshold) |
| W1_Pillow | python-pillow/Pillow | 0.9440 | 9.21 | non-T (M₂ > threshold) |
| W1_fastapi | fastapi/fastapi | 0.8576 | 3.41 | non-T (M₁ < threshold by 0.001075) |
| W1_black | psf/black | 0.7233 | 4.78 | non-T (M₁ < threshold) |

**Wave-1 T-cell count: k₁ = 7, n₁ = 20, rate = 0.3500**

---

## Primary test: Fisher exact (one-sided)

2×2 table:

|          | T-cell | non-T | total |
|----------|--------|-------|-------|
| wave-1   |   7    |  13   |  20   |
| EXP-002  |  11    |  39   |  50   |
| total    |  18    |  52   |  70   |

- Odds ratio: 1.9091
- p one-sided (wave-1 > EXP-002): **0.2039**
- p two-sided: 0.3641
- Expected value under null: E[X] = 20 × 18/70 = 5.14

**Primary outcome: NOT_CONFIRMED** (p=0.204 ≥ 0.05)

Success condition: one-sided Fisher exact p < 0.05. Condition not met.

---

## Interpretation bounds (per protocol)

The direction is consistent with H₅: wave-1 rate 0.350 > EXP-002 rate 0.220,
OR=1.91. The test is underpowered at n₁=20 to resolve this direction at p<0.05.
The null (equal T-cell proportions) cannot be rejected.

This result neither confirms nor refutes Account A (selection bias). The enrichment
direction is correct; the evidence is insufficient.

---

## Margin note: fastapi threshold proximity

fastapi M₁ = 0.8576, threshold = 0.858675, delta = −0.001075 (non-T by 0.1%).
Under the preregistered strict threshold (M₁ > 0.858675), fastapi is non-T.
If fastapi were T-cell: k₁=8/20=0.40, p_one-sided ≈ 0.079 — still not significant.
Nearest significant threshold: k₁ ≥ 10/20=0.50 → p ≈ 0.005. Not achieved.

---

## Protocol compliance

- Thresholds fixed at EXP-003 values (commit 4e809c8); not recalibrated.
- Script hash verified: c23785200e79467b (E-015, E-016 pre-execution errata).
- No score_ownership.json consulted during moderator computation.
- EXP-002 T-cell count (11/50) used as fixed reference; not recomputed.
- Forbidden interpretations: post_hoc_threshold_shift, clone_cherry_pick,
  two_sided_retest.
