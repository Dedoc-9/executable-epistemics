# Run Notes — Repository 1 of 20: psf/requests

**Claim class of this file**: operational record. Per E-005, classifications
below are INTERMEDIATE DATA, not reportable results; nothing here updates
any hypothesis.

## Pin
- HEAD scored: 6f66281a1d6326b1b9c4ac09ca30de0fc4e6ef43 (branch main, full clone)
- Ground-truth chain: 1a7bbe8bdf11ce14 · E-006 filter = 3
- Precommitments pushed BEFORE scoring: commit f288e7c (forecasts, priors,
  update commitments, secondary analysis registration, E-011/E-012 fixes)

## Events (UPDATE_COMMITMENTS §A branches exercised)
1. First run CRASHED (UnicodeDecodeError, cp1252) → SUSPEND branch →
   **E-011** (361ec77d25885f5e): locale-dependent decoding; fixed to explicit
   utf-8 + deterministic degradation. Instrument erratum **1 of 3** budget.
2. Filter alarm (filter=3 < 5) → scrutiny → **E-012** (9472ce652ae5b901):
   value verified CORRECT against raw distribution (p95 of commit sizes = 3;
   74% of commits touch one file). Rule recalibrated; classified
   commitment-rule calibration, not instrument defect (operator may
   reclassify at countersign → would make count 2 of 3).
3. Rescore post-fix: pipeline clean, exit 0. Cross-platform check: operator
   (Windows/cp1252) and diagnostic (Linux/LC_ALL=C) runs agree to 6 decimals
   on every metric.

## Classifications (intermediate data, n=1, not reportable)
| family | capture | null_p95 | null_median | activity | classification |
|---|---|---|---|---|---|
| dep_graph | 0.005998 | 0.305913 | 0.103685 | 0.258783 | NOT_DETECTED |
| ast_metrics | 0.258783 | 0.477292 | — | 0.258783 | NOT_DETECTED |
| ownership | 0.477292 | 0.477292 | — | 0.258783 | NOT_DETECTED |

## Scrutiny items (resolved)
- Exact ties (ast==activity; ownership==own null_p95) traced by diagnostic
  partition inspection: ast_metrics, ownership, AND the activity baseline
  all collapse to block profile [36,1] (single-linkage giant component at
  n=37, known kernel property). Identical partitions → identical capture;
  identical sizes → identical nulls; [36,1] admits only 37 discrete capture
  values → observed==p95 is discreteness, not defect. NOT an erratum.
- Consequence recorded without interpretation: at this repo size,
  ast_metrics and ownership partitions carry ~no resolution (2 blocks).

## Surprise register
- Assistant's pre-run condition (b) for dep_graph — "capture BELOW null
  median" — FIRED (0.005998 < 0.103685). Recorded as a registered surprise
  hit. No mechanism is asserted. Recurrence across repos is observable at
  aggregate time only.

## Brier scores (assistant; realized = NOT_DETECTED ×3)
dep_graph 0.665 · ast_metrics 0.450 · ownership 0.865 · mean 0.660
(uniform-guess = 0.75; ownership forecast scored WORSE than guessing).
Operator rows were committed UNFILLED at first contact → operator repo-1
forecasts are void (contaminated); operator may still record forecasts for
repositories 2–20 before each respective run.

## Committed action (per §A, clean-pipeline row)
Record (this file) → commit → push → proceed to next declared repository.
No theoretical update. Campaign: 1/20 scored. Erratum budget: 1 of 3 used.
