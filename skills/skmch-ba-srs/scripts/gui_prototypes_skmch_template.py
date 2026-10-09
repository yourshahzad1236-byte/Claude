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
        val=('' if r is None else r)
        rem='<div class="in" style="min-height:24px"></div>' if edit else ''
        rows+=f'<tr class="{"hl" if i==0 else ""}"><td class="{"err" if err else ""}">{p} <span style="color:#c8102e">*</span></td><td>{d}</td><td class="c cy">{val if not edit else f"<div class=\'in sel\' style=\'min-height:24px;text-align:left\'>{val}</div>"}</td><td style="width:30%">{rem}</td></tr>'
    g=f'<table class="g"><tr><th style="width:190px">Parameter</th><th>Description</th><th class="c cy" style="width:90px">Rating</th><th>Remarks (if any)</th></tr>{rows}</table>'
    return g
def summary(t,o): return f'<div class="sum"><span>Total Score: <b>{t}</b></span><span>Obtained Score: <b>{o}</b></span><span>Performance %: <b>{round(o*100/t,2)}</b></span></div>'
TABS=["Evaluation Criteria","Recommendation","Approval History","Finalization"]
T="S07APX0XXXX"  # APEX page code to be assigned

# 1 Pending tasks
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026","15",chip("EVALUATION PENDING",C["pend"])),
      ("EMP-TEST-0002","Sara Ahmed","Pharmacy","18-Oct-2026","8",chip("DRAFT",C["draft"])),
      ("EMP-TEST-0003","Omar Farooq","Radiology","14-Oct-2026","4",chip("RETURNED",C["ret"]))]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td class="c">{e}</td><td>{s}</td><td class="lnk">Open ›</td></tr>' for i,(a,b,c,d,e,s) in enumerate(rows))
page("01_pending_tasks",f"My Pending Tasks | Probation Evaluation | EMP-TEST-0100 | Nadia Khan",
 reg("Probation Evaluations Assigned to Me",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th class="c">Days Left</th><th>Status</th><th>Action</th></tr>{tr}</table>',False)
 +'<div class="sum"><span>Total: <b>3</b></span><span>Returned: <b style="color:#c8102e">1</b></span><span>Due within 7 days: <b style="color:#ef8a17">1</b></span></div>'
 +'<div class="info">Tasks are created automatically 15 days before the probation end date.</div>',[("ex","Exit")])

# 2 Evaluation form - criteria tab
page("02_evaluation_form",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Evaluation Criteria")
 +reg("Probation Assessment",'<div class="msg">Submit blocked: “Quality of Work” rating is mandatory.</div><div class="row"><div style="flex:1">'+crit_grid()+'</div>'+SCALE+'</div>'+summary(30,23))
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 2b recommendation tab
page("03_evaluation_recommendation",f"Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 EMPREG+tabs(TABS,"Recommendation")
 +reg("Evaluator Recommendation",'<div class="f" style="margin-bottom:8px"><label class="req">Recommendation</label><div class="radio" style="padding:5px 0"><span><i class="on"></i>Confirm</span><span><i></i>Extend Probation</span><span><i></i>Not to Confirm</span></div></div>'
  '<div class="fg"><div class="f"><label>Extend by (days)</label><div class="in hint">enabled only for Extend</div></div><div class="f" style="grid-column:span 3"><label>Attachment</label><div class="in">📎 evaluation_form_signed.pdf</div></div></div>'
  '<div class="f" style="margin-top:8px"><label class="req">Evaluator Comments</label><div class="in ta">Performs duties well and meets the expectations of the role. Recommend confirmation.</div></div>')
 ,[("pv","Preview"),("sv","Save as Draft"),("sb","Submit"),("ex","Exit")])

# 3 Approver
route='<div class="route"><span class="st d">✔ Evaluator · Submitted 15-Oct-2026</span>➜<span class="st c">● Level 1 · HOD Nursing (you)</span>➜<span class="st">Level 2 · Director Nursing</span>➜<span class="st">HR Department</span></div>'
CRIT[1]=("Quality of Work","Work is accurate, thorough and meets required standards.",3)
page("04_approver",f"Probation Evaluation – Approval {T} | EMP-TEST-0001 | Ali Raza",
 reg("Approval Routing",route)+EMPREG+tabs(["Evaluation Criteria","Recommendation","Approval History"],"Evaluation Criteria")
 +reg("Probation Assessment (read-only)",'<div class="row"><div style="flex:1">'+crit_grid(False,False)+'</div>'+SCALE+'</div>'+summary(30,26))
 +reg("Approver Decision",'<div class="f"><label>Recommendation by Evaluator</label><div class="v" style="width:300px">Confirm</div></div><div class="f" style="margin-top:8px"><label>Approver Comments (mandatory for Return)</label><div class="in ta"></div></div>')
 ,[("pv","Preview"),("rt","Return to Evaluator"),("sv","Approve"),("ex","Exit")])

# 4 Hierarchy setup
hr=[("Nursing","1","Head of Department","DEPARTMENT_HEAD","Y"),("Nursing","2","Director Nursing","Named employee","Y"),("Pharmacy","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All Departments)","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All Departments)","2","Department Manager","DEPARTMENT_MANAGER","N")]
tr="".join(f'<tr><td><div class="in sel">{a}</div></td><td class="c" style="width:80px"><div class="in">{b}</div></td><td><div class="in sel">{c}</div></td><td>{d}</td><td class="c">{chip("Active","#1e8a3c") if e=="Y" else chip("Inactive","#9aa3ab")}</td></tr>' for a,b,c,d,e in hr)
page("05_hierarchy_setup",f"Probation Approval Hierarchy Setup {T}",
 '<div class="info">Levels are applied in order on Submit. Approver on leave → acting-for person (HRD.ACTING_FOR), if confirmed by HR.</div>'
 +reg("Hierarchy Levels",f'<div style="padding:8px 12px"><span class="b sb">＋ Add Row</span></div><table class="g"><tr><th>Department</th><th class="c">Level</th><th>Approver Role</th><th>Resolved From</th><th class="c">Status</th></tr>{tr}</table>',False)
 ,[("sv","Save"),("ex","Exit")])

# 5 HR queue
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026","Confirm","L2 Director Nursing","86.67"),("EMP-TEST-0004","Hina Malik","Administration","30-Oct-2026","Extend 90 days","L1 HOD Admin","63.33"),("EMP-TEST-0008","Bilal Aslam","IT","02-Nov-2026","Confirm","L2 Director IT","90.00")]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td><b>{e}</b></td><td>{f}</td><td class="c cy">{g}</td><td>{chip("FORWARDED TO HR",C["hr"])}</td><td class="lnk">Process ›</td></tr>' for i,(a,b,c,d,e,f,g) in enumerate(rows))
page("06_hr_queue","HR – Completed Probation Evaluations | Human Resource Department",
 reg("Evaluations Awaiting HR Decision",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th>Recommendation</th><th>Final Approval</th><th class="c cy">Performance %</th><th>Status</th><th>Action</th></tr>{tr}</table>',False)
 ,[("ex","Exit")])

# 6 HR decision
route2='<div class="route"><span class="st d">✔ Evaluator · 15-Oct-2026</span>➜<span class="st d">✔ L1 HOD Nursing · 16-Oct-2026</span>➜<span class="st d">✔ L2 Director Nursing · 20-Oct-2026</span>➜<span class="st c">● HR Department</span></div>'
page("07_hr_decision",f"HR Decision – Probation Evaluation {T} | EMP-TEST-0001 | Ali Raza",
 reg("Approval Routing",route2)+EMPREG+tabs(["Evaluation Criteria","Recommendation","Approval History","Finalization"],"Finalization")
 +reg("HR Finalization",summary(30,26)+'<div class="f" style="margin:10px 0 8px"><label class="req">HR Decision</label><div class="radio" style="padding:5px 0"><span><i class="on"></i>Confirm Employment</span><span><i></i>Extend Probation</span><span><i></i>Other (per HR policy)</span></div></div>'
  '<div class="fg"><div class="f"><label>Extension Days</label><div class="in hint">only for Extend</div></div><div class="f"><label>Extension Reason</label><div class="in sel hint">Probation Reasons</div></div><div class="f"><label>Confirmation Date</label><div class="v">26-Oct-2026</div></div><div class="f"><label>Evaluator Recommendation</label><div class="v">Confirm</div></div></div>'
  '<div class="f" style="margin-top:8px"><label>HR Remarks</label><div class="in ta"></div></div><div class="info">On Finalize with Confirm, the probation record is set to Confirmed: confirmation date is updated and eligible allowances are queued.</div>')
 ,[("pv","Preview"),("sv","Finalize"),("ex","Exit")])

# 7 Monitoring
rows=[("EMP-TEST-0001","Ali Raza","Nursing","25-Oct-2026",chip("PENDING APPROVAL – L2",C["appr"]),"Director Nursing",""),
 ("EMP-TEST-0005","Asad Iqbal","Finance","08-Oct-2026",chip("DRAFT",C["draft"]),"EMP-TEST-0110",chip("OVERDUE","#c8102e")),
 ("EMP-TEST-0006","Zoya Haider","Laboratory","20-Oct-2026",chip("NO SUPERVISOR",C["nosup"]),"HR exception list",'<span class="lnk">Assign Evaluator ›</span>'),
 ("EMP-TEST-0004","Hina Malik","Administration","30-Oct-2026",chip("FORWARDED TO HR",C["hr"]),"HR",""),
 ("EMP-TEST-0009","Usman Tariq","Nursing","01-Oct-2026",chip("COMPLETED",C["done"]),"—","")]
tr="".join(f'<tr class="{"hl" if i==0 else ""}"><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td class="c">{d}</td><td>{s}</td><td>{w}</td><td>{fl}</td></tr>' for i,(a,b,c,d,s,w,fl) in enumerate(rows))
hist=[("10-Oct-2026 02:00","SYSTEM","Queue created","—",chip("EVALUATION PENDING",C["pend"])),("12-Oct-2026 10:15","EMP-TEST-0100","Saved","—",chip("DRAFT",C["draft"])),("15-Oct-2026 09:40","EMP-TEST-0100","Submitted","—",chip("PENDING APPROVAL – L1",C["appr"])),("16-Oct-2026 14:05","EMP-TEST-0200","Approved","Agreed",chip("PENDING APPROVAL – L2",C["appr"]))]
th="".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a,b,c,d,e in hist)
page("08_monitoring",f"Probation Evaluation Monitoring {T} | Human Resource Department",
 reg("Search Criteria",'<div class="fg" style="grid-template-columns:repeat(5,1fr)"><div class="f"><label>Status</label><div class="in sel">All</div></div><div class="f"><label>Department</label><div class="in sel">All</div></div><div class="f"><label>Evaluator</label><div class="in"></div></div><div class="f"><label>Probation End From</label><div class="in">01-Oct-2026</div></div><div class="f"><label>To</label><div class="in">31-Oct-2026</div></div></div>')
 +reg("Probation Evaluations",f'<table class="g"><tr><th>Employee No.</th><th>Employee Name</th><th>Department</th><th class="c">Probation End</th><th>Status</th><th>Currently With</th><th>Flag / Action</th></tr>{tr}</table>',False)
 +'<div class="sum" style="margin-bottom:12px"><span>Open: <b>42</b></span><span>Pending Approval: <b style="color:#ef8a17">18</b></span><span>Overdue: <b style="color:#c8102e">3</b></span><span>No Supervisor: <b style="color:#6d4c41">2</b></span><span>With HR: <b>7</b></span></div>'
 +reg("Status History – EMP-TEST-0001 · Ali Raza (read-only)",f'<table class="g"><tr><th>Date / Time</th><th>By</th><th>Action</th><th>Comments</th><th>New Status</th></tr>{th}</table>',False)
 ,[("pv","Preview"),("ex","Exit")])
print("ok")
