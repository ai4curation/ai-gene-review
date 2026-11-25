"""Verify PR6175 scoped ordered-payload/source preservation without changing inputs."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def check():
    baseline = json.loads((HERE / "baseline.json").read_text())
    parent_path = HERE.parent / "baseline.json"
    assert sha(parent_path) == baseline["parent_baseline_sha256"]
    parent = json.loads(parent_path.read_text())
    results = []
    historical = 0
    inherited_new = 0
    for name, frozen in baseline["reviews"].items():
        assert hashlib.sha256(frozen["text"].encode()).hexdigest() == frozen["sha256"]
        assert yaml.safe_load(frozen["text"]) == frozen["document"]
        before = frozen["document"]["existing_annotations"]
        current = yaml.safe_load((ROOT / name).read_text())
        after = current["existing_annotations"]
        assert [payload(row) for row in before] == [payload(row) for row in after], name
        assert current["status"] == "COMPLETE", name
        actions = []
        for index, (a, b) in enumerate(zip(before, after, strict=True)):
            if a["review"]["action"] == "NEW":
                inherited_new += 1
                assert b["review"]["action"] == "NEW"
            if a["review"]["action"] != b["review"]["action"]:
                actions.append(
                    {
                        "index": index,
                        "term": a["term"]["id"],
                        "before": a["review"]["action"],
                        "after": b["review"]["action"],
                    }
                )
        if name == "genes/PSEPK/hscA/hscA-ai-review.yaml":
            assert before[4] == after[4], "Parent-owned proposal lifecycle changed"
        assert all(
            line == line.rstrip() for line in (ROOT / name).read_text().splitlines()
        )
        historical += len(after)
        results.append(
            {
                "path": name,
                "sha256": sha(ROOT / name),
                "rows": len(after),
                "actions": dict(Counter(row["review"]["action"] for row in after)),
                "action_changes": actions,
            }
        )
    for name, text in baseline["notes"].items():
        assert (ROOT / name).read_text().startswith(text), name
    for name, digest in parent["protected_files_sha256"].items():
        assert sha(ROOT / name) == digest, name
    receipt = {
        "status": "PASS",
        "historical_ordered_rows": historical,
        "historical_NEW_actions_preserved": inherited_new,
        "added_rows": 0,
        "deleted_rows": 0,
        "PSEPK_hscA_retired_proposal_entire_row_unchanged": True,
        "protected_files_unchanged": len(parent["protected_files_sha256"]),
        "notes_append_only": True,
        "reviews": results,
        "baseline_sha256": sha(HERE / "baseline.json"),
        "parent_baseline_sha256": sha(parent_path),
        "protected_sha256": parent["protected_files_sha256"],
    }
    (HERE / "preservation-results.json").write_text(
        json.dumps(receipt, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                k: v
                for k, v in receipt.items()
                if k not in {"reviews", "protected_sha256"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    check()
