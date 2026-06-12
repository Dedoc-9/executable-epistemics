# MOVED: encoder families now live in encoders/ (see ENCODER_CONTRACT.md).
# This shim exists because the host filesystem blocks deletion; it re-exports
# the canonical registry so stale imports fail loudly toward the right place.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from encoders import FAMILIES, enc_dep_graph, enc_ast_metrics, enc_ownership  # noqa: F401
