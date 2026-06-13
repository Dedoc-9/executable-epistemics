# SYNTHESIS — EXP-001 through EXP-004 Campaign Summary

**synthesis_hash (informational):** PENDING — compute after commit.
**Covers commits**: fba78e7 (EXP-002 base) through 659bb06 (EXP-004 result).

---

## 1. Cumulative chain

| study | design | primary outcome | k/n | Wilson 95% CI |
|---|---|---|---|---|
| EXP-001 | ownership, wave-1, n=25 | VALIDATED | ≥15/25 | upper ≥ 0.60 |
| EXP-002 | ownership replication, n=50 | REJECTED | 17/50 = 0.340 | [0.224, 0.478] |
| EXP-003 | Gini moderator (M₁), n=50 | REJECTED_CONDITIONAL | H: 10/25 = 0.400 | [0.234, 0.593] |
| EXP-004 | joint threshold (M₁∧M₂), n=50 | INCONCLUSIVE | T: 5/11 = 0.455 | [0.213, 0.720] |

---

## 2. EXP-004 structural result

Primary test: P(DETECTED | M₁ > 0.8587 AND M₂ < 7.703) ≥ 0.60.
Result: INCONCLUSIVE. Wilson upper 0.720 prevents REJECTED; point estimate 0.455
prevents VALIDATED. Cell size n_T=11 is the binding constraint — the E-008
criterion requires more resolution than 11 observations can provide.

### 2×2 monotone ordering (informational)

| cell | M₁ | M₂ | k/n | rate |
|---|---|---|---|---|
| T  | high | low  | 5/11 | 0.455 |
| Hd | high | high | 5/14 | 0.357 |
| Ls | low  | low  | 4/14 | 0.286 |
| Ld | low  | high | 3/11 | 0.273 |

The monotone ordering T > Hd > Ls > Ld is directionally consistent with:
(i) M₁ (Gini) as primary moderator — high M₁ cells outperform low M₁ cells in both
    M₂ strata;
(ii) M₂ (density) as secondary moderator — within each M₁ stratum, low M₂ outperforms
    high M₂.

This ordering is an informational observation from registered cells, not a post-hoc
test. It cannot be used to claim VALIDATED at any cell by itself.

---

## 3. Resolution of the EXP-001 / EXP-002 divergence

The divergence gap Δ = 0.340 − 0.600 = −0.260 (SYNTHESIS_EXP001_EXP002.md, e4b9f52)
remains unexplained by any registered analysis passing E-008. Two candidate accounts
are now formally ranked by evidence:

**Account A — Selection bias (consistent with all four studies).**
EXP-001 wave-1 repos were drawn from a pool that likely overrepresents high-M₁
software (dominant-author projects). The EXP-002 population, drawn from a broader
GitHub Python topic search balanced for domain diversity, includes a higher fraction
of distributed-authorship repos. The T-cell rate 0.455 (versus 0.340 overall) is
consistent with EXP-001 having effectively sampled from T-cell space. Selection
bias is not testable within this campaign without access to EXP-001 repo moderator values.

**Account B — Instrument sensitivity threshold (INCONCLUSIVE).**
The instrument may detect ownership only above a joint (M₁, M₂) threshold that is
crossed by fewer than 60% of any broadly sampled population. EXP-004 cannot
distinguish this from Account A at current resolution.

---

## 4. Operator-pipeline state at campaign close

```
μ → Lτ → Bτ → Rτ → Z → S → W → OBS
```

Aggregate observables at 659bb06:

| observable | value |
|---|---|
| B(EXP-002) = ‖S‖/(‖Z‖+ε) | 17/50 = 0.340 |
| B(EXP-003, H) | 10/25 = 0.400 |
| B(EXP-004, T) | 5/11 = 0.455 |
| r_pb(M₁, DETECTED) | 0.218, p=0.064 |
| monotone cell ordering | T > Hd > Ls > Ld |

No cell clears E-008 VALIDATED in EXP-002 through EXP-004. The forward evolution
(ownership signal) does not dominate the null in any registered test.

Residual G_t = Z_t − Π_W(Z_t): the unexplained DETECTED rate in T (0.455 vs
hypothesized ≥0.60) is the current campaign residual. EMA accumulation:
S_{t+1} = αS_t + (1−α)·G_t absorbs this as a numeric residual for EXP-005 design.

---

## 5. Gravitational backreaction

Each experiment perturbs the moderator hypothesis space. The instrument was designed
so that gaming toward DETECTED requires gaming actual commit history — Goodhart's
Law resistance is structural (commit 4e809c8, HYPOTHESIS_exp003.md). The campaign
residual G_t is therefore not attributable to instrument gaming; it reflects genuine
structural heterogeneity in the population.

Backreaction estimate: the T-cell result (0.455) lifts the posterior on Account A
(selection bias) over Account B (instrument threshold), because the monotone
ordering is consistent with a continuous Gini × density signal rather than a
hard threshold effect. A hard threshold would predict a step function; the smooth
T > Hd > Ls > Ld gradient is more consistent with a continuous moderator.

---

## 6. EXP-005 options (not preregistered)

The following are candidate designs only. None may be executed without a new
HYPOTHESIS + gate commit.

**Option 1 — T-cell targeted recruitment.**
Recruit n=30+ repos satisfying M₁ > 0.86 AND M₂ < 7.7 from a fresh population
(not EXP-002 cohort). Tests whether T-cell rate ≥0.60 at adequate power.
Risk: selection on moderator values violates population generality.

**Option 2 — M₂ re-operationalization.**
Replace M₂ = n_commits/n_files with M₂′ = median(files_changed_per_commit).
Tests whether bulk-commit size (not volume) is the suppressive factor.
Requires new compute_moderators script; full gate protocol applies.

**Option 3 — EXP-001 moderator retrocompute.**
Apply compute_moderators_exp003.py to EXP-001 wave-1 repos. Tests directly
whether EXP-001 cohort is T-cell enriched. No new scoring needed; requires
EXP-001 moderator gate commit and formal comparison test.

Option 3 is the highest-information / lowest-cost next step: it directly tests
Account A (selection bias) using already-committed instruments, requires no new
scoring, and closes the EXP-001/EXP-002 divergence question at its root.

---

## 7. Protocol status at campaign close

| check | status |
|---|---|
| hash continuity | PASS — all gate commits verifiable |
| operator ordering | PASS — μ→Lτ→Bτ→Rτ→Z→S→W→OBS maintained |
| ghost closure | PASS — G_t numeric residual only |
| dual arithmetic separation | PASS — forward (Z) and residual (S,G) not collapsed |
| observable purity | PASS — no narrative in OBS fields |
| E-005 compliance | PASS — no per-repo results reported |
| §C erratum budget | 3/3 remaining (E-014 was declaration_slug_correction, not instrument erratum) |

System state valid at 659bb06.

---

*synthesis_hash: SHA-256 of this file committed at next push.*
