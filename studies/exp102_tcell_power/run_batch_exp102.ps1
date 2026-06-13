# EXP-102 Component D batch runner -- T-cell power test (Pivot A, Series 200).
# Population frozen at gate commit (REPO_DECLARATION_exp102.json, hash 970f4c4f).
# Instrument: ownership family only. scorer.py hash must equal cd6bf9a6c3f3ab36.
#
# Discipline (per HYPOTHESIS_exp102.md):
#   - Stops on first nonzero exit (SUSPEND; paste log before scoring anything else)
#   - Commits results after each clean repo (checkpoint against index corruption)
#   - compute_moderators_exp102.py MUST run before reviewing any score
#   - Skip-logic prevents re-scoring already-completed repos (safe to re-run)
#
# Run from MCL_OBS2 root:
#   powershell -File studies\exp102_tcell_power\run_batch_exp102.ps1

param(
    [string]$StartAt   = "D001",
    [string]$StopAfter = "D100"
)

$base    = "C:\Users\dillb_lzxy763\Desktop\tests_epi\exp102"
$outroot = "results_exp102"

New-Item -ItemType Directory -Force -Path $base    | Out-Null
New-Item -ItemType Directory -Force -Path $outroot | Out-Null

# -- Component D declared population (REPO_DECLARATION_exp102.json) --
$repos = @(
    [pscustomobject]@{ id="D001"; slug="nedbat/coveragepy" },
    [pscustomobject]@{ id="D002"; slug="pytest-dev/pluggy" },
    [pscustomobject]@{ id="D003"; slug="pytest-dev/pytest-mock" },
    [pscustomobject]@{ id="D004"; slug="pytest-dev/pytest-asyncio" },
    [pscustomobject]@{ id="D005"; slug="python-attrs/attrs" },
    [pscustomobject]@{ id="D006"; slug="python-attrs/cattrs" },
    [pscustomobject]@{ id="D007"; slug="pallets/jinja" },
    [pscustomobject]@{ id="D008"; slug="pallets/markupsafe" },
    [pscustomobject]@{ id="D009"; slug="pallets-eco/blinker" },
    [pscustomobject]@{ id="D010"; slug="PyCQA/pyflakes" },
    [pscustomobject]@{ id="D011"; slug="hhatto/autopep8" },
    [pscustomobject]@{ id="D012"; slug="google/yapf" },
    [pscustomobject]@{ id="D013"; slug="rthalley/dnspython" },
    [pscustomobject]@{ id="D014"; slug="benoitc/gunicorn" },
    [pscustomobject]@{ id="D015"; slug="encode/uvicorn" },
    [pscustomobject]@{ id="D016"; slug="encode/httpcore" },
    [pscustomobject]@{ id="D017"; slug="jpadilla/pyjwt" },
    [pscustomobject]@{ id="D018"; slug="pycurl/pycurl" },
    [pscustomobject]@{ id="D019"; slug="pyca/bcrypt" },
    [pscustomobject]@{ id="D020"; slug="lepture/authlib" },
    [pscustomobject]@{ id="D021"; slug="oauthlib/oauthlib" },
    [pscustomobject]@{ id="D022"; slug="pyca/pyopenssl" },
    [pscustomobject]@{ id="D023"; slug="kvesteri/sqlalchemy-utils" },
    [pscustomobject]@{ id="D024"; slug="tiangolo/sqlmodel" },
    [pscustomobject]@{ id="D025"; slug="omnilib/aiosqlite" },
    [pscustomobject]@{ id="D026"; slug="RaRe-Technologies/sqlitedict" },
    [pscustomobject]@{ id="D027"; slug="agronholm/anyio" },
    [pscustomobject]@{ id="D028"; slug="python-trio/trio" },
    [pscustomobject]@{ id="D029"; slug="grantjenks/python-sortedcontainers" },
    [pscustomobject]@{ id="D030"; slug="grantjenks/python-diskcache" },
    [pscustomobject]@{ id="D031"; slug="tobgu/pyrsistent" },
    [pscustomobject]@{ id="D032"; slug="more-itertools/more-itertools" },
    [pscustomobject]@{ id="D033"; slug="pytoolz/toolz" },
    [pscustomobject]@{ id="D034"; slug="tkem/cachetools" },
    [pscustomobject]@{ id="D035"; slug="jmcnamara/xlsxwriter" },
    [pscustomobject]@{ id="D036"; slug="scanny/python-pptx" },
    [pscustomobject]@{ id="D037"; slug="python-openxml/python-docx" },
    [pscustomobject]@{ id="D038"; slug="pikepdf/pikepdf" },
    [pscustomobject]@{ id="D039"; slug="py-pdf/pypdf" },
    [pscustomobject]@{ id="D040"; slug="pdfminer/pdfminer.six" },
    [pscustomobject]@{ id="D041"; slug="py-pdf/fpdf2" },
    [pscustomobject]@{ id="D042"; slug="yaml/pyyaml" },
    [pscustomobject]@{ id="D043"; slug="construct/construct" },
    [pscustomobject]@{ id="D044"; slug="GrahamDumpleton/wrapt" },
    [pscustomobject]@{ id="D045"; slug="mahmoud/boltons" },
    [pscustomobject]@{ id="D046"; slug="Suor/funcy" },
    [pscustomobject]@{ id="D047"; slug="amoffat/sh" },
    [pscustomobject]@{ id="D048"; slug="SethMMorton/natsort" },
    [pscustomobject]@{ id="D049"; slug="Delgan/loguru" },
    [pscustomobject]@{ id="D050"; slug="sdispater/pendulum" },
    [pscustomobject]@{ id="D051"; slug="python-humanize/humanize" },
    [pscustomobject]@{ id="D052"; slug="astanin/python-tabulate" },
    [pscustomobject]@{ id="D053"; slug="chardet/chardet" },
    [pscustomobject]@{ id="D054"; slug="jd/tenacity" },
    [pscustomobject]@{ id="D055"; slug="hynek/structlog" },
    [pscustomobject]@{ id="D056"; slug="GrahamDumpleton/mod_wsgi" },
    [pscustomobject]@{ id="D057"; slug="micheles/decorator" },
    [pscustomobject]@{ id="D058"; slug="maxbachmann/RapidFuzz" },
    [pscustomobject]@{ id="D059"; slug="LuminosoInsight/python-ftfy" },
    [pscustomobject]@{ id="D060"; slug="jquast/wcwidth" },
    [pscustomobject]@{ id="D061"; slug="ilanschnell/bitarray" },
    [pscustomobject]@{ id="D062"; slug="ifduyue/python-xxhash" },
    [pscustomobject]@{ id="D063"; slug="WoLpH/python-progressbar" },
    [pscustomobject]@{ id="D064"; slug="pypa/flit" },
    [pscustomobject]@{ id="D065"; slug="pypa/build" },
    [pscustomobject]@{ id="D066"; slug="pypa/packaging" },
    [pscustomobject]@{ id="D067"; slug="pypa/virtualenv" },
    [pscustomobject]@{ id="D068"; slug="pypa/twine" },
    [pscustomobject]@{ id="D069"; slug="pydoit/doit" },
    [pscustomobject]@{ id="D070"; slug="wntrblm/nox" },
    [pscustomobject]@{ id="D071"; slug="tox-dev/tox" },
    [pscustomobject]@{ id="D072"; slug="Zulko/moviepy" },
    [pscustomobject]@{ id="D073"; slug="imageio/imageio" },
    [pscustomobject]@{ id="D074"; slug="asweigart/pyautogui" },
    [pscustomobject]@{ id="D075"; slug="boppreh/keyboard" },
    [pscustomobject]@{ id="D076"; slug="bastibe/python-soundfile" },
    [pscustomobject]@{ id="D077"; slug="quodlibet/mutagen" },
    [pscustomobject]@{ id="D078"; slug="geopy/geopy" },
    [pscustomobject]@{ id="D079"; slug="python-visualization/folium" },
    [pscustomobject]@{ id="D080"; slug="prompt-toolkit/python-prompt-toolkit" },
    [pscustomobject]@{ id="D081"; slug="Textualize/textual" },
    [pscustomobject]@{ id="D082"; slug="jaraco/keyring" },
    [pscustomobject]@{ id="D083"; slug="skorokithakis/shortuuid" },
    [pscustomobject]@{ id="D084"; slug="html5lib/html5lib-python" },
    [pscustomobject]@{ id="D085"; slug="beetbox/beets" },
    [pscustomobject]@{ id="D086"; slug="nicfit/eyeD3" },
    [pscustomobject]@{ id="D087"; slug="asweigart/pyperclip" },
    [pscustomobject]@{ id="D088"; slug="dbader/schedule" },
    [pscustomobject]@{ id="D089"; slug="aio-libs/aiodns" },
    [pscustomobject]@{ id="D090"; slug="pyca/pyotp" },
    [pscustomobject]@{ id="D091"; slug="pypa/cachecontrol" },
    [pscustomobject]@{ id="D092"; slug="agronholm/typeguard" },
    [pscustomobject]@{ id="D093"; slug="keleshev/docopt" },
    [pscustomobject]@{ id="D094"; slug="pydantic/pydantic-settings" },
    [pscustomobject]@{ id="D095"; slug="encode/broadcaster" },
    [pscustomobject]@{ id="D096"; slug="Bogdanp/molten" },
    [pscustomobject]@{ id="D097"; slug="pytries/datrie" },
    [pscustomobject]@{ id="D098"; slug="tartley/colorama" },
    [pscustomobject]@{ id="D099"; slug="nficano/pytube" },
    [pscustomobject]@{ id="D100"; slug="python-trio/exceptiongroup" }
)

# -- Main loop --
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
    git commit -m "$($r.id) scored: $($r.slug) (EXP-102 E-005 intermediate data)"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "GIT COMMIT FAILED after $($r.id). Check index state before continuing."
        break
    }

    if ($r.id -eq $StopAfter) { break }
}

git push
Write-Host "=== batch complete ==="
Write-Host "Next: python studies\exp102_tcell_power\compute_moderators_exp102.py"
Write-Host "Then: python studies\exp102_tcell_power\analyze_exp102.py"
