# EXP-002 campaign batch runner — ownership replication, n=50.
# Population frozen at commit e36d2dd (declaration_hash 8d2577eed52d16068ea5c1c5767af5a8e6d00e1fd94ae2731b85ed9bdca1df25).
# Three families are computed (existing instrument, no code changes) but only
# ownership is classified in RUN_NOTES and counted in E-008.  dep_graph and
# ast_metrics output files are written but are NOT reportable in EXP-002.
#
# Discipline (UPDATE_COMMITMENTS_exp002.md §A):
#   - Stops on first nonzero exit (SUSPEND; paste log before scoring anything else)
#   - Commits results after each clean repo (checkpoint against index corruption)
#   - Skip-logic prevents re-scoring already-completed repos (safe to re-run)
#
# Run from MCL_OBS2 root:
#   powershell -File studies\exp002_ownership_replication\run_batch_exp002.ps1
#
# To run a sub-range (e.g. R001-R010 only):
#   powershell -File ... -StartAt R001 -StopAfter R010

param(
    [string]$StartAt   = "R001",
    [string]$StopAfter = "R050"
)

$base    = "C:\Users\dillb_lzxy763\Desktop\tests_epi\exp002"
$outroot = "results_exp002"

# Ensure clone root exists
New-Item -ItemType Directory -Force -Path $base | Out-Null
New-Item -ItemType Directory -Force -Path $outroot | Out-Null

# ── Declared population (REPO_DECLARATION_exp002.json, e36d2dd) ──────────────
# Format: id, slug, optional exclude_glob
$repos = @(
    [pscustomobject]@{ id="R001"; slug="tortoise/tortoise-orm" },
    [pscustomobject]@{ id="R002"; slug="coleifer/peewee" },
    [pscustomobject]@{ id="R003"; slug="ponyorm/pony" },
    [pscustomobject]@{ id="R004"; slug="piccolo-orm/piccolo" },
    [pscustomobject]@{ id="R005"; slug="python-gino/gino" },
    [pscustomobject]@{ id="R006"; slug="psycopg/psycopg2" },
    [pscustomobject]@{ id="R007"; slug="redis/redis-py" },
    [pscustomobject]@{ id="R008"; slug="MagicStack/asyncpg" },
    [pscustomobject]@{ id="R009"; slug="pydantic/pydantic" },
    [pscustomobject]@{ id="R010"; slug="marshmallow-code/marshmallow" },
    [pscustomobject]@{ id="R011"; slug="pyeve/cerberus" },
    [pscustomobject]@{ id="R012"; slug="python-jsonschema/jsonschema" },
    [pscustomobject]@{ id="R013"; slug="encode/starlette" },
    [pscustomobject]@{ id="R014"; slug="sanic-org/sanic" },
    [pscustomobject]@{ id="R015"; slug="falconry/falcon" },
    [pscustomobject]@{ id="R016"; slug="aio-libs/aiohttp" },
    [pscustomobject]@{ id="R017"; slug="pallets/werkzeug" },
    [pscustomobject]@{ id="R018"; slug="encode/httpx" },
    [pscustomobject]@{ id="R019"; slug="mitmproxy/mitmproxy" },
    [pscustomobject]@{ id="R020"; slug="tiangolo/typer" },
    [pscustomobject]@{ id="R021"; slug="httpie/httpie" },
    [pscustomobject]@{ id="R022"; slug="Textualize/rich" },
    [pscustomobject]@{ id="R023"; slug="tqdm/tqdm" },
    [pscustomobject]@{ id="R024"; slug="rq/rq" },
    [pscustomobject]@{ id="R025"; slug="Bogdanp/dramatiq" },
    [pscustomobject]@{ id="R026"; slug="coleifer/huey" },
    [pscustomobject]@{ id="R027"; slug="taskiq-python/taskiq" },
    [pscustomobject]@{ id="R028"; slug="agronholm/apscheduler" },
    [pscustomobject]@{ id="R029"; slug="PyCQA/isort" },
    [pscustomobject]@{ id="R030"; slug="PyCQA/flake8" },
    [pscustomobject]@{ id="R031"; slug="PyCQA/bandit" },
    [pscustomobject]@{ id="R032"; slug="PyCQA/pycodestyle" },
    [pscustomobject]@{ id="R033"; slug="PyCQA/pylint" },
    [pscustomobject]@{ id="R034"; slug="pre-commit/pre-commit" },
    [pscustomobject]@{ id="R035"; slug="pypa/setuptools" },
    [pscustomobject]@{ id="R036"; slug="boto/boto3" },
    [pscustomobject]@{ id="R037"; slug="urllib3/urllib3" },
    [pscustomobject]@{ id="R038"; slug="psf/cryptography" },
    [pscustomobject]@{ id="R039"; slug="HypothesisWorks/hypothesis" },
    [pscustomobject]@{ id="R040"; slug="joke2k/faker" },
    [pscustomobject]@{ id="R041"; slug="getsentry/responses" },
    [pscustomobject]@{ id="R042"; slug="spulec/freezegun" },
    [pscustomobject]@{ id="R043"; slug="kevin1024/vcrpy" },
    [pscustomobject]@{ id="R044"; slug="mkdocs/mkdocs" },
    [pscustomobject]@{ id="R045"; slug="rubik/radon" },
    [pscustomobject]@{ id="R046"; slug="jazzband/pip-tools" },
    [pscustomobject]@{ id="R047"; slug="mongodb/motor" },
    [pscustomobject]@{ id="R048"; slug="elastic/elasticsearch-py" },
    [pscustomobject]@{ id="R049"; slug="Pylons/colander" },
    [pscustomobject]@{ id="R050"; slug="arrow-py/arrow" }
)

# ── Main loop ─────────────────────────────────────────────────────────────────
$active = $false
foreach ($r in $repos) {
    if ($r.id -eq $StartAt) { $active = $true }
    if (-not $active) { Write-Host "[range-skip] $($r.id) $($r.slug)"; continue }

    $name    = $r.slug.Split("/")[1]
    $outdir  = "$outroot\$name"
    $cloneto = Join-Path $base $name

    # Skip-logic: ownership score already present
    if (Test-Path "$outdir\score_ownership.json") {
        Write-Host "[skip] $($r.id) $($r.slug) already scored"
        if ($r.id -eq $StopAfter) { break }
        continue
    }

    # Clone if needed
    if (-not (Test-Path $cloneto)) {
        Write-Host "--- cloning $($r.slug) ---"
        git clone "https://github.com/$($r.slug)" $cloneto
        if ($LASTEXITCODE -ne 0) {
            Write-Host "CLONE FAILED: $($r.id) $($r.slug)"
            Write-Host "SUSPEND (§C mechanical unavailability): attempt 1 of 3. Retry over 2 days before substituting."
            break
        }
    }

    # Score
    Write-Host "=== $($r.id) scoring $($r.slug) ==="
    New-Item -ItemType Directory -Force -Path $outdir | Out-Null
    $t0 = Get-Date
    python validity_framework\run_study.py `
        --repo $cloneto `
        --outdir $outdir `
        2>&1 | Tee-Object -FilePath "$outdir\run.log"

    if ($LASTEXITCODE -ne 0) {
        Write-Host "SUSPEND (§A nonzero exit): $($r.id) $($r.slug). STOP."
        Write-Host "Paste $outdir\run.log before scoring anything else."
        break
    }
    Write-Host ("wall time: " + ((Get-Date) - $t0))

    # Checkpoint commit after each clean repo
    git add $outdir
    git commit -m "$($r.id) scored: $($r.slug) (EXP-002 E-005 intermediate data)"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "GIT COMMIT FAILED after $($r.id). Check index state before continuing."
        break
    }

    if ($r.id -eq $StopAfter) { break }
}

git push
Write-Host "=== batch complete. Run RUN_NOTES for each scored repo, then commit notes. ==="
