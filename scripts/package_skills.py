#!/usr/bin/env python3
"""Sync shared files into every SKMCH skill, validate the skills, and build dist/*.skill.

Each skill must work when uploaded on its own (claude.ai org skills), so shared
references and scripts are COPIED into each skill that needs them. Edit the originals in
shared/ (or skills/oracle-plsql-apex-hrd-standards/SKILL.md), never the copies.

Usage:
  python scripts/package_skills.py            # sync + validate + build dist/ (+ bundle zips)
  python scripts/package_skills.py --check    # verify copies are in sync + validate (CI); no writes
"""
import argparse
import os
import re
import sys
import zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILLS = os.path.join(ROOT, "skills")
SHARED = os.path.join(ROOT, "shared")
DIST = os.path.join(ROOT, "dist")
STANDARDS = os.path.join(SKILLS, "oracle-plsql-apex-hrd-standards", "SKILL.md")

# skill -> (shared references, shared scripts)
MANIFEST = {
    "skmch-ba-srs": (["sdlc-conventions.md", "srs-structure.md", "hrd-naming-standards.md"], ["render_docx.py", "build_schema_index.py"]),
    "skmch-sa-srs-review": (["sdlc-conventions.md", "srs-structure.md", "hrd-naming-standards.md"], ["render_docx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-sa-design-rfc": (["sdlc-conventions.md", "hrd-naming-standards.md"], ["render_docx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-dev-implement": (["sdlc-conventions.md", "hrd-naming-standards.md"], ["render_docx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-qa-testcases": (["sdlc-conventions.md"], ["render_xlsx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-qa-execute": (["sdlc-conventions.md"], ["render_xlsx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-sysdoc-update": (["sdlc-conventions.md"], ["render_docx.py", "check_trace.py", "build_schema_index.py"]),
    "skmch-sdlc-guide": (["sdlc-conventions.md"], ["check_trace.py", "build_schema_index.py"]),
    "skmch-hrd-system-context": ([], ["build_schema_index.py"]),
}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def shared_content(kind, name):
    if name == "hrd-naming-standards.md":
        s = open(STANDARDS, encoding="utf-8").read()
        body = s.split("\n---", 2)[-1] if s.startswith("---") else s
        return ("<!-- Copied from skills/oracle-plsql-apex-hrd-standards/SKILL.md by scripts/package_skills.py. "
                "Edit the original, not this copy. -->\n" + body.lstrip("\n")).encode()
    return open(os.path.join(SHARED, kind, name), "rb").read()


def sync(check):
    stale = []
    for skill, (refs, scripts) in MANIFEST.items():
        for kind, sub, names in (("references", "references", refs), ("scripts", "scripts", scripts)):
            for n in names:
                dst = os.path.join(SKILLS, skill, sub, n)
                want = shared_content(kind, n)
                have = open(dst, "rb").read() if os.path.exists(dst) else None
                if have != want:
                    stale.append(os.path.relpath(dst, ROOT))
                    if not check:
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        with open(dst, "wb") as f:
                            f.write(want)
    return stale


def validate():
    errors = []
    for skill in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, skill, "SKILL.md")
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{skill}: missing YAML frontmatter"); continue
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name or name.group(1).strip().strip('"') != skill:
            errors.append(f"{skill}: frontmatter name must equal folder name")
        elif not NAME_RE.match(skill):
            errors.append(f"{skill}: name must be lowercase letters, digits, hyphens (<=64)")
        if not desc:
            errors.append(f"{skill}: missing description")
        else:
            d = desc.group(1).strip()
            if len(d) > 1024:
                errors.append(f"{skill}: description is {len(d)} chars (max 1024)")
            if "<" in d or ">" in d:
                errors.append(f"{skill}: description must not contain angle brackets")
        for ref in re.findall(r"`((?:references|templates|scripts)/[\w./-]+?)`", text):
            if "<" in ref or ref.endswith("/"):
                continue
            if not os.path.exists(os.path.join(SKILLS, skill, ref)):
                errors.append(f"{skill}: SKILL.md mentions missing file {ref}")
    return errors


def build():
    os.makedirs(DIST, exist_ok=True)
    for f in os.listdir(DIST):
        if f.endswith(".skill"):
            os.remove(os.path.join(DIST, f))
    for skill in sorted(os.listdir(SKILLS)):
        base = os.path.join(SKILLS, skill)
        if not os.path.isfile(os.path.join(base, "SKILL.md")):
            continue
        out = os.path.join(DIST, f"{skill}.skill")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(base):
                dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
                for fn in sorted(files):
                    if fn.endswith(".pyc") or fn.startswith("."):
                        continue
                    full = os.path.join(root, fn)
                    z.write(full, os.path.join(skill, os.path.relpath(full, base)))
        print(f"built dist/{skill}.skill ({os.path.getsize(out) // 1024} KB)")
    bundle()


# Generated schema snapshot inside skmch-hrd-system-context (kept out of git and the plugin zip).
PRIVATE = ("skills/skmch-hrd-system-context/references/tables/", "skills/skmch-hrd-system-context/references/programs/",
           "skills/skmch-hrd-system-context/references/schemas/", "skills/skmch-hrd-system-context/references/apex/",
           "skills/skmch-hrd-system-context/references/src", "schema/")


def bundle():
    skills_zip = os.path.join(DIST, "skmch-sdlc-all-skills.zip")
    with zipfile.ZipFile(skills_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(DIST)):
            if f.endswith(".skill"):
                z.write(os.path.join(DIST, f), f)
    plugin_zip = os.path.join(DIST, "skmch-sdlc-plugin.zip")
    with zipfile.ZipFile(plugin_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = sorted(d for d in dirs if d not in (".git", "__pycache__", "demo"))
            for fn in sorted(files):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
                if fn.endswith((".pyc", ".zip")) or fn == ".DS_Store" or fn.startswith("~$"):
                    continue
                if rel.startswith(PRIVATE) and rel != "schema/README.md":
                    continue
                z.write(full, rel)
    print("built dist/skmch-sdlc-all-skills.zip and dist/skmch-sdlc-plugin.zip")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    stale = sync(a.check)
    if stale:
        print(("Out of sync (run scripts/package_skills.py):\n  " if a.check else "Synced:\n  ") + "\n  ".join(stale))
    errors = validate()
    for e in errors:
        print("ERROR:", e)
    if errors or (a.check and stale):
        sys.exit(1)
    if not a.check:
        build()
    print("OK")


if __name__ == "__main__":
    main()
