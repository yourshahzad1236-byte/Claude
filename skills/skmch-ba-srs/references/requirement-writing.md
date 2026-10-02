# Writing SKMCH requirements

## 1. Functional requirements
- One behaviour per FR. If the sentence has "and" or "or" joining two behaviours, split it.
- Form: "The system shall <verb> <object> <condition/constraint>."
- Actor-explicit where it matters: "The system shall allow a Nursing Supervisor to …".
- What, not how: no table names, package names or UI widget choices unless the business
  imposed them (then they are constraints and are marked as such).
- Every FR has at least 2 acceptance criteria, one of them negative or validation.
- Every FR cites its MoM sources (`M-NN`). An FR with no source is either an inferred
  necessity (mark it `Inferred` and raise a `Q-NN`) or it should not exist.

**Weak:** "Leave module should be improved and approvals should be fast."
**Strong:**
- FR-004: The system shall route a submitted leave request to the applicant's reporting
  manager, as defined in the employee's current posting.
  - AC1: Given an employee with an active posting and reporting manager, when they submit
    a leave request, then the request appears in that manager's pending approvals.
  - AC2 (negative): Given an employee with no reporting manager on record, when they
    submit, then submission is blocked with the message "Reporting manager not defined.
    Contact HR" and no request is created.
- NFR-PERF-01: The pending-approvals list shall load within 3 seconds for up to 500
  pending requests (95th percentile, hospital LAN).

## 2. Ambiguous words: replace with a measure or raise a Q-NN
fast, quick, efficient, user-friendly, easy, simple, flexible, robust, secure (on its
own), appropriate, adequate, as needed, etc., and so on, TBD, normally, usually, some,
many, most, real-time (without latency), automatically (without a trigger), all users,
should (in an FR, use "shall"), support (unspecified), handle.

## 3. Priority (MoSCoW)
- **Must:** stated as mandatory in the meeting, or needed for legal/safety/compliance.
- **Should:** important but has a workaround.
- **Could:** nice to have.
- **Won't (this release):** agreed as deferred. Also list it in Out of scope.
When the meeting didn't say, default to Should and flag it in assumptions.

## 4. Healthcare NFR checklist: consider EVERY category in EVERY SRS
| Category | Code | Ask yourself |
|---|---|---|
| Security & access | SEC | Which roles see or modify this data? Is it patient or employee personal data? Is masking needed? Does it follow existing APEX authorization schemes? |
| Audit | AUD | Must we record who created, changed, approved or viewed it, and when? Does it need history (HIS) tables? |
| Performance | PERF | How many records and users? Peak times (OPD morning, month-end payroll)? Response-time target? |
| Availability | AVL | Is it used 24×7 (wards, ER)? Is downtime allowed for deployment? What happens if it is unavailable? |
| Data retention & quality | DAT | How long is data kept? Can it be deleted? Are there duplicate checks and mandatory fields? |
| Usability | USA | Who are the users (clinical staff under time pressure)? Language? Mobile/tablet use? |
| Compliance | CMP | Hospital policy, medical-records rules, labour/HR law, finance audit, accreditation (e.g. JCI) evidence? |
| Integration | INT | Other systems affected (HIS, LIS, RIS/PACS, pharmacy, billing, ERP, payroll, biometric attendance)? |
| Operations | OPS | Scheduled jobs, notifications (email/SMS), reports, backups, monitoring, support handover? |

## 5. Patient safety
If a requirement touches clinical orders, medication, results, patient identity, billing
of care or clinical staff rostering, add a note that says so. The architect and QA then
treat it as high-risk.

## 6. Quality gate (run before producing the document)
- [ ] Every M-NN is mapped (Appendix A has no blank "Mapped to").
- [ ] Every FR: atomic, "shall", ≥2 ACs incl. a negative, priority set, source cited.
- [ ] No ambiguous words from §2 remain without a measure or a Q-NN.
- [ ] Every NFR category in §4 was considered (included, or consciously "Not applicable: reason").
- [ ] Access matrix covers every role mentioned in the meeting.
- [ ] Impact tables: every object has Evidence + Confidence. Nothing is presented as
      existing without evidence. New objects follow HRD naming and are marked NEW (proposed).
- [ ] No real patient or employee identifiers anywhere. Examples are synthetic.
- [ ] Conflicting stakeholder statements became Q-NNs, not silent choices.
- [ ] Open questions state who must answer them and whether they block.
- [ ] SRS v1.3 acceptance criteria (Section 5) checked one by one: Clear (one
      interpretation, examples/decision tables/formulas instead of loose prose), Unique
      (no two FRs specify the same function), Traceable (every requirement cites M-NN,
      policy, standard or email), Complete (all sections filled or "Not applicable"/TBD
      with owner, every acronym in Section 7), Testable (≥1 acceptance criterion each),
      Implementable, Consistent (no conflict with each other or with earlier SRSs, rules,
      policies). Tick the Author column only for the ones met.
- [ ] Section 2 has exactly one estimation band with its basis; Section 6 has sanity test
      cases for every Must FR; Sections 1–7 keep the template order and headings.
