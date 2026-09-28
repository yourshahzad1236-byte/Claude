# Packages ONE folder of .md files as ONE skill zip:
#   <skill-name>/SKILL.md          entry point (yours if the folder has one, else generated)
#   <skill-name>/<your .md files>  kept as-is, sub-folders included
# Only files inside $SourceDir are used.
param
(
    [string] $SourceDir = 'D:\CLAUDE_SKILLS\Oracle Developer',
    [string] $SkillName = 'oracle-developer',
    [string] $Description = 'Oracle developer guides: SQL, PL/SQL, APEX and related standards. Use when writing or reviewing Oracle database code.'
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$SourceDir = (Resolve-Path -LiteralPath $SourceDir).ProviderPath.TrimEnd('\', '/')
$OutputDir = Split-Path $SourceDir -Parent
$zipPath   = Join-Path $OutputDir "$SkillName.zip"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$files = @(Get-ChildItem -LiteralPath $SourceDir -Recurse -File |
    Where-Object { $_.Extension -notin @('.zip', '.skill', '.ps1') -and
                   $_.FullName -notmatch '[\\/]skill-zips[\\/]' })
$mdFiles = @($files | Where-Object { $_.Extension -eq '.md' })
if (-not $mdFiles) { throw "No .md files found in $SourceDir" }

function Get-Relative($File) { $File.FullName.Substring($SourceDir.Length + 1) -replace '\\', '/' }

$rootSkill = $files | Where-Object { (Get-Relative $_) -ieq 'SKILL.md' } | Select-Object -First 1

if ($rootSkill) {
    # Use the folder's own SKILL.md; make sure name/description are present
    $text = [IO.File]::ReadAllText($rootSkill.FullName).TrimStart([char]0xFEFF)
    $fm = [regex]::Match($text, '\A---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|\z)', 'Singleline')
    $front = if ($fm.Success) { $fm.Groups[1].Value } else { '' }
    $body  = if ($fm.Success) { $text.Substring($fm.Length) } else { $text }
    $keep  = $front -split '\r?\n' | Where-Object { $_ -notmatch '^name\s*:' -and $_.Trim() }
    if (-not ($keep -match '^description\s*:')) { $keep = @("description: `"$Description`"") + $keep }
    $skillMd = "---`nname: $SkillName`n" + ($keep -join "`n") + "`n---`n`n" + $body.TrimStart()
}
else {
    # Generate SKILL.md that indexes every .md file in the folder
    $lines = foreach ($f in $mdFiles | Sort-Object FullName) {
        $rel = Get-Relative $f
        $m = [regex]::Match([IO.File]::ReadAllText($f.FullName), '(?m)^#{1,6}\s+(.+?)\s*$')
        $title = if ($m.Success) { $m.Groups[1].Value } else { $f.BaseName }
        "- [$title]($($rel -replace ' ', '%20')) - ``$rel``"
    }
    $skillMd = @"
---
name: $SkillName
description: "$($Description -replace '"', '\"')"
---

# $SkillName

Reference guides for this skill. Read the file that matches the task before answering.

$($lines -join "`n")
"@ -replace "`r`n", "`n"
}

if (Test-Path -LiteralPath $zipPath) { Remove-Item -LiteralPath $zipPath -Force }
$zip = [IO.Compression.ZipFile]::Open($zipPath, [IO.Compression.ZipArchiveMode]::Create)
try {
    $entry = $zip.CreateEntry("$SkillName/SKILL.md")
    $w = New-Object IO.StreamWriter($entry.Open(), $utf8NoBom)
    try { $w.Write($skillMd) } finally { $w.Dispose() }

    foreach ($f in $files) {
        if ($rootSkill -and $f.FullName -eq $rootSkill.FullName) { continue }
        [IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $f.FullName, "$SkillName/$(Get-Relative $f)") | Out-Null
    }
}
finally { $zip.Dispose() }

Write-Host "Skill      : $SkillName"
Write-Host "SKILL.md   : $(if ($rootSkill) { 'your own' } else { 'generated index of ' + $mdFiles.Count + ' .md files' })"
Write-Host "Files      : $($files.Count + [int](-not $rootSkill))"
Write-Host "Zip        : $zipPath"
