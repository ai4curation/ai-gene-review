"""Coverage of Swiss-Prot-used RHEA master reactions by predicated GO xrefs (go-edit.obo).
A master is covered only by an xref on the master id itself; xrefs on directional ids are reported separately."""
import sys, csv, collections, json
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import *
D,OBO=sys.argv[1],sys.argv[2]
tomaster=load_dirs(D); sp=load_sp(D); T=parse_obo(OBO)
byid=collections.defaultdict(list)
for t in T.values():
    if t["obs"]: continue
    for db,x,p in t["xrefs"]:
        if db=="RHEA": byid[x].append((t["id"],p))
kids=collections.defaultdict(list)
for i,m in tomaster.items():
    if i!=m: kids[m].append(i)
cov=collections.Counter(); ent=collections.Counter(); rows=[]
for m,prots in sp.items():
    preds={p for _,p in byid.get(m,[])}
    kp={p for k in kids[m] for _,p in byid.get(k,[])}
    if "skos:exactMatch" in preds: c="exact"
    elif "skos:narrowMatch" in preds: c="go_broader"
    elif None in preds: c="untyped"
    elif kp & {"skos:exactMatch","skos:narrowMatch"}: c="directional_only"
    elif "skos:broadMatch" in preds: c="go_narrower_only"
    else: c="unmapped"
    cov[c]+=1; ent[c]+=len(prots); rows.append((m,c,len(prots)))
print("Swiss-Prot RHEA masters:",len(sp))
for k,v in cov.most_common(): print(f"  {k:18s} {v:6d} reactions {ent[k]:7d} entry-reaction pairs")
json.dump({"rows":rows},open(f"{D}/coverage.json","w"))
