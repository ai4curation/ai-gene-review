"""Check the ECO-literal seed, immutable sources and prior family release."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def main():
    before = json.loads((HERE / "pre-edit-proof.json").read_text())
    baseline_path = ROOT / before["baseline"]
    assert digest(baseline_path) == before["baseline_sha256"]
    baseline = json.loads(baseline_path.read_text())
    current = yaml.safe_load((ROOT / baseline["review_path"]).read_text())
    original = baseline["document"]["existing_annotations"]
    rows = current["existing_annotations"]
    assert len(rows) == len(original) == 1
    assert list(map(payload, rows)) == list(map(payload, original))
    assert rows[0]["evidence_type"] == "ECO:0007744"
    assert rows[0]["review"]["action"] == "ACCEPT"
    assert current["status"] == "COMPLETE"
    sources = dict(baseline["protected_files_sha256"])
    root_baseline = json.loads((HERE.parent / "baseline.json").read_text())
    sources.update(root_baseline["protected_files_sha256"])
    sources["publications/PMID_40050408.md"] = before["source_publication_sha256"]
    for path, expected in sources.items():
        assert digest(ROOT / path) == expected, path
    family_manifest_path = HERE.parent / "family-consultation/handoff.json"
    family_manifest = json.loads(family_manifest_path.read_text())
    for path, expected in family_manifest["files"].items():
        assert digest(ROOT / path) == expected, path
    source = yaml.safe_load((HERE / "source-assessment.yaml").read_text())
    text = (ROOT / source["path"]).read_text()
    for finding in source["findings"]:
        assert finding["supporting_text"] in text
    tool = json.loads((HERE / "tool-overlay-proof.json").read_text())
    for path, expected in tool["copied_source_files"].items():
        assert digest(Path(tool["overlay"]) / "src" / path) == expected, path
        assert digest(Path(tool["fixed_tool_worktree"]) / "src" / path) == expected, (
            path
        )
    result = {
        "status": "PASS",
        "ordered_original_rows": len(rows),
        "original_evidence_code": rows[0]["evidence_type"],
        "new_rows": 0,
        "retired_rows": 0,
        "raw_gene_sources": len(baseline["protected_files_sha256"]),
        "protected_sources_total": len(sources),
        "prior_family_release_files_unchanged": len(family_manifest["files"]),
        "prior_family_manifest_sha256": digest(family_manifest_path),
        "exact_primary_quotes": len(source["findings"]),
        "fixed_tool_commit": tool["fixed_tool_commit"],
        "byte_identical_overlay_source_files": len(tool["copied_source_files"]),
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
