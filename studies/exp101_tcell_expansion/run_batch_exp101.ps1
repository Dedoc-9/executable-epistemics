# EXP-101 Component C batch runner — T-cell targeted expansion.
# Population frozen at commit 5864fb2 (REPO_DECLARATION_exp101.json, hash 8f17a0c4).
# Instrument: ownership family only. scorer.py hash must equal cd6bf9a6c3f3ab36.
#
# Discipline (per HYPOTHESIS_exp101.md + UPDATE_COMMITMENTS protocol):
#   - Stops on first nonzero exit (SUSPEND; paste log before scoring anything else)
#   - Commits results after each clean repo (checkpoint against index corruption)
#   - compute_moderators_exp101.py MUST run before reviewing any score
#   - Skip-logic prevents re-scoring already-completed repos (safe to re-run)
#
# Run from MCL_OBS2 root:
#   powershell -File studies\exp101_tcell_expansion\run_batch_exp101.ps1

param(
    [string]$StartAt   = "C001",
    [string]$StopAfter = "C022"
)

$base    = "C:\Users\dillb_lzxy763\Desktop\tests_epi\exp101"
$outroot = "results_exp101"

New-Item -ItemType Directory -Force -Path $base    | Out-Null
New-Item -ItemType Directory -Force -Path $outroot | Out-Null

# ── Component C declared population (REPO_DECLARATION_exp101.json, 5864fb2) ──
$repos = @(
    [pscustomobject]@{ id="C001"; slug="paramiko/paramiko" },
    [pscustomobject]@{ id="C002"; slug="cython/cython" },
    [pscustomobject]@{ id="C003"; slug="pyparsing/pyparsing" },
    [pscustomobject]@{ id="C004"; slug="pygments/pygments" },
    [pscustomobject]@{ id="C005"; slug="ipython/ipython" },
    [pscustomobject]@{ id="C006"; slug="networkx/networkx" },
    [pscustomobject]@{ id="C007"; slug="pyinvoke/invoke" },
    [pscustomobject]@{ id="C008"; slug="statsmodels/statsmodels" },
    [pscustomobject]@{ id="C009"; slug="joblib/joblib" },
    [pscustomobject]@{ id="C010"; slug="twisted/twisted" },
    [pscustomobject]@{ id="C011"; slug="numba/numba" },
    [pscustomobject]@{ id="C012"; slug="zeromq/pyzmq" },
    [pscustomobject]@{ id="C013"; slug="bokeh/bokeh" },
    [pscustomobject]@{ id="C014"; slug="pexpect/pexpect" },
    [pscustomobject]@{ id="C015"; slug="gitpython-developers/GitPython" },
    [pscustomobject]@{ id="C016"; slug="tomerfiliba/plumbum" },
    [pscustomobject]@{ id="C017"; slug="pyserial/pyserial" },
    [pscustomobject]@{ id="C018"; slug="astropy/astropy" },
    [pscustomobject]@{ id="C019"; slug="docutils/docutils" },
    [pscustomobject]@{ id="C020"; slug="Supervisor/supervisor" },
    [pscustomobject]@{ id="C021"; slug="giampaolo/psutil" },
    [pscustomobject]@{ id="C022"; slug="dateutil/dateutil" }
)

# ── Main loop ─────────────────────────────────────────────────────────────────
$active = $false
foreach ($r in $repos) {
    if ($r.id -eq $StartAt) { $active = $true }
    if (-not $active) { Write-Host "[range-skip] $($r.id) $($r.slug)"; continue }

    $name    = $r.slug.Split("/")[1]
    $outdir  = "$outroot\$name"
    $cloneto = Join-Path $base $name

    if (Test-Path "$outdir\score_ownership.json") {
        Write-Host "[skip] $($r.id) $($r.slug) already scored"
        if ($r.id -eq $StopAfter) { break }
        continue
    }

    if (-not (Test-Path $cloneto)) {
        Write-Host "--- cloning $($r.slug) ---"
        git clone "https://github.com/$($r.slug)" $cloneto
        if ($LASTEXITCODE -ne 0) {
            Write-Host "CLONE FAILED: $($r.id) $($r.slug)"
            Write-Host "SUSPEND (mechanical unavailability): attempt 1 of 3. Retry over 2 days before substituting."
            break
        }
    }

    Write-Host "=== $($r.id) scoring $($r.slug) ==="
    New-Item -ItemType Directory -Force -Path $outdir | Out-Null
    $t0 = Get-Date
    python validity_framework\run_study.py `
        --repo $cloneto `
        --outdir $outdir `
        2>&1 | Tee-Object -FilePath "$outdir\run.log"

    if ($LASTEXITCODE -ne 0) {
        Write-Host "SUSPEND (nonzero exit): $($r.id) $($r.slug). STOP."
        Write-Host "Paste $outdir\run.log before scoring anything else."
        break
    }
    Write-Host ("wall time: " + ((Get-Date) - $t0))

    git add $outdir
    git commit -m "$($r.id) scored: $($r.slug) (EXP-101 E-005 intermediate data)"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "GIT COMMIT FAILED after $($r.id). Check index state before continuing."
        break
    }

    if ($r.id -eq $StopAfter) { break }
}

git push
Write-Host "=== batch complete ==="
Write-Host "Next: python studies\exp101_tcell_expansion\compute_moderators_exp101.py"
Write-Host "Then: python studies\exp101_tcell_expansion\analyze_exp101.py"
