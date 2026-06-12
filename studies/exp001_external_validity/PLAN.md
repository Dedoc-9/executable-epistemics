# P1: External Validity Study (Experiment 001)

Registered in `studies/REGISTRY.json` BEFORE execution; hypothesis, success
condition, failure condition, and interpretation limits are hash-locked there.

## Ground truth decision (and the rejection that matters)

**Rejected: cyclomatic-complexity thresholds.** Complexity is computed from
the same artifact the encoders measure — using it as ground truth tests
whether structure predicts a function of itself. That is the single-family
trap relocated to the validity layer. Complexity belongs on the ENCODER side.

**Primary ground truth: co-change coupling** — entities modified in the same
commits, mined from git history. Behaviorally grounded, causally independent
of any static encoder, available at scale without labeling cost.

**Secondary: human-labeled module boundaries** — package/ownership maps.
Independent of the encoders but conventional (humans may draw boundaries by
habit, not function); reported separately, never merged with primary.

## Phases
1. Corpus builder: git mining + AST + dependency extraction -> runtime corpus
   format, 5 repositories first, then 20+.
2. Encoder suite: dependency-graph, AST-metric, co-change-history*,
   embedding families. (*excluded from runs scored against co-change ground
   truth — same circularity rule.)
3. Null model: size-matched random partitions, 1000 draws per repo.
4. Scoring: per-family, per-repo; witness Artifacts only.
5. Tool gate: the PR structural-diff tool ships only if the success condition
   is met. No validity, no tool.
