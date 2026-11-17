"""Verify seeded payloads, immutable sources and the frozen literature release."""
import hashlib
import json
from collections import Counter
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
AUDIT = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(rows):
    return [{k: v for k, v in row.items() if k != "review"} for row in rows]


def main():
    receipt = json.loads((HERE / "seed-receipt.json").read_text())
    result = {"genes": {}, "protected_seed_sources": 0, "new_rows": 0, "retired_rows": 0}
    for path, digest in receipt["seed_sources"].items():
        assert sha(ROOT / path) == digest, path
        seed = json.loads((ROOT / path).read_text())
        org, gene = seed["organism"], seed["gene"]
        review = ROOT / "genes" / org / gene / f"{gene}-ai-review.yaml"
        data = yaml.safe_load(review.read_text())
        before, after = seed["review"]["existing_annotations"], data["existing_annotations"]
        assert payload(before) == payload(after), f"ordered payload mismatch: {gene}"
        assert data["status"] == "COMPLETE"
        assert all(row["review"]["action"] not in {"PENDING", "NEW"} for row in after)
        assert not any(row.get("retired") for row in after)
        for source, expected in seed["files_sha256"].items():
            if source.endswith("-ai-review.yaml"):
                continue
            assert sha(ROOT / source) == expected, source
            result["protected_seed_sources"] += 1
        history = json.loads((HERE / f"{gene}-history.json").read_text())["path"]
        record = yaml.safe_load((ROOT / history).read_text())
        assert record["target"]["path"] == str(review.relative_to(ROOT))
        for task, marker in [("validate", "All validations passed"), ("render", "Rendered to"), ("history-validate", "No issues found")]:
            assert marker in (HERE / f"{gene}-{task}.log").read_text()
        assert "403" in (HERE / f"{gene}-falcon.log").read_text()
        result["genes"][f"{org}/{gene}"] = {"original_rows": len(before), "actions": dict(sorted(Counter(row["review"]["action"] for row in after).items())), "review_sha256": sha(review), "history": history}
    baseline = json.loads((AUDIT / "baseline.json").read_text())
    for source, expected in baseline["protected_files_sha256"].items():
        assert sha(ROOT / source) == expected, source
    result["original_module_sources_preserved"] = len(baseline["protected_files_sha256"])
    literature = AUDIT / "literature-consultation/handoff.json"
    assert sha(literature) == "a33c1db2bbc3a4596ea2b2db2569ce3881bd7511bdbae5c4b229d8e5d444864f"
    manifest = json.loads(literature.read_text())
    for key in ["files", "unchanged_external_publication_inputs"]:
        for source, expected in manifest[key].items():
            assert sha(ROOT / source) == expected, source
    result["frozen_literature_files_verified"] = len(manifest["files"])
    result["status"] = "PASS"
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
