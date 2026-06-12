# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Brier scorer for preregistered forecasts. Proper scoring rule:
score = sum_i (p_i - o_i)^2 over outcome classes; o is the realized
one-hot vector. Uniform-over-4 baseline = 0.75. Usage:
    python brier.py '{"DETECTED":0.15,"UNRESOLVED":0.25,"LEAKAGE":0.30,"NOT_DETECTED":0.30}' LEAKAGE
"""
import json, sys


def brier(probs: dict, realized: str) -> float:
    assert abs(sum(probs.values()) - 1.0) < 1e-6, "probabilities must sum to 1"
    assert realized in probs, f"realized outcome {realized!r} not a forecast class"
    return round(sum((p - (1.0 if k == realized else 0.0)) ** 2
                     for k, p in probs.items()), 4)


if __name__ == "__main__":
    print(brier(json.loads(sys.argv[1]), sys.argv[2]))
