"""Verify original RHIME payloads, approved retirement, sources and sequence bridge."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml
from Bio import SeqIO

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((AUDIT / "baseline.json").read_text())
    results = {"genes": {}, "original_rows": 0, "protected_files": {}, "added_rows": 0}
    for relative, old in baseline["genes"].items():
        path = ROOT / relative
        current = yaml.safe_load(path.read_text())
        rows = current["existing_annotations"]
        payloads = [{k: v for k, v in row.items() if k not in {"review", "retired"}} for row in rows]
        assert payloads == old["payloads"], relative
        assert sum(bool(r.get("retired")) for r in rows) == (1 if current["id"] == "Q92NF6" else 0)
        assert current["status"] == "COMPLETE", relative
        assert current["id"] == old["document"]["id"], relative
        assert current["taxon"] == old["document"]["taxon"], relative
        assert path.with_name(current["gene_symbol"] + "-notes.md").read_text().startswith(
            old["notes_text"]
        )
        retired = []
        for index, original in enumerate(old["document"]["existing_annotations"]):
            if original["review"]["action"] == "NEW":
                assert rows[index]["review"]["action"] == "NEW", relative
            if rows[index].get("retired"):
                assert current["id"] == "Q92NF6" and index == 3
                archive = yaml.safe_load(
                    (path.parent / "bcoG-source-analysis/historical-process-proposal.yaml").read_text()
                )
                assert archive["original_row"] == original
                retired.append(index)
        for source, expected in old["protected"].items():
            assert sha256(ROOT / source) == expected, source
            results["protected_files"][source] = expected
        assert not list(path.parent.glob("*-deep-research-*.md")), "Unexpected provider file"
        actions = Counter(r["review"]["action"] for r in rows)
        assert "PENDING" not in actions
        results["genes"][relative] = {
            "sha256": sha256(path),
            "original_rows": len(rows),
            "actions": dict(actions),
            "historical_new": sum(r["review"]["action"] == "NEW" for r in rows),
            "approved_retired_indices": retired,
        }
        results["original_rows"] += len(rows)
    for source, expected in baseline["publications"].items():
        assert sha256(ROOT / source) == expected, source
        results["protected_files"][source] = expected
    record = SeqIO.read(AUDIT / "CP004140.1-2423202-2443202.gb", "genbank")
    comparisons = []
    for feature in record.features:
        locus = feature.qualifiers.get("locus_tag", [""])[0]
        if feature.type != "CDS" or locus not in {"SM2011_c01637", "SM2011_c01638"}:
            continue
        gene = "bcoG" if locus.endswith("01637") else "bcoE-bcoF"
        raw = (ROOT / f"genes/RHIME/{gene}/{gene}-uniprot.txt").read_text()
        sequence = "".join(raw.split("SQ   SEQUENCE")[1].split("\n", 1)[1].split("//")[0].split())
        assert sequence == feature.qualifiers["translation"][0], gene
        comparisons.append({"gene": gene, "identical_residues": len(sequence), "locus": locus})
    assert len(comparisons) == 2
    results["sequence_bridges"] = comparisons
    results["payloads_and_sources_preserved"] = True
    (AUDIT / "preservation-results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
