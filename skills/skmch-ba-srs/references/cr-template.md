# SKMCH Change Request (CR) document: client template

Use this layout whenever the user asks for a **CR**, or for requirements "in my CR
template". It is the client-facing document. The detailed SRS (`srs-structure.md`) stays
the internal source of IDs, acceptance criteria and impact analysis. The CR may merge the
SRS detail into this layout when the user asks for one combined document.

Status: FINAL template agreed with the user on 09-Oct-2026 (reference CR: `docs/CR-2026-XXX-PEV/CR-2026-XXX-PEV_CR_v0.4`).
Use exactly this layout for every new CR.
GUI template supplied on 09-Oct-2026 (see "GUI template" below).

## Section layout (final, client-approved rules)

0. **Control table**: CR No., module/schema, requested by, prepared by, version/status, date, sources.
   Add one note line: Q-NN / A-NN references point to the internal SRS, and table details are in
   the Design Document.
1. **Client Needs / Expectations**: keep all sub-sections: Business requirements, Background,
   Current process (As-Is, from the schema), Scope (in/out), Stakeholders, Definitions, References.
2. **Workflow**: **graphical swimlane diagram** (PNG embedded, editable SVG beside it), never
   ASCII, plus a short step table (actor, action, status) and the status model. Generator:
   `scripts/example_workflow_diagram.py`.
3. **Functional Requirements**: for each client requirement: a short description with summary
   acceptance, **Prototype (GUI)** images in the SKMCH GUI template, then the **detailed FR-NNN**
   blocks (Given/When/Then acceptance criteria). Generator: `scripts/gui_prototypes_skmch_template.py`.
   Use synthetic data only; never copy real names or codes from screenshots.
4. **Business Rules, Data and Access**: all **bullets**, no tables:
   - 4.1 Business rules (RULE-NN, one line each)
   - 4.2 Data requirements, **only items needed for development**: field, type/length, mandatory,
     validation, source table.column. Point to the Design Document for full table definitions.
   - 4.3 User roles and access (one bullet per role)
   - 4.4 Reports and notifications (one bullet each)
5. **Impact Analysis**: **bullets and plain text**, no tables: 5.1 Business, 5.2 System, 5.3 Database.
   Keep the key schema facts (trigger side effects, reused frameworks). **No Risks sub-section.**

**Exclude from the CR** (keep them in the internal SRS or give them in chat):
Non-functional Requirements, Risks, System Interfaces (hardware/software), Assumptions/Constraints/Dependencies, Open Points / open
questions list, Appendix A (MoM breakdown), Appendix B (traceability). Give the blocking open
questions to the user in chat instead.

## Design Document (DD) for a CR

When the user asks for the **DD** (it means **Design Document**, not data dictionary), use the
`skmch-sa-design-rfc` skill, written **short and in bullet points**, and include:
1. a design summary and key decisions (bullets);
2. the DB structure: an **ER diagram image** (SVG → PNG), new tables as column bullets (name,
   type, key, purpose), and the existing objects used, with read/write and trigger side effects;
3. technical details: package procedures (signature, numbered logic, error codes, commit owner),
   changes to existing packages, jobs, notifications, authorization schemes;
4. **GUI pages**: one bullet block per APEX page (regions, items, buttons → package calls,
   authorization) followed by the prototype image;
5. requirement coverage (list every FR/NFR ID explicitly, then run `check_trace.py`);
6. change inventory / deployment order, verification, rollback, dependents to retest;
7. risks and open questions (bullets).
Also write `<CR-ID>_01_ddl.sql` and `<CR-ID>_99_rollback.sql`. File: `<CR-ID>_Design_v<ver>.md/.docx`.

## GUI template (SKMCH APEX screens, from the user's "PA Performance S07APX00340" screen)

- **Title bar**: full width, blue `#1f78a8`, white bold text:
  `<Screen name> <APEX page code> | <Employee code> | <Employee name>`. Use `S07APX0XXXX`
  until the page code is assigned.
- **No left menu.** The screen is full width on a light grey body with a white card.
- **Tabs** under the header: the active tab is filled blue `#1f78a8` with white text,
  inactive tabs are bold dark text on light grey (e.g. Evaluation Criteria |
  Recommendation | Approval History | Finalization).
- **Region header**: slate blue-grey bar `#57768f`, white bold title (e.g. "Behavioral
  Assessment", "Employee Information").
- **Grid**: thin light-grey cell borders, bold column headers, two-row header when
  needed (e.g. Current Year / Previous Year Rating). The current-value column has a light
  green background `#eaf6ec`, the selected row is light blue `#e3edf7`, and a missing
  mandatory cell is pink `#f8c6c9`. Columns: Parameter | Description | Rating |
  Remarks (if any).
- **Rating Scale panel** on the right of rating grids: orange header `#f9ad57`, rows
  Very Low 1, Low 2, Medium 3, High 4, Very High 5.
- **Score summary bar** under the grid: light green `#eefaf2` with a green border,
  right-aligned: Total Score, Obtained Score, Performance % (values bold green).
- **Buttons** bottom-right, with icons: Preview (light blue `#7cc4f5`), Save (green
  `#1e8a3c`), Exit (red `#c8102e`). Workflow screens add Submit (blue `#1f78a8`) and
  Return (orange `#ef8a17`). The Approve and Finalize buttons are green.
- Font: Segoe UI, about 12 px; compact, dense business layout.

## Rules

- Schema first (`sdlc-conventions.md` §7). Every object named in the CR must exist in the
  schema or be marked NEW (proposed).
- Embed images in Word: render the Markdown with `scripts/render_docx.py`, then replace
  each `![caption](path)` paragraph with the picture at page width (python-docx).
- Files: `docs/<CR-ID>/<CR-ID>_CR_v<version>.md/.docx`, `<CR-ID>_Workflow.svg/.png`,
  `prototypes/NN_<screen>.png`.
