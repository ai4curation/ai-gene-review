"""Consistency of Swiss-Prot RHEA annotations with native GO MF annotations.

For each GO xref RHEA:id -> GO term g (exactMatch/narrowMatch; GO term equal or broader) and each Swiss-Prot
entry whose catalytic-activity annotation carries that exact RHEA id (master or directional), classify the entry
by its MF annotations from sources other than the RHEA/EC mappings themselves:
  consistent     has g or an is_a descendant of g
  ancestor_only  only catalytic/transporter terms that are ancestors of g (less specific, compatible)
  disjoint       has catalytic/transporter terms, none in g's lineage (potential conflict)
  none           no catalytic/transporter MF at all
Computed twice: curated sources (non-IEA) and all non-circular sources (curated + InterPro2GO, UniRule, ARBA, ...).
Circular sources excluded: IEA:RHEA, IEA:UniProtKB-EC (they are generated from this very mapping / the EC bridge).
"""
import sys, glob, json, csv, collections
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import *
D,OBO=sys.argv[1],sys.argv[2]
eq,rec=load_rhea(D)
T=parse_obo(OBO); anc=ancestors(T)
G=parse_obo(f"{D}/go-basic.obo"); ganc=ancestors(G)
def A(x): return ganc(x) if x in G else anc(x)
ROOTS={"GO:0003824","GO:0005215"}
CIRC={"IEA:RHEA","IEA:UniProtKB-EC"}
native={}
for f in glob.glob(f"{D}/sp_mf.*.jsonl"):
    for l in open(f):
        e=json.loads(l); native[e["ac"]]=[(t,ev) for t,ev in e["mf"] if ev not in CIRC]
byid=collections.defaultdict(list)
for t in T.values():
    if t["obs"]: continue
    for db,x,p in t["xrefs"]:
        if db=="RHEA" and p in ("skos:exactMatch","skos:narrowMatch"): byid[x].append((t["id"],p))
pairs=collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/rhea2uniprot_sprot.tsv"),delimiter="\t"):
    for g,p in byid.get(r["RHEA_ID"],[]): pairs[(r["MASTER_ID"],g,p,r["RHEA_ID"])].add(r["ID"])
def classify(terms,g,ga):
    enz={t for t in terms if A(t)&ROOTS}
    if any(g in A(t) for t in terms): return "consistent"
    if any(t in ga and t not in ROOTS for t in enz): return "ancestor_only"
    if enz: return "disjoint"
    return "none"
K=("consistent","ancestor_only","disjoint","none")
rows=[]; tot={"cur":collections.Counter(),"all":collections.Counter()}
for (m,g,p,via),prots in pairs.items():
    ga=A(g); c={"cur":collections.Counter(),"all":collections.Counter()}; ex=collections.defaultdict(list); oth=collections.Counter()
    for ac in prots:
        if ac not in native: c["all"]["not_fetched"]+=1; continue
        cur={t for t,ev in native[ac] if not ev.startswith("IEA")}; al={t for t,_ in native[ac]}
        kc=classify(cur,g,ga); ka=classify(al,g,ga)
        c["cur"][kc]+=1; c["all"][ka]+=1
        if ka=="disjoint":
            if len(ex["dis"])<6: ex["dis"].append(ac)
            for t,ev in native[ac]:
                if A(t)&ROOTS and t not in ga: oth[(t,ev.split(":")[1] if ":" in ev else ev)]+=1
    for s in ("cur","all"): tot[s].update(c[s])
    n=sum(c["all"][k] for k in K)
    rows.append({"rhea":m,"via":via,"go":g,"label":T[g]["name"],"pred":p,"released": g in G,"n":n,
        **{f"all_{k}":c["all"][k] for k in K},**{f"cur_{k}":c["cur"][k] for k in K},"not_fetched":c["all"]["not_fetched"],
        "disjoint_examples":",".join(ex["dis"]),
        "disjoint_terms":"; ".join(f"{t} {G.get(t,T.get(t,{})).get('name','?')} [{s}]x{k}" for (t,s),k in oth.most_common(4)),
        "equation":eq.get(m,"")})
w=csv.DictWriter(open(f"{D}/consistency.tsv","w"),fieldnames=list(rows[0].keys()),delimiter="\t"); w.writeheader()
w.writerows(sorted(rows,key=lambda r:-r["all_disjoint"]))
for s in ("cur","all"): print(s, dict(tot[s]))
