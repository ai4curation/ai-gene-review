# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""List Neurospora crassa OR74A (taxon 367110) proteins carrying SMN-complex / Sm-assembly signatures.

Queries UniProt live for Pfam signatures; nothing is hardcoded except the Pfam ids queried.
  PF06003 SMN (survival motor neuron Tudor-containing core)
  PF20635 SMN Gemin2-binding domain
  PF04938 SIP1 (Gemin2 / yeast Brr1 family)
Also reports PANTHER subfamily placement of SmG proteins used for evolutionary grounding.
"""
import requests

BASE = "https://rest.uniprot.org/uniprotkb"
PFAM = {"PF06003": "SMN", "PF20635": "SMN Gemin2-binding domain", "PF04938": "SIP1 (Gemin2/Brr1)"}
SMG = ["Q7S234", "P40204", "O74966", "Q9VXE0", "P62308"]

for pf, name in PFAM.items():
    r = requests.get(
        f"{BASE}/search",
        params={"query": f"organism_id:367110 AND xref:pfam-{pf}", "fields": "accession,gene_names,protein_name,length", "format": "tsv"},
        timeout=60,
    )
    r.raise_for_status()
    rows = r.text.strip().splitlines()[1:]
    print(f"{pf}\t{name}\thits={len(rows)}")
    for row in rows:
        print(f"  {row}")

for acc in SMG:
    r = requests.get(f"{BASE}/{acc}.txt", timeout=60)
    r.raise_for_status()
    lines = r.text.splitlines()
    os_line = next(l for l in lines if l.startswith("OS   "))
    panther = [l for l in lines if l.startswith("DR   PANTHER")]
    print(acc, os_line[5:].strip())
    for p in panther:
        print(f"  {p}")
