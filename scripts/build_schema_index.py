#!/usr/bin/env python3
"""Build the HRD system-context index from the shared schema folder.

Scans a folder of Oracle sources:
  * DDL (.sql .ddl .tab): CREATE TABLE / ALTER TABLE / INDEX / SEQUENCE / COMMENT
  * PL/SQL (.pks .pkb .pls .plb .prc .fnc .trg .vw .sql): packages, procedures, functions, triggers, views
  * APEX exports (f<app>.sql or split export application/pages/page_NNNNN.sql)
  * data-dictionary CSV (columns TABLE_NAME, COLUMN_NAME, DATA_TYPE[, DATA_LENGTH, NULLABLE])
  * documents (.md .txt .docx): listed in the index so skills can open them

Writes (default: skills/skmch-hrd-system-context/references/):
  INDEX.md                  overview + one line per object (read this first)
  tables/<TABLE>.md         columns, keys, indexes, triggers, comments, REFERENCED BY
  programs/<NAME>.md        package/procedure/function/trigger/view: units, tables used
  apex/<APP>.md             pages and the tables each page references
  objects.json              everything above in machine-readable form

Usage:
  python scripts/build_schema_index.py <schema_folder> [--out DIR] [--schema HRD] [--copy-src]
"""
import argparse
import csv
import json
import os
import re
import shutil
from collections import defaultdict

SRC_EXT = {".sql", ".ddl", ".tab", ".pks", ".pkb", ".pls", ".plb", ".prc", ".fnc", ".trg", ".vw", ".typ"}
DOC_EXT = {".md", ".txt", ".docx", ".pdf", ".xlsx"}
IDENT = r'"?([A-Za-z][\w$#]*)"?'
QUAL = r'(?:"?[A-Za-z][\w$#]*"?\s*\.\s*)?' + IDENT


def strip_comments(s):
    s = re.sub(r"/\*.*?\*/", " ", s, flags=re.S)
    return re.sub(r"--[^\n]*", " ", s)


def balanced(s, start):
    """Return the text inside the parentheses that open at s[start] == '('."""
    depth, i = 0, start
    in_str = False
    while i < len(s):
        c = s[i]
        if c == "'" and not in_str:
            in_str = True
        elif c == "'" and in_str:
            in_str = False
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
        self.schema = schema.upper()
        self.tables = defaultdict(new_table)
        self.programs = {}   # name -> {type, units, file, text}
        self.sequences = {}
        self.apex = defaultdict(lambda: {"pages": {}, "files": set()})
        self.docs = []

    # ---------- DDL ----------
    def parse_ddl(self, text, rel):
        for m in re.finditer(r"CREATE\s+(?:GLOBAL\s+TEMPORARY\s+|PRIVATE\s+TEMPORARY\s+)?TABLE\s+" + QUAL + r"\s*\(", text, re.I):
            name = m.group(1).upper()
            t = self.tables[name]
            t["files"].add(rel)
            body = balanced(text, m.end() - 1)
            for part in split_top(body):
                self._table_part(name, part)
        for m in re.finditer(r"ALTER\s+TABLE\s+" + QUAL + r"\s+ADD\s*(\(?)", text, re.I):
            name = m.group(1).upper()
            t = self.tables[name]
            t["files"].add(rel)
            if m.group(2):
                for part in split_top(balanced(text, m.end() - 1)):
                    self._table_part(name, part)
            else:
                stmt = text[m.end():text.find(";", m.end()) if ";" in text[m.end():] else len(text)]
                self._table_part(name, stmt.strip())
        for m in re.finditer(r"CREATE\s+(?:UNIQUE\s+|BITMAP\s+)?INDEX\s+" + QUAL + r"\s+ON\s+" + QUAL + r"\s*\(([^;]*?)\)", text, re.I):
            self.tables[m.group(2).upper()]["indexes"].append(f"{m.group(1).upper()} ({' '.join(m.group(3).split()).upper()})")
        for m in re.finditer(r"CREATE\s+SEQUENCE\s+" + QUAL, text, re.I):
            self.sequences[m.group(1).upper()] = rel
        for m in re.finditer(r"COMMENT\s+ON\s+TABLE\s+" + QUAL + r"\s+IS\s+'((?:[^']|'')*)'", text, re.I):
            self.tables[m.group(1).upper()]["comment"] = m.group(2).replace("''", "'")
        for m in re.finditer(r"COMMENT\s+ON\s+COLUMN\s+(?:\"?\w+\"?\.)?\"?(\w+)\"?\.\"?(\w+)\"?\s+IS\s+'((?:[^']|'')*)'", text, re.I):
            self.tables[m.group(1).upper()]["col_comments"][m.group(2).upper()] = m.group(3).replace("''", "'")

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
                                 "ref_table": ref.group(1).upper() if ref else "?",
                                 "ref_columns": [c.strip(' "').upper() for c in (ref.group(2) or "").split(",") if c.strip()] if ref else []})
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
            t["fks"].append({"name": "", "columns": [col], "ref_table": r.group(1).upper(), "ref_columns": []})

    # ---------- PL/SQL ----------
    def parse_plsql(self, text, rel):
        pat = re.compile(r"CREATE\s+(?:OR\s+REPLACE\s+)?(?:(?:NON)?EDITIONABLE\s+)?(?:FORCE\s+|NO\s+FORCE\s+)?"
                         r"(PACKAGE\s+BODY|PACKAGE|PROCEDURE|FUNCTION|TRIGGER|VIEW|MATERIALIZED\s+VIEW|TYPE\s+BODY|TYPE)\s+" + QUAL, re.I)
        hits = list(pat.finditer(text))
        for i, m in enumerate(hits):
            kind = " ".join(m.group(1).upper().split())
            name = m.group(2).upper()
            chunk = text[m.start(): hits[i + 1].start() if i + 1 < len(hits) else len(text)]
            key = name + (" (BODY)" if kind in ("PACKAGE BODY", "TYPE BODY") else "")
            entry = self.programs.setdefault(key, {"type": kind, "name": name, "units": [], "files": set(), "text": ""})
            entry["files"].add(rel)
            entry["text"] += "\n" + chunk
            if kind == "PACKAGE":
                for u in re.finditer(r"\b(PROCEDURE|FUNCTION)\s+" + IDENT + r"([^;]*?)(?:RETURN\s+([\w.%]+))?\s*;", chunk, re.I):
                    params = " ".join(u.group(3).split())
                    sig = f"{u.group(1).upper()} {u.group(2).upper()}{params}" + (f" RETURN {u.group(4).upper()}" if u.group(4) else "")
                    entry["units"].append(sig[:300])
            if kind == "TRIGGER":
                on = re.search(r"\bON\s+" + QUAL, chunk, re.I)
                timing = re.search(r"\b(BEFORE|AFTER|INSTEAD\s+OF)\s+([\w\s,]+?)\s+(?:OF\s+[\w\s,]+?\s+)?ON\b", chunk, re.I)
                if on:
                    self.tables[on.group(1).upper()]["triggers"].append(
                        f"{name} ({' '.join(timing.group(0).split()[:-1]).upper() if timing else ''})")

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
        if not rows or "TABLE_NAME" not in {k.upper() for k in rows[0]}:
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
            t = self.tables[r["TABLE_NAME"].upper()]
            t["files"].add(rel)
            t["columns"].setdefault(r["COLUMN_NAME"].upper(), {"type": dtype.upper(), "nullable": r.get("NULLABLE", "Y") != "N", "default": ""})
            if r.get("COMMENTS"):
                t["col_comments"][r["COLUMN_NAME"].upper()] = r["COMMENTS"]
        return True

    # ---------- cross references ----------
    def link(self):
        names = set(self.tables) | {p["name"] for p in self.programs.values() if p["type"] in ("VIEW", "MATERIALIZED VIEW")}
        code = defaultdict(list)  # program name -> keys (spec, body)
        for key, p in self.programs.items():
            if p["type"] not in ("VIEW", "MATERIALIZED VIEW"):
                code[p["name"]].append(key)
            p.setdefault("called_by", set())
        ident = re.compile(r"[A-Za-z][\w$#]*")

        def record(words, who):
            used = sorted((words & names) - {who[1]})
            calls = sorted((words & set(code)) - {who[1]})
            for tname in used:
                if tname in self.tables:
                    self.tables[tname]["referenced_by"].add(who[0])
            for c in calls:
                for k in code[c]:
                    self.programs[k]["called_by"].add(who[0])
            return used, calls

        for key, p in self.programs.items():
            words = {w.upper() for w in ident.findall(strip_comments(p["text"]))}
            p["uses"], p["calls"] = record(words, (f"{p['type']} {key}", p["name"]))
        for app_id, a in self.apex.items():
            for no, pg in a["pages"].items():
                words = {w.upper() for w in ident.findall(pg["text"])}
                pg["uses"], pg["calls"] = record(words, (f"APEX {app_id}:{no} {pg['name']}", None))


def fname(name):
    return re.sub(r"[^\w$#.-]", "_", name) + ".md"


def write(idx, out, src_root, copy_src):
    for d in ("tables", "programs", "apex"):
        shutil.rmtree(os.path.join(out, d), ignore_errors=True)
        os.makedirs(os.path.join(out, d))
    s = idx.schema
    for name, t in sorted(idx.tables.items()):
        L = [f"# {s}.{name}", ""]
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
        children = sorted({f"{o} ({', '.join(fk['columns'])})" for o, ot in idx.tables.items() for fk in ot["fks"] if fk["ref_table"] == name})
        if children:
            L += ["", "## Referenced by foreign keys from"] + [f"- {c}" for c in children]
        if t["uniques"]:
            L += ["", "## Unique keys"] + [f"- ({', '.join(u)})" for u in t["uniques"]]
        if t["indexes"]:
            L += ["", "## Indexes"] + [f"- {i}" for i in t["indexes"]]
        if t["triggers"]:
            L += ["", "## Triggers"] + [f"- {x}" for x in t["triggers"]]
        L += ["", "## Referenced by (code, views, APEX pages)"]
        L += [f"- {r}" for r in sorted(t["referenced_by"])] or ["- none found"]
        with open(os.path.join(out, "tables", fname(name)), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
    for key, p in sorted(idx.programs.items()):
        L = [f"# {s}.{key}", "", f"Type: {p['type']}  ", f"Source: {', '.join(sorted(p['files']))}", ""]
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

    pk = lambda n: [p for p in idx.programs.values() if p["type"] == n]
    L = [f"# {s} system context index", "",
         f"Generated by scripts/build_schema_index.py from `{os.path.basename(os.path.abspath(src_root))}`.", "",
         "Open `tables/<TABLE>.md`, `programs/<NAME>.md` or `apex/app_<ID>.md` for details. "
         "Each table file lists everything that references it: use that for impact analysis.", "",
         "| Object type | Count |", "|---|---|",
         f"| Tables | {len(idx.tables)} |", f"| Packages | {len(pk('PACKAGE'))} |",
         f"| Procedures / functions | {len(pk('PROCEDURE')) + len(pk('FUNCTION'))} |",
         f"| Views | {len(pk('VIEW')) + len(pk('MATERIALIZED VIEW'))} |", f"| Triggers | {len(pk('TRIGGER'))} |",
         f"| Sequences | {len(idx.sequences)} |",
         f"| APEX applications / pages | {len(idx.apex)} / {sum(len(a['pages']) for a in idx.apex.values())} |",
         f"| Documents | {len(idx.docs)} |", "", "## Tables", "",
         "| Table | Columns | Referenced by | Comment |", "|---|---|---|---|"]
    for name, t in sorted(idx.tables.items()):
        L.append(f"| [{name}](tables/{fname(name)}) | {len(t['columns'])} | {len(t['referenced_by'])} | {t['comment'][:80]} |")
    L += ["", "## Packages, procedures, functions, views, triggers", "", "| Object | Type | Units | Tables used | Called by |", "|---|---|---|---|---|"]
    for key, p in sorted(idx.programs.items()):
        L.append(f"| [{key}](programs/{fname(key)}) | {p['type']} | {len(p['units'])} | {len(p.get('uses', []))} | {len(p.get('called_by', []))} |")
    if idx.sequences:
        L += ["", "## Sequences", ""] + [f"- {q}" for q in sorted(idx.sequences)]
    if idx.apex:
        L += ["", "## APEX applications", ""] + [f"- [App {a}](apex/app_{a}.md): {len(v['pages'])} pages" for a, v in sorted(idx.apex.items())]
    if idx.docs:
        L += ["", "## System documents", ""] + [f"- {d}" for d in sorted(idx.docs)]
    with open(os.path.join(out, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    dump = {"schema": s,
            "tables": {n: {**{k: v for k, v in t.items() if k not in ("files", "referenced_by")},
                           "files": sorted(t["files"]), "referenced_by": sorted(t["referenced_by"])} for n, t in idx.tables.items()},
            "programs": {k: {"type": p["type"], "units": p["units"], "uses": p.get("uses", []), "calls": p.get("calls", []),
                             "called_by": sorted(p.get("called_by", [])), "files": sorted(p["files"])} for k, p in idx.programs.items()},
            "sequences": sorted(idx.sequences),
            "apex": {a: {str(n): {"name": pg["name"], "uses": pg["uses"], "calls": pg["calls"]} for n, pg in v["pages"].items()} for a, v in idx.apex.items()},
            "documents": sorted(idx.docs)}
    with open(os.path.join(out, "objects.json"), "w", encoding="utf-8") as f:
        json.dump(dump, f, indent=1)
    if copy_src:
        dst = os.path.join(out, "src")
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(src_root, dst, ignore=shutil.ignore_patterns(".git", "*.zip"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--out", default=os.path.join(here, "..", "skills", "skmch-hrd-system-context", "references"))
    ap.add_argument("--schema", default="HRD")
    ap.add_argument("--copy-src", action="store_true", help="also copy raw sources into <out>/src")
    a = ap.parse_args()
    idx = Index(a.schema)
    for root, dirs, files in os.walk(a.folder):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in files:
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, a.folder)
            ext = os.path.splitext(fn)[1].lower()
            if ext == ".csv":
                if not idx.parse_csv(path, rel):
                    idx.docs.append(rel)
                continue
            if ext in DOC_EXT:
                idx.docs.append(rel)
                continue
            if ext not in SRC_EXT:
                continue
            with open(path, encoding="utf-8", errors="ignore") as f:
                raw = f.read()
            if re.search(r"wwv_flow_(imp|api)|wwv_flow_imp_page", raw, re.I):
                idx.parse_apex(raw, rel)
                continue
            text = strip_comments(raw)
            idx.parse_ddl(text, rel)
            idx.parse_plsql(text, rel)
    idx.link()
    os.makedirs(a.out, exist_ok=True)
    write(idx, a.out, a.folder, a.copy_src)
    print(f"Indexed {len(idx.tables)} tables, {len(idx.programs)} code objects, "
          f"{sum(len(v['pages']) for v in idx.apex.values())} APEX pages, {len(idx.docs)} documents → {os.path.relpath(a.out)}")


if __name__ == "__main__":
    main()
