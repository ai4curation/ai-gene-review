"""Verify ordered comparator payloads, inherited proposals and frozen sources."""

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
    baseline = json.loads((AUDIT / "baseline.json").read_text())
    result = {"genes": {}, "original_rows": 0, "protected_files": {}}
    for relative, old in baseline["genes"].items():
        current = yaml.safe_load((ROOT / relative).read_text())
        rows = current["existing_annotations"]
        payloads = [{k: v for k, v in row.items() if k != "review"} for row in rows]
        assert payloads == old["payloads"], relative
        assert current["status"] == "COMPLETE", relative
        assert current["id"] == old["document"]["id"], relative
        assert current["taxon"] == old["document"]["taxon"], relative
        for index, row in enumerate(old["document"]["existing_annotations"]):
            if row.get("review", {}).get("action") == "NEW":
                assert rows[index]["review"]["action"] == "NEW", relative
        for source, expected in old["protected"].items():
            assert sha256(ROOT / source) == expected, source
            result["protected_files"][source] = expected
        actions = Counter(row["review"]["action"] for row in rows)
        assert "PENDING" not in actions
        result["genes"][relative] = {
            "sha256": sha256(ROOT / relative),
            "rows": len(rows),
            "actions": dict(actions),
            "inherited_new": sum(
                r.get("review", {}).get("action") == "NEW"
                for r in old["document"]["existing_annotations"]
            ),
            "added_rows": 0,
        }
        result["original_rows"] += len(rows)
    for source, expected in baseline["publications"].items():
        assert sha256(ROOT / source) == expected, source
        result["protected_files"][source] = expected
    donor = json.loads((AUDIT / "A0A0H2XIE2.json").read_text())
    target_text = (ROOT / "genes/STAA8/kdpD/kdpD-uniprot.txt").read_text()
    target_sequence = "".join(target_text.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//", 1)[0].split())
    assert target_sequence == donor["sequence"]["value"]
    assert len(target_sequence) == 885
    result["identical_donor_target_residues"] = len(target_sequence)
    result["ordered_payloads_and_sources_preserved"] = True
    (AUDIT / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
