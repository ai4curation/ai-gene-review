"""Reproduce ordered payload, historical-proposal, and protected-source checks.

Run from repository root: uv run python analysis/module_audits/
bacterial_l_carnitine_catabolism/pseae-consultation/verify.py
"""

import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
GENES = ("cdhA", "cdhB", "cdhC", "Q9HTH6", "cbcW", "cbcV")
RETIREMENTS = {"cdhB": "GO:0016289", "cdhC": "GO:0016747"}


def read_json(path):
    return json.loads(path.read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def evidence_pairs(value):
    found = set()
    if isinstance(value, dict):
        if "reference_id" in value and "supporting_text" in value:
            found.add((value["reference_id"], " ".join(value["supporting_text"].split())))
        for item in value.values():
            found.update(evidence_pairs(item))
    elif isinstance(value, list):
        for item in value:
            found.update(evidence_pairs(item))
    return found


def core_terms(value):
    found = set()
    if isinstance(value, dict):
        if str(value.get("id", "")).startswith("GO:"):
            found.add(value["id"])
        for item in value.values():
            found.update(core_terms(item))
    elif isinstance(value, list):
        for item in value:
            found.update(core_terms(item))
    return found


def main():
    baseline = read_json(AUDIT / "baseline.json")
    seeds = read_json(AUDIT / "new-seed-baseline.json")
    root_baseline = read_json(AUDIT.parent / "baseline.json")
    reviews = baseline["reviews"] | seeds["reviews"]
    assert len(reviews) == 6
    sources = (
        root_baseline["protected_files_sha256"]
        | baseline["protected"]
        | seeds["protected"]
    )
    # Recover pre-existing local/provider analyses from the pinned original commit,
    # including files not enumerated in the root's raw/publication manifest.
    head = root_baseline["head"]
    dirs = [f"genes/PSEAE/{gene}" for gene in GENES[:4]]
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", head, "--", *dirs], cwd=ROOT, text=True
    ).splitlines()
    for path in paths:
        if path.endswith(("-ai-review.yaml", "-ai-review.html", "-notes.md")):
            continue
        content = subprocess.check_output(["git", "show", f"{head}:{path}"], cwd=ROOT)
        sources[path] = digest(content)
    # Protect every pre-existing local evidence source, including historical
    # comparator analyses outside the owned gene directories.
    source_names = set(re.findall(r'file:([^"\\]+)', json.dumps(baseline["reviews"])))
    for name in source_names:
        candidate = ROOT / name
        if not candidate.exists():
            candidate = ROOT / "genes" / name
        path = candidate.relative_to(ROOT).as_posix()
        content = subprocess.check_output(["git", "show", f"{head}:{path}"], cwd=ROOT)
        sources[path] = digest(content)
    additional = ["publications/PMID_21478341.md", "publications/PMID_23763788.md"]
    for family in ("PTHR48075", "PTHR31793", "PTHR37418", "PTHR47737", "PTHR43869"):
        folder = ROOT / "interpro" / "panther" / family
        additional.extend(
            path.relative_to(ROOT).as_posix()
            for path in folder.glob("*")
            if path.is_file() and "review" not in path.name
        )
    for path in additional:
        content = subprocess.check_output(["git", "show", f"{head}:{path}"], cwd=ROOT)
        sources[path] = digest(content)
    for path, expected in sources.items():
        assert digest((ROOT / path).read_bytes()) == expected, path
    result = []
    ledger = []
    archives = {}
    for path, old in reviews.items():
        gene = Path(path).parent.name
        new = yaml.safe_load((ROOT / path).read_text())
        if path in baseline["reviews"]:
            assert old == root_baseline["reviews"][path]["document"], path
        for field in ("id", "gene_symbol", "taxon", "product_type"):
            assert old.get(field) == new.get(field), (gene, field)
        original = old["existing_annotations"]
        current = new["existing_annotations"]
        assert len(original) == len(current), gene
        assert new["status"] == "COMPLETE", gene
        for index, (before, after) in enumerate(zip(original, current, strict=True)):
            expected = payload(before)
            if gene in RETIREMENTS and index == 3:
                assert before["term"]["id"] == RETIREMENTS[gene]
                assert before["original_reference_id"] == "PMID:24240508"
                assert before["evidence_type"] == "IDA"
                assert before["review"]["action"] == after["review"]["action"] == "NEW"
                assert before.get("retired", False) is False
                expected = copy.deepcopy(expected)
                expected["retired"] = True
                # Exact proposal is still supplied by the pre-existing third row's
                # replacement and by the active core, not merely a related ancestor.
                replacement = current[2]["review"]
                assert replacement["action"] == "MODIFY"
                assert before["term"] in replacement["proposed_replacement_terms"]
                assert before["term"]["id"] in core_terms(new["core_functions"])
                support = evidence_pairs(before["review"])
                assert support <= evidence_pairs(after["review"])
                assert support <= evidence_pairs(replacement)
                assert support <= evidence_pairs(new["core_functions"])
                archives[gene] = {
                    "zero_based_index": index,
                    "original_object": before,
                    "retirement_only_payload_delta": {"retired": True},
                    "active_exact_replacement_index": 2,
                    "distinct_evidence_preserved_in_active_replacement_and_core": True,
                }
            assert expected == payload(after), (gene, index)
            assert after["review"]["action"] != "PENDING", (gene, index)
            if before.get("review", {}).get("action") == "NEW":
                assert after["review"]["action"] == "NEW", (gene, index)
            ledger.append({
                "gene": gene,
                "zero_based_index": index,
                "term": before["term"]["id"],
                "evidence": before["evidence_type"],
                "reference": before["original_reference_id"],
                "before": before.get("review", {}).get("action", "PENDING"),
                "after": after["review"]["action"],
                "retired": after.get("retired", False),
                "reason": after["review"]["reason"],
            })
        if path in baseline["reviews"]:
            assert core_terms(old.get("core_functions", [])) == core_terms(new["core_functions"])
        result.append({
            "gene": gene,
            "ordered_rows": len(current),
            "historical_NEW": sum(row["review"]["action"] == "NEW" for row in current),
            "active_NEW": sum(
                row["review"]["action"] == "NEW" and not row.get("retired", False)
                for row in current
            ),
            "review_sha256": digest((ROOT / path).read_bytes()),
        })
    assert sum(row["ordered_rows"] for row in result) == 90
    assert sum(row["historical_NEW"] for row in result) == 2
    assert sum(row["active_NEW"] for row in result) == 0
    assert set(archives) == set(RETIREMENTS)
    output = {
        "result": "PASS",
        "baseline_head": head,
        "reviews": result,
        "protected_source_count": len(sources),
        "protected_source_sha256": sources,
        "annotation_changes_allowed": "Only review judgments and the two exact retired:true deltas",
        "existing_core_GO_assertions": "Unchanged; supporting metadata/prose updated",
    }
    for name, data in (
        ("preservation.json", output),
        ("action-ledger.json", ledger),
        ("historical-proposals.json", archives),
    ):
        (AUDIT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"result": "PASS", "rows": 90, "sources": len(sources)}))


if __name__ == "__main__":
    main()
