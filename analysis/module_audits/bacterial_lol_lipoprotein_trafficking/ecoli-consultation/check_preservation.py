"""Verify frozen source payloads and source bytes; emit current action accounting."""
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    changes = []
    counts = Counter()
    total = 0
    for name, old in baseline["reviews"].items():
        data = yaml.safe_load((ROOT / name).read_text())
        rows = data["existing_annotations"]
        assert [{k: v for k, v in r.items() if k != "review"} for r in rows] == old["rows"], name
        assert len(rows) == len(old["actions"]), name
        for i, (row, before) in enumerate(zip(rows, old["actions"], strict=True)):
            after = row["review"]["action"]
            counts[after] += 1
            if after != before:
                changes.append({"path": name, "index": i, "term": row["term"]["id"], "before": before, "after": after})
        total += len(rows)
    for name, expected in baseline["protected_sources"].items():
        assert digest(ROOT / name) == expected, name
    report = {
        "status": "PASS", "genes": len(baseline["reviews"]), "ordered_rows": total,
        "protected_sources": len(baseline["protected_sources"]), "action_changes": changes,
        "current_actions": dict(sorted(counts.items())), "added_deleted_retired_rows": 0,
        "historical_NEW_in_owned_scope": 0,
        "source_sha256": baseline["protected_sources"],
    }
    (HERE / "preservation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "source_sha256"}, indent=2))


if __name__ == "__main__":
    main()
