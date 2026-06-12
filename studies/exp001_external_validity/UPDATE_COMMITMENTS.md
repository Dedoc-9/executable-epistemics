# Update Commitments & Retirement Criteria (recorded before repository 1)

Layer 5 of the evidence stack: precommitted operational consequences.
Commitments are over ACTIONS and RESOURCES, never credences (beliefs cannot
be promised; queue positions can). All updates are GATED on instrument
validity: a result triggers belief-space consequences only if no instrument
erratum applies to it; otherwise it routes to errata and the affected
repositories rescore after the fix. Per E-005, repo-level outcomes trigger
ONLY operational actions; hypothesis-level updates key EXCLUSIVELY to the
E-008 aggregate over the declared population.

## A. Repo-level outcome mapping (operational only)

| Repo-1 (and each subsequent repo) outcome | Committed action |
|---|---|
| any classification, pipeline clean | record, commit, push; proceed to checkpoint; NO theoretical update |
| instrument failure / crash / implausible metric (null_p95 ∈ {0, ~1}, filter at cap or < 5) | SUSPEND campaign; erratum before any further repo is scored; affected repo rescored post-fix |
| *amendment per E-012 (9472ce652ae5b901)*: the fixed filter threshold is superseded — a filter alarm resolves by direct distribution verification recorded with the repo's artifacts; verified-correct values close without suspension | — |
| outcome outside the registered classification space | STOP; record verbatim; no improvised interpretation; re-registration required before continuing |
| runtime > 12h on any single repo | record as infeasibility datum; erratum proposing (pre-declared) kernel port; campaign continues on remaining repos meanwhile |

## B. Aggregate-level mapping (after all 20, E-008)

| Aggregate outcome | Committed consequence |
|---|---|
| any family VALIDATED | H1 survives for wave-1 scope; committed next action: independent reproduction solicitation BEFORE any tool-building on the result (per the evidence hierarchy — replication outranks elaboration); wave-2 (cross-language) registration may proceed |
| all families REJECTED | **H1 RETIRED for wave-1 scope**: no further experiments premised on structural-family co-change prediction in Python repos without new registration AND new encoder families from genuinely new measurement bases; the negative result is published with the same prominence a positive would have received; the PR-diff tool is NOT built (the tool gate holds) |
| INCONCLUSIVE | no retirement, no validation; committed action: power analysis BEFORE any wave-2 — if the declared n=20 cannot in principle resolve the question, the fix is design, not repetition |
| CAMPAIGN never completes | see stop rules below; an incomplete campaign licenses NO claims in either direction |

## C. Campaign stop rules (program-level, precommitted)

1. **Erratum budget**: if more than 3 instrument errata are required during
   the campaign, the campaign STOPS — the instrument was not ready; the
   completed repos' artifacts are preserved as calibration-class data; the
   campaign re-registers in full after hardening. (Rationale: each erratum
   is legitimate alone; an accumulation means the run is debugging in
   production while calling it measurement.)
2. **Operator override**: any deviation from the runbook, however small,
   that is not recorded before the next repo runs, voids that repo's
   artifact (rescore required).

## D. Retirement criterion for the methodology itself (the uncomfortable row)

The witness methodology (claim classes, preregistration, errata, forecasts,
this file) is RETIRED as a recommended practice for this project's successors
if either of the following is observed and recorded:

1. The campaign fails to complete primarily because of the methodology's own
   overhead (stop-rule 1 fires on errata that exist only to service the
   protocol rather than the measurement), OR
2. Post-campaign review finds that every catch the protocol made during the
   empirical phase was of complexity the protocol itself introduced.

Either observation would mean the discipline measures itself rather than the
world — the exact failure it was built to prevent, one level up. This row
exists because a methodology that cannot specify its own disconfirming
observation has escaped empirical constraint, and no exception was earned.

## E. Completion definition (closing the last latent degree of freedom, pre-run)

**Completion = 20 valid scorings**, where valid = pipeline executed per
runbook with no unresolved erratum applying to that repo's artifacts.

**Mechanical unavailability** (the ONLY grounds for substitution, criteria
frozen now): (a) clone fails on 3 attempts across 2 days; (b) repository
deleted/private; (c) fewer than 10 tracked .py files; (d) fewer than 100
non-merge commits. Nothing else qualifies — not runtime, not inconvenient
size, not unexpected structure (those are data or errata, never exclusions).

**Replacement queue, declared now, used strictly in order, one substitution
per unavailable repo, recorded via erratum BEFORE the substitute is scored**:
1. pydantic/pydantic  2. scrapy/scrapy  3. ipython/ipython

If more than 3 substitutions are needed, the campaign is INCOMPLETE and
licenses no claims (the population was mis-declared; re-register).
The E-008 denominator is always 20: the declared-or-substituted population,
never a shrunken one.

## F. Signatures

Recorded by the assistant before repository 1; the operator countersigns by
committing this file. Amendments after first contact: errata only.
