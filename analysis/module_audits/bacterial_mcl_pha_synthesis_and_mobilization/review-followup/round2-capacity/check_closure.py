"""Full explicit reference closure, original rows and additive round-two scope."""

import json
import re

import yaml

from seal import AUDIT, HERE, IMPL, ROOT, sha, verify_seal


def objects(value, reference=None):
    if isinstance(value, dict):
        reference = value.get("reference_id", value.get("source_id", value.get("id", reference)))
        yield value, reference
        for child in value.values():
            yield from objects(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child, reference)


def normalized(text):
    return re.sub(r"\s+", " ", re.sub(r"(?m)^CC\s{3}", "", text)).strip()


def payload(row):
    return {k: v for k, v in row.items() if k not in {"review", "retired"}}


def unique(rows):
    return sorted({json.dumps(r, sort_keys=True): r for r in rows}.values(),
                  key=lambda r: json.dumps(r, sort_keys=True))


def run():
    accepted = verify_seal()
    inputs = {}
    missing = []

    def record(path):
        if not path.is_file():
            missing.append(str(path.relative_to(ROOT)))
            return None
        inputs[str(path.relative_to(ROOT))] = sha(path)
        return path

    def read(path):
        return yaml.safe_load(record(path).read_text())

    def resolve(ref):
        if not isinstance(ref, str):
            return None
        if ref.startswith("PMID:"):
            return record(ROOT / "publications" / (ref.replace(":", "_") + ".md"))
        if ref.startswith("file:"):
            direct = ROOT / ref[5:]
            return record(direct if direct.exists() else ROOT / "genes" / ref[5:])
        return None

    record(IMPL / "handoff.json")
    for name, expected in {**accepted["source_dependencies"], **accepted["files"]}.items():
        assert sha(record(ROOT / name)) == expected, name
    # The previous 552-input closure is retained in full. Only the explicitly
    # accepted 13 round-two science/note successors and the separately authorized
    # deletion of one invalid provider quote may differ.
    prior = read(HERE.parent / "module-integration/input-closure.json")["inputs"]
    superseded = []
    for name, expected in prior.items():
        path = record(ROOT / name)
        if path is None:
            continue
        actual = sha(path)
        if actual != expected:
            assert accepted["files"].get(name) == actual, name
            superseded.append({"path": name, "historical_sha256": expected,
                               "accepted_round2_sha256": actual})
    assert len(superseded) == 14
    record(HERE / "phaA-quote-repair.json")
    record(HERE / "closure-before-phaA-quote-repair.json")
    member_names = []
    ordered = historical = added = retired = 0
    protected = {}
    for filename in ["baseline.json", "additional-seed-baseline.json", "cupnh-seed-baseline.json"]:
        baseline = read(AUDIT / filename)
        for name, expected in baseline["protected_files_sha256"].items():
            assert sha(record(ROOT / name)) == expected, name
            protected[name] = expected
        for name, original in baseline.get("reviews", baseline.get("genes", {})).items():
            member_names.append(name)
            before = original["document"]["existing_annotations"]
            review = read(ROOT / name)
            assert review["status"] == "COMPLETE"
            after = review["existing_annotations"]
            assert [payload(r) for r in after[:len(before)]] == [payload(r) for r in before], name
            ordered += len(before)
            for index, (old, current) in enumerate(zip(before, after, strict=False)):
                if old["review"]["action"] == "NEW":
                    historical += 1
                    assert current["review"]["action"] == "NEW"
                if bool(old.get("retired")) != bool(current.get("retired")):
                    assert name == "genes/PSEPK/phaZ/phaZ-ai-review.yaml" and index == 2 and current["retired"]
                retired += bool(current.get("retired"))
            extra = after[len(before):]
            if extra:
                assert name == "genes/PSEAE/phaG/phaG-ai-review.yaml" and len(extra) == 1
                assert extra[0]["term"]["id"] == "GO:0016747" and extra[0]["evidence_type"] == "IC"
                assert extra[0]["review"]["action"] == "NEW" and not extra[0].get("retired")
            added += len(extra)
    assert (len(member_names), ordered, historical, added, retired) == (9, 23, 5, 1, 1)
    family_names = [name for name in prior if name.startswith("interpro/panther/") and name.endswith("-review.yaml")]
    assert len(family_names) == 4
    module_name = "modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml"
    queue = [ROOT / name for name in sorted(member_names + family_names + [module_name])]
    sources = {}
    edges = []
    quotes = []
    quote_failures = []
    visited = set()
    while queue:
        path = queue.pop()
        name = str(path.relative_to(ROOT))
        if name in visited:
            continue
        visited.add(name)
        document = read(path)
        for obj, inherited in objects(document):
            for key in ["id", "reference_id", "source_id"]:
                ref = obj.get(key)
                source = resolve(ref)
                if source is not None:
                    target = str(source.relative_to(ROOT))
                    sources[target] = sha(source)
                    edges.append({"document": name, "reference": ref, "source": target})
                    if source.suffix in {".yaml", ".yml"} and target not in visited:
                        queue.append(source)
            if obj.get("supporting_text"):
                source = resolve(inherited)
                if source is None:
                    quote_failures.append({"document": name, "reference": inherited, "reason": "No resolvable local source"})
                    continue
                entry = {"document": name, "source": str(source.relative_to(ROOT)), "quote": obj["supporting_text"]}
                if normalized(entry["quote"]) not in normalized(source.read_text()):
                    quote_failures.append(entry)
                else:
                    quotes.append(entry)
    # Preserve the independently adjudicated primary-excerpt checks, not only hashes.
    excerpts = 0
    for entry in read(AUDIT / "literature-consultation/reference-ledger.yaml"):
        path = record(ROOT / entry["source_path"])
        assert sha(path) == entry["source_sha256"]
        for finding in entry["findings"]:
            assert normalized(finding["supporting_text"]) in normalized(path.read_text()), entry["id"]
            excerpts += 1
    for pmid, quote in [("10612741", "These data strongly suggested that R. eutropha PHA synthase accepts"),
                        ("35341893", "without any synthase modification")]:
        path = record(ROOT / f"publications/PMID_{pmid}.md")
        assert quote in normalized(path.read_text())
        excerpts += 1
    # Retain durable alternatives for every historical ignored acquisition path.
    aliases = read(AUDIT / "capacity-consultation/publication-bundle/mapping.json")["files"]
    for alias in aliases:
        assert sha(record(ROOT / alias["published_path"])) == alias["sha256"]
    capacity = read(HERE / "capacity-results.json")
    assert capacity["status"] == "PASS" and capacity["module_sha256"] == sha(ROOT / module_name)
    for name, expected in capacity["input_hashes"].items():
        assert sha(record(ROOT / name)) == expected, name
    record(HERE / "check_closure.py")
    verify_seal()
    for name, expected in inputs.items():
        assert sha(ROOT / name) == expected, name
    output = {
        "status": "PASS" if not missing and not quote_failures else "NEEDS_FOLLOWUP",
        "counts": {"members": 9, "families": 4, "modules": 1,
                   "original_ordered_rows": ordered, "original_machine_rows": ordered - historical,
                   "historical_NEW_preserved": historical, "previously_authored_NEW_preserved": added,
                   "retired_historical_NEW": retired, "final_rows": ordered + added,
                   "new_rows_authored_in_round2": 0, "protected_baseline_sources": len(protected),
                   "sealed_dependency_entries": 433, "prior_input_entries_retained": len(prior),
                   "explicit_reference_sources": len(sources), "explicit_reference_edges": len(unique(edges)),
                   "distinct_literal_quotes": len(unique(quotes)), "independent_primary_excerpts": excerpts,
                   "durable_cache_aliases": len(aliases)},
        "module_sha256": sha(ROOT / module_name), "member_documents": sorted(member_names),
        "family_documents": sorted(family_names), "transitively_scanned_documents": sorted(visited),
        "explicit_science_supersessions": superseded, "reference_edges": unique(edges),
        "quotes": unique(quotes), "missing_sources": sorted(set(missing)),
        "quote_failures": quote_failures, "source_hashes": dict(sorted(sources.items())),
        "historical_cache_aliases": aliases, "input_hashes": dict(sorted(inputs.items())),
        "limits": "Explicit local/PMID reference closure and literal source verification, not a replacement for scientific source assessment or production validation. No source acquisition or source mutation."}
    (HERE / "closure-results.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": output["status"], "counts": output["counts"],
                      "missing_sources": output["missing_sources"], "quote_failures": quote_failures}))
    return output


if __name__ == "__main__":
    result = run()
    assert result["status"] == "PASS"
