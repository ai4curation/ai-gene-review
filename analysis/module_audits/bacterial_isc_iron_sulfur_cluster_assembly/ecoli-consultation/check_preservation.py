"""Check immutable E. coli ISC payloads and source bytes against pre-edit captures."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    baseline = json.loads((HERE / "preservation-baseline.json").read_text())
    counts = []
    for relative, frozen in baseline["reviews"].items():
        document = yaml.safe_load((ROOT / relative).read_text())
        rows = document["existing_annotations"]
        payloads = [
            {key: value for key, value in row.items() if key != "review"}
            for row in rows
        ]
        assert payloads == frozen["payloads"], f"Changed ordered payloads: {relative}"
        actions = [row["review"]["action"] for row in rows]
        for index, action in enumerate(frozen["actions"]):
            if action == "NEW":
                assert actions[index] == "NEW", (
                    f"Changed historical NEW: {relative}:{index}"
                )
        assert document["status"] == "COMPLETE", relative
        assert "PENDING" not in actions, relative
        assert not any(
            line.rstrip() != line for line in (ROOT / relative).read_text().splitlines()
        )
        counts.append(
            {
                "path": relative,
                "sha256": sha256(ROOT / relative),
                "historical_rows": len(rows),
                "historical_new": frozen["actions"].count("NEW"),
                "added_rows": 0,
                "actions": dict(Counter(actions)),
            }
        )
    for relative, expected in baseline["protected_sha256"].items():
        assert sha256(ROOT / relative) == expected, (
            f"Changed protected source: {relative}"
        )
    result = {
        "status": "PASS",
        "review_count": len(counts),
        "historical_rows": sum(row["historical_rows"] for row in counts),
        "historical_new": sum(row["historical_new"] for row in counts),
        "added_rows": 0,
        "protected_files": len(baseline["protected_sha256"]),
        "reviews": counts,
        "protected_sha256": baseline["protected_sha256"],
        "new_publication_sha256": {
            relative: sha256(ROOT / relative)
            for relative in baseline["new_publications"]
        },
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"reviews", "protected_sha256", "new_publication_sha256"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
