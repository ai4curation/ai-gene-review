"""For unmapped Swiss-Prot RHEA masters, propose a GO target from the native MF annotations of the entries
carrying the reaction: the most specific catalytic/transporter term (or ancestor) shared by >= FRAC of entries.
Circular sources (IEA:RHEA, IEA:UniProtKB-EC) excluded. Adds columns to candidates2.tsv -> candidates3.tsv."""
import sys, glob, json, csv, collections
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import *
D=sys.argv[1]; FRAC=float(sys.argv[2]) if len(sys.argv)>2 else 0.6
G=parse_obo(f"{D}/go-basic.obo"); anc=ancestors(G)
ROOTS={"GO:0003824","GO:0005215","GO:0003674"}
CIRC={"IEA:RHEA","IEA:UniProtKB-EC"}
nat={}
for f in glob.glob(f"{D}/sp_mf.*.jsonl"):
    for l in open(f):
        e=json.loads(l); nat[e["ac"]]=[t for t,ev in e["mf"] if ev not in CIRC]
sp=load_sp(D)
depth={}
def dep(t):
    if t not in depth: depth[t]=1+max([dep(p) for p in G.get(t,{}).get("isa",[])] or [0])
    return depth[t]
rows=list(csv.DictReader(open(f"{D}/candidates2.tsv"),delimiter="\t"))
for r in rows:
    prots=[p for p in sp[r["rhea"]] if p in nat]
    c=collections.Counter()
    for p in prots:
        cl=set()
        for t in nat[p]:
            if t in G and anc(t)&{"GO:0003824","GO:0005215"}: cl|=anc(t)
        c.update(cl-ROOTS)
    n=len(prots); ok=[t for t,k in c.items() if n and k/n>=FRAC]
    best=sorted(ok,key=lambda t:(-dep(t),-c[t]))[:1]
    r["native_n"]=n
    r["native_cand"]=best[0] if best else ""
    r["native_label"]=G[best[0]]["name"] if best else ""
    r["native_frac"]=round(c[best[0]]/n,2) if best else ""
w=csv.DictWriter(open(f"{D}/candidates3.tsv","w"),fieldnames=list(rows[0].keys()),delimiter="\t"); w.writeheader(); w.writerows(rows)
print("unmapped:",len(rows),"| native candidate found:",sum(bool(r["native_cand"]) for r in rows))
print(collections.Counter((r["tier"],bool(r["native_cand"])) for r in rows))
