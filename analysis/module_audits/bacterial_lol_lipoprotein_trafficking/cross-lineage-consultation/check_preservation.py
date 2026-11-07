"""Audit zero-row seeds, explicitly authored proposals, and immutable sources."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
EXPECTED = {
    "CC_3705": {"GO:0140598", "GO:0044874", "GO:0030288"},
    "Fjoh_1066": {"GO:0044874", "GO:0031241"},
}


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    for name, expected in baseline["protected_files_sha256"].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    ledger = []
    for name, old in baseline["reviews"].items():
        assert not old["document"].get("existing_annotations"), name
        data = yaml.safe_load((ROOT / name).read_text())
        for slot in ["id", "gene_symbol", "taxon", "product_type"]:
            assert data[slot] == old["document"][slot], (name, slot)
        assert data["status"] == "COMPLETE", name
        rows = data["existing_annotations"]
        ids = [row["term"]["id"] for row in rows]
        assert set(ids) == EXPECTED[data["gene_symbol"]], name
        assert len(ids) == len(set(ids)), name
        for row in rows:
            assert row["review"]["action"] == "NEW", name
            assert not row.get("retired"), name
            assert row["review"]["supported_by"], name
        ledger.append({"path": name, "original_rows": 0, "NEW": len(rows), "terms": ids})
    result = {"status": "PASS", "protected_source_files": len(baseline["protected_files_sha256"]),
              "original_rows": 0, "historical_NEW": 0, "new_proposals": 5,
              "deleted_or_retired_rows": 0, "ledger": ledger,
              "source_sha256": baseline["protected_files_sha256"]}
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "source_sha256"}, indent=2))


if __name__ == "__main__":
    main()
