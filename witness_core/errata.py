# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Errata: corrections as first-class, append-only artifacts."""
import json, os
from .provenance import chain_hash


class ErrataLog:
    def __init__(self, path):
        self.path = path
        self.entries = []
        if os.path.exists(path):
            with open(path) as fh:
                self.entries = json.load(fh)

    def record(self, erratum_id, supersedes, corrected_statement):
        if any(e["erratum_id"] == erratum_id for e in self.entries):
            raise ValueError(f"duplicate:{erratum_id}")
        entry = {"erratum_id": erratum_id, "supersedes": supersedes,
                 "corrected_statement": corrected_statement}
        entry["hash"] = chain_hash(entry)
        self.entries.append(entry)
        with open(self.path, "w") as fh:
            json.dump(self.entries, fh, indent=2, sort_keys=True)
        return entry
