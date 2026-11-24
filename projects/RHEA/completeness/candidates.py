import sys, collections, json, csv
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import *
D,OBO=sys.argv[1],sys.argv[2]
tomaster=load_dirs(D); sp=load_sp(D); eq,rec=load_rhea(D)
T=parse_obo(OBO); anc=ancestors(T)
live={k:v for k,v in T.items() if not v["obs"]}
rmap=collections.defaultdict(list); ecmap=collections.defaultdict(list)
for t in live.values():
    for db,x,p in t["xrefs"]:
        if db=="RHEA": rmap[tomaster.get(x,x)].append((t["id"],p))
        else: ecmap[x].append((t["id"],p))
COVER={"skos:exactMatch","skos:narrowMatch"}
def covered(m): return [g for g,p in rmap.get(m,[]) if p in COVER]
# RHEA is_a (direction-specific ids too -> masters)
rpar=collections.defaultdict(set)
for r in csv.DictReader(open(f"{D}/rhea-relationships.tsv"),delimiter="\t"):
    a,b=tomaster.get(r["FROM_REACTION_ID"],r["FROM_REACTION_ID"]),tomaster.get(r["TO_REACTION_ID"],r["TO_REACTION_ID"])
    if a!=b: rpar[a].add(b)
def rhea_anc_targets(m):
    # BFS upwards; return GO targets at nearest mapped level
    seen=set(); frontier=set(rpar.get(m,()))
    while frontier:
        hits={(g,a) for a in frontier for g in covered(a)}
        if hits: return hits
        seen|=frontier; frontier={p for a in frontier for p in rpar.get(a,()) if p not in seen}
    return set()
def ec_targets(e):
    # walk up EC: 2.7.11.1 -> 2.7.11.- -> 2.7.-.- ...
    parts=e.split("."); level=0
    while True:
        k=".".join(parts)
        hits=[g for g,p in ecmap.get(k,[]) if p in ("skos:exactMatch","skos:narrowMatch",None)]
        if hits: return hits, level
        i=max(j for j,x in enumerate(parts) if x!="-") if any(x!="-" for x in parts) else -1
        if i<=0: return [],level
        parts[i]="-"; level+=1
def lca(gos):
    gos=list(gos)
    common=set.intersection(*[anc(g) for g in gos]) if gos else set()
    # most specific: those with no descendant in common
    return [c for c in common if not any(c!=d and c in anc(d) for d in common)]
ec_rxn_count=collections.Counter(e for m,es in rec.items() for e in es)
out=[]
for m,prots in sp.items():
    if covered(m): continue
    row={"rhea":m,"n_sp":len(prots),"equation":eq.get(m,""),"ec":";".join(sorted(rec.get(m,()))),
         "existing":";".join(f"{g}|{p}" for g,p in rmap.get(m,[]))}
    ra=rhea_anc_targets(m)
    if ra:
        row["tier"]="A_rhea_parent"; row["cand"]=";".join(sorted({g for g,_ in ra})); row["pred"]="skos:narrowMatch"
        row["via"]=";".join(sorted({"RHEA:"+a for _,a in ra}))
    elif rec.get(m):
        res=[ec_targets(e) for e in sorted(rec[m])]
        gos=[g for h,_ in res for g in h]; lvl=max(l for _,l in res)
        if all(h for h,_ in res):
            cands=lca(set(gos)) if len(set(gos))>1 else list(set(gos))
            single = len(rec[m])==1 and lvl==0 and ec_rxn_count[next(iter(rec[m]))]==1 and len(set(gos))==1
            row["tier"]="B_ec_exact" if single else ("B_ec" if lvl==0 else "C_ec_parent")
            row["cand"]=";".join(sorted(cands)); row["pred"]="skos:exactMatch" if single else "skos:narrowMatch"
            row["via"]="EC up %d"%lvl
        else:
            row["tier"]="D_ec_nogo"; row["cand"]=""; row["pred"]=""
    else:
        row["tier"]="E_noec"; row["cand"]=""; row["pred"]=""
    row["cand_labels"]=";".join(T[g]["name"] for g in row["cand"].split(";") if g in T)
    out.append(row)
cols=["rhea","tier","pred","cand","cand_labels","via","n_sp","ec","existing","equation"]
w=csv.DictWriter(open(f"{D}/candidates.tsv","w"),fieldnames=cols,delimiter="\t",extrasaction="ignore")
w.writeheader(); [w.writerow(r) for r in sorted(out,key=lambda r:(r["tier"],-r["n_sp"]))]
c=collections.Counter(r["tier"] for r in out); print(c)
generic=collections.Counter(r["cand"] for r in out if r["cand"]); print(generic.most_common(25))
