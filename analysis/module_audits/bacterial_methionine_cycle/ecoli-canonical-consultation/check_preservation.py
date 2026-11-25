"""Verify seeded rows and immutable sources without changing any curated input."""

from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
GENES = ("metK", "metE", "metH")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def main():
    failures = []
    reviews = []
    protected = json.loads((AUDIT.parent / "baseline.json").read_text())[
        "protected_files_sha256"
    ]
    seed_hashes = {}
    for gene in GENES:
        seed_path = AUDIT.parent / f"new-member-seeds/ECOLI-{gene}.json"
        seed = json.loads(seed_path.read_text())
        seed_hashes[str(seed_path.relative_to(ROOT))] = sha(seed_path)
        for path, digest in seed["files_sha256"].items():
            if not path.endswith("-ai-review.yaml"):
                protected[path] = digest
        path = f"genes/ECOLI/{gene}/{gene}-ai-review.yaml"
        current = yaml.safe_load((ROOT / path).read_text())
        before = seed["review"]["existing_annotations"]
        after = current["existing_annotations"]
        preserved = [payload(row) for row in before] == [payload(row) for row in after]
        historical = [
            i for i, row in enumerate(before) if row["review"]["action"] == "NEW"
        ]
        lifecycle = all(
            after[i]["review"]["action"] == "NEW"
            and after[i].get("retired", False) == before[i].get("retired", False)
            for i in historical
        )
        complete = current["status"] == "COMPLETE" and all(
            row["review"]["action"] != "PENDING" for row in after
        )
        if not (preserved and lifecycle and complete):
            failures.append(f"review invariant failed: {path}")
        reviews.append(
            {
                "path": path,
                "sha256": sha(ROOT / path),
                "original_rows": len(before),
                "current_rows": len(after),
                "ordered_payloads_preserved": preserved,
                "historical_new": len(historical),
                "new_rows": len(after) - len(before),
                "new_actions": sum(row["review"]["action"] == "NEW" for row in after),
                "lifecycle_preserved": lifecycle,
                "complete": complete,
                "actions": dict(Counter(row["review"]["action"] for row in after)),
            }
        )
    source_checks = {}
    for path, expected in protected.items():
        actual = sha(ROOT / path)
        source_checks[path] = {"expected": expected, "actual": actual}
        if actual != expected:
            failures.append(f"protected source changed: {path}")
    prior_checks = {}
    for slug in ("psepk-consultation", "ecoli-existing-consultation"):
        manifest_path = AUDIT.parent / slug / "handoff.json"
        manifest = json.loads(manifest_path.read_text())
        changed = [
            path
            for path, expected in manifest["files"].items()
            if sha(ROOT / path) != expected
        ]
        failures.extend(f"prior frozen handoff changed: {path}" for path in changed)
        prior_checks[slug] = {
            "manifest_sha256": sha(manifest_path),
            "files_checked": len(manifest["files"]),
            "changed": changed,
        }
    result = {
        "pass": not failures,
        "failures": failures,
        "seed_baseline_sha256": seed_hashes,
        "original_rows": sum(row["original_rows"] for row in reviews),
        "new_rows": sum(row["new_rows"] for row in reviews),
        "historical_new": sum(row["historical_new"] for row in reviews),
        "protected_sources_count": len(source_checks),
        "protected_sources": source_checks,
        "frozen_prior_handoffs": prior_checks,
        "reviews": reviews,
    }
    (AUDIT / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"protected_sources", "reviews"}
            },
            indent=2,
        )
    )
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
