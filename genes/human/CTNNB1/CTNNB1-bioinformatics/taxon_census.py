"""Taxonomic census of the beta-catenin family outside animals, from UniProt.

Counts UniProtKB entries classified in PANTHER PTHR45976 (ARMADILLO SEGMENT
POLARITY PROTEIN, the beta-catenin/Armadillo family that contains human CTNNB1)
or carrying InterPro IPR013284 (Beta-catenin), split into Metazoa (NCBI 33208)
and non-Metazoa, and lists the non-metazoan entries. Also reports the PANTHER
family of Dictyostelium Aardvark (Q54I71). Uses only the public UniProt REST API.
Run: python3 taxon_census.py
"""
import urllib.request, urllib.parse

BASE = "https://rest.uniprot.org/uniprotkb/search"


def query(q, fields="accession,organism_name,organism_id,protein_name,xref_panther", size=500):
    url = f"{BASE}?query={urllib.parse.quote(q)}&fields={fields}&format=tsv&size={size}"
    with urllib.request.urlopen(url) as resp:
        total = resp.headers.get("X-Total-Results")
        body = resp.read().decode()
    rows = [l.split("\t") for l in body.strip().split("\n")[1:] if l]
    return int(total or 0), rows


for label, xref in [("PANTHER PTHR45976", "xref:panther-PTHR45976"),
                    ("InterPro IPR013284", "xref:interpro-IPR013284")]:
    n_met, _ = query(f"{xref} AND taxonomy_id:33208", size=1)
    n_non, rows = query(f"{xref} AND NOT taxonomy_id:33208")
    print(f"## {label}: Metazoa={n_met} non-Metazoa={n_non}")
    for r in rows:
        print("   ", " | ".join(r))
    for clade, tid in [("Choanoflagellata", 28009), ("Filasterea", 2687318),
                       ("Ichthyosporea", 127916), ("Dictyostelium (genus)", 5782)]:
        n, _ = query(f"{xref} AND taxonomy_id:{tid}", size=1)
        print(f"    {clade} (taxon {tid}): {n}")

_, rows = query("accession:Q54I71")
print("## Dictyostelium Aardvark Q54I71:", " | ".join(rows[0]) if rows else "not found")
