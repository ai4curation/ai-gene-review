#!/usr/bin/env python3
"""Reproduce annotation-source tracing; annotation state is not functional evidence.

Read only GO term, reference, evidence and WITH/FROM from the normal seed TSVs;
relationship qualifiers are neither read into outputs nor interpreted. The authored
transfer-evidence-audit.yaml fixes the reviewed rows; TSV is its derived export. QuickGO supplies donor
bibliography, which must then be assessed from the primary publications.
"""

from pathlib import Path
import csv
import json
import hashlib
import requests
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def main():
    parser = YAML(typ="safe")
    selected = parser.load(OUT / "transfer-evidence-audit.yaml")["cases"]
    fields = [
        "organism",
        "gene",
        "row_zero_based",
        "go_id",
        "label",
        "action",
        "donor_trace",
        "primary_pmid",
        "primary_full_text",
        "rationale",
    ]
    pmids = sorted({pmid for case in selected for pmid in case["primary_pmids"]})
    access = []
    for pmid in pmids:
        path = ROOT / "publications" / f"PMID_{pmid}.md"
        raw = path.read_bytes()
        meta = parser.load(raw.decode().split("---", 2)[1])
        access.append(
            {
                "pmid": pmid,
                "path": str(path.relative_to(ROOT)),
                "title": meta["title"],
                "full_text_available": meta["full_text_available"],
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    full = {r["pmid"]: r["full_text_available"] for r in access}
    (OUT / "publication-access.json").write_text(json.dumps(access, indent=2) + "\n")
    with (OUT / "transfer-evidence-audit.tsv").open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=fields, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        for case in selected:
            row = {key: case[key] for key in fields if key in case}
            row["primary_pmid"] = "|".join(case["primary_pmids"])
            row["primary_full_text"] = "|".join(
                str(full[p]) for p in case["primary_pmids"]
            )
            writer.writerow(row)
    trace = {}
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
            assert row["review"]["action"] == case["action"]
            assert row["review"]["reason"] == case["rationale"]
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
    pairs = []
    for mouse in trace["mouse/Casp3"]:
        for human in trace["human/CASP3"]:
            if mouse["term"]["id"] != human["term"]["id"]:
                continue
            exact = all(
                mouse[key] == human[key]
                for key in ["evidence", "reference", "seed_donor_trace"]
            )
            pairs.append(
                {
                    "mouse_row": mouse["row"],
                    "human_row": human["row"],
                    "go_id": mouse["term"]["id"],
                    "exact_evidence_reference_donor_tuple": exact,
                    "mouse_seed_donors": mouse["seed_donor_trace"],
                    "human_seed_donors": human["seed_donor_trace"],
                }
            )
    (OUT / "cross-species-tuples.json").write_text(json.dumps(pairs, indent=2) + "\n")
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
    response = requests.get(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        params={
            "geneProductId": "UniProtKB:P42574",
            "goId": "GO:0035655,GO:0043066,GO:0072734",
            "goUsage": "exact",
            "limit": 200,
        },
        headers={"Accept": "application/json"},
        timeout=60,
    )
    response.raise_for_status()
    human = response.json()
    assert human["pageInfo"]["total"] <= 1, "Human exact-term query needs pagination"
    (OUT / "human-annotation-provenance.json").write_text(
        json.dumps(
            [{key: row.get(key) for key in fields} for row in human["results"]],
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
