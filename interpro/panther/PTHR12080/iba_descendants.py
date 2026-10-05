"""List human/mouse/rat IBA recipients of each PTHR12080 PAINT node (QuickGO)
and their current UniProt PANTHER family, to check which proteins actually
inherit each node's assertions. Writes PTHR12080-iba-descendants.tsv."""
import csv, json, urllib.request

QG = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?withFrom=PANTHER:{n}"
      "&evidenceCode=ECO:0000318&evidenceCodeUsage=descendants&taxonId=9606,10090,10116&limit=200")
UP = "https://rest.uniprot.org/uniprotkb/accessions?accessions={a}&fields=accession,xref_panther&format=tsv"

def get(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"Accept": accept})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()

nodes = sorted({row["node"] for row in csv.DictReader(open("PTHR12080-paint.tsv"), delimiter="\t")})
rows = []
for n in nodes:
    for r in json.loads(get(QG.format(n=n)))["results"]:
        rows.append((n, r["goId"], "NOT" if "not" in (r.get("qualifier") or "").lower() else "",
                     r["symbol"], r["taxonId"], r["geneProductId"].split(":")[1]))
accs = sorted({r[5] for r in rows})
fam = {}
for i in range(0, len(accs), 100):
    for line in get(UP.format(a=",".join(accs[i:i + 100])), "text/tab-separated-values").splitlines()[1:]:
        acc, pan = (line.split("\t") + [""])[:2]
        fam[acc] = ";".join(sorted(p for p in pan.split(";") if p and ":" not in p))
with open("PTHR12080-iba-descendants.tsv", "w") as out:
    out.write("node\tgo_id\tnegated\tsymbol\ttaxon\taccession\tuniprot_panther_family\n")
    for r in sorted(set(rows)):
        out.write("\t".join(map(str, r)) + "\t" + fam.get(r[5], "") + "\n")
print(f"{len(set(rows))} rows written")
