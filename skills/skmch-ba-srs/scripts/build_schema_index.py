#!/usr/bin/env python3
"""Build the SKMCH system-context index from schema files.

Reads Oracle schema exports for one or more schemas (HRD, PAYROLL, REGISTRATION,
DEFINITIONS, RFID, ...) and writes a searchable index that the SKMCH skills use for
impact analysis. Objects are keyed as OWNER.NAME, so the same name in two schemas stays
separate, and synonyms are resolved to the object they point to.

Accepted input (a folder such as D:\\SKM_SCHEMA, a .zip of it, or a single file):
  * DDL (.sql .ddl .tab, or .txt exports such as PL/SQL Developer "Export User Objects"):
    CREATE TABLE / ALTER TABLE / INDEX / SEQUENCE / SYNONYM / COMMENT
  * PL/SQL (.pks .pkb .pls .plb .prc .fnc .trg .vw .typ .sql .txt): packages, procedures,
    functions, triggers, views, types
  * APEX exports (f<app>.sql or split export application/pages/page_NNNNN.sql)
  * data-dictionary CSV (columns [OWNER,] TABLE_NAME, COLUMN_NAME, DATA_TYPE[, DATA_LENGTH, NULLABLE])
  * documents (.md .txt .docx .pdf .xlsx): listed in the index so skills can open them

Writes (default: skills/skmch-hrd-system-context/references/ when run from the skills
repository, otherwise ./schema-index):
  INDEX.md                    overview: schemas, counts, one line per table (read this first)
  schemas/<OWNER>.md          one line per table and code object of that schema
  tables/<OWNER>.<TABLE>.md   columns, keys, indexes, triggers, comments, REFERENCED BY
  programs/<OWNER>.<NAME>.md  package/procedure/function/trigger/view/type: units, tables used, callers
  apex/app_<APP>.md           pages and the tables each page references
  objects.json                everything above in machine-readable form

Usage:
  python build_schema_index.py <schema folder | .zip | file> [--out DIR] [--schema HRD] [--copy-src | --zip-src]
--copy-src copies the raw sources to <out>/src; --zip-src stores them as <out>/src.zip (much smaller).
--schema is the owner assumed for unqualified objects when a file doesn't reveal its owner.
"""
import argparse
import csv
import datetime
import json
import os
import re
import shutil
import tempfile
import zipfile
from collections import Counter, defaultdict

SRC_EXT = {".sql", ".ddl", ".tab", ".pks", ".pkb", ".pls", ".plb", ".prc", ".fnc", ".trg", ".vw", ".typ"}
DOC_EXT = {".md", ".txt", ".docx", ".pdf", ".xlsx"}
ID = r'"?([A-Za-z][\w$#]*)"?'
QUAL = r'(?:"?([A-Za-z][\w$#]*)"?\s*\.\s*)?' + ID          # groups: owner (optional), name
SQL_SNIFF = re.compile(r"\bcreate\s+(?:or\s+replace\s+)?(?:\w+\s+){0,3}(?:table|package|procedure|function|view|trigger|synonym)\b", re.I)
BOUNDARY = re.compile(r"\n\s*(?:prompt\b|CREATE\s+(?:OR\s+REPLACE\s+)?(?:(?:NON)?EDITIONABLE\s+)?(?:FORCE\s+|NO\s+FORCE\s+)?"
                      r"(?:PUBLIC\s+)?(?:GLOBAL\s+TEMPORARY\s+|UNIQUE\s+|BITMAP\s+)?"
                      r"(?:TABLE|INDEX|SEQUENCE|SYNONYM|PACKAGE|PROCEDURE|FUNCTION|TRIGGER|VIEW|MATERIALIZED|TYPE)\b)", re.I)


def strip_comments(s):
    s = re.sub(r"/\*.*?\*/", " ", s, flags=re.S)
    return re.sub(r"--[^\n]*", " ", s)


def balanced(s, start):
    """Return the text inside the parentheses that open at s[start] == '('."""
    depth, i = 0, start
    in_str = False
    while i < len(s):
        c = s[i]
        if c == "'":
            in_str = not in_str
        elif not in_str:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return s[start + 1:i]
        i += 1
    return s[start + 1:]


def split_top(s):
    parts, depth, cur, in_str = [], 0, [], False
    for c in s:
        if c == "'":
            in_str = not in_str
        if not in_str:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            elif c == "," and depth == 0:
                parts.append("".join(cur).strip()); cur = []; continue
        cur.append(c)
    if "".join(cur).strip():
        parts.append("".join(cur).strip())
    return parts


def new_table():
    return {"columns": {}, "pk": [], "fks": [], "uniques": [], "checks": [], "indexes": [],
            "triggers": [], "comment": "", "col_comments": {}, "files": set(), "referenced_by": set()}


class Index:
    def __init__(self, schema):
        self.default = schema.upper()
        self.owner = self.default          # owner assumed for unqualified names in the current file
        self.tables = defaultdict(new_table)
        self.programs = {}   # OWNER.NAME[ (BODY)] -> {type, owner, name, units, files, text}
        self.sequences = {}  # OWNER.NAME -> file
        self.synonyms = {}   # OWNER.NAME (or PUBLIC.NAME) -> OWNER.NAME target
        self.apex = defaultdict(lambda: {"pages": {}, "files": set()})
        self.docs = []

    def key(self, owner, name):
        return f"{(owner or self.owner).upper()}.{name.upper()}"

    def guess_owner(self, text):
        owners = Counter(o.upper() for o in re.findall(
            r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:(?:NON)?EDITIONABLE\s+)?(?:\w+\s+){0,2}"
            r"(?:TABLE|PACKAGE|PROCEDURE|FUNCTION|VIEW|TRIGGER|SEQUENCE|SYNONYM|TYPE)\s+\"?([A-Za-z][\w$#]*)\"?\s*\.", text, re.I))
        self.owner = owners.most_common(1)[0][0] if owners else self.default

    # ---------- DDL ----------
    def parse_ddl(self, text, rel):
        for m in re.finditer(r"CREATE\s+(?:GLOBAL\s+TEMPORARY\s+|PRIVATE\s+TEMPORARY\s+)?TABLE\s+" + QUAL + r"\s*\(", text, re.I):
            k = self.key(m.group(1), m.group(2))
            self.tables[k]["files"].add(rel)
            for part in split_top(balanced(text, m.end() - 1)):
                self._table_part(k, part)
        for m in re.finditer(r"ALTER\s+TABLE\s+" + QUAL + r"\s+ADD\s*(\(?)", text, re.I):
            k = self.key(m.group(1), m.group(2))
            self.tables[k]["files"].add(rel)
            if m.group(3):
                for part in split_top(balanced(text, m.end() - 1)):
                    self._table_part(k, part)
            else:
                end = text.find(";", m.end())
                self._table_part(k, text[m.end():end if end >= 0 else len(text)].strip())
        for m in re.finditer(r"CREATE\s+(?:UNIQUE\s+|BITMAP\s+)?INDEX\s+" + QUAL + r"\s+ON\s+" + QUAL + r"\s*\(([^;]*?)\)", text, re.I):
            self.tables[self.key(m.group(3), m.group(4))]["indexes"].append(
                f"{m.group(2).upper()} ({' '.join(m.group(5).split()).upper()})")
        for m in re.finditer(r"CREATE\s+SEQUENCE\s+" + QUAL, text, re.I):
            self.sequences[self.key(m.group(1), m.group(2))] = rel
        for m in re.finditer(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:(?:NON)?EDITIONABLE\s+)?(PUBLIC\s+)?SYNONYM\s+" + QUAL +
                             r"\s+FOR\s+" + QUAL, text, re.I):
            syn = f"PUBLIC.{m.group(3).upper()}" if m.group(1) else self.key(m.group(2), m.group(3))
            self.synonyms[syn] = self.key(m.group(4), m.group(5))
        for m in re.finditer(r"COMMENT\s+ON\s+TABLE\s+" + QUAL + r"\s+IS\s+'((?:[^']|'')*)'", text, re.I):
            self.tables[self.key(m.group(1), m.group(2))]["comment"] = m.group(3).replace("''", "'")
        for m in re.finditer(r"COMMENT\s+ON\s+COLUMN\s+(?:\"?(\w+)\"?\.)?\"?(\w+)\"?\.\"?(\w+)\"?\s+IS\s+'((?:[^']|'')*)'", text, re.I):
            self.tables[self.key(m.group(1), m.group(2))]["col_comments"][m.group(3).upper()] = m.group(4).replace("''", "'")

    def _table_part(self, table, part):
        t = self.tables[table]
        p = " ".join(part.split())
        up = p.upper()
        cons = re.match(r"(?:CONSTRAINT\s+\"?(\w+)\"?\s+)?(PRIMARY\s+KEY|FOREIGN\s+KEY|UNIQUE|CHECK)\b(.*)", p, re.I)
        if cons:
            cname = (cons.group(1) or "").upper()
            kind = cons.group(2).upper().split()[0]
            rest = cons.group(3)
            cols = re.search(r"\(([^)]*)\)", rest)
            cols = [c.strip(' "').upper() for c in cols.group(1).split(",")] if cols else []
            if kind == "PRIMARY":
                t["pk"] = cols
            elif kind == "FOREIGN":
                ref = re.search(r"REFERENCES\s+" + QUAL + r"\s*(?:\(([^)]*)\))?", rest, re.I)
                t["fks"].append({"name": cname, "columns": cols,
                                 "ref_table": self.key(ref.group(1) or table.split(".")[0], ref.group(2)) if ref else "?",
                                 "ref_columns": [c.strip(' "').upper() for c in (ref.group(3) or "").split(",") if c.strip()] if ref else []})
            elif kind == "UNIQUE":
                t["uniques"].append(cols)
            else:
                t["checks"].append(p[:200])
            return
        m = re.match(r'"?([A-Za-z][\w$#]*)"?\s+([A-Za-z][\w ]*?(?:\([^)]*\))?(?:\s+(?:CHAR|BYTE))?)(\s.*)?$', p)
        if not m or m.group(1).upper() in {"CONSTRAINT", "PRIMARY", "FOREIGN", "UNIQUE", "CHECK", "SUPPLEMENTAL", "PERIOD"}:
            return
        col, dtype, rest = m.group(1).upper(), m.group(2).upper().strip(), (m.group(3) or "").upper()
        dtype = re.sub(r"\s+(DEFAULT|NOT|NULL|CONSTRAINT|PRIMARY|REFERENCES|UNIQUE|CHECK|GENERATED).*", "", dtype)
        info = {"type": dtype, "nullable": "NOT NULL" not in up and "PRIMARY KEY" not in up, "default": ""}
        d = re.search(r"DEFAULT\s+(.+?)(?:\s+NOT\s+NULL|\s+NULL|\s+CONSTRAINT|\s+CHECK|$)", rest)
        if d:
            info["default"] = d.group(1).strip()
        t["columns"][col] = info
        if "PRIMARY KEY" in up:
            t["pk"] = [col]
        r = re.search(r"REFERENCES\s+" + QUAL, rest)
        if r:
            t["fks"].append({"name": "", "columns": [col], "ref_table": self.key(r.group(1) or table.split(".")[0], r.group(2)),
                             "ref_columns": []})

    # ---------- PL/SQL ----------
    def parse_plsql(self, text, rel):
        pat = re.compile(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:(?:NON)?EDITIONABLE\s+)?(?:FORCE\s+|NO\s+FORCE\s+)?"
                         r"(PACKAGE\s+BODY|PACKAGE|PROCEDURE|FUNCTION|TRIGGER|VIEW|MATERIALIZED\s+VIEW|TYPE\s+BODY|TYPE)\s+" + QUAL, re.I)
        for m in pat.finditer(text):
            kind = " ".join(m.group(1).upper().split())
            owner = (m.group(2) or self.owner).upper()
            name = m.group(3).upper()
            nxt = BOUNDARY.search(text, m.end())
            chunk = text[m.start(): nxt.start() if nxt else len(text)]
            key = f"{owner}.{name}" + (" (BODY)" if kind in ("PACKAGE BODY", "TYPE BODY") else "")
            entry = self.programs.setdefault(key, {"type": kind, "owner": owner, "name": name, "units": [], "files": set(), "text": ""})
            entry["files"].add(rel)
            entry["text"] += "\n" + chunk
            if kind == "PACKAGE":
                for u in re.finditer(r"\b(PROCEDURE|FUNCTION)\s+" + ID + r"([^;]*?)(?:RETURN\s+([\w.%]+))?\s*;", chunk, re.I):
                    params = " ".join(u.group(3).split())
                    sig = f"{u.group(1).upper()} {u.group(2).upper()}{params}" + (f" RETURN {u.group(4).upper()}" if u.group(4) else "")
                    entry["units"].append(sig[:300])
            if kind == "TRIGGER":
                on = re.search(r"\bON\s+" + QUAL, chunk, re.I)
                timing = re.search(r"\b(BEFORE|AFTER|INSTEAD\s+OF)\s+([\w\s,]+?)\s+(?:OF\s+[\w\s,]+?\s+)?ON\b", chunk, re.I)
                if on:
                    tk = f"{(on.group(1) or owner).upper()}.{on.group(2).upper()}"
                    self.tables[tk]["triggers"].append(
                        f"{owner}.{name} ({' '.join(timing.group(0).split()[:-1]).upper() if timing else ''})")

    # ---------- APEX ----------
    def parse_apex(self, text, rel):
        app = re.search(r"p_default_application_id\s*=>\s*(\d+)", text) or re.search(r"[\\/]f(\d+)[\\/.]", "/" + rel)
        app_id = app.group(1) if app else "UNKNOWN"
        a = self.apex[app_id]
        a["files"].add(rel)
        pages = list(re.finditer(r"create_page\s*\(\s*p_id\s*=>\s*(\d+)", text, re.I))
        for i, m in enumerate(pages):
            chunk = text[m.start(): pages[i + 1].start() if i + 1 < len(pages) else len(text)]
            nm = re.search(r"p_name\s*=>\s*'((?:[^']|'')*)'", chunk)
            a["pages"][int(m.group(1))] = {"name": nm.group(1) if nm else "", "text": chunk, "file": rel}

    def parse_csv(self, path, rel):
        with open(path, encoding="utf-8", errors="ignore", newline="") as f:
            rows = list(csv.DictReader(f))
        if not rows or "TABLE_NAME" not in {k.upper() for k in rows[0] if k}:
            return False
        for r in rows:
            r = {k.upper(): (v or "").strip() for k, v in r.items() if k}
            if not r.get("TABLE_NAME") or not r.get("COLUMN_NAME"):
                continue
            dtype = r.get("DATA_TYPE", "")
            if r.get("DATA_LENGTH") and dtype.upper() in ("VARCHAR2", "CHAR", "NVARCHAR2", "RAW"):
                dtype += f"({r['DATA_LENGTH']})"
            elif r.get("DATA_PRECISION"):
                dtype += f"({r['DATA_PRECISION']}{',' + r['DATA_SCALE'] if r.get('DATA_SCALE') not in (None, '', '0') else ''})"
            t = self.tables[self.key(r.get("OWNER"), r["TABLE_NAME"])]
            t["files"].add(rel)
            t["columns"].setdefault(r["COLUMN_NAME"].upper(), {"type": dtype.upper(), "nullable": r.get("NULLABLE", "Y") != "N", "default": ""})
            if r.get("COMMENTS"):
                t["col_comments"][r["COLUMN_NAME"].upper()] = r["COMMENTS"]
        return True

    # ---------- cross references ----------
    def link(self):
        # bare name -> qualified keys of tables/views and of callable code
        data, code = defaultdict(set), defaultdict(set)
        for k in self.tables:
            data[k.split(".", 1)[1]].add(k)
        for key, p in self.programs.items():
            p.setdefault("called_by", set())
            if p["type"] in ("VIEW", "MATERIALIZED VIEW"):
                data[p["name"]].add(f"{p['owner']}.{p['name']}")
            elif p["type"] != "TRIGGER":
                code[p["name"]].add(f"{p['owner']}.{p['name']}")
        code_keys = defaultdict(list)  # OWNER.NAME -> program keys (spec, body)
        for key, p in self.programs.items():
            code_keys[f"{p['owner']}.{p['name']}"].append(key)
        # synonyms: the synonym name resolves to its target
        syn_by_name = defaultdict(set)
        for syn, target in self.synonyms.items():
            syn_by_name[syn.split(".", 1)[1]].add((syn.split(".", 1)[0], target))
        qual_ref = re.compile(r"\b([A-Za-z][\w$#]*)\s*\.\s*([A-Za-z][\w$#]*)")
        ident = re.compile(r"[A-Za-z][\w$#]*")

        def resolve(word, owner, quals, pool):
            """Resolve a bare identifier used by code owned by `owner`."""
            hits = {q for q in quals.get(word, ()) if q in pool.get(word, set()) or q in self.synonyms}
            if hits:
                return {self.synonyms.get(h, h) for h in hits}
            cands = pool.get(word, set())
            own = f"{owner}.{word}"
            if own in cands:
                return {own}
            for syn_owner, target in syn_by_name.get(word, ()):
                if syn_owner in (owner, "PUBLIC") and target.split(".", 1)[1] in pool:
                    return {target}
            return cands if len(cands) == 1 else set()

        def record(text, owner, who, self_key):
            words = {w.upper() for w in ident.findall(text)}
            quals = defaultdict(set)
            for o, n in qual_ref.findall(text):
                quals[n.upper()].add(f"{o.upper()}.{n.upper()}")
            used, calls = set(), set()
            for w in words:
                if w in data or w in syn_by_name:
                    used |= resolve(w, owner, quals, data)
                if w in code or w in syn_by_name:
                    calls |= {c for c in resolve(w, owner, quals, code) if c in code_keys}
            used.discard(self_key); calls.discard(self_key)
            for tk in used:
                if tk in self.tables:
                    self.tables[tk]["referenced_by"].add(who)
            for c in calls:
                for k in code_keys[c]:
                    self.programs[k]["called_by"].add(who)
            return sorted(used), sorted(calls)

        for key, p in self.programs.items():
            p["uses"], p["calls"] = record(p["text"], p["owner"], f"{p['type']} {key}", f"{p['owner']}.{p['name']}")
        for app_id, a in self.apex.items():
            for no, pg in a["pages"].items():
                pg["uses"], pg["calls"] = record(pg["text"], self.default, f"APEX {app_id}:{no} {pg['name']}", None)


def fname(name):
    return re.sub(r"[^\w$#.-]", "_", name) + ".md"


def write(idx, out, src_root, copy_src, label=None, zip_src=False):
    for d in ("tables", "programs", "apex", "schemas"):
        shutil.rmtree(os.path.join(out, d), ignore_errors=True)
        os.makedirs(os.path.join(out, d))
    child_fks = defaultdict(set)
    for o, ot in idx.tables.items():
        for fk in ot["fks"]:
            child_fks[fk["ref_table"]].add(f"{o} ({', '.join(fk['columns'])})")
    for name, t in sorted(idx.tables.items()):
        L = [f"# {name}", ""]
        if t["comment"]:
            L += [t["comment"], ""]
        L += [f"Source: {', '.join(sorted(t['files'])) or 'referenced only (no DDL found)'}", "",
              "| Column | Type | Null | Default | PK | Comment |", "|---|---|---|---|---|---|"]
        for c, ci in t["columns"].items():
            L.append(f"| {c} | {ci['type']} | {'Y' if ci['nullable'] else 'N'} | {ci['default']} | "
                     f"{'PK' if c in t['pk'] else ''} | {t['col_comments'].get(c, '')} |")
        if t["fks"]:
            L += ["", "## Foreign keys"] + [f"- {fk['name'] or '(inline)'}: ({', '.join(fk['columns'])}) → {fk['ref_table']}"
                                             f"{' (' + ', '.join(fk['ref_columns']) + ')' if fk['ref_columns'] else ''}" for fk in t["fks"]]
        children = sorted(child_fks.get(name, ()))
        if children:
            L += ["", "## Referenced by foreign keys from"] + [f"- {c}" for c in children]
        if t["uniques"]:
            L += ["", "## Unique keys"] + [f"- ({', '.join(u)})" for u in t["uniques"]]
        if t["indexes"]:
            L += ["", "## Indexes"] + [f"- {i}" for i in t["indexes"]]
        if t["triggers"]:
            L += ["", "## Triggers"] + [f"- {x}" for x in t["triggers"]]
        syns = sorted(s for s, tg in idx.synonyms.items() if tg == name)
        if syns:
            L += ["", "## Synonyms pointing here"] + [f"- {s}" for s in syns]
        L += ["", "## Referenced by (code, views, APEX pages)"]
        L += [f"- {r}" for r in sorted(t["referenced_by"])] or ["- none found"]
        with open(os.path.join(out, "tables", fname(name)), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
    for key, p in sorted(idx.programs.items()):
        L = [f"# {key}", "", f"Type: {p['type']}  ", f"Source: {', '.join(sorted(p['files']))}", ""]
        if p["units"]:
            L += ["## Public program units (spec)"] + [f"- `{u}`" for u in p["units"]] + [""]
        L += ["## Tables / views referenced"] + ([f"- {u}" for u in p["uses"]] or ["- none found"])
        L += ["", "## Calls packages / procedures / functions"] + ([f"- {c}" for c in p["calls"]] or ["- none found"])
        L += ["", "## Called by (code, APEX pages)"] + ([f"- {c}" for c in sorted(p["called_by"])] or ["- none found"])
        with open(os.path.join(out, "programs", fname(key)), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
    for app_id, a in sorted(idx.apex.items()):
        L = [f"# APEX application {app_id}", "", f"Source: {', '.join(sorted(a['files']))}", "",
             "| Page | Name | Tables / views referenced | Code called |", "|---|---|---|---|"]
        for no, pg in sorted(a["pages"].items()):
            L.append(f"| {no} | {pg['name']} | {', '.join(pg['uses'])} | {', '.join(pg['calls'])} |")
        with open(os.path.join(out, "apex", f"app_{app_id}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")

    owners = sorted({k.split(".", 1)[0] for k in idx.tables} | {p["owner"] for p in idx.programs.values()})
    by_type = lambda o, *types: [p for p in idx.programs.values() if p["owner"] == o and p["type"] in types]
    for o in owners:
        L = [f"# Schema {o}", "", "## Tables", "", "| Table | Columns | Referenced by | Comment |", "|---|---|---|---|"]
        for name, t in sorted(idx.tables.items()):
            if name.startswith(o + "."):
                L.append(f"| [{name}](../tables/{fname(name)}) | {len(t['columns'])} | {len(t['referenced_by'])} | {t['comment'][:80]} |")
        L += ["", "## Packages, procedures, functions, views, triggers, types", "",
              "| Object | Type | Units | Tables used | Called by |", "|---|---|---|---|---|"]
        for key, p in sorted(idx.programs.items()):
            if p["owner"] == o:
                L.append(f"| [{key}](../programs/{fname(key)}) | {p['type']} | {len(p['units'])} | "
                         f"{len(p.get('uses', []))} | {len(p.get('called_by', []))} |")
        seqs = sorted(q for q in idx.sequences if q.startswith(o + "."))
        if seqs:
            L += ["", "## Sequences", ""] + [f"- {q}" for q in seqs]
        syns = sorted((s, tg) for s, tg in idx.synonyms.items() if s.startswith(o + "."))
        if syns:
            L += ["", "## Synonyms", "", "| Synonym | Points to |", "|---|---|"] + [f"| {s} | {tg} |" for s, tg in syns]
        with open(os.path.join(out, "schemas", f"{o}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")

    L = ["# SKMCH system context index", "",
         f"Generated by build_schema_index.py from `{label or os.path.basename(os.path.abspath(src_root))}` "
         f"on {datetime.date.today().isoformat()}. Quote this source and date in every impact analysis.", "",
         "How to use: find the object below or in `schemas/<OWNER>.md`, then open `tables/<OWNER>.<TABLE>.md` or "
         "`programs/<OWNER>.<NAME>.md`. Each table file lists everything that references it (code, views, triggers, "
         "APEX pages, child foreign keys, synonyms): that list is the dependency list for impact analysis.", "",
         "| Schema | Tables | Packages | Procedures / functions | Views | Triggers | Types | Sequences | Synonyms |",
         "|---|---|---|---|---|---|---|---|---|"]
    for o in owners:
        L.append(f"| [{o}](schemas/{o}.md) | {sum(1 for k in idx.tables if k.startswith(o + '.'))} | "
                 f"{len(by_type(o, 'PACKAGE'))} | {len(by_type(o, 'PROCEDURE', 'FUNCTION'))} | "
                 f"{len(by_type(o, 'VIEW', 'MATERIALIZED VIEW'))} | {len(by_type(o, 'TRIGGER'))} | {len(by_type(o, 'TYPE'))} | "
                 f"{sum(1 for q in idx.sequences if q.startswith(o + '.'))} | {sum(1 for s in idx.synonyms if s.startswith(o + '.'))} |")
    L += ["", f"APEX applications / pages: {len(idx.apex)} / {sum(len(a['pages']) for a in idx.apex.values())}. "
          f"Documents: {len(idx.docs)}.", "", "## Tables (all schemas)", "", "| Table | Columns | Referenced by |", "|---|---|---|"]
    for name, t in sorted(idx.tables.items()):
        L.append(f"| [{name}](tables/{fname(name)}) | {len(t['columns'])} | {len(t['referenced_by'])} |")
    if idx.apex:
        L += ["", "## APEX applications", ""] + [f"- [App {a}](apex/app_{a}.md): {len(v['pages'])} pages" for a, v in sorted(idx.apex.items())]
    if idx.docs:
        L += ["", "## System documents", ""] + [f"- {d}" for d in sorted(idx.docs)]
    with open(os.path.join(out, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    dump = {"source": label, "generated": datetime.date.today().isoformat(), "schemas": owners,
            "tables": {n: {**{k: v for k, v in t.items() if k not in ("files", "referenced_by")},
                           "files": sorted(t["files"]), "referenced_by": sorted(t["referenced_by"])} for n, t in idx.tables.items()},
            "programs": {k: {"type": p["type"], "units": p["units"], "uses": p.get("uses", []), "calls": p.get("calls", []),
                             "called_by": sorted(p.get("called_by", [])), "files": sorted(p["files"])} for k, p in idx.programs.items()},
            "sequences": sorted(idx.sequences),
            "synonyms": dict(sorted(idx.synonyms.items())),
            "apex": {a: {str(n): {"name": pg["name"], "uses": pg["uses"], "calls": pg["calls"]} for n, pg in v["pages"].items()} for a, v in idx.apex.items()},
            "documents": sorted(idx.docs)}
    with open(os.path.join(out, "objects.json"), "w", encoding="utf-8") as f:
        json.dump(dump, f, indent=1)
    dst = os.path.join(out, "src")
    shutil.rmtree(dst, ignore_errors=True)
    if os.path.exists(dst + ".zip"):
        os.remove(dst + ".zip")
    if copy_src:
        shutil.copytree(src_root, dst, ignore=shutil.ignore_patterns(".git", "*.zip"))
    elif zip_src:
        with zipfile.ZipFile(dst + ".zip", "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(src_root):
                dirs[:] = [d for d in dirs if not d.startswith(".")]
                for fn in sorted(files):
                    if not fn.endswith(".zip"):
                        full = os.path.join(root, fn)
                        z.write(full, os.path.relpath(full, src_root))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", help="schema folder (e.g. D:\\SKM_SCHEMA), a .zip of it, or a single schema file")
    here = os.path.dirname(os.path.abspath(__file__))
    repo_out = os.path.join(here, "..", "..", "skills", "skmch-hrd-system-context", "references")
    ap.add_argument("--out", default=repo_out if os.path.isdir(repo_out) else "schema-index")
    ap.add_argument("--schema", default="HRD", help="owner assumed for unqualified objects")
    ap.add_argument("--copy-src", action="store_true", help="also copy raw sources into <out>/src")
    ap.add_argument("--zip-src", action="store_true", help="also store raw sources as <out>/src.zip")
    a = ap.parse_args()
    if not os.path.exists(a.folder):
        raise SystemExit(f"Schema source not found: {a.folder}")
    label = os.path.basename(os.path.normpath(os.path.abspath(a.folder)))
    if zipfile.is_zipfile(a.folder):
        tmp = tempfile.mkdtemp(prefix="schema-")
        with zipfile.ZipFile(a.folder) as z:
            z.extractall(tmp)
        a.folder = tmp
    elif os.path.isfile(a.folder):
        tmp = tempfile.mkdtemp(prefix="schema-")
        shutil.copy(a.folder, tmp)
        a.folder = tmp
    idx = Index(a.schema)
    for root, dirs, files in os.walk(a.folder):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in sorted(files):
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, a.folder)
            ext = os.path.splitext(fn)[1].lower()
            if ext == ".csv":
                if not idx.parse_csv(path, rel):
                    idx.docs.append(rel)
                continue
            if ext == ".txt":
                with open(path, encoding="utf-8", errors="ignore") as f:
                    if not SQL_SNIFF.search(f.read(200000)):
                        idx.docs.append(rel)
                        continue
            elif ext in DOC_EXT:
                idx.docs.append(rel)
                continue
            elif ext not in SRC_EXT:
                continue
            with open(path, encoding="utf-8", errors="ignore") as f:
                raw = f.read()
            if re.search(r"wwv_flow_(imp|api)|wwv_flow_imp_page", raw, re.I):
                idx.parse_apex(raw, rel)
                continue
            text = strip_comments(raw)
            idx.guess_owner(text)
            idx.parse_ddl(text, rel)
            idx.parse_plsql(text, rel)
    idx.link()
    os.makedirs(a.out, exist_ok=True)
    write(idx, a.out, a.folder, a.copy_src, label, a.zip_src)
    print(f"Indexed {len(idx.tables)} tables, {len(idx.programs)} code objects, {len(idx.synonyms)} synonyms, "
          f"{sum(len(v['pages']) for v in idx.apex.values())} APEX pages, {len(idx.docs)} documents "
          f"across schemas {', '.join(sorted({k.split('.', 1)[0] for k in idx.tables}))} → {os.path.relpath(a.out)}")


if __name__ == "__main__":
    main()
