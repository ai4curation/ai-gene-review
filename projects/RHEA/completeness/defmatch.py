import sys, re, csv, collections
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import *
D,OBO=sys.argv[1],sys.argv[2]
T=parse_obo(OBO)
def norm_side(s):
    items=[x.strip() for x in re.split(r" \+ (?![^\[\(]*[\]\)])",s)]
    out=set()
    for x in items:
        x=re.sub(r"^\d+ ","",x); x=re.sub(r"^n ","",x)
        x=x.lower().replace("(+)","").replace("(-)","").replace("(2-)","").replace("(3-)","").replace("(4-)","")
        x=re.sub(r"\s+"," ",x).strip(" .")
        if x in ("h","h+","h2o","water"): continue
        out.add(x)
    return frozenset(out)
def key(eq):
    if "=" not in eq: return None
    l,r=eq.split("=",1)
    a,b=norm_side(l),norm_side(r)
    return frozenset([a,b])
idx=collections.defaultdict(set)
for t in T.values():
    if t["obs"] or t["ns"]!="molecular_function": continue
    d=t["def"]
    for m in re.finditer(r"[Cc]atalysis of the reactions?: (.+?)(?:\.\"| \[|\.\s*\[|\"\s*\[)",d):
        for eq in re.split(r"(?<!\w)\.? (?:and|or) (?=\S)",m.group(1).rstrip(".")) if False else [m.group(1)]:
            for part in re.split(r"\.\s+|; ", eq):
                k=key(part)
                if k: idx[k].add(t["id"])
rows=list(csv.DictReader(open(f"{D}/candidates.tsv"),delimiter="\t"))
hit=0
for r in rows:
    k=key(r["equation"]); g=idx.get(k,set())
    r["defmatch"]=";".join(sorted(g)); r["defmatch_labels"]=";".join(T[x]["name"] for x in sorted(g))
    if g: hit+=1
print("def-equation matches",hit,"of",len(rows)); print(collections.Counter(r["tier"] for r in rows if r["defmatch"]))
w=csv.DictWriter(open(f"{D}/candidates2.tsv","w"),fieldnames=list(rows[0].keys()),delimiter="\t"); w.writeheader(); w.writerows(rows)
for r in [r for r in rows if r["defmatch"]][:15]: print(r["rhea"],r["tier"],r["defmatch"],r["defmatch_labels"],"|",r["equation"][:80])
