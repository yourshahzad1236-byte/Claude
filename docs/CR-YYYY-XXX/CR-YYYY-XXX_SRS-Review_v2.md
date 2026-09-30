# 1. Review summary
| Item | Value |
|---|---|
| SRS reviewed | CR-YYYY-XXX_SRS_v0.2 (DRAFT), Word file and the shared doc (identical content) |
| Review type | Re-review. The previous review was review v1 of SRS v0.1 |
| MoM available for coverage check | Yes: all 19 meeting points are still mapped |
| Schema context used | None: the HRD schema is still not indexed |
| Recommendation | **Return to BA / client** |
| Open findings | Blocker 3 · Major 4 · Minor 5 · Observation 4 |
| Resolved since review v1 | 9 of 17 (RV-04, RV-05, RV-06, RV-08, RV-09, RV-11, RV-12, RV-16, RV-17) |

v0.2 is a clear improvement. Every change from review v1 is traceable, no IDs were renumbered, and the key risks are now explicit open questions instead of hidden assumptions. The recommendation doesn't change, because the three Blockers are business decisions that only Mr. Ubaid, HR and Finance can make: the working-days rule, eligibility, and how direction is detected.

The re-review found 2 new Major gaps: staff whose shift has no bus would be flagged as misusers, and requests stall when the approver is absent. It also found 3 new Minor inconsistencies. The Majors can be fixed in the SRS now, without waiting for stakeholders.

**Timing.** Today is 30 September. The build is due at the end of October and 10 questions block design, so answers are needed in the first week of October to leave time for design, build and testing.

# 2. Findings
## 2.1 Open findings carried from review v1
| ID | Severity | Location | Status in v0.2 | What is still needed | Question for |
|---|---|---|---|---|---|
| RV-01 | Blocker | RULE-01, FR-010, Q-07 | Documented well (§1.2, Q-07 with options a/b/c) but not decided | Finance chooses option a, b or c. If a/b leaves deductions above the allowance, confirm the policy basis for salary recovery | Finance, Mr. Ubaid |
| RV-02 | Blocker | Q-03, FR-001, BR-04 | Unchanged | Decide eligibility, and whether bus use is mandatory. BR-04 and FR-014 depend on it | Mr. Ubaid, HR, Management |
| RV-03 | Blocker | FR-003, FR-006, Q-15, Q-02 | Documented (Q-15 added) but not decided | Decide separate boarding/disembarking readers vs swipe order, and per-trip vs per-swipe deduction. This also affects hardware procurement | Mr. Ubaid, IS |
| RV-07 | Major | FR-014 | Flagged for SA decision; still "Should" | SA decides: raise FR-014 to Must, or accept and record the risk | Solution Architect |
| RV-10 | Major | §8.2, §8.3 | Unchanged: all existing-system items PROVISIONAL | Index the HRD schema; IS names the card, attendance and payroll objects (Q-09) | IS |
| RV-13 | Minor | §1.4, §1.6, Q-01 | Unchanged | Meeting date and attendee list | BA |
| RV-14 | Minor | §1.4 | Unchanged | Name the business owner who signs the SRS | BA |
| RV-15 | Observation | IMP-20 | Deferred to design (as agreed) | Settle the `HRD_FUEL_PRICE_HIS` vs MST name at design | Solution Architect |

## 2.2 New findings in v0.2
| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
|---|---|---|---|---|---|---|
| RV-18 | Major | FR-014 acceptance criteria | FR-014 AC1 flags anyone "marked present by attendance on 10 days and has trips on only 2 of them". There is no criterion for staff whose shift has no bus service (Q-17), such as night shifts, on-call call-outs, or staff approved to use their own transport | Clinical staff on shifts with no bus would appear as misusers, and Q-12 raises disciplinary action or forced deduction. A false accusation is a serious HR risk | Add "AC3 (negative): Given an employee's attended day falls on a shift with no bus service (per Q-17), when the report runs, then that day is not counted as a missed trip." | Mr. Ubaid, HR |
| RV-19 | Major | FR-012 | FR-012 AC2 handles "no approver is defined" but not an approver who is on leave or doesn't act. Nothing is set for delegation, escalation or a time limit | Requests stall past payroll cut-off and employees are charged for trips they did take. This will recur every month | Add "AC3 (negative): Given the approver has not acted within N working days (N configurable, proposed 2) or is on approved leave, when that time passes, then the request escalates to the transport coordinator and both are notified." Confirm N with HR | HR, Mr. Ubaid |
| RV-20 | Minor | FR-010 AC3 | AC3 still says "the result follows Q-07 (cap at zero, or recover the excess from salary)". Q-07 now has three options (a/b/c) | The acceptance criterion contradicts the open question and may mislead QA | Replace with "the result follows the rule chosen in Q-07, and the case is listed for Finance review". If option (c) is chosen, FR-007 and FR-009 also change | BA |
| RV-21 | Minor | RULE-04 | RULE-04 says "the pairing rule and the handling of single swipes are to be confirmed" and cites Q-02 only, not the new Q-15 | The direction question is part of the trip rule | Add Q-15 to RULE-04's source column | BA |
| RV-22 | Minor | FR-012, FR-013 | If Q-11 routes a request to both the supervisor and the transport coordinator, nothing defines what happens when both act, or act differently | Double approval, or a conflicting approval and rejection | Once Q-11 is decided, and if both can act: add "the first decision closes the request; later actions are blocked with 'Already decided by <name>'" | BA |
| RV-23 | Observation | §8.1 | IMP-24 is listed between IMP-05 and IMP-06 | Readers may think numbers are missing | Keep the IDs, but move the IMP-24 row to the end of §8.1 | BA |
| RV-24 | Observation | FR-014, NFR-SEC-01 | Attendance data is reused to detect possible transport misuse | Staff should know how their data is used. It's also a fairness point if deductions or discipline follow | Add to IMP-05 that the transport policy tells staff that attendance and swipe data are compared | HR |
| RV-25 | Observation | NFR-SEC-02, Q-16 | Maker-checker means a new fuel price takes effect only once a second person activates it. If that happens late, the late-entry question (Q-16) arises every time prices change | Deductions at the old price, then disputes | Decide Q-16 together with the NFR-SEC-02 working pattern, for example a named backup checker in Finance | Finance |

# 3. MoM coverage
All 19 meeting points (M-01 to M-19) are still mapped in Appendix A. There are no regressions from v0.1. The points only partly covered are the same as in review v1, and each is waiting on a Blocker or Major above:
- M-04: RV-03
- M-06: RV-01
- M-08: RV-02, RV-07 and the new RV-18

# 4. Impact analysis verification
## 4.1 Confirmed items
| IMP-ID | Object | Verified against | Result |
|---|---|---|---|
| None | None | No schema snapshot available | Nothing can be confirmed |

## 4.2 Missed dependencies
| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
|---|---|---|---|---|---|
| Leave records | Application data | Approved leave per employee | RV-19 (approver on leave), Q-04 (proration for leave) | FR-002, FR-012 | Add a read-only impact item: the leave system, for proration and approver availability |

## 4.3 Incorrect or unverifiable items
| IMP-ID | Object | Problem | Correction |
|---|---|---|---|
| IMP-08 to IMP-11, IMP-15, IMP-16, IMP-25, IMP-26 | Existing systems and objects | Still unnamed and unverifiable | Name them after the schema is indexed and IS answers Q-09 |
| IMP-17 to IMP-23 | Proposed new tables | These follow HRD naming, but duplicates can't be ruled out | Check at design against the schema |

# 5. NFR coverage
| Category | Present in SRS | Adequate | Comment |
|---|---|---|---|
| SEC | Yes | Yes | Maker ≠ checker added in v0.2 |
| AUD | Yes | Yes | Unchanged |
| PERF | Yes | Yes | Targets proposed; confirm the terminal response time with the vendor |
| AVL | Yes | Yes | Offline buffering |
| DAT | Yes | Partly | Retention now tracked as Q-18 |
| USA | Yes | Yes | Unchanged |
| CMP | Yes | Partly | Tax treatment still open (Q-08) |
| INT | Yes | Partly | Card system still unidentified (Q-09) |
| OPS | Yes | Yes | Unchanged |

# 6. Patient-safety and compliance notes
- **False misuse flags (RV-18):** these hit clinical staff on night and on-call shifts hardest. Fix this before any disciplinary use of FR-014 is agreed (Q-12).
- **Salary recovery (RV-01, options a/b):** recovering money from salary needs a policy basis agreed by HR and Finance.
- **Transparency to staff (RV-24):** the policy should say that attendance and swipe data are compared.

# 7. Resolution log
| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
|---|---|---|---|
| RV-01 |  | Documented as Q-07 (blocking); decision pending |  |
| RV-02 |  | Pending Q-03 |  |
| RV-03 |  | Documented as Q-15 (blocking); decision pending |  |
| RV-04 | Applied by BA in v0.2 (SA to confirm) | Q-14 marked blocking | 0.2 |
| RV-05 | Applied by BA in v0.2 (SA to confirm) | Q-16 added | 0.2 |
| RV-06 | Applied by BA in v0.2 (SA to confirm) | Q-17 added (blocking) | 0.2 |
| RV-07 |  | Awaiting SA decision |  |
| RV-08 | Applied by BA in v0.2 (SA to confirm) | Q-05 extended | 0.2 |
| RV-09 | Applied by BA in v0.2 (SA to confirm) | FR-018 AC3 added | 0.2 |
| RV-10 |  | Awaiting schema |  |
| RV-11 | Applied by BA in v0.2 (SA to confirm) | Interval labelled as a proposal | 0.2 |
| RV-12 | Applied by BA in v0.2 (SA to confirm) | Maker ≠ checker | 0.2 |
| RV-13 |  | Pending |  |
| RV-14 |  | Pending |  |
| RV-15 |  | Deferred to design |  |
| RV-16 | Applied by BA in v0.2 (SA to confirm) | Q-18 added | 0.2 |
| RV-17 | Applied by BA in v0.2 (SA to confirm) | Labelled as a proposal | 0.2 |
| RV-18 |  | New |  |
| RV-19 |  | New |  |
| RV-20 |  | New |  |
| RV-21 |  | New |  |
| RV-22 |  | New |  |
| RV-23 |  | New |  |
| RV-24 |  | New |  |
| RV-25 |  | New |  |
