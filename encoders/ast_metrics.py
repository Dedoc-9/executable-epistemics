# Copyright (C) 2026 Daniel Dillberg <bigdilly95@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Encoder family: AST metrics (syntactic shape). See ENCODER_CONTRACT.md."""
import ast, os, subprocess


def _py_files(repo):
    out = subprocess.run(["git", "-C", repo, "ls-files", "*.py"],
                         capture_output=True, text=True, check=True).stdout
    return sorted(f for f in out.split("\n") if f.strip())


def enc_ast_metrics(repo):
    sig = {}
    for f in _py_files(repo):
        try:
            src = open(os.path.join(repo, f)).read()
            tree = ast.parse(src)
        except SyntaxError:
            sig[f] = [0.0] * 5
            continue
        n_fn = sum(isinstance(n, ast.FunctionDef) for n in ast.walk(tree))
        n_cls = sum(isinstance(n, ast.ClassDef) for n in ast.walk(tree))
        n_br = sum(isinstance(n, (ast.If, ast.For, ast.While))
                   for n in ast.walk(tree))
        n_call = sum(isinstance(n, ast.Call) for n in ast.walk(tree))
        sig[f] = [n_fn / 10, n_cls / 5, n_br / 10, n_call / 20,
                  len(src.splitlines()) / 100]
    return sig

