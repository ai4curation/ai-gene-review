"""Read-only deterministic module/member/source and historical payload closure."""

import hashlib
import json
import re
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
BASE = A.parent
ROOT = A.parents[3]
INPUTS = {}


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


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def normalized(text):
    # UniProt continuation record prefixes are formatting, not quotation content.
    text = re.sub(r"(?m)^CC\s{3}", "", text)
    return re.sub(r"\s+", " ", text)


def source_path(ref):
    if ref.startswith("PMID:"):
        return record("publications/PMID_" + ref.split(":")[1] + ".md")
    if ref.startswith("file:"):
        path = ROOT / ref[5:]
        if not path.exists():
            path = ROOT / "genes" / ref[5:]
        return record(path)
    raise AssertionError(ref)


def run():
    module_path = record("modules/bacterial_mnma_trna_thiolation.yaml")
    module = read(module_path)
    assert module["status"] == "COMPLETE"
    status = read(BASE / "module-status-supersession.json")
    assert sha(module_path) == status["after_sha256"]
    prior = module_path.read_bytes().replace(
        b"status: COMPLETE\n", b"status: DRAFT\n", 1
    )
    assert hashlib.sha256(prior).hexdigest() == status["before_sha256"]
    releases = {}
    for folder, filename in [
        ("existing-review-consultation", "handoff.yaml"),
        ("new-member-consultation", "handoff.json"),
        ("family-consultation", "handoff.json"),
        ("independent-module-review", "handoff.json"),
    ]:
        path = record(BASE / folder / filename)
        manifest = read(path)
        for name, expected in manifest["files"].items():
            assert sha(record(name)) == expected, name
        releases[str(path.relative_to(ROOT))] = {
            "sha256": sha(path),
            "files_verified": len(manifest["files"]),
        }
    family_inputs = read(BASE / "family-consultation/input-closure.json")
    for name, expected in family_inputs["files"].items():
        assert sha(record(name)) == expected, name
    for name in [
        "root-progress-verification.json",
        "root-family-and-new-member-receipt.json",
        "root-existing-review-receipt.yaml",
        "module-research-provenance.yaml",
        "module-falcon-failure.log",
    ]:
        record(BASE / name)
    history = list(
        (ROOT / "history/modules/bacterial_mnma_trna_thiolation").glob("*113621Z*.yaml")
    )
    assert len(history) == 1
    record(history[0])
    baseline = read(BASE / "baseline.yaml")
    seeds = read(BASE / "new-seed-baseline.yaml")
    rows = dict(baseline["existing_annotation_rows"])
    for seed in seeds["seeds"]:
        rows[seed["review"]] = [payload(row) for row in seed["rows"]]
    assert len(rows) == 19
    originals = 0
    historical_new = 0
    active_new = 0
    member_records = []
    documents = [("module", module)]
    for name, expected_rows in sorted(rows.items()):
        review = read(name)
        current_rows = review["existing_annotations"]
        assert [payload(row) for row in current_rows] == expected_rows, name
        originals += len(expected_rows)
        new_indices = [
            i for i, row in enumerate(current_rows) if row["review"]["action"] == "NEW"
        ]
        assert new_indices == baseline["historical_new_rows"].get(name, []), name
        historical_new += len(new_indices)
        active_new += sum(
            not current_rows[i].get("retired", False) for i in new_indices
        )
        member_records.append(
            {
                "accession": review["id"],
                "review": name,
                "review_sha256": sha(ROOT / name),
                "rows": len(current_rows),
                "historical_NEW": len(new_indices),
            }
        )
        documents.append((name, review.get("core_functions", [])))
    protected = 0
    for table in [baseline["source_files_sha256"], seeds["source_files_sha256"]]:
        for name, expected in table.items():
            if (
                name.endswith("-ai-review.yaml")
                or name.endswith("-review.yaml")
                or name.startswith("modules/")
            ):
                continue
            assert sha(record(name)) == expected, name
            protected += 1
    quotes = []
    source_edges = []
    for label, document in documents:
        for obj in walk(document):
            ref = obj.get("source_id", obj.get("reference_id"))
            if not ref:
                continue
            path = source_path(ref)
            source_edges.append(
                {"from": label, "to": str(path.relative_to(ROOT)), "sha256": sha(path)}
            )
            if obj.get("supporting_text"):
                quote = obj["supporting_text"]
                assert normalized(quote) in normalized(path.read_text()), (
                    label,
                    ref,
                    quote,
                )
                quotes.append(
                    {
                        "from": label,
                        "source": str(path.relative_to(ROOT)),
                        "quote": quote,
                    }
                )
    assert originals == 166 and historical_new == active_new == 4
    capacity = json.loads((A / "results.json").read_text())
    assert capacity["status"] == "PASS" and capacity["module_sha256"] == sha(
        module_path
    )
    for name, expected in capacity["input_hashes"].items():
        assert sha(record(name)) == expected, name
    # Deduplication/sorting is explicit: no set traversal can reorder a frozen quote ledger.
    quotes = sorted(
        {json.dumps(q, sort_keys=True): q for q in quotes}.values(),
        key=lambda q: (q["from"], q["source"], q["quote"]),
    )
    source_edges = sorted(
        {json.dumps(e, sort_keys=True): e for e in source_edges}.values(),
        key=lambda e: (e["from"], e["to"]),
    )
    record(Path(__file__).resolve())
    if (A / "handoff.json").exists():
        for name, expected in yaml.safe_load((A / "handoff.json").read_text())[
            "files"
        ].items():
            assert sha(ROOT / name) == expected, name
    return {
        "status": "PASS",
        "module_sha256": sha(module_path),
        "reviewed_prior_module_status_exception_verified": True,
        "counts": {
            "reviews": len(member_records),
            "ordered_rows": originals,
            "historical_NEW": historical_new,
            "active_NEW": active_new,
            "retired_NEW": historical_new - active_new,
            "protected_baseline_source_entries": protected,
            "exact_module_and_member_core_quotes": len(quotes),
        },
        "member_records": member_records,
        "release_receipts": releases,
        "source_edges": source_edges,
        "quotes": quotes,
        "input_hashes": dict(sorted(INPUTS.items())),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
