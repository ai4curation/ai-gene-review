"""Preserve PR-head payloads, sources and inherited proposals after activity review."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(doc):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in doc["existing_annotations"]
    ]


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    ledger = []
    actions = Counter()
    reviews = {}
    for relative, before in baseline["reviews"].items():
        path = ROOT / relative
        after = yaml.safe_load(path.read_text())
        assert after["id"] == before["id"]
        assert after["status"] == "COMPLETE"
        assert payloads(after) == payloads(before), relative
        original_proposals = [
            i
            for i, row in enumerate(before["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        current_proposals = [
            i
            for i, row in enumerate(after["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        assert original_proposals == current_proposals, relative
        reviews[relative] = {
            "sha256": sha(path),
            "rows": len(after["existing_annotations"]),
            "ordered_payloads_preserved": True,
            "inherited_NEW_indices": original_proposals,
        }
        for i, (old, new) in enumerate(
            zip(
                before["existing_annotations"],
                after["existing_annotations"],
                strict=True,
            )
        ):
            action = new["review"]["action"]
            actions[action] += 1
            if old["review"] != new["review"]:
                ledger.append(
                    {
                        "file": relative,
                        "index": i,
                        "term": new["term"]["id"],
                        "reference": new["original_reference_id"],
                        "before_action": old["review"]["action"],
                        "after_action": action,
                        "reason": new["review"]["reason"],
                    }
                )
    for relative, expected in baseline["sources_sha256"].items():
        assert sha(ROOT / relative) == expected, relative
    assert len(ledger) == 3, ledger
    assert sum(row["before_action"] != row["after_action"] for row in ledger) == 2
    result = {
        "status": "PASS",
        "baseline_sha256": sha(HERE / "baseline.json"),
        "base_head": baseline["head"],
        "reviews": reviews,
        "source_sha256": baseline["sources_sha256"],
        "source_count": len(baseline["sources_sha256"]),
        "rows": sum(actions.values()),
        "actions": dict(actions),
        "new_proposals_added": 0,
        "rows_deleted": 0,
        "retirements": 0,
        "changed_reviews": ledger,
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        {
            key: value
            for key, value in result.items()
            if key not in ["reviews", "source_sha256", "changed_reviews"]
        }
    )


if __name__ == "__main__":
    main()
