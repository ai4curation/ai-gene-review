# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""List WLM-domain (Pfam PF08325) proteins in S. pombe and S. cerevisiae with PANTHER
assignments, and report the HExxH...H zinc-ligand spacing in each sequence."""
import re
import requests

URL = "https://rest.uniprot.org/uniprotkb/search"
for taxon in (284812, 559292):
    r = requests.get(URL, params={
        "query": f"xref:pfam-PF08325 AND organism_id:{taxon}",
        "fields": "accession,gene_names,length,xref_panther,sequence",
        "format": "tsv"})
    r.raise_for_status()
    lines = r.text.strip().split("\n")
    for line in lines[1:]:
        acc, genes, length, panther, seq = line.split("\t")
        hits = []
        for m in re.finditer(r"HE..H", seq):
            h1 = m.start() + 1
            nxt = seq.find("H", h1 + 5)
            hits.append(f"H{h1}-E{h1+1}-H{h1+4}; next H at {nxt+1 if nxt >= 0 else None}")
        print("\t".join([str(taxon), acc, genes, length, panther, " | ".join(hits)]))
