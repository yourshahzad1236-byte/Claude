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
<!-- Source of schema info, date/version of export, or "None – PROVISIONAL". -->

# 2. Solution approach
## 2.1 Approach
## 2.2 Alternatives considered
| Option | Pros | Cons | Decision |
## 2.3 Key design decisions
| ID | Decision | Rationale | Related FR/NFR |

# 3. Requirements-to-design traceability
| Requirement | Design elements (DS-NN) | Notes |
<!-- EVERY FR and NFR from the SRS, no exceptions. -->

# 4. Current-state impact analysis
## 4.1 Existing objects involved
| Object | Type | Current role | Change (Modify / Read-only / None) | Evidence |
## 4.2 Dependency analysis
| Changed object | Dependent object | Dependent type | Impact | Action (Modify / Recompile / Retest) |
## 4.3 Reuse
| Existing unit | What it does | How reused / extended |

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
