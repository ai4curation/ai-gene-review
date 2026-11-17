"""Check LnsAB seed/source preservation and assay-specific identity/role boundaries."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
TARGETS = {
    "SAOUHSC_00822": ("Q2G006", 189, "GO:0009897", "IPR056567", "NF041769"),
    "SAOUHSC_02761": ("Q2FVF3", 249, "GO:0005886", "IPR056566", "NF041768"),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(value):
    return " ".join(value.split())


def quote_entries(value):
    if isinstance(value, dict):
        if "reference_id" in value and "supporting_text" in value:
            yield value
        for child in value.values():
            yield from quote_entries(child)
    elif isinstance(value, list):
        for child in value:
            yield from quote_entries(child)


def main():
    baseline = json.loads((AUDIT / "seed-baseline.json").read_text())
    for path, expected in baseline["protected"].items():
        assert sha(ROOT / path) == expected, path
    publications = {
        f"PMID:{pmid}": norm((ROOT / f"publications/PMID_{pmid}.md").read_text())
        for pmid in (32723923, 42580408)
    }
    records = {}
    ledger = []
    for gene, (acc, length, location, family, ncbifam) in TARGETS.items():
        path = f"genes/STAA8/{gene}/{gene}-ai-review.yaml"
        doc = yaml.safe_load((ROOT / path).read_text())
        seed = baseline["reviews"][path]
        assert not seed.get("existing_annotations")
        for field in ("id", "gene_symbol", "taxon", "product_type"):
            assert doc[field] == seed[field], (path, field)
        assert doc["status"] == "COMPLETE"
        assert doc["id"] == acc and doc["taxon"]["id"] == "NCBITaxon:93061"
        raw = (ROOT / f"genes/STAA8/{gene}/{gene}-uniprot.txt").read_text()
        sequence = re.sub(r"[^A-Z]", "", raw.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0])
        assert len(sequence) == length
        official = json.loads((AUDIT / f"{acc}-official.json").read_text())["results"]
        assert len(official) == 1 and official[0]["primaryAccession"] == acc
        assert official[0]["sequence"]["value"] == sequence
        assert official[0]["organism"]["taxonId"] == 93061
        assert family in raw and ncbifam in raw and "DR   PANTHER;" not in raw
        rows = doc["existing_annotations"]
        assert [r["term"]["id"] for r in rows] == ["GO:0016747", "GO:0042158", location]
        assert [r["evidence_type"] for r in rows] == ["IDA", "IMP", "IDA"]
        assert [r["original_reference_id"] for r in rows] == ["PMID:42580408", "PMID:32723923", "PMID:42580408"]
        for row in rows:
            assert row["review"]["action"] == "NEW" and not row.get("retired", False)
            ledger.append({"gene": gene, "accession": acc, "term": row["term"]["id"],
                           "action": "NEW", "qualifier": row.get("qualifier"),
                           "evidence": row["evidence_type"], "reason": row["review"]["reason"]})
        core = doc["core_functions"][0]
        if gene == "SAOUHSC_00822":
            assert all(sequence[pos - 1] == aa for pos, aa in {27: "A", 28: "D", 60: "H", 129: "Y", 143: "C"}.items())
            assert "qualifier" not in rows[0]
            assert core["molecular_function"]["id"] == "GO:0016747"
            assert "contributes_to_molecular_function" not in core
        else:
            assert rows[0]["qualifier"] == "contributes_to"
            assert core["contributes_to_molecular_function"]["id"] == "GO:0016747"
            assert "molecular_function" not in core
            assert all(sequence[pos - 1] == aa for pos, aa in {167: "C", 168: "Q", 172: "R", 196: "E", 200: "Y", 201: "Y", 238: "Q", 242: "I"}.items())
        assert core["directly_involved_in"] == [{"id": "GO:0042158", "label": "lipoprotein biosynthetic process"}]
        assert core["locations"][0]["id"] == location
        for source in quote_entries(doc):
            if source["reference_id"] in publications:
                assert norm(source["supporting_text"]) in publications[source["reference_id"]]
            else:
                assert source["reference_id"] == f"file:STAA8/{gene}/{gene}-uniprot.txt"
                assert norm(source["supporting_text"]) in norm(raw)
                assert source["record_section"] == ["DR:NCBIfam"]
        for ref in doc["references"]:
            for finding in ref.get("findings", []):
                source = publications.get(ref["id"], norm(raw))
                assert norm(finding["supporting_text"]) in source
        records[gene] = {"accession": acc, "original_rows": 0, "new_rows": 3,
                         "review_sha256": sha(ROOT / path), "family": family,
                         "sequence_length": length, "taxon": 93061}
    bridge = json.loads((AUDIT / "epidermidis-identity-bridge.json").read_text())
    moved = []
    for gene, tag, length in [("SE_0583", "SE0583", 184), ("SE_2027", "SE2027", 272)]:
        entry = bridge[gene]
        assert entry["taxon"] == 176280 and not entry["current_gene_review"]
        assert not (ROOT / "genes/STAEP" / gene).exists()
        assert subprocess.check_output(["git", "ls-files", "--", f"genes/STAEP/{gene}"], cwd=ROOT, text=True) == ""
        raw = (AUDIT / f"{tag}-ncbi.gp").read_text()
        seq = re.sub(r"[^a-z]", "", raw.split("ORIGIN", 1)[1].split("//")[0]).upper()
        assert seq == entry["sequence"]["value"] and len(seq) == length
        assert '/db_xref="taxon:176280"' in raw
        latest = [x for x in entry["historical_uniprot"] if x["id"].startswith("A0A")]
        assert len(latest) == 1 and latest[0]["active"] is False
        assert latest[0]["geneName"] == gene
        for path, expected in entry["archived_files"].items():
            assert sha(ROOT / path) == expected
            moved.append({"from": f"genes/STAEP/{gene}/{Path(path).name}", "to": path, "sha256": expected})
        assert (AUDIT / "acquisition-failures" / gene / f"{gene}-uniprot.txt").stat().st_size == 0
    pairs = json.loads((AUDIT / "pairing-evidence.json").read_text())["cases"]
    assert [(c["A"], c["B"], c["cellular_product"]) for c in pairs] == [
        ("Sa:Q2G006", "Sa:Q2FVF3", True), ("Sa:Q2G006", "Se:AAO05668", True),
        ("Se:AAO04180", "Sa:Q2FVF3", False), ("Se:AAO04180", "Se:AAO05668", True),
    ]
    assert [c["PG_sn1_measured"] for c in pairs] == [True, False, False, False]
    assert [c["purified_reconstitution"] for c in pairs] == [True, False, False, False]
    for acc, expected in [("P23930", 5), ("Q88DN4", 1)]:
        data = json.loads((AUDIT / f"{acc}-lipoprotein-biosynthesis-comparator.json").read_text())
        assert data["numberOfHits"] == expected
        assert all(r["goId"] == "GO:0042158" and r["geneProductId"] == f"UniProtKB:{acc}" for r in data["results"])
    for term, other in [("GO0016747", "GO:0042158"), ("GO0042158", "GO:0016747")]:
        result = json.loads((AUDIT / f"{term}-ancestors.json").read_text())["results"][0]
        assert other not in result["ancestors"]
    for term in ["GO0016747", "GO0042158", "GO0009897", "GO0005886"]:
        result = json.loads((AUDIT / f"{term}-quickgo.json").read_text())["results"][0]
        assert not result.get("isObsolete", False)
    receipt = {"result": "PASS", "records": records, "original_rows": 0,
               "new_rows": 6, "protected_sources": baseline["protected"],
               "failed_acquisition_files_moved": moved,
               "scope": "Two Sa gene reviews; Se sequences are comparative controls only. No native Se phenotype or purified Se donor assay is claimed."}
    (AUDIT / "preservation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (AUDIT / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "original_rows": 0, "new_rows": 6,
                      "protected_sources": len(baseline["protected"]), "archived_failed_files": len(moved)}))


if __name__ == "__main__":
    main()
