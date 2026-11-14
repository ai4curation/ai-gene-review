"""Verify immutable NA1000 seed payloads and protected source bytes.

Run with: uv run python analysis/module_audits/bacterial_kdp_potassium_homeostasis/caulobacter-consultation/check_preservation.py
"""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((AUDIT / "seed-baseline.json").read_text())
    results = {"genes": {}, "historical_rows": 0, "added_rows": 0, "raw_files": 0}
    for relative, original in baseline["genes"].items():
        path = ROOT / relative
        review = yaml.safe_load(path.read_text())
        payloads = [
            {key: value for key, value in row.items() if key != "review"}
            for row in review["existing_annotations"]
        ]
        assert payloads == original["payloads"], f"Changed ordered payloads: {relative}"
        assert review["status"] == "COMPLETE", relative
        assert review["id"] == original["seed_document"]["id"], relative
        assert review["taxon"]["id"] == "NCBITaxon:565050", relative
        assert all(row["review"]["action"] != "PENDING" for row in review["existing_annotations"])
        for raw, expected in original["raw_sha256"].items():
            assert sha256(ROOT / raw) == expected, f"Changed raw source: {raw}"
            results["raw_files"] += 1
        assert not list(path.parent.glob("*-deep-research-*.md")), "Unexpected provider artifact"
        actions = Counter(row["review"]["action"] for row in review["existing_annotations"])
        results["genes"][relative] = {
            "sha256": sha256(path),
            "original_rows": len(payloads),
            "actions": dict(actions),
            "inherited_new": sum(
                row.get("review", {}).get("action") == "NEW"
                for row in original["seed_document"]["existing_annotations"]
            ),
            "added_new": 0,
        }
        results["historical_rows"] += len(payloads)
    for source, expected in baseline["protected_publications"].items():
        assert sha256(ROOT / source) == expected, f"Changed publication: {source}"
    results["protected_publications"] = baseline["protected_publications"]
    results["payloads_and_sources_preserved"] = True
    (AUDIT / "preservation-results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
