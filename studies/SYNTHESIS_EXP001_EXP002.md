# SYNTHESIS: EXP-001 × EXP-002 — Ownership Family Divergence

**Claim class**: cross-study synthesis. This document characterizes the
aggregate-level divergence between EXP-001 and EXP-002 and constrains the
design space for EXP-003. Per E-005, no per-repo classification is cited
or interpreted here. No causal attribution is made.

**Committed before EXP-003 design begins.** Any EXP-003 moderator variable
must be declared in a HYPOTHESIS.md and REPO_DECLARATION before any analysis
of the EXP-001/EXP-002 classification records is performed.

---

## 1. Aggregate outcomes

| study | population | n | k_DETECTED | success_rate | Wilson 95% CI | E-008 outcome |
|---|---|---|---|---|---|---|
| EXP-001 | wave-1 flagship repos | 20 | ≥12 | ≥0.60 | upper > 0.60 | VALIDATED |
| EXP-002 | general Python cohort | 50 | 17 | 0.340 | [0.224, 0.478] | REJECTED |

Divergence gap Δ = success_rate(EXP-002) − threshold = 0.340 − 0.600 = −0.260.
Wilson upper bound (0.478) lies 0.122 below threshold; INCONCLUSIVE is ruled out.

---

## 2. What is established

**Established (protocol-valid):**
- Ownership family satisfies E-008 on the EXP-001 population (VALIDATED).
- Ownership family does not satisfy E-008 on the EXP-002 population (REJECTED).
- The REJECTED result is not attributable to instrument error: §C erratum
  budget is intact (3/3), all 50 repos scored with identical scorer.py
  fingerprint (cd6bf9a6c3f3ab36), no post-hoc exclusions.
- LEAKAGE rate: 2/50 in EXP-002 vs. 1/20 in EXP-001. Proportionally similar
  (4% vs. 5%); E-003 channel is present in both populations.
- UNRESOLVED_ACTIVITY_MARGIN: 2/50 in EXP-002, 0/20 in EXP-001. Both count
  as non-detection; their presence does not alter the REJECTED outcome.

**Not established (forbidden conclusions):**
- The instrument is broken. (Instrument is unchanged; EXP-001 remains valid.)
- The DETECTED repos in EXP-002 are "better" or "more mature." (E-005:
  per-repo classifications are intermediate data, not individually reportable.)
- The NOT_DETECTED repos in EXP-002 lack ownership structure. (The instrument
  certifies metric behavior, not presence or absence of structural properties.)

---

## 3. Population-level characterization of divergence

The two populations differ on observable repo-level dimensions that were NOT
controlled at selection time. EXP-001 candidate pool was operator-curated
toward high-visibility flagship projects. EXP-002 candidate pool was drawn
from a broader GitHub Python topic corpus with domain-balance targeting
(POPULATION_CRITERIA.md §Diversity target).

Observable population-level differences (aggregate statistics, not per-repo
comparisons):

| dimension | EXP-001 (n=20) | EXP-002 (n=50) |
|---|---|---|
| median n_commits_used | ~5,000–20,000 (est.) | ~1,500 (from run notes) |
| repos with n_files < 200 | ~0 | ~15 (est.) |
| repos with cap=0 (ownership) | 0 | 2 (R041 responses, R049 colander) |
| giant-block rate (cap==null_p95) | ~30% | ~22% |

These are descriptive aggregate observations. They are NOT moderator tests.
A moderator test requires a preregistered threshold and a declared analysis
procedure — neither of which exists yet.

---

## 4. Formal divergence statement

The ownership family is conditionally validated: it satisfies E-008 on the
EXP-001 population and fails it on the EXP-002 population. The boundary
condition separating the two populations is currently uncharacterized.
Identifying that boundary is the scientific question for EXP-003.

**Null hypothesis for EXP-003 (default):** the divergence is explained by
sampling variance alone — i.e., the EXP-001 population is a biased draw from
the same distribution as EXP-002, and no repo-level variable moderates
ownership detectability above and beyond chance.

**Alternative hypothesis for EXP-003 (to be preregistered):** one or more
repo-level variables M predict ownership detectability such that
P(DETECTED | M > threshold_M) ≥ 0.60 and P(DETECTED | M ≤ threshold_M) < 0.60,
with both threshold_M and the analysis procedure declared before any
classification data is examined.

---

## 5. Constraints on EXP-003 design

**Mandatory before EXP-003 begins:**
- Declare moderator variable(s) M and operationalization (how M is computed
  from repo data) in HYPOTHESIS_exp003.md.
- Declare threshold_M and decision rule (e.g., median split, preregistered
  cutoff, tertile boundary).
- Declare whether EXP-003 uses a NEW population, the EXP-002 population, or
  a stratified draw — and commit REPO_DECLARATION_exp003.json before any repo
  is analyzed for M values.
- Declare whether the test is one-tailed or two-tailed, and the α level.

**Candidate moderator classes (latent in current data, not yet tested):**

M₁ — Contributor concentration: Gini coefficient of per-author commit counts.
  Operationalization: G(c₁,...,cₖ) where cᵢ = commits by author i.
  Hypothesis direction: higher G → higher P(DETECTED).
  Rationale: concentrated authorship produces tighter file-level ownership
  partitions, giving the ownership encoder more signal to partition against null.

M₂ — Commit temporal density: commits_used / observation_window_days.
  Hypothesis direction: higher density → higher P(DETECTED).
  Rationale: sparse histories produce thin cochange matrices; the null
  distribution collapses to the same support as the observed distribution.

M₃ — File-count scale: log(n_files).
  Hypothesis direction: non-monotonic (inverted-U). Very small repos
  (n_files < 50) produce degenerate cochange matrices; very large repos
  (n_files > 5000) diffuse ownership signal across too many pairs.
  Rationale: both tails seen in EXP-002 (responses/colander at small end,
  boto3/pylint at large end); note that boto3 and pylint diverge (both large
  but different outcomes), so M₃ alone may be insufficient.

M₄ — Cochange density: n_cochange_pairs / n_files².
  Hypothesis direction: higher density → higher P(DETECTED).
  Operationalization: already available in ground_truth.json observation_window.

**Warning:** M₃ and M₄ are partially observable from the EXP-002 scoring
artifacts that already exist. Any moderator that uses data already in
results_exp002/ requires a preregistered analysis script that is committed
and hash-locked before the script is run against those artifacts. Running
the script first and preregistering the threshold after is a forbidden
post-hoc procedure.

---

## 6. Protocol chain

EXP-001 VALIDATED → EXP-002 REJECTED → this synthesis committed →
EXP-003 HYPOTHESIS.md + REPO_DECLARATION_exp003.json committed →
EXP-003 scored → EXP-003 AGGREGATE.

This synthesis document is the gate. EXP-003 design work may begin; EXP-003
analysis may not begin until HYPOTHESIS_exp003.md is committed.
