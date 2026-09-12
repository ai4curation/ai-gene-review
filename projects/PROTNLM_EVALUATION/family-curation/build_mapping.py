"""Reproduce exact-input family assignments from frozen records and baseline index.

Run from the repository root. This never infers a mapping from a gene symbol or
canonical counterpart and never edits the global PANTHER membership index.
"""

import collections
import csv
import gzip
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def main():
    scope = list(csv.DictReader((BASE / "scope.csv").open()))
    grouped = collections.defaultdict(list)
    for row in scope:
        grouped[row["accession"]].append(row)
    records = {}
    for name in ["uniprot-records.jsonl.gz", "uniprot-retries.jsonl.gz"]:
        with gzip.open(BASE / name, "rt") as stream:
            for line in stream:
                record = json.loads(line)
                if record["status"] == 200:
                    records[record["accession"]] = record["record"]
    assert set(records) == set(grouped), "Incomplete exact-accession retrieval"
    baseline = {
        r["accession"]: r["member_index_panther"]
        for r in csv.DictReader((BASE / "baseline-membership.csv").open())
    }
    rows = []
    families = collections.defaultdict(list)
    for accession, memberships in grouped.items():
        record = records[accession]
        assert record["primaryAccession"] == accession, (
            "Accession redirect requires review"
        )
        xrefs = [
            x["id"]
            for x in record.get("uniProtKBCrossReferences", [])
            if x["database"] == "PANTHER"
        ]
        previous = baseline[accession]
        identifiers = set(xrefs) | set(filter(None, previous.split(";")))
        row = dict(memberships[0])
        row.update(
            cohort=";".join(sorted({x["cohort"] for x in memberships})),
            uniprot_panther=";".join(xrefs),
            member_index_panther=previous,
            resolved_accession=accession,
            families=";".join(sorted({x.split(":")[0] for x in identifiers})),
            mapping_status="MAPPED" if identifiers else "NO_PANTHER_ASSIGNMENT",
        )
        rows.append(row)
        for family in sorted({x.split(":")[0] for x in identifiers}):
            families[family].append(row)
    with (BASE / "mapping.csv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (BASE / "family-groups.json").write_text(json.dumps(families, indent=2) + "\n")
    print(f"{len(rows)} exact accessions; {len(families)} mapped families")


if __name__ == "__main__":
    main()
