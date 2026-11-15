"""Verify frozen family inputs, PAINT payloads, member additions and local quotes."""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.validation.local_source_text import (
    find_local_quote_failures,
    iter_local_quotes,
)

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assertion_payload(node: dict) -> dict:
    return {
        key: value
        for key, value in node.items()
        if key not in {"assessment", "assessment_reason", "supported_by"}
    }


def main() -> None:
    baseline = json.loads((HERE / "baseline.json").read_text())
    tree_proof = json.loads((HERE / "tree-scope.json").read_text())
    result = {"protected_sources": [], "reviews": [], "tree_checks": []}
    original = json.loads((HERE.parent / "baseline.json").read_text())
    result["original_module_sources"] = []
    for relative, expected in original["protected_files_sha256"].items():
        assert digest(ROOT / relative) == expected, relative
        result["original_module_sources"].append({"path": relative, "sha256": expected})
    for relative, expected in baseline["protected"].items():
        assert digest(ROOT / relative) == expected, relative
        result["protected_sources"].append({"path": relative, "sha256": expected})
    for relative, frozen in baseline["families"].items():
        old = frozen["document"]
        new = yaml.safe_load((ROOT / relative).read_text())
        assert (old["family_id"], old["family_name"]) == (
            new["family_id"], new["family_name"]
        )
        before = old.get("node_assessments", [])
        after = new.get("node_assessments", [])
        assert [assertion_payload(n) for n in before] == [
            assertion_payload(n) for n in after
        ], relative
        for old_sf in old["subfamilies"]:
            current = next(
                s for s in new["subfamilies"]
                if s["subfamily_id"] == old_sf["subfamily_id"]
            )
            assert current["label"] == old_sf["label"]
            for member in old_sf.get("representative_members", []):
                assert member in current["representative_members"], member
        current_refs = {r["id"]: r["title"] for r in new["references"]}
        for ref in old["references"]:
            assert current_refs[ref["id"]] == ref["title"]
        failures = find_local_quote_failures(new, ROOT)
        assert not failures, (relative, failures)
        result["reviews"].append({
            "path": relative,
            "sha256": digest(ROOT / relative),
            "original_sha256": hashlib.sha256(frozen["text"].encode()).hexdigest(),
            "preserved_node_assertions": len(before),
            "local_quotes_passed": len(list(iter_local_quotes(new))),
            "verdict_changes": [
                {"node": a["node_id"], "term": a["asserted_term"]["id"],
                 "old": a["assessment"], "new": b["assessment"]}
                for a, b in zip(before, after, strict=True)
                if a["assessment"] != b["assessment"]
            ],
        })
        family = new["family_id"].split(":")[1]
        tree_path = ROOT / ".cache/panther_trees" / f"{family}.json.gz"
        with gzip.open(tree_path, "rt") as stream:
            tree = json.load(stream)
        proof = tree_proof[family]
        assert proof["tree_sha256"] == digest(tree_path)
        assert proof["leaf_count"] == len(tree["leaves"])
        for node, report in proof["nodes"].items():
            assert report["present"] == (node in tree["under"])
            expected = {p: tree["leaves"][p] for p in tree["under"][node]}
            assert report["leaves"] == expected
            assert report["leaf_count"] == len(expected)
        result["tree_checks"].append({"family": family, "leaves": len(tree["leaves"])})
    for family, accession, gene in [
        ("PTHR47737", "Q9HTI7", "cbcW"),
        ("PTHR43869", "Q9HTI8", "cbcV"),
    ]:
        raw = (ROOT / f"genes/PSEAE/{gene}/{gene}-uniprot.txt").read_text()
        assert accession in raw and f"PANTHER; {family}:SF1;" in raw
    # Independent scope controls: known leaf versus missing leaf is not the same.
    with gzip.open(ROOT / ".cache/panther_trees/PTHR48075.json.gz", "rt") as stream:
        tree = json.load(stream)
    node_members = {tree["leaves"][x]["uniprot"] for x in tree["under"]["PTN008732775"]}
    all_members = {x["uniprot"] for x in tree["leaves"].values()}
    assert {"P76083", "P9WNP7"} <= node_members
    assert "Q9HTH8" in all_members and "Q9HTH8" not in node_members
    assert not {"Q88R32", "Q92NF5"} & all_members
    gulonate = {tree["leaves"][x]["uniprot"] for x in tree["under"]["PTN000592731"]}
    assert {"Q89HA7", "Q7LXQ8"} <= gulonate
    result["scope_controls"] = "PASS: verified exclusion differs from absent leaf; SF1 includes nonanimals"
    result["status"] = "PASS"
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(result['reviews'])} reviews, "
          f"{len(result['protected_sources'])} protected sources, "
          f"{sum(r['preserved_node_assertions'] for r in result['reviews'])} PAINT assertions")


if __name__ == "__main__":
    main()
