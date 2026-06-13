# EXP-002 Hypothesis Registration

**Status**: PREREGISTERED — no wave-2 repo has been cloned or scored at time of writing.
**Instrument version**: ownership encoder v1 (same as EXP-001; no code changes).
**Prior**: EXP-001 wave-1 result — ownership INCONCLUSIVE, k=10/20, Wilson [0.299, 0.701].

---

## Primary hypothesis

H1: The ownership encoder detects co-change coupling (per E-004 dual-baseline rule)
in ≥ 0.60 of the wave-2 declared population (n=50 repos).

H0: Detection rate ≤ 0.60 (same threshold as EXP-001).

Success condition (E-008 rule, frozen): VALIDATED iff point estimate ≥ 0.60.

---

## Power specification

| scenario | true_p | n | power | interpretation |
|---|---|---|---|---|
| Signal above threshold | 0.65 | 50 | 0.814 | Primary power target |
| Strong signal | 0.70 | 50 | 0.952 | Comfortable |
| At-threshold | 0.60 | 50 | 0.561 | Underpowered at exact boundary |
| EXP-001 midpoint | 0.50 | 50 | 0.336 (REJECT) | See note below |
| Clear null | 0.35 | 50 | 0.960 (REJECT) | Strong rejection power |

**Note on true_p = 0.50**: If EXP-001's point estimate (50%) is the true population
rate, EXP-002 at n=50 has only 34% power to REJECT (Wilson_upper < 0.60) and ~8%
power to VALIDATE. In this scenario, INCONCLUSIVE is the most likely outcome (~58%).
This is a documented limitation, not a study flaw. If EXP-002 returns INCONCLUSIVE,
the pre-committed consequence is closure (see §Consequence paths).

**Decision boundary at n=50**:
- REJECTED zone: k ≤ 23 (detection rate ≤ 0.46)
- INCONCLUSIVE zone: k = 24–29 (0.48–0.58)
- VALIDATED zone: k ≥ 30 (≥ 0.60)

---

## Consequence paths (pre-committed before any data)

| outcome | action |
|---|---|
| VALIDATED (k ≥ 30) | Publish positive replication. Proceed to instrument hardening for dep_graph (EXP-003). |
| REJECTED (k ≤ 23) | Retire ownership hypothesis. Publish null + prior update. Full methodology review. |
| INCONCLUSIVE (k = 24–29) | Publish inconclusive. No further ownership waves — INCONCLUSIVE on wave-1 AND wave-2 constitutes effective retirement absent new theoretical grounding. |

The INCONCLUSIVE→retire rule is frozen here to prevent indefinite "one more wave"
escalation. Two consecutive INCONCLUSIVEs at different n are evidence of a hypothesis
that cannot be resolved with the current instrument design, not evidence of a signal
awaiting a larger sample.

---

## Scope limits

- Claim class: `exp002_scored_observation` (per-repo) / `exp002_aggregate_result` (final)

- Forbidden interpretations (inherited from EXP-001 + added):
  - post_hoc_repo_exclusion
  - cherry_picked_subsets
  - retroactive_EXP001_revision (EXP-002 cannot change EXP-001's published result)
  - AI_supply_chain_certification (out of scope until positive replication + independent validation)
  - **ownership_as_causal_lever**: A DETECTED result does not license the inference
    that reassigning file ownership will reduce co-change coupling. The encoder
    measures correlation between ownership partition and co-change structure. It does
    not measure whether ownership is the generative cause. Intervening on ownership
    (e.g., reassigning files to a new contributor) addresses only the instrument's
    input signal; the structural coupling that drove both the ownership pattern and
    the co-change pattern may be unchanged. "DETECTED" means the partition predicts
    the coupling; it does not mean the partition causes it.
  - **latent_factor_identification**: A DETECTED result does not identify the latent
    factor responsible for both ownership concentration and co-change coupling. Task
    complexity, architectural modularity, and contributor expertise are all compatible
    with a DETECTED result. None is confirmed by detection. The instrument certifies
    only that the ownership partition carries mutual information with co-change
    structure above the activity baseline — it does not decompose that mutual
    information into causal components.
  - **negative_is_not_validation**: A NOT_DETECTED result does not certify
    architectural health, absence of hidden coupling, or low structural risk. It
    certifies only that this encoder, at this instrument version, on this repository's
    commit history, did not find ownership-partition mutual information exceeding the
    activity baseline above the null p95. Coupling may exist and be driven by factors
    outside the instrument's scope: cross-repository dependencies, undocumented
    coordination protocols, contributor churn that scrambled the ownership signal, or
    structural families not tested (dep_graph, ast_metrics are REJECTED for this
    instrument version, not for the underlying hypothesis). NOT_DETECTED is the
    absence of a specific signal under specific conditions. It is not a clean bill of
    health.

- Validity scope:
  - DETECTED certifies: ownership partition carries mutual information with co-change
    coupling above both random null and activity baseline, in this repository, at this
    point in history. Permitted use: flag for human architectural review.
  - NOT_DETECTED certifies: the above condition was not met. Permitted use: de-prioritize
    this repository relative to DETECTED repositories for ownership-based review.
    Does not permit: declaring the repository structurally sound or coupling-free.

- Family tested: ownership only. dep_graph and ast_metrics NOT tested in EXP-002.
  Their REJECTED verdicts from EXP-001 stand independently.
