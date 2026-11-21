"""Verify frozen annotation payloads, inherited proposals and source bytes."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in document["existing_annotations"]
    ]


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    parent_path = HERE.parent / "baseline.json"
    assert sha(parent_path) == baseline["parent_baseline_sha256"]
    parent = json.loads(parent_path.read_text())
    sources = dict(baseline["sources_sha256"])
    sources.update(json.loads((HERE / "additional-sources.json").read_text()))
    ledger = []
    actions = Counter()
    reviews = {}
    for relative, old in baseline["reviews"].items():
        path = ROOT / relative
        new = yaml.safe_load(path.read_text())
        assert new["id"] == old["id"], relative
        assert new["status"] == "COMPLETE", relative
        assert payloads(new) == payloads(old), relative
        assert (
            payloads(new) == parent["members"][relative]["ordered_annotation_payloads"]
        ), relative
        old_new = [
            i
            for i, row in enumerate(old["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        new_new = [
            i
            for i, row in enumerate(new["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        assert old_new == new_new, relative
        reviews[relative] = {
            "sha256": sha(path),
            "rows": len(new["existing_annotations"]),
            "payloads_and_order_preserved": True,
            "inherited_NEW_indices": old_new,
        }
        for index, (before, after) in enumerate(
            zip(old["existing_annotations"], new["existing_annotations"], strict=True)
        ):
            action = after["review"]["action"]
            assert action != "PENDING", relative
            actions[action] += 1
            ledger.append(
                {
                    "file": relative,
                    "index": index,
                    "term": after["term"]["id"],
                    "before": before["review"]["action"],
                    "after": action,
                    "reason": after["review"]["reason"],
                }
            )
    for relative, expected in sources.items():
        assert sha(ROOT / relative) == expected, relative
    report = {
        "status": "PASS",
        "baseline_sha256": sha(HERE / "baseline.json"),
        "reviews": reviews,
        "source_sha256": sources,
        "source_count": len(sources),
        "rows": sum(actions.values()),
        "actions": dict(actions),
        "new_proposals_added": 0,
        "retirements": 0,
        "ledger": ledger,
    }
    (HERE / "preservation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(
        {
            key: value
            for key, value in report.items()
            if key not in ["reviews", "source_sha256", "ledger"]
        }
    )


if __name__ == "__main__":
    main()
