"""Boolean completeness of the F-type ATP synthase across bacterial reference proteomes."""
import csv, re, collections as C

F = ["alpha", "beta", "gamma", "delta", "epsilon", "a", "b", "c"]
def members(path):
    hits = C.defaultdict(list)
    for r in csv.DictReader(open(path), delimiter="\t"):
        for up in re.findall(r"UP\d+", r["Proteomes"]):
            hits[up].append(r)
    return hits

prot = {r["Proteome Id"]: r for r in csv.DictReader(open("proteomes.tsv"), delimiter="\t")}
def busco_c(s):
    m = re.match(r"C:([\d.]+)%", s or "")
    return float(m.group(1)) if m else None
good = {u for u, r in prot.items() if (busco_c(r["BUSCO"]) or 0) >= 95}
print(f"bacterial reference proteomes: {len(prot)}; BUSCO C>=95%: {len(good)}")

fam = {n: members(f"fam_{n}.tsv") for n in F + ["V_alpha", "V_beta"]}
go = members("go_0046933.tsv")

def phylum(u):
    lin = [x.strip() for x in prot[u]["Taxonomic lineage"].split(",")]
    return lin[4] if len(lin) > 4 else "?"

for label, U in [("all", set(prot)), ("BUSCO>=95", good)]:
    n_sub = C.Counter(sum(u in fam[s] for s in F) for u in U)
    print(f"\n[{label}] n={len(U)}  proteomes by # of 8 F-type subunit families present:")
    for k in sorted(n_sub): print(f"  {k}: {n_sub[k]}")
    for s in F: print(f"  {s:8s} present in {sum(u in fam[s] for u in U)/len(U):.4f}")

U = good
complete = {u for u in U if all(u in fam[s] for s in F)}
none = {u for u in U if not any(u in fam[s] for s in F)}
partial = U - complete - none
hasV = {u for u in U if u in fam["V_alpha"] and u in fam["V_beta"]}
print(f"\ncomplete F-type: {len(complete)}  none: {len(none)}  partial: {len(partial)}")
print(f"of 'none', have V/A-type catalytic pair: {len(none & hasV)}")
print(f"of 'partial', have V/A-type catalytic pair: {len(partial & hasV)}")

# 'Truth' (first-principles/structural): the organism encodes a complete F-type complex.
# 'Prediction': any protein in the proteome is annotated GO:0046933 (mostly InterPro2GO IEA).
pred = {u for u in U if u in go}
tp, fp, fn = len(pred & complete), len(pred - complete), len(complete - pred)
print(f"\nproteome-level: TP={tp} FP={fp} FN={fn} precision={tp/(tp+fp):.4f} recall={tp/(tp+fn):.4f}")

# protein-level: GO:0046933 proteins that are not in any of the 8 F-type families
Fipr = {"IPR005294","IPR005722","IPR000131","IPR000711","IPR001469","IPR000568","IPR002146","IPR000454"}
odd = C.Counter()
for r in csv.DictReader(open("go_0046933.tsv"), delimiter="\t"):
    if not Fipr & set(filter(None, r["InterPro"].split(";"))):
        odd[r["Protein names"].split(" (")[0]] += 1
print(f"\nGO:0046933 proteins outside the 8 F-type families: {sum(odd.values())}")
for k, v in odd.most_common(15): print(f"  {v:6d}  {k}")

def show(title, S, n=40):
    print(f"\n{title} ({len(S)}), by phylum:", C.Counter(phylum(u) for u in S).most_common(12))
    for u in sorted(S, key=lambda u: prot[u]["Organism"])[:n]:
        miss = [s for s in F if u not in fam[s]]
        print(f"  {u} {prot[u]['Organism'][:60]:60s} missing={','.join(miss) if len(miss)<8 else 'ALL'} V/A={'y' if u in hasV else 'n'}")
show("NO F-type subunits", none)
show("PARTIAL F-type", partial)
