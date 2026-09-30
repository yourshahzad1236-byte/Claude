#!/usr/bin/env python3
"""Turn per-schema skill folders into 4 flat .md files + one master skill that references them."""
import os, re, sys, shutil
src, out = sys.argv[1], sys.argv[2]   # src = dir from build_skills.py
schemas = ['DEFINITIONS', 'HRD', 'PAYROLL', 'RFID']
ref = os.path.join(out, 'skm-schema', 'references'); os.makedirs(ref, exist_ok=True)
info = {}
for s in schemas:
    d = os.path.join(src, f'skm-{s.lower()}-schema')
    body = re.sub(r'^---.*?---\n', '', open(os.path.join(d, 'SKILL.md')).read(), flags=re.S)
    body = re.sub(r'## References \(read only what you need\).*?(?=## Conventions)', '', body, flags=re.S)
    parts = [f"# {s} schema - reference\n\n" + body.split('\n', 2)[2]]
    for f, title in [('tables.md', 'Tables'), ('views.md', 'Views'), ('code-objects.md', 'Packages, procedures, functions, sequences'), ('synonyms.md', 'Synonyms')]:
        t = open(os.path.join(d, 'references', f)).read()
        t = re.sub(r'^# .*\n', '', t, count=1)
        t = re.sub(r'^(#{2,3}) ', lambda m: m.group(1) + '# ', t, flags=re.M)   # demote headings one level
        parts.append(f"\n\n# PART: {title}\n{t}")
    txt = ''.join(parts)
    txt = txt.replace('`references/tables.md`', 'the Tables part below')
    txt = txt.replace('load the master skill `skm-schema-master` and the other schema skill', 'use the skill `skm-schema` and the other schema reference file')
    open(os.path.join(ref, f'{s}_SCHEMA.md'), 'w').write(txt)
    info[s] = (txt.count('\n### '), os.path.getsize(os.path.join(ref, f'{s}_SCHEMA.md')))
master = open(os.path.join(src, 'skm-schema-master', 'SKILL.md')).read()
master = re.sub(r'^name: .*$', 'name: skm-schema', master, count=1, flags=re.M)
master = re.sub(r'\| Skill \|.*?(?=\n## How to route)', '''| Reference file | Schema | Use for |
|---|---|---|
| `references/DEFINITIONS_SCHEMA.md` | DEFINITIONS | master/lookup data (LOVs, locations, services, CPT, patients, abbreviations) shared by other schemas |
| `references/HRD_SCHEMA.md` | HRD | employees, applicants, leave, appraisal (PA), recruitment, other HR processes |
| `references/PAYROLL_SCHEMA.md` | PAYROLL | pay, loans, expenses, employee pay components, performance income |
| `references/RFID_SCHEMA.md` | RFID | attendance machines, attendance records, access rights, door logs |

Each reference file is one markdown document with four parts: **Tables** (columns, types, nullability, comments, PK/UK/FK/CHECK, indexes, triggers), **Views**, **Packages/procedures/functions/sequences**, **Synonyms**. Search a file for `### SCHEMA.TABLE_NAME` instead of reading it whole.
''', master, flags=re.S)
master = master.replace('Each has its own skill; load the one(s) that match the request.', 'Each has its own reference file; read the one(s) that match the request.')
master = master.replace("Open that skill's `references/tables.md` and find the table (`## SCHEMA.TABLE`).", "Open that reference file and find the table (`### SCHEMA.TABLE`) in the Tables part.")
master = master.replace("skm-definitions-schema", "references/DEFINITIONS_SCHEMA.md").replace("skm-hrd-schema", "references/HRD_SCHEMA.md").replace("skm-payroll-schema", "references/PAYROLL_SCHEMA.md").replace("skm-rfid-schema", "references/RFID_SCHEMA.md")
master = master.replace("Load the target schema's skill", "Read the target schema's reference file").replace("check `references/code-objects.md`", "check the Packages part")
master = master.replace("# SKM Schema - Master Skill", "# SKM Schema")
open(os.path.join(out, 'skm-schema', 'SKILL.md'), 'w').write(master)
print(info)
