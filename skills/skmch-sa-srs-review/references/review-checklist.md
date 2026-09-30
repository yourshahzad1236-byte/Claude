# SRS review checklist

## A. Structure
- [ ] Sections 1–10 and Appendices A–B present (or "Not applicable: reason").
- [ ] Cover shows CR ID, version, status (DRAFT/IN REVIEW), author, source MoM.
- [ ] IDs unique and well-formed (FR-NNN, NFR-CAT-NN, BR-NN, RULE-NN, IMP-NN, Q-NN, A-NN).
- [ ] Version history updated. No renumbering relative to the previous version.

## B. Requirement quality (each FR/NFR)
- [ ] Atomic: one behaviour.
- [ ] Unambiguous: no weasel words (fast, user-friendly, etc., TBD, as needed…).
- [ ] Testable: ACs state observable results. At least one negative AC.
- [ ] Complete: actor, trigger, data, result, error handling.
- [ ] Consistent: no conflicts with other FRs, rules or NFRs.
- [ ] Feasible within the current platform (Oracle/APEX) and constraints.
- [ ] Traceable: source M-NN. Priority set.
- [ ] Solution-neutral, unless a real business constraint.
- [ ] NFRs measurable (number + unit + condition).

## C. Domain and architecture
- [ ] Every workflow has: submit, approve, reject, return for correction, cancel/withdraw,
      edit after submission, and delegation or escalation (approver absent or on leave).
- [ ] Back-dated / future-dated entries, cut-offs (month-end payroll, fiscal year),
      time zones and shift boundaries (night shift crossing midnight).
- [ ] Concurrency: two users on the same record. Double submission.
- [ ] Bulk operations and upload/import. Volume at peak.
- [ ] Status model defined (states + allowed transitions).
- [ ] Deletion policy: soft delete / deactivate vs hard delete. History and audit.
- [ ] Roles: every function has an owner role. Segregation of duties (requester ≠ approver).
- [ ] Notifications: who, when, channel, content. Failure handling.
- [ ] Reporting impact: existing reports/extracts still correct? New reports defined?
- [ ] Integrations: payroll, attendance/biometric, HIS, ERP/finance, BI. Failure/retry behaviour.
- [ ] Patient safety: any path that could harm patient care, identity or billing has
      explicit validation and a negative AC.
- [ ] Privacy: personal data minimised, masked where appropriate, access-controlled, audited.
- [ ] Availability: 24×7 areas identified. Deployment downtime expectation stated.
- [ ] Migration: existing data needs conversion/backfill? Parallel run? Cut-over?

## D. Impact analysis verification
- [ ] Every impacted object named in the SRS exists in the schema context (or is marked NEW/PROVISIONAL).
- [ ] Column names and types used in the SRS match the schema.
- [ ] Dependencies searched: for every modified table/column, list views, triggers,
      packages, APEX pages, reports and jobs that reference it. Anything the SRS missed = finding.
- [ ] No duplicate of an existing object or function.
- [ ] Data volume and growth of new tables estimated.
- [ ] Proposed new object names follow `oracle-plsql-apex-hrd-standards`.
