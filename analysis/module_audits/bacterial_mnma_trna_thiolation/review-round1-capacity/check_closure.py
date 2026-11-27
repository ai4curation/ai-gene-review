"""Additive full-document source closure and explicit historical supersession.

All inputs are repository-relative and read-only. Historical releases are checked
at their own hashes; only paths explicitly included in the accepted correction
seal may supersede a historical scientific input. No old receipt is rewritten.
"""

import hashlib
import json
import re
from pathlib import Path

import yaml
from accepted_seal import current_seal

A = Path(__file__).resolve().parent
BASE = A.parent
ROOT = A.parents[3]
INPUTS = {}
SUPERSESSIONS = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    assert path.is_file(), path
    INPUTS[str(path.relative_to(ROOT))] = sha(path)
    return path


def read(path):
    return yaml.safe_load(record(path).read_text())


def walk(value, reference=None):
    if isinstance(value, dict):
        reference = value.get("reference_id", value.get("source_id", value.get("id", reference)))
        yield value, reference
        for child in value.values():
            yield from walk(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child, reference)


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def normalized(text):
    text = re.sub(r"(?m)^CC\s{3}", "", text)
    return re.sub(r"\s+", " ", text).strip()


def source_path(ref):
    if not isinstance(ref, str):
        return None
    if ref.startswith("PMID:"):
        return record("publications/PMID_" + ref.split(":")[1] + ".md")
    if ref.startswith("file:"):
        path = ROOT / ref[5:]
        if not path.exists():
            path = ROOT / "genes" / ref[5:]
        return record(path)
    return None


def run():
    seal = current_seal()
    record(A / "accepted-science-seal.json")
    record(A / "quote-supersession.json")
    record(A / "accepted_seal.py")
    for name, expected in seal.items():
        assert sha(record(name)) == expected, name

    def historical_files(files, receipt):
        for name, expected in files.items():
            actual = sha(record(name))
            if actual != expected:
                assert name in seal and actual == seal[name], (receipt, name)
                SUPERSESSIONS.append({"receipt": receipt, "path": name,
                                      "historical_sha256": expected, "accepted_sha256": actual})

    # Preserve each old release; changed science is an explicit additive supersession.
    releases = {}
    for folder, filename in [
        ("existing-review-consultation", "handoff.yaml"),
        ("new-member-consultation", "handoff.json"),
        ("family-consultation", "handoff.json"),
        ("independent-module-review", "handoff.json"),
        ("capacity-consultation", "handoff.json"),
    ]:
        path = record(BASE / folder / filename)
        manifest = read(path)
        label = str(path.relative_to(ROOT))
        historical_files(manifest["files"], label)
        releases[label] = {"sha256": sha(path), "files_verified_or_explicitly_superseded": len(manifest["files"])}
    fi = read(BASE / "family-consultation/input-closure.json")
    historical_files(fi["files"], "family-consultation/input-closure.json")
    prior_status = read(BASE / "module-status-supersession.json")
    prior_capacity = read(BASE / "capacity-consultation/results.json")
    assert prior_status["after_sha256"] == prior_capacity["module_sha256"]
    # This old DRAFT->COMPLETE receipt is historical; round-one is a substantive successor.
    assert prior_status["after_sha256"] != sha(ROOT / "modules/bacterial_mnma_trna_thiolation.yaml")

    original = read(BASE / "baseline.yaml")
    seeds = read(BASE / "new-seed-baseline.yaml")
    expected = dict(original["existing_annotation_rows"])
    for seed in seeds["seeds"]:
        expected[seed["review"]] = [payload(row) for row in seed["rows"]]
    assert len(expected) == 19
    round1_before = read(BASE / "review-round1-consultation/input-baseline.json")
    for name, expected_hash in round1_before["protected_hashes"].items():
        assert sha(record(name)) == expected_hash, name
    member_records = []
    documents = []
    authored = []
    for name, prior_rows in sorted(expected.items()):
        review = read(name)
        rows = review["existing_annotations"]
        assert [payload(row) for row in rows[:len(prior_rows)]] == prior_rows, name
        extra = rows[len(prior_rows):]
        if name == "genes/THET2/mnmA/mnmA-ai-review.yaml":
            assert len(extra) == 1 and extra[0]["term"]["id"] == "GO:0051539"
            assert extra[0]["evidence_type"] == "IDA" and extra[0]["review"]["action"] == "NEW"
            authored.append({"review": name, "index": len(prior_rows), "row": extra[0]})
        else:
            assert not extra, name
        for old in round1_before["historical_new"][name]:
            assert old in rows, name
        member_records.append({"review": name, "accession": review["id"],
                               "inherited_rows": len(prior_rows), "final_rows": len(rows)})
        documents.append((name, review))
    assert sum(r["inherited_rows"] for r in member_records) == 166
    assert sum(len(v) for v in round1_before["historical_new"].values()) == 4
    assert len(authored) == 1
    families = ["PTHR11601", "PTHR11933", "PTHR43586", "PTHR37526",
                "PTHR37010", "PTHR38780", "PTHR33279", "PTHR34874"]
    for family in families:
        name = f"interpro/panther/{family}/{family}-review.yaml"
        documents.append((name, read(name)))
    module_name = "modules/bacterial_mnma_trna_thiolation.yaml"
    module = read(module_name)
    assert module["status"] == "COMPLETE"
    documents.append((module_name, module))

    sources = {}
    edges = []
    quotes = []
    for label, document in documents:
        for obj, inherited_ref in walk(document):
            for key in ["id", "reference_id", "source_id"]:
                path = source_path(obj.get(key))
                if path is not None:
                    name = str(path.relative_to(ROOT))
                    sources[name] = sha(path)
                    edges.append({"document": label, "reference": obj[key], "source": name})
            if obj.get("supporting_text"):
                path = source_path(inherited_ref)
                assert path is not None, (label, inherited_ref)
                quote = obj["supporting_text"]
                assert normalized(quote) in normalized(path.read_text()), (label, inherited_ref, quote)
                quotes.append({"document": label, "source": str(path.relative_to(ROOT)), "quote": quote})
            # Family cross-links are explicit local dependencies even without a quotation.
            if isinstance(obj.get("gene_review"), str):
                record(obj["gene_review"])

    # Include the previous source-supplement scope and all the accepted 41 dependencies.
    previous_sources = read(BASE / "source-closure-supplement.json")
    historical_files(previous_sources["additional_source_hashes"], "source-closure-supplement.json")
    for name in previous_sources["additional_source_hashes"]:
        sources[name] = sha(record(name))
    new_member_sources = read(BASE / "new-member-consultation/preservation-and-evidence.json")["source_dependencies"]
    historical_files(new_member_sources, "new-member-consultation/preservation-and-evidence.json")
    for name in new_member_sources:
        sources[name] = sha(record(name))
    scoped = read(BASE / "review-round1-consultation/source-closure.json")["sources"]
    assert len(scoped) == 41
    for name, info in scoped.items():
        assert sha(record(name)) == info["sha256"], name
        sources[name] = info["sha256"]
    for table in [original["source_files_sha256"], seeds["source_files_sha256"]]:
        for name, expected_hash in table.items():
            if name.endswith(("-ai-review.yaml", "-review.yaml")) or name.startswith("modules/"):
                continue
            assert sha(record(name)) == expected_hash, name
            sources[name] = expected_hash
    capacity = read(A / "results.json")
    assert capacity["status"] == "PASS" and capacity["module_sha256"] == sha(ROOT / module_name)
    for name, expected_hash in capacity["input_hashes"].items():
        assert sha(record(name)) == expected_hash, name
    record(Path(__file__).resolve())
    # Check again after all source reads: neither checking nor concurrent work changed inputs.
    for name, expected_hash in INPUTS.items():
        assert sha(ROOT / name) == expected_hash, name
    def unique(rows):
        return sorted({json.dumps(r, sort_keys=True): r for r in rows}.values(),
                      key=lambda r: json.dumps(r, sort_keys=True))
    return {
        "status": "PASS",
        "module_sha256": sha(ROOT / module_name),
        "counts": {"members": 19, "families": 8, "modules": 1,
                   "original_machine_rows": 162, "historical_NEW_unchanged": 4,
                   "authored_NEW": 1, "final_rows": 167, "active_NEW": 5,
                   "sources_including_frozen_acquisition_dependencies": len(sources),
                   "direct_document_reference_edges": len(unique(edges)),
                   "distinct_exact_document_quotes": len(unique(quotes)),
                   "accepted_supplement_dependencies": 41},
        "member_records": member_records, "authored_NEW": authored,
        "historical_receipts": releases, "explicit_science_supersessions": unique(SUPERSESSIONS),
        "prior_status_receipt": {"historical_after_sha256": prior_status["after_sha256"],
                                 "interpretation": "Preserved historical status-only change; current science is the explicitly sealed substantive successor."},
        "reference_edges": unique(edges), "quotes": unique(quotes),
        "source_hashes": dict(sorted(sources.items())),
        "input_hashes": dict(sorted(INPUTS.items())),
        "limits": ["Direct explicit local/PMID references of all 28 curated documents are resolved, including reference-list entries without quotes.",
                   "Frozen acquisition dependencies and the earlier source supplement are included; external URLs and database identifiers are not downloaded.",
                   "Source presence and exact quotation do not replace the manual scientific assessments."]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
