# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Encoder family: registry. See ENCODER_CONTRACT.md."""
from .dep_graph import enc_dep_graph
from .ast_metrics import enc_ast_metrics
from .ownership import enc_ownership

FAMILIES = {"dep_graph": enc_dep_graph, "ast_metrics": enc_ast_metrics,
            "ownership": enc_ownership}
# llm_embedding: see llm_embedding.py — admission conditions in ENCODER_CONTRACT.md;
# not in FAMILIES until a cached, content-only embedding source is provided.
