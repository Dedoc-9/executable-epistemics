# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""mcl-runtime: reference implementation (Layer 1) on witness-core.

Deterministic observer-comparison instrument. Depends on witness_core;
witness_core never depends on this — the dependency direction is the
abstraction boundary.
"""
from .kernel import q_tau, vi, project, refines, merge_heights, perturb
from .runtime import analyze, register_encoder, ForbiddenTransformation
from .tools import detect_divergence, triage_content, analyze_trajectory

__version__ = "2.0.0"
__all__ = ["q_tau", "vi", "project", "refines", "merge_heights", "perturb",
           "analyze", "register_encoder", "ForbiddenTransformation",
           "detect_divergence", "triage_content", "analyze_trajectory"]
