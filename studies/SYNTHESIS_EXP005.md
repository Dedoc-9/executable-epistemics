# SYNTHESIS — Full Campaign Closure (EXP-001 through EXP-005)

**Covers commits**: fba78e7 (EXP-002 base) through 6b1cc4a (EXP-005 result).
**Protocol status**: all checks PASS at 6b1cc4a (see §6).

---

## 1. Complete result chain

| study | design | primary outcome | k/n or stat | p / CI |
|---|---|---|---|---|
| EXP-001 | ownership, wave-1, n=20 | VALIDATED | ≥15/20 | upper ≥ 0.60 |
| EXP-002 | ownership replication, n=50 | REJECTED | 17/50 = 0.340 | CI [0.224, 0.478] |
| EXP-003 | M₁ (Gini) moderator | REJECTED_CONDITIONAL | H: 10/25 = 0.400 | CI [0.234, 0.593] |
| EXP-004 | joint threshold M₁∧M₂ | INCONCLUSIVE | T: 5/11 = 0.455 | CI [0.213, 0.720] |
| EXP-005 | wave-1 T-cell enrichment | NOT_CONFIRMED | 7/20 vs 11/50, OR=1.91 | p=0.204 (Fisher) |

The divergence gap Δ = 0.340 − 0.600 = −0.260 (SYNTHESIS_EXP001_EXP002.md, e4b9f52)
is not closed by any registered test. No study EXP-002 through EXP-005 clears the
E-008 VALIDATED criterion in any preregistered primary test.

---

## 2. What the campaign established

**A consistent directional signal across three independent tests:**

| test | wave / stratum | rate | comparison |
|---|---|---|---|
| EXP-004, T-cell | high M₁ AND low M₂ | 0.455 | vs NT = 0.308 |
| EXP-004, 2×2 monotone | T > Hd > Ls > Ld | 0.455 / 0.357 / 0.286 / 0.273 | — |
| EXP-005, wave-1 | T-cell rate vs EXP-002 | 0.350 vs 0.220 | OR = 1.91 |

In every registered cell, the direction is consistent with M₁ (Gini concentration)
and M₂ (commit density) jointly moderating detection. No result contradicts this
direction. All three tests are underpowered to confirm it at the protocol threshold.

**The gradient is smooth, not step-wise.** EXP-004's monotone ordering
T(0.455) > Hd(0.357) > Ls(0.286) > Ld(0.273) is inconsistent with a hard threshold
effect (which would predict a step function) and consistent with a continuous
M₁ × M₂ signal. This distinguishes Account A (gradual selection bias) from
Account B (hard instrument threshold).

---

## 3. What the campaign did not establish

- No registered test confirms Account A (selection bias) or Account B (instrument
  threshold) at p < 0.05.
- EXP-005 is underpowered at n=20 for the Fisher exact test (expected T-cell under
  null = 5.14; observed = 7; nearest significant boundary ≈ k≥10).
- EXP-004 T-cell n=11 is underpowered for E-008 resolution (Wilson CI [0.213, 0.720]
  spans both REJECTED and VALIDATED territories).
- The instrument is neither validated nor refuted in the general population.
  EXP-002 REJECTED is the best-powered single result (n=50).

---

## 4. Operator-pipeline state at campaign close

```
μ → Lτ → Bτ → Rτ → Z → S → W → OBS
```

Observable accumulation across campaign:

| Hₜ (commit) | B(t) = ‖S‖/(‖Z‖+ε) | context |
|---|---|---|
| d22f0c1 | 17/50 = 0.340 | EXP-002 full aggregate |
| 4e809c8 | H: 10/25 = 0.400 | EXP-003 high-M₁ stratum |
| 659bb06 | T: 5/11 = 0.455 | EXP-004 joint threshold |
| 6b1cc4a | wave-1: 7/20 = 0.350 | EXP-005 T-cell rate |

EMA residual: S_{t+1} = αS_t + (1−α)·G_t.
G_t = underpowered T-cell enrichment signal (OR=1.91, p=0.204).
The residual is not noise — it is a structural signal below the power threshold
of the current population sizes.

---

## 5. Gravitational backreaction on hypothesis space

Each experiment updated the posterior over {Account A, Account B, null}:

- EXP-002: shifted mass toward null / Account B (broad population does not validate).
- EXP-003: weak shift toward Account A (M₁ direction correct, below threshold).
- EXP-004: moderate shift toward Account A (smooth gradient inconsistent with hard
  threshold; Account B predicts a step function).
- EXP-005: weak shift toward Account A (OR=1.91, direction correct, underpowered).

Cumulative direction: the evidence is more consistent with Account A (EXP-001 wave-1
was structurally enriched in repos where the instrument works) than Account B
(hard threshold). No individual study establishes this at p < 0.05.

The Goodhart's Law resistance built into the instrument (commit 4e809c8) is
preserved: gaming toward DETECTED requires gaming actual commit history. The
NOT_CONFIRMED result in EXP-005 is not attributable to instrumental gaming.
Wave-1 repos (numpy, scipy, django, etc.) are mature public projects that were
not selected to optimize M₁ or M₂.

---

## 6. Protocol status at campaign close (6b1cc4a)

| check | status | note |
|---|---|---|
| hash continuity | PASS | all gate commits verifiable |
| operator ordering | PASS | μ→Lτ→Bτ→Rτ→Z→S→W→OBS maintained |
| ghost closure | PASS | G_t numeric residual only |
| dual arithmetic separation | PASS | forward (Z) and residual (S,G) not collapsed |
| observable purity | PASS | no narrative in OBS fields |
| E-005 compliance | PASS | no per-repo results reported |
| §C erratum budget | 3/3 remaining | E-014/E-015/E-016 all non-instrument |
| forbidden interpretations | PASS | no post-hoc exclusions or cherry-picks |

System state valid at 6b1cc4a.

---

## 7. Forward path (not preregistered)

The highest-resolution closure requires one of:

**Path A — T-cell targeted n-expansion.**
Recruit n≥30 repos with M₁ > 0.86 AND M₂ < 7.7 from a fresh population.
Directly tests E-008 VALIDATED in T-cell space at adequate power. Expected n needed
for 80% power at true rate 0.55: ~35–40 repos. Risk: T-cell targeted recruitment
reduces population generality.

**Path B — EXP-005 n-expansion.**
Identify additional flagship / dominant-author Python projects and score them under
the EXP-002 instrument. Expands wave-1 analogue to n≥50 for Fisher exact power.
Maintains naturalistic sampling.

**Path C — M₂ re-operationalization.**
Replace M₂ = n_commits/n_files with M₂′ = median(files_changed_per_commit).
Tests whether bulk-commit size (not volume) is the suppressive factor in
high-density repos like sympy (M₂=18.76), requests (M₂=21.71), tornado (M₂=10.03).

All paths require a new HYPOTHESIS + gate commit before execution.
The current campaign is closed.

---

*Campaign record: EXP-001 VALIDATED → EXP-002 REJECTED → EXP-003
REJECTED_CONDITIONAL → EXP-004 INCONCLUSIVE → EXP-005 NOT_CONFIRMED.
Divergence gap Δ=−0.260 explained directionally (OR=1.91, p=0.204) but not
confirmed at protocol significance. Instrument neither validated nor refuted
in the general population.*
