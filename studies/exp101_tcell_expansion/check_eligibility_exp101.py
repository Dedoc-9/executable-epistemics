"""
check_eligibility_exp101.py — EXP-101 Component C candidate eligibility audit.

Uses curl.exe (bundled with Windows 10+) so system proxy settings are inherited
automatically — the same transport layer git clone uses.

Usage (no token needed for public repos up to ~60 req/hr):
    python studies\exp101_tcell_expansion\check_eligibility_exp101.py

With token (recommended — 5000 req/hr):
    $env:GH_TOKEN = "ghp_your_real_token_here"
    python studies\exp101_tcell_expansion\check_eligibility_exp101.py

Run from MCL_OBS2 root. Does NOT clone any repository.
Output: eligibility_audit_exp101.json
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

CANDIDATES = [
    ("paramiko/paramiko",      "SSH library; Jeff Forcier primary author"),
    ("fabric/fabric",          "Deployment tool; Jeff Forcier primary"),
    ("invoke/invoke",          "Task execution; Jeff Forcier primary"),
    ("cython/cython",          "Cython compiler; Stefan Behnel primary"),
    ("pyparsing/pyparsing",    "Parsing library; Paul McGuire primary"),
    ("pygments/pygments",      "Syntax highlighting; Georg Brandl era"),
    ("ipython/ipython",        "Interactive Python; Fernando Perez era"),
    ("networkx/networkx",      "Graph library; structured committer history"),
    ("statsmodels/statsmodels","Statistics; Josef Perktold + Skipper Seabold"),
    ("joblib/joblib",          "Parallel utilities; Olivier Grisel primary"),
    ("twisted/twisted",        "Networking framework; Glyph era"),
    ("numba/numba",            "JIT compiler; small core team"),
    ("pyzmq/pyzmq",            "ZeroMQ bindings; Min Ragan-Kelley primary"),
    ("bokeh/bokeh",            "Visualization; Bryan Van de Ven era"),
    ("pexpect/pexpect",        "Terminal automation; Thomas Kluyver"),
    ("gitpython/gitpython",    "Git Python interface"),
    ("plumbum/plumbum",        "CLI and remote commands"),
    ("pyserial/pyserial",      "Serial communications; Chris Liechti primary"),
    ("pytest-dev/pluggy",      "pytest plugin hook machinery"),
    ("nox/nox",                "Test session management"),
    ("docutils/docutils",      "reStructuredText; David Goodger primary"),
    ("astropy/astropy",        "Astronomy; large structured team"),
]

EXCLUDED_WAVE1 = {
    "numpy/numpy","scipy/scipy","pandas-dev/pandas","scikit-learn/scikit-learn",
    "matplotlib/matplotlib","sympy/sympy","django/django","pallets/flask",
    "psf/requests","pallets/click","pytest-dev/pytest","sphinx-doc/sphinx",
    "celery/celery","tornadoweb/tornado","python-pillow/Pillow",
    "sqlalchemy/sqlalchemy","fastapi/fastapi","psf/black","python/mypy","pypa/pip"
}
EXCLUDED_EXP002 = {
    "tortoise/tortoise-orm","coleifer/peewee","ponyorm/pony","piccolo-orm/piccolo",
    "python-gino/gino","psycopg/psycopg2","redis/redis-py","MagicStack/asyncpg",
    "pydantic/pydantic","marshmallow-code/marshmallow","pyeve/cerberus",
    "python-jsonschema/jsonschema","encode/starlette","sanic-org/sanic",
    "falconry/falcon","aio-libs/aiohttp","pallets/werkzeug","encode/httpx",
    "mitmproxy/mitmproxy","tiangolo/typer","httpie/httpie","Textualize/rich",
    "tqdm/tqdm","rq/rq","Bogdanp/dramatiq","coleifer/huey","taskiq-python/taskiq",
    "agronholm/apscheduler","PyCQA/isort","PyCQA/flake8","PyCQA/bandit",
    "PyCQA/pycodestyle","PyCQA/pylint","pre-commit/pre-commit","pypa/setuptools",
    "boto/boto3","urllib3/urllib3","pyca/cryptography","HypothesisWorks/hypothesis",
    "joke2k/faker","getsentry/responses","spulec/freezegun","kevin1024/vcrpy",
    "mkdocs/mkdocs","rubik/radon","jazzband/pip-tools","mongodb/motor",
    "elastic/elasticsearch-py","Pylons/colander","arrow-py/arrow"
}

GH_TOKEN = os.environ.get("GH_TOKEN", "").strip()

def curl_get(path: str) -> dict | None:
    """Call GitHub API via curl.exe (inherits system proxy + TLS settings)."""
    url = f"https://api.github.com{path}"
    cmd = [
        "curl.exe", "-s", "-f",        # -f = fail on HTTP errors
        "-H", "Accept: application/vnd.github+json",
        "-H", "X-GitHub-Api-Version: 2022-11-28",
    ]
    if GH_TOKEN:
        cmd += ["-H", f"Authorization: Bearer {GH_TOKEN}"]
    cmd.append(url)

    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=30)
        if r.returncode != 0:
            # curl -f returns non-zero on HTTP 4xx/5xx
            stderr = r.stderr.strip()
            print(f"    [curl] non-zero exit for {path}: rc={r.returncode} {stderr[:80]}",
                  file=sys.stderr)
            return None
        return json.loads(r.stdout)
    except subprocess.TimeoutExpired:
        print(f"    [timeout] {url}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"    [json-err] {url}: {e}", file=sys.stderr)
        return None

def count_python_files(slug: str, tree_sha: str) -> int | str:
    data = curl_get(f"/repos/{slug}/git/trees/{tree_sha}?recursive=1")
    time.sleep(0.25)
    if not data:
        return "ERROR"
    if data.get("truncated"):
        # Large repo — count what we got, flag as minimum
        n = sum(1 for f in data.get("tree", [])
                if f.get("type") == "blob" and f.get("path","").endswith(".py"))
        return f"≥{n}(truncated)"
    return sum(1 for f in data.get("tree", [])
               if f.get("type") == "blob" and f.get("path","").endswith(".py"))

def count_commits_approx(slug: str) -> int:
    """Sum contributor commit counts (paged)."""
    total, page = 0, 1
    while True:
        data = curl_get(f"/repos/{slug}/contributors?per_page=100&page={page}&anon=true")
        time.sleep(0.3)
        if not data or not isinstance(data, list) or len(data) == 0:
            break
        total += sum(c.get("contributions", 0) for c in data if isinstance(c, dict))
        if len(data) < 100:
            break
        page += 1
    return total

def audit(slug: str, notes: str) -> dict:
    print(f"\n  [{slug}]")
    r = {"slug": slug, "notes": notes, "eligibility": "PENDING",
         "fail_reason": "", "archived": None, "language": None,
         "n_commits_approx": None, "n_python_files": None}

    if slug in EXCLUDED_WAVE1:
        r.update(eligibility="EXCLUDED", fail_reason="EXP-001 wave-1"); print("    EXCLUDED (wave-1)"); return r
    if slug in EXCLUDED_EXP002:
        r.update(eligibility="EXCLUDED", fail_reason="EXP-002 cohort"); print("    EXCLUDED (EXP-002)"); return r

    repo = curl_get(f"/repos/{slug}")
    time.sleep(0.3)
    if repo is None:
        r.update(eligibility="FAILED", fail_reason="API unreachable or 404"); print("    FAILED: API unreachable"); return r

    r["archived"] = repo.get("archived", False)
    r["language"] = repo.get("language", "")

    if r["archived"]:
        r.update(eligibility="FAILED", fail_reason=f"archived {repo.get('pushed_at','')}"); print("    FAILED: archived"); return r

    if r["language"] != "Python":
        print(f"    NOTE: primary language={r['language']} — may still qualify (e.g. Cython)")

    # Python file count
    branch = curl_get(f"/repos/{slug}/branches/{repo.get('default_branch','main')}")
    time.sleep(0.3)
    if branch:
        tree_sha = branch.get("commit",{}).get("commit",{}).get("tree",{}).get("sha","")
        if tree_sha:
            r["n_python_files"] = count_python_files(slug, tree_sha)

    if isinstance(r["n_python_files"], int) and r["n_python_files"] < 50:
        r.update(eligibility="FAILED", fail_reason=f"only {r['n_python_files']} Python files < 50")
        print(f"    FAILED: {r['n_python_files']} Python files"); return r

    # Commit count
    n_c = count_commits_approx(slug)
    r["n_commits_approx"] = n_c
    if n_c < 500:
        r.update(eligibility="FAILED", fail_reason=f"~{n_c} commits < 500")
        print(f"    FAILED: ~{n_c} commits"); return r

    if r["eligibility"] == "PENDING":
        r["eligibility"] = "CONFIRMED"
    print(f"    {r['eligibility']}: ~{n_c} commits | {r['n_python_files']} py files | lang={r['language']}")
    return r


def main():
    if not GH_TOKEN:
        print("[INFO] No GH_TOKEN — using unauthenticated (60 req/hr). To set:")
        print("       $env:GH_TOKEN = 'ghp_your_real_token'\n")
    else:
        print(f"[INFO] Using GH_TOKEN (length={len(GH_TOKEN)})\n")

    results = [audit(slug, notes) for slug, notes in CANDIDATES]

    confirmed = [r for r in results if r["eligibility"] == "CONFIRMED"]
    failed    = [r for r in results if r["eligibility"] == "FAILED"]
    needs_man = [r for r in results if r["eligibility"] == "NEEDS_MANUAL"]

    print(f"\n{'='*60}")
    print(f"CONFIRMED ({len(confirmed)}): {[r['slug'] for r in confirmed]}")
    if failed:
        print(f"FAILED    ({len(failed)}):    {[(r['slug'], r['fail_reason']) for r in failed]}")
    if needs_man:
        print(f"MANUAL    ({len(needs_man)}):    {[r['slug'] for r in needs_man]}")
    print(f"\nComponent C candidate n: {len(confirmed)}")

    out = Path("studies/exp101_tcell_expansion/eligibility_audit_exp101.json")
    out.write_text(json.dumps({"candidates": results,
                               "n_confirmed": len(confirmed),
                               "n_failed": len(failed)}, indent=2),
                  encoding="utf-8")
    print(f"Written: {out}")


if __name__ == "__main__":
    main()
