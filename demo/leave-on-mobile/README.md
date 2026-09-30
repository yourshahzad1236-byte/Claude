# Demo: "Leave on mobile" (synthetic)

An end-to-end run of the skills on made-up meeting notes and a small mock HRD schema
(2 tables, 1 package, 1 view, 1 trigger, APEX app 200). No real SKMCH data is used.

| Step | Prompt given to Claude | Skill that triggered | Output |
|---|---|---|---|
| 1 | "The minutes of meeting are in mom.txt. Please create the SRS." | skmch-ba-srs | `CR-YYYY-XXX_SRS_v0.1.docx` |
| 2 | "Write test cases for the SRS …" | skmch-qa-testcases | `CR-YYYY-XXX_TestCases_v0.1.xlsx` (80 TCs, 100% FR/NFR traced) |
| 3 | "… Create the technical design document / RFC." | skmch-sa-design-rfc | `CR-YYYY-XXX_Design_v0.1.docx` + DDL, migration, views and rollback scripts |

Things to look for:
- The HR Manager and the Director of Nursing disagreed about who approves. The SRS
  records both views as an open question and doesn't pick one. The design makes the
  approver rule configurable.
- Impact analysis cites the schema index as evidence, with a confidence level for each item.
- The skills found issues nobody raised in the meeting: the balance function returns a
  constant, a sequence is missing from the snapshot, and the employee ID can be tampered
  with on page 20.
- Everything is DRAFT, and no AI-produced document is marked approved.

The CR number is `CR-YYYY-XXX` because the notes didn't give one. The skill asks for it.
