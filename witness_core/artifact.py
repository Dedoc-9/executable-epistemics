# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""The Artifact: data + provenance + claim_class + validity_scope
+ forbidden_interpretations. No field exists for a verdict; adding one
is a WitnessViolation, not a feature request."""
from .provenance import chain_hash

_VERDICT_KEYS = {"verdict", "valid", "passed", "healthy", "anomaly",
                 "correct", "legal", "safe", "approved", "score_is_good"}


class WitnessViolation(Exception):
    pass


class Artifact(dict):
    REQUIRED = ("data", "provenance", "claim_class", "validity_scope",
                "forbidden_interpretations")

    def __init__(self, data, provenance, claim_class, validity_scope,
                 forbidden_interpretations):
        super().__init__()
        self["data"] = data
        self["provenance"] = dict(provenance)
        self["claim_class"] = str(claim_class)
        self["validity_scope"] = dict(validity_scope)
        self["forbidden_interpretations"] = list(forbidden_interpretations)
        self.validate()
        self["chain_hash"] = chain_hash(
            {k: self[k] for k in self.REQUIRED})

    def validate(self):
        for k in self.REQUIRED:
            if k not in self or self[k] in (None, "", [], {}):
                raise WitnessViolation(f"missing_or_empty:{k}")
        # the interpretive firewall: no verdict-shaped keys anywhere in data
        def scan(node, path="data"):
            if isinstance(node, dict):
                for key, v in node.items():
                    if str(key).lower() in _VERDICT_KEYS:
                        raise WitnessViolation(f"verdict_field:{path}.{key}")
                    scan(v, f"{path}.{key}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    scan(v, f"{path}[{i}]")
        scan(self["data"])
        if not self["validity_scope"].get("certifies"):
            raise WitnessViolation("validity_scope.certifies required")

    def verify_chain(self):
        return self["chain_hash"] == chain_hash(
            {k: self[k] for k in self.REQUIRED})
