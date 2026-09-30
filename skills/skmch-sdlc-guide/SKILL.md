---
name: skmch-sdlc-guide
description: Explains and navigates the SKMCH software development lifecycle (MoM → SRS → SA review → design doc/RFC → development → QA test cases and execution → system documentation). Also checks an existing set of CR documents for completeness and end-to-end traceability. Use when someone asks what the SDLC process is, what the next step or document is, who approves what, which Claude skill or template to use, what state a CR is in, or whether the documents for a CR are consistent and traceable from FRs through design, code, test cases and system documentation. Do NOT use to create any single SDLC document; the stage-specific SKMCH skills do that.
---

# SKMCH SDLC guide and traceability audit

Read `references/sdlc-conventions.md`. It is the authoritative description of the flow,
IDs, gates and rules.

## 1. Answering process questions
Answer from the conventions: stage, owner, input, output, the skill that produces it,
and the approval gate. Keep it short. Useful routing table:

| The user has… | …and wants | Next skill |
|---|---|---|
| Meeting notes / MoM | SRS | `skmch-ba-srs` |
| SRS (draft) | Review before approval | `skmch-sa-srs-review` |
| Approved SRS | Design / RFC | `skmch-sa-design-rfc` |
| Approved SRS | Test cases | `skmch-qa-testcases` (can run in parallel with development) |
| Approved design | Code | `skmch-dev-implement` |
| Test cases + build | Scripts, results, defects, sign-off report | `skmch-qa-execute` |
| Tested release | System documentation | `skmch-sysdoc-update` |

If the user has already given the input the next step needs, offer to do it right away.

## 2. CR status and traceability audit
When given a set of CR documents (any subset of MoM, SRS, review, design, code, test
cases, execution report, system-doc update):
1. Identify each document, its version and its status. Flag any AI-produced document
   marked APPROVED without a named approver.
2. Determine the current stage and the next gate.
3. Run traceability checks with `scripts/check_trace.py`:
   - SRS → Design: `--ids FR,NFR` (every requirement designed)
   - SRS → Test cases: `--ids FR,NFR` (every requirement tested)
   - Design → Code: `--ids DS` (every design element implemented)
   - SRS → System doc: `--ids FR`
4. Check version alignment: design cites the approved SRS version, test cases cite the same
   SRS version, the execution report covers the latest TC version.
5. Report as a short table: Check | Result | Gaps | Action/owner. End with "Ready for
   <next gate>: Yes/No, because …".

## Reference files
- `references/sdlc-conventions.md`
- `scripts/check_trace.py`
