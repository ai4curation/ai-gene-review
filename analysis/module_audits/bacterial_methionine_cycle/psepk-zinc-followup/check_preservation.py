"""Prove the exact one-field correction and additive frozen-manifest supersession."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    b = json.loads((HERE / "baseline.json").read_text())
    review_path = ROOT / "genes/PSEPK/metE/metE-ai-review.yaml"
    current = yaml.safe_load(review_path.read_text())
    expected = copy.deepcopy(b["review"])
    assert expected["existing_annotations"][1]["term"]["id"] == "GO:0008270"
    assert expected["existing_annotations"][1]["review"]["action"] == "KEEP_AS_NON_CORE"
    expected["existing_annotations"][1]["review"]["action"] = "ACCEPT"
    assert current == expected, "Only the explicitly authorized action may differ"
    text = review_path.read_text()
    start = text.index("- term:\n    id: GO:0008270")
    pos = text.index("    action: ACCEPT", start)
    restored = text[:pos] + text[pos:].replace(
        "    action: ACCEPT", "    action: KEEP_AS_NON_CORE", 1
    )
    assert (
        hashlib.sha256(restored.encode()).hexdigest()
        == b["files_sha256"]["genes/PSEPK/metE/metE-ai-review.yaml"]
    ), "Review bytes differ beyond exact action token"
    notes = (ROOT / "genes/PSEPK/metE/metE-notes.md").read_text()
    assert notes.startswith(b["old_notes"])
    assert notes[len(b["old_notes"]) :].startswith(
        "\n## 2026-11-07 additive catalytic-zinc correction\n"
    )
    assert sha(ROOT / b["prior_handoff_path"]) == b["prior_handoff_sha256"]
    changed = set(b["files_sha256"])
    supersedes = {}
    preserved = 0
    for path, expected_sha in b["prior_handoff"]["files"].items():
        observed = sha(ROOT / path)
        if path in changed:
            assert expected_sha == b["files_sha256"][path]
            assert observed != expected_sha
            supersedes[path] = {"old_sha256": expected_sha, "new_sha256": observed}
        else:
            assert observed == expected_sha, ("unrelated frozen file", path)
            preserved += 1
    assert set(supersedes) == changed
    root = json.loads((HERE.parent / "baseline.json").read_text())
    for path, expected_sha in root["protected_files_sha256"].items():
        assert sha(ROOT / path) == expected_sha, ("protected source", path)
    result = {
        "status": "PASS",
        "supersedes_manifest": b["prior_handoff_path"],
        "supersedes_manifest_sha256": b["prior_handoff_sha256"],
        "old_manifest_unchanged": True,
        "supersedes_files": supersedes,
        "all_other_prior_manifest_files_unchanged": preserved,
        "protected_sources_unchanged": len(root["protected_files_sha256"]),
        "exact_review_delta": {
            "path": "existing_annotations[1].review.action",
            "old": "KEEP_AS_NON_CORE",
            "new": "ACCEPT",
        },
        "source_payloads_order_qualifiers_lifecycle_core_evidence_exact": True,
        "review_bytes_exact_except_action_token": True,
        "notes_append_only": True,
        "original_rows": len(current["existing_annotations"]),
        "historical_NEW": sum(
            x["review"]["action"] == "NEW" for x in current["existing_annotations"]
        ),
    }
    (HERE / "supersession.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if not isinstance(v, dict)}))


if __name__ == "__main__":
    main()
