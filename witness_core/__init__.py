# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""witness-core: a claim-boundary library (Layer 0, domain-agnostic).

Not an analytics library. Every analytical artifact carries a
machine-readable statement of what it certifies and what it does not.
"""
from .artifact import Artifact, WitnessViolation
from .provenance import Provenance, chain_hash
from .registry import ExperimentRegistry, RegistryViolation
from .errata import ErrataLog

__version__ = "0.1.0"
__all__ = ["Artifact", "WitnessViolation", "Provenance", "chain_hash",
           "ExperimentRegistry", "RegistryViolation", "ErrataLog"]
