# SKMCH Change Request (CR) document: client template

Use this layout whenever the user asks for a **CR**, or for requirements "in my CR
template". It is the client-facing document. The detailed SRS (`srs-structure.md`) stays
the internal source of IDs, acceptance criteria and impact analysis. The CR may merge the
SRS detail into this layout when the user asks for one combined document.

Status: agreed with the user on 09-Oct-2026 (reference CR: `docs/CR-2026-XXX-PEV/`).
**PENDING from the user:** (a) which sections to shorten into bullets, (b) which
sections to exclude from the CR, and (c) their GUI template for prototypes. Apply those
rules here as soon as they are supplied. Until then, follow the layout below.

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
   - **Prototype (GUI)**: real screen mock-ups as images, never ASCII. Style: Oracle APEX
     (or the user's GUI template once supplied): header bar, left menu, regions, form
     items, report grids, status badges and action buttons. Use synthetic data only
     (`EMP-TEST-0001` etc.) and mark form content as indicative until the business supplies
     it. Generator to adapt: `scripts/example_gui_prototypes.py` (HTML → PNG). Keep the
     HTML sources in `docs/<CR-ID>/prototypes/src/`.
   - (Merged version only) Detailed FR-NNN with Given/When/Then acceptance criteria.
4. **System Interfaces**
   - **Hardware Interfaces**: devices, servers, mail server, biometric/RFID, printers
     ("no new hardware" is a valid answer).
   - **Software Interfaces**: table of the real schema objects/systems used (verified
     against the DDL), direction, data exchanged and purpose.
5. **Open Points**: blocking questions for the client.

## Rules

- Schema first (`sdlc-conventions.md` §7). Every object named in the CR must exist in the
  schema or be marked NEW (proposed).
- Embed images in Word: render the Markdown with `scripts/render_docx.py`, then replace
  each `![caption](path)` paragraph with the picture at page width (python-docx).
- Files: `docs/<CR-ID>/<CR-ID>_CR_v<version>.md/.docx`, `<CR-ID>_Workflow.svg/.png`,
  `prototypes/NN_<screen>.png`.
