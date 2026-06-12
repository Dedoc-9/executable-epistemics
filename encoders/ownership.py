# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Encoder family: ownership (author distribution). See ENCODER_CONTRACT.md."""
import ast, os, subprocess


def _py_files(repo):
    out = subprocess.run(["git", "-C", repo, "ls-files", "*.py"],
                         capture_output=True, text=True, check=True).stdout
    return sorted(f for f in out.split("\n") if f.strip())


def enc_ownership(repo):
    files = _py_files(repo)
    authors = sorted(set(subprocess.run(
        ["git", "-C", repo, "log", "--pretty=%ae"],
        capture_output=True, text=True, check=True).stdout.split()))
    sig = {}
    for f in files:
        out = subprocess.run(
            ["git", "-C", repo, "log", "--pretty=%ae", "--", f],
            capture_output=True, text=True, check=True).stdout.split()
        total = max(len(out), 1)
        sig[f] = [out.count(a) / total for a in authors]
    return sig

