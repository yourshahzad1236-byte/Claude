# Samples: upload real SKMCH documents here

These samples teach each skill your hospital's actual format, depth and vocabulary.
The maintainers curate them into the skills (`skills/<skill>/references/examples/`
and `templates/`), then re-package the skills.

## How to upload
On GitHub: open the folder → **Add file → Upload files** → drag the files in → commit.
Limit: 25 MB per file via the web. Zip bigger sets.

## Before uploading: mask sensitive data
This repository is on GitHub. Remove or replace **patient identifiers** (MR number,
names, CNIC, phone, diagnosis), employee personal data, passwords, connection strings
and server names. Replace them with values like `MRN-TEST-0001` and `EMP-TEST-001`.

## What goes where

| Folder | Put here | Used by skill |
|---|---|---|
| `01-mom/` | 2–3 real minutes of meeting, as they are (docx, txt, email, photo of notes) | skmch-ba-srs |
| `02-srs/` | The SRS written from those same MoMs, plus the **blank SRS template** (name it `TEMPLATE_SRS.docx`) | skmch-ba-srs, skmch-sa-srs-review |
| `03-srs-review/` | SA review comments or a marked-up SRS | skmch-sa-srs-review |
| `04-design-rfc/` | Design doc / RFC for the same feature, plus `TEMPLATE_Design.docx` | skmch-sa-design-rfc |
| `05-code/` | The resulting DDL, package specs/bodies, APEX export (or representative files) | skmch-dev-implement |
| `06-test-cases/` | Test case sheet, plus `TEMPLATE_TestCases.xlsx` | skmch-qa-testcases |
| `07-test-results/` | Execution / defect sheet, plus template if you have one | skmch-qa-execute |
| `08-system-doc/` | The system-document section that was updated, plus template | skmch-sysdoc-update |

**Best:** one or two complete end-to-end chains, meaning the *same* feature through every
folder. Prefix the files with the same CR number (e.g. `CR-2025-031_MoM.docx`,
`CR-2025-031_SRS.docx` …) so the chain is obvious.
