# EXP-003 Aggregate Result — Ownership Moderator Analysis (M₁/M₂)

**Claim class**: E-008-consistent moderator analysis. Per E-005,
per-repo classifications are intermediate data. The aggregate outcomes
below are the only reportable results of EXP-003.

---

## Population
- n = 50 repos (EXP-002 cohort, declaration hash 13ffc9a71c3fda50471592c22c9f209448b7c66082eeeeb76b3ac4e230f68a0e)
- Rows excluded (M1 unavailable or clone missing): 0
- DETECTED: 17/50
- Baseline success_rate: 0.3400 (EXP-002 REJECTED)

## Primary test: M₁ (Gini) median split

M₁ median = 0.858675

| stratum | n | k_DETECTED | rate | Wilson 95% CI | E-008 outcome |
|---|---|---|---|---|---|
| H (M₁ > median) | 25 | 10 | 0.4000 | [0.2340, 0.5926] | REJECTED |
| L (M₁ ≤ median) | 25 | 7 | 0.2800 | [0.1428, 0.4758] | REJECTED |

**Primary outcome: REJECTED_CONDITIONAL**

Success condition (preregistered):
  k_H / n_H ≥ 0.60 AND Wilson_upper(H) > 0.40

## Secondary test: point-biserial correlation r(M₁, DETECTED)

r_pb = 0.2182   p (one-tailed, H_alt: r > 0) = 0.0640   α = 0.05
Result: NOT SIGNIFICANT at α=0.05

## M₂ (commit density) — informational secondary

M₂ median = 7.7029
k_DETECTED in H stratum (M₂ > median): 8/25
k_DETECTED in L stratum (M₂ ≤ median): 9/25
r_pb(M₂, DETECTED) = -0.1812   p (one-tailed) = 0.8960

## M₁ distribution

| id | slug | M₁_gini | M₂_density | classification |
|---|---|---|---|---|
| R002 | coleifer/peewee | 0.9555 | 17.10 | NOT_DETECTED |
| R003 | ponyorm/pony | 0.9504 | 8.27 | NOT_DETECTED |
| R038 | pyca/cryptography | 0.9466 | 11.84 | DETECTED |
| R004 | piccolo-orm/piccolo | 0.9415 | 3.11 | NOT_DETECTED |
| R036 | boto/boto3 | 0.9404 | 0.43 | NOT_DETECTED |
| R039 | HypothesisWorks/hypothesis | 0.9347 | 13.21 | DETECTED |
| R006 | psycopg/psycopg2 | 0.9240 | 8.72 | NOT_DETECTED |
| R028 | agronholm/apscheduler | 0.9194 | 5.84 | NOT_DETECTED |
| R012 | python-jsonschema/jsonschema | 0.9066 | 9.61 | NOT_DETECTED |
| R019 | mitmproxy/mitmproxy | 0.9053 | 4.31 | DETECTED |
| R047 | mongodb/motor | 0.9051 | 9.09 | DETECTED |
| R016 | aio-libs/aiohttp | 0.9043 | 7.35 | DETECTED |
| R026 | coleifer/huey | 0.9032 | 6.78 | NOT_DETECTED |
| R035 | pypa/setuptools | 0.8984 | 9.57 | NOT_DETECTED |
| R020 | tiangolo/typer | 0.8973 | 3.95 | DETECTED |
| R023 | tqdm/tqdm | 0.8895 | 13.22 | NOT_DETECTED |
| R033 | PyCQA/pylint | 0.8820 | 1.91 | DETECTED |
| R005 | python-gino/gino | 0.8774 | 4.69 | NOT_DETECTED |
| R010 | marshmallow-code/marshmallow | 0.8731 | 26.33 | NOT_DETECTED |
| R021 | httpie/httpie | 0.8708 | 7.97 | NOT_DETECTED |
| R034 | pre-commit/pre-commit | 0.8644 | 4.88 | DETECTED |
| R045 | rubik/radon | 0.8618 | 5.76 | UNRESOLVED_ACTIVITY_MARGIN |
| R022 | Textualize/rich | 0.8608 | 8.12 | DETECTED |
| R029 | PyCQA/isort | 0.8607 | 14.03 | NOT_DETECTED |
| R011 | pyeve/cerberus | 0.8597 | 12.35 | DETECTED |
| R030 | PyCQA/flake8 | 0.8576 | 6.47 | NOT_DETECTED |
| R017 | pallets/werkzeug | 0.8548 | 9.79 | DETECTED |
| R025 | Bogdanp/dramatiq | 0.8514 | 5.93 | NOT_DETECTED |
| R008 | MagicStack/asyncpg | 0.8508 | 5.49 | NOT_DETECTED |
| R048 | elastic/elasticsearch-py | 0.8489 | 3.10 | DETECTED |
| R009 | pydantic/pydantic | 0.8368 | 3.21 | DETECTED |
| R015 | falconry/falcon | 0.8302 | 2.99 | DETECTED |
| R001 | tortoise/tortoise-orm | 0.8263 | 3.14 | DETECTED |
| R032 | PyCQA/pycodestyle | 0.8132 | 10.74 | NOT_DETECTED |
| R037 | urllib3/urllib3 | 0.8055 | 8.86 | NOT_DETECTED |
| R044 | mkdocs/mkdocs | 0.8052 | 4.91 | UNRESOLVED_ACTIVITY_MARGIN |
| R018 | encode/httpx | 0.7953 | 7.55 | NOT_DETECTED |
| R046 | jazzband/pip-tools | 0.7887 | 7.85 | DETECTED |
| R040 | joke2k/faker | 0.7649 | 5.20 | LEAKAGE |
| R027 | taskiq-python/taskiq | 0.7637 | 1.71 | NOT_DETECTED |
| R049 | Pylons/colander | 0.7624 | 9.72 | NOT_DETECTED |
| R031 | PyCQA/bandit | 0.7609 | 3.02 | LEAKAGE |
| R043 | kevin1024/vcrpy | 0.7557 | 8.63 | DETECTED |
| R013 | encode/starlette | 0.7530 | 9.13 | NOT_DETECTED |
| R024 | rq/rq | 0.7471 | 10.77 | NOT_DETECTED |
| R007 | redis/redis-py | 0.7344 | 6.36 | NOT_DETECTED |
| R014 | sanic-org/sanic | 0.7339 | 4.28 | NOT_DETECTED |
| R041 | getsentry/responses | 0.7100 | 15.37 | NOT_DETECTED |
| R050 | arrow-py/arrow | 0.6838 | 14.21 | NOT_DETECTED |
| R042 | spulec/freezegun | 0.6488 | 11.82 | NOT_DETECTED |

## Protocol compliance
- compute_moderators_exp003.py executed without reading any score_*.json files.
- analyze_exp003.py executed after compute; script hashes match HYPOTHESIS_exp003.md.
- No per-repo results were examined before median threshold was set.
- Forbidden interpretations: geometry_truth, causal_coupling, design_quality.