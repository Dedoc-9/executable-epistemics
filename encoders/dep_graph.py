# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Encoder family: dependency graph (imports, fan-in/out). See ENCODER_CONTRACT.md."""
import ast, os, subprocess


def _py_files(repo):
    out = subprocess.run(["git", "-C", repo, "ls-files", "*.py"],
                         capture_output=True, text=True, check=True,
                         encoding="utf-8", errors="replace").stdout
    return sorted(f for f in out.split("\n") if f.strip())


def enc_dep_graph(repo):
    files = _py_files(repo)
    mods = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
    vocab = sorted(mods)
    imports = {f: set() for f in files}
    for f in files:
        try:
            tree = ast.parse(open(os.path.join(repo, f),
                                  encoding="utf-8", errors="replace").read())
        except (SyntaxError, ValueError, OSError):  # E-011: deterministic degradation
            continue
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module.split(".")[0]]
            for n in names:
                if n in mods:
                    imports[f].add(n)
    fan_in = {m: 0 for m in vocab}
    for f in files:
        for m in imports[f]:
            fan_in[m] += 1
    sig = {}
    for f in files:
        base = os.path.splitext(os.path.basename(f))[0]
        sig[f] = [1.0 if m in imports[f] else 0.0 for m in vocab] + \
                 [fan_in.get(base, 0) / max(len(files), 1)]
    return sig

