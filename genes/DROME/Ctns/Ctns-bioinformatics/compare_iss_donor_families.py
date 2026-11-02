"""Compare family/domain assignments of Ctns (Q9VCR7) with the ISS donors of its GO rows.

FlyBase ISS rows for GO:0015171 / GO:0003333 cite FB:FBgn0026439 (Eaat1) as the
similarity partner; the UniProt ISS rows cite human CTNS (O60931). This script
queries the live UniProt REST API for PANTHER and Pfam cross-references of each
protein and prints them, so that sequence-family relatedness can be checked.

Run: uv run --with requests python compare_iss_donor_families.py
"""

import requests

QUERIES = {
    "Ctns (target)": "accession:Q9VCR7",
    "human CTNS (UniProt ISS donor)": "accession:O60931",
    "Eaat1 FBgn0026439 (FlyBase ISS donor)": "xref:flybase-FBgn0026439",
}
URL = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = "accession,gene_names,length,xref_pfam,xref_panther"

for label, query in QUERIES.items():
    r = requests.get(URL, params={"query": query, "fields": FIELDS, "format": "tsv"}, timeout=60)
    r.raise_for_status()
    rows = r.text.strip().split("\n")[1:]
    print(f"## {label}")
    for row in rows:
        acc, genes, length, pfam, panther = row.split("\t")
        print(f"{acc}\tlen={length}\tgene={genes.split()[0]}\tPfam={pfam}\tPANTHER={panther}")
    print()
