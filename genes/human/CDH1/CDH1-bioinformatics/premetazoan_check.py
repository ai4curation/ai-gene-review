"""Premetazoan checks for CDH1 (E-cadherin).

1. Counts UniProtKB entries carrying Pfam PF01049 (Cadherin_C, the classical
   cadherin cytoplasmic beta-catenin-binding domain) in unicellular holozoan
   lineages and in Metazoa.
2. For each PANTHER PTN node behind a CDH1 IBA row, lists QuickGO annotations
   that reach unicellular holozoan proteins (withFrom = node), and for each
   protein reached reports its PANTHER subfamily and Pfam domains.

Usage: uv run python premetazoan_check.py  (stdlib only; needs network)
"""
import json
import urllib.request

TAXA = {"Choanoflagellata": 28009, "Filasterea": 2687318, "Ichthyosporea": 127916}
NODES = ["PTN000616280", "PTN000616414", "PTN008601603", "PTN002771833"]


def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode(), dict(r.headers)


def pfam_count(taxon):
    url = ("https://rest.uniprot.org/uniprotkb/search?query=xref:pfam-PF01049"
           f"+AND+taxonomy_id:{taxon}&size=1")
    _, h = get(url)
    return int({k.lower(): v for k, v in h.items()}.get("x-total-results", 0))


def quickgo(node, taxon):
    url = ("https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
           f"withFrom=PANTHER:{node}&taxonId={taxon}&taxonUsage=descendants&limit=100")
    body, _ = get(url, {"Accept": "application/json"})
    return json.loads(body)


def protein(acc):
    body, _ = get(f"https://rest.uniprot.org/uniprotkb/{acc}.json")
    d = json.loads(body)
    xr = d.get("uniProtKBCrossReferences", [])
    panther = [x["id"] for x in xr if x["database"] == "PANTHER"]
    pfam = [x["id"] + ":" + next((p["value"] for p in x.get("properties", [])
                                  if p["key"] == "EntryName"), "") for x in xr if x["database"] == "Pfam"]
    return d["organism"]["scientificName"], d["sequence"]["length"], panther, pfam


def main():
    print("## Pfam PF01049 (Cadherin_C) UniProtKB entry counts")
    for name, t in list(TAXA.items()) + [("Metazoa", 33208)]:
        print(f"{name}\t{t}\t{pfam_count(t)}")
    print("\n## QuickGO annotations with PTN node in withFrom, unicellular holozoans")
    reached = set()
    for node in NODES:
        for name, t in TAXA.items():
            d = quickgo(node, t)
            rows = sorted({(a["geneProductId"], a["goId"], a["goEvidence"], a["reference"])
                           for a in d["results"]})
            print(f"{node}\t{name}\thits={d['numberOfHits']}")
            for r in rows:
                print("\t" + "\t".join(r))
                reached.add(r[0].split(":")[1])
    print("\n## Proteins reached")
    for acc in sorted(reached):
        org, ln, panther, pfam = protein(acc)
        print(f"{acc}\t{org}\t{ln} aa\t{','.join(panther)}\t{','.join(pfam)}")
        print(f"\thas Cadherin_C (PF01049): {any(p.startswith('PF01049') for p in pfam)}")


if __name__ == "__main__":
    main()
