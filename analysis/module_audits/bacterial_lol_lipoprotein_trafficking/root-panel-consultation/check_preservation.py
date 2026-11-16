"""Independent whole-panel check; reads frozen inputs and emits JSON to stdout only."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
ROOT = HERE.parents[3]
MANIFESTS = (
    "ecoli-consultation", "psepk-consultation", "aciad-consultation",
    "cross-lineage-consultation", "flaj1-lola-consultation",
    "family-consultation", "module-consultation", "capacity-consultation",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str) -> dict:
    return json.loads((AUDIT / name).read_text())


def check_hashes(mapping: dict[str, str]) -> None:
    for name, expected in mapping.items():
        assert sha(ROOT / name) == expected, f"Hash mismatch: {name}"


def payload(row: dict) -> dict:
    return {key: value for key, value in row.items() if key != "review"}


def main() -> None:
    baselines = [read("baseline.json"), read("additional-seed-baseline.json")]
    flaj = read("flaj1-lola-seed-baseline.json")
    reviews = {}
    protected = {}
    for baseline in [*baselines, flaj]:
        for name, value in baseline.get("reviews", {}).items():
            assert name not in reviews
            reviews[name] = value["document"]
        for name, value in baseline["protected_files_sha256"].items():
            assert name not in protected or protected[name] == value
            protected[name] = value
    reviews[flaj["review_path"]] = flaj["document"]
    assert len(reviews) == 17
    check_hashes(protected)
    panel = []
    for name, before in sorted(reviews.items()):
        after = yaml.safe_load((ROOT / name).read_text())
        old = before.get("existing_annotations", [])
        new = after.get("existing_annotations", [])
        assert len(new) >= len(old), name
        assert [payload(row) for row in new[:len(old)]] == [payload(row) for row in old], name
        historical = []
        for index, row in enumerate(old):
            if row["review"]["action"] == "NEW":
                current = new[index]
                assert current["review"]["action"] == "NEW", name
                assert current.get("retired") == row.get("retired"), name
                historical.append({"index": index, "term": row["term"],
                                   "retired": row.get("retired", False)})
        additions = new[len(old):]
        assert all(row["review"]["action"] == "NEW" for row in additions), name
        assert after["status"] == "COMPLETE", name
        panel.append({"path": name, "id": after["id"], "taxon": after["taxon"],
                      "sha256": sha(ROOT / name), "original_rows": len(old),
                      "final_rows": len(new), "historical_NEW": historical,
                      "authored_NEW": [{"index": len(old) + i, "payload": payload(row),
                                        "action": row["review"]["action"]}
                                       for i, row in enumerate(additions)]})
    original = sum(p["original_rows"] for p in panel)
    historic_new = sum(len(p["historical_NEW"]) for p in panel)
    authored_new = sum(len(p["authored_NEW"]) for p in panel)
    assert original == 140 and historic_new == 6
    # Preserve the unusual deterministic importer payload, not an invented GO code.
    literal = yaml.safe_load((ROOT / flaj["review_path"]).read_text())["existing_annotations"][0]
    assert literal["evidence_type"] == "ECO:0007744"
    assert literal["qualifier"] == "acts_upstream_of_or_within_positive_effect"
    manifest_results = {}
    for name in MANIFESTS:
        doc = read(f"{name}/handoff.json")
        files = doc.get("files", doc.get("files_sha256", {}))
        assert files, name
        check_hashes(files)
        check_hashes(doc.get("protected_sources_sha256", {}))
        check_hashes(doc.get("input_sha256", {}))
        manifest_results[name] = {"sha256": sha(AUDIT / name / "handoff.json"),
                                  "file_count": len(files), "status": "PASS"}
    required = read("required-ignored-provenance.json")
    assert len(required["files"]) == 9
    check_hashes(required["files"])
    family = read("family-consultation/preservation-results.json")
    assert family["status"] == "PASS" and family["ordered_paint_assertions"] == 12
    capacity = read("capacity-consultation/results.json")
    closure = read("capacity-consultation/source-closure.json")
    assert capacity["status"] == closure["status"] == "PASS"
    assert not closure["errors"]
    assert all(q["valid"] and not q["skipped"] for q in closure["quotations"])
    module_path = ROOT / "modules/bacterial_lol_lipoprotein_trafficking.yaml"
    assert sha(module_path) == capacity["module_sha256"]
    module = yaml.safe_load(module_path.read_text())
    references = module["references"]
    review_references = [r["id"] for r in references if r.get("publication_type") == "REVIEW"]
    result = {
        "status": "PASS", "scope": "Preservation and frozen-evidence closure, not full-corpus validation",
        "baseline_sha256": {n: sha(AUDIT / n) for n in
                            ["baseline.json", "additional-seed-baseline.json", "flaj1-lola-seed-baseline.json"]},
        "reviews": len(panel), "original_ordered_rows": original,
        "original_machine_rows": original - historic_new,
        "historical_NEW": historic_new, "historical_NEW_lifecycle_unchanged": True,
        "authored_NEW": authored_new, "final_rows": sum(p["final_rows"] for p in panel),
        "baseline_protected_files": len(protected), "baseline_protected_sha256": protected,
        "manifest_verification": manifest_results,
        "family_ordered_PAINT_assertions_preserved_by_verified_receipt": 12,
        "required_ignored_provenance": required["files"],
        "required_provenance_state": "PRESENT_HASH_VERIFIED_PUBLICATION_PENDING",
        "module_sha256": sha(module_path), "module_status": module["status"],
        "module_references": len(references), "review_article_ids": review_references,
        "capacity": {"cases": capacity["case_count"], "mutations": len(capacity["mutations"]),
                     "sensitivities": len(capacity["sensitivity"]), "verified_quotes": closure["quote_count"],
                     "rerun_here": False, "basis": "Frozen results and all input hashes independently verified"},
        "code_dependency": {"commit": flaj["tool_commit"],
                            "state": "NOT_INTEGRATED_IN_LOL; dependency full run 92793 pending per root"},
        "panel": panel,
    }
    assert len(references) == 17 and len(review_references) == 3
    assert (capacity["case_count"], len(capacity["mutations"]), len(capacity["sensitivity"]),
            closure["quote_count"]) == (32, 5, 5, 186)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
