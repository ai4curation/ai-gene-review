"""Verify the bounded PR6182 CbcV/CbcW evidence repair without rewriting inputs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    baseline = json.loads((AUDIT / "baseline.json").read_text())
    rows = []
    for relative, frozen in baseline["reviews"].items():
        document = yaml.safe_load((ROOT / relative).read_text())
        old = frozen["document"]["existing_annotations"]
        current = document["existing_annotations"]
        payloads = [{k: v for k, v in row.items() if k != "review"} for row in current]
        assert payloads == frozen["ordered_payloads"], relative
        assert [a["review"]["action"] for a in current] == [a["review"]["action"] for a in old]
        assert document["status"] == "COMPLETE"
        rows.append({
            "path": relative,
            "rows": len(current),
            "historical_NEW": sum(a["review"]["action"] == "NEW" for a in old),
            "added_rows": 0,
            "actions_changed": 0,
            "ordered_payloads_equal": True,
            "before_sha256": frozen["sha256"],
            "after_sha256": sha(ROOT / relative),
            "action_counts": {action: sum(a["review"]["action"] == action for a in current)
                              for action in sorted({a["review"]["action"] for a in current})},
        })
    protected = baseline["protected_sources_sha256"]
    for relative, expected in protected.items():
        assert sha(ROOT / relative) == expected, relative
    for relative, frozen in baseline["before_files"].items():
        if relative.endswith("-notes.md"):
            assert (ROOT / relative).read_text().startswith(frozen["text"]), relative
    result = {
        "status": "PASS",
        "baseline_sha256": sha(AUDIT / "baseline.json"),
        "parent_baseline_sha256": baseline["parent_baseline_sha256"],
        "ordered_rows": sum(r["rows"] for r in rows),
        "protected_sources": len(protected),
        "protected_sources_equal": True,
        "notes_append_only": True,
        "no_retirement_or_qualifier_change": True,
        "reviews": rows,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
