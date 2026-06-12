# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Encoder family: llm_embedding (STUB — admission conditions unmet). See ENCODER_CONTRACT.md."""

def enc_llm_embedding(repo, cache_path=None):
    """Admission conditions (ENCODER_CONTRACT.md): (1) determinism — embeddings
    must be precomputed to a cache file whose hash enters provenance; live API
    calls are not reproducible. (2) circularity — embed file CONTENT only; any
    input containing git metadata, history, or churn voids the comparison.
    Raises until a conforming cache is supplied."""
    raise NotImplementedError("provide cached content-only embeddings; see contract")
