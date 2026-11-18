"""Verify the frozen PSEPK payloads, historical proposals and protected sources."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
GENES = ("metK", "ahcY", "metH", "metE")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def main():
    baseline = json.loads((AUDIT.parent / "baseline.json").read_text())
    rows = []
    failures = []
    for gene in GENES:
        path = f"genes/PSEPK/{gene}/{gene}-ai-review.yaml"
        original = baseline["reviews"][path]["document"]
        current = yaml.safe_load((ROOT / path).read_text())
        before = original["existing_annotations"]
        after = current["existing_annotations"]
        preserved = [payload(r) for r in before] == [payload(r) for r in after]
        if not preserved:
            failures.append(f"ordered payload mismatch: {path}")
        historical_new = [
            i for i, r in enumerate(before) if r["review"]["action"] == "NEW"
        ]
        lifecycle = all(
            after[i]["review"]["action"] == "NEW"
            and before[i].get("retired", False) == after[i].get("retired", False)
            for i in historical_new
        )
        if not lifecycle:
            failures.append(f"historical proposal lifecycle mismatch: {path}")
        rows.append(
            {
                "path": path,
                "original_rows": len(before),
                "current_rows": len(after),
                "ordered_payloads_preserved": preserved,
                "historical_new": historical_new,
                "lifecycle_preserved": lifecycle,
                "actions": dict(Counter(r["review"]["action"] for r in after)),
                "sha256": sha(ROOT / path),
            }
        )
    protected = {}
    for path, expected in baseline["protected_files_sha256"].items():
        actual = sha(ROOT / path)
        protected[path] = {
            "expected": expected,
            "actual": actual,
            "unchanged": actual == expected,
        }
        if actual != expected:
            failures.append(f"protected source changed: {path}")
    result = {
        "baseline_sha256": sha(AUDIT.parent / "baseline.json"),
        "review_count": len(rows),
        "original_rows": sum(r["original_rows"] for r in rows),
        "new_rows": 0,
        "historical_new": sum(len(r["historical_new"]) for r in rows),
        "protected_files": len(protected),
        "reviews": rows,
        "protected_sources": protected,
        "failures": failures,
        "pass": not failures,
    }
    (AUDIT / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: result[k]
                for k in (
                    "review_count",
                    "original_rows",
                    "new_rows",
                    "historical_new",
                    "protected_files",
                    "pass",
                )
            },
            indent=2,
        )
    )
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
