"""Verify the frozen five-gene consultation against pre-edit evidence."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[3]
    baseline = json.loads((audit / "preservation-baseline.json").read_text())
    root_baseline = json.loads((audit.parent / "baseline.json").read_text())
    results = {}
    total_rows = 0
    historical_new = 0
    for path, before in baseline["members"].items():
        document = yaml.safe_load((root / path).read_text())
        annotations = document["existing_annotations"]
        payloads = [
            {key: value for key, value in row.items() if key != "review"}
            for row in annotations
        ]
        assert payloads == before["payloads"], path
        assert payloads == root_baseline["members"][path]["ordered_annotation_payloads"], path
        actions = [row["review"]["action"] for row in annotations]
        original_new = [i for i, action in enumerate(before["actions"]) if action == "NEW"]
        assert [i for i, action in enumerate(actions) if action == "NEW"] == original_new, path
        assert document["status"] == "COMPLETE", path
        assert all(action != "PENDING" for action in actions), path
        total_rows += len(payloads)
        historical_new += len(original_new)
        results[path] = {
            "sha256": sha256((root / path).read_bytes()),
            "rows": len(payloads),
            "historical_NEW": len(original_new),
            "actions": dict(Counter(actions)),
            "action_changes": [
                {"index": i, "term": annotations[i]["term"]["id"], "before": old, "after": new}
                for i, (old, new) in enumerate(zip(before["actions"], actions, strict=True))
                if old != new
            ],
        }
    for path, expected in baseline["protected_sha256"].items():
        assert sha256((root / path).read_bytes()) == expected, path
    for path, expected in baseline["notes_prefix"].items():
        prefix = (root / path).read_text()[: expected["length"]]
        assert sha256(prefix.encode()) == expected["sha256"], path
    report = {
        "status": "PASS",
        "reviewed_genes": len(results),
        "preserved_ordered_rows": total_rows,
        "preserved_historical_NEW": historical_new,
        "added_NEW": 0,
        "protected_files": len(baseline["protected_sha256"]),
        "append_only_notes": len(baseline["notes_prefix"]),
        "results": results,
    }
    (audit / "preservation-results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key != "results"}, indent=2))


if __name__ == "__main__":
    main()
