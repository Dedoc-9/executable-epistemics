# EXP-002 Update Commitments

Inherits EXP-001 protocol (errata chain, E-006 filter, E-007 three-way
classification, E-008 aggregate rule). Additions and changes noted below.

---

## §A Per-repo branches (identical to EXP-001)

| condition | action |
|---|---|
| Pipeline clean, exit 0 | Record RUN_NOTES → commit → push → proceed |
| Nonzero exit | SUSPEND: paste log before scoring anything else |
| Filter alarm | Verify distribution; record decision; proceed or suspend |
| Implausible metric | Scrutinize; record; classify as instrument or commitment erratum |
| Ownership DETECTED by margin < 0.005 | Record razor-thin note; classification stands |

## §B Aggregate outcome (E-008, n=50, denominator always 50)

| outcome | condition | action |
|---|---|---|
| VALIDATED | point ≥ 0.60 (k ≥ 30) | Publish positive replication |
| REJECTED | Wilson_upper < 0.60 (k ≤ 23) | Publish null; retire ownership hypothesis |
| INCONCLUSIVE | 24 ≤ k ≤ 29 | Publish inconclusive; retire ownership hypothesis (see §D) |

## §C Campaign stop rules

- Erratum budget: 3 instrument errata maximum (resets from EXP-001; new campaign).
- If budget exhausted: suspend, publish protocol-failure analysis, do not report
  partial results.
- If ≥ 5 mechanical unavailability events: record as INCOMPLETE; E-008 denominator
  stays 50 (partial campaigns are not reportable).
- Mechanical unavailability: repo deleted, gone private, or scoring crashes after
  3 attempts over 2 days with no instrument fix available.
- Replacement queue (up to 3 substitutions before INCOMPLETE): declared in
  REPO_DECLARATION_exp002.json alongside primary list.

## §D Methodology retirement criterion

**Two consecutive INCONCLUSIVE results (EXP-001 wave-1 + EXP-002 wave-2) trigger
automatic retirement of the ownership hypothesis under the current instrument design.**

Retirement means:
- No further ownership waves without new theoretical grounding for why the instrument
  should produce a detection rate near 0.60.
- The dep_graph redesign (module-level encoder) may proceed independently as
  a new instrument under a new hypothesis, requiring fresh preregistration.
- The EXP-001/EXP-002 combined dataset becomes a prior for Bayesian re-analysis
  if a theoretical model is later developed.

## §E Completion definition

Completion = 50 valid scorings. Denominator is always 50 regardless of substitutions.
