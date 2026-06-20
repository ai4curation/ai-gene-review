"""Fetch broad taxonomic lineage for taxon IDs from UniProt taxonomy API.

Produces: lineage.tsv (taxon_id, organism, broad_group)
"""

import csv
import json
import time
import urllib.request
from pathlib import Path

# Ordered: first match wins
LINEAGE_GROUPS = [
    ("Mammalia", "Mammal"),
    ("Aves", "Bird"),
    ("Amphibia", "Amphibian"),
    ("Actinopterygii", "Ray-finned fish"),
    ("Chondrichthyes", "Cartilaginous fish"),
    ("Vertebrata", "Other vertebrate"),
    ("Insecta", "Insect"),
    ("Nematoda", "Nematode"),
    ("Mollusca", "Mollusc"),
    ("Arthropoda", "Other arthropod"),
    ("Metazoa", "Other animal"),
    ("Fungi", "Fungus"),
    ("Streptophyta", "Land plant"),
    ("Chlorophyta", "Green alga"),
    ("Viridiplantae", "Plant (other)"),
    ("Euglenozoa", "Euglenozoan"),
    ("Alveolata", "Alveolate"),
    ("Stramenopiles", "Stramenopile"),
    ("Rhodophyta", "Red alga"),
    ("Archaea", "Archaeon"),
    ("Bacteria", "Bacterium"),
    ("Viruses", "Virus"),
]


def classify_lineage(lineage_names: list[str]) -> str:
    for ancestor, group in LINEAGE_GROUPS:
        if ancestor in lineage_names:
            return group
    return "Other"


def fetch_taxon(taxon_id: int) -> tuple[str, list[str]]:
    url = f"https://rest.uniprot.org/taxonomy/{taxon_id}?format=json"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    sci_name = data.get("scientificName", "")
    lineage = [node.get("scientificName", "") for node in data.get("lineage", [])]
    return sci_name, lineage


def main():
    import pandas as pd

    base = Path(__file__).parent
    taxonomy = pd.read_csv(base / "taxonomy.tsv", sep="\t")
    unique_taxids = taxonomy["taxon_id"].dropna().astype(int).unique()

    out_path = base / "lineage.tsv"
    done = {}
    if out_path.exists():
        with open(out_path) as f:
            for row in csv.DictReader(f, delimiter="\t"):
                done[int(row["taxon_id"])] = row["broad_group"]
        print(f"{len(done)} already fetched")

    remaining = [t for t in unique_taxids if t not in done]
    print(f"Fetching lineage for {len(remaining)}/{len(unique_taxids)} taxon IDs...")

    results = dict(done)
    for i, taxid in enumerate(remaining):
        try:
            _, lineage = fetch_taxon(taxid)
            group = classify_lineage(lineage)
            results[taxid] = group
        except Exception as e:
            print(f"  Error for {taxid}: {e}")
            results[taxid] = "Unknown"

        if (i + 1) % 50 == 0:
            print(f"  {i + 1}/{len(remaining)}")
        time.sleep(0.3)

    # Write all results
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["taxon_id", "broad_group"])
        for taxid in sorted(results):
            w.writerow([taxid, results[taxid]])

    from collections import Counter
    counts = Counter(results.values())
    print(f"\nDone. Group distribution:")
    for group, n in counts.most_common():
        print(f"  {n:4d}  {group}")


if __name__ == "__main__":
    main()
