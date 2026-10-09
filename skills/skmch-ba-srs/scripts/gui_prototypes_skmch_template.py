"""SKMCH GUI prototype generator - styled on the SKMCH APEX template (PA Performance S07APX00340).
Usage: python gen2.py <out_dir>   -> writes one HTML per screen; render with headless Chromium."""
import os,sys
OUT=sys.argv[1]
CSS="""
*{box-sizing:border-box}body{margin:0;background:#dfe3e6;font-family:'Segoe UI',Arial,sans-serif;font-size:12px;color:#222}
.app{width:1500px;background:#fff;border:1px solid #c9ced3;border-radius:6px;overflow:hidden}
.tbar{background:#1f78a8;color:#fff;font-weight:700;font-size:15px;padding:9px 12px;border-bottom:3px solid #16648d}
.body{padding:14px 14px 10px;background:#f4f5f6}
.tabs{display:flex;gap:4px;background:#f0f1f2;padding:6px 6px 0;border-radius:4px 4px 0 0}
.tab{padding:9px 13px;font-weight:600;font-size:13px;color:#222;border-radius:4px 4px 0 0}.tab.on{background:#1f78a8;color:#fff}
.reg{background:#fff;border:1px solid #d4d8dc;border-radius:4px;margin-bottom:12px;overflow:hidden}
.rh{background:#57768f;color:#fff;font-weight:700;font-size:14px;padding:7px 12px}
.rb{padding:10px 12px}
.row{display:flex;gap:10px;align-items:flex-start}
table.g{border-collapse:collapse;width:100%}
.g th{font-weight:700;text-align:left;padding:9px 8px;border:1px solid #e1e4e7;background:#fff;font-size:12px}
.g td{padding:7px 8px;border:1px solid #e6e8ea;vertical-align:middle}
.g .c{text-align:center}.g .cy{background:#eaf6ec}.g tr.hl td{background:#e3edf7}.g td.err{background:#f8c6c9}
.g td.lnk,.lnk{color:#1f6fa0;font-weight:600}
.scale{width:300px;border:1px solid #e1e4e7;background:#fff}.scale .sh{background:#f9ad57;font-weight:700;padding:10px}
.scale div.i{display:flex;justify-content:space-between;padding:8px 12px;border-bottom:1px solid #f0f0f0}
.sum{display:flex;justify-content:flex-end;gap:26px;background:#eefaf2;border:1px solid #9fd8b4;border-radius:4px;padding:10px 16px;font-size:13px;margin-top:8px}
.sum b{color:#1b7a3a}
.fg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 18px}
.f label{display:block;font-size:11px;font-weight:600;color:#555;margin-bottom:2px}.f label.req:after{content:' *';color:#c8102e}
.v{border:1px solid #e1e4e7;background:#f7f8f9;padding:5px 7px;min-height:27px}
.in{border:1px solid #aab3bb;background:#fff;padding:5px 7px;min-height:27px}.in.err{background:#f8c6c9;border-color:#e57373}
.sel:after{content:'▾';float:right;color:#666}.ta{min-height:52px}.hint{color:#9aa3ab}
.btns{display:flex;justify-content:flex-end;gap:6px;padding:8px 0 2px}
.b{padding:7px 13px;font-weight:700;font-size:12px;border-radius:2px;color:#fff;display:inline-flex;gap:6px;align-items:center}
.b.pv{background:#7cc4f5;color:#123}.b.sv{background:#1e8a3c}.b.ex{background:#c8102e}.b.sb{background:#1f78a8}.b.rt{background:#ef8a17}.b.df{background:#fff;color:#333;border:1px solid #aab3bb}
.chip{display:inline-block;border-radius:3px;padding:2px 8px;font-size:11px;font-weight:700;color:#fff}
.route{display:flex;gap:6px;align-items:center;flex-wrap:wrap}.st{border:1px solid #c9ced3;padding:5px 10px;border-radius:3px;background:#fff}
.st.d{background:#eaf6ec;border-color:#7cc49a}.st.c{background:#fff3e0;border-color:#ef8a17;font-weight:700}
.msg{background:#f8c6c9;border:1px solid #e57373;color:#8b0000;padding:7px 10px;border-radius:3px;margin-bottom:10px;font-weight:600}
.info{background:#fff8e1;border:1px solid #f3d27a;padding:7px 10px;border-radius:3px;margin:8px 0;font-size:12px}
.radio span{margin-right:18px}.radio i{display:inline-block;width:12px;height:12px;border:2px solid #555;border-radius:50%;vertical-align:-2px;margin-right:5px}.radio i.on{border-color:#1f78a8;background:radial-gradient(#1f78a8 45%,#fff 50%)}
"""
IC={"pv":"🖶","sv":"💾","ex":"✖","sb":"➤","rt":"↩","df":""}
def btn(k,t): return f'<span class="b {k}">{IC[k]} {t}</span>'
def page(name,title,body,buttons):
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="app"><div class="tbar">{title}</div><div class="body">{body}<div class="btns">{"".join(btn(k,t) for k,t in buttons)}</div></div></div></body></html>'
    open(os.path.join(OUT,name+".html"),"w").write(html)
def reg(t,b,pad=True): return f'<div class="reg"><div class="rh">{t}</div><div class="{"rb" if pad else ""}">{b}</div></div>'
def tabs(names,on): return '<div class="tabs">'+''.join(f'<div class="tab {"on" if n==on else ""}">{n}</div>' for n in names)+'</div>'
def ro(l,v): return f'<div class="f"><label>{l}</label><div class="v">{v}</div></div>'
def chip(t,c): return f'<span class="chip" style="background:{c}">{t}</span>'
C={"pend":"#5c6bc0","draft":"#78909c","appr":"#ef8a17","ret":"#c8102e","hr":"#1e8a3c","done":"#14532d","nosup":"#6d4c41"}
EMP=ro("Employee No.","EMP-TEST-0001")+ro("Employee Name","Ali Raza")+ro("Designation","Staff Nurse")+ro("Department","Nursing")+ro("Joining Date","26-Apr-2026")+ro("Probation Period","26-Apr-2026 to 25-Oct-2026")+ro("Evaluator","EMP-TEST-0100 · Nadia Khan")+ro("Evaluation No.","PEV-2026-000123")
EMPREG=reg("Employee Information",f'<div class="fg">{EMP}</div>')
SCALE='<div class="scale"><div class="sh">Rating Scale</div>'+''.join(f'<div class="i"><span>{a}</span><b>{b}</b></div>' for a,b in [("Very Low",1),("Low",2),("Medium",3),("High",4),("Very High",5)])+'</div>'
# ---------------- Probation evaluation screens (form = Assignments / Training Needs / Recommendation) ----------------
TABS=["Evaluation Criteria","Assignments","Training Needs","Recommendation"]
T="S07APX0XXXX"  # APEX page code to be assigned
CRIT=[("Job Knowledge","Has the knowledge and skills to perform the job competently.",5),
 ("Quality of Work","Work is accurate, thorough and meets required standards.",None),
 ("Punctuality &amp; Attendance","Reports on time; attendance meets policy.",5),
 ("Teamwork &amp; Communication","Works well with colleagues; communicates clearly.",4),
 ("Patient / Customer Care","Shows courtesy and care towards patients and customers.",4),
 ("Policy Compliance","Follows hospital policies, SOPs and safety rules.",5)]
def crit_grid(edit=True,missing=True):
    rows=""
    for i,(p,d,r) in enumerate(CRIT):
        err=missing and r is None
        val='' if r is None else r
        cell=f"<div class='in sel' style='min-height:24px;text-align:left'>{val}</div>" if edit else val
        rem='<div class="in" style="min-height:24px"></div>' if edit else ''
        rows+=f'<tr class="{"hl" if i==0 else ""}"><td class="{"err" if err else ""}">{p} <span style="color:#c8102e">*</span></td><td>{d}</td><td class="c cy">{cell}</td><td style="width:30%">{rem}</td></tr>'
    return f'<table class="g"><tr><th style="width:190px">Parameter</th><th>Description</th><th class="c cy" style="width:90px">Rating</th><th>Remarks (if any)</th></tr>{rows}</table>'
ASSIGN=[("Managed admission and discharge documentation for the ward",5),
        ("Completed medication-administration competency assessment",None),
        ("Participated in the quarterly infection-control audit",4),
        ("Covered night shifts independently after orientation",4),
        ("Trained new staff on the HIS nursing documentation module",5)]
def assign_grid(edit=True,missing=True):
    rows=""
    for i,(a,r) in enumerate(ASSIGN,1):
        err=missing and r is None
        if edit:
            desc=f'<div class="in">{a}</div>'; rat=f"<div class='in sel' style='min-height:24px;text-align:left'>{'' if r is None else r}</div>"; rem='<div class="in" style="min-height:24px"></div>'
        else:
            desc=a; rat='' if r is None else r; rem=''
        rows+=f'<tr class="{"hl" if i==1 else ""}"><td class="c" style="width:40px">{i}</td><td>{desc}</td><td class="c cy {"err" if err else ""}" style="width:95px">{rat}</td><td style="width:30%">{rem}</td></tr>'
    add='<div style="padding:8px 0 0"><span class="b sb">＋ Add Assignment</span></div>' if edit else ''
    return f'<table class="g"><tr><th class="c">#</th><th>Assignment Completed During Probationary Period <span style="color:#c8102e">*</span></th><th class="c cy">Rating (1–5)</th><th>Remarks (if any)</th></tr>{rows}</table>'+add
def summary(t,o): return f'<div class="sum"><span>Total Score: <b>{t}</b></span><span>Obtained Score: <b>{o}</b></span><span>Performance %: <b>{round(o*100/t,2)}</b></span></div>'
TRN=[("Advanced Cardiac Life Support (ACLS) certification","Before confirmation review"),("HIS nursing documentation – advanced module",""),("Time management and shift handover communication","")]
def training_grid(edit=True):
    rows="".join(f'<tr><td class="c" style="width:40px">{i}</td><td>{"<div class=in>"+a+"</div>" if edit else a}</td><td style="width:35%">{"<div class=in>"+b+"</div>" if edit else b}</td></tr>' for i,(a,b) in enumerate(TRN,1))
    add='<div style="padding:8px 0 0"><span class="b sb">＋ Add Training Need</span></div>' if edit else ''
    return f'<table class="g"><tr><th class="c">#</th><th>Assessed Training Need</th><th>Remarks</th></tr>{rows}</table>'+add
EVID=[("absence_record_aug-sep.pdf","Attendance record showing 6 unplanned absences","EMP-TEST-0100"),("incident_report_IR-TEST-014.pdf","Documentation error incident – corrective action given","EMP-TEST-0100")]
def evidence_grid(edit=True):
    rows="".join(f'<tr><td>📎 {a}</td><td>{b}</td><td>{c}</td>{"<td class=lnk>Remove</td>" if edit else ""}</tr>' for a,b,c in EVID)
    add='<div style="padding:8px 0 0"><span class="b sb">＋ Attach Evidence</span></div>' if edit else ''
    return f'<table class="g"><tr><th>File</th><th>Description</th><th>Attached By</th>{"<th></th>" if edit else ""}</tr>{rows}</table>'+add
REASONS="1. Six unplanned absences in Aug–Sep 2026 (attendance record attached).\n2. One documentation error incident (IR-TEST-014); corrective action given and improvement seen.\n3. Clinical skills satisfactory; needs more time to show consistent attendance."
def recommend_block(edit=True,extend=True):
    cls="in" if edit else "v"
    return ('<div class="f" style="margin-bottom:8px"><label class="req">Recommendation</label><div class="radio" style="padding:5px 0">'
      f'<span><i class="{"" if extend else "on"}"></i>Confirm</span><span><i class="{"on" if extend else ""}"></i>Extend Probation</span><span><i></i>Not to Confirm</span></div></div>'
      f'<div class="fg"><div class="f"><label class="req">Extend by (days)</label><div class="{cls}">90</div></div></div>'
      '<div class="f" style="margin-top:8px"><label class="req">Specific Reasons and Observations <span style="font-weight:400;color:#777">(mandatory if not recommended for confirmation)</span></label>'
      f'<div class="{cls} ta" style="white-space:pre-line;min-height:70px">{REASONS}</div></div>')
TRACK='<div class="info">ℹ Reasons, observations and evidence are mandatory when the recommendation is <b>Extend Probation</b> or <b>Not to Confirm</b>.</div>'

# 1 Pending tasks
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026","15",chip("EVALUATION PENDING",C["pend"])),
      ("EMP-TEST-0002","Sara Ahmed","Pharmacy","18-Oct-2026","8",chip("DRAFT",C["draft"])),
      ("EMP-TEST-0003","Omar Farooq","Radiology","14-Oct-2026","4",chip("RETURNED",C["ret"]))]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td class="c">{e}</td><td>{s}</td><td class="lnk">Open ›</td></tr>' for i,(a,b,c,d,e,s) in enumerate(rows))
page("01_pending_tasks","My Pending Tasks | Probation Evaluation | EMP-TEST-0100 | Nadia Khan",
 reg("Probation Evaluations Assigned to Me",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th class="c">Days Left</th><th>Status</th><th>Action</th></tr>{tr}</table>',False)
 +'<div class="sum"><span>Total: <b>3</b></span><span>Returned: <b style="color:#c8102e">1</b></span><span>Due within 7 days: <b style="color:#ef8a17">1</b></span></div>'
 +'<div class="info">Tasks are created automatically 15 days before the probation end date and replace the Excel evaluation form sent with the probation-ending alert.</div>',[("ex","Exit")])

# 2 Assignments tab
page("02_evaluation_criteria",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Evaluation Criteria")
 +reg("Probation Assessment",'<div class="msg">Submit blocked: “Quality of Work” rating is mandatory.</div><div class="row"><div style="flex:1">'+crit_grid()+'</div>'+SCALE+'</div>'+summary(30,23))
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 3 Assignments tab
page("03_evaluation_assignments",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Assignments")
 +reg("Assignments Completed During Probationary Period",'<div class="msg">Submit blocked: rating is mandatory for every assignment (row 2).</div><div class="row"><div style="flex:1">'+assign_grid()+'</div>'+SCALE+'</div>'+summary(25,18))
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 3 Training needs tab
page("04_evaluation_training_needs",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Training Needs")
 +reg("Employee's Assessed Training Needs",training_grid())
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 4 Recommendation tab
page("05_evaluation_recommendation",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Recommendation")
 +reg("Evaluator Recommendation",recommend_block())
 +reg("Evidence (attachments)",evidence_grid())+TRACK
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 5 Approver
ASSIGN[1]=("Completed medication-administration competency assessment",3)
CRIT[1]=("Quality of Work","Work is accurate, thorough and meets required standards.",3)
route='<div class="route"><span class="st d">✔ Evaluator · Submitted 15-Oct-2026</span>➜<span class="st c">● Level 1 · HOD Nursing (you)</span>➜<span class="st">Level 2 · Director Nursing</span>➜<span class="st">HR Department</span></div>'
page("06_approver",f"Probation Evaluation – Approval {T} | EMP-TEST-0001 | Ali Raza",
 reg("Approval Routing",route)+EMPREG+tabs(TABS,"Evaluation Criteria")
 +reg("Probation Assessment (read-only)",'<div class="row"><div style="flex:1">'+crit_grid(False,False)+'</div>'+SCALE+'</div>'+summary(30,26))
 +reg("Approver Decision",'<div class="fg"><div class="f"><label>Evaluator Recommendation</label><div class="v">Extend Probation – 90 days</div></div><div class="f" style="grid-column:span 3"><label>Reasons / Evidence</label><div class="v">2 reasons recorded · 2 evidence files (see Recommendation tab)</div></div></div><div class="f" style="margin-top:8px"><label>Approver Comments (mandatory for Return)</label><div class="in ta"></div></div>')
 ,[("pv","Preview"),("rt","Return to Evaluator"),("sv","Approve"),("ex","Exit")])

# 6 Hierarchy setup
hr=[("Nursing","1","Head of Department","DEPARTMENT_HEAD","Y"),("Nursing","2","Director Nursing","Named employee","Y"),("Pharmacy","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All Departments)","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All Departments)","2","Department Manager","DEPARTMENT_MANAGER","N")]
tr="".join(f'<tr><td><div class="in sel">{a}</div></td><td class="c" style="width:80px"><div class="in">{b}</div></td><td><div class="in sel">{c}</div></td><td>{d}</td><td class="c">{chip("Active","#1e8a3c") if e=="Y" else chip("Inactive","#9aa3ab")}</td></tr>' for a,b,c,d,e in hr)
page("07_hierarchy_setup",f"Probation Approval Hierarchy Setup {T}",
 '<div class="info">Levels are applied in order on Submit. Approver on leave → acting-for person (HRD.ACTING_FOR), if confirmed by HR.</div>'
 +reg("Hierarchy Levels",f'<div style="padding:8px 12px"><span class="b sb">＋ Add Row</span></div><table class="g"><tr><th>Department</th><th class="c">Level</th><th>Approver Role</th><th>Resolved From</th><th class="c">Status</th></tr>{tr}</table>',False)
 ,[("sv","Save"),("ex","Exit")])

# 7 HR queue
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026","Extend 90 days","L2 Director Nursing","84.00","2"),("EMP-TEST-0004","Hina Malik","Administration","30-Oct-2026","Confirm","L1 HOD Admin","92.00","0"),("EMP-TEST-0008","Bilal Aslam","IT","02-Nov-2026","Not to Confirm","L2 Director IT","52.00","3")]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td><b>{e}</b></td><td>{f}</td><td class="c cy">{g}</td><td class="c">{h}</td><td>{chip("FORWARDED TO HR",C["hr"])}</td><td class="lnk">Process ›</td></tr>' for i,(a,b,c,d,e,f,g,h) in enumerate(rows))
page("08_hr_queue","HR – Completed Probation Evaluations | Human Resource Department",
 reg("Evaluations Awaiting HR Decision",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th>Recommendation</th><th>Final Approval</th><th class="c cy">Performance %</th><th class="c">Evidence</th><th>Status</th><th>Action</th></tr>{tr}</table>',False)
 ,[("ex","Exit")])

# 8 HR decision
route2='<div class="route"><span class="st d">✔ Evaluator · 15-Oct-2026</span>➜<span class="st d">✔ L1 HOD Nursing · 16-Oct-2026</span>➜<span class="st d">✔ L2 Director Nursing · 20-Oct-2026</span>➜<span class="st c">● HR Department</span></div>'
page("09_hr_decision",f"HR Decision – Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 reg("Approval Routing",route2)+EMPREG
 +reg("HR Finalization",summary(55,47)
  +'<div class="fg" style="margin-top:10px"><div class="f"><label>Evaluator Recommendation</label><div class="v">Extend Probation – 90 days</div></div><div class="f" style="grid-column:span 3"><label>Reasons and Observations</label><div class="v">Six unplanned absences (evidence attached); one documentation incident, corrected.</div></div></div>'
  +'<div class="f" style="margin:10px 0 8px"><label class="req">HR Decision</label><div class="radio" style="padding:5px 0"><span><i></i>Confirm Employment</span><span><i class="on"></i>Extend Probation</span><span><i></i>Other (per HR policy)</span></div></div>'
  '<div class="fg"><div class="f"><label class="req">Extension Days</label><div class="in">90</div></div><div class="f"><label class="req">Extension Reason</label><div class="in sel">Attendance not satisfactory</div></div><div class="f"><label>New Probation End</label><div class="v">23-Jan-2027</div></div><div class="f"><label>Training Needs</label><div class="v">3 recorded</div></div></div>'
  '<div class="f" style="margin-top:8px"><label>HR Remarks</label><div class="in ta"></div></div><div class="info">On Finalize: Confirm sets the probation record to Confirmed (confirmation date and allowances follow); Extend updates the probation period.</div>')
 ,[("pv","Preview"),("sv","Finalize"),("ex","Exit")])

# 9 Monitoring
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026",chip("PENDING APPROVAL – L2",C["appr"]),"Director Nursing",""),
 ("EMP-TEST-0005","Asad Iqbal","Finance","08-Oct-2026",chip("DRAFT",C["draft"]),"EMP-TEST-0110",chip("OVERDUE","#c8102e")),
 ("EMP-TEST-0006","Zoya Haider","Laboratory","20-Oct-2026",chip("NO SUPERVISOR",C["nosup"]),"HR exception list",'<span class="lnk">Assign Evaluator ›</span>'),
 ("EMP-TEST-0004","Hina Malik","Administration","30-Oct-2026",chip("FORWARDED TO HR",C["hr"]),"HR",""),
 ("EMP-TEST-0009","Usman Tariq","Nursing","01-Oct-2026",chip("COMPLETED",C["done"]),"—","")]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td>{s}</td><td>{w}</td><td>{fl}</td></tr>' for i,(a,b,c,d,s,w,fl) in enumerate(rows))
hist=[("10-Oct-2026 02:00","SYSTEM","Queue created","—",chip("EVALUATION PENDING",C["pend"])),("12-Oct-2026 10:15","EMP-TEST-0100","Saved","—",chip("DRAFT",C["draft"])),("15-Oct-2026 09:40","EMP-TEST-0100","Submitted","—",chip("PENDING APPROVAL – L1",C["appr"])),("16-Oct-2026 14:05","EMP-TEST-0200","Approved","Agreed",chip("PENDING APPROVAL – L2",C["appr"]))]
th="".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a,b,c,d,e in hist)
page("10_monitoring",f"Probation Evaluation Monitoring {T} | Human Resource Department",
 reg("Search Criteria",'<div class="fg" style="grid-template-columns:repeat(5,1fr)"><div class="f"><label>Status</label><div class="in sel">All</div></div><div class="f"><label>Department</label><div class="in sel">All</div></div><div class="f"><label>Evaluator</label><div class="in"></div></div><div class="f"><label>Probation End From</label><div class="in">01-Oct-2026</div></div><div class="f"><label>To</label><div class="in">31-Oct-2026</div></div></div>')
 +reg("Probation Evaluations",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th>Status</th><th>Currently With</th><th>Flag / Action</th></tr>{tr}</table>',False)
 +'<div class="sum" style="margin-bottom:12px"><span>Open: <b>42</b></span><span>Pending Approval: <b style="color:#ef8a17">18</b></span><span>Overdue: <b style="color:#c8102e">3</b></span><span>No Supervisor: <b style="color:#6d4c41">2</b></span><span>With HR: <b>7</b></span></div>'
 +reg("Status History – EMP-TEST-0001 · Ali Raza (read-only)",f'<table class="g"><tr><th>Date / Time</th><th>By</th><th>Action</th><th>Comments</th><th>New Status</th></tr>{th}</table>',False)
 ,[("pv","Preview"),("ex","Exit")])
print("ok")
