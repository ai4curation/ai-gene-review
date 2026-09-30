"""Summarize a frozen ProtNLM accession list and matching API responses.

Run from this directory: python summarize.py
Counts records and statements, not genes or biological correctness.
"""

import csv
import gzip
import json
from collections import Counter
from pathlib import Path


def summarize(metadata, payloads):
    by_accession = {p["primaryAccession"]: p for p in payloads}
    if len(by_accession) != len(payloads):
        raise ValueError("Duplicate accession in prediction snapshot")
    expected = {r["Entry"] for r in metadata}
    if expected != set(by_accession):
        raise ValueError("Accession list and prediction snapshot do not match")
    inventory = []
    predictions = []
    for row in metadata:
        acc = row["Entry"]
        data = by_accession[acc]
        description = data.get("proteinDescription", {})
        name = description.get("recommendedName", {}).get("fullName", {}).get("value", "")
        if not name:
            submitted = description.get("submissionNames", [])
            name = submitted[0].get("fullName", {}).get("value", "") if submitted else ""
        counts = Counter()
        for ref in data.get("uniProtKBCrossReferences", []):
            if ref.get("database") != "GO":
                continue
            props = {p["key"]: p["value"] for p in ref.get("properties", [])}
            label = props.get("GoTerm", "")
            aspect = label.split(":", 1)[0]
            counts["go"] += 1
            counts["go_" + aspect] += 1
            predictions.append({"accession": acc, "taxon_id": row["Organism (ID)"],
                                "type": "GO", "id": ref["id"], "text": label})
        for comment in data.get("comments", []):
            if comment.get("commentType") == "FUNCTION":
                for value in comment.get("texts", []):
                    counts["function"] += 1
                    predictions.append({"accession": acc, "taxon_id": row["Organism (ID)"],
                                        "type": "function", "id": "", "text": value["value"]})
            elif comment.get("commentType") == "SUBCELLULAR LOCATION":
                for value in comment.get("subcellularLocations", []):
                    location = value.get("location", {})
                    counts["location"] += 1
                    predictions.append({"accession": acc, "taxon_id": row["Organism (ID)"],
                                        "type": "location", "id": location.get("id", ""),
                                        "text": location.get("value", "")})
        for keyword in data.get("keywords", []):
            counts["keyword"] += 1
            predictions.append({"accession": acc, "taxon_id": row["Organism (ID)"],
                                "type": "keyword", "id": keyword["id"], "text": keyword["name"]})
        inventory.append({"accession": acc, "taxon_id": row["Organism (ID)"],
                          "organism": row["Organism"], "gene_names": row["Gene Names"],
                          "release_length": row["Length"], "predicted_name": name,
                          "go_count": counts["go"], "go_mf": counts["go_F"],
                          "go_bp": counts["go_P"], "go_cc": counts["go_C"],
                          "function_count": counts["function"],
                          "location_count": counts["location"],
                          "keyword_count": counts["keyword"],
                          "name_only": int(not any(counts.values()))})
    species = []
    for taxon in sorted({r["taxon_id"] for r in inventory}):
        records = [r for r in inventory if r["taxon_id"] == taxon]
        species.append({"taxon_id": taxon, "organism": records[0]["organism"],
                        "records": len(records),
                        "with_go": sum(r["go_count"] > 0 for r in records),
                        "go_statements": sum(r["go_count"] for r in records),
                        "with_function": sum(r["function_count"] > 0 for r in records),
                        "with_location": sum(r["location_count"] > 0 for r in records),
                        "with_keyword": sum(r["keyword_count"] > 0 for r in records),
                        "name_only": sum(r["name_only"] for r in records)})
    return inventory, predictions, species


def main():
    root = Path(__file__).parent
    with (root / "accessions.tsv").open() as handle:
        metadata = list(csv.DictReader(handle, delimiter="\t"))
    with gzip.open(root / "predictions.jsonl.gz", "rt") as handle:
        payloads = [json.loads(line) for line in handle]
    inventory, predictions, species = summarize(metadata, payloads)
    for name, rows in [("inventory.csv", inventory), ("prediction-statements.csv", predictions),
                       ("species-counts.csv", species)]:
        with (root / name).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(species, indent=2))


if __name__ == "__main__":
    main()
