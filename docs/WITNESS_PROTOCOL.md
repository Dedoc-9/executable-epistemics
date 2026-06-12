# The Witness Protocol (Layer 0 Specification)

**Principle**: a result is incomplete until the boundaries of its
interpretation are machine-readable alongside the result itself.

## The Artifact (mandatory five fields)
| field | guarantee |
|---|---|
| data | payload; recursively scanned — verdict-shaped keys raise WitnessViolation |
| provenance | env, code fingerprints, seeds; participates in chain identity |
| claim_class | the reasoning primitive consumers are typed against |
| validity_scope | measured region + `certifies` (required) + unmeasured axes |
| forbidden_interpretations | explicit disallowed semantic leaps |

`chain_hash` covers all five; `verify_chain()` detects tampering. A chain
hash certifies integrity, never truth.

## The Registry (precommitment)
Registration REQUIRES, before execution: hypothesis, success_condition,
**failure_condition**, interpretation_limits. Script hash binds declaration
to code; one conclusion per experiment; tampering detectable via
registration hash. Post-hoc rationalization becomes a recorded state.

## The Errata Log
Corrections are append-only first-class artifacts, each hashed, each naming
what it supersedes. Errors are not deleted; they are superseded on the record.

## Operator Taxonomy (naming an enforced separation)

Every executable in a study is exactly one of three operator kinds, and the
kind is fixed at registration:

| kind | maps | may run | may NOT |
|---|---|---|---|
| **measurement** | world → artifacts | during campaign | choose what to measure next |
| **inference** | artifacts → registered statistics | after data, per frozen spec (seeds, tests, corrections fixed ex ante) | compute undeclared statistics; expand its query set at runtime |
| **hypothesis-generating** | artifacts → candidate hypotheses | only BETWEEN registrations | feed the registration that produced its inputs |

The rule the taxonomy names: **no operator changes kind at runtime, and no
output flows backward into the registration that licensed it.** A
measurement that starts selecting becomes policy (GEN-005); an inference
that starts exploring becomes hypothesis generation wearing a correction
(the all-pairs trap); hypothesis generation is legal — in its slot, before
the next freeze. Multiplicity correction (Holm, Bonferroni) is a statistical
patch for a taxonomy violation; the preferred fix is syntactic: the
inference operator's query set is closed at registration, so the violation
cannot be expressed. Reference implementation: exp001 secondary_corr.py.
Nothing in this layer references partitions, geometry, or encoders. It
applies unchanged to eval harnesses, agent reports, security scans, and
scientific workflows. Layer 1 of this repository is its first consumer,
not its definition.
