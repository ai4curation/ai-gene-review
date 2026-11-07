"""Verify Lnb seed preservation, source identities and explicitly scoped evidence."""

import hashlib
import json
from pathlib import Path
import re

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
TARGETS = {
    "BACFN/BF9343_0945": ("Q5LGL3", 272559, 408),
    "BACTN/BT_4364": ("Q89ZL3", 226186, 395),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return " ".join(text.split())


def sources(value):
    if isinstance(value, dict):
        if value.get("reference_id") == "PMID:39495918":
            yield value
        for child in value.values():
            yield from sources(child)
    elif isinstance(value, list):
        for child in value:
            yield from sources(child)


def main():
    baseline = json.loads((AUDIT / "seed-baseline.json").read_text())
    for path, expected in baseline["protected"].items():
        assert sha(ROOT / path) == expected, path
    primary = normalized((ROOT / "publications/PMID_39495918.md").read_text())
    ledger = []
    records = {}
    required = {"IPR025178", "IPR057436", "PF13387", "PF25221", "NF051878"}
    for target, (accession, taxon, length) in TARGETS.items():
        gene = target.split("/")[1]
        path = f"genes/{target}/{gene}-ai-review.yaml"
        before = baseline["reviews"][path]
        doc = yaml.safe_load((ROOT / path).read_text())
        assert before.get("existing_annotations", []) == []
        for field in ("id", "gene_symbol", "product_type", "taxon"):
            assert doc[field] == before[field], (target, field)
        assert doc["status"] == "COMPLETE"
        assert doc["id"] == accession
        assert doc["taxon"]["id"] == f"NCBITaxon:{taxon}"
        official = json.loads((AUDIT / f"{gene}-uniprot-query.json").read_text())["results"]
        assert len(official) == 1
        official = official[0]
        assert official["primaryAccession"] == accession
        assert official["organism"]["taxonId"] == taxon
        sequence = official["sequence"]["value"]
        assert len(sequence) == length
        assert required <= {item["id"] for item in official["uniProtKBCrossReferences"]}
        assert not any(item["database"] == "PANTHER" for item in official["uniProtKBCrossReferences"])
        raw = (ROOT / f"genes/{target}/{gene}-uniprot.txt").read_text()
        raw_sequence = re.sub(r"[^A-Z]", "", raw.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0])
        assert raw_sequence == sequence
        rows = doc["existing_annotations"]
        assert len(rows) == 2
        assert [(row["term"]["id"], row["evidence_type"]) for row in rows] == [
            ("GO:0016747", "EXP"), ("GO:0042158", "IMP")
        ]
        for row in rows:
            assert row["review"]["action"] == "NEW"
            assert row["original_reference_id"] == "PMID:39495918"
            assert not row.get("retired", False)
            assert all(normalized(s["supporting_text"]) in primary for s in sources(row))
            ledger.append({"target": target, "term": row["term"]["id"],
                           "action": "NEW", "evidence": row["evidence_type"],
                           "reason": row["review"]["reason"]})
        for finding in doc["references"][0]["findings"]:
            assert normalized(finding["supporting_text"]) in primary
        assert doc["core_functions"][0]["molecular_function"]["id"] == "GO:0016747"
        assert doc["core_functions"][0]["directly_involved_in"][0]["id"] == "GO:0042158"
        assert doc["core_functions"][0]["locations"][0]["id"] == "GO:0016020"
        record = {"accession": accession, "taxon": taxon, "sequence_length": length,
                  "original_seed_rows": 0, "new_rows": 2,
                  "review_sha256": sha(ROOT / path)}
        if accession == "Q89ZL3":
            residues = {49: "H", 66: "N", 148: "C", 198: "C"}
            assert all(sequence[position - 1] == amino_acid for position, amino_acid in residues.items())
            record["mapped_paper_positions"] = residues
            record["experimental_mutations"] = {"C148S": "fails cellular rescue", "C198S": "retains cellular rescue"}
            record["unresolved_length_discrepancy"] = {"primary_narrative": 398, "official_sequence": 395}
        records[target] = record
    counts = {}
    for acc, expected in (("P23930", 5), ("Q88DN4", 1)):
        response = json.loads((AUDIT / f"{acc}-lipoprotein-biosynthesis-comparator.json").read_text())
        assert response["numberOfHits"] == expected
        assert all(row["geneProductId"] == f"UniProtKB:{acc}" for row in response["results"])
        assert all(row["goId"] == "GO:0042158" for row in response["results"])
        counts[acc] = expected
    for term in ("GO0016747", "GO0042158"):
        record = json.loads((AUDIT / f"{term}-ancestors.json").read_text())["results"][0]
        other = "GO:0042158" if term == "GO0016747" else "GO:0016747"
        assert other not in record.get("ancestors", [])
    result = {"result": "PASS", "records": records, "source_hashes": baseline["protected"],
              "original_rows": 0, "new_rows": 4, "same_role_exact_term_comparators": counts,
              "limits": "No donor identity, purified-Lnb activity, independently tested H49/N66 mechanism, BF residue-number transfer, or compartment-resolved topology assay is asserted."}
    (AUDIT / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    (AUDIT / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "original_rows": 0, "new_rows": 4, "protected_sources": 5}))


if __name__ == "__main__":
    main()
