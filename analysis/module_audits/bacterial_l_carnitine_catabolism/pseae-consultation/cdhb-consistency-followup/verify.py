"""Verify only the authorized CdhB judgment changes and immutable release chain."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[4]
TARGETS = {"PSEAE/cdhB": 2, "PSEPK/PP_0301": 0}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(doc):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in doc["existing_annotations"]
    ]


def normalized(doc, target, index):
    result = copy.deepcopy(doc)
    review = result["existing_annotations"][index]["review"]
    for key in ("summary", "reason", "propagation_review", "source_defects"):
        review.pop(key, None)
    if target == "PSEAE/cdhB":
        result["existing_annotations"][3]["review"].pop("reason")
        for ref in result["references"]:
            if ref["id"] == "PMID:24240508":
                ref["reference_review"].pop("review_notes")
    return result


def main():
    before = json.loads((AUDIT / "before.json").read_text())
    allowed = set()
    reviews = {}
    for target, index in TARGETS.items():
        gene = target.split("/")[1]
        path = f"genes/{target}/{gene}-ai-review.yaml"
        old = yaml.safe_load(before[path]["text"])
        new = yaml.safe_load((ROOT / path).read_text())
        assert normalized(old, target, index) == normalized(new, target, index), target
        assert payloads(old) == payloads(new), target
        assert old["core_functions"] == new["core_functions"], target
        assert old["proposed_new_terms"] == new["proposed_new_terms"], target
        assert [r["review"]["action"] for r in old["existing_annotations"]] == [
            r["review"]["action"] for r in new["existing_annotations"]
        ], target
        r = new["existing_annotations"][index]["review"]
        assert r["action"] == "MODIFY"
        assert r["propagation_review"]["root_cause"] == "UNRESOLVED"
        assert "FUNCTIONAL_DIVERGENCE" not in r["propagation_review"].get("failure_modes", [])
        assert all(d["requested_change"] == "CHECK" for d in r["source_defects"])
        assert all(d["confidence"] == "SUSPECTED" for d in r["source_defects"])
        reviews[path] = {
            "before_sha256": before[path]["sha256"],
            "after_sha256": sha(ROOT / path),
            "ordered_rows": len(new["existing_annotations"]),
            "all_actions_payloads_lifecycle_core_and_proposals_unchanged": True,
            "modified_review_index": index,
            "before_review": old["existing_annotations"][index]["review"],
            "after_review": r,
        }
        for suffix in ("ai-review.yaml", "ai-review.html", "notes.md"):
            allowed.add(f"genes/{target}/{gene}-{suffix}")
    manifests = {}
    frozen = {}
    for path, record in before.items():
        if "handoff." not in path:
            continue
        assert sha(ROOT / path) == record["sha256"], path
        data = yaml.safe_load(record["text"])
        frozen.update(data.get("files", data.get("files_sha256", {})))
        manifests[path] = record["sha256"]
    changed = {}
    for path, expected in frozen.items():
        current = sha(ROOT / path)
        if path in allowed:
            assert before[path]["sha256"] == expected, path
            changed[path] = {"before_sha256": expected, "after_sha256": current}
        else:
            assert current == expected, path
    assert set(changed) == allowed
    protected = json.loads((AUDIT.parent / "preservation.json").read_text())[
        "protected_source_sha256"
    ]
    for path, expected in protected.items():
        assert sha(ROOT / path) == expected, path
    result = {
        "result": "PASS",
        "prior_manifests_unchanged": manifests,
        "authorized_updates": changed,
        "reviews": reviews,
        "other_frozen_files_unchanged": len(frozen) - len(allowed),
        "protected_sources_unchanged": len(protected),
        "action_changes": 0,
        "payload_or_lifecycle_changes": 0,
        "core_or_new_term_changes": 0,
    }
    (AUDIT / "preservation-update.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "updated_paths": len(changed), "sources": len(protected)}))


if __name__ == "__main__":
    main()
