# EXP-002 Aggregate Result — Ownership Replication (n=50)

**Claim class**: E-008 aggregate outcome record.
Per E-005: this aggregate (≥60%-of-repos rule) is the ONLY reportable result
of EXP-002. Per-repo classifications in RUN_NOTES are intermediate data only.

## E-008 Computation

| metric | value |
|---|---|
| n (declared repos scored) | 50 |
| k (DETECTED) | 17 |
| k (LEAKAGE) | 2 |
| k (UNRESOLVED_ACTIVITY_MARGIN) | 2 |
| k (NOT_DETECTED) | 29 |
| success_rate = k/n | 17/50 = 0.340000 |
| Wilson 95% CI lower | 0.224368 |
| Wilson 95% CI upper | 0.478464 |
| threshold (locked, E-008) | 0.600000 |

Wilson formula: z=1.96, standard score interval, clipped to [0,1].

## E-008 Outcome: **REJECTED**

Condition: point estimate < 0.60 AND Wilson 95% CI upper bound < 0.60.
- 0.340 < 0.60 ✓
- 0.478 < 0.60 ✓

The ownership family does NOT meet the preregistered replication threshold
at n=50. The Wilson upper bound (0.478) lies well below 0.60; an
INCONCLUSIVE result is ruled out — this is a rejection, not a data
sufficiency problem.

## DETECTED repos (17/50)
R001 tortoise/tortoise-orm, R009 pydantic/pydantic, R011 pyeve/cerberus,
R015 falconry/falcon, R016 aio-libs/aiohttp, R017 pallets/werkzeug,
R019 mitmproxy/mitmproxy, R020 tiangolo/typer, R022 Textualize/rich,
R033 PyCQA/pylint, R034 pre-commit/pre-commit, R038 pyca/cryptography,
R039 HypothesisWorks/hypothesis, R043 kevin1024/vcrpy,
R046 jazzband/pip-tools, R047 mongodb/motor, R048 elastic/elasticsearch-py

## LEAKAGE repos (2/50) — count as non-detection per E-004/E-007
R031 PyCQA/bandit, R040 joke2k/faker

## UNRESOLVED_ACTIVITY_MARGIN repos (2/50) — count as non-detection per E-007
R044 mkdocs/mkdocs, R045 rubik/radon

## Protocol compliance
- Population declared and committed at e36d2dd BEFORE any repo cloned.
- E-014 slug correction (psf→pyca/cryptography) filed as declaration_slug_correction,
  NOT instrument erratum; §C budget unchanged (3/3 remaining).
- All 50 repos scored with identical instrument (scorer.py cd6bf9a6c3f3ab36).
- No post-hoc exclusions or cherry-picked subsets.
- Forbidden interpretations enforced: geometry_truth, causal_coupling, design_quality.
