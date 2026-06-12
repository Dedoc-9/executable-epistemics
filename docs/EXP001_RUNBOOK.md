# EXP-001 Campaign Runbook (deterministic; no decisions remain)

## Preconditions
- Python >= 3.9, git >= 2.30; no other dependencies.
- `studies/REGISTRY.json` shows EXP-001 status `registered`.
- `studies/population/REPO_DECLARATION.json` unchanged (chain 13076c4084f9d9cb) or amended
  ONLY via errata recorded before the affected repo is scored.

## Per repository (run exactly once per declared repo)
    git clone --no-tags https://github.com/<owner>/<repo> work/<repo>
    python validity_framework/run_study.py \
        --repo work/<repo> --outdir results/<repo>
Notes: filter is computed by the E-006 formula (printed in output);
exclusions beyond the default require a pre-run erratum; NEVER pass
--calibration on declared repos (that flag is for rehearsals only).

## Aggregate (run once, after all 20)
    python validity_framework/aggregate.py \
        --results-root results/ --output EXP001_CONCLUSION.json
Then: registry conclusion is recorded against the artifact; the outcome
field reads POSITIVE / NEGATIVE / INCONCLUSIVE / INCOMPLETE and is final.

## Expected artifacts
results/<repo>/ground_truth.json (claim: historical_cochange_observation_only)
results/<repo>/score_{dep_graph,ast_metrics,ownership}.json (E-007 classification)
EXP001_CONCLUSION.json (claim: exp001_aggregate_conclusion)

## Failure modes (observed in rehearsal, n=20 synthetic)
1. SMALL-REPO POWER FLOOR: repos with few files/commits yield permissive
   nulls; even truly modular rehearsal repos scored 1/20 detections.
   Declared repos are large; if any yields <100 scored files, expect
   non-detection to be uninformative — report as-is, never substitute.
2. UNDECLARED DIRECTORY: aggregate (strict mode) excludes it and lists it
   under excluded_not_declared. Do not rename directories to match; record
   an erratum or omit.
3. ZERO SCORED FAMILIES: outcome NO_DECLARED_RESULTS (not NEGATIVE).
4. ENCODER <4 FILES: runner skips the family for that repo; the skip is
   logged; the repo still counts in the denominator (E-005 discipline).
5. NULL-BYTE/SYNC CORRUPTION (host-specific): verify artifacts parse as
   JSON after each run; chain hashes detect any post-write mutation.

## Prohibitions (enforced, listed for humans)
- No synthetic or mirrored-with-edits repositories as evidence (claim-class
  firewall + population firewall both block this).
- No per-repo narrative reporting (E-005). No threshold changes (E-008).
- No reruns with modified parameters: one scoring run per repo, period.
