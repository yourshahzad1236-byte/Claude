<#
.SYNOPSIS
    Converts every .md file in a folder into a skill .zip package.

.DESCRIPTION
    For each <file>.md the script builds <skill-name>.zip containing:

        <skill-name>/SKILL.md

    SKILL.md starts with YAML front matter holding at least `name` and
    `description`. Existing front matter is kept; missing fields are added:
      * name        - taken from the file name (lowercase, hyphens, max 64 chars)
      * description - taken from the first paragraph of the file

    Zip entries use forward slashes, so the packages open correctly on
    Linux/macOS based tools (Compress-Archive on Windows PowerShell 5.1 does not).

.EXAMPLE
    .\Convert-MdToSkillZip.ps1 -SourceDir "D:\CLAUDE_SKILLS\Oracle Developer"

.EXAMPLE
    .\Convert-MdToSkillZip.ps1 -SourceDir "D:\CLAUDE_SKILLS\Oracle Developer" -OutputDir "D:\CLAUDE_SKILLS\zips"
#>
[CmdletBinding()]
param
(
    [Parameter(Mandatory = $true)]
    [string] $SourceDir,

    [string] $OutputDir
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

if (-not (Test-Path -LiteralPath $SourceDir -PathType Container)) {
    throw "Source folder not found: $SourceDir"
}
if (-not $OutputDir) {
    $OutputDir = Join-Path $SourceDir 'skill-zips'
}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

function Get-SkillName([string] $Text) {
    $slug = $Text.ToLowerInvariant() -replace '[^a-z0-9]+', '-'
    $slug = $slug.Trim('-')
    if ($slug.Length -gt 64) { $slug = $slug.Substring(0, 64).TrimEnd('-') }
    if (-not $slug) { $slug = 'skill' }
    return $slug
}

function Get-FirstParagraph([string] $Body) {
    foreach ($block in ($Body -split '(\r?\n){2,}')) {
        $line = ($block -replace '\r?\n', ' ').Trim()
        # skip headings, code fences, tables, rules and empty blocks
        if ($line -and $line -notmatch '^(#|```|\||---|\*\*\*|<)') {
            $line = $line -replace '[*_`]', ''
            if ($line.Length -gt 1000) { $line = $line.Substring(0, 1000) }
            return $line
        }
    }
    return $null
}

function Get-FirstHeading([string] $Body) {
    $m = [regex]::Match($Body, '(?m)^#{1,6}\s+(.+?)\s*$')
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return $null
}

function ConvertTo-YamlString([string] $Value) {
    return '"' + ($Value -replace '\\', '\\' -replace '"', '\"') + '"'
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$files = Get-ChildItem -LiteralPath $SourceDir -Filter '*.md' -File

if (-not $files) {
    Write-Warning "No .md files found in $SourceDir"
    return
}

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    $content = $content.TrimStart([char]0xFEFF)

    # Split existing front matter (--- ... ---) from the body
    $frontMatter = ''
    $body = $content
    $fm = [regex]::Match($content, '\A---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|\z)', 'Singleline')
    if ($fm.Success) {
        $frontMatter = $fm.Groups[1].Value
        $body = $content.Substring($fm.Length)
    }

    $nameMatch = [regex]::Match($frontMatter, '(?m)^name\s*:\s*["'']?(.+?)["'']?\s*$')
    $descMatch = [regex]::Match($frontMatter, '(?m)^description\s*:\s*\S')

    $skillName = if ($nameMatch.Success) { Get-SkillName $nameMatch.Groups[1].Value } else { Get-SkillName $file.BaseName }

    # name must be lowercase-hyphen and match the folder: normalise it
    $lines = @()
    if ($frontMatter) {
        $lines = $frontMatter -split '\r?\n' | Where-Object { $_ -notmatch '^name\s*:' }
    }
    $newFront = @("name: $skillName")

    if (-not $descMatch.Success) {
        $desc = Get-FirstParagraph $body
        if (-not $desc) { $desc = Get-FirstHeading $body }
        if (-not $desc) { $desc = $file.BaseName }
        $newFront += "description: $(ConvertTo-YamlString $desc)"
    }
    $newFront += $lines | Where-Object { $_.Trim() -ne '' }

    $skillMd = "---`n" + ($newFront -join "`n") + "`n---`n`n" + $body.TrimStart("`r", "`n")

    $zipPath = Join-Path $OutputDir "$skillName.zip"
    if (Test-Path -LiteralPath $zipPath) { Remove-Item -LiteralPath $zipPath -Force }

    $zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
    try {
        $entry = $zip.CreateEntry("$skillName/SKILL.md", [System.IO.Compression.CompressionLevel]::Optimal)
        $writer = New-Object System.IO.StreamWriter($entry.Open(), $utf8NoBom)
        try { $writer.Write($skillMd) } finally { $writer.Dispose() }
    }
    finally {
        $zip.Dispose()
    }

    Write-Host ("{0,-45} -> {1}" -f $file.Name, $zipPath)
}

Write-Host "`nDone. $($files.Count) skill zip(s) written to $OutputDir"
