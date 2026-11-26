"""Verify frozen E. coli Lpt source claims and protected source bytes."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    rows = 0
    inherited = 0
    changes = []
    audit = []
    for path, entry in baseline["reviews"].items():
        old = entry["document"]
        new = yaml.safe_load((ROOT / path).read_text())
        before = old["existing_annotations"]
        after = new["existing_annotations"]
        assert list(map(payload, before)) == list(map(payload, after)), path
        assert new["status"] == "COMPLETE", path
        rows += len(before)
        for index, (a, b) in enumerate(zip(before, after, strict=True)):
            if a["review"]["action"] == "NEW":
                inherited += 1
                assert b["review"]["action"] == "NEW", (path, index)
            if a["review"]["action"] != b["review"]["action"]:
                changes.append(
                    {
                        "path": path,
                        "index": index,
                        "term": a["term"],
                        "before": a["review"]["action"],
                        "after": b["review"]["action"],
                    }
                )
            audit.append(
                {
                    "path": path,
                    "index": index,
                    "term": b["term"],
                    "action": b["review"]["action"],
                    "reason": b["review"].get("reason"),
                }
            )
    assert len(changes) == 1 and changes[0]["term"]["id"] == "GO:0042802"
    assert changes[0]["after"] == "KEEP_AS_NON_CORE"
    for path, expected in baseline["protected_files_sha256"].items():
        assert sha(ROOT / path) == expected, path
    for path, old in baseline["notes"].items():
        assert (ROOT / path).read_text().startswith(old), path
    root_base = HERE.parent / "baseline.json"
    assert sha(root_base) == baseline["root_baseline_sha256"]
    result = {
        "result": "PASS",
        "ordered_historical_rows": rows,
        "historical_NEW_preserved": inherited,
        "added_NEW": 0,
        "protected_sources": len(baseline["protected_files_sha256"]),
        "append_only_notes": len(baseline["notes"]),
        "action_changes": changes,
        "final_action_counts": dict(Counter(a["action"] for a in audit)),
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    (HERE / "row-audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
