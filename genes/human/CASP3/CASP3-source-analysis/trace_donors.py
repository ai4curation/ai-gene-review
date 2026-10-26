#!/usr/bin/env python3
"""Reproduce annotation-source tracing; annotation state is not functional evidence.

Read only GO term, reference, evidence and WITH/FROM from the normal seed TSVs;
relationship qualifiers are neither read into outputs nor interpreted. The manual
transfer-evidence-audit.tsv fixes the reviewed 37 rows. QuickGO supplies donor
bibliography, which must then be assessed from the primary publications.
"""

from pathlib import Path
import csv
import json
import requests
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def main():
    with (OUT / "transfer-evidence-audit.tsv").open() as stream:
        selected = list(csv.DictReader(stream, delimiter="\t"))
    trace = {}
    parser = YAML(typ="safe")
    for org, gene in [("human", "CASP3"), ("mouse", "Casp3")]:
        folder = ROOT / "genes" / org / gene
        review = parser.load(folder / f"{gene}-ai-review.yaml")
        with (folder / f"{gene}-goa.tsv").open() as stream:
            fields = ["GO TERM", "REFERENCE", "WITH/FROM", "GO EVIDENCE CODE"]
            sources = [
                {k: row[k] for k in fields}
                for row in csv.DictReader(stream, delimiter="\t")
            ]
        records = []
        for case in selected:
            if case["organism"] != org:
                continue
            index = int(case["row_zero_based"])
            row = review["existing_annotations"][index]
            assert row["term"]["id"] == case["go_id"]
            records.append(
                {
                    "row": index,
                    "term": row["term"],
                    "evidence": row["evidence_type"],
                    "reference": row["original_reference_id"],
                    "supporting_entities": row.get("supporting_entities", []),
                    "seed_donor_trace": [
                        source["WITH/FROM"]
                        for source in sources
                        if source["GO TERM"] == row["term"]["id"]
                        and source["REFERENCE"] == row["original_reference_id"]
                        and source["GO EVIDENCE CODE"] == row["evidence_type"]
                    ],
                }
            )
        trace[f"{org}/{gene}"] = records
    (OUT / "donor-trace.json").write_text(json.dumps(trace, indent=2) + "\n")
    records = []
    page = 1
    while True:
        response = requests.get(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            params={"geneProductId": "UniProtKB:P55213", "limit": 200, "page": page},
            headers={"Accept": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        fields = [
            "geneProductId",
            "goId",
            "goName",
            "evidenceCode",
            "reference",
            "withFrom",
            "taxonId",
            "assignedBy",
        ]
        records.extend({k: row.get(k) for k in fields} for row in data["results"])
        if page >= data["pageInfo"]["total"]:
            break
        page += 1
    (OUT / "rat-annotation-provenance.json").write_text(
        json.dumps(records, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
