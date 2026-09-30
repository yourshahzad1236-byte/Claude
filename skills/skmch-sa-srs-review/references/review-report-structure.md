# SRS review report structure

```markdown
# 1. Review summary
| Item | Value |
|---|---|
| SRS reviewed | <file name>, version <x> |
| MoM available for coverage check | Yes / No |
| Schema context used | <source> / None (impact verification not possible) |
| Recommendation | Ready for SA approval / Approve after minor fixes / Revise and re-review / Return to BA / client |
| Findings | Blocker n · Major n · Minor n · Observation n |

<One short paragraph: overall quality and the main risks.>

# 2. Findings
| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
<!-- Order: Blocker → Major → Minor → Observation. Quote the problematic text in "Issue". -->

# 3. MoM coverage
| M-ID | Statement | Covered by | Status |
<!-- Status: Covered / Partially / Missing / Out of scope. Omit the section if there is no MoM. -->

# 4. Impact analysis verification
## 4.1 Confirmed items
| IMP-ID | Object | Verified against | Result |
## 4.2 Missed dependencies
| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
## 4.3 Incorrect or unverifiable items
| IMP-ID | Object | Problem | Correction |

# 5. NFR coverage
| Category | Present in SRS | Adequate | Comment |
<!-- SEC, AUD, PERF, AVL, DAT, USA, CMP, INT, OPS -->

# 6. Patient-safety and compliance notes

# 7. Resolution log
| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
<!-- Leave decisions blank for the SA unless running in Apply-comments mode. -->
```
