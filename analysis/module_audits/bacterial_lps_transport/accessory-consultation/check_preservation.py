"""Verify two accessory reviews without changing protected inputs or prior handoffs."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(rows):
    return [{k: v for k, v in row.items() if k != "review"} for row in rows]


def main():
    seed = json.loads((HERE / "seed-baseline.json").read_text())
    original = json.loads((HERE.parent / "baseline.json").read_text())
    sources = original["protected_files_sha256"] | seed["protected_sources"]
    consulted = json.loads((HERE / "consulted-source-hashes.json").read_text())
    sources.update(consulted)
    for path, expected in sources.items():
        assert sha(ROOT / path) == expected, path
    count = 0
    actions = Counter()
    for path, entry in seed["genes"].items():
        before = entry["document"]["existing_annotations"]
        doc = yaml.safe_load((ROOT / path).read_text())
        after = doc["existing_annotations"]
        assert payloads(before) == payloads(after), path
        assert doc["status"] == "COMPLETE", path
        assert len(after) == len(before), path
        count += len(after)
        actions.update(row["review"]["action"] for row in after)
    assert "NEW" not in actions and "PENDING" not in actions
    bridges = json.loads((HERE / "sequence-bridge.json").read_text())
    for bridge in bridges:
        g = bridge["gene"]
        raw = (ROOT / f"genes/ECOLI/{g}/{g}-uniprot.txt").read_text()
        tail = raw.split("SQ   SEQUENCE", 1)[1].split("\n", 1)[1].split("//")[0]
        sequence = "".join(re.findall("[A-Z]+", tail))
        entity_path = HERE / bridge["entity"]
        assert sha(entity_path) == bridge["entity_sha256"]
        entity = json.loads(entity_path.read_text())
        actual = entity["entity_poly"]["pdbx_seq_one_letter_code_can"]
        expected = sequence + "HHHHHHHH" if g == "lptM" else sequence[20:]
        assert actual == expected
    prior = {}
    for name in ["ecoli-consultation", "neisseria-consultation"]:
        path = HERE.parent / name / "handoff.json"
        receipt = json.loads(path.read_text())
        for filename, expected in receipt["files_sha256"].items():
            assert sha(ROOT / filename) == expected, filename
        prior[name] = {"handoff_sha256": sha(path), "files": receipt["file_count"]}
    result = {
        "status": "PASS",
        "ordered_seed_rows": count,
        "new_rows": 0,
        "protected_sources": len(sources),
        "actions": dict(actions),
        "deposited_sequence_checks": len(bridges),
        "prior_handoffs_unchanged": prior,
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
