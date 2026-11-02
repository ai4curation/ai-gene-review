"""PP_0149 (Q88RI0) DUF7844 (PF25226) family analysis.
- Fetch every UniProtKB member of PF25226 (sequence, Pfam xrefs, lineage).
- Report domain-architecture and taxonomic breadth.
- Globally align Q88RI0 to one member per genus (plus PA5464 and Smlt2198) and report conservation of
  candidate catalytic residues: the DUF7844 HExxH (H123/E124/H127; M90-like metallopeptidase motif per
  InterPro) and every His/Cys/Asn-Cys in the Lnb_N region (272-430; InterPro: conserved His + NCT motif,
  papain-like Asn-His-Cys).
- Signal peptide/lipobox check on the N-terminus.
Usage: /opt/conda/bin/python -I domain_family.py OUTDIR"""
import json, os, re, sys, urllib.request, collections
from Bio import Align
from Bio.Align import substitution_matrices

out = sys.argv[1]
os.makedirs(out, exist_ok=True)
UA = {"User-Agent": "curl/8.5.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=300) as r:
        return r.read().decode(), r.headers


url = ("https://rest.uniprot.org/uniprotkb/search?query=xref:pfam-PF25226&format=json&size=500"
       "&fields=accession,gene_oln,organism_name,lineage,length,xref_pfam,sequence,ft_signal,ft_transmem")
entries = []
while url:
    txt, h = get(url)
    entries += json.loads(txt)["results"]
    m = re.search(r'<([^>]+)>; rel="next"', h.get("Link", "") or "")
    url = m.group(1) if m else None
rows = []
for e in entries:
    lin = [x["scientificName"] for x in e.get("lineages", [])] if e.get("lineages") else []
    lin_rank = {x.get("rank"): x["scientificName"] for x in e.get("lineages", [])}
    pf = sorted({x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "Pfam"})
    feats = e.get("features", [])
    rows.append({"acc": e["primaryAccession"], "org": e["organism"]["scientificName"],
                 "phylum": lin_rank.get("phylum"), "class": lin_rank.get("class"), "genus": lin_rank.get("genus"),
                 "len": e["sequence"]["length"], "pfam": pf, "seq": e["sequence"]["value"],
                 "signal": any(f["type"] == "Signal" for f in feats),
                 "n_tm": sum(1 for f in feats if f["type"] == "Transmembrane")})
res = {"n_members": len(rows)}
res["architectures"] = collections.Counter(";".join(r["pfam"]) for r in rows).most_common(15)
res["frac_with_PF13387_Lnb_N"] = round(sum("PF13387" in r["pfam"] for r in rows) / len(rows), 3)
res["frac_with_signal"] = round(sum(r["signal"] for r in rows) / len(rows), 3)
res["frac_with_any_TM"] = round(sum(r["n_tm"] > 0 for r in rows) / len(rows), 3)
res["phyla"] = collections.Counter(r["phylum"] for r in rows).most_common()
res["classes"] = collections.Counter(r["class"] for r in rows).most_common()
res["n_genera"] = len({r["genus"] for r in rows})
res["length_median"] = sorted(r["len"] for r in rows)[len(rows) // 2]

q = [r for r in rows if r["acc"] == "Q88RI0"][0]["seq"]
aligner = Align.PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                                open_gap_score=-11, extend_gap_score=-1)
aligner.end_gap_score = 0
# Positions of interest (1-based, Q88RI0)
poi = {"H123": 123, "E124": 124, "H127": 127}
for i, c in enumerate(q, 1):
    if 272 <= i <= 430 and c in "HC":
        poi[f"{c}{i}"] = i
for m in re.finditer("N(?=C)", q):
    poi[f"N{m.start() + 1}(NC)"] = m.start() + 1
# glutamates 20-80 aa after HExxH (M90/gluzincin-like third ligand candidates)
for i in range(140, 210):
    if q[i - 1] == "E":
        poi[f"E{i}"] = i
pick, seen = [], set()
for r in rows:
    if r["acc"] in ("Q9HTA6", "B2FPQ3"):
        pick.append(r)
        seen.add(r["genus"] + "_forced")
for r in sorted(rows, key=lambda r: r["acc"]):
    if r["genus"] not in seen and r["acc"] != "Q88RI0":
        seen.add(r["genus"])
        pick.append(r)
aln_rows = []
for r in pick:
    a = aligner.align(q, r["seq"])[0]
    m = {}
    ident = alnd = 0
    for (qs, qe), (ss, se) in zip(*a.aligned):
        for k in range(qe - qs):
            m[qs + k + 1] = r["seq"][ss + k]
            alnd += 1
            ident += q[qs + k] == r["seq"][ss + k]
    aln_rows.append({"acc": r["acc"], "org": r["org"], "class": r["class"], "pfam": r["pfam"], "len": r["len"],
                     "pct_id": round(100 * ident / alnd, 1), "aligned": alnd,
                     "residues": {k: m.get(p, "-") for k, p in poi.items()}})
res["n_aligned_reps"] = len(aln_rows)
cons = {}
for k, p in poi.items():
    col = [a["residues"][k] for a in aln_rows]
    cons[k] = {"query": q[p - 1], "frac_identical": round(sum(c == q[p - 1] for c in col) / len(col), 3),
               "counts": collections.Counter(col).most_common(4)}
res["conservation"] = cons
res["reps"] = aln_rows
res["nterm"] = {"first40": q[:40], "lipobox_LxxC_at_20_25": bool(re.search("[LVI][ASTVI][GAS]C", q[15:28]))}
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
with open(os.path.join(out, "pf25226_members.tsv"), "w") as f:
    f.write("acc\torg\tphylum\tclass\tgenus\tlen\tpfam\tsignal\tn_tm\n")
    for r in rows:
        f.write("\t".join(map(str, [r["acc"], r["org"], r["phylum"], r["class"], r["genus"], r["len"], ";".join(r["pfam"]), r["signal"], r["n_tm"]])) + "\n")
print(json.dumps({k: v for k, v in res.items() if k != "reps"}, indent=1))
for a in aln_rows[:6]:
    print(a["acc"], a["org"], a["pct_id"], a["aligned"])
