# EXP-002 Population Selection Criteria

**Status**: CRITERIA FROZEN — repo list not yet declared.
The final 50-repo list must be committed to REPO_DECLARATION_exp002.json
BEFORE any repository is cloned. Criteria below are the only permissible
basis for inclusion/exclusion decisions.

---

## Inclusion criteria (all must be satisfied)

1. **Language**: primary language Python (≥ 70% of tracked files by extension).
2. **Activity**: ≥ 500 non-merge commits in the default branch history at time of
   declaration (same floor as EXP-001 implicit minimum — all wave-1 repos exceeded this).
3. **Size**: ≥ 50 tracked Python files (prevents degenerate small-corpus behavior).
4. **Public**: repository publicly accessible on GitHub at declaration time.
5. **Not in EXP-001 wave-1**: the 20 wave-1 repos are excluded by identity.
   (numpy, scipy, pandas-dev/pandas, scikit-learn, matplotlib, sympy, django,
    pallets/flask, psf/requests, pallets/click, pytest-dev/pytest, sphinx-doc/sphinx,
    celery/celery, tornadoweb/tornado, python-pillow/Pillow, sqlalchemy/sqlalchemy,
    fastapi/fastapi, psf/black, python/mypy, pypa/pip)

## Exclusion criteria

- Repositories where the primary committer is a bot or automated system
  (CI-only commit history contaminates ownership encoder).
- Monorepos with ≥ 5 distinct top-level packages (ownership partition becomes
  inter-package rather than intra-project; different validity scope).
- Forks of EXP-001 wave-1 repos (measurement on the same codebase under a different name).

## Selection process (operator must follow)

1. Generate candidate list from a defined source (e.g., GitHub topic search
   "python" sorted by stars, filtered by criteria above). Source must be
   recorded in REPO_DECLARATION_exp002.json.
2. Apply inclusion/exclusion criteria mechanically. No subjective quality judgments.
3. Take the first 50 passing candidates in the defined sort order.
   Do NOT skip candidates based on anticipated results.
4. Commit the list. Push. Only then begin cloning.

## Diversity target (non-binding, recorded for transparency)

EXP-001 skewed toward ecosystem-defining libraries. Wave-2 should include
application frameworks, data pipelines, developer tools, and domain-specific
libraries to test generalization. This is a GOAL, not an inclusion criterion —
it does not permit exclusions of otherwise-qualifying repos.

---

## Amendment rule

Changes to this criteria document after the REPO_DECLARATION_exp002.json is
committed are prohibited. Pre-declaration amendments require a new erratum
in studies/errata/ERRATA.json with hash continuity.
