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

## Portability
Nothing in this layer references partitions, geometry, or encoders. It
applies unchanged to eval harnesses, agent reports, security scans, and
scientific workflows. Layer 1 of this repository is its first consumer,
not its definition.
