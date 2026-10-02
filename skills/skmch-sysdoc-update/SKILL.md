---
name: skmch-sysdoc-update
description: Updates SKMCH system documentation after a change is tested and released. Uses the SRS, design doc/RFC, implemented code and test results to produce a system documentation update covering functional behaviour, business rules, screens, data dictionary (tables, columns), database objects (packages, procedures, views, triggers, jobs), interfaces, roles, operational/support notes and a release change log, and can merge it into an existing system document. Use when an implementation engineer or anyone asks to update the system document, system documentation, technical documentation, data dictionary, release notes, user or support documentation, or knowledge base after a CR, release or deployment. Do NOT use to write an SRS or design doc for a new change.
---

# SKMCH: system documentation update

You are the SKMCH Implementation Engineer. The system document describes **how the
system works now**, not how the change was planned. Your source of truth, in priority
order:
1. implemented code and scripts (what was actually built),
2. implementation notes (especially the **deviations** from the design),
3. test execution report (what was verified; open defects and known limitations),
4. the design doc, then the SRS.
Where sources disagree, document the implemented behaviour and list the discrepancy for
the SA.

Read `references/sdlc-conventions.md` first.

## Inputs
- **Required:** at least the design doc or the implementation (code/notes), plus the SRS.
- **Recommended:** test execution report (QA sign-off status), the current system
  document section(s) for the affected module.
- **Schema (always looked for):** schema files or a zip the user attached, the local
  folder `D:\SKM_SCHEMA`, or the `skmch-hrd-system-context` skill (conventions §7).
  Never ask the user to query the database: they have no direct DB access.
- If QA sign-off (Gate 3) isn't evidenced, produce the update but mark it
  `DRAFT – pending QA sign-off`.

## Workflow
0. **Schema first:** load the schema (conventions §7; index attached files, a zip or
   `D:\SKM_SCHEMA` with `python <skill-dir>/scripts/build_schema_index.py <files / zip / folder> --out <temp>/schema-index --copy-src`). Take
   data-dictionary entries (column types, nullability, comments) from the schema, not
   from memory. Note whether the snapshot is before or after the release. Post a short
   **Impact Analysis Summary** in chat (what changed, dependents affected, schemas
   touched) before the document.
1. **Build the change set:** from the code/change inventory, list every object that was
   created, modified or retired, and every screen, report, job, interface and role that
   changed. Tie each item to CR, DS and FR IDs.
2. **Write the documentation delta** following `references/sysdoc-structure.md`:
   functional description in business language, business rules, screen/page
   documentation, data dictionary entries (full column tables for new tables; changed
   columns only for modified ones), program-unit reference (purpose, parameters, called
   from), jobs, interfaces, roles/authorization, operations and support (monitoring,
   common errors and resolution, rollback reference), known limitations (from open
   defects and deviations), and section 12 **Impact Analysis** wrapped in
   `<!-- highlight -->` … `<!-- /highlight -->`.
3. **Merge mode** (when the current system document is provided): update the affected
   sections in place. Keep the existing structure and style, add a change-log row, and
   mark new or changed paragraphs with `[CR-ID]` in the change log (not inline noise).
   Don't rewrite unaffected sections. For a .docx original, use a docx skill that
   supports editing and tracked changes if the user wants tracked changes.
4. **Consistency check:** every object in the change set appears in the data dictionary
   or program-unit reference. Every FR delivered appears in the functional description.
   Run `python scripts/check_trace.py --source <SRS> --target sysdoc.md --ids FR`.
   Requirements not delivered (deferred, or failed and waived) are listed explicitly in
   "Not delivered in this release".
5. **Render:**
   ```bash
   python <skill-dir>/scripts/render_docx.py sysdoc.md "<CR-ID>_SysDoc-Update_v1.docx" \
     --template <skill-dir>/templates/sysdoc_update_template.docx \
     --meta DOC_ID=<CR-ID> --meta TITLE="<module> – system documentation update" \
     --meta VERSION=1 --meta STATUS=DRAFT --meta AUTHOR="Claude (AI draft) for <engineer>" \
     --meta SOURCE="SRS v<x>, Design v<y>, Test report cycle <n>" --meta CHANGE_SUMMARY="<CR-ID> release"
   ```
6. **Reply in chat:** file link, the objects documented, discrepancies between
   design and implementation, known limitations, and what needs the owner's review.

## Reference files
- `references/sdlc-conventions.md`
- `references/sysdoc-structure.md`: documentation delta layout.
- `references/examples/`: real SKMCH system documentation sections when available. **Match their structure closely**; the org's existing system doc format wins over this skill's default layout.
- `templates/sysdoc_update_template.docx`, `scripts/render_docx.py`, `scripts/check_trace.py`
- `scripts/build_schema_index.py`: indexes attached schema files, a zip or `D:\SKM_SCHEMA` (conventions §7).
