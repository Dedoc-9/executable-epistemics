# EXP-003 Hypothesis — Ownership Moderator Study

**Preregistration gate.** This file and the two scripts below are committed
in a single atomic commit BEFORE either script is executed. Executing
analyze_exp003.py before this commit is a forbidden post-hoc procedure
equivalent to threshold selection after observing the data.

Basis: SYNTHESIS_EXP001_EXP002.md (committed prior to this file).

---

## Study design

**Population**: EXP-002 declared cohort (n=50 repos).
Declaration reference: REPO_DECLARATION_exp002.json,
declaration_hash = 13ffc9a71c3fda50471592c22c9f209448b7c66082eeeeb76b3ac4e230f68a0e.
No new repos are scored. No new instrument runs are performed.

**Outcome variable**: ownership classification per EXP-002 scoring artifacts.
DETECTED = 1; all other classifications (LEAKAGE, UNRESOLVED_ACTIVITY_MARGIN,
NOT_DETECTED) = 0. This preserves the binary E-008 framework.

---

## Moderator variables

### M₁ — Contributor concentration (Gini coefficient)

    M₁ᵢ = Gini({commits_by_author_a : a ∈ authors(repoᵢ)})

**Operationalization**: per-author non-merge commit counts from git log,
restricted to the observation window [first_commit_ts, last_commit_ts]
recorded in results_exp002/<name>/ground_truth.json. Author identity is
normalised to lowercase email address.

**Gini formula** (frozen, verbatim in compute_moderators_exp003.py):

    def gini(counts):          # counts: list[int], all > 0
        c = sorted(counts)
        n = len(c)
        if n == 0 or sum(c) == 0: return nan
        return (2 * sum((i+1)*v for i,v in enumerate(c))) / (n*sum(c)) - (n+1)/n

**Edge case declaration**: repos with n_unique_authors = 1 receive M₁ = 0.0
and are flagged notes="single_author_gini_zero". They are retained in the
analysis (Gini=0 is valid; single-author repos are maximally concentrated in
the trivial sense but Gini cannot distinguish them from equal-share repos).
If ≥5 repos carry this flag a sensitivity analysis excluding them is reported.

**Hypothesis direction**: higher M₁ → higher P(DETECTED). One-tailed.

### M₂ — Commit density

    M₂ᵢ = n_commits_used_i / n_files_i

Both inputs read from results_exp002/<name>/ground_truth.json
observation_window. M₂ is a secondary moderator; it does not contribute to
the primary success criterion.

---

## Primary test: E-008-consistent stratification (M₁)

**Split rule**: median of {M₁ᵢ} over all n repos with valid M₁.
The median is computed mechanically by compute_moderators_exp003.py from
the M₁ distribution. No researcher choice is involved in the threshold.

    Stratum H = {repos : M₁ > M₁_median}
    Stratum L = {repos : M₁ ≤ M₁_median}

**Success criterion (VALIDATED_CONDITIONAL)**:

    k_H / |H| ≥ 0.60  AND  Wilson_95_upper(k_H, |H|) > 0.40

Both conditions must hold simultaneously.

**Falsification criterion (REJECTED_CONDITIONAL)**:

    k_H / |H| < 0.60  AND  Wilson_95_upper(k_H, |H|) < 0.60

**Minimum stratum size**: |H| ≥ 10 and |L| ≥ 10 required for the primary
test to be interpretable. If either stratum has n < 10, the primary result
is UNDERPOWERED and only the secondary test is reportable.

**Wilson CI formula**: z = 1.96, standard score interval, clipped to [0,1].
Frozen verbatim in analyze_exp003.py.

---

## Secondary test: point-biserial correlation

    r_pb = Pearson(M₁_i, DETECTED_i),  DETECTED_i ∈ {0,1}

One-tailed test, H_alt: r > 0 (higher M₁ → higher P(DETECTED)), α = 0.05.
p-value via scipy.stats.pointbiserialr if available; otherwise t-distribution
approximation (df = n-2). Formula frozen verbatim in analyze_exp003.py.

The secondary test is informational. A significant r_pb that co-occurs with
VALIDATED_CONDITIONAL strengthens the interpretation. A significant r_pb
that co-occurs with REJECTED_CONDITIONAL does not rescue the primary outcome.

---

## Script hash lock

Both scripts are committed in this same commit. Their SHA-256 hashes are:

    compute_moderators_exp003.py : 41c66d626214af5cea00626728ec2e84e7372ed025ca2ffca256dde7104f55e6
    analyze_exp003.py            : 64121317291ccb2ec882818a697fbba95a18f5228e6e0051825691aea026fa58

Executing either script after modifying it without updating this file and
re-committing is a protocol violation. Verify before running:

    python -c "import hashlib; print(hashlib.sha256(open('studies/exp003_moderator/compute_moderators_exp003.py','rb').read()).hexdigest())"
    python -c "import hashlib; print(hashlib.sha256(open('studies/exp003_moderator/analyze_exp003.py','rb').read()).hexdigest())"

---

## Execution order (mandatory)

1. This file committed with script hashes → git push           [DONE at this commit]
2. python studies/exp003_moderator/compute_moderators_exp003.py
   → writes studies/exp003_moderator/moderators_exp003.json
3. python studies/exp003_moderator/analyze_exp003.py
   → writes studies/exp003_moderator/AGGREGATE_exp003.md
4. git add moderators_exp003.json AGGREGATE_exp003.md → commit → push

Steps 2 and 3 may be inspected between execution (moderators_exp003.json
contains only M₁/M₂ values, no outcome data). They must not be re-run with
modified scripts after step 4 is committed.
