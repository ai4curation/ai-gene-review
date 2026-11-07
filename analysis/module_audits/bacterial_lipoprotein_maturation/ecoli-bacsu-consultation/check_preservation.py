"""Check frozen annotation/source payloads and explicit construct/ontology bridges.

Run with: uv run python analysis/module_audits/bacterial_lipoprotein_maturation/
ecoli-bacsu-consultation/check_preservation.py
This is a preservation and evidence-boundary check, not an independent biology test.
"""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def check():
    baseline = json.loads((HERE / "baseline.json").read_text())
    root_baseline = (
        ROOT / "analysis/module_audits/bacterial_lipoprotein_maturation/baseline.json"
    )
    assert digest(root_baseline) == baseline["root_baseline_sha256"]
    results = []
    total = 0
    inherited_new = 0
    for name, before in baseline["reviews"].items():
        assert (
            hashlib.sha256(before["frozen_text"].encode()).hexdigest()
            == before["sha256"]
        )
        assert yaml.safe_load(before["frozen_text"]) == before["document"]
        old = before["document"]["existing_annotations"]
        current = yaml.safe_load((ROOT / name).read_text())
        new = current["existing_annotations"]
        assert [payload(row) for row in old] == [payload(row) for row in new], name
        assert current["status"] == "COMPLETE", name
        assert not any(row["review"]["action"] == "PENDING" for row in new)
        changes = []
        for index, (a, b) in enumerate(zip(old, new, strict=True)):
            if a["review"]["action"] == "NEW":
                inherited_new += 1
                assert b["review"]["action"] == "NEW", (name, index)
            if a["review"]["action"] != b["review"]["action"]:
                changes.append(
                    {
                        "index": index,
                        "term": a["term"]["id"],
                        "before": a["review"]["action"],
                        "after": b["review"]["action"],
                    }
                )
        assert all(
            line.rstrip() == line for line in (ROOT / name).read_text().splitlines()
        )
        results.append(
            {
                "review": name,
                "sha256": digest(ROOT / name),
                "ordered_rows": len(new),
                "actions": dict(Counter(row["review"]["action"] for row in new)),
                "action_changes": changes,
            }
        )
        total += len(new)
    for name, expected in baseline["protected_sources"].items():
        assert digest(ROOT / name) == expected, name
    sequence = json.loads((HERE / "lgt-sequence-check.json").read_text())
    assert (
        sequence["construct_sequence"]
        == "MV" + sequence["target_sequence"][1:] + "LEHHHHHH"
    )
    assert len(sequence["target_sequence"]) == 291
    assert digest(HERE / "5azb-entity.json") == sequence["response_sha256"]
    assert (
        digest(ROOT / "genes/ECOLI/lgt/lgt-uniprot.txt")
        == sequence["target_raw_sha256"]
    )
    assert total == 61
    assert inherited_new == 1
    receipt = {
        "status": "PASS",
        "ordered_historical_rows": total,
        "inherited_new_preserved": inherited_new,
        "added_rows": 0,
        "retired_rows": 0,
        "protected_sources_unchanged": len(baseline["protected_sources"]),
        "reviews": results,
        "protected_source_sha256": baseline["protected_sources"],
        "baseline_sha256": digest(HERE / "baseline.json"),
        "sequence_bridge": "P60955 residues 2–291, not an unmodified native construct",
        "limits": [
            "Preservation is not independent verification of biological truth.",
            "Focused reference validators and primary-source reading are reported separately.",
        ],
    }
    (HERE / "preservation-results.json").write_text(
        json.dumps(receipt, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in receipt.items()
                if key not in {"reviews", "protected_source_sha256"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    check()
