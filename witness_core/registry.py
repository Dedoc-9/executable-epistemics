# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Experiment registry: precommitment device against post-hoc rationalization.

Four fields are mandatory BEFORE execution, and the failure condition is
first-class: a registry that cannot record falsification only produces
confirmations.
"""
import json, os, time
from .provenance import chain_hash, file_fingerprint


class RegistryViolation(Exception):
    pass


REQUIRED_FIELDS = ("hypothesis", "success_condition", "failure_condition",
                   "interpretation_limits")


class ExperimentRegistry:
    def __init__(self, path):
        self.path = path
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path) as fh:
                self.entries = json.load(fh)
        else:
            self.entries = []

    def _save(self):
        with open(self.path, "w") as fh:
            json.dump(self.entries, fh, indent=2, sort_keys=True)

    def register(self, experiment_id, script_path=None, **fields):
        for f in REQUIRED_FIELDS:
            if not fields.get(f):
                raise RegistryViolation(f"missing_field:{f}")
        if any(e["experiment_id"] == experiment_id for e in self.entries):
            raise RegistryViolation(f"duplicate_id:{experiment_id}")
        entry = {"experiment_id": experiment_id,
                 **{f: fields[f] for f in REQUIRED_FIELDS},
                 "script_hash": file_fingerprint(script_path)
                 if script_path else None,
                 "status": "registered", "results_hash": None}
        entry["registration_hash"] = chain_hash(entry)
        self.entries.append(entry)
        self._save()
        return entry

    def record_result(self, experiment_id, results_artifact):
        e = self._get(experiment_id)
        if e["status"] != "registered":
            raise RegistryViolation(f"already_concluded:{experiment_id}")
        e["results_hash"] = results_artifact["chain_hash"]
        e["status"] = "concluded"
        self._save()
        return e

    def _get(self, experiment_id):
        for e in self.entries:
            if e["experiment_id"] == experiment_id:
                return e
        raise RegistryViolation(f"unknown_id:{experiment_id}")

    def verify(self, experiment_id, script_path=None):
        """Registration must predate and bind the executed code."""
        e = self._get(experiment_id)
        body = {k: v for k, v in e.items()
                if k not in ("registration_hash", "status", "results_hash")}
        if chain_hash(body) != e["registration_hash"]:
            raise RegistryViolation(f"tampered:{experiment_id}")
        if script_path and e["script_hash"] and                 file_fingerprint(script_path) != e["script_hash"]:
            raise RegistryViolation(f"script_drift:{experiment_id}")
        return True
