# SKMCH Change Request (CR) document: client template

Use this layout whenever the user asks for a **CR**, or for requirements "in my CR
template". It is the client-facing document. The detailed SRS (`srs-structure.md`) stays
the internal source of IDs, acceptance criteria and impact analysis. The CR may merge the
SRS detail into this layout when the user asks for one combined document.

Status: agreed with the user on 09-Oct-2026 (reference CR: `docs/CR-2026-XXX-PEV/`).
**PENDING from the user:** (a) which sections to shorten into bullets and (b) which
sections to exclude from the CR. Apply those rules here as soon as they are supplied.
Until then, follow the layout below. The GUI template was supplied on 09-Oct-2026 (see
"GUI template" below).

## Section layout (client template, in this order)

1. **Client Needs / Expectations**: what the client wants and why, the expected benefits,
   and how it works today (taken from the schema, e.g. existing queues and screens).
2. **Workflow**: a **graphical swimlane diagram** (PNG embedded, editable SVG beside it),
   never ASCII. Lanes per actor (System, requester/evaluator, approvers, HR or the owning
   department). Show decisions, return/correction paths, exception paths and a status tag
   at each step, plus a legend. After it, a short step table: actor, action, status.
   Generator to adapt: `scripts/example_workflow_diagram.py` (SVG → PNG with headless
   Chromium).
3. **Functional Requirements**: one block per client requirement:
   - **Requirement N: <title>**: short description and summary acceptance.
   - **Prototype (GUI)**: real screen mock-ups as images, never ASCII, always in the
     **SKMCH GUI template** below. Use synthetic data only (`EMP-TEST-0001` etc.); never
     copy real names or employee codes from screenshots the user shares. Mark form content
     as indicative until the business supplies it. Generator to adapt:
     `scripts/gui_prototypes_skmch_template.py` (HTML → PNG with headless Chromium). Keep
     the HTML sources in `docs/<CR-ID>/prototypes/src/`.
   - (Merged version only) Detailed FR-NNN with Given/When/Then acceptance criteria.
4. **System Interfaces**
   - **Hardware Interfaces**: devices, servers, mail server, biometric/RFID, printers
     ("no new hardware" is a valid answer).
   - **Software Interfaces**: table of the real schema objects/systems used (verified
     against the DDL), direction, data exchanged and purpose.
5. **Open Points**: blocking questions for the client.

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
