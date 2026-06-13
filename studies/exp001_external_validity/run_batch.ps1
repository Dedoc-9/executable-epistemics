# EXP-001 campaign batch runner. Operational tooling only — touches no
# measurement code. Execution order is unregistered (population is frozen:
# REPO_DECLARATION 13076c4084f9d9cb); order here is cost-ascending.
# Discipline: stops on first nonzero exit (UPDATE_COMMITMENTS section A
# SUSPEND); commits results after each clean repo (checkpoint).
# Run from MCL_OBS2 root:  powershell -File studies\exp001_external_validity\run_batch.ps1

$base  = "C:\Users\dillb_lzxy763\Desktop\tests_epi"
$repos = @(
    "pallets/click",
    "pallets/flask",
    "tornadoweb/tornado",
    "psf/black",
    "pytest-dev/pytest",
    "fastapi/fastapi",
    "celery/celery",
    "python-pillow/Pillow",
    "sphinx-doc/sphinx",
    "sqlalchemy/sqlalchemy",
    "python/mypy",
    "scikit-learn/scikit-learn",
    "matplotlib/matplotlib",
    "numpy/numpy",
    "scipy/scipy",
    "pandas-dev/pandas",
    "django/django",
    "sympy/sympy"
    # pip handled separately below (E-013: vendored-tree exclusion)
)

foreach ($r in $repos) {
    $name = $r.Split("/")[1]
    $path = Join-Path $base $name
    if (Test-Path "results\$name\score_ownership.json") {
        Write-Host "[skip] $r already scored"; continue
    }
    if (-not (Test-Path $path)) {
        git clone "https://github.com/$r" $path
        if ($LASTEXITCODE -ne 0) {
            Write-Host "CLONE FAILED: $r -- section E criteria apply (3 attempts / 2 days) before any substitution"; break
        }
    }
    Write-Host "=== scoring $r ==="
    $t0 = Get-Date
    python validity_framework\run_study.py --repo $path --outdir "results\$name" 2>&1 | Tee-Object -FilePath "results\${name}_run.log"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "SUSPEND (section A): $r failed. STOP. Paste results\${name}_run.log before scoring anything else."; break
    }
    Write-Host ("wall time: " + ((Get-Date) - $t0))
    git add results/
    git commit -m "Repo scored: $r (E-005 intermediate data)"
}

# --- pypa/pip (repo 20/20) ---
# E-013 (b3c1e7f2a904d658): src/pip/_vendor/* excluded for population
# comparability (no other wave-1 repo carries a vendored subtree at this scale).
# Option B chosen pre-observation. Parameter --exclude-glob was pre-existing.
$pip_path = Join-Path $base "pip"
if (-not (Test-Path "results\pip\score_ownership.json")) {
    if (-not (Test-Path $pip_path)) {
        git clone "https://github.com/pypa/pip" $pip_path
        if ($LASTEXITCODE -ne 0) {
            Write-Host "CLONE FAILED: pypa/pip -- section E criteria apply"; exit 1
        }
    }
    Write-Host "=== scoring pypa/pip (E-013: --exclude-glob src/pip/_vendor/*) ==="
    $t0 = Get-Date
    python validity_framework\run_study.py --repo $pip_path --outdir "results\pip" `
        --exclude-glob "src/pip/_vendor/*" 2>&1 | Tee-Object -FilePath "results\pip_run.log"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "SUSPEND (section A): pypa/pip failed. STOP."; exit 1
    }
    Write-Host ("wall time: " + ((Get-Date) - $t0))
    git add results/
    git commit -m "Repo scored: pypa/pip (E-005 intermediate data, E-013 exclusion applied)"
} else {
    Write-Host "[skip] pypa/pip already scored"
}

git push
