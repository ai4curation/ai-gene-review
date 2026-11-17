"""Verify the frozen PSEPK inputs and the single authorized lifecycle exception."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = (
    ROOT
    / "analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/baseline.json"
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k not in {"review", "retired"}}


def main():
    baseline = json.loads(BASE.read_text())
    results = {}
    historical = 0
    lifecycle = []
    for rel, captured in baseline["reviews"].items():
        old = captured["document"]["existing_annotations"]
        now = yaml.safe_load((ROOT / rel).read_text())
        current = now["existing_annotations"]
        assert len(old) == len(current), rel
        assert [payload(x) for x in old] == [payload(x) for x in current], rel
        for index, (before, after) in enumerate(zip(old, current, strict=True)):
            if before["review"]["action"] == "NEW":
                historical += 1
                assert after["review"]["action"] == "NEW", (rel, index)
            if before.get("retired", False) != after.get("retired", False):
                assert rel == "genes/PSEPK/phaZ/phaZ-ai-review.yaml" and index == 2
                assert after["retired"] is True
                lifecycle.append(
                    {
                        "path": rel,
                        "index": index,
                        "before_retired": False,
                        "after_retired": True,
                        "action_preserved": "NEW",
                    }
                )
        assert now["status"] == "COMPLETE"
        results[rel] = {
            "rows": len(current),
            "sha256": sha(ROOT / rel),
            "actions": dict(Counter(x["review"]["action"] for x in current)),
        }
    assert historical == 5 and len(lifecycle) == 1
    archive = yaml.safe_load((HERE / "retired-phaZ-proposal.yaml").read_text())
    original = baseline["reviews"][archive["review_path"]]["document"][
        "existing_annotations"
    ][2]
    assert archive["original_row"] == original
    checked = {}
    for rel, expected in baseline["protected_files_sha256"].items():
        actual = sha(ROOT / rel)
        assert actual == expected, rel
        checked[rel] = actual
    result = {
        "status": "PASS",
        "baseline_sha256": sha(BASE),
        "ordered_rows": 11,
        "historical_new": 5,
        "active_historical_new": 4,
        "retired_historical_new": 1,
        "added_rows": 0,
        "authorized_lifecycle_exception": lifecycle,
        "protected_sources": len(checked),
        "protected_sha256": checked,
        "reviews": results,
        "limits": "Preservation is not independent experimental proof. KT2442 inference remains explicit.",
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        "PASS: 11 ordered payloads; 5 historical NEW (4 active, 1 authorized retirement); "
        f"{len(checked)} protected files; 0 added rows."
    )


if __name__ == "__main__":
    main()
