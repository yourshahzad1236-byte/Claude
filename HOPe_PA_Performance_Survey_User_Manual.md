# HOPe PA Performance Survey – User Manual

## 1. Purpose

This user manual explains the steps to complete the **HOPe PA Performance Survey** in the Hospital Management Information System (HMIS) – **Human Resources** module. It describes each screen (tab) with its screenshot, fields, buttons and the **business rules** applied on that screen.

## 2. Process

1. HR distributes the Performance Appraisal. The task is generated in the user's **Pending Queue**.
2. The user opens the task and lands on the **PA Performance** screen. The screen title shows: `PA Performance <Appraisal No> | <Employee No> | <Employee Name>`.
3. The user completes the tabs (in any order), then goes to **Finalization** and forwards the appraisal.
4. Once forwarded, the appraisal is removed from the user's Pending Queue and appears in the Pending Queue of the next appraiser / HR.

### Screens (Tabs)

| # | Screen | Purpose |
|---|---|---|
| 1 | Discussion Points | Answer the discussion questions. |
| 2 | Peer Nomination | Nominate the required peers per category. |
| 3 | Medical Education/Research | Review/complete CPD (education/research) details. |
| 4 | Finalization | Check completion, add remarks, forward the appraisal. |

> Which tabs appear depends on the user's tab rights for the appraisal. *Behavioral Assessment* and *Management Traits* tabs are part of the same page but are displayed only when enabled for the appraisal type/role. Their rules are listed in section 8.

### General rules (apply to all screens)

- **Tab rights:** only the tabs assigned to the user for this appraisal are shown; **Finalization** is always available.
- **Role-based screen:** for the **self (appraisee)** role, the remarks section is titled **Appraisee Remarks** and the *To Previous Appraiser* remarks option is hidden. Other appraisers see **Add your Remarks**.
- **Save:** entered data must be saved using **Save** before leaving the screen; unsaved changes are lost on Reset.
- **Session timeout:** the session times out after about 30 minutes of inactivity; save frequently.
- **Switching tabs:** the system may show a warning (see section 9) but allows the user to continue to another tab; incomplete tabs are marked on the Finalization screen and must be completed before forwarding.

---

## 3. Screen: Discussion Points

![Discussion Points](images/discussion-points.png)

### Fields

| Field | Description |
|---|---|
| Sr# | Serial number of the question. |
| Description | The discussion question. |
| 2026 (current year) | Editable answer box for the current year. |
| 2025 / 2024 | Answers of previous years – read-only, for reference. |

Questions: (1) professional experience over the past year, (2) most difficult elements of the job, (3) elements that interest you most, (4) most important aims and tasks in the coming year, (5) actions you could take to improve your performance, (6) actions your supervisor could take to improve your performance.

### Buttons

**Save**, **Add Row**, **Reset**, **Actions / Grid Settings** (grid view options), **Edit** (switch grid to edit mode).

### Steps

1. Click the current-year cell of a question and type the answer.
2. Repeat for all questions.
3. Click **Save**.

### Business rules

- Only the **current-year** column is editable; previous-year columns are read-only.
- Questions marked required must be answered. A question with a **missing answer is highlighted in red** after Save.
- If **all** questions are empty, the tab is flagged as incomplete on the Finalization screen.
- The tab may be left incomplete when switching to another tab (a "Required Information Missing" message appears), but the appraisal **cannot be forwarded** until all highlighted answers are completed.
- For the self role, the answers are entered by the employee; other appraisers view them.

---

## 4. Screen: Peer Nomination

![Peer Nomination](images/peer-nomination.png)

### Fields

**Peers to be Nominated (left)**

| Field | Description |
|---|---|
| Description | Peer category. |
| Required No. of Peers | Number of peers that must be nominated for the category. |
| Not Applicable | Tick if nomination is not applicable for the category. |

Categories and required peers: Pharmacist/Technician/Technologist – 2; Consultant/Senior Instructors/Ancillary Health Practitioners – 6; Nurses – 4; Health Care Assistant/Secretary – 2.

**List of Employees to Choose Peers From (right)**

| Field | Description |
|---|---|
| Name, Employee Code, Designation, Department | Details of the nominated (internal) peers. |
| Name, Contact Details, Email | Details of external peers, where applicable. |
| Remarks | Shown when the category is marked *Not Applicable*. |
| Delete | Removes a nominated peer. |

### Buttons

**Refresh**, **Save**, **Delete**.

### Steps

1. Select a category in the left panel.
2. Choose the required number of peers from the list on the right (or add external peers).
3. If the category does not apply, tick **Not Applicable** and confirm.
4. Click **Save**; click **Refresh** to see the updated status.

### Business rules

- The number of nominated peers must match **Required No. of Peers** for each category unless it is marked **Not Applicable**.
- A category row highlighted in **red** is incomplete.
- Ticking **Not Applicable** shows the confirmation *"Are you sure you want to mark this as not applicable? All previous data will be lost."* – on confirmation, the peers already nominated for that category are removed and the employee list is hidden.
- Unticking **Not Applicable** brings the employee list back so peers can be nominated again.
- **Delete** asks for confirmation (*"Are you sure, you want to delete the selected record?"*); an unsaved new row is removed without confirmation.
- Peer nomination must be complete (or Not Applicable) before forwarding.

---

## 5. Screen: Medical Education/Research

> [Screenshot: Medical Education/Research tab – to be added]

This tab shows the employee's **Continuing Professional Development (CPD) – Medical Education/Research** details loaded inside the screen from the CPD page.

### Steps

1. Open the **Medical Education/Research** tab.
2. Review or enter the CPD/education/research entries shown.
3. Save the entries.

### Business rules

- If the CPD entries are **zero / not entered**, the system shows the alert **"Zero Values Detected – Highlighted fields have been entered as zero."** with the options **Review Values** (stay on the tab) or **Proceed to forward**.
- Choosing *Review Values* returns the user to this tab and marks it in error on the Finalization screen.
- The tab is checked when the appraisal is forwarded.

---

## 6. Screen: Finalization

> [Screenshot: Finalization tab – to be added]

### Fields

| Field | Description |
|---|---|
| Appraisers' Remarks – name | Name of the employee/appraiser. |
| Checklist | "Complete the item(s) below before forwarding to HR": Discussion Points, Peer Nomination, Medical Education/Research. Incomplete items are flagged. |
| Add your Remarks / Appraisee Remarks | Free-text remarks. |

### Buttons

| Button | Action |
|---|---|
| **To Previous Appraiser** | Returns the appraisal to the previous appraiser (shown only when applicable). |
| **Forward Appraisal to HR Department** | Validates all tabs and forwards the appraisal (label changes to the next stage where applicable). |
| **Preview** | Previews the appraisal before forwarding. |
| **Save** | Saves entered information. |
| **Exit** | Closes the screen. |

### Steps

1. Check that every item in the checklist is complete.
2. Enter remarks.
3. Click **Forward Appraisal…**.

### Business rules

- On forwarding, all allowed tabs are validated: Discussion Points, Peer Nomination, Medical Education/Research (and Behavioral Assessment / Management Traits if enabled).
- Tabs with missing required data are flagged on this screen and the user is taken back to the tab; the appraisal is **not forwarded** until they are complete.
- Zero values in Medical Education/Research show a confirmation (Review Values / Proceed to forward).
- Remarks are required where the screen asks for justification (*"Please provide justification"*).
- After a successful forward the appraisal leaves the user's Pending Queue.
- **Mark Deduction** and **Previous Year Deduction** buttons are shown only for the final authority role, not for the self role.

---

## 7. Quick Checklist

1. Open the task from the Pending Queue.
2. **Discussion Points:** answer all questions → Save.
3. **Peer Nomination:** nominate required peers (or Not Applicable) → Save.
4. **Medical Education/Research:** review entries.
5. **Finalization:** confirm checklist, add remarks, Forward.

---

## 8. Additional Screens (shown only when enabled)

**Behavioral Assessment** – grid of Parameter / Description with Current Year and Previous Year ratings. Shows Grade, Total Score, Obtained Score, Marks After Deduction, Performance %, and *Final Aggregate Rating (FAR) = Performance × 0.3 (30%)*. Rating values are selected per parameter; **Mark Deduction** / **Previous Year Deduction** are available to the final authority only. If the employee's role changed between Supervisory and Non-Supervisory this year, the screen shows a message that the previous-year rating must be viewed from reports.

**Management Traits** – "From the list of adjectives, choose the 4 that best describe you." **Rule:** exactly the maximum allowed (4) values must be selected; selecting more than 4 shows *"You have selected maximum allowed values"* and the extra selection is reverted; selecting fewer shows *"Kindly select maximum allowed values (4)"* with **Review Traits** / **Continue to Switch Tab**.

---

## 9. System Messages

| Message | Meaning | Options |
|---|---|---|
| Zero Values Detected – *Highlighted fields have been entered as zero. Please verify…* | Zero values entered (Behavioral / CPD). | Review Values · Continue to Switch Tab / Proceed to forward |
| Required Information Missing – *You may continue to other tabs; however, all highlighted fields must be completed before the form can be submitted.* | Mandatory data missing on the tab. | Review Missing Fields · Continue to Switch Tab |
| Management Traits – *Kindly select maximum allowed values (4)* | Wrong number of traits selected. | Review Traits · Continue to Switch Tab |
| Are you sure you want to mark this as not applicable? All previous data will be lost. | Not Applicable ticked on Peer Nomination. | Yes / No |
| Are you sure, you want to delete the selected record? | Deleting a nominated peer. | Yes / No |
| Unable to process delete action. Please refresh and try again. | Delete failed. | Refresh the page and retry |
