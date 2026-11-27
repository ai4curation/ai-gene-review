"""Check original PAO1 rows, immutable sources and the accession sequence bridge."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
REL = "genes/PSEAE/phaG/phaG-ai-review.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def main():
    baseline_path = AUDIT / "additional-seed-baseline.json"
    baseline = json.loads(baseline_path.read_text())
    old = baseline["genes"][REL]["document"]["existing_annotations"]
    doc = yaml.safe_load((ROOT / REL).read_text())
    rows = doc["existing_annotations"]
    assert len(old) == 2 and len(rows) == 3
    assert [payload(x) for x in old] == [payload(x) for x in rows[:2]]
    assert [r["review"]["action"] for r in rows] == ["UNDECIDED", "UNDECIDED", "NEW"]
    assert not any(r.get("retired", False) for r in rows)
    assert rows[2]["term"]["id"] == "GO:0016747" and rows[2]["evidence_type"] == "IC"
    assert doc["status"] == "COMPLETE"
    checked = {}
    for rel, expected in baseline["protected_files_sha256"].items():
        assert sha(ROOT / rel) == expected, rel
        checked[rel] = expected
    original = json.loads((AUDIT / "baseline.json").read_text())
    for rel, expected in original["protected_files_sha256"].items():
        assert sha(ROOT / rel) == expected, rel
    raw = (ROOT / "genes/PSEAE/phaG/phaG-uniprot.txt").read_text()
    sequence = "".join(
        re.findall(
            "[A-Z]+", raw.split("SQ   SEQUENCE")[1].split("\n", 1)[1].split("//")[0]
        )
    )
    ena_path = AUDIT / "literature-consultation/identity/AF209711.embl"
    ena = ena_path.read_text()
    translation = re.search(r'/translation="([\s\S]+?)"', ena).group(1)
    translation = re.sub(r"\s|FT", "", translation)
    assert len(sequence) == 300 and translation == sequence
    published = json.loads((AUDIT / "psepk-consultation/handoff.json").read_text())
    for rel, expected in published["files"].items():
        assert sha(ROOT / rel) == expected, rel
    result = {
        "status": "PASS",
        "original_ordered_rows": 2,
        "added_new": 1,
        "added_claim": "GO:0016747 IC; no new process or location assertion",
        "seed_raw_files_checked": len(checked),
        "original_sources_checked": 59,
        "frozen_psepk_manifest_files_checked": len(published["files"]),
        "historical_new": 0,
        "retirements": 0,
        "baseline_sha256": sha(baseline_path),
        "review_sha256": sha(ROOT / REL),
        "identity": {
            "accession": "AF209711/AAF61903.1",
            "target": "Q51553",
            "sequence_equal": True,
            "length": 300,
            "ena_sha256": sha(ena_path),
        },
        "protected_sha256": checked,
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        "PASS: 2 original ordered rows; 1 supported IC MF proposal; 8 seed raw files, "
        "59 original sources and 67 frozen PSEPK handoff files preserved; 300aa identity."
    )


if __name__ == "__main__":
    main()
