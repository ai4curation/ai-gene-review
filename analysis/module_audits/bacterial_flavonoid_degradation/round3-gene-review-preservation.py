"""Verify round3 preserves all ordered panel annotation payloads/actions and sources."""

from pathlib import Path
from collections import Counter
import hashlib
import json
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def payloads(d):
    return [
        {k: v for k, v in r.items() if k != "review"} for r in d["existing_annotations"]
    ]


def main():
    baseline = AUDIT / "round3-gene-review-baseline.json"
    data = json.loads(baseline.read_text())
    actions = Counter()
    retired = []
    reviews = {}
    for path, old in data["reviews"].items():
        p = ROOT / path
        d = yaml.safe_load(p.read_text())
        rows = d["existing_annotations"]
        assert payloads(d) == old["payloads"], path
        assert [r["review"]["action"] for r in rows] == old["actions"], path
        actions.update(r["review"]["action"] for r in rows)
        retired.extend(
            {
                "path": path,
                "index": i,
                "term": r["term"]["id"],
                "action": r["review"]["action"],
            }
            for i, r in enumerate(rows)
            if r.get("retired")
        )
        reviews[path] = {
            "sha256": sha(p),
            "rows": len(rows),
            "ordered_payloads_and_actions_preserved": True,
        }
    for path, expected in data["protected_sha256"].items():
        assert sha(ROOT / path) == expected, path
    for path, expected in data["module_and_checker_sha256"].items():
        assert sha(ROOT / path) == expected, path
    historical = ["round2-fdeb-sequence-map.yaml", "round2-primary-site-map.yaml"]
    for name in historical:
        p = AUDIT / name
        original = subprocess.check_output(
            ["git", "show", f"{data['head']}:{p.relative_to(ROOT)}"], cwd=ROOT
        )
        assert original == p.read_bytes(), name
    assert len(retired) == 9 and all(
        r["term"] == "GO:0046275" and r["action"] == "REMOVE" for r in retired
    )
    assert sum(actions.values()) == 46 and actions["NEW"] == 7
    result = {
        "status": "PASS",
        "baseline_head": data["head"],
        "baseline_sha256": sha(baseline),
        "panel_reviews": len(reviews),
        "rows": sum(actions.values()),
        "actions": dict(sorted(actions.items())),
        "action_changes": 0,
        "rows_added": 0,
        "rows_deleted": 0,
        "NEW": 7,
        "retired": retired,
        "protected_sources_preserved": len(data["protected_sha256"]),
        "source_sha256": data["protected_sha256"],
        "module_and_checker_unchanged": True,
        "historical_maps_unchanged": historical,
        "current_reviews": reviews,
    }
    (AUDIT / "round3-gene-review-preservation.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(
        {
            k: v
            for k, v in result.items()
            if k not in ["retired", "source_sha256", "current_reviews"]
        }
    )


if __name__ == "__main__":
    main()
