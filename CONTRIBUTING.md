# Contributing

Three rules outrank all style preferences:

1. **The kernel is single-sourced.** q_tau, vi, project, refines,
   merge_heights, perturb exist only in `mcl_runtime/kernel.py`. The firewall
   test fails any duplicate definition.
2. **No verdicts.** Outputs are `witness_core.Artifact` objects; the
   validator rejects verdict-shaped fields recursively. Do not add
   accept/reject/healthy/valid fields anywhere; do not work around this.
3. **Methodology changes are errata.** Frozen policies (studies/) change only
   through `witness_core.ErrataLog` entries recorded BEFORE affected runs.

Before submitting: `SOURCE_DATE_EPOCH=0 python tests/test_all.py` must pass
in full; new experiments must register with hypothesis, success condition,
FAILURE CONDITION, and interpretation limits; new encoders must satisfy
`encoders/ENCODER_CONTRACT.md`. LLM contributors: read `docs/HANDOFF.md`
first — it is the binding contract, not advice.
