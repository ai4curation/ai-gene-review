"""Recompute exact-sequence and shared-gene checks for unassigned benchmark inputs.

Uses only frozen source responses. Canonical context never assigns a family to
an unassigned exact target. Run from any directory with Python 3.10+.
"""

import gzip
import hashlib
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent


def gene_ids(record):
    result = set()
    for xref in record.get("uniProtKBCrossReferences", []):
        database = xref["database"]
        if database in {"WormBase", "Ensembl"}:
            result.update(
                (database, prop["value"])
                for prop in xref.get("properties", [])
                if prop["key"] == "GeneId"
            )
        elif database in {"HGNC", "MGI", "FlyBase", "PomBase", "VGNC"}:
            result.add((database, xref["id"]))
    return result


def main():
    result = json.loads((BASE / "unassigned-results.json").read_text())
    records = {}
    for name in ["uniprot-records.jsonl.gz", "uniprot-retries.jsonl.gz"]:
        with gzip.open(BASE / name, "rt") as handle:
            for line in handle:
                response = json.loads(line)
                if response.get("status") == 200:
                    records[response["accession"]] = response["record"]
    with gzip.open(BASE / "unmapped-sources.jsonl.gz", "rt") as handle:
        for line in handle:
            response = json.loads(line)
            for record in response.get("response", {}).get("results", []):
                records[record["primaryAccession"]] = record
    assert len(result["cases"]) == 18
    for case in result["cases"]:
        record = records[case["accession"]]
        assert not any(
            ref["database"] == "PANTHER"
            for ref in record.get("uniProtKBCrossReferences", [])
        ), case["accession"]
        assert case["length"] == record["sequence"]["length"]
    relationships = (
        result["verified_same_gene_bridges"]
        + result["distinct_locus_sequence_relationships"]
    )
    for bridge in relationships:
        target = records[bridge["target_accession"]]
        context = records[bridge["context_accession"]]
        shared = gene_ids(target) & gene_ids(context)
        if bridge["relationship"] == "SAME_GENE_CONTEXT_ONLY":
            assert sorted(shared) == [
                tuple(value) for value in bridge["shared_gene_identifiers"]
            ]
            assert shared
        else:
            assert not shared
        query = target["sequence"]["value"]
        subject = context["sequence"]["value"]
        position = subject.find(query)
        assert bridge["exact_target_substring_start_1based"] == (
            position + 1 if position >= 0 else None
        )
        assert bridge["exact_target_substring_end_1based"] == (
            position + len(query) if position >= 0 else None
        )
        if "common_prefix_length" in bridge:
            assert bridge["common_prefix_length"] == len(
                os.path.commonprefix([query, subject])
            )
        assert (
            hashlib.sha256(query.encode()).hexdigest()
            == bridge["target_sequence_sha256"]
        )
        assert (
            hashlib.sha256(subject.encode()).hexdigest()
            == bridge["context_sequence_sha256"]
        )
    assert (
        hashlib.sha256((BASE / "unmapped-sources.jsonl.gz").read_bytes()).hexdigest()
        == result["sources"]["additional_sources_sha256"]
    )
    print(
        "Validated 18 unassigned exact targets, 3 same-gene bridges, and 1 distinct-locus terminal relationship."
    )


if __name__ == "__main__":
    main()
