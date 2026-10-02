# Technical design document (RFC) structure

The cover, version history and approvals come from the Word template.

~~~markdown
# 1. Overview
## 1.1 Summary
<!-- 3–6 sentences: what is being built and the chosen approach. -->
## 1.2 Source requirements
| Document | Version | Status |
<!-- If SRS is not APPROVED, add: > WARNING: based on unapproved SRS; design may change. -->
## 1.3 Scope of this design / out of scope
## 1.4 Schema context used
<!-- One line; details are in section 2.1. -->

<!-- highlight -->
# 2. Impact Analysis
<!-- Done BEFORE the design, from the schema files (conventions §7–8). Keep the highlight markers so the section renders shaded and boxed in Word. If no schema was available, start with: > WARNING: PROVISIONAL – impact analysis done without schema files. -->
## 2.1 Schema source used
| Source | Schemas covered | Snapshot / export date | Notes |
<!-- e.g. "D:\SKM_SCHEMA (HRD, PAYROLL, REGISTRATION, DEFINITIONS, RFID, HIS, TRAINING)", attached files, or "None – PROVISIONAL". -->
## 2.2 Impact summary
| Measure | Count |
|---|---|
| Objects to create (NEW) | n |
| Objects to modify | n |
| Dependent objects to recompile | n |
| Dependent objects / screens to retest | n |
| Schemas touched | HRD, … |
| High-risk impact items | n |
| Objects referenced by the SRS but NOT found in schema | n |
**Overall impact rating:** High / Medium / Low, with a one-line reason.
## 2.3 Existing objects impacted
| IMP | Object (OWNER.NAME) | Type | Current role | Change (Modify / Read-only / None) | Risk (H/M/L) | Related FR | Evidence (schema file / index entry) |
## 2.4 Column-level impact
| IMP | OWNER.TABLE.COLUMN | Current definition | Proposed change | Code that reads / writes it | Data migration needed |
## 2.5 Dependency (where-used) analysis
| Changed object | Dependent object | Dependent type (package / view / trigger / APEX page / job / synonym / other schema) | Impact | Action (Modify / Recompile / Retest) |
## 2.6 Cross-schema and integration impact
| Schema / interface | Objects involved | Impact | Action |
<!-- e.g. PAYROLL reads HRD employee tables; DEFINITIONS synonyms; RFID attendance feeds. -->
## 2.7 Reuse of existing code
| Existing unit | What it does | How reused / extended |
## 2.8 Not found in schema
| Name used in SRS / MoM | Searched where | Result | Action (Q-NN / NEW) |
## 2.9 Impact risks
| IMP | Risk | Likelihood | Impact | Mitigation | Patient-safety relevant (Y/N) |
<!-- /highlight -->

# 3. Solution approach
## 3.1 Approach
## 3.2 Alternatives considered
| Option | Pros | Cons | Decision |
## 3.3 Key design decisions
| ID | Decision | Rationale | Related FR/NFR |

# 4. Requirements-to-design traceability
| Requirement | Design elements (DS-NN) | Notes |
<!-- EVERY FR and NFR from the SRS, no exceptions. -->

# 5. Data design
## 5.1 Entity changes overview
<!-- Short description of new and changed entities and relationships (text or table). -->
## 5.2 New tables
### DS-NN HRD.<TABLE_NAME> (satisfies FR-…)
Purpose: …  Estimated volume: … rows/year.
| Column | Data type | Null | Default | Constraint | Description |
## 5.3 Modified tables
### DS-NN HRD.<TABLE_NAME>
| Column | Change (Add / Modify / Drop) | Old definition | New definition | Backfill rule |
## 5.4 Constraints, indexes, sequences, triggers, views
| DS | Object name | Type | Definition | Reason |
## 5.5 Grants, synonyms, VPD / security policies
## 5.6 Data migration / backfill
<!-- Steps, idempotency guard, volume, estimated run time, validation queries. -->

# 6. Application logic design
## 6.x DS-NN HRD.PKG_<MODULE>.<P_/F_NAME> (satisfies FR-…) [NEW / MODIFIED]
**Signature:**
```sql
PROCEDURE P_… (P_… IN HRD_…_MST.…%TYPE, P_… OUT …);
```
**Logic:**
1. Validate …, raise `-20xxx` "message" when …
2. …
**Transaction:** commits here / caller commits.
**Exceptions:** | Code | Condition | Message |
**Called from:** APEX page …, job …

# 7. APEX design
## 7.x DS-NN App <id> Page <no> <name> [NEW / MODIFIED]
| Component | Static ID / name | Type | Source / behaviour | Validation | Authorization |
<!-- Regions REG_, items P<no>_, buttons BTN_, DAs DA_, LOVs LOV_ -->

# 8. Integrations, jobs and notifications
| DS | Name | Type (job / interface / email / SMS) | Trigger / schedule | Logic | Failure handling |

# 9. Security and audit design
<!-- Role → authorization scheme mapping, data masking, audit columns / history tables, segregation of duties. -->

# 10. Non-functional design
| NFR | Design measure (DS-NN) | How it will be verified |

# 11. Change inventory
| # | File / object | Path in repo | Change type (New / Modify / Recompile) | DS | Owner |
<!-- Every object from sections 5–8 plus dependents to recompile. -->

# 12. Deployment plan
## 12.1 Script execution order
| Step | Script | Content | Downtime needed |
## 12.2 Post-deployment verification
## 12.3 Rollback plan
<!-- Reverse order. Data-safety notes (what is lost on rollback). -->

# 13. Testing notes for developers and QA
<!-- Unit-test points per program unit, edge cases, performance test hints. Does not replace QA test cases. -->

# 14. Risks, assumptions and open questions
## 14.1 Risks
| Risk | Impact | Mitigation |
## 14.2 Assumptions
| ID | Assumption |
## 14.3 Open questions
| ID | Question | Owner | Blocking |

# Appendix A. Full DDL script
# Appendix B. Rollback script
~~~
