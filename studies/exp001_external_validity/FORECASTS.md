# Quantitative Pre-Run Forecasts (Brier-scored)

Upgrade of SURPRISE_PRIORS.md per the "prove we predicted it" principle:
probabilities recorded BEFORE execution, scored with a proper scoring rule
after outcomes exist. Multi-class Brier per question (lower = better;
uniform guessing over 4 outcomes scores 0.75). Forecasts are precommitments,
not evidence; they amend nothing.

## Assistant forecasts — repository 1 (psf/requests), recorded 2026-06-12 pre-run

Outcomes per family: DETECTED / UNRESOLVED_ACTIVITY_MARGIN / LEAKAGE / NOT_DETECTED

| family | DETECTED | UNRESOLVED | LEAKAGE | NOT_DETECTED |
|---|---|---|---|---|
| dep_graph | 0.15 | 0.25 | 0.30 | 0.30 |
| ast_metrics | 0.05 | 0.15 | 0.35 | 0.45 |
| ownership | 0.20 | 0.25 | 0.35 | 0.20 |

## Assistant forecasts — EXP-001 aggregate (after all 20, E-008 rule)

| POSITIVE | NEGATIVE | INCONCLUSIVE | never completes |
|---|---|---|---|
| 0.10 | 0.30 | 0.55 | 0.05 |

## Assistant forecasts — operational

P(at least one erratum required mid-campaign by instrument breakage on real
data) = 0.40 — high on purpose; E-010 is the precedent and pure-Python at
numpy scale is unbenchmarked.

## Operator forecasts (Daniel — fill with numbers summing to 1.0 per row,
## BEFORE running; then commit; scored identically)

| family | DETECTED | UNRESOLVED | LEAKAGE | NOT_DETECTED |
|---|---|---|---|---|
| dep_graph |  |  |  |  |
| ast_metrics |  |  |  |  |
| ownership |  |  |  |  |

Aggregate: POSITIVE __ / NEGATIVE __ / INCONCLUSIVE __ / never __
Operational: P(mid-campaign erratum) = __
