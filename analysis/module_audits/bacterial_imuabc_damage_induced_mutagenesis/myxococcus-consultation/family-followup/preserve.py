"""Check source and frozen-gene preservation plus retained canonical family assertions."""

import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FAMILY = Path("interpro/panther/PTHR45900/PTHR45900-review.yaml")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retained(item):
    return {
        key: value
        for key, value in item.items()
        if key not in {"assessment_reason", "supported_by"}
    }


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    old = baseline["family"]
    new = yaml.safe_load((ROOT / FAMILY).read_text())
    assert (
        sha(ROOT / baseline["frozen_gene_handoff"])
        == baseline["frozen_gene_handoff_sha256"]
    )
    for relative, expected in {
        **baseline["protected_sources"],
        **baseline["frozen_gene_files"],
    }.items():
        assert sha(ROOT / relative) == expected, relative
    assert new["family_id"] == old["family_id"]
    assert new["family_name"] == old["family_name"]
    assert new["reference_protein"] == old["reference_protein"]
    assert new["subfamilies"][1:] == old["subfamilies"][1:]
    previous_members = old["subfamilies"][0]["representative_members"]
    assert (
        new["subfamilies"][0]["representative_members"][: len(previous_members)]
        == previous_members
    )
    assert new["references"][: len(old["references"])] == old["references"]
    for before, after in zip(
        old["node_assessments"], new["node_assessments"], strict=True
    ):
        assert retained(before) == retained(after), before["asserted_term"]
        assert (
            after["supported_by"][: len(before["supported_by"])]
            == before["supported_by"]
        )
    assert new["term_assessments"][1:3] == old["term_assessments"][1:3]
    old_exceptions = [
        exception
        for item in old["term_assessments"]
        for exception in item.get("member_exceptions", [])
    ]
    new_exceptions = [
        exception
        for item in new["term_assessments"]
        for exception in item.get("member_exceptions", [])
    ]
    assert new_exceptions == old_exceptions
    report = {
        "status": "PASS",
        "family_sha256": sha(ROOT / FAMILY),
        "baseline_sha256": sha(HERE / "baseline.json"),
        "frozen_gene_files_unchanged": len(baseline["frozen_gene_files"]),
        "protected_sources_unchanged": len(baseline["protected_sources"]),
        "existing_node_assertions_and_verdicts_preserved": len(new["node_assessments"]),
        "negative_member_exceptions_added": len(new_exceptions) - len(old_exceptions),
        "node_placements_or_losses_added": len(new["node_assessments"])
        - len(old["node_assessments"]),
        "term_scopes": [
            {"term": item["assessed_term"]["id"], "scope": item["scope"]}
            for item in new["term_assessments"]
        ],
        "note": "Structural preservation check, not independent biological adjudication.",
    }
    (HERE / "preservation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
