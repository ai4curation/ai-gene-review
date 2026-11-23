"""Prove the authorized ManX core-only supersession of the frozen gene review."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    frozen = json.loads((HERE / "before.json").read_text())
    path = "genes/ECOLI/manX/manX-ai-review.yaml"
    current = yaml.safe_load((ROOT / path).read_text())
    expected = copy.deepcopy(frozen["document"])
    changed = []
    for i, core in enumerate(expected["core_functions"]):
        if "molecular_function" in core:
            core["contributes_to_molecular_function"] = core.pop("molecular_function")
            changed.append(i)
    assert changed == [0], changed
    for index in [0, 6, 9, 23]:
        a = expected["existing_annotations"][index]["review"]
        b = current["existing_annotations"][index]["review"]
        assert a["action"] == b["action"] == "MODIFY"
        assert b["proposed_replacement_terms"][:1] == a["proposed_replacement_terms"]
        assert [t["id"] for t in b["proposed_replacement_terms"][1:]] == [
            "GO:0022855",
            "GO:0022877",
            "GO:0022880",
        ]
        assert b["supported_by"][:-2] == a["supported_by"]
        assert b["reason"].startswith(a["reason"])
        for field in [
            "summary",
            "reason",
            "supported_by",
            "proposed_replacement_terms",
        ]:
            a[field] = copy.deepcopy(b[field])
    assert current["references"][:-2] == expected["references"]
    assert current["references"][-2]["id"] == "PMID:9864311"
    assert current["references"][-1]["id"].endswith(
        "core-contribution-followup/substrate-evidence.md"
    )
    expected["references"] = current["references"]
    assert current == expected, (
        "Unexpected change outside the authorized core/refinement scope"
    )
    baseline = json.loads((HERE.parent.parent / "baseline.json").read_text())
    for source, digest in baseline["protected_files_sha256"].items():
        assert sha(ROOT / source) == digest, source
    extra = json.loads((HERE.parent / "additional-protected.json").read_text())
    for source, digest in extra["files"].items():
        assert sha(ROOT / source) == digest, source
    rows = 0
    for source, old in baseline["reviews"].items():
        new = yaml.safe_load((ROOT / source).read_text())
        before, after = (
            old["document"]["existing_annotations"],
            new["existing_annotations"],
        )
        assert len(before) == len(after)
        for a, b in zip(before, after, strict=True):
            assert {k: v for k, v in a.items() if k != "review"} == {
                k: v for k, v in b.items() if k != "review"
            }
        rows += len(before)
    old_handoff = json.loads((HERE.parent / "handoff.json").read_text())
    files = old_handoff["files"]
    if isinstance(files, list):
        files = {row["path"]: row["sha256"] for row in files}
    allowed = {
        f"genes/ECOLI/manX/manX-{s}"
        for s in ["ai-review.yaml", "ai-review.html", "notes.md"]
    }
    deviations = {}
    for source, digest in files.items():
        actual = sha(ROOT / source)
        if actual != digest:
            assert source in allowed, source
            deviations[source] = {"before": digest, "after": actual}
    assert set(deviations) == allowed
    result = {
        "status": "PASS",
        "original_handoff_sha256": sha(HERE.parent / "handoff.json"),
        "exact_curated_change": "Core role slot rename plus four broad-MF replacement expansions and two supporting references",
        "all_annotation_source_payloads_and_actions_identical_to_pre_followup": True,
        "review_only_refinement_rows": [0, 6, 9, 23],
        "ordered_original_payloads_preserved": rows,
        "protected_sources": len(baseline["protected_files_sha256"]),
        "additional_provider_prediction_sources": len(extra["files"]),
        "authorized_superseded_paths": deviations,
        "other_frozen_paths_unchanged": len(files) - len(deviations),
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
