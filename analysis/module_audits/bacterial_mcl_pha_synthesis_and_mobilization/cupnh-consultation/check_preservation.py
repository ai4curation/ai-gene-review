"""Recheck the H16 seed and earlier frozen consultation artifacts."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
REL = "genes/CUPNH/phaC/phaC-ai-review.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    base_path = AUDIT / "cupnh-seed-baseline.json"
    baseline = json.loads(base_path.read_text())
    old = baseline["genes"][REL]["document"]["existing_annotations"]
    doc = yaml.safe_load((ROOT / REL).read_text())
    rows = doc["existing_annotations"]

    def payload(row):
        return {key: value for key, value in row.items() if key != "review"}

    assert len(rows) == len(old) == 3
    assert [payload(r) for r in rows] == [payload(r) for r in old]
    assert [r["review"]["action"] for r in rows] == ["MODIFY", "MODIFY", "ACCEPT"]
    assert doc["status"] == "COMPLETE"
    for rel, expected in baseline["protected_files_sha256"].items():
        assert sha(ROOT / rel) == expected, rel
    original = json.loads((AUDIT / "baseline.json").read_text())
    for rel, expected in original["protected_files_sha256"].items():
        assert sha(ROOT / rel) == expected, rel
    checked = {}
    for name in ["psepk-consultation", "pseae-consultation", "class-i-consultation"]:
        p = AUDIT / name / "handoff.json"
        receipt = json.loads(p.read_text())
        for rel, expected in receipt["files"].items():
            assert sha(ROOT / rel) == expected, rel
        checked[name] = {"manifest_sha256": sha(p), "files": len(receipt["files"])}
    raw = (ROOT / "genes/CUPNH/phaC/phaC-uniprot.txt").read_text()
    sequence = "".join(
        re.findall(
            "[A-Z]+", raw.split("SQ   SEQUENCE")[1].split("\n", 1)[1].split("//")[0]
        )
    )
    ena_path = AUDIT / "class-i-consultation/J05003.embl"
    translation = re.search(r'/translation="([\s\S]+?)"', ena_path.read_text()).group(1)
    translation = re.sub(r"\s|FT", "", translation)
    assert translation == sequence and len(sequence) == 589
    result = {
        "status": "PASS",
        "ordered_original_rows": 3,
        "added_rows": 0,
        "historical_new": 0,
        "retired": 0,
        "protected_seed_sources": 2,
        "original_protected_sources": 59,
        "baseline_sha256": sha(base_path),
        "review_sha256": sha(ROOT / REL),
        "prior_frozen_handoffs": checked,
        "identity": {
            "archive": "J05003/AAA21975.1",
            "target": "P23608",
            "exact_residues": 589,
            "archive_sha256": sha(ena_path),
            "limit": "Reference sequence equality, not 2000 assay-construct audit.",
        },
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        "PASS: 3 ordered payloads, 2 raw files, 59 original sources and prior handoffs "
        "unchanged; 589aa sequence identity; no new or retired row."
    )


if __name__ == "__main__":
    main()
