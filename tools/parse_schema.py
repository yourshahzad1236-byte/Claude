#!/usr/bin/env python3
"""Parse PL/SQL Developer "Export User Objects" scripts into Markdown docs.

Usage:
    python tools/parse_schema.py <export.sql|.txt> [<export> ...] --out docs/schema

For every input file it writes <OUT>/<SCHEMA>.md (full data dictionary) and
refreshes <OUT>/README.md (index of all schemas documented so far).
It also writes a compact per-schema reference used by the skm-domain skill
when --skill-refs <dir> is given.
"""
import argparse
import json
import os
import re
from collections import defaultdict, OrderedDict

SECTION_RE = re.compile(
    r"^prompt Creating (table|view|sequence|package body|package|procedure|function|trigger|type body|type|synonym|materialized view|java source) (\S+)\s*$",
    re.I | re.M,
)
COMMENT_RE = re.compile(
    r"comment on (table|column) ([\w$#.\"]+)\s+is\s+'((?:[^']|'')*)'\s*;", re.I | re.S
)
CONSTRAINT_RE = re.compile(
    r"alter table ([\w$#.\"]+)\s+add constraint ([\w$#\"]+)\s+(primary key|unique|foreign key|check)\s*(.*?);",
    re.I | re.S,
)
INDEX_RE = re.compile(
    r"create (unique |bitmap )?index ([\w$#.\"]+) on ([\w$#.\"]+)\s*\(([^;]*?)\)\s*(?:\n|tablespace|;|local|nologging|compress|reverse)",
    re.I | re.S,
)
TABLE_RE = re.compile(
    r"create (global temporary )?table ([\w$#.\"]+)\s*\((.*?)\n\)", re.I | re.S
)
COL_RE = re.compile(r"^\s*(\"?[\w$#]+\"?)\s+(.+?)\s*,?\s*$")
TRIGGER_HDR_RE = re.compile(
    r"TRIGGER\s+([\w$#.\"]+)\s+(.*?)\s+ON\s+([\w$#.\"]+)", re.I | re.S
)
SYN_RE = re.compile(r"synonym ([\w$#.\"]+)\s+for ([\w$#.@\"]+)\s*;", re.I)
SEQ_RE = re.compile(r"create sequence ([\w$#.\"]+)(.*?);", re.I | re.S)
SUBPROG_RE = re.compile(
    r"^\s*(procedure|function)\s+([\w$#\"]+)(.*?);", re.I | re.S | re.M
)
STANDALONE_RE = re.compile(
    r"create or replace (?:editionable )?(procedure|function)\s+([\w$#.\"]+)(.*?)\b(is|as)\b",
    re.I | re.S,
)


def short(name):
    return name.replace('"', "").split(".")[-1].upper()


def unquote(s):
    return s.replace("''", "'").strip()


def strip_comments(sql):
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    sql = re.sub(r"--[^\n]*", " ", sql)
    return sql


def one_line(s, limit=None):
    s = re.sub(r"\s+", " ", s).strip()
    if limit and len(s) > limit:
        s = s[: limit - 3] + "..."
    return s


def md_escape(s):
    return s.replace("|", "\\|").replace("\n", " ").replace("\r", "")


def parse(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read().replace("\r\n", "\n")

    sections = []
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append((m.group(1).lower(), m.group(2).upper(), text[m.end():end]))

    schema = None
    m = re.search(r"create (?:global temporary )?table (\w+)\.", text, re.I) or re.search(
        r"create or replace \w+ (\w+)\.", text, re.I
    )
    if m:
        schema = m.group(1).upper()

    db = {
        "schema": schema,
        "tables": OrderedDict(),
        "views": OrderedDict(),
        "sequences": OrderedDict(),
        "packages": OrderedDict(),
        "procedures": OrderedDict(),
        "functions": OrderedDict(),
        "triggers": OrderedDict(),
        "types": OrderedDict(),
        "synonyms": OrderedDict(),
    }

    for kind, name, body in sections:
        if kind == "table":
            parse_table(db, name, body)
        elif kind == "view":
            vm = re.search(r"create or replace (?:force )?(?:editionable )?view\s+[\w$#.\"]+\s*(\([^)]*\))?\s*as\s*(.*)", body, re.I | re.S)
            sql = vm.group(2).strip() if vm else body.strip()
            sql = re.sub(r"\n\s*prompt\s*$", "", sql.strip(), flags=re.I).strip()
            srcs = sorted(
                {short(x) for x in re.findall(r"\b(?:from|join)\s+([\w$#.\"]+)", strip_comments(sql), re.I)}
                - {"DUAL", "TABLE", "(", "SELECT"}
            )
            db["views"][name] = {"sql": sql, "sources": srcs}
        elif kind == "sequence":
            sm = SEQ_RE.search(body)
            opts = one_line(sm.group(2)) if sm else ""
            db["sequences"][name] = opts
        elif kind == "package":
            spec = strip_comments(body)
            subs = []
            for sm in SUBPROG_RE.finditer(spec):
                subs.append((sm.group(1).upper(), sm.group(2).upper(), one_line(sm.group(3), 400)))
            doc = leading_doc(body)
            db["packages"].setdefault(name, {"subprograms": [], "doc": "", "has_body": False})
            db["packages"][name]["subprograms"] = subs
            db["packages"][name]["doc"] = doc
        elif kind == "package body":
            db["packages"].setdefault(name, {"subprograms": [], "doc": "", "has_body": False})
            db["packages"][name]["has_body"] = True
        elif kind in ("procedure", "function"):
            sm = STANDALONE_RE.search(strip_comments(body))
            sig = one_line(sm.group(3), 400) if sm else ""
            db[kind + "s"][name] = {"signature": sig, "doc": leading_doc(body)}
        elif kind == "trigger":
            tm = TRIGGER_HDR_RE.search(strip_comments(body))
            if tm:
                event = one_line(tm.group(2))
                table = short(tm.group(3))
                row = bool(re.search(r"for each row", body[:2000], re.I))
                db["triggers"][name] = {"table": table, "event": event, "row": row}
            else:
                db["triggers"][name] = {"table": "", "event": "", "row": False}
        elif kind == "type":
            tm = re.search(r"type\s+[\w$#.\"]+\s+(?:force\s+)?(as|is)\s+(.*?)(?:;|\n/)", body, re.I | re.S)
            db["types"][name] = one_line(tm.group(2), 600) if tm else ""
        elif kind == "synonym":
            sm = SYN_RE.search(body)
            db["synonyms"][name] = sm.group(2).replace('"', "") if sm else ""

    return db


def leading_doc(body):
    m = re.search(r"/\*+(.*?)\*/", body[:4000], re.S)
    if not m:
        return ""
    doc = m.group(1)
    om = re.search(r"(?:OBJECTIVE|PURPOSE|DESCRIPTION)\s*:?=?\s*(.*?)(?:\n\s*-{5,}|REVISIONS|\n\s*\n)", doc, re.I | re.S)
    if om:
        return one_line(om.group(1).strip("=: -*"), 300)
    return ""


def parse_table(db, name, body):
    tm = TABLE_RE.search(body)
    if not tm:
        return
    cols = OrderedDict()
    for line in tm.group(3).split("\n"):
        line = line.rstrip()
        if not line.strip():
            continue
        cm = COL_RE.match(line)
        if not cm:
            continue
        col = cm.group(1).replace('"', "").upper()
        spec = cm.group(2).rstrip(",")
        not_null = bool(re.search(r"\bnot null\b", spec, re.I))
        spec_nn = re.sub(r"\s*\bnot null\b", "", spec, flags=re.I)
        dm = re.search(r"\bdefault\b\s*(.*)$", spec_nn, re.I)
        default = dm.group(1).strip() if dm else ""
        dtype = spec_nn[: dm.start()].strip() if dm else spec_nn.strip()
        dtype = re.sub(r"\s+(generated|invisible|visible).*$", "", dtype, flags=re.I)
        cols[col] = {"type": dtype, "not_null": not_null, "default": default, "comment": ""}

    t = {
        "temporary": bool(tm.group(1)),
        "columns": cols,
        "comment": "",
        "pk": None,
        "uks": [],
        "fks": [],
        "checks": [],
        "indexes": [],
    }
    db["tables"][name] = t

    for cm in COMMENT_RE.finditer(body):
        target = cm.group(2).replace('"', "").upper().split(".")
        txt = unquote(cm.group(3))
        if cm.group(1).lower() == "table":
            t["comment"] = txt
        else:
            c = target[-1]
            if c in cols:
                cols[c]["comment"] = txt

    for km in CONSTRAINT_RE.finditer(body):
        cname = km.group(2).replace('"', "").upper()
        ctype = km.group(3).lower()
        rest = km.group(4)
        disabled = bool(re.search(r"\bdisable\b", rest, re.I))
        if ctype in ("primary key", "unique"):
            cm2 = re.match(r"\s*\((.*?)\)", rest, re.S)
            ccols = one_line(cm2.group(1)).upper() if cm2 else ""
            if ctype == "primary key":
                t["pk"] = {"name": cname, "cols": ccols}
            else:
                t["uks"].append({"name": cname, "cols": ccols})
        elif ctype == "foreign key":
            fm = re.match(r"\s*\((.*?)\)\s*references\s+([\w$#.\"]+)\s*\((.*?)\)(.*)", rest, re.S | re.I)
            if fm:
                ref = fm.group(2).replace('"', "").upper()
                t["fks"].append({
                    "name": cname,
                    "cols": one_line(fm.group(1)).upper(),
                    "ref_table": ref,
                    "ref_cols": one_line(fm.group(3)).upper(),
                    "on_delete": "CASCADE" if re.search(r"on delete cascade", fm.group(4), re.I)
                    else ("SET NULL" if re.search(r"on delete set null", fm.group(4), re.I) else ""),
                    "disabled": disabled,
                })
        else:
            cond = re.sub(r"\s*(disable|enable|novalidate|validate|deferrable.*)\s*$", "", rest.strip(), flags=re.I)
            cond = re.sub(r"\s*(disable|enable|novalidate|validate)\s*$", "", cond, flags=re.I)
            t["checks"].append({"name": cname, "cond": one_line(cond, 300), "disabled": disabled})

    for im in INDEX_RE.finditer(body):
        t["indexes"].append({
            "name": short(im.group(2)),
            "kind": (im.group(1) or "").strip().upper(),
            "cols": one_line(im.group(4)).upper(),
        })


# ---------------------------------------------------------------- output


def anchor(name):
    return name.lower().replace("$", "").replace("#", "")


def write_full(db, out_dir, source_name):
    s = db["schema"]
    tables = db["tables"]
    trig_by_table = defaultdict(list)
    for tn, tr in db["triggers"].items():
        trig_by_table[tr["table"]].append((tn, tr))
    referenced_by = defaultdict(list)
    for tn, t in tables.items():
        for fk in t["fks"]:
            referenced_by[fk["ref_table"]].append((f"{s}.{tn}", fk))

    L = []
    L.append(f"# {s} schema\n")
    L.append(f"_Generated from `{source_name}` by `tools/parse_schema.py`. Do not edit by hand — re-run the script._\n")
    L.append("## Summary\n")
    L.append("| Object type | Count |\n|---|---|")
    for label, key in [("Tables", "tables"), ("Views", "views"), ("Sequences", "sequences"),
                       ("Packages", "packages"), ("Procedures", "procedures"), ("Functions", "functions"),
                       ("Triggers", "triggers"), ("Types", "types"), ("Synonyms", "synonyms")]:
        L.append(f"| {label} | {len(db[key])} |")
    fk_total = sum(len(t["fks"]) for t in tables.values())
    L.append(f"| Foreign keys | {fk_total} |")
    L.append("")

    external = defaultdict(set)
    for tn, t in tables.items():
        for fk in t["fks"]:
            rs = fk["ref_table"].split(".")[0] if "." in fk["ref_table"] else s
            if rs != s:
                external[rs].add(fk["ref_table"])
    if external:
        L.append("### Cross-schema foreign-key dependencies\n")
        for rs, refs in sorted(external.items()):
            L.append(f"- **{rs}**: " + ", ".join(f"`{r}`" for r in sorted(refs)))
        L.append("")

    # Table index
    L.append("## Tables\n")
    L.append("| Table | Cols | PK | Description |\n|---|---|---|---|")
    for tn, t in tables.items():
        pk = t["pk"]["cols"] if t["pk"] else ""
        tmp = " _(GTT)_" if t["temporary"] else ""
        L.append(f"| [{tn}](#{anchor(tn)}){tmp} | {len(t['columns'])} | {md_escape(pk)} | {md_escape(t['comment'])} |")
    L.append("")

    for tn, t in tables.items():
        L.append(f"### {tn}\n")
        if t["temporary"]:
            L.append("_Global temporary table._\n")
        if t["comment"]:
            L.append(f"{t['comment']}\n")
        L.append("| # | Column | Type | Null | Default | Comment |\n|---|---|---|---|---|---|")
        pkcols = {c.strip() for c in t["pk"]["cols"].split(",")} if t["pk"] else set()
        fkcols = {}
        for fk in t["fks"]:
            for c in fk["cols"].split(","):
                fkcols[c.strip()] = fk["ref_table"]
        for i, (cn, c) in enumerate(t["columns"].items(), 1):
            mark = ""
            if cn in pkcols:
                mark += " 🔑"
            if cn in fkcols:
                mark += f" → `{fkcols[cn]}`"
            L.append(
                f"| {i} | **{cn}**{mark} | {md_escape(c['type'])} | {'N' if c['not_null'] else 'Y'} | "
                f"{md_escape(c['default'])} | {md_escape(c['comment'])} |"
            )
        L.append("")
        if t["pk"]:
            L.append(f"- **Primary key** `{t['pk']['name']}` ({t['pk']['cols']})")
        for uk in t["uks"]:
            L.append(f"- **Unique** `{uk['name']}` ({uk['cols']})")
        for fk in t["fks"]:
            extra = []
            if fk["on_delete"]:
                extra.append(f"ON DELETE {fk['on_delete']}")
            if fk["disabled"]:
                extra.append("DISABLED")
            ex = f" _{', '.join(extra)}_" if extra else ""
            L.append(f"- **FK** `{fk['name']}` ({fk['cols']}) → `{fk['ref_table']}` ({fk['ref_cols']}){ex}")
        for ck in t["checks"]:
            dis = " _DISABLED_" if ck["disabled"] else ""
            L.append(f"- **Check** `{ck['name']}`: `{md_escape(ck['cond'])}`{dis}")
        for ix in t["indexes"]:
            k = f"{ix['kind']} " if ix["kind"] else ""
            L.append(f"- **{k}Index** `{ix['name']}` ({ix['cols']})")
        refs = referenced_by.get(f"{s}.{tn}", [])
        if refs:
            L.append("- **Referenced by**: " + ", ".join(sorted({f"`{r[0].split('.')[-1]}`" for r in refs})))
        trs = trig_by_table.get(tn, [])
        if trs:
            L.append("- **Triggers**: " + ", ".join(f"`{n}` ({tr['event']})" for n, tr in trs))
        L.append("")

    if db["views"]:
        L.append("## Views\n")
        for vn, v in db["views"].items():
            L.append(f"### {vn}\n")
            if v["sources"]:
                L.append("Sources: " + ", ".join(f"`{x}`" for x in v["sources"]) + "\n")
            L.append("```sql\n" + v["sql"].rstrip().rstrip(";") + "\n```\n")

    if db["sequences"]:
        L.append("## Sequences\n")
        L.append("| Sequence | Options |\n|---|---|")
        for n, o in db["sequences"].items():
            L.append(f"| {n} | {md_escape(o)} |")
        L.append("")

    if db["packages"]:
        L.append("## Packages\n")
        for pn, p in db["packages"].items():
            L.append(f"### {pn}\n")
            if p["doc"]:
                L.append(f"{p['doc']}\n")
            if p["subprograms"]:
                for kind, sn, sig in p["subprograms"]:
                    L.append(f"- `{kind.lower()} {sn}{md_escape(sig)}`")
            else:
                L.append("_No public subprograms parsed from the specification._")
            L.append("")

    for key, label in (("procedures", "Procedures"), ("functions", "Functions")):
        if db[key]:
            L.append(f"## Standalone {label}\n")
            for n, p in db[key].items():
                doc = f" — {p['doc']}" if p["doc"] else ""
                L.append(f"- `{n}{md_escape(p['signature'])}`{doc}")
            L.append("")

    if db["types"]:
        L.append("## Types\n")
        for n, d in db["types"].items():
            L.append(f"- **{n}**: `{md_escape(d)}`")
        L.append("")

    if db["triggers"]:
        L.append("## Triggers\n")
        L.append("| Trigger | Table | Event | Row-level |\n|---|---|---|---|")
        for n, tr in db["triggers"].items():
            L.append(f"| {n} | {tr['table']} | {md_escape(tr['event'])} | {'Y' if tr['row'] else 'N'} |")
        L.append("")

    if db["synonyms"]:
        L.append("## Synonyms\n")
        L.append("| Synonym | Target |\n|---|---|")
        for n, tgt in db["synonyms"].items():
            L.append(f"| {n} | {tgt} |")
        L.append("")

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{s}.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


AUDIT_COLS = ["ORIGINAL_USER_ID", "ORIGINAL_TERMINAL", "ORIGINAL_TRN_DATE", "USER_ID", "TERMINAL", "TRN_DATE"]
ML_COLS = ["ORG_ID", "ZON_ID", "LOC_ID", "WS_SYNC_DATE"]


def write_compact(db, ref_dir):
    """One block per table: grep-friendly reference for the skm-domain skill."""
    s = db["schema"]
    L = [f"# {s} — compact table reference\n",
         "Generated by `tools/parse_schema.py`. Search with `grep -n '^## TABLE_NAME' <this file>`.\n",
         "Legend: `*` = primary-key column, `!` = NOT NULL, `«…»` = column comment.",
         "`[+audit]` = has the 6 standard audit columns (ORIGINAL_USER_ID, ORIGINAL_TERMINAL, ORIGINAL_TRN_DATE, USER_ID, TERMINAL, TRN_DATE) — omitted from `cols`.",
         "`[+ml]` = has the 4 multi-location columns (ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE) — omitted from `cols`.",
         "`fk … [disabled]` = constraint exists but is DISABLED/NOVALIDATE: the relationship is logical only, not enforced.\n"]
    for tn, t in db["tables"].items():
        pkcols = {c.strip() for c in t["pk"]["cols"].split(",")} if t["pk"] else set()
        desc = f" — {one_line(t['comment'], 400)}" if t["comment"] else ""
        tmp = " [GTT]" if t["temporary"] else ""
        has_audit = all(c in t["columns"] for c in AUDIT_COLS)
        has_ml = all(c in t["columns"] for c in ML_COLS)
        skip = set()
        flags = ""
        if has_audit:
            skip |= set(AUDIT_COLS) - pkcols
            flags += " [+audit]"
        if has_ml:
            skip |= set(ML_COLS) - pkcols
            flags += " [+ml]"
        L.append(f"## {tn}{tmp}{flags}{desc}")
        cols = []
        for cn, c in t["columns"].items():
            if cn in skip:
                continue
            flag = ("*" if cn in pkcols else "") + ("!" if c["not_null"] and cn not in pkcols else "")
            cc = f" «{one_line(c['comment'], 300)}»" if c["comment"] else ""
            cols.append(f"{cn} {c['type']}{flag}{cc}")
        L.append("cols: " + "; ".join(cols))
        for fk in t["fks"]:
            L.append(f"fk: ({fk['cols']}) → {fk['ref_table']}({fk['ref_cols']})" + (" [disabled]" if fk["disabled"] else ""))
        for uk in t["uks"]:
            L.append(f"uk: ({uk['cols']})")
        for ck in t["checks"]:
            if not re.fullmatch(r'"?\w+"?\s+is not null', ck["cond"], re.I):
                L.append(f"check: {ck['cond']}")
        L.append("")
    if db["views"]:
        L.append("# Views\n")
        for vn, v in db["views"].items():
            L.append(f"- {vn}: from {', '.join(v['sources'])}")
        L.append("")
    if db["packages"]:
        L.append("# Packages (public API)\n")
        for pn, p in db["packages"].items():
            names = sorted({f"{sn}" for _, sn, _ in p["subprograms"]})
            doc = f" — {p['doc']}" if p["doc"] else ""
            L.append(f"- {pn}{doc}: {', '.join(names)}")
        L.append("")
    for key in ("procedures", "functions"):
        if db[key]:
            L.append(f"# Standalone {key}\n")
            for n, p in db[key].items():
                L.append(f"- {n}{p['signature']}")
            L.append("")
    if db["sequences"]:
        L.append("# Sequences\n")
        L.append(", ".join(db["sequences"].keys()) + "\n")
    os.makedirs(ref_dir, exist_ok=True)
    with open(os.path.join(ref_dir, f"{s}.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def write_stats(db, out_dir):
    tables = db["tables"]
    stats = {
        "schema": db["schema"],
        "counts": {k: len(db[k]) for k in ("tables", "views", "sequences", "packages", "procedures",
                                           "functions", "triggers", "types", "synonyms")},
        "fk_total": sum(len(t["fks"]) for t in tables.values()),
        "tables_without_pk": [tn for tn, t in tables.items() if not t["pk"] and not t["temporary"]],
    }
    with open(os.path.join(out_dir, f".{db['schema']}.stats.json"), "w") as fh:
        json.dump(stats, fh, indent=1)
    return stats


def write_index(out_dir):
    rows = []
    for f in sorted(os.listdir(out_dir)):
        if f.startswith(".") and f.endswith(".stats.json"):
            with open(os.path.join(out_dir, f)) as fh:
                rows.append(json.load(fh))
    L = ["# Database schema documentation\n",
         "Generated by `tools/parse_schema.py` from PL/SQL Developer object exports.\n",
         "| Schema | Tables | Views | Packages | Procedures | Functions | Triggers | Sequences | Synonyms | FKs |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        c = r["counts"]
        L.append(f"| [{r['schema']}]({r['schema']}.md) | {c['tables']} | {c['views']} | {c['packages']} | "
                 f"{c['procedures']} | {c['functions']} | {c['triggers']} | {c['sequences']} | {c['synonyms']} | {r['fk_total']} |")
    L.append("\nRegenerate with:\n\n```bash\npython tools/parse_schema.py schema/*.txt --out docs/schema --skill-refs skm-domain/references\n```\n")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default="docs/schema")
    ap.add_argument("--skill-refs")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for f in a.files:
        if os.path.getsize(f) == 0:
            print(f"skip (empty): {f}")
            continue
        db = parse(f)
        if not db["schema"]:
            print(f"skip (no schema detected): {f}")
            continue
        write_full(db, a.out, re.sub(r"^[0-9a-f]{8}-", "", os.path.basename(f)))
        st = write_stats(db, a.out)
        if a.skill_refs:
            write_compact(db, a.skill_refs)
        print(db["schema"], st["counts"], "fks", st["fk_total"], "no-pk", len(st["tables_without_pk"]))
    write_index(a.out)


if __name__ == "__main__":
    main()
