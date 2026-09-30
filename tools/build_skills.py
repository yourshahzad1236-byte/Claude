#!/usr/bin/env python3
"""Build Multica-style skills (SKILL.md + references/) from Oracle DDL export files."""
import re, sys, os, collections

AUDIT = {'user_id','terminal','trn_date','original_user_id','original_terminal',
         'original_trn_date','org_id','zon_id','loc_id','ws_sync_date'}
BOILER = re.compile(r'This column contains (ORG_ID|ZON_ID|LOC_ID|WS_SYNC_DATE)', re.I)

def split_stmts(text):
    """Yield (kind, name, body) for top-level create/alter/comment statements."""
    return text

def parse(path, schema):
    text = open(path, encoding='utf-8', errors='replace').read()
    tables = collections.OrderedDict()
    # tables
    for m in re.finditer(r'^create (?:global temporary )?table (\w+)\.("?[\w$#]+"?)\s*\n\((.*?)\n\)', text, re.I|re.M|re.S):
        name = m.group(2).strip('"').upper()
        cols = []
        for line in m.group(3).split('\n'):
            line = line.strip().rstrip(',')
            if not line: continue
            cm = re.match(r'("?[\w$#]+"?)\s+(.*)$', line)
            if not cm: continue
            cname = cm.group(1).strip('"')
            rest = cm.group(2)
            nn = bool(re.search(r'\bnot null\b', rest, re.I))
            rest = re.sub(r'\s*\bnot null\b', '', rest, flags=re.I).strip()
            cols.append({'name': cname.upper(), 'type': rest, 'nn': nn, 'comment': ''})
        tables[name] = {'cols': cols, 'pk': None, 'uk': [], 'fk': [], 'ck': [], 'comment': '',
                        'triggers': [], 'indexes': []}
    # table & column comments
    for m in re.finditer(r"^comment on table \w+\.(\w+)\s*\n\s*is '((?:[^']|'')*)'", text, re.I|re.M):
        t = tables.get(m.group(1).upper())
        if t: t['comment'] = m.group(2).replace("''", "'")
    for m in re.finditer(r"^comment on column \w+\.(\w+)\.(\w+)\s*\n\s*is '((?:[^']|'')*)'", text, re.I|re.M):
        t = tables.get(m.group(1).upper())
        if not t: continue
        c = m.group(3).replace("''", "'").strip()
        if BOILER.search(c): continue
        for col in t['cols']:
            if col['name'] == m.group(2).upper(): col['comment'] = c
    # constraints
    for m in re.finditer(r'^alter table \w+\.(\w+)\s*\n\s*add constraint (\w+)\s+(primary key|unique|foreign key|check)\s*\(([^;]*?)\)(?:\s*\n\s*references (\w+\.\w+)\s*\(([^)]*)\))?', text, re.I|re.M|re.S):
        t = tables.get(m.group(1).upper())
        if not t: continue
        kind = m.group(3).lower(); cols = re.sub(r'\s+', ' ', m.group(4)).upper()
        rest = text[m.end():m.end()+80].lower()
        disabled = bool(re.match(r'\s*\n\s*disable', rest))
        if kind == 'primary key': t['pk'] = (m.group(2), cols)
        elif kind == 'unique': t['uk'].append((m.group(2), cols))
        elif kind == 'foreign key':
            if not m.group(5): continue
            t['fk'].append((m.group(2), cols, m.group(5).upper(), re.sub(r'\s+',' ',m.group(6)).upper(), disabled))
        else: t['ck'].append((m.group(2), cols))
    # indexes
    for m in re.finditer(r'^create (unique |bitmap )?index (\w+)\.(\w+)\s*\n\s*on (\w+)\.(\w+)\s*\((.*?)\)', text, re.I|re.M|re.S):
        t = tables.get(m.group(5).upper())
        if t: t['indexes'].append((m.group(3).upper(), re.sub(r'\s+',' ',m.group(6)).upper(), bool(m.group(1))))
    # triggers
    for m in re.finditer(r'^create or replace trigger \w+\.(\w+)\s*\n\s*((?:before|after|instead of)[^\n]*?) on (?:\w+\.)?(\w+)', text, re.I|re.M):
        t = tables.get(m.group(3).upper())
        if t: t['triggers'].append((m.group(1).upper(), re.sub(r'\s+',' ',m.group(2)).lower()))
    # sequences
    seqs = [m.group(1).upper() for m in re.finditer(r'^create sequence \w+\.(\w+)', text, re.I|re.M)
            if not m.group(1).upper().startswith('ISEQ$$')]
    # synonyms
    syns = [(m.group(1).upper(), m.group(2).upper()) for m in re.finditer(
        r'^create or replace synonym \w+\.(\w+)\s*\n\s*for (\S+?);', text, re.I|re.M)]
    # views
    views = collections.OrderedDict()
    for m in re.finditer(r'^create or replace (?:force )?view (\w+)\.(\w+)(.*?)^\s*;?\s*$(?=\s*\n(?:prompt|create|comment|alter|$))', text, re.I|re.M|re.S):
        views[m.group(2).upper()] = (m.group(0)).strip()
    # packages (spec), procs, functions
    pkgs = collections.OrderedDict()
    for m in re.finditer(r'^create or replace package (\w+)\.(\w+)\s+(?:authid \w+\s+)?(?:is|as)\b(.*?)^end(?: \w+)?;', text, re.I|re.M|re.S):
        pkgs[m.group(2).upper()] = m.group(0).strip()
    procs = collections.OrderedDict()
    for m in re.finditer(r'^create or replace (procedure|function) (\w+)\.(\w+)(.*?)\b(?:is|as)\b', text, re.I|re.M|re.S):
        procs[m.group(3).upper()] = (m.group(1).lower(), re.sub(r'[ \t]+$', '', m.group(0).strip(), flags=re.M))
    return dict(tables=tables, seqs=seqs, syns=syns, views=views, pkgs=pkgs, procs=procs)

def esc(s): return s.replace('|', '\\|').replace('\n', ' ')

def write_tables_md(schema, d, fh):
    fh.write(f"# {schema} tables\n\nAudit/multi-location columns (user_id, terminal, trn_date, original_user_id, "
             f"original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column "
             f"lists below; every table has them unless noted.\n\n")
    for name, t in d['tables'].items():
        fh.write(f"## {schema}.{name}\n")
        if t['comment']: fh.write(f"{t['comment']}\n")
        audit_present = sum(1 for c in t['cols'] if c['name'].lower() in AUDIT)
        fh.write("\n| Column | Type | Null | Comment |\n|---|---|---|---|\n")
        for c in t['cols']:
            if c['name'].lower() in AUDIT: continue
            fh.write(f"| {c['name']} | {esc(c['type'])} | {'N' if c['nn'] else 'Y'} | {esc(c['comment'])} |\n")
        fh.write("\n")
        if audit_present == 0: fh.write("_No standard audit columns._\n\n")
        if t['pk']: fh.write(f"- **PK** `{t['pk'][0]}`: {t['pk'][1]}\n")
        for n, c in t['uk']: fh.write(f"- **UK** `{n}`: {c}\n")
        for n, c, rt, rc, dis in t['fk']:
            fh.write(f"- **FK** `{n}`: ({c}) -> {rt}({rc}){' [disabled]' if dis else ''}\n")
        for n, c in t['ck']: fh.write(f"- **CHECK** `{n}`: {c}\n")
        for n, c, u in t['indexes']: fh.write(f"- **INDEX** `{n}`{' (unique)' if u else ''}: {c}\n")
        if t['triggers']:
            fh.write("- **Triggers**: " + ", ".join(f"`{n}` ({e})" for n, e in t['triggers']) + "\n")
        fh.write("\n")

def build(schema, path, out, purpose):
    d = parse(path, schema)
    slug = f"skm-{schema.lower()}-schema"
    sd = os.path.join(out, slug); rd = os.path.join(sd, 'references'); os.makedirs(rd, exist_ok=True)
    with open(os.path.join(rd, 'tables.md'), 'w') as fh: write_tables_md(schema, d, fh)
    with open(os.path.join(rd, 'code-objects.md'), 'w') as fh:
        fh.write(f"# {schema} code objects\n\n")
        fh.write(f"## Sequences\n" + ("\n".join(f"- {s}" for s in d['seqs']) or "_none_") + "\n\n")
        fh.write(f"## Packages (specifications)\n\n")
        for n, body in d['pkgs'].items(): fh.write(f"### {schema}.{n}\n```sql\n{body}\n```\n\n")
        fh.write(f"## Standalone procedures and functions (headers)\n\n")
        for n, (k, hdr) in d['procs'].items(): fh.write(f"### {schema}.{n} ({k})\n```sql\n{hdr}\n```\n\n")
    with open(os.path.join(rd, 'views.md'), 'w') as fh:
        fh.write(f"# {schema} views\n\n")
        for n, body in d['views'].items(): fh.write(f"## {schema}.{n}\n```sql\n{body}\n```\n\n")
    with open(os.path.join(rd, 'synonyms.md'), 'w') as fh:
        fh.write(f"# {schema} synonyms\n\n| Synonym | Target |\n|---|---|\n")
        for a, b in d['syns']: fh.write(f"| {a} | {b} |\n")
    # SKILL.md with table index
    idx = "\n".join(f"- `{n}`" + (f" - {t['comment']}" if t['comment'] else '') for n, t in d['tables'].items())
    fk_out = collections.Counter()
    for t in d['tables'].values():
        for fk in t['fk']:
            s = fk[2].split('.')[0]
            if s != schema: fk_out[s] += 1
    xs = ", ".join(f"{s} ({n} FKs)" for s, n in fk_out.most_common()) or "none found"
    desc = (f"{schema} Oracle schema of the SKM database: {purpose} Use for any question, SQL, PL/SQL or "
            f"change involving {schema}.* tables ({len(d['tables'])}), views ({len(d['views'])}), packages "
            f"({len(d['pkgs'])}) - columns, keys, relationships, comments.")
    with open(os.path.join(sd, 'SKILL.md'), 'w') as fh:
        fh.write(f"""---
name: {slug}
description: "{desc.replace('"', "'")}"
---

# {schema} schema

{purpose}

**Counts:** {len(d['tables'])} tables, {len(d['views'])} views, {len(d['pkgs'])} packages, {len(d['procs'])} standalone procedures/functions, {len(d['seqs'])} sequences, {len(d['syns'])} synonyms.

## References (read only what you need)
- `references/tables.md` - every table: columns, types, nullability, column comments, PK/UK/FK/CHECK, indexes, triggers. **Search it by `## {schema}.TABLE_NAME`.**
- `references/views.md` - view definitions.
- `references/code-objects.md` - package specs, procedure/function headers, sequences.
- `references/synonyms.md` - synonym -> target mapping (many synonyms point at *_AUDIT schemas and are used by delete-audit triggers).

## Conventions
- Standard audit columns on nearly every table: `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_USER_ID, ORIGINAL_TERMINAL, ORIGINAL_TRN_DATE`.
- Multi-location columns: `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` (location where the record was first created).
- Insert/update/delete triggers fill the audit columns and copy deleted rows to audit tables through `SYN_*` synonyms - do not set audit columns manually.
- Flag columns are usually `CHAR/VARCHAR2(1)` with `'Y'/'N'` (e.g. `ACTIVE`).
- Cross-schema FKs from this schema point to: {xs}.

## Rules
- Use only tables/columns that exist in `references/tables.md`; never guess names.
- Qualify objects with the schema (`{schema}.TABLE`).
- For joins across schemas load the master skill `skm-schema-master` and the other schema skill.

## Table index
{idx}
""")
    return slug, d

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    cfg = [
      ('DEFINITIONS', '657baf8c-DEFINITIONS_SCHEMA.txt', 'master/lookup data (LOVs, definitions, locations, services, CPT, patients, abbreviations) shared by the other schemas.'),
      ('HRD', '964a4c8a-HRD_SCHEMA.txt', 'human resource data (employees, applicants, leave, PA/appraisal, recruitment and related HR processes).'),
      ('PAYROLL', 'b1172d2e-PAYROLL_SCHMA.txt', 'payroll (pay, loans, expenses, employee pay components, performance income and related processing).'),
      ('RFID', '6d7471d2-RFID_SCHEMA.txt', 'RFID/attendance machines, attendance records, machine access rights and door logs.'),
    ]
    summ = []
    for schema, fn, purpose in cfg:
        slug, d = build(schema, os.path.join(src, fn), out, purpose)
        summ.append((schema, slug, d, purpose)); print(schema, len(d['tables']), len(d['views']), len(d['pkgs']), len(d['procs']))
    rows = "\n".join(f"| `{s}` | {sch} | {len(d['tables'])} | {len(d['views'])} | {len(d['pkgs'])} | {p} |" for sch, s, d, p in summ)
    md = os.path.join(out, 'skm-schema-master'); os.makedirs(md, exist_ok=True)
    open(os.path.join(md, 'SKILL.md'), 'w').write(f"""---
name: skm-schema-master
description: "Entry point for the SKM Oracle database (schemas DEFINITIONS, HRD, PAYROLL, RFID). Routes to the per-schema skills and explains cross-schema relationships. Use first for any SKM database question, SQL/PL-SQL generation, reporting query or schema change."
---

# SKM Schema - Master Skill

The SKM database is split in four Oracle schemas. Each has its own skill; load the one(s) that match the request.

| Skill | Schema | Tables | Views | Packages | Purpose |
|---|---|---|---|---|---|
{rows}

## How to route
1. Identify the business area: lookup/master data -> `skm-definitions-schema`; employees/HR -> `skm-hrd-schema`; salary/loans/expenses -> `skm-payroll-schema`; attendance machines/RFID -> `skm-rfid-schema`.
2. Open that skill's `references/tables.md` and find the table (`## SCHEMA.TABLE`). Read columns, PK and FK lines.
3. Follow `FK` lines across schemas: `DEFINITIONS` is referenced by the others for lookup values; `HRD` employees link to `PAYROLL` and `RFID` records. Load the target schema's skill for the referenced table.
4. Before writing PL/SQL, check `references/code-objects.md` for an existing package/procedure instead of duplicating logic.
5. Use only names present in the skills. If a table or column is missing, say so and ask.

## Common conventions (all schemas)
- Audit columns `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_*` are maintained by triggers.
- Multi-location columns `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` mark where a record was created.
- Deleted rows are copied to `*_AUDIT` schemas via `SYN_*` synonyms.
- Y/N flag columns (e.g. `ACTIVE`) are single-character.
- Always schema-qualify objects; follow the company naming standards skill `oracle-plsql-apex-hrd-standards` for new objects.
""")
