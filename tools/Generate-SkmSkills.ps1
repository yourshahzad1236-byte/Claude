<#
 Generates one skill per schema file in D:\SKM_SCHEMA plus a master skill
 that references them all. Output format: <out>\<skill-name>\SKILL.md
 (YAML frontmatter name/description + markdown body), as used by Multica AI.

 Usage:  powershell -ExecutionPolicy Bypass -File Generate-SkmSkills.ps1
         [-Source D:\SKM_SCHEMA] [-Out D:\SKM_SCHEMA_SKILLS]
#>
param(
  [string]$Source = 'D:\SKM_SCHEMA',
  [string]$Out    = 'D:\SKM_SCHEMA_SKILLS',
  [string[]]$Ext  = @('.sql','.txt','.md','.csv','.json','.xml','.pks','.pkb','.prc','.fnc','.trg','.vw','.tab')
)
$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding($false)

function ToSlug([string]$s) {
  $s = $s.ToLower() -replace '[^a-z0-9]+','-'
  return $s.Trim('-')
}

$files = Get-ChildItem -Path $Source -Recurse -File | Where-Object { $Ext -contains $_.Extension.ToLower() }
if (-not $files) { throw "No schema files found in $Source" }
New-Item -ItemType Directory -Force -Path $Out | Out-Null

$index = @()
$used  = @{}
foreach ($f in $files) {
  $base = ToSlug ([IO.Path]::GetFileNameWithoutExtension($f.Name))
  $slug = "skm-$base"
  if ($used[$slug]) { $slug = "$slug-" + (ToSlug $f.Extension) }
  $used[$slug] = $true

  $text = [IO.File]::ReadAllText($f.FullName)
  # Objects mentioned (tables/views/packages...) for a useful description
  $objs = [regex]::Matches($text,'(?im)^\s*create\s+(?:or\s+replace\s+)?(?:global\s+temporary\s+)?(table|view|package(?:\s+body)?|procedure|function|trigger|sequence|index)\s+("?[\w\.\$#]+"?)') |
          ForEach-Object { "$($_.Groups[1].Value.ToLower()) $($_.Groups[2].Value)" } | Select-Object -Unique
  $objLine = if ($objs) { ($objs | Select-Object -First 8) -join ', ' } else { $f.Name }
  $desc = "Schema reference for $($f.BaseName) in the SKM database ($objLine). Use when a question involves these objects, their columns, keys, or relationships."
  $desc = $desc -replace '"',"'"

  $dir = Join-Path $Out $slug
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $lang = switch ($f.Extension.ToLower()) { '.json' {'json'} '.xml' {'xml'} '.md' {'markdown'} '.csv' {'csv'} default {'sql'} }
  $body = @"
---
name: $slug
description: "$desc"
---

# $($f.BaseName)

Source file: ``$($f.FullName.Substring($Source.Length).TrimStart('\'))``

## How to use
- Treat the definition below as the source of truth for names, datatypes, constraints and relationships.
- Never invent columns or tables that are not listed here.
- For objects that relate to other parts of the schema, consult ``skm-schema-master``.

## Definition

````$lang
$text
````
"@
  [IO.File]::WriteAllText((Join-Path $dir 'SKILL.md'), $body, $utf8)
  $index += [pscustomobject]@{ Slug=$slug; File=$f.Name; Desc=$objLine }
}

# Master skill referencing all others
$rows = ($index | ForEach-Object { "| ``$($_.Slug)`` | $($_.File) | $($_.Desc) |" }) -join "`n"
$master = @"
---
name: skm-schema-master
description: "Entry point for the SKM database schema. Routes to the per-file skills (one per schema file) for tables, views, packages and relationships. Use first for any SKM database question, SQL generation, or schema change."
---

# SKM Schema - Master Skill

This skill indexes every SKM schema skill. Pick the relevant skill(s), load them, then answer.

## Skill index

| Skill | Source file | Contents |
|---|---|---|
$rows

## Workflow
1. Identify which objects the request touches and load the matching skill(s) above.
2. For joins across areas, load every skill involved and follow foreign keys as defined there.
3. Write SQL / PL/SQL using only names and datatypes present in those skills.
4. If something is missing from the skills, say so and ask instead of guessing.
"@
$mdir = Join-Path $Out 'skm-schema-master'
New-Item -ItemType Directory -Force -Path $mdir | Out-Null
[IO.File]::WriteAllText((Join-Path $mdir 'SKILL.md'), $master, $utf8)

Write-Host "Created $($index.Count) skills + skm-schema-master in $Out"
