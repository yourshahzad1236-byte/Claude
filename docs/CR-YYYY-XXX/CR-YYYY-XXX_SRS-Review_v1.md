# 1. Review summary
| Item | Value |
|---|---|
| SRS reviewed | CR-YYYY-XXX_SRS_v0.1.docx, version 0.1 (DRAFT) |
| MoM available for coverage check | Yes (4 agenda items, re-derived independently into 19 points) |
| Schema context used | None: the HRD schema is not indexed yet, so no database impact item can be verified |
| Recommendation | **Return to BA / client** |
| Findings | Blocker 3 · Major 7 · Minor 4 · Observation 3 |

The SRS is well structured and fully traced: all 19 meeting points are mapped, and every FR has a negative acceptance criterion. It is not ready for approval, because three core business rules decide whether the calculation works at all, and none of them is settled.
- With a Monday–Saturday week, a regular bus user's deductions exceed the 24,000 PKR allowance every month.
- The first payroll month is a partial month for every employee.
- The misuse control depends on eligibility rules that don't exist yet.

These need answers from Mr. Ubaid, HR and Finance before design starts. That is urgent given the end-of-October build date.

# 2. Findings
| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
|---|---|---|---|---|---|---|
| RV-01 | Blocker | RULE-01, FR-010, Q-07 | The allowance is "24,000 PKR for a 24-day month", but November 2026 has 25 Monday–Saturday days and December 2026 has 27. At 500 PKR a trip × 2 trips a day, a regular bus user is charged 25,000 (Nov) and 27,000 (Dec). The SRS treats deductions above the allowance as an edge case (FR-010 AC3); it will be the normal case | The payout rule is wrong for most bus users every month; either staff lose money or the system recovers from salary without anyone having agreed to it | Make Q-07 a Blocker. Ask Finance to choose: (a) cap the payout at 0; (b) scale the allowance to actual working days; or (c) set the per-trip cost as allowance ÷ (2 × working days). Record the decision as a new rule | Finance, Mr. Ubaid |
| RV-02 | Blocker | Q-03, FR-001, BR-04, FR-014 | Eligibility and whether bus use is mandatory are undefined. If staff may use their own transport, an employee who never swipes keeps 24,000 PKR in cash. That can't be told apart from misuse, so readers at both ends (M-09) don't address the concern raised in M-08 | BR-04 (Must) can't be met, and the misuse control has nothing to measure against | Keep Q-03 as blocking. Once it is answered, make FR-014 a Must if bus use is mandatory, or reword BR-04 if it is optional | Mr. Ubaid, HR, Management |
| RV-03 | Blocker | FR-003, FR-006, Q-02 | FR-003 says each swipe records "direction (boarding or disembarking)", but there is one terminal per location. The KDC terminal handles morning boarding and evening disembarking, so it can't know the direction by itself. The MoM also doesn't say whether the deduction is per swipe or per boarding/disembarking pair | Trip counts, and so deductions, could be doubled or halved | Add Q-15: is direction taken from separate boarding and disembarking readers, or worked out from the order of an employee's swipes that day? Make Q-02 answer "per trip or per swipe" explicitly | Mr. Ubaid, IS |
| RV-04 | Major | Q-14, FR-002 AC3 | The hospital opens in the first week of November, so the first payroll month is partial for everyone. Q-14 is marked "not blocking", yet FR-002 AC3 blocks the calculation until a proration rule exists | The first payroll run would stop for all staff | Mark Q-04 and Q-14 as blocking and get a proration rule before the November payroll cut-off | Finance, HR |
| RV-05 | Major | Missing (FR-007, FR-008) | There is no requirement for a fuel price entered after it takes effect (for example, effective 16th, entered 18th). Trips on the 16th–17th have already been charged at the old price and notified to employees | Deductions shown to employees would change silently, or stay wrong | Add Q-16: recalculate the open month's trips on late entry and re-notify, or apply prices only from the date they are entered? Then add the FR | Finance |
| RV-06 | Major | Scope, NFR-AVL | The SRS doesn't address 24×7 hospital staff: night shifts, 12-hour rotas, on-call call-outs. Do buses run for every shift? If not, those staff can't use the bus. The allowance rule for them is undefined, and FR-014 would flag them as non-swipers | Unfair deductions or false misuse flags for clinical staff; the IMP-06 shift-cover risk is understated | Add Q-17: which shifts does the bus serve, and what is the allowance rule for staff on shifts without a bus? | Mr. Ubaid, Nursing, HR |
| RV-07 | Major | FR-014 priority vs BR-04 | BR-04 (prevent and detect non-swiping) is a Must, but FR-014, the only detection requirement, is "Should" and "inferred" | The Must goal has no Must requirement behind it | The SA should decide: raise FR-014 to Must, or accept the risk and record it | Solution Architect |
| RV-08 | Major | FR-009, M-07 | The MoM says HR/Finance get a frontend "for deduction formulas". FR-009 turns this into parameters of a fixed formula. Finance may expect to edit a free formula expression | The wrong build choice leads to rework after the Finance alignment (M-18) | Confirm with Finance, as part of Q-05, that a parameterised formula is acceptable. Record it as a constraint | Finance |
| RV-09 | Major | FR-018, Q-08, §7.5 | The payroll hand-off has no cut-off date, reversal process or correction rule for adjustments approved after the register is sent. FR-013 AC3 says they carry forward, but FR-018 doesn't say how | Payroll disputes after every month-end | Add acceptance criteria to FR-018 for late adjustments (carried forward as a next-month credit/debit, shown separately on the register) | Finance, Payroll |
| RV-10 | Major | Impact analysis §8.2–8.3 | Every existing-system item (card system, attendance, payroll, employee master, dashboard) is PROVISIONAL with no named object. The design can't start without them | The design is blocked, or it guesses | Before design: index the HRD schema, and have IS name the card/attendance system and payroll tables (Q-09) | IS |
| RV-11 | Minor | FR-006 AC2 | "Within 2 minutes" is a number no one in the meeting gave | It looks like an agreed rule when it is only proposed | Label it "proposed default 2 minutes, configurable" | BA |
| RV-12 | Minor | §7.3 access matrix vs NFR-SEC-02 | Maker-checker needs two different users to enter and activate a price. The matrix gives Finance both roles but doesn't say they must be different people | Weak segregation of duties | Add to NFR-SEC-02: "the activator must be a different user from the maker" | BA |
| RV-13 | Minor | Q-01, §1.6 | The meeting date and attendee list aren't recorded. HR and Finance attendance is "to be confirmed" | Weak audit of where the requirements came from | Record the date and attendees in §1.4/§1.6 | BA |
| RV-14 | Minor | §1.4 | Mr. Ubaid's department is "to be confirmed" | The business owner and final approver are unclear | Name the business owner who signs the SRS | BA |
| RV-15 | Observation | IMP-20 | `HRD_FUEL_PRICE_HIS` uses the HIS (history) suffix, but it is an effective-dated reference table that is actively read. MST may fit the HRD standards better | Naming consistency | Settle the name at design time | Solution Architect |
| RV-16 | Observation | NFR-DAT-01 | The retention period is left to "Finance policy". Swipe data is employee location and time data | Privacy and storage planning | Confirm retention with HR/Finance, and whether swipe details are purged after payroll audit | HR, Finance |
| RV-17 | Observation | §8.4 | The schedule risk mitigation (phased go-live) is a sound proposal, but nobody has agreed it | It could be read as decided | Put it to Mr. Ubaid and management at the layout approval (M-19) | Mr. Shahzad |

# 3. MoM coverage
| M-ID | Statement | Covered by | Status |
|---|---|---|---|
| M-01 | Operational flow presented by Mr. Ubaid | §1.2 | Covered |
| M-02 | 24,000 PKR allowance for a 24-day month | FR-001, FR-002, RULE-01 | Covered (see RV-01) |
| M-03 | 500 PKR per trip (example) | FR-007, RULE-02 | Covered |
| M-04 | Swipe when boarding or disembarking | FR-003, FR-006 | Partially (see RV-03) |
| M-05 | Deduction based on current fuel rates | FR-007, FR-008 | Partially (see RV-05) |
| M-06 | Unused portion paid with salary | FR-010, FR-018 | Partially (see RV-01, RV-09) |
| M-07 | Frontend for HR/Finance for formulas and fuel prices | FR-008, FR-009 | Partially (see RV-08) |
| M-08 | Concern: avoiding swipes to keep cash | BR-04, FR-014 | Partially (see RV-02, RV-07) |
| M-09 | Readers at KDC and the hospital | FR-005 | Covered |
| M-10 | Manual adjustment portal for honest mistakes | FR-011, FR-013 | Covered |
| M-11 | Approval by supervisors or transport coordinator | FR-012 | Covered (Q-11 open) |
| M-12 | RFID via the existing employee ID card | FR-004, NFR-INT-01 | Covered |
| M-13 | Dashboard notification on every swipe | FR-015 | Covered |
| M-14 | Transparency and transaction trail for HR/Finance | FR-016, FR-017 | Covered |
| M-15 | Operational by the first week of November | §9.2 | Covered (see RV-04) |
| M-16 | Testable build by end of October | §9.2, §8.4 | Covered |
| M-17 | System design sketch | §9.2 | Covered |
| M-18 | Align formula with Finance | FR-009, Q-05 | Covered |
| M-19 | Management approval of layout before development | §9.2 | Covered |

# 4. Impact analysis verification
## 4.1 Confirmed items
| IMP-ID | Object | Verified against | Result |
|---|---|---|---|
| None | None | No schema snapshot available | Nothing can be confirmed |

## 4.2 Missed dependencies
| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
|---|---|---|---|---|---|
| Final settlement / exit process | Payroll process | Transport payout for leavers | Domain knowledge; not in the MoM | FR-010, Q-04 | Add an impact item: the transport balance is included in final settlement |
| Shift roster / duty schedule | Application | Shift times per employee | Needed for RV-06 and FR-014 | FR-014 | Add as a read-only dependency if a roster system exists |
| Card replacement process | Operational process | Card status | Lost cards cause missed swipes | FR-004, FR-011 | Add a business impact item: link card-replacement delays to the adjustment policy |

## 4.3 Incorrect or unverifiable items
| IMP-ID | Object | Problem | Correction |
|---|---|---|---|
| IMP-08, IMP-09, IMP-10, IMP-11, IMP-15, IMP-16 | Existing card, attendance, payroll, dashboard and employee objects | Not named and not verifiable | Name them after the schema is indexed and IS answers Q-09 |
| IMP-17 to IMP-23 | Proposed new tables | These follow the HRD standards (MST/TRN/HIS suffixes), but duplicates can't be ruled out without the schema | Check for any existing transport or allowance tables at design |

# 5. NFR coverage
| Category | Present in SRS | Adequate | Comment |
|---|---|---|---|
| SEC | Yes | Mostly | Add a maker ≠ checker rule (RV-12) |
| AUD | Yes | Yes | Swipes never deleted, only reversed. Good |
| PERF | Yes | Yes | Targets are proposed. Confirm the 1-second terminal response with the vendor |
| AVL | Yes | Yes | Offline buffering covers the KDC network risk |
| DAT | Yes | Partly | Retention period open (RV-16) |
| USA | Yes | Yes | Mobile-friendly adjustment form |
| CMP | Yes | Partly | Tax treatment open (Q-08) |
| INT | Yes | Partly | Card system not identified (Q-09) |
| OPS | Yes | Yes | Terminal health alerts |

# 6. Patient-safety and compliance notes
- **Staff arrival:** a transport scheme that fails, or is slow at boarding, can affect staff arriving for clinical shifts at a newly opened hospital. RV-06 (shift coverage) and NFR-PERF-02 (1-second terminal response) should be treated as go-live criteria.
- **Payroll deductions:** recovering money from salary (RV-01 option) usually needs employee consent or a policy basis. HR and Finance should confirm the policy before the rule is built.
- **Privacy:** swipe records show employee movements. Access is appropriately restricted (NFR-SEC-01), but retention needs a decision (RV-16).

# 7. Resolution log
| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
|---|---|---|---|
| RV-01 |  |  |  |
| RV-02 |  |  |  |
| RV-03 |  |  |  |
| RV-04 |  |  |  |
| RV-05 |  |  |  |
| RV-06 |  |  |  |
| RV-07 |  |  |  |
| RV-08 |  |  |  |
| RV-09 |  |  |  |
| RV-10 |  |  |  |
| RV-11 |  |  |  |
| RV-12 |  |  |  |
| RV-13 |  |  |  |
| RV-14 |  |  |  |
| RV-15 |  |  |  |
| RV-16 |  |  |  |
| RV-17 |  |  |  |
