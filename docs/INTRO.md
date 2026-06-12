# Toolkit Introduction: Witnessed Software Experiments

**What this is**: an executable framework for contamination-aware validation of
structural software representations — plus one registered, not-yet-executed
experiment built on it.

**Author**: Daniel Dillberg · **License**: AGPL-3.0-or-later · **Contact**: bigdilly95@gmail.com

---

## 1. The three claims (read this before anything else)

This toolkit contains three separable contributions. Only one of them is a
hypothesis; the other two exist regardless of how that hypothesis fares.

**Claim A — Executable epistemics** (`witness_core/`, exists today).
Methodology constraints that are code, not prose: experiments cannot be
registered without failure conditions; forbidden interpretations are
serialized into every artifact; errata are chained and append-only; rehearsal
artifacts are structurally barred from becoming evidence; claim classes
propagate through outputs *and through every human-readable rendering*. Most
reproducibility systems preserve artifacts. This layer preserves
**interpretation constraints**.

**Claim B — Structural validity framework** (`studies/`, exists today).
A dual-baseline evaluation protocol for any representation of software
structure: a candidate is detected only if it beats BOTH a size-matched
random null (1000 draws) AND an activity baseline (per-file churn + size,
pair-blind), by a margin wider than the null's own spread. This controls for
the soft circularity channel: file size partially encodes change frequency,
so any size-correlated feature can rediscover history while appearing to
discover structure. The framework evaluates symbolic and learned
representations under identical contamination controls, and survives even if
every tested representation fails.

**Claim C — A specific representation family predicts coupling** (EXP-001,
registered, NOT executed). The risky claim. Everything else survives its
failure; this doesn't. Its hypothesis, success condition, failure condition,
interpretation limits, scoring rule, population, and decision thresholds are
hash-locked and cannot be amended after data contact except through recorded
errata.

**Scope statement, stated plainly because reviewers will ask**: this toolkit
does not measure software architecture quality. It measures whether a
representation captures historical maintenance coupling better than declared
baselines. Co-change is a proxy, chosen for behavioral grounding and causal
independence from static encoders — and it is only that.

## 2. Bash-first: the campaign in four commands

```bash
# 1. Clone the frozen population (declared in REPO_DECLARATION.json)
mkdir repos && cd repos
git clone https://github.com/numpy/numpy.git
git clone https://github.com/django/django.git
# ... all 20 declared repositories

# 2 + 3. Per repository: frozen ground truth + family scoring (one command)
python validity_framework/run_study.py \
    --repo repos/numpy --outdir results/numpy
#   -> results/numpy/ground_truth.json   claim: historical_cochange_observation_only
#   -> results/numpy/score_<family>.json classification per E-007

# 4. Aggregate once, after all 20
python validity_framework/aggregate.py \
    --results-root results/ --output EXP001_CONCLUSION.json
#   -> outcome under E-008: POSITIVE / NEGATIVE / INCONCLUSIVE / INCOMPLETE
```

No discretionary steps exist: the commit-size filter is computed by formula
(E-006), thresholds are frozen, and the aggregator refuses repositories that
are not in the declared population. See `docs/EXP001_RUNBOOK.md` for failure modes.

## 3. How to interpret what comes out

**Per-family, per-repo classification (E-004/E-007):**

| classification | meaning |
|---|---|
| `DETECTED` | beat random null AND activity baseline, by more than the null's spread |
| `LEAKAGE` | beat the null but not the activity baseline — rediscovered churn, not structure |
| `UNRESOLVED_ACTIVITY_MARGIN` | beat both, but the activity margin is inside the noise band — counts as non-detection |
| `NOT_DETECTED` | did not beat the null |

**Aggregate outcome (E-008)**: a family is VALIDATED at ≥60% detection across
the declared population; REJECTED only if the Wilson 95% upper bound is also
below 60%; INCONCLUSIVE between. Per-repo classifications are intermediate
data — never report them individually (E-005).

**Claim classes you will see, and what they permit:**

| claim_class | may be used as |
|---|---|
| `historical_cochange_observation_only` | ground truth; never a quality judgment |
| `exp001_scored_observation` | input to the aggregate; nothing alone |
| `campaign_rehearsal_only` / `pipeline_calibration_only` | mechanics validation; **never evidence** |
| `exp001_aggregate_conclusion` | the study's reportable result |
| `preregistered_methodology_only` | rules; not findings |

**Two reading rules that outrank everything**: (1) check `validity_scope`
before summarizing any artifact — `forbidden_interpretations` lists the
semantic leaps the artifact prohibits about itself; (2) when quoting any
number out of an artifact, the claim_class travels with it. Every rendering
this toolkit produces prints its scope; renderings you produce must too.

## 4. Running custom data

**Any corpus.** The runtime layer accepts `{id: [float, ...]}` — entities of
any kind, not just files. `mcl_runtime.analyze(corpus, encoders=...)` returns
a witness Artifact with geometry-tagged partitions, family-annotated
comparisons, and a validity scope. The verdict-field firewall applies: if
your data contains keys like `valid` or `healthy`, the Artifact constructor
refuses it.

**Custom encoders.** Deterministic callables, total over the corpus, any
randomness seeded by a declared constant:

```python
from mcl_runtime import register_encoder, analyze
register_encoder("my_view", lambda native, raw: {k: v[2:5] for k, v in native.items()})
r = analyze(corpus, encoders=("native", "my_view"))
print(r["data"]["families"])   # membership is MEASURED (distance correlation),
                               # never assumed — two views of the same features
                               # will land in one family and confirm nothing
```

**An `llm_embedding` family** slots in under the same rules, with two
conditions. Determinism: API embeddings are not reproducible calls — embed
once, cache to a file, hash the cache into provenance, and the encoder reads
the cache. Circularity: embed file *content only*; any prompt or input that
includes git metadata, commit history, or churn statistics re-imports the
ground truth and voids the comparison. Subject to those, learned and symbolic
representations compete under identical controls — which is the point.

**Custom ground truths / new experiments.** Use the registry; it will refuse
you until you state how you could be wrong:

```python
from witness_core import ExperimentRegistry
reg = ExperimentRegistry("my_registry.json")
reg.register("EXP-mine-001",
    hypothesis="...",
    success_condition="...",
    failure_condition="...",          # mandatory; no confirmation-only studies
    interpretation_limits="...")
```

Beat the analogue of both baselines, freeze your scoring before contact with
data, and record every methodology change as an erratum. The toolkit will
hold you to it; that is what it is for.

## 5. What the toolkit will not do

It will not tell you a system is correct, broken, healthy, or well-designed.
It will not gate actions, repair state, or rank quality. It issues
deterministic, provenance-chained statements about agreement between declared
observers and about preregistered scores against frozen references — and it
declares, on every output, where those statements stop being meaningful.
