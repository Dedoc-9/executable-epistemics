# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Provenance: code, environment, and seed identity for artifacts."""
import hashlib, json, os, platform


def chain_hash(obj):
    """Deterministic identity over JSON-serializable content."""
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]


def file_fingerprint(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


class Provenance(dict):
    """Environment + code + seed record. Participates in artifact identity."""

    @classmethod
    def capture(cls, code_files=(), seeds=None, extra=None):
        p = cls()
        p["python_version"] = platform.python_version()
        p["platform"] = platform.system().lower()
        p["source_date_epoch"] = os.environ.get("SOURCE_DATE_EPOCH")
        p["code_fingerprints"] = {os.path.basename(f): file_fingerprint(f)
                                  for f in code_files}
        p["seeds"] = dict(seeds or {})
        if extra:
            p.update(extra)
        return p
