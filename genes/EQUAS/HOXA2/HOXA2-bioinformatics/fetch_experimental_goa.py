"""Fetch experimental GO annotations (ECO:0000269 and descendants: EXP/IDA/IPI/IMP/IGI/IEP)
for ortholog accessions from QuickGO, look up GO term names, and print one line per
distinct annotation.

Usage: python fetch_experimental_goa.py <out_tsv> <ACC1,ACC2,...>
Output lines: accession symbol qualifier GO-id "GO name" evidence reference
"""
import sys, json, urllib.request, csv, io
out, accs = sys.argv[1], sys.argv[2]
url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?geneProductId=" + accs +
       "&evidenceCode=ECO:0000269&evidenceCodeUsage=descendants")
req = urllib.request.Request(url, headers={"Accept": "text/tsv"})
txt = urllib.request.urlopen(req).read().decode()
open(out, "w").write(txt)
rows = list(csv.DictReader(io.StringIO(txt), delimiter="\t"))
ids = sorted({r["GO TERM"] for r in rows})
names = {}
for i in range(0, len(ids), 50):
    u = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/" + ",".join(ids[i:i+50])
    for t in json.load(urllib.request.urlopen(u))["results"]:
        names[t["id"]] = t["name"]
seen = []
for r in rows:
    line = (f"{r['GENE PRODUCT ID']} {r['SYMBOL']} {r['QUALIFIER']} {r['GO TERM']} "
            f"\"{names.get(r['GO TERM'], '?')}\" {r['GO EVIDENCE CODE']} {r['REFERENCE']}")
    if line not in seen:
        seen.append(line)
for line in sorted(seen):
    print(line)
