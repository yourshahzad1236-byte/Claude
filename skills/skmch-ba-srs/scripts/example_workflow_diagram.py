import sys
W,H=1700,880
o=[]
a=o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif">')
a('''<defs>
<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#37474f"/></marker>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c62828"/></marker>
<marker id="ard" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6d4c41"/></marker>
</defs>''')
a(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
a('<text x="30" y="42" font-size="24" font-weight="700" fill="#1a237e">Automated Employee Probation Evaluation – Workflow</text>')
a('<text x="30" y="66" font-size="14" fill="#546e7a">CR-2026-XXX-PEV · swimlane view · status shown in coloured tags</text>')
lanes=[("SYSTEM","(daily job)","#e8eaf6"),("SUPERVISOR","(evaluator)","#ffffff"),("APPROVERS","(configured hierarchy)","#f3f6f9"),("HR","DEPARTMENT","#ffffff")]
for i,(n,s,c) in enumerate(lanes):
    y=80+i*160
    a(f'<rect x="20" y="{y}" width="{W-40}" height="160" fill="{c}" stroke="#90a4ae"/>')
    a(f'<rect x="20" y="{y}" width="130" height="160" fill="#263238"/>')
    a(f'<text x="85" y="{y+76}" font-size="16" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')
    a(f'<text x="85" y="{y+98}" font-size="12" fill="#cfd8dc" text-anchor="middle">{s}</text>')
def lines(x,y,txt,size=13,color="#212121",bold=False):
    ls=txt.split("|"); h=size+3; y0=y-(len(ls)-1)*h/2+size/3
    for k,l in enumerate(ls):
        a(f'<text x="{x}" y="{y0+k*h}" font-size="{size}" fill="{color}" text-anchor="middle"{" font-weight=\"700\"" if bold else ""}>{l}</text>')
def box(x,y,txt,kind="task"):
    st={"task":('#ffffff','#1565c0','#212121'),"sys":('#1565c0','#0d47a1','#ffffff'),"end":('#2e7d32','#1b5e20','#ffffff'),"exc":('#fff8e1','#6d4c41','#4e342e')}[kind]
    dash=' stroke-dasharray="6 4"' if kind=="exc" else ''
    a(f'<rect x="{x-95}" y="{y-32}" width="190" height="64" rx="12" fill="{st[0]}" stroke="{st[1]}" stroke-width="2"{dash}/>')
    lines(x,y,txt,13,st[2],kind in("sys","end"))
def dia(x,y,txt):
    a(f'<polygon points="{x},{y-42} {x+80},{y} {x},{y+42} {x-80},{y}" fill="#fff3e0" stroke="#ef6c00" stroke-width="2"/>')
    lines(x,y,txt,12,"#4e342e",True)
def start(x,y):
    a(f'<circle cx="{x}" cy="{y}" r="14" fill="#263238"/>')
def path(pts,kind="n",label=None,lx=None,ly=None,anchor="middle"):
    m={"n":("#37474f","ar",""),"r":("#c62828","arr",""),"d":("#6d4c41","ard",' stroke-dasharray="6 4"')}[kind]
    d="M"+" L".join(f"{p[0]},{p[1]}" for p in pts)
    a(f'<path d="{d}" fill="none" stroke="{m[0]}" stroke-width="2"{m[2]} marker-end="url(#{m[1]})"/>')
    if label: a(f'<text x="{lx}" y="{ly}" font-size="12" font-weight="600" fill="{m[0]}" text-anchor="{anchor}">{label}</text>')
def tag(x,y,txt,col):
    w=len(txt)*7.2+16
    a(f'<rect x="{x-w/2}" y="{y-11}" width="{w}" height="22" rx="11" fill="{col}"/>')
    a(f'<text x="{x}" y="{y+4}" font-size="11" font-weight="700" fill="#fff" text-anchor="middle">{txt}</text>')
Y=[160,320,480,640]
# nodes
start(185,Y[0]); path([(199,Y[0]),(205,Y[0])])
box(300,Y[0],"Daily job finds employees|with probation end date|≤ 15 days away","sys")
box(540,Y[0],"Create evaluation queue|for respective supervisor|+ e-mail notification","sys")
box(540,Y[1],"Open &amp; fill|Probation Evaluation form")
dia(790,Y[1],"Save or|Submit?")
box(1010,Y[2],"Level n approver|reviews evaluation")
dia(1250,Y[2],"Approve or|Return?")
dia(1470,Y[2],"Last|level?")
box(1470,Y[0],"Route completed evaluation|to HR Department queue","sys")
box(1580,Y[3],"HR reviews &amp; decides|Confirm / Extend")
box(1300,Y[3],"COMPLETED|probation record updated","end")
box(300,Y[3],"HR exception list|HR assigns evaluator","exc")
# arrows
path([(395,Y[0]),(443,Y[0])])
path([(520,Y[0]+32),(520,Y[1]-34)])
tag(640,Y[0]+52,"EVALUATION PENDING","#5c6bc0")
path([(635,Y[1]),(708,Y[1])])
# draft loop
path([(790,Y[1]+42),(790,Y[1]+62),(580,Y[1]+62),(580,Y[1]+34)],"n","Save as Draft",690,Y[1]+57)
tag(685,Y[1]+76,"DRAFT","#78909c")
# submit
path([(870,Y[1]),(1010,Y[1]),(1010,Y[2]-34)],"n","Submit (mandatory fields validated)",880,Y[1]-12,"start")
tag(1095,Y[1]+46,"PENDING APPROVAL – L1","#ef6c00")
path([(1105,Y[2]),(1168,Y[2])])
path([(1330,Y[2]),(1388,Y[2])],"n","Approve",1359,Y[2]-8)
# return
path([(1250,Y[2]-42),(1250,Y[1]-62),(560,Y[1]-62),(560,Y[1]-34)],"r","Return with comments",1120,Y[1]-68)
tag(1250,Y[1]+10,"RETURNED","#c62828")
# next level
path([(1470,Y[2]+42),(1470,Y[2]+62),(1010,Y[2]+62),(1010,Y[2]+34)],"n","No → next level",1240,Y[2]+57)
tag(1240,Y[2]+76,"PENDING APPROVAL – L n+1","#ef6c00")
# last level yes
path([(1470,Y[2]-42),(1470,Y[0]+34)],"n","Yes",1485,Y[1])
path([(1565,Y[0]),(1640,Y[0]),(1640,Y[3]-34)])
tag(1570,Y[1]+40,"FORWARDED TO HR","#2e7d32")
path([(1485,Y[3]),(1397,Y[3])])
tag(1300,Y[3]+50,"COMPLETED","#1b5e20")
# exception
path([(470,Y[0]+32),(470,Y[0]+60),(300,Y[0]+60),(300,Y[3]-34)],"d","No supervisor on record",390,Y[0]+77)
path([(395,Y[3]),(500,Y[3]),(500,Y[1]+34)],"d","Evaluator assigned",510,Y[3]-40,"start")
# legend
ly=748
a(f'<rect x="20" y="{ly}" width="{W-40}" height="112" rx="8" fill="#fafafa" stroke="#cfd8dc"/>')
a(f'<text x="40" y="{ly+26}" font-size="14" font-weight="700" fill="#263238">Legend</text>')
lx=40
def lg(x,shape,txt):
    if shape=="sys": a(f'<rect x="{x}" y="{ly+40}" width="34" height="22" rx="6" fill="#1565c0"/>')
    if shape=="task": a(f'<rect x="{x}" y="{ly+40}" width="34" height="22" rx="6" fill="#fff" stroke="#1565c0" stroke-width="2"/>')
    if shape=="dia": a(f'<polygon points="{x+17},{ly+38} {x+34},{ly+51} {x+17},{ly+64} {x},{ly+51}" fill="#fff3e0" stroke="#ef6c00" stroke-width="2"/>')
    if shape=="end": a(f'<rect x="{x}" y="{ly+40}" width="34" height="22" rx="6" fill="#2e7d32"/>')
    if shape=="exc": a(f'<rect x="{x}" y="{ly+40}" width="34" height="22" rx="6" fill="#fff8e1" stroke="#6d4c41" stroke-width="2" stroke-dasharray="4 3"/>')
    if shape=="ret": a(f'<line x1="{x}" y1="{ly+51}" x2="{x+34}" y2="{ly+51}" stroke="#c62828" stroke-width="2" marker-end="url(#arr)"/>')
    a(f'<text x="{x+44}" y="{ly+56}" font-size="13" fill="#37474f">{txt}</text>')
for i,(s,t) in enumerate([("sys","Automatic system step"),("task","User action"),("dia","Decision"),("ret","Return / correction path"),("exc","Exception handling"),("end","End")]):
    lg(40+i*270,s,t)
a(f'<text x="40" y="{ly+92}" font-size="12.5" fill="#37474f">Rules: one evaluation per employee per probation period · Draft is visible only to the evaluator · approver on leave → acting-for person (HRD.ACTING_FOR, to be confirmed) ·</text>')
a(f'<text x="40" y="{ly+108}" font-size="12.5" fill="#c62828" font-weight="600">PROBATION_STATUS = \'C\' (Confirmed) is written only at the HR step — it sets CONFIRMATION_DATE and starts incentives. Employee separates before HR completes → CANCELLED.</text>')
a('</svg>')
open(sys.argv[1],'w').write("\n".join(o))
