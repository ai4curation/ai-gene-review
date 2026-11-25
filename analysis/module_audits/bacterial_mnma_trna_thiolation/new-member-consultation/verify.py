"""Verify imported payloads, immutable sources, quotations and curation boundaries."""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(value):
    return " ".join(value.split())


def payload(rows):
    return [{k: v for k, v in row.items() if k != "review"} for row in rows]


def quotations(obj):
    if isinstance(obj, dict):
        if "supporting_text" in obj:
            yield obj
        for value in obj.values():
            yield from quotations(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from quotations(value)


def source_path(rid):
    if rid.startswith("PMID:"):
        return ROOT / f"publications/PMID_{rid.split(':')[1]}.md"
    if rid.startswith("file:"):
        relative = rid.removeprefix("file:")
        local = ROOT / "genes" / relative
        return local if local.exists() else ROOT / relative
    raise AssertionError(rid)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Check frozen inputs without rewriting the receipt",
    )
    args = parser.parse_args()
    baseline = json.loads((A / "baseline.json").read_text())
    reviews = {x["review"] for x in baseline["seeds"]}
    protected = {
        p: h
        for p, h in baseline["protected_and_seed_files"].items()
        if p not in reviews
    }
    for path, expected in protected.items():
        assert sha(ROOT / path) == expected, f"Immutable source changed: {path}"
    sources = dict(protected)
    for node_source in json.loads((A / "paint-node-evidence.json").read_text()):
        assert sha(ROOT / node_source["source"]) == node_source["sha256"]
        sources[node_source["source"]] = node_source["sha256"]
    sources[
        "analysis/module_audits/bacterial_mnma_trna_thiolation/new-seed-baseline.yaml"
    ] = sha(A.parent / "new-seed-baseline.yaml")
    for path in (A.parent / "preflight").iterdir():
        if path.is_file():
            sources[str(path.relative_to(ROOT))] = sha(path)
    actions = Counter()
    quote_count = 0
    original_count = 0
    preserved = []
    docs = {}
    for seed in baseline["seeds"]:
        path = ROOT / seed["review"]
        doc = yaml.safe_load(path.read_text())
        docs[f"{seed['organism']}/{seed['gene']}"] = doc
        assert payload(seed["rows"]) == payload(doc["existing_annotations"]), seed[
            "review"
        ]
        assert doc["status"] == "COMPLETE"
        assert doc["id"] == seed["accession"]
        assert not any(r.get("retired") for r in doc["existing_annotations"])
        assert all(
            r["review"]["action"] not in {"NEW", "PENDING"}
            for r in doc["existing_annotations"]
        )
        original_count += len(seed["rows"])
        actions.update(r["review"]["action"] for r in doc["existing_annotations"])
        refs = {r["id"]: r for r in doc["references"]}
        for rid in refs:
            if rid.startswith("PMID:"):
                source = ROOT / f"publications/PMID_{rid.split(':')[1]}.md"
                sources[str(source.relative_to(ROOT))] = sha(source)
        # Row/core evidence objects contain their own reference_id.
        for obj in quotations(doc):
            rid = obj.get("reference_id")
            if rid:
                assert rid in refs
                text = source_path(rid).read_text()
                assert norm(obj["supporting_text"]) in norm(text), (path, rid)
                quote_count += 1
        # Findings inherit the enclosing reference rather than carrying an id.
        for rid, reference in refs.items():
            if not rid.startswith(("PMID:", "file:")):
                continue
            text = source_path(rid).read_text()
            for finding in reference.get("findings", []):
                assert norm(finding["supporting_text"]) in norm(text), (path, rid)
                quote_count += 1
        preserved.append(
            {
                "review": seed["review"],
                "rows": len(seed["rows"]),
                "ordered_payload_exact": True,
                "review_sha256": sha(path),
            }
        )
    assert original_count == 93
    for gene in ("tusB", "tusC"):
        core = docs[f"ECOLI/{gene}"]["core_functions"][0]
        assert "molecular_function" not in core
        assert core["contributes_to_molecular_function"]["id"] == "GO:0016783"
        assert core["in_complex"]["id"] == "GO:1990228"
    for org in ("ECOLI", "BACSU", "THET2"):
        assert (
            docs[f"{org}/mnmA"]["core_functions"][0]["molecular_function"]["id"]
            == "GO:0103016"
        )
    for org, gene in (("BACSU", "iscS1"), ("THET2", "TT_C0087"), ("THET2", "TT_C1373")):
        assert (
            docs[f"{org}/{gene}"]["core_functions"][0]["molecular_function"]["id"]
            == "GO:0031071"
        )
    specific = {
        ("ECOLI/tusA", "GO:0016226"): "MARK_AS_OVER_ANNOTATED",
        ("ECOLI/tusA", "GO:0019448"): "ACCEPT",
        ("ECOLI/tusD", "GO:0016783"): "ACCEPT",
        ("ECOLI/mnmA", "GO:0097532"): "KEEP_AS_NON_CORE",
        ("BACSU/mnmA", "GO:1990228"): "UNDECIDED",
    }
    for (gene, tid), action in specific.items():
        rows = [r for r in docs[gene]["existing_annotations"] if r["term"]["id"] == tid]
        assert rows and all(r["review"]["action"] == action for r in rows)
    providers = json.loads((A / "provider-attempts.json").read_text())
    assert len(providers) == 11
    assert all(
        r["returncode"] != 0 and "403" in (A / r["log"]).read_text() for r in providers
    )
    results = json.loads((A / "focused-results.json").read_text())
    assert len(results) == 22
    assert all(
        r.get("validate", 0) == r.get("render", 0) == r.get("validate_history", 0) == 0
        for r in results
    )
    histories = json.loads((A / "histories.json").read_text())
    assert len(histories) == 11
    for h in histories:
        assert (ROOT / h).exists()
    receipt = {
        "result": "PASS",
        "reviews": 11,
        "ordered_seed_rows": original_count,
        "added_rows": 0,
        "deleted_rows": 0,
        "retired_rows": 0,
        "historical_new_rows": 0,
        "unchanged_protected_sources": len(protected),
        "verified_quotations": quote_count,
        "actions": dict(sorted(actions.items())),
        "falcon_attempts": 11,
        "falcon_403_failures": 11,
        "paint_target_absent_unresolved": [
            "THET2/mnmA",
            "THET2/TT_C0087",
            "THET2/TT_C1373",
        ],
        "preserved_reviews": preserved,
        "validation_history_render": "11/11 each PASS",
        "source_dependencies": dict(sorted(sources.items())),
        "limitations": [
            "Scientific action assertions check that the documented decisions persist; they are not independent experimental validation.",
            "No native Thermus donor allocation or E. coli terminal covalent mechanism is inferred from a passing validator.",
            "PAINT absence for the three Thermus targets prevents resolved target-lineage loss claims.",
        ],
    }
    receipt_path = A / "preservation-and-evidence.json"
    if args.check_only:
        assert json.loads(receipt_path.read_text()) == receipt, (
            "Frozen receipt no longer matches inputs"
        )
    else:
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in receipt.items()
                if k not in {"preserved_reviews", "source_dependencies"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
