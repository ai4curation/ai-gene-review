"""Verify exact PSEPK source-row preservation and evidence closure for this audit."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
GENES = ("lolA", "lolB", "lolC", "lolD", "lolE")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in document["existing_annotations"]
    ]


def verify():
    before = yaml.safe_load((AUDIT / "before.yaml").read_text())
    baseline = json.loads((AUDIT.parent / "baseline.json").read_text())
    expected_actions = {("lolB", 1): "MODIFY", ("lolD", 0): "ACCEPT"}
    total_rows = historical_new = active_new = 0
    action_changes = []
    for gene in GENES:
        path = f"genes/PSEPK/{gene}/{gene}-ai-review.yaml"
        original = before["reviews"][gene]
        root_original = baseline["reviews"][path]["document"]
        current = yaml.safe_load((ROOT / path).read_text())
        assert original == root_original, f"Frozen baseline differs: {gene}"
        assert payloads(original) == payloads(current), f"Payload/order/lifecycle changed: {gene}"
        assert current["status"] == "COMPLETE"
        for key in ("id", "gene_symbol", "taxon", "product_type"):
            assert current[key] == original[key], (gene, key)
        for index, (old, new) in enumerate(
            zip(original["existing_annotations"], current["existing_annotations"], strict=True)
        ):
            old_action = old["review"]["action"]
            action = new["review"]["action"]
            assert action == expected_actions.get((gene, index), old_action), (gene, index)
            assert new["review"].get("reason")
            assert new["review"].get("supported_by")
            if old_action != action:
                action_changes.append(
                    {"gene": gene, "row": index, "term": old["term"]["id"], "before": old_action, "after": action}
                )
            historical_new += old_action == "NEW"
            active_new += action == "NEW" and not new.get("retired", False)
        total_rows += len(current["existing_annotations"])
        # Mutation checks prove the ordered-payload guard rejects common corruption.
        for field, value in (("qualifier", "contributes_to"), ("evidence_type", "EXP"), ("retired", True)):
            altered = copy.deepcopy(original)
            altered["existing_annotations"][0][field] = value
            assert payloads(altered) != payloads(original), (gene, field)
        reordered = copy.deepcopy(original)
        reordered["existing_annotations"].reverse()
        assert payloads(reordered) != payloads(original), gene
        core = current["core_functions"][0]
        if gene in ("lolC", "lolE"):
            assert "molecular_function" not in core
            assert core["contributes_to_molecular_function"]["id"] == "GO:0140306"
        elif gene == "lolD":
            assert core["molecular_function"]["id"] == "GO:0016887"
            assert core["contributes_to_molecular_function"]["id"] == "GO:0140306"
        elif gene == "lolB":
            assert core["proposed_molecular_function"] == current["proposed_new_terms"][0]["proposed_name"]
    protected = {
        path: sha
        for path, sha in before["files_sha256"].items()
        if not path.endswith(("-ai-review.yaml", "-ai-review.html", "-notes.md"))
    }
    protected.update(baseline["protected_files_sha256"])
    source_closure = yaml.safe_load((AUDIT / "source-closure.yaml").read_text())
    protected.update(source_closure["files_sha256"])
    for path, sha in protected.items():
        assert digest(ROOT / path) == sha, f"Protected source changed: {path}"
    ontology = {}
    for term in ("0044874", "0042953", "0005524", "0016887"):
        ontology[term] = json.loads((AUDIT / f"GO{term}-ancestors.json").read_text())["results"][0]
    for first, second in (("0044874", "0042953"), ("0005524", "0016887")):
        assert f"GO:{first}" not in ontology[second]["ancestors"]
        assert f"GO:{second}" not in ontology[first]["ancestors"]
    assert (total_rows, historical_new, active_new) == (32, 6, 6)
    return {
        "result": "PASS",
        "ordered_original_rows": total_rows,
        "historical_new_rows_preserved": historical_new,
        "active_new_rows": active_new,
        "new_rows_added": 0,
        "lifecycle_changes": 0,
        "payload_mutation_tests": 20,
        "protected_sources_checked": len(protected),
        "action_changes": action_changes,
        "scope": "Five PSEPK reviews only; full-corpus validation not run.",
    }


if __name__ == "__main__":
    print(yaml.safe_dump(verify(), sort_keys=False))
