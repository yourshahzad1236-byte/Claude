# Sets up Claude Code (VS Code extension) on an SKMCH Windows workstation for the SKMCH SDLC skills.
#
# What it does:
#   1. Checks that Git for Windows and Python are installed.
#   2. Installs the Python packages the skills use to create Word/Excel files.
#   3. Creates .claude\settings.json in your work folder so Claude can read D:\SKM_SCHEMA.
#   4. Installs the private schema skill into your personal Claude skills folder, if you have it.
#
# Run it from PowerShell (no admin rights needed):
#   powershell -ExecutionPolicy Bypass -File setup-claude-vscode.ps1 -WorkFolder "D:\MyProject"
# Optional: -SchemaDir "D:\SKM_SCHEMA" -PrivateSkill "C:\Downloads\skmch-hrd-system-context-SKMCH-PRIVATE.skill"

param(
    [Parameter(Mandatory = $true)][string]$WorkFolder,
    [string]$SchemaDir = "D:\SKM_SCHEMA",
    [string]$PrivateSkill = ""
)

$ErrorActionPreference = "Stop"
function Ok($msg)   { Write-Host "[OK]   $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "[WARN] $msg" -ForegroundColor Yellow }

# 1. Prerequisites
if (Get-Command git -ErrorAction SilentlyContinue) { Ok "Git for Windows found" }
else { Warn "Git for Windows not found. Install it from https://git-scm.com/download/win and run this script again." }

$python = $null
foreach ($cmd in @("python", "py")) {
    if (Get-Command $cmd -ErrorAction SilentlyContinue) { $python = $cmd; break }
}
if ($python) {
    Ok "Python found ($python)"
    # 2. Python packages for the Word/Excel output
    & $python -m pip install --user --quiet python-docx openpyxl
    if ($LASTEXITCODE -eq 0) { Ok "Installed python-docx and openpyxl" }
    else { Warn "pip install failed. Run manually: $python -m pip install python-docx openpyxl" }
} else {
    Warn "Python not found. Install Python 3 from https://www.python.org/downloads/ (tick 'Add to PATH'), then run this script again."
}

# 3. Project settings: schema folder access
if (-not (Test-Path $WorkFolder)) { New-Item -ItemType Directory -Path $WorkFolder | Out-Null }
if (-not (Test-Path $SchemaDir)) { Warn "Schema folder $SchemaDir not found. Copy the schema export files there." }
else { Ok "Schema folder found: $SchemaDir ($((Get-ChildItem $SchemaDir -File).Count) files)" }

$claudeDir = Join-Path $WorkFolder ".claude"
$settingsFile = Join-Path $claudeDir "settings.json"
New-Item -ItemType Directory -Force -Path $claudeDir | Out-Null

$settings = [ordered]@{}
if (Test-Path $settingsFile) {
    Copy-Item $settingsFile "$settingsFile.bak" -Force
    Ok "Backed up existing settings to settings.json.bak"
    $existing = Get-Content $settingsFile -Raw | ConvertFrom-Json
    foreach ($p in $existing.PSObject.Properties) { $settings[$p.Name] = $p.Value }
}
# env.SKMCH_SCHEMA_DIR
$envBlock = [ordered]@{}
if ($settings.Contains("env")) { foreach ($p in $settings["env"].PSObject.Properties) { $envBlock[$p.Name] = $p.Value } }
$envBlock["SKMCH_SCHEMA_DIR"] = $SchemaDir
$settings["env"] = $envBlock
# permissions.additionalDirectories += SchemaDir
$perm = [ordered]@{}
if ($settings.Contains("permissions")) { foreach ($p in $settings["permissions"].PSObject.Properties) { $perm[$p.Name] = $p.Value } }
$dirs = @()
if ($perm.Contains("additionalDirectories")) { $dirs = @($perm["additionalDirectories"]) }
if ($dirs -notcontains $SchemaDir) { $dirs += $SchemaDir }
$perm["additionalDirectories"] = $dirs
$settings["permissions"] = $perm

# Write UTF-8 without a byte-order mark so the JSON parses everywhere
$json = $settings | ConvertTo-Json -Depth 10
[System.IO.File]::WriteAllText($settingsFile, $json, (New-Object System.Text.UTF8Encoding($false)))
Ok "Wrote $settingsFile"

# 4. Private schema skill (optional; stays on this computer only)
if ($PrivateSkill) {
    if (Test-Path $PrivateSkill) {
        $skillsDir = Join-Path $env:USERPROFILE ".claude\skills"
        $target = Join-Path $skillsDir "skmch-hrd-system-context"
        New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
        if (Test-Path $target) { Remove-Item $target -Recurse -Force }
        $zip = Join-Path $env:TEMP "skmch-private-skill.zip"
        Copy-Item $PrivateSkill $zip -Force
        Expand-Archive -Path $zip -DestinationPath $skillsDir -Force
        Remove-Item $zip -Force
        if (Test-Path (Join-Path $target "SKILL.md")) { Ok "Installed private schema skill to $target" }
        else { Warn "Extracted the file, but $target\SKILL.md is missing. Check the .skill file." }
    } else { Warn "Private skill file not found: $PrivateSkill" }
}

Write-Host ""
Write-Host "Last step: open VS Code in $WorkFolder, open the Claude panel and type these two commands:" -ForegroundColor Cyan
Write-Host "  /plugin marketplace add yourshahzad1236-byte/claude"
Write-Host "  /plugin install skmch-sdlc@skmch"
Write-Host "Then restart VS Code. Test with: 'Create the SRS for these minutes' and attach meeting notes."
