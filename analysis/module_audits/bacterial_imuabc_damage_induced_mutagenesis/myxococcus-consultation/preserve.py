"""Verify seeded payload order and source bytes; report explicitly appended proposals."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    path = ROOT / baseline["review_path"]
    current = yaml.safe_load(path.read_text())
    previous = baseline["review"]
    old_rows = previous["existing_annotations"]
    rows = current["existing_annotations"]
    assert current["id"] == previous["id"]
    assert current["status"] == "COMPLETE"
    assert [payload(row) for row in rows[: len(old_rows)]] == [
        payload(row) for row in old_rows
    ]
    assert all(row["review"]["action"] == "NEW" for row in rows[len(old_rows) :])
    assert not any(row["review"]["action"] == "PENDING" for row in rows)
    for relative, expected in baseline["source_sha256"].items():
        assert sha(ROOT / relative) == expected, relative
    report = {
        "status": "PASS",
        "baseline_sha256": sha(HERE / "baseline.json"),
        "review_sha256": sha(path),
        "original_rows": len(old_rows),
        "ordered_payloads_preserved": True,
        "new_proposals_added": len(rows) - len(old_rows),
        "retirements": sum(bool(row.get("retired")) for row in rows),
        "source_sha256": baseline["source_sha256"],
        "actions": dict(Counter(row["review"]["action"] for row in rows)),
        "ledger": [
            {
                "index": i,
                "term": row["term"]["id"],
                "before": old_rows[i]["review"]["action"]
                if i < len(old_rows)
                else None,
                "after": row["review"]["action"],
                "reason": row["review"]["reason"],
            }
            for i, row in enumerate(rows)
        ],
        "limitation": "Preservation accounting is not independent biological validation.",
    }
    (HERE / "preservation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: value
                for key, value in report.items()
                if key not in {"ledger", "source_sha256"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
