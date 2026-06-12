# executable-epistemics

*(reference instrument: mcl-observer-runtime v2, witness-core architecture)*

**Author**: Daniel Dillberg · **License**: AGPL-3.0-or-later · **Contact**: bigdilly95@gmail.com

A reference implementation of **executable epistemics**: every computed claim
carries a machine-enforced description of its evidentiary boundaries.

## Layered architecture

```
Layer 0  witness_core/     claim-boundary library (domain-agnostic)
Layer 1  mcl_runtime/      observer-comparison instrument (reference impl.)
Layer 2  studies/          registered experiments (EXP-000, EXP-001)
```

The dependency direction IS the abstraction boundary: `witness_core` never
imports geometry; `mcl_runtime` cannot emit anything but witness Artifacts.

## Layer 0 — witness-core

Every artifact is:

```python
Artifact(data=..., provenance=..., claim_class=...,
         validity_scope=..., forbidden_interpretations=...)
```

with hard guarantees: no verdict-shaped field can exist anywhere in `data`
(scanned recursively — `valid`, `healthy`, `anomaly`, `passed`... raise
`WitnessViolation`); chain hashes detect post-compilation tampering; the
experiment registry refuses any registration lacking a **failure condition**
— a registry that cannot record falsification only produces confirmations.

## Layer 1 — the instrument

`analyze(corpus, encoders, tau_policy)` compares representations and emits
geometry-tagged partitions, family-annotated VI, and consensus objects.
Three tools: `detect_divergence`, `triage_content`, `analyze_trajectory`.
All outputs: `claim_class = "observer_agreement_only"`. The runtime issues
deterministic judgments about agreement among declared observers and none
about the world they observe.

## Layer 2 — the studies

**EXP-000 (concluded)**: the v1 instrument witnessed this rebuild — kernel
behavioral equivalence verified on fixture corpora, success condition met,
witness artifact in `studies/EXP000_witness.json`. The tool's first certified
act in this repository was auditing its own successor.

**EXP-001 (registered, awaiting execution)**: the external-validity study.
Hypothesis, success/failure conditions, and interpretation limits are
hash-locked in `studies/REGISTRY.json` before any code runs. Ground truth:
co-change coupling (primary), human-labeled boundaries (secondary);
cyclomatic complexity is excluded as circular.

## Start here

`docs/INTRO.md` — the three-claims framing, four-command campaign
guide, output interpretation tables, and custom-data/encoder rules (including
the `llm_embedding` family conditions). `docs/EXP001_RUNBOOK.md`
— deterministic campaign execution with observed failure modes.

## What this is not

Not a truth detector, safety layer, anomaly classifier, or decision engine.
It locates where your notion of "the system" stops being singular and names
the layer of your stack that owes the verdict it refuses to counterfeit.
