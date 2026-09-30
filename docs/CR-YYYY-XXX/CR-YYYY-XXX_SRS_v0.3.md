# 1. Introduction
## 1.1 Purpose
This SRS specifies the Karachi Transport Allowance System. Karachi staff receive a monthly transport allowance. Each bus trip recorded by an RFID card swipe is deducted from it, at a cost linked to the current fuel price, and the unused balance is paid with the monthly salary. The document is for the Solution Architect's review and approval, and is the basis for design, development and QA.

## 1.2 Background
The Karachi hospital opens in the first week of November. Staff will travel on hospital buses between the KDC pickup point and the hospital. Management wants the transport benefit given as a cash allowance that reflects actual bus use (M-01, M-02, M-15).

**How the numbers fit together.** 24,000 PKR ÷ 24 days = 1,000 PKR per day = 2 trips × 500 PKR. At the reference cost, an employee who takes the bus both ways on all 24 days would have nothing left to pay out. An employee who uses the bus less receives the difference in cash (M-02, M-03, M-06). This reading is assumption A-01.

**Working days vs the 24-day basis (added in v0.2).** On a Monday–Saturday week, November 2026 has 25 working days and December 2026 has 27. At 500 PKR a trip × 2 trips a day, a regular bus user is charged 25,000 and 27,000 PKR, more than the 24,000 PKR allowance. So deductions above the allowance will be the normal monthly case, not an exception. The rule for this is open question Q-07, now blocking.

**The key risk** is that employees skip swiping to keep more cash. The meeting agreed to mitigate this by installing readers at both ends of the route, and by making every swipe visible and auditable (M-08, M-09, M-13, M-14).

## 1.3 Scope
### In scope
- Monthly transport allowance for eligible Karachi staff (M-02).
- RFID swipe capture at designated terminals at the KDC pickup point and the hospital, using existing employee ID cards (M-04, M-09, M-12).
- Per-trip deduction calculated from the current fuel price and a Finance-defined formula (M-05, M-07).
- A frontend for HR and Finance to maintain the deduction formula and fuel prices (M-07).
- Payout of the unused allowance with the monthly salary (M-06).
- A manual adjustment portal for missed swipes, with an approval workflow (M-10, M-11).
- A notification on the employee's dashboard for every swipe, plus a transaction trail for HR and Finance (M-13, M-14).

### Out of scope
- Procurement and installation of the RFID reader hardware. This SRS only defines what the system needs from it (see §7.5).
- Bus routing, scheduling and fleet management. None were discussed.
- Transport for cities other than Karachi.
- Changes to how cafeteria and attendance use the ID card (M-12). These must keep working unchanged.

## 1.4 Stakeholders
| Name / Role | Department | Interest / responsibility | Attended meeting |
|---|---|---|---|
| Mr. Ubaid | Transport / Operations (to be confirmed) | Presented the operational flow; owns the go-live date | Yes |
| Mr. Shahzad | Information Systems | Raised the misuse concern; owns delivery, the design sketch and management presentation | Yes |
| HR | Human Resources | Maintains formulas and fuel prices; eligibility; audit trail | To be confirmed |
| Finance | Finance | Owns the deduction formula; payroll payout; audit trail | To be confirmed (alignment is an action item) |
| Transport Coordinator | Transport | Approves missed-swipe adjustments | No |
| Supervisors | All Karachi departments | Approve missed-swipe adjustments | No |
| Karachi employees | All | Swipe cards; view trips; request adjustments; receive payout | No |
| Management | Hospital management | Approve the final layout before development | No |

## 1.5 Definitions and abbreviations
| Term | Meaning |
|---|---|
| RFID | Radio-frequency identification: the contactless chip in the employee ID card |
| Terminal | An RFID reader at a designated boarding or disembarking point |
| Swipe | One card read at a terminal |
| Trip | One journey between the KDC pickup point and the hospital, in either direction (definition to be confirmed: Q-02) |
| Allowance | The monthly transport amount granted to an eligible employee (reference: 24,000 PKR) |
| Deduction | The amount subtracted from the allowance for a trip |
| Payout | Allowance minus total deductions for the month, paid with salary |
| KDC | The Karachi pickup point named in the meeting. Full name to be confirmed (Q-01) |
| Adjustment | An approved manual trip record for a missed swipe |

## 1.6 References
- Minutes of meeting: Karachi Transport Allowance System & RFID Deduction Mechanism. The meeting date is not stated in the notes (Q-01).
- Finance deduction formula: pending, as an action item from the meeting (M-18).
- System design sketch and management-approved layout: pending (M-17, M-19).

# 2. Current state (As-Is)
The Karachi hospital is not yet operating, so there is no existing transport allowance process for Karachi staff. Employee ID cards are already used for cafeteria transactions and attendance tracking (M-12). The systems behind those card uses are not described in the notes. They matter for integration (Q-09).

# 3. Proposed solution overview (To-Be)
1. HR marks eligible Karachi employees for the transport allowance (FR-001).
2. Finance sets the deduction formula and keeps the fuel price current through an HR/Finance screen (FR-008, FR-009).
3. The employee swipes their ID card at the KDC terminal when boarding and at the hospital terminal when getting off, and the reverse on the return journey (FR-003, FR-005).
4. The system turns swipes into trips and calculates each trip's deduction from the fuel price in effect (FR-006, FR-007).
5. The employee sees a dashboard notification for each swipe and can review their trips and month-to-date balance (FR-015, FR-016).
6. For a missed swipe, the employee submits an adjustment request. A supervisor or the transport coordinator approves or rejects it (FR-011 to FR-013).
7. At the monthly payroll cut-off, the system computes allowance − deductions and passes the payout to payroll to be paid with the salary (FR-010, FR-018).
8. HR and Finance review the full transaction trail and the exception report of possible non-swiping (FR-014, FR-017).

# 4. Business requirements
| ID | Business requirement | Source (M-NN) | Priority |
|---|---|---|---|
| BR-01 | Give Karachi staff a monthly transport allowance that reflects their actual bus use | M-02, M-03, M-06 | Must |
| BR-02 | Record bus use automatically with the existing employee ID card, without a new card | M-04, M-12 | Must |
| BR-03 | Link the cost of each trip to current fuel prices, maintained by HR/Finance without IT involvement | M-05, M-07 | Must |
| BR-04 | Prevent and detect employees not swiping in order to keep cash, while allowing honest mistakes to be corrected | M-08, M-09, M-10, M-11 | Must |
| BR-05 | Make every trip and deduction transparent to the employee and auditable by HR and Finance | M-13, M-14 | Must |
| BR-06 | Be operational for the Karachi hospital opening in the first week of November | M-15, M-16 | Must |

# 5. Functional requirements
## 5.1 Eligibility and allowance
### FR-001 Maintain transport allowance eligibility
**Description:** The system shall allow HR to mark a Karachi employee as eligible or not eligible for the transport allowance, with an effective-from date.
**Priority:** Must
**Source:** M-02 (inferred: the notes say "employees will receive" without defining who)
**Acceptance criteria:**
- AC1: Given HR marks employee EMP-TEST-001 eligible from 01-11-2026, when the November allowance is calculated, then EMP-TEST-001 receives an allowance.
- AC2 (negative): Given an employee not marked eligible, when they swipe at a transport terminal, then the swipe is recorded but no deduction is posted, and the swipe appears on the exception report as "non-eligible user".
**Notes / open questions:** Q-03 (who is eligible; is bus use mandatory)

### FR-002 Calculate monthly allowance
**Description:** The system shall calculate each eligible employee's monthly transport allowance from a configurable amount and base-day count (reference: 24,000 PKR for a 24-day month).
**Priority:** Must
**Source:** M-02
**Business rules:** RULE-01
**Acceptance criteria:**
- AC1: Given the configured allowance is 24,000 PKR for 24 days and an employee is eligible for the whole month, when the month closes, then their allowance is 24,000 PKR.
- AC2: Given Finance changes the allowance amount effective next month, when the current month closes, then the current month still uses the old amount.
- AC3 (negative): Given an employee who is eligible for only part of the month, when the month closes, then the allowance follows the proration rule agreed under Q-04. Until that is agreed, the calculation is blocked with the message "Proration rule not configured".
**Notes / open questions:** Q-04 (proration for joiners, leavers, leave and shift patterns)

## 5.2 RFID trip capture
### FR-003 Record swipes
**Description:** The system shall record every RFID swipe at a designated transport terminal with the card, the resolved employee, the terminal, its location, the direction (boarding or disembarking, determined by the rule agreed in Q-15), and the date and time. (changed in v0.2)
**Priority:** Must
**Source:** M-04, M-09
**Notes / open questions:** Q-15 (one terminal per location cannot tell boarding from disembarking by itself)
**Acceptance criteria:**
- AC1: Given EMP-TEST-001 swipes at the KDC boarding terminal at 07:05, when the swipe is received, then a swipe record exists with employee EMP-TEST-001, terminal KDC, direction Boarding and time 07:05.
- AC2 (negative): Given a card that is not linked to any active employee, when it is swiped, then the swipe is stored as "Unknown card", no deduction is posted, and it appears on the exception report.

### FR-004 Use the existing employee ID card
**Description:** The system shall identify the employee from their existing employee ID card, the same card used for cafeteria and attendance, and require no additional card.
**Priority:** Must
**Source:** M-12
**Acceptance criteria:**
- AC1: Given an employee whose ID card works for attendance, when they swipe at a transport terminal, then the system identifies the same employee.
- AC2 (negative): Given a card reported lost and deactivated, when it is swiped at a transport terminal, then the swipe is rejected as "Inactive card" and nothing is charged.
- AC3: Given a transport swipe, when the employee later uses the card for the cafeteria and attendance, then both work exactly as before.

### FR-005 Maintain transport terminals
**Description:** The system shall allow an administrator to register transport terminals with location (at least the KDC pickup point and the hospital), direction or usage, and active status.
**Priority:** Must
**Source:** M-04, M-09
**Acceptance criteria:**
- AC1: Given terminals are registered at KDC and at the hospital, when swipes arrive from them, then each swipe shows the right location.
- AC2 (negative): Given a swipe from a reader that is not registered as a transport terminal (for example a cafeteria reader), then it is not treated as a trip.

### FR-006 Derive trips from swipes
**Description:** The system shall turn swipes into trips following the trip rules (RULE-04), including ignoring repeat swipes within a configurable interval.
**Priority:** Must
**Source:** M-04, M-09
**Business rules:** RULE-04
**Acceptance criteria:**
- AC1: Given a boarding swipe at KDC at 07:05 and a disembarking swipe at the hospital at 07:50 on the same day, when trips are derived, then exactly one trip KDC→Hospital is created.
- AC2: Given the employee swipes twice at the same terminal within 2 minutes (proposed default, not agreed in the meeting; configurable) (changed in v0.2), when trips are derived, then only one swipe counts.
- AC3 (negative): Given only a boarding swipe with no matching disembarking swipe, when trips are derived, then the result follows the rule agreed in Q-02, and the trip is marked "Incomplete" for review.
**Notes / open questions:** Q-02

## 5.3 Deduction calculation
### FR-007 Calculate the per-trip deduction
**Description:** The system shall calculate each trip's deduction with the active deduction formula and the fuel price effective on the trip date, and store the formula version, fuel price and amount on the trip.
**Priority:** Must
**Source:** M-03, M-05
**Business rules:** RULE-02, RULE-06
**Acceptance criteria:**
- AC1: Given the formula and fuel price give a per-trip cost of 500 PKR, when a trip is recorded, then 500 PKR is deducted and the trip stores the fuel price and formula version used.
- AC2: Given the fuel price changes on the 16th, when trips on the 15th and 16th are calculated, then each uses the price effective on its own date.
- AC3 (negative): Given no fuel price is effective on the trip date, when the deduction is calculated, then the trip is marked "Rate missing", no amount is posted, and Finance is alerted.
**Notes / open questions:** Q-05 (the formula itself), Q-06 (price effective date vs "real time")

### FR-008 Maintain fuel prices
**Description:** The system shall provide HR and Finance with a screen to enter fuel prices with an effective date and time, keeping the full history.
**Priority:** Must
**Source:** M-05, M-07
**Acceptance criteria:**
- AC1: Given Finance enters 280 PKR/litre effective 16-11-2026 00:00, when trips on or after that time are calculated, then they use 280 PKR/litre.
- AC2 (negative): Given a user without the Finance/HR transport role, when they open the screen, then access is denied.
- AC3 (negative): Given a price entry with a date in a payroll month that has already closed, when saved, then it is rejected with "Payroll month closed".

### FR-009 Maintain the deduction formula
**Description:** The system shall provide HR and Finance with a screen to maintain the deduction formula's parameters (for example the base per-trip cost, reference fuel price and distance or consumption factors) as versions with effective dates.
**Priority:** Must
**Source:** M-07, M-18
**Acceptance criteria:**
- AC1: Given Finance saves a new formula version effective 01-12-2026, when November trips are calculated, then they still use the previous version.
- AC2: Given a formula version is saved, when a user views it, then the screen shows a worked example per-trip cost at the current fuel price before it is activated.
- AC3 (negative): Given a formula whose parameters produce a zero or negative per-trip cost, when activation is attempted, then it is blocked with a validation message.
**Notes / open questions:** Q-05 (the formula's form is not yet agreed with Finance)

### FR-010 Calculate the monthly payout
**Description:** At the payroll cut-off, the system shall calculate each eligible employee's payout as the monthly allowance minus total deductions for valid trips (including approved adjustments), and apply the agreed rule when deductions exceed the allowance.
**Priority:** Must
**Source:** M-06
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given an allowance of 24,000 PKR and 30 trips at 500 PKR, when the month closes, then the payout is 9,000 PKR.
- AC2: Given 48 trips at 500 PKR, when the month closes, then the payout is 0 PKR.
- AC3 (negative): Given deductions of 25,000 PKR against an allowance of 24,000 PKR, when the month closes, then the result follows the rule chosen in Q-07, and the case is listed for Finance review. (changed in v0.3)
**Notes / open questions:** Q-07 (blocking: see §1.2, deductions will exceed the allowance in any month with more than 24 working days), Q-08, Q-14 (changed in v0.2)

## 5.4 Missed-swipe adjustments
### FR-011 Submit an adjustment request
**Description:** The system shall allow an employee to submit a missed-swipe adjustment request stating the date, the direction or trip, and a reason, within the allowed submission window.
**Priority:** Must
**Source:** M-10
**Acceptance criteria:**
- AC1: Given EMP-TEST-001 forgot to swipe on 05-11-2026 morning, when they submit a request with a reason, then the request is created with status Submitted and routed for approval.
- AC2 (negative): Given the employee already has a recorded trip for that date and direction, when they submit a request for it, then it is rejected with "Trip already recorded".
- AC3 (negative): Given the request date is outside the submission window (Q-10), when submitted, then it is rejected with a message stating the window.

### FR-012 Route adjustment requests for approval
**Description:** The system shall route each adjustment request to the approver defined by the routing rule: the employee's supervisor or the transport coordinator.
**Priority:** Must
**Source:** M-11
**Acceptance criteria:**
- AC1: Given the routing rule agreed in Q-11, when a request is submitted, then it appears in the correct approver's pending list.
- AC2 (negative): Given no approver is defined for the employee, when the request is submitted, then it goes to the transport coordinator and the gap is flagged to HR.
- AC3 (negative, added in v0.3): Given the approver has not acted within N working days (N configurable, proposed default 2, to be confirmed by HR) or is on approved leave, when that time passes, then the request escalates to the transport coordinator and both the approver and the coordinator are notified.
**Notes / open questions:** Q-11

### FR-013 Approve or reject adjustments
**Description:** The system shall allow the approver to approve or reject an adjustment with a comment. An approved adjustment creates a trip flagged "Manual" that is deducted like any other trip.
**Priority:** Must
**Source:** M-10, M-11
**Acceptance criteria:**
- AC1: Given a pending request, when the approver approves it, then a Manual trip is created, the deduction is calculated (FR-007), and the employee is notified.
- AC2 (negative): Given the approver is the requester, when they try to approve their own request, then the action is blocked.
- AC3 (negative): Given a request still pending at payroll cut-off, when the month closes, then it is carried to the next month's calculation (rule to be confirmed in Q-10) and is not silently lost.
- AC4 (negative, added in v0.3): Given the routing rule in Q-11 lets more than one approver act on a request, and one of them has already approved or rejected it, when another approver tries to act, then the action is blocked with "Already decided by [approver name]".

### FR-014 Report possible non-swiping
**Description:** The system shall produce a report for HR and the transport coordinator of eligible employees whose trip records suggest missed or skipped swipes. Examples: attendance at the hospital with no trip, a boarding swipe with no matching disembark, and unusually low monthly trips. Thresholds are configurable.
**Priority:** Should
**Source:** M-08 (inferred: the meeting agreed readers at both ends as the control; this report is proposed to detect the misuse that concern describes)
**Acceptance criteria:**
- AC1: Given EMP-TEST-002 is marked present by attendance on 10 days and has trips on only 2 of them, when the report runs, then EMP-TEST-002 is listed with the 8 unmatched days.
- AC2 (negative): Given an employee not eligible for the allowance, when the report runs, then they are not listed as a potential non-swiper.
- AC3 (negative, added in v0.3): Given an employee's attended day falls on a shift with no bus service (per Q-17), or the employee is approved to use their own transport, when the report runs, then that day is not counted as a missed trip.
**Notes / open questions:** Q-03, Q-12, Q-17. Priority for the Solution Architect to confirm: BR-04 is Must, and this is its only detection requirement (review RV-07). (changed in v0.2)

## 5.5 Transparency and audit
### FR-015 Swipe notification on the employee dashboard
**Description:** The system shall post a notification on the employee's dashboard for every recorded swipe, showing date, time, location, direction and (once calculated) the deduction.
**Priority:** Must
**Source:** M-13
**Acceptance criteria:**
- AC1: Given EMP-TEST-001 swipes at KDC at 07:05, when they open their dashboard, then a notification shows "Swipe recorded: KDC, Boarding, 07:05".
- AC2 (negative): Given another employee is logged in, when they view their dashboard, then EMP-TEST-001's swipes are not visible.
**Notes / open questions:** Q-13 (which dashboard)

### FR-016 Employee trip and balance view
**Description:** The system shall let an employee view their own trips, deductions, pending adjustments and month-to-date estimated payout.
**Priority:** Should
**Source:** M-13, M-14
**Acceptance criteria:**
- AC1: Given 10 trips at 500 PKR so far in the month, when the employee opens the view, then it shows deductions of 5,000 PKR and an estimated payout of 19,000 PKR, labelled as an estimate.
- AC2 (negative): Given an employee not eligible for the allowance, when they open the view, then it states they are not enrolled.

### FR-017 Transaction trail for HR and Finance
**Description:** The system shall give HR and Finance a searchable, exportable trail of all swipes, trips, deductions (with fuel price and formula version), adjustments (with approver and comments), and fuel price and formula changes.
**Priority:** Must
**Source:** M-14
**Acceptance criteria:**
- AC1: Given a trip deducted at 500 PKR, when Finance opens its trail, then they see the originating swipes, the fuel price and formula version used, and any adjustment that created it.
- AC2 (negative): Given a supervisor without the HR/Finance role, when they open the trail, then access is denied.

### FR-018 Monthly transport payroll register
**Description:** For each payroll month, the system shall produce a register per employee (allowance, number of trips, total deduction, payout) and pass the payout to payroll as a salary component.
**Priority:** Must
**Source:** M-06 (inferred: a hand-off to payroll is needed to pay with salary)
**Acceptance criteria:**
- AC1: Given the month is closed, when Finance generates the register, then the payout per employee equals FR-010's result, and the totals match the sum of employee rows.
- AC2 (negative): Given the register was already sent to payroll, when someone tries to regenerate it, then it is blocked unless Finance reopens the month, and the reopening is audited.
- AC3 (added in v0.2): Given an adjustment for a trip in a closed month is approved after that month's register was sent to payroll, when the next month's register is generated, then the adjustment appears as a separate prior-month correction line and the sent register is unchanged. The exact mechanism depends on Q-10.

# 6. Non-functional requirements
| ID | Category | Requirement | Measure / target | Source | Status |
|---|---|---|---|---|---|
| NFR-PERF-01 | PERF | A swipe is recorded and its dashboard notification is visible quickly | Within 60 seconds of the swipe, when the terminal is online | M-13 | Proposed (not discussed in meeting) |
| NFR-PERF-02 | PERF | The terminal responds to a swipe fast enough for boarding queues | Accept/reject feedback within 1 second | M-04 | Proposed (not discussed in meeting) |
| NFR-AVL-01 | AVL | No swipe is lost when the network at a terminal is down | Terminals store swipes offline for at least 7 days and sync when back online, with the original timestamp | M-08, M-09 | Proposed (not discussed in meeting) |
| NFR-SEC-01 | SEC | Role-based access | Employees see only their own data. Approvers see only requests routed to them. HR/Finance see the trail. Only HR/Finance transport roles change prices or formulas | M-07, M-14 | Proposed (not discussed in meeting) |
| NFR-SEC-02 | SEC | Changes to fuel price and formula use maker-checker | Any change is entered by one user and activated by a second authorised user who is not the maker (changed in v0.2) | M-07 | Proposed (not discussed in meeting) |
| NFR-AUD-01 | AUD | Full audit trail | Who, when, old value and new value for every price, formula, eligibility, adjustment and month-reopen action. Swipes are never deleted, only reversed with a reason | M-14 | Discussed |
| NFR-DAT-01 | DAT | Data retention | Swipe and trip records kept at least as long as payroll records (period per Finance policy; see Q-18) | M-14 | Proposed (not discussed in meeting) |
| NFR-CMP-01 | CMP | Payroll and tax treatment | The payout is paid, and taxed if applicable, as Finance specifies. Amounts are rounded to whole rupees using an agreed rule | M-06 | Proposed (not discussed in meeting) |
| NFR-INT-01 | INT | Reuse of the existing card infrastructure | Transport terminals work with the same card numbers and card status as the cafeteria and attendance systems, with no re-issue of cards | M-12 | Discussed |
| NFR-USA-01 | USA | Easy to use for staff | Adjustment requests and trip views work on a phone browser and take at most 3 steps to submit | M-10 | Proposed (not discussed in meeting) |
| NFR-OPS-01 | OPS | Operational readiness | Terminal health is monitored (online/offline, last swipe time) and failures alert the transport coordinator and IS | M-09 | Proposed (not discussed in meeting) |

# 7. Business rules, data and access
## 7.1 Business rules
| ID | Rule | Applies to (FR) | Source |
|---|---|---|---|
| RULE-01 | The reference monthly allowance is 24,000 PKR for a 24-day month. The amount and base days are configurable. Months with more than 24 working days: see Q-07 (changed in v0.2) | FR-002, FR-010 | M-02 |
| RULE-02 | The reference per-trip cost is 500 PKR (given as an example). The actual cost comes from the formula and the current fuel price | FR-007, FR-009 | M-03, M-05 |
| RULE-03 | Monthly payout = allowance − sum of deductions for valid trips (automatic plus approved manual), paid with the monthly salary | FR-010, FR-018 | M-06 |
| RULE-04 | A trip is recorded from swipes at designated terminals when boarding or disembarking. The pairing rule and the handling of single swipes are to be confirmed | FR-006 | M-04, M-09, Q-02, Q-15 (changed in v0.3) |
| RULE-05 | A missed-swipe trip counts only after approval by a supervisor or the transport coordinator | FR-011 to FR-013 | M-10, M-11 |
| RULE-06 | Each trip uses the fuel price and formula version in effect at the trip's date and time | FR-007 | M-05 (assumption A-02) |

## 7.2 Data requirements
| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
|---|---|---|---|---|---|
| Eligibility flag + effective date | Whether the employee receives the allowance | Yes | From date ≤ to date | EMP-TEST-001, from 01-11-2026 | FR-001 |
| Allowance amount / base days | Monthly allowance and its day basis | Yes | Amount > 0; days 1–31 | 24,000 PKR / 24 | FR-002 |
| Terminal | A reader at a location | Yes | Unique code; location; status | KDC-01, Hospital-01 | FR-005 |
| Swipe | One card read | Yes | Card, terminal, direction, timestamp | Card 0000-TEST-01, KDC-01, Boarding, 05-11-2026 07:05 | FR-003 |
| Trip | A derived journey | Yes | Date, from/to, source (RFID/Manual), deduction | 05-11-2026, KDC→Hospital, 500 PKR | FR-006, FR-007 |
| Fuel price | Price per litre with effective date/time | Yes | > 0; no overlapping periods | 280 PKR/L from 16-11-2026 | FR-008 |
| Formula version | Deduction formula parameters | Yes | Effective date; activated by checker | v1 from 01-11-2026 | FR-009 |
| Adjustment request | Missed-swipe claim | Yes | Date, trip, reason (min. 10 characters), status | Forgot card, 05-11-2026 AM | FR-011 |
| Monthly result | Allowance, trips, deductions, payout | Yes | Payout ≥ 0 unless Q-07 allows otherwise | 24,000 / 30 / 15,000 / 9,000 | FR-010, FR-018 |

## 7.3 User roles and access matrix
| Function / screen | Employee | Supervisor | Transport Coordinator | HR | Finance | IS Admin |
|---|---|---|---|---|---|---|
| Swipe card / view own trips and notifications | R | R (own) | R (own) | R (own) | R (own) | - |
| Submit adjustment request | C | C (own) | C (own) | C (own) | C (own) | - |
| Approve/reject adjustment | - | A (own team) | A | - | - | - |
| Eligibility maintenance | - | - | R | C R U | R | - |
| Fuel price maintenance | - | - | - | C R U | C R U A | - |
| Formula maintenance | - | - | - | C R U | C R U A | - |
| Transaction trail / exception report | - | - | R | R | R | - |
| Monthly register / send to payroll | - | - | - | R | C R A | - |
| Terminal maintenance | - | - | R | - | - | C R U D |

C = create, R = read, U = update, D = delete, A = approve/activate. Whether HR or Finance, or both, can activate price and formula changes is part of Q-05.

## 7.4 Reports and notifications
| Report / notification | Audience | Trigger / frequency | Content | Related FR |
|---|---|---|---|---|
| Swipe notification | Employee | Every swipe | Location, direction, time, deduction | FR-015 |
| Adjustment request pending | Approver | On submission | Employee, date, trip, reason | FR-012 |
| Adjustment decision | Employee | On approve/reject | Decision, comment | FR-013 |
| Missing fuel price alert | Finance | When a trip has no effective price | Trip date, count affected | FR-007 |
| Possible non-swiping report | HR, Transport Coordinator | On demand and monthly before cut-off | Employee, attended days without trips, incomplete trips | FR-014 |
| Transaction trail | HR, Finance | On demand, exportable | Swipes, trips, rates, adjustments, changes | FR-017 |
| Monthly transport payroll register | Finance, Payroll | Monthly at cut-off | Allowance, trips, deductions, payout per employee | FR-018 |
| Terminal offline alert | Transport Coordinator, IS | When a terminal stops reporting | Terminal, last contact | NFR-OPS-01 |

## 7.5 Interfaces
| System | Direction (in/out) | Data exchanged | Frequency | Related FR |
|---|---|---|---|---|
| RFID terminals (KDC, hospital) | In | Card number, terminal, timestamp | Real time, with offline buffering | FR-003, FR-006 |
| ID card / access management system (used by cafeteria and attendance) | In | Card-to-employee mapping, card status | Real time or daily sync (Q-09) | FR-004 |
| Attendance system | In | Days present per employee | Daily | FR-014 |
| Payroll | Out | Monthly transport payout per employee | Monthly at cut-off | FR-018 |
| Employee dashboard / self-service portal | Out | Swipe notifications, trip views, adjustment forms | Real time | FR-011, FR-015, FR-016 |

# 8. Impact analysis
> Schema context used: none. The HRD schema has not been indexed yet, so all database and system impact items below are PROVISIONAL and must be verified against the schema. New object names follow HRD standards and are proposals only.

## 8.1 Business impact
| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
|---|---|---|---|---|
| IMP-01 | All Karachi staff | New benefit model: cash allowance reduced by actual bus use. Staff must swipe at both ends of every trip | FR-002, FR-003, FR-010 | N |
| IMP-02 | Finance | Owns the deduction formula, fuel price updates, monthly register and payroll payout. Needs a routine for price updates | FR-007 to FR-010, FR-018 | N |
| IMP-03 | HR | Maintains eligibility; reviews the exception report; handles disputes | FR-001, FR-014, FR-017 | N |
| IMP-04 | Supervisors and Transport Coordinator | New approval workload for missed-swipe adjustments | FR-012, FR-013 | N |
| IMP-05 | Policy / SOP | A transport allowance policy is needed covering eligibility, the swipe obligation, the adjustment window, misuse consequences and tax treatment | FR-001, FR-011, FR-014 | N |
| IMP-24 | Card replacement process (added in v0.2) | Lost or damaged cards cause missed swipes until replaced. Replacement time drives adjustment volume | FR-004, FR-011 | N |
| IMP-06 | Hospital opening | Clinical staff who miss or are delayed by the bus could affect shift cover. Boarding queues at the terminals must not delay departures | NFR-PERF-02, NFR-AVL-01 | Y (indirect: staff arrival for clinical shifts) |

## 8.2 System impact
| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|
| IMP-07 | RFID terminals at KDC and the hospital | New | Hardware and reader integration; offline buffering | FR-003, FR-005 | MoM M-09 | PROVISIONAL – not verified |
| IMP-08 | ID card / access management system (cafeteria and attendance) | Read-only | Card-to-employee mapping and card status reused | FR-004 | MoM M-12 (system not identified) | PROVISIONAL – not verified |
| IMP-09 | Attendance system | Read-only | Days present, for the non-swiping report | FR-014 | MoM M-12 | PROVISIONAL – not verified |
| IMP-10 | Payroll | Modify | New earning component for the transport payout; monthly import | FR-018 | MoM M-06 | PROVISIONAL – not verified |
| IMP-11 | Employee dashboard / self-service | Modify | Swipe notifications, trip view, adjustment request form | FR-011, FR-015, FR-016 | MoM M-13 | PROVISIONAL – not verified |
| IMP-12 | New APEX pages: fuel price, formula, eligibility, approvals, trail, reports | New | HR/Finance frontend and approver screens | FR-001, FR-008, FR-009, FR-013, FR-014, FR-017 | Not in snapshot | NEW (proposed) |
| IMP-13 | New package `HRD.PKG_TRANSPORT_ALLOWANCE` | New | Trip derivation, deduction, monthly payout, adjustment workflow | FR-006, FR-007, FR-010, FR-013 | Not in snapshot | NEW (proposed) |
| IMP-25 | Final settlement process for leavers (added in v0.2) | Modify | Transport balance included in the leaver's final settlement | FR-010 | Domain; not in MoM | PROVISIONAL – not verified |
| IMP-26 | Shift roster / duty schedule, if a roster system exists (added in v0.2) | Read-only | Shift times, to tell staff with no bus for their shift apart from non-swipers | FR-014 | Domain; not in MoM | PROVISIONAL – not verified |
| IMP-27 | Leave records (added in v0.3) | Read-only | Approved leave, to escalate requests when the approver is on leave, and for proration (Q-04) | FR-002, FR-012 | Review v2 §4.2; not in MoM | PROVISIONAL – not verified |
| IMP-14 | Scheduled jobs: trip derivation, month-end calculation, terminal health check | New | DBMS_SCHEDULER jobs | FR-006, FR-010, NFR-OPS-01 | Not in snapshot | NEW (proposed) |

## 8.3 Database impact
| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|
| IMP-15 | Employee master (name to be confirmed) | Read-only or Modify | Eligibility may be stored here or in a new table | To be identified | No | FR-001 | None | PROVISIONAL – not verified |
| IMP-16 | Card / RFID mapping table used by cafeteria and attendance (name to be confirmed) | Read-only | Resolve card to employee | To be identified | No | FR-004 | MoM M-12 | PROVISIONAL – not verified |
| IMP-17 | `HRD_TRANSPORT_TERMINAL_MST` | New | Terminals and locations | PKG_TRANSPORT_ALLOWANCE | Seed KDC and hospital terminals | FR-005 | Proposed | NEW (proposed) |
| IMP-18 | `HRD_TRANSPORT_SWIPE_TRN` | New | Raw swipes (high volume: about 2–4 per employee per day) | Trip derivation job | No | FR-003 | Proposed | NEW (proposed) |
| IMP-19 | `HRD_TRANSPORT_TRIP_TRN` | New | Derived and manual trips with deduction, fuel price and formula version | Monthly calculation, reports | No | FR-006, FR-007 | Proposed | NEW (proposed) |
| IMP-20 | `HRD_FUEL_PRICE_HIS` | New | Effective-dated fuel prices | Deduction calculation | Initial price at go-live | FR-008 | Proposed | NEW (proposed) |
| IMP-21 | `HRD_TRANSPORT_FORMULA_MST` | New | Versioned formula parameters and allowance settings | Deduction calculation | Initial version from Finance | FR-002, FR-009 | Proposed | NEW (proposed) |
| IMP-22 | `HRD_TRANSPORT_ADJ_REQUEST` | New | Missed-swipe requests and approvals | Approval pages, trip creation | No | FR-011 to FR-013 | Proposed | NEW (proposed) |
| IMP-23 | `HRD_TRANSPORT_MONTHLY_DTL` | New | Monthly allowance, deductions and payout per employee | Payroll interface | No | FR-010, FR-018 | Proposed | NEW (proposed) |

## 8.4 Risks
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Schedule: build due end of October, live first week of November, leaves about a week for UAT, hardware installation and fixes | High | High | Proposal (not agreed; to raise at the management layout approval, M-19): swipe capture, notifications and adjustments live for the opening; the month-end payout calculation ready before the November payroll cut-off, which gives extra weeks (changed in v0.2) |
| The Finance formula is not agreed in time (M-18) | Medium | High | Get a formula decision by a fixed date; build a parameterised formula (FR-009) so the final values are data, not code |
| Employees skip swiping to keep cash (M-08) | High | Medium | Readers at both ends (M-09); the non-swiping report (FR-014); a policy on consequences (IMP-05) |
| Terminal or network outage at the KDC pickup point loses swipes | Medium | High | Offline buffering (NFR-AVL-01); terminal health alerts (NFR-OPS-01); adjustment portal as a fallback |
| The card system behind cafeteria and attendance can't give real-time card data | Medium | Medium | Confirm the interface early (Q-09); fall back to a daily sync |
| Frequent fuel price changes cause disputes over which price applied | Medium | Low | Effective-dated prices, with the price stored on each trip (RULE-06, FR-017) |

# 9. Assumptions, constraints and dependencies
## 9.1 Assumptions
| ID | Assumption | Needs confirmation from |
|---|---|---|
| A-01 | 24,000 PKR covers 2 trips a day (to and from the hospital) × 24 days × 500 PKR, so a full-use employee's payout at the reference price is 0 | Mr. Ubaid, Finance |
| A-02 | A fuel price applies from its effective date and time. "Real-time" means Finance can update it at any time, not that it is fetched automatically from an external source | Finance |
| A-03 | The existing employee ID cards are already RFID-enabled and readable by the new transport terminals | IS / card vendor |
| A-04 | The payout is a salary component in the same monthly payroll run | Finance / Payroll |
| A-05 | The "employee dashboard" is an existing self-service portal that can show notifications | IS |
| A-06 | The allowance applies to Karachi hospital staff only | Mr. Ubaid, HR |

## 9.2 Constraints
- The system must be operational in the first week of November, for the Karachi hospital opening (M-15).
- A complete, testable build is due by the end of October (M-16).
- The system design sketch and finalised layout must be approved by management before development starts (M-17, M-19).
- Existing employee ID cards must be used. Cafeteria and attendance use must not be disrupted (M-12).

## 9.3 Dependencies
- The Finance deduction formula (M-18, Q-05).
- RFID terminal procurement and installation at KDC and the hospital (M-09).
- Access to the card/attendance system's data (Q-09).
- A payroll interface for the new earning component (IMP-10).
- The transport allowance policy (IMP-05).

# 10. Open questions
| ID | Question | Raised because (M-NN / FR) | Addressed to | Blocking? |
|---|---|---|---|---|
| Q-01 | What is the meeting date, and what does "KDC" stand for? Is it the only pickup point, or will there be more routes and stops? | M-09 | Mr. Ubaid | No |
| Q-02 | What exactly is a trip? Is the deduction per trip (a boarding and disembarking pair) or per swipe? What happens with only one swipe of a pair? | M-04, M-09, FR-006 | Mr. Ubaid, Finance | Yes |
| Q-03 | Who is eligible? Is bus use mandatory for eligible staff, or can staff use their own transport and keep the full allowance? | M-02, M-08, FR-001, FR-014 | Mr. Ubaid, HR | Yes |
| Q-04 | How is the allowance prorated for joiners, leavers, leave, and staff on shift patterns (for example 12-hour shifts with fewer than 24 duty days)? | M-02, FR-002 | HR, Finance | Yes |
| Q-05 | What is the deduction formula (for example 500 × current fuel price ÷ reference fuel price)? Who enters it and who activates it: HR, Finance or both? Is a formula with editable parameters acceptable, or does Finance expect to write a free formula? (changed in v0.2) | M-05, M-07, M-18 | Finance | Yes |
| Q-06 | How often does the fuel price change, and from when does a new price apply (its announcement date, a set date, or the date it is entered)? | M-05, FR-007 | Finance | No |
| Q-07 | Deductions will exceed the allowance in every month with more than 24 working days (§1.2). Should the system (a) cap the payout at 0, (b) scale the allowance to actual working days, or (c) set the per-trip cost as allowance ÷ (2 × working days)? If the excess is recovered from salary, what is the policy basis? (changed in v0.2) | M-02, M-06, FR-010 | Finance, Mr. Ubaid | Yes |
| Q-08 | Is the payout taxable, and how should it appear on the payslip? | M-06 | Finance | No |
| Q-09 | Which system manages the ID cards for cafeteria and attendance? Can it give card-to-employee data in real time? Are the new terminals from the same vendor? | M-12, FR-004 | IS | Yes |
| Q-10 | How long after a missed swipe can an employee request an adjustment? What happens to requests still pending at payroll cut-off? Is there a limit per month? | M-10, FR-011, FR-013 | HR, Mr. Ubaid | No |
| Q-11 | Which approver handles a request: the supervisor or the transport coordinator? Under what rule, for example by department or by reason? | M-11, FR-012 | Mr. Ubaid, HR | Yes |
| Q-12 | What action is taken when misuse is suspected (warning, forced deduction, disciplinary)? Should the system auto-deduct for attended days without trips? | M-08, FR-014 | HR, Management | No |
| Q-13 | Which "employee dashboard" should show the notifications? Should staff also get SMS or email, for example if they have no dashboard access? | M-13, FR-015 | IS, HR | No |
| Q-14 | What month does the first payout cover (a partial November from the opening date)? What is the payroll cut-off date? Without this, the first payroll calculation is blocked for all staff (changed in v0.2) | M-15, FR-010 | Finance | Yes |
| Q-15 | With one terminal per location, how is direction known: separate boarding and disembarking readers, or the order of an employee's swipes that day? (added in v0.2) | M-04, M-09, FR-003, FR-006 | Mr. Ubaid, IS | Yes |
| Q-16 | When a fuel price is entered after its effective date, should the open month's affected trips be recalculated and employees re-notified, or should prices apply only from when they are entered? (added in v0.2) | M-05, FR-007, FR-008 | Finance | No |
| Q-17 | Which shifts do the buses serve (day, evening, night, 12-hour rotas, on-call)? What is the allowance rule for staff whose shift has no bus? (added in v0.2) | M-02, M-08, M-15, FR-014 | Mr. Ubaid, Nursing, HR | Yes |
| Q-18 | How long are swipe records (employee movement data) kept, and are details purged after the payroll audit period? (added in v0.2) | M-14, NFR-DAT-01 | HR, Finance | No |

# Appendix A. Minutes of meeting breakdown
| M-ID | Original statement | Type | Mapped to |
|---|---|---|---|
| M-01 | Mr. Ubaid presented the operational flow for the Karachi staff transport system | Information | §1.2 |
| M-02 | Employees will receive a monthly transport allowance of 24,000 PKR for a 24-day month | Requirement | BR-01, FR-001, FR-002, RULE-01, Q-03, Q-04 |
| M-03 | Calculated at a per-trip cost of 500 PKR (e.g.) | Requirement | FR-007, RULE-02, A-01 |
| M-04 | Employees must swipe their RFID cards at designated terminals when boarding or disembarking | Requirement | BR-02, FR-003, FR-005, FR-006, RULE-04, Q-15 |
| M-05 | The system will dynamically calculate the deduction based on current fuel rates | Requirement | BR-03, FR-007, FR-008, RULE-06, Q-05, Q-06, Q-16 |
| M-06 | Any unused portion of the allowance will be paid out with the monthly salary | Requirement | FR-010, FR-018, RULE-03, Q-07, Q-08 |
| M-07 | Frontend setup for HR and Finance for deduction formulas and updating real-time fuel prices | Requirement | FR-008, FR-009, NFR-SEC-02 |
| M-08 | Concern: employees might avoid swiping to retain cash allowances | Constraint | BR-04, FR-014, Q-12, Q-17 |
| M-09 | RFID readers will be installed at both the KDC pickup point and the hospital | Decision | FR-005, IMP-07, Q-01 |
| M-10 | A manual adjustment portal for missed swipes due to honest mistakes | Requirement | FR-011, FR-013, Q-10 |
| M-11 | Adjustment requests go through approval by supervisors or the transport coordinator | Requirement | FR-012, FR-013, RULE-05, Q-11 |
| M-12 | RFID integrated into the existing Employee ID Cards used for cafeteria and attendance | Decision | FR-004, NFR-INT-01, Q-09 |
| M-13 | Notifications on employees' dashboards whenever their card is swiped | Requirement | FR-015, FR-016, Q-13 |
| M-14 | Easy auditing of trip records; a comprehensive transaction trail for HR and Finance | Requirement | FR-016, FR-017, NFR-AUD-01, NFR-DAT-01, Q-18 |
| M-15 | The system must be fully operational by the first week of November (hospital opening) | Constraint | BR-06, §9.2, Q-14 |
| M-16 | Shahzad committed to a complete, testable build by the end of October | Decision | §9.2, §8.4 |
| M-17 | Shahzad to create a system design sketch | Action item | §9.2 |
| M-18 | Align with the Finance team on formula details | Action item | FR-009, Q-05 |
| M-19 | Present the finalised layout for management approval before development | Action item | §9.2 |

# Appendix B. Requirement traceability
| Requirement | Source (M-NN) | Impact items (IMP-NN) |
|---|---|---|
| FR-001 | M-02 | IMP-03, IMP-15 |
| FR-002 | M-02 | IMP-01, IMP-21, IMP-27 |
| FR-003 | M-04, M-09 | IMP-07, IMP-18 |
| FR-004 | M-12 | IMP-08, IMP-16, IMP-24 |
| FR-005 | M-04, M-09 | IMP-07, IMP-17 |
| FR-006 | M-04, M-09 | IMP-13, IMP-14, IMP-19 |
| FR-007 | M-03, M-05 | IMP-02, IMP-13, IMP-19 |
| FR-008 | M-05, M-07 | IMP-12, IMP-20 |
| FR-009 | M-07, M-18 | IMP-12, IMP-21 |
| FR-010 | M-06 | IMP-01, IMP-13, IMP-23, IMP-25 |
| FR-011 | M-10 | IMP-11, IMP-22, IMP-24 |
| FR-012 | M-11 | IMP-04, IMP-22, IMP-27 |
| FR-013 | M-10, M-11 | IMP-04, IMP-12, IMP-22 |
| FR-014 | M-08 | IMP-03, IMP-09, IMP-12, IMP-26 |
| FR-015 | M-13 | IMP-11 |
| FR-016 | M-13, M-14 | IMP-11 |
| FR-017 | M-14 | IMP-03, IMP-12 |
| FR-018 | M-06 | IMP-10, IMP-23 |

# Appendix C. Changes in v0.2
| Change | Where | Reason |
|---|---|---|
| Added the working-days issue: 25 (Nov) and 27 (Dec) Monday–Saturday days vs the 24-day basis | §1.2, RULE-01, FR-010, Q-07 | Review RV-01 |
| Q-07 rewritten with three options and marked blocking | §10 | Review RV-01 |
| Direction rule linked to new Q-15 | FR-003, Q-15 | Review RV-03 |
| Q-14 marked blocking (first payroll month is partial for everyone) | §10 | Review RV-04 |
| New Q-16: fuel price entered late | §10 | Review RV-05 |
| New Q-17: shift coverage (night, 12-hour, on-call) | §10, FR-014 | Review RV-06 |
| FR-014 priority flagged for SA decision | FR-014 | Review RV-07 |
| Q-05 extended: editable parameters vs free formula | §10 | Review RV-08 |
| FR-018 AC3: late adjustments after the register is sent | FR-018 | Review RV-09 |
| 2-minute repeat-swipe interval labelled as a proposal | FR-006 | Review RV-11 |
| Maker must differ from checker | NFR-SEC-02 | Review RV-12 |
| New Q-18: retention of swipe data | §10, NFR-DAT-01 | Review RV-16 |
| Phased go-live labelled as a proposal, not agreed | §8.4 | Review RV-17 |
| New impact items IMP-24 (card replacement), IMP-25 (final settlement), IMP-26 (shift roster) | §8.1, §8.2 | Review §4.2 |

Not changed; needs answers from stakeholders or the SA: RV-02 (eligibility, Q-03), RV-10 (schema not yet indexed), RV-13 and RV-14 (meeting date, attendees, business owner), RV-15 (table name, at design).

# Appendix D. Changes in v0.3
| Change | Where | Reason |
|---|---|---|
| New AC3: days on a shift with no bus, or with approved own transport, are not counted as missed trips | FR-014 | Review v2 RV-18 |
| New AC3: escalation when the approver doesn't act within N working days or is on leave | FR-012 | Review v2 RV-19 |
| AC3 aligned with the three Q-07 options | FR-010 | Review v2 RV-20 |
| Q-15 added to the trip rule's source | RULE-04 | Review v2 RV-21 |
| New AC4: first decision wins when more than one approver can act | FR-013 | Review v2 RV-22 |
| New impact item IMP-27: leave records | §8.2, Appendix B | Review v2 §4.2 |

Not changed; still waiting on stakeholders or the SA: RV-01 (Q-07), RV-02 (Q-03), RV-03 (Q-15), RV-07 (FR-014 priority), RV-10 (schema), RV-13, RV-14, and the observations RV-15, RV-23, RV-24, RV-25.

