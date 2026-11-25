"""Compare Mst27D (Q8IPI4) with Drosophila Eb1 (A1Z6P3) and human MAPRE1 (Q15691).

Reports PANTHER (v19) subfamily per accession, InterPro/Pfam domain matches,
sequence length and the C-terminal 10 residues (EB family proteins end in an
EEY/F motif). Uses only public REST APIs; prints whatever is returned.

Run: python3 domain_architecture.py
"""
import json
import urllib.request

ACCS = {"Q8IPI4": 7227, "A1Z6P3": 7227, "A1ZBF1": 7227, "Q15691": 9606}


def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


for acc, taxon in ACCS.items():
    pan = json.loads(get(
        f"https://pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList={acc}&organism={taxon}"))
    g = pan["search"]["mapped_genes"]["gene"]
    seq = "".join(get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").splitlines()[1:])
    ipr = json.loads(get(f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}"))
    print(f"## {acc} length={len(seq)} PANTHER={g.get('family_id')} SF={g.get('sf_id')} C-term={seq[-10:]}")
    for r in ipr["results"]:
        m = r["metadata"]
        if m["source_database"] not in ("interpro", "pfam"):
            continue
        locs = [(f["start"], f["end"]) for p in r["proteins"]
                for loc in p["entry_protein_locations"] for f in loc["fragments"]]
        print(f"  {m['accession']}\t{m['name']}\t{locs}")
