<#
.SYNOPSIS
    Packages Markdown skills as .zip files (<skill-name>/SKILL.md layout).

.DESCRIPTION
    Two layouts are handled automatically:

    1. Folder skill - SourceDir has a SKILL.md at its root (other .md files
       and sub-folders are reference material). The whole folder becomes ONE
       zip:  <skill-name>/SKILL.md + <skill-name>/<every other file>

    2. Loose .md files - no root SKILL.md. Every .md file (sub-folders
       included) becomes its own zip:  <skill-name>/SKILL.md

    SKILL.md front matter always ends up with `name` (lowercase-hyphen,
    matching the folder in the zip) and `description` (kept if present,
    otherwise taken from the first paragraph). Zip entries use forward
    slashes so Linux/macOS based tools can read them.

.EXAMPLE
    .\Convert-MdToSkillZip.ps1 -SourceDir "D:\CLAUDE_SKILLS" -ExcludeFolder "Oracle Developer"

.EXAMPLE
    .\Convert-MdToSkillZip.ps1 -SourceDir "D:\CLAUDE_SKILLS\Oracle Developer" -OutputDir "D:\skill-zips"
#>
[CmdletBinding()]
param
(
    [Parameter(Mandatory = $true)]
    [string] $SourceDir,

    [string] $OutputDir,

    # Top-level sub-folders of SourceDir to leave out, e.g. "Oracle Developer"
    [string[]] $ExcludeFolder = @()
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

if (-not (Test-Path -LiteralPath $SourceDir -PathType Container)) {
    throw "Source folder not found: $SourceDir"
}
$SourceDir = (Resolve-Path -LiteralPath $SourceDir).ProviderPath.TrimEnd('\', '/')
if (-not $OutputDir) {
    $OutputDir = Join-Path $SourceDir 'skill-zips'
}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$OutputDir = (Resolve-Path -LiteralPath $OutputDir).ProviderPath.TrimEnd('\', '/')

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

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

# Returns @{ Name = <skill-name>; Text = <SKILL.md text with normalised front matter> }
function ConvertTo-SkillMd([string] $Path, [string] $FallbackName) {
    $content = [System.IO.File]::ReadAllText($Path).TrimStart([char]0xFEFF)

    $frontMatter = ''
    $body = $content
    $fm = [regex]::Match($content, '\A---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|\z)', 'Singleline')
    if ($fm.Success) {
        $frontMatter = $fm.Groups[1].Value
        $body = $content.Substring($fm.Length)
    }

    $nameMatch = [regex]::Match($frontMatter, '(?m)^name\s*:\s*["'']?(.+?)["'']?\s*$')
    $descMatch = [regex]::Match($frontMatter, '(?m)^description\s*:\s*\S')

    $skillName = if ($nameMatch.Success) { Get-SkillName $nameMatch.Groups[1].Value } else { Get-SkillName $FallbackName }

    $newFront = @("name: $skillName")
    if (-not $descMatch.Success) {
        $desc = Get-FirstParagraph $body
        if (-not $desc) { $desc = Get-FirstHeading $body }
        if (-not $desc) { $desc = $FallbackName }
        $newFront += "description: $(ConvertTo-YamlString $desc)"
    }
    if ($frontMatter) {
        $newFront += $frontMatter -split '\r?\n' |
            Where-Object { $_ -notmatch '^name\s*:' -and $_.Trim() -ne '' }
    }

    $text = "---`n" + ($newFront -join "`n") + "`n---`n`n" + $body.TrimStart("`r", "`n")
    return @{ Name = $skillName; Text = $text }
}

function New-Zip([string] $ZipPath) {
    if (Test-Path -LiteralPath $ZipPath) { Remove-Item -LiteralPath $ZipPath -Force }
    return [System.IO.Compression.ZipFile]::Open($ZipPath, [System.IO.Compression.ZipArchiveMode]::Create)
}

function Add-TextEntry($Zip, [string] $EntryName, [string] $Text) {
    $entry = $Zip.CreateEntry($EntryName, [System.IO.Compression.CompressionLevel]::Optimal)
    $writer = New-Object System.IO.StreamWriter($entry.Open(), $utf8NoBom)
    try { $writer.Write($Text) } finally { $writer.Dispose() }
}

function Test-Excluded([System.IO.FileInfo] $File) {
    # never package the output folder, other zips or this script
    if ($File.FullName.StartsWith($OutputDir + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)) { return $true }
    foreach ($folder in $ExcludeFolder) {
        $prefix = (Join-Path $SourceDir $folder) + [System.IO.Path]::DirectorySeparatorChar
        if ($File.FullName.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) { return $true }
    }
    return $File.Extension -in @('.zip', '.skill', '.ps1')
}

$rootSkillMd = Join-Path $SourceDir 'SKILL.md'

if (Test-Path -LiteralPath $rootSkillMd -PathType Leaf) {
    #---------------------------------------------------------------------------
    # Layout 1: whole folder is one skill
    #---------------------------------------------------------------------------
    $skill = ConvertTo-SkillMd $rootSkillMd (Split-Path $SourceDir -Leaf)
    $zipPath = Join-Path $OutputDir "$($skill.Name).zip"
    $count = 0

    $zip = New-Zip $zipPath
    try {
        Add-TextEntry $zip "$($skill.Name)/SKILL.md" $skill.Text
        $count++

        Get-ChildItem -LiteralPath $SourceDir -Recurse -File |
            Where-Object { $_.FullName -ne $rootSkillMd -and -not (Test-Excluded $_) } |
            ForEach-Object {
                $relative = $_.FullName.Substring($SourceDir.Length + 1) -replace '\\', '/'
                [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                    $zip, $_.FullName, "$($skill.Name)/$relative",
                    [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
                $count++
            }
    }
    finally {
        $zip.Dispose()
    }

    Write-Host "Found SKILL.md in $SourceDir - packaged the whole folder as one skill."
    Write-Host "Skill name : $($skill.Name)"
    Write-Host "Files      : $count"
    Write-Host "Zip        : $zipPath"
}
else {
    #---------------------------------------------------------------------------
    # Layout 2: every .md file is its own skill
    #---------------------------------------------------------------------------
    $files = Get-ChildItem -LiteralPath $SourceDir -Filter '*.md' -File -Recurse |
        Where-Object { -not (Test-Excluded $_) }

    if (-not $files) {
        Write-Warning "No .md files found in $SourceDir (sub-folders included). Contents:"
        Get-ChildItem -LiteralPath $SourceDir -Recurse | Select-Object -First 50 |
            ForEach-Object { Write-Host ("  " + $_.FullName.Substring($SourceDir.Length + 1)) }
        return
    }

    $written = @{}
    foreach ($file in $files) {
        $skill = ConvertTo-SkillMd $file.FullName $file.BaseName
        $name = $skill.Name
        # two files may map to the same name (e.g. many README.md) - make unique
        if ($written.ContainsKey($name)) {
            $name = Get-SkillName ("{0}-{1}" -f $file.Directory.Name, $name)
            $skill.Text = $skill.Text -replace '(?m)\A---\nname: [^\n]*', "---`nname: $name"
        }
        $written[$name] = $true

        $zipPath = Join-Path $OutputDir "$name.zip"
        $zip = New-Zip $zipPath
        try { Add-TextEntry $zip "$name/SKILL.md" $skill.Text } finally { $zip.Dispose() }

        Write-Host ("{0,-55} -> {1}" -f $file.FullName.Substring($SourceDir.Length + 1), $zipPath)
    }

    Write-Host "`nDone. $($files.Count) skill zip(s) written to $OutputDir"
}
