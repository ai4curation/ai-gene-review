"""Assign each taxon in the CACAO snapshot to a broad group via UniProt taxonomy.

Writes projects/CACAO/data/taxon-groups.yaml, mapping NCBI taxon id to
scientific name and group (Bacteria, Archaea, Viruses, Fungi, Metazoa,
Viridiplantae, or Other eukaryote). Taxa UniProt does not return are left out.

Usage:
    uv run python projects/CACAO/scripts/fetch_taxon_groups.py [QUICKGO_TSV]
"""

import csv
import sys
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TSV = ROOT / "projects/CACAO/data/cacao-quickgo-2026-10-28.tsv"
OUT = ROOT / "projects/CACAO/data/taxon-groups.yaml"
URL = "https://rest.uniprot.org/taxonomy/search"
GROUPS = ["Bacteria", "Archaea", "Viruses", "Fungi", "Metazoa", "Viridiplantae"]


def group_of(lineage, name):
    names = set(lineage) | {name}
    for g in GROUPS:
        if g in names:
            return g
    return "Other eukaryote" if "Eukaryota" in names else "Unclassified"


def main():
    tsv = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TSV
    with open(tsv) as fh:
        taxa = sorted({r["TAXON ID"] for r in csv.DictReader(fh, delimiter="\t")}, key=int)
    out = {}
    for i in range(0, len(taxa), 50):
        chunk = taxa[i : i + 50]
        q = " OR ".join(f"tax_id:{t}" for t in chunk)
        resp = requests.get(
            URL,
            params={"query": q, "fields": "id,scientific_name,lineage", "format": "json", "size": 500},
            timeout=60,
        )
        resp.raise_for_status()
        for r in resp.json()["results"]:
            lineage = [x["scientificName"] for x in r.get("lineage", [])]
            out[int(r["taxonId"])] = {
                "name": r["scientificName"],
                "group": group_of(lineage, r["scientificName"]),
            }
    missing = [t for t in taxa if int(t) not in out]
    OUT.write_text(yaml.safe_dump(dict(sorted(out.items())), sort_keys=False, width=100))
    print(f"{len(out)} taxa grouped, {len(missing)} not returned: {missing[:20]}")


if __name__ == "__main__":
    main()
