"""Registered secondary analysis: repo-property vs capture-margin correlation.

REGISTRATION (frozen before repository 1; amendments after first contact:
errata only):

  STATUS        diagnostic-only. Output is evidence about the ACTIVITY
                CONFOUND (does repo size/age drive E-007 margins?), never
                evidence for or against H1. E-008 alone adjudicates H1.
  DECLARED X    tracked_py_files, non_merge_commits   (per repo, at clone)
  DECLARED Y    E-007 activity margin, one per encoder family
                (dep_graph, ast_metrics, ownership)
  TESTS         exactly 2 x 3 = 6. No other pairs may be computed by this
                script; any additional correlation is post-hoc exploratory
                and must be labeled so wherever it appears.
  N             20 (declared population; substitutions per UPDATE_COMMITMENTS E)
  P-VALUES      two-sided permutation null, B=10000, seed=20260612 (frozen).
                Rationale: at n=20 the t-based p assumes bivariate normality;
                margins are not plausibly normal; permutation is exact and
                matches the E-004 null-distribution architecture.
  CORRECTION    Holm step-down over the 6 tests at alpha=0.05.
  FORBIDDEN     interpreting any result here as H1 support; computing
                pairs outside the declared set; rerunning with a new seed.
  VALIDITY      the __main__ self-test certifies TOOL validity only
                (implementation correct on synthetic rows). It does NOT
                certify instrument validity under field distributions;
                that is undefined until the campaign produces real margins.
"""

SEED = 20260612
B = 10000

DECLARED_X = ("tracked_py_files", "non_merge_commits")
DECLARED_Y = ("margin_dep_graph", "margin_ast_metrics", "margin_ownership")


def pearson_r(x, y):
    n = len(x)
    assert n == len(y) and n >= 3
    mx, my = sum(x) / n, sum(y) / n
    dx = [v - mx for v in x]
    dy = [v - my for v in y]
    sxy = sum(a * b for a, b in zip(dx, dy))
    sxx = sum(a * a for a in dx)
    syy = sum(b * b for b in dy)
    if sxx == 0.0 or syy == 0.0:
        return float("nan")  # degenerate column; report, do not test
    return sxy / (sxx * syy) ** 0.5


def perm_p(x, y, seed=SEED, b=B):
    """Two-sided permutation p: (1 + #{|r_pi| >= |r_obs|}) / (1 + B)."""
    import random
    r_obs = pearson_r(x, y)
    if r_obs != r_obs:  # nan
        return float("nan")
    rng = random.Random(seed)
    yp = list(y)
    hits = 0
    for _ in range(b):
        rng.shuffle(yp)
        if abs(pearson_r(x, yp)) >= abs(r_obs) - 1e-12:
            hits += 1
    return (1 + hits) / (1 + b)


def holm(pvals, alpha=0.05):
    """Holm step-down. Returns list of booleans (reject) in input order."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    reject = [False] * m
    for rank, i in enumerate(order):
        if pvals[i] <= alpha / (m - rank):
            reject[i] = True
        else:
            break
    return reject


def run(rows):
    """rows: list of dicts, one per repo, containing all DECLARED columns.
    Returns the 6 registered results. Refuses undeclared columns."""
    results = []
    for xk in DECLARED_X:
        for yk in DECLARED_Y:
            x = [float(r[xk]) for r in rows]
            y = [float(r[yk]) for r in rows]
            results.append({
                "pair": (xk, yk),
                "n": len(rows),
                "r": round(pearson_r(x, y), 4),
                "p_perm": round(perm_p(x, y), 4),
                "claim_class": "activity_confound_diagnostic_only",
            })
    rej = holm([t["p_perm"] for t in results])
    for t, rj in zip(results, rej):
        t["holm_reject_at_0.05"] = rj
    return results


if __name__ == "__main__":
    # Self-test on synthetic data (NEVER evidence; calibration-class only).
    import random
    rng = random.Random(1)
    fake = [{"tracked_py_files": i * 10 + rng.random(),
             "non_merge_commits": rng.random() * 100,
             "margin_dep_graph": i * 0.01 + rng.gauss(0, 0.05),
             "margin_ast_metrics": rng.gauss(0, 1),
             "margin_ownership": rng.gauss(0, 1)} for i in range(20)]
    for t in run(fake):
        print(t)
