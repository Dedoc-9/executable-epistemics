# EXP-004 Aggregate Result — Joint Threshold (M₁ × M₂)

**Claim class**: E-008-consistent moderator analysis (joint threshold).
Per E-005, per-repo classifications are intermediate data only.

---

## Population
- n = 50 repos (EXP-002 cohort; moderator data from moderators_exp003.json 4e809c8)
- M₁ median = 0.858675  (Gini threshold)
- M₂ median = 7.702891  (density threshold)
- Baseline success_rate: 0.3400 (EXP-002 REJECTED)

## Primary test: target cell T (high M₁ AND low M₂)

| cell | label | n | k_DETECTED | rate | Wilson 95% CI | E-008 |
|---|---|---|---|---|---|---|
| T  | high M₁, low M₂  | 11  | 5  | 0.4545 | [0.2127, 0.7199] | INCONCLUSIVE |
| NT | all others        | 39 | 12 | 0.3077 | [0.1857, 0.4642] | REJECTED |

**Primary outcome: INCONCLUSIVE (INCONCLUSIVE)**

Success condition: P(DETECTED | T) ≥ 0.60 AND Wilson_upper(T) > 0.40

## 2×2 informational table

| cell | M₁ | M₂ | n | k | rate | CI |
|---|---|---|---|---|---|---|
| T | high | low | 11 | 5 | 0.4545 | [0.2127, 0.7199] |
| Hd | high | high | 14 | 5 | 0.3571 | [0.1634, 0.6124] |
| Ls | low | low | 14 | 4 | 0.2857 | [0.1172, 0.5465] |
| Ld | low | high | 11 | 3 | 0.2727 | [0.0975, 0.5657] |

## M₁ × M₂ distribution (target cell T marked)

| id | slug | M₁ | M₂ | cell | classification |
|---|---|---|---|---|---|
| R002 | coleifer/peewee | 0.9555 | 17.10 | Hd | NOT_DETECTED |
| R003 | ponyorm/pony | 0.9504 | 8.27 | Hd | NOT_DETECTED |
| R038 | pyca/cryptography | 0.9466 | 11.84 | Hd | DETECTED |
| R004 | piccolo-orm/piccolo | 0.9415 | 3.11 | T | NOT_DETECTED |
| R036 | boto/boto3 | 0.9404 | 0.43 | T | NOT_DETECTED |
| R039 | HypothesisWorks/hypothesis | 0.9347 | 13.21 | Hd | DETECTED |
| R006 | psycopg/psycopg2 | 0.9240 | 8.72 | Hd | NOT_DETECTED |
| R028 | agronholm/apscheduler | 0.9194 | 5.84 | T | NOT_DETECTED |
| R012 | python-jsonschema/jsonschema | 0.9066 | 9.61 | Hd | NOT_DETECTED |
| R019 | mitmproxy/mitmproxy | 0.9053 | 4.31 | T | DETECTED |
| R047 | mongodb/motor | 0.9051 | 9.09 | Hd | DETECTED |
| R016 | aio-libs/aiohttp | 0.9043 | 7.35 | T | DETECTED |
| R026 | coleifer/huey | 0.9032 | 6.78 | T | NOT_DETECTED |
| R035 | pypa/setuptools | 0.8984 | 9.57 | Hd | NOT_DETECTED |
| R020 | tiangolo/typer | 0.8973 | 3.95 | T | DETECTED |
| R023 | tqdm/tqdm | 0.8895 | 13.22 | Hd | NOT_DETECTED |
| R033 | PyCQA/pylint | 0.8820 | 1.91 | T | DETECTED |
| R005 | python-gino/gino | 0.8774 | 4.69 | T | NOT_DETECTED |
| R010 | marshmallow-code/marshmallow | 0.8731 | 26.33 | Hd | NOT_DETECTED |
| R021 | httpie/httpie | 0.8708 | 7.97 | Hd | NOT_DETECTED |
| R034 | pre-commit/pre-commit | 0.8644 | 4.88 | T | DETECTED |
| R045 | rubik/radon | 0.8618 | 5.76 | T | UNRESOLVED_ACTIVITY_MARGIN |
| R022 | Textualize/rich | 0.8608 | 8.12 | Hd | DETECTED |
| R029 | PyCQA/isort | 0.8607 | 14.03 | Hd | NOT_DETECTED |
| R011 | pyeve/cerberus | 0.8597 | 12.35 | Hd | DETECTED |
| R030 | PyCQA/flake8 | 0.8576 | 6.47 | Ls | NOT_DETECTED |
| R017 | pallets/werkzeug | 0.8548 | 9.79 | Ld | DETECTED |
| R025 | Bogdanp/dramatiq | 0.8514 | 5.93 | Ls | NOT_DETECTED |
| R008 | MagicStack/asyncpg | 0.8508 | 5.49 | Ls | NOT_DETECTED |
| R048 | elastic/elasticsearch-py | 0.8489 | 3.10 | Ls | DETECTED |
| R009 | pydantic/pydantic | 0.8368 | 3.21 | Ls | DETECTED |
| R015 | falconry/falcon | 0.8302 | 2.99 | Ls | DETECTED |
| R001 | tortoise/tortoise-orm | 0.8263 | 3.14 | Ls | DETECTED |
| R032 | PyCQA/pycodestyle | 0.8132 | 10.74 | Ld | NOT_DETECTED |
| R037 | urllib3/urllib3 | 0.8055 | 8.86 | Ld | NOT_DETECTED |
| R044 | mkdocs/mkdocs | 0.8052 | 4.91 | Ls | UNRESOLVED_ACTIVITY_MARGIN |
| R018 | encode/httpx | 0.7953 | 7.55 | Ls | NOT_DETECTED |
| R046 | jazzband/pip-tools | 0.7887 | 7.85 | Ld | DETECTED |
| R040 | joke2k/faker | 0.7649 | 5.20 | Ls | LEAKAGE |
| R027 | taskiq-python/taskiq | 0.7637 | 1.71 | Ls | NOT_DETECTED |
| R049 | Pylons/colander | 0.7624 | 9.72 | Ld | NOT_DETECTED |
| R031 | PyCQA/bandit | 0.7609 | 3.02 | Ls | LEAKAGE |
| R043 | kevin1024/vcrpy | 0.7557 | 8.63 | Ld | DETECTED |
| R013 | encode/starlette | 0.7530 | 9.13 | Ld | NOT_DETECTED |
| R024 | rq/rq | 0.7471 | 10.77 | Ld | NOT_DETECTED |
| R007 | redis/redis-py | 0.7344 | 6.36 | Ls | NOT_DETECTED |
| R014 | sanic-org/sanic | 0.7339 | 4.28 | Ls | NOT_DETECTED |
| R041 | getsentry/responses | 0.7100 | 15.37 | Ld | NOT_DETECTED |
| R050 | arrow-py/arrow | 0.6838 | 14.21 | Ld | NOT_DETECTED |
| R042 | spulec/freezegun | 0.6488 | 11.82 | Ld | NOT_DETECTED |

## Protocol compliance
- analyze_exp004.py hash verified against HYPOTHESIS_exp004.md before execution.
- Thresholds (M₁_median, M₂_median) computed mechanically from moderators_exp003.json.
- No per-repo outcome data examined before thresholds were computed.
- Forbidden interpretations: geometry_truth, causal_coupling, design_quality.