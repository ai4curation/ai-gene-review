"""Reproduce accession/sequence identity checks using public UniProt records.

Run with the repository environment. Default uses adjacent recorded JSON;
--refresh retrieves the four records normally from UniProt. No curated review,
GOA, or flat-file source is modified.
"""

import argparse
import hashlib
import json
from pathlib import Path

import requests

p = Path(__file__).parent
ap = argparse.ArgumentParser()
ap.add_argument("--refresh", action="store_true")
args = ap.parse_args()
accessions = ["Q59104", "Q0KBD6", "Q9RBF6", "Q0K2K1"]
data = {}
for acc in accessions:
    file = p / f"{acc}.json"
    if args.refresh:
        response = requests.get(
            f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60
        )
        response.raise_for_status()
        record = response.json()
        assert record["primaryAccession"] == acc
        file.write_text(json.dumps(record, indent=2) + "\n")
    data[acc] = json.loads(file.read_text())
report = {
    "source": "Public current UniProt JSON; primary sequence/reference identity, not GO annotation support",
    "record_sha256": {
        a: hashlib.sha256((p / f"{a}.json").read_bytes()).hexdigest()
        for a in accessions
    },
    "comparisons": [],
}
for left, right in [("Q59104", "Q0KBD6"), ("Q9RBF6", "Q0K2K1")]:
    a = data[left]["sequence"]["value"]
    b = data[right]["sequence"]["value"]
    report["comparisons"].append(
        {
            "published_accession": left,
            "genome_accession": right,
            "lengths": [len(a), len(b)],
            "identical_sequences": a == b,
            "position_wise_identical": sum(x == y for x, y in zip(a, b)),
            "mismatch_positions_1_based": [
                i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y
            ],
        }
    )
(p / "sequence-identity-proof.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
