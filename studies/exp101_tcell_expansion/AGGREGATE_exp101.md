# EXP-101 Aggregate Result — T-Cell Combined Pool (A + C_T)

**Claim class**: E-008 primary test on preregistered combined T-cell pool.
Per E-005, per-repo classifications are intermediate data only.

---

## Population
- Component A: n=11 (EXP-004 T-cell, committed 659bb06)
- Component C declared: n=22 (REPO_DECLARATION_exp101.json, commit 5864fb2)
- Component C_T (T-cell confirmed): n=9 (M1 > 0.858675, M2 < 7.702891)
- Combined A + C_T: n=20
- Component B (holdout, not in primary): n=7

## Primary test: k_(A+C_T) / n_(A+C_T) ≥ 0.60

| pool | n | k_DETECTED | rate | Wilson 95% CI | E-008 |
|---|---|---|---|---|---|
| A + C_T (primary) | 20 | 8 | 0.4000 | [0.2188, 0.6134] | INCONCLUSIVE |
| A only            | 11 | 5 | 0.4545 | [0.2127, 0.7199] | UNDERPOWERED |
| C_T only          | 9 | 3 | 0.3333 | [0.1206, 0.6458] | UNDERPOWERED |

**Primary outcome: INCONCLUSIVE (INCONCLUSIVE)**

Success condition: k/n ≥ 0.60 AND Wilson_upper > 0.40

## Component C T-cell classification

| id | slug | M1 | M2 | T-cell | classification |
|---|---|---|---|---|---|
| C007 | pyinvoke/invoke | 0.9617 | 17.16 | non-T | DETECTED |
| C021 | giampaolo/psutil | 0.9523 | 15.27 | non-T | NOT_DETECTED |
| C002 | cython/cython | 0.9418 | 7.49 | T | NOT_DETECTED |
| C013 | bokeh/bokeh | 0.9324 | 2.64 | T | UNRESOLVED_ACTIVITY_MARGIN |
| C008 | statsmodels/statsmodels | 0.9316 | 5.94 | T | NOT_DETECTED |
| C018 | astropy/astropy | 0.9247 | 9.13 | non-T | DETECTED |
| C003 | pyparsing/pyparsing | 0.9218 | 6.25 | T | NOT_DETECTED |
| C001 | paramiko/paramiko | 0.9212 | 12.09 | non-T | DETECTED |
| C012 | zeromq/pyzmq | 0.9203 | 6.14 | T | NOT_DETECTED |
| C005 | ipython/ipython | 0.9171 | 8.86 | non-T | DETECTED |
| C011 | numba/numba | 0.9132 | 9.61 | non-T | NOT_DETECTED |
| C017 | pyserial/pyserial | 0.9028 | 8.41 | non-T | NOT_DETECTED |
| C020 | Supervisor/supervisor | 0.8960 | 12.18 | non-T | UNRESOLVED_ACTIVITY_MARGIN |
| C010 | twisted/twisted | 0.8777 | 4.17 | T | DETECTED |
| C014 | pexpect/pexpect | 0.8751 | 6.93 | T | DETECTED |
| C015 | gitpython-developers/GitPython | 0.8734 | 12.73 | non-T | DETECTED |
| C019 | docutils/docutils | 0.8700 | 3.83 | T | UNRESOLVED_ACTIVITY_MARGIN |
| C006 | networkx/networkx | 0.8600 | 5.39 | T | DETECTED |
| C009 | joblib/joblib | 0.8565 | 8.21 | non-T | NOT_DETECTED |
| C016 | tomerfiliba/plumbum | 0.8480 | 5.40 | non-T | NOT_DETECTED |
| C022 | dateutil/dateutil | 0.8329 | 4.66 | non-T | NOT_DETECTED |
| C004 | pygments/pygments | 0.8123 | 3.59 | non-T | NOT_DETECTED |

## Component A decomposition (EXP-004 T-cell, for audit)

| id | slug | classification |
|---|---|---|
| R004 | piccolo-orm/piccolo | NOT_DETECTED |
| R036 | boto/boto3 | NOT_DETECTED |
| R028 | agronholm/apscheduler | NOT_DETECTED |
| R019 | mitmproxy/mitmproxy | DETECTED |
| R016 | aio-libs/aiohttp | DETECTED |
| R026 | coleifer/huey | NOT_DETECTED |
| R020 | tiangolo/typer | DETECTED |
| R033 | PyCQA/pylint | DETECTED |
| R005 | python-gino/gino | NOT_DETECTED |
| R045 | rubik/radon | UNRESOLVED_ACTIVITY_MARGIN |
| R034 | pre-commit/pre-commit | DETECTED |

## Component B confirmatory holdout (wave-1 T-cell, post-primary only)

| pool | n | k | rate | CI |
|---|---|---|---|---|
| B (wave-1 T-cell) | 7 | 5 | 0.7143 | [0.3589, 0.9178] |

| W1_scipy | scipy/scipy | DETECTED |
| W1_matplotlib | matplotlib/matplotlib | DETECTED |
| W1_django | django/django | UNRESOLVED_ACTIVITY_MARGIN |
| W1_pytest | pytest-dev/pytest | DETECTED |
| W1_sqlalchemy | sqlalchemy/sqlalchemy | DETECTED |
| W1_mypy | python/mypy | DETECTED |
| W1_pip | pypa/pip | LEAKAGE |

## Protocol compliance
- compute_moderators_exp101.py run before any ownership score review.
- T-cell threshold fixed: M1 > 0.858675 AND M2 < 7.702891 (commit 4e809c8).
- Component A sourced from AGGREGATE_exp004.md (commit 659bb06), not re-scored.
- Component B excluded from primary test (incorporation bias prevention).
- Forbidden interpretations: post_hoc_threshold_shift, component_b_in_primary,
  non_tcell_inflation, per_repo_outcome_report.