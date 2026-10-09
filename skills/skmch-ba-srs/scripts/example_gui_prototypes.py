import os,sys
OUT=sys.argv[1]
CSS="""
*{box-sizing:border-box}body{margin:0;background:#e9edf2;font-family:'Segoe UI',Arial,sans-serif;font-size:13px;color:#263238}
.app{width:1280px;background:#f5f7fa;border:1px solid #cfd8dc}
.top{height:46px;background:#0b5394;color:#fff;display:flex;align-items:center;padding:0 16px;gap:14px}
.top .logo{font-weight:700;font-size:15px}.top .sp{flex:1}.top .u{font-size:12px;opacity:.9}
.top .bell{background:#e53935;border-radius:10px;padding:1px 7px;font-size:11px;font-weight:700}
.wrap{display:flex}
.nav{width:200px;background:#263238;color:#cfd8dc;min-height:100%;padding:10px 0}
.nav div{padding:9px 18px;font-size:13px}.nav .on{background:#0b5394;color:#fff;border-left:4px solid #64b5f6}
.nav .h{font-size:10px;letter-spacing:1px;color:#78909c;padding-top:14px}
.main{flex:1;padding:16px 18px 20px}
.bc{font-size:11px;color:#78909c;margin-bottom:4px}
h1{font-size:20px;margin:0 0 12px;color:#0b3d6e;display:flex;align-items:center;gap:10px}
.badge{font-size:11px;font-weight:700;color:#fff;border-radius:11px;padding:3px 10px}
.b-pend{background:#5c6bc0}.b-draft{background:#78909c}.b-appr{background:#ef6c00}.b-ret{background:#c62828}.b-hr{background:#2e7d32}.b-done{background:#1b5e20}
.region{background:#fff;border:1px solid #dfe3e8;border-radius:4px;margin-bottom:14px}
.region .rh{padding:9px 14px;border-bottom:1px solid #e6e9ed;font-weight:700;font-size:14px;color:#37474f;display:flex;align-items:center;gap:8px}
.region .rb{padding:12px 14px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 22px}
.f label{display:block;font-size:11px;color:#607d8b;margin-bottom:3px}.f label.req:after{content:' *';color:#c62828}
.v{border:1px solid #cfd8dc;background:#f7f9fb;border-radius:3px;padding:6px 8px;min-height:30px}
.in{border:1px solid #90a4ae;background:#fff;border-radius:3px;padding:6px 8px;min-height:30px}
.in.err{border-color:#c62828;background:#fff5f5}
.sel:after{content:'▾';float:right;color:#607d8b}
table{border-collapse:collapse;width:100%}th{background:#eef2f6;text-align:left;font-size:12px;color:#455a64;padding:8px;border-bottom:2px solid #d5dbe1}
td{padding:8px;border-bottom:1px solid #edf0f3;font-size:13px}tr:hover td{background:#f3f8fd}
.lnk{color:#0b5394;font-weight:600}
.btns{display:flex;gap:8px;justify-content:flex-end;padding:10px 14px;border-top:1px solid #e6e9ed;background:#fafbfc}
.btn{padding:7px 16px;border-radius:3px;border:1px solid #b0bec5;background:#fff;font-weight:600;font-size:13px}
.btn.p{background:#0b5394;color:#fff;border-color:#0b5394}.btn.g{background:#2e7d32;color:#fff;border-color:#2e7d32}.btn.r{background:#fff;color:#c62828;border-color:#c62828}
.tb{display:flex;gap:8px;align-items:center;margin-bottom:10px}.search{border:1px solid #b0bec5;border-radius:3px;padding:6px 10px;width:260px;color:#90a4ae;background:#fff}
.chip{display:inline-block;border-radius:10px;padding:2px 9px;font-size:11px;font-weight:700;color:#fff}
.rating span{display:inline-block;width:28px;height:28px;line-height:26px;text-align:center;border:1px solid #b0bec5;border-radius:3px;margin-right:4px;background:#fff}
.rating span.on{background:#0b5394;color:#fff;border-color:#0b5394}
.radio span{margin-right:18px}.radio i{display:inline-block;width:13px;height:13px;border:2px solid #607d8b;border-radius:50%;vertical-align:-2px;margin-right:5px}.radio i.on{border-color:#0b5394;background:radial-gradient(#0b5394 45%,#fff 50%)}
.note{font-size:12px;color:#607d8b}.alert{background:#fff8e1;border:1px solid #ffe082;border-radius:4px;padding:8px 12px;font-size:12px;margin-bottom:12px}
.alert.e{background:#ffebee;border-color:#ef9a9a;color:#b71c1c}
.route{display:flex;align-items:center;gap:6px;flex-wrap:wrap}.step{border:1px solid #cfd8dc;border-radius:16px;padding:5px 12px;font-size:12px;background:#fff}
.step.done{background:#e8f5e9;border-color:#66bb6a}.step.cur{background:#fff3e0;border-color:#ef6c00;font-weight:700}.arw{color:#90a4ae}
.kpi{display:flex;gap:12px;margin-bottom:14px}.k{flex:1;background:#fff;border:1px solid #dfe3e8;border-radius:4px;padding:10px 14px}.k b{font-size:22px;display:block}.k span{font-size:11px;color:#607d8b}
.tl{border-left:2px solid #cfd8dc;margin-left:8px;padding-left:16px}.tl div{position:relative;margin-bottom:10px}.tl div:before{content:'';position:absolute;left:-23px;top:3px;width:10px;height:10px;border-radius:50%;background:#0b5394}
.ta{min-height:54px}
"""
NAV=["Home","My Pending Tasks","Probation Evaluation","HR Monitoring","Approval Hierarchy Setup","Reports"]
def page(name,title,active,body,badge=None,bc="HRD ▸ Probation Evaluation"):
    nav="".join(f'<div class="{"on" if n==active else ""}">{n}</div>' for n in NAV)
    b=f'<span class="badge {badge[1]}">{badge[0]}</span>' if badge else ''
    html=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="app">
<div class="top"><span class="logo">SKMCH · HRD</span><span>Human Resource System</span><span class="sp"></span><span class="bell">3</span><span class="u">EMP-TEST-0100 ▾</span></div>
<div class="wrap"><div class="nav"><div class="h">MENU</div>{nav}</div><div class="main"><div class="bc">{bc}</div><h1>{title} {b}</h1>{body}</div></div></div></body></html>"""
    open(os.path.join(OUT,name+".html"),"w").write(html)
def ro(l,v): return f'<div class="f"><label>{l}</label><div class="v">{v}</div></div>'
def emp_region(st=""):
    return f'''<div class="region"><div class="rh">Employee Information</div><div class="rb"><div class="grid">
{ro("Employee No.","EMP-TEST-0001")}{ro("Employee Name","Ali Raza")}{ro("Designation","Staff Nurse")}
{ro("Department","Nursing")}{ro("Joining Date","26-Apr-2026")}{ro("Evaluator (Supervisor)","EMP-TEST-0100 · Nadia Khan")}
{ro("Probation Start","26-Apr-2026")}{ro("Probation End","25-Oct-2026")}{ro("Evaluation No.","PEV-2026-000123")}</div></div></div>'''
def criteria(edit=True):
    rows=[("Job knowledge",4),("Quality of work",3),("Punctuality &amp; attendance",5),("Teamwork &amp; communication",4),("Patient / customer care",4)]
    tr=""
    for i,(c,v) in enumerate(rows,1):
        rt="".join(f'<span class="{"on" if k==v else ""}">{k}</span>' for k in range(1,6))
        rem='<div class="in" style="min-height:28px"></div>' if edit else '<div class="v" style="min-height:28px">—</div>'
        tr+=f'<tr><td>{i}</td><td>{c} <span style="color:#c62828">*</span></td><td class="rating">{rt}</td><td style="width:38%">{rem}</td></tr>'
    return f'''<div class="region"><div class="rh">Evaluation Criteria <span class="note">(template from HR · rating 1 = Poor … 5 = Excellent)</span></div><div class="rb" style="padding:0">
<table><tr><th style="width:40px">#</th><th>Criterion</th><th>Rating</th><th>Remarks</th></tr>{tr}</table></div></div>'''
def recommend(edit=True,extend=False):
    cls="in" if edit else "v"
    return f'''<div class="region"><div class="rh">Recommendation</div><div class="rb">
<div class="f" style="margin-bottom:10px"><label class="req">Evaluator recommendation</label><div class="radio" style="padding:6px 0"><span><i class="{'' if extend else 'on'}"></i>Confirm</span><span><i class="{'on' if extend else ''}"></i>Extend probation</span><span><i></i>Not to confirm</span></div></div>
<div class="grid"><div class="f"><label>Extend by (days)</label><div class="{cls}" style="color:#b0bec5">{'90' if extend else 'enabled only for Extend'}</div></div>
<div class="f" style="grid-column:span 2"><label>Attachments</label><div class="{cls}">📎 evaluation_form_signed.pdf</div></div></div>
<div class="f" style="margin-top:10px"><label class="req">Evaluator comments</label><div class="{cls} ta">Performs duties well; meets expectations of the role. Recommend confirmation.</div></div></div></div>'''

# 1 pending tasks
rows=[("Probation Evaluation","EMP-TEST-0001 · Ali Raza","Nursing","25-Oct-2026","15 days",("EVALUATION PENDING","#5c6bc0")),
      ("Probation Evaluation","EMP-TEST-0002 · Sara Ahmed","Pharmacy","18-Oct-2026","8 days",("DRAFT","#78909c")),
      ("Probation Evaluation","EMP-TEST-0003 · Omar Farooq","Radiology","14-Oct-2026","4 days",("RETURNED","#c62828")),
      ("Leave Application","EMP-TEST-0007 · Hina Shah","Nursing","—","—",("PENDING","#90a4ae"))]
tr="".join(f'<tr><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td><span class="chip" style="background:{s[1]}">{s[0]}</span></td><td class="lnk">Open ›</td></tr>' for a,b,c,d,e,s in rows)
page("01_pending_tasks","My Pending Tasks","My Pending Tasks",f'''
<div class="kpi"><div class="k"><b>3</b><span>Probation evaluations</span></div><div class="k"><b style="color:#c62828">1</b><span>Returned for correction</span></div><div class="k"><b style="color:#ef6c00">1</b><span>Due within 7 days</span></div><div class="k"><b>1</b><span>Other tasks</span></div></div>
<div class="region"><div class="rh">Pending Tasks</div><div class="rb"><div class="tb"><div class="search">🔍 Search…</div><span class="btn">Task type: All ▾</span><span class="sp" style="flex:1"></span><span class="btn">Actions ▾</span></div>
<table><tr><th>Task</th><th>Employee</th><th>Department</th><th>Probation End</th><th>Due In</th><th>Status</th><th></th></tr>{tr}</table></div></div>
<div class="note">Probation evaluation tasks are created automatically 15 days before the probation end date. Click “Open” to evaluate.</div>''',bc="HRD ▸ Home ▸ My Pending Tasks")

# 2 evaluation form
page("02_evaluation_form","Probation Evaluation","Probation Evaluation",f'''
<div class="alert e">ℹ Example validation: Submit is blocked until every field marked * is completed; missing fields are highlighted in red.</div>
{emp_region()}{criteria()}{recommend()}
<div class="region"><div class="btns" style="border-top:0"><span class="btn">Cancel</span><span class="btn">Save as Draft</span><span class="btn p">Submit for Approval</span></div></div>
<div class="note">* Mandatory on Submit only. Save as Draft keeps the evaluation in your queue and is visible only to you.</div>''',badge=("DRAFT","b-draft"))

# 3a approver
page("03_approver","Probation Evaluation – Approval","My Pending Tasks",f'''
<div class="region"><div class="rh">Approval Routing</div><div class="rb"><div class="route">
<span class="step done">✔ Evaluator · EMP-TEST-0100 · Submitted 15-Oct-2026</span><span class="arw">➜</span>
<span class="step cur">● Level 1 · HOD Nursing (you)</span><span class="arw">➜</span><span class="step">Level 2 · Director Nursing</span><span class="arw">➜</span><span class="step">HR Department</span></div></div></div>
{emp_region()}{criteria(False)}{recommend(False)}
<div class="region"><div class="rh">Approver Decision</div><div class="rb"><div class="f"><label>Approver comments <span class="note">(mandatory for Return)</span></label><div class="in ta"></div></div></div>
<div class="btns"><span class="btn">Back</span><span class="btn r">↩ Return to Evaluator</span><span class="btn g">✔ Approve</span></div></div>''',badge=("PENDING APPROVAL – L1","b-appr"))

# 3b hierarchy setup
hr=[("Nursing","1","Head of Department","DEPARTMENT_HEAD","Y"),("Nursing","2","Director Nursing","Named employee","Y"),("Pharmacy","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All departments)","1","Head of Department","DEPARTMENT_HEAD","Y"),("(All departments)","2","Department Manager","DEPARTMENT_MANAGER","N")]
tr="".join(f'<tr><td><div class="in sel" style="min-height:28px;padding:4px 8px">{a}</div></td><td style="width:70px"><div class="in" style="min-height:28px;padding:4px 8px">{b}</div></td><td><div class="in sel" style="min-height:28px;padding:4px 8px">{c}</div></td><td>{d}</td><td style="width:70px"><span class="chip" style="background:{"#2e7d32" if e=="Y" else "#90a4ae"}">{"Active" if e=="Y" else "Inactive"}</span></td></tr>' for a,b,c,d,e in hr)
page("04_hierarchy_setup","Probation Approval Hierarchy Setup","Approval Hierarchy Setup",f'''
<div class="alert">Levels are applied in order on Submit. Approver on leave → acting-for person (HRD.ACTING_FOR), if confirmed by HR.</div>
<div class="region"><div class="rh">Hierarchy Levels</div><div class="rb"><div class="tb"><span class="btn p">+ Add Row</span><div class="search">🔍 Search…</div></div>
<table><tr><th>Department</th><th>Level</th><th>Approver role</th><th>Resolved from</th><th>Status</th></tr>{tr}</table></div>
<div class="btns"><span class="btn">Cancel</span><span class="btn p">Save</span></div></div>''',bc="HRD ▸ Setup ▸ Probation Approval Hierarchy")

# 4a HR queue
rows=[("EMP-TEST-0001 · Ali Raza","Nursing","25-Oct-2026","Confirm","L2 Director Nursing","20-Oct-2026"),("EMP-TEST-0004 · Hina Malik","Administration","30-Oct-2026","Extend 90 days","L1 HOD Admin","22-Oct-2026"),("EMP-TEST-0008 · Bilal Aslam","IT","02-Nov-2026","Confirm","L2 Director IT","23-Oct-2026")]
tr="".join(f'<tr><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td><b>{d}</b></td><td>{e}</td><td>{f}</td><td><span class="chip" style="background:#2e7d32">FORWARDED TO HR</span></td><td class="lnk">Process ›</td></tr>' for a,b,c,d,e,f in rows)
page("05_hr_queue","HR – Completed Probation Evaluations","My Pending Tasks",f'''
<div class="region"><div class="rh">Evaluations awaiting HR decision</div><div class="rb"><div class="tb"><div class="search">🔍 Search…</div><span class="btn">Department: All ▾</span></div>
<table><tr><th>Employee</th><th>Department</th><th>Probation End</th><th>Recommendation</th><th>Final approval</th><th>Received</th><th>Status</th><th></th></tr>{tr}</table></div></div>''',bc="HRD ▸ HR ▸ Probation Evaluations")

# 4b HR decision
page("06_hr_decision","HR Decision – Probation Evaluation","My Pending Tasks",f'''
<div class="region"><div class="rh">Approval Routing</div><div class="rb"><div class="route">
<span class="step done">✔ Evaluator · 15-Oct-2026</span><span class="arw">➜</span><span class="step done">✔ L1 HOD Nursing · 16-Oct-2026</span><span class="arw">➜</span><span class="step done">✔ L2 Director Nursing · 20-Oct-2026</span><span class="arw">➜</span><span class="step cur">● HR Department</span></div></div></div>
{emp_region()}
<div class="region"><div class="rh">Evaluation Summary <span class="note">(full evaluation: View ›)</span></div><div class="rb"><div class="grid">{ro("Overall rating","4.0 / 5")}{ro("Evaluator recommendation","Confirm")}{ro("Approver comments","Agreed – L1, L2")}</div></div></div>
<div class="region"><div class="rh">HR Decision</div><div class="rb">
<div class="f" style="margin-bottom:10px"><label class="req">Decision</label><div class="radio" style="padding:6px 0"><span><i class="on"></i>Confirm employment</span><span><i></i>Extend probation</span><span><i></i>Other (per HR policy)</span></div></div>
<div class="grid"><div class="f"><label>Extension days</label><div class="in" style="color:#b0bec5">only for Extend</div></div><div class="f"><label>Extension reason</label><div class="in sel" style="color:#b0bec5">Probation Reasons</div></div><div class="f"><label>Effective confirmation date</label><div class="v">26-Oct-2026</div></div></div>
<div class="f" style="margin-top:10px"><label>HR remarks</label><div class="in ta"></div></div>
<div class="alert" style="margin:10px 0 0">ℹ On “Complete” with Confirm, the probation record is set to Confirmed: confirmation date is updated and eligible allowances are queued.</div></div>
<div class="btns"><span class="btn">Back</span><span class="btn g">✔ Complete</span></div></div>''',badge=("FORWARDED TO HR","b-hr"),bc="HRD ▸ HR ▸ Probation Evaluations")

# 5 monitoring
rows=[("EMP-TEST-0001 · Ali Raza","Nursing","25-Oct-2026",("PENDING APPROVAL – L2","#ef6c00"),"Director Nursing",""),
      ("EMP-TEST-0005 · Asad Iqbal","Finance","08-Oct-2026",("DRAFT","#78909c"),"EMP-TEST-0110",'<span class="chip" style="background:#c62828">OVERDUE</span>'),
      ("EMP-TEST-0006 · Zoya Haider","Laboratory","20-Oct-2026",("NO SUPERVISOR","#6d4c41"),"HR exception list",'<span class="lnk">Assign evaluator ›</span>'),
      ("EMP-TEST-0004 · Hina Malik","Administration","30-Oct-2026",("FORWARDED TO HR","#2e7d32"),"HR",""),
      ("EMP-TEST-0009 · Usman Tariq","Nursing","01-Oct-2026",("COMPLETED","#1b5e20"),"—","")]
tr="".join(f'<tr><td class="lnk">{a}</td><td>{b}</td><td>{c}</td><td><span class="chip" style="background:{s[1]}">{s[0]}</span></td><td>{w}</td><td>{fl}</td></tr>' for a,b,c,s,w,fl in rows)
page("07_monitoring","Probation Evaluation Monitoring","HR Monitoring",f'''
<div class="kpi"><div class="k"><b>42</b><span>Open evaluations</span></div><div class="k"><b style="color:#ef6c00">18</b><span>Pending approval</span></div><div class="k"><b style="color:#c62828">3</b><span>Overdue</span></div><div class="k"><b style="color:#6d4c41">2</b><span>No supervisor</span></div><div class="k"><b style="color:#2e7d32">7</b><span>With HR</span></div></div>
<div class="region"><div class="rh">Filters</div><div class="rb"><div class="grid" style="grid-template-columns:repeat(5,1fr)">
<div class="f"><label>Status</label><div class="in sel">All</div></div><div class="f"><label>Department</label><div class="in sel">All</div></div><div class="f"><label>Evaluator</label><div class="in"></div></div><div class="f"><label>Probation end from</label><div class="in">01-Oct-2026</div></div><div class="f"><label>to</label><div class="in">31-Oct-2026</div></div></div></div></div>
<div class="region"><div class="rh">Evaluations</div><div class="rb" style="padding:0"><table><tr><th>Employee</th><th>Department</th><th>Probation End</th><th>Status</th><th>Currently with</th><th>Flag / Action</th></tr>{tr}</table></div></div>
<div class="region"><div class="rh">Status History – EMP-TEST-0001 · Ali Raza</div><div class="rb"><div class="tl">
<div><b>10-Oct-2026 02:00</b> · SYSTEM · Queue created → <span class="chip" style="background:#5c6bc0">EVALUATION PENDING</span></div>
<div><b>12-Oct-2026 10:15</b> · EMP-TEST-0100 · Saved → <span class="chip" style="background:#78909c">DRAFT</span></div>
<div><b>15-Oct-2026 09:40</b> · EMP-TEST-0100 · Submitted → <span class="chip" style="background:#ef6c00">PENDING APPROVAL – L1</span></div>
<div><b>16-Oct-2026 14:05</b> · EMP-TEST-0200 · Approved “Agreed” → <span class="chip" style="background:#ef6c00">PENDING APPROVAL – L2</span></div></div>
<div class="note">History is read-only and cannot be edited or deleted.</div></div></div>''',bc="HRD ▸ HR ▸ Probation Monitoring")
print("ok")
