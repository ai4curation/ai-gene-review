"""Verify released consultation hashes, ordered row payloads and protected source bytes."""

from pathlib import Path
import hashlib
import json
import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
PLAN = yaml.safe_load((A / "closure.yaml").read_text())
FILES = {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def record(p):
    assert p.is_file(), str(p)
    rel = str(p.relative_to(ROOT))
    assert not rel.startswith(".cache/"), rel
    FILES[rel] = sha(p)


def source_payload(row):
    return {k: v for k, v in row.items() if k != "review"}


def reference_ids(obj):
    if isinstance(obj, dict):
        for key, val in obj.items():
            if (
                key in {"source_id", "reference_id", "id"}
                and isinstance(val, str)
                and val.startswith(("PMID:", "file:"))
            ):
                yield val
            yield from reference_ids(val)
    elif isinstance(obj, list):
        for val in obj:
            yield from reference_ids(val)


def main():
    base_path = ROOT / PLAN["baseline"]
    new_path = ROOT / PLAN["new_seed_baseline"]
    base = yaml.safe_load(base_path.read_text())
    new = yaml.safe_load(new_path.read_text())
    record(base_path)
    record(new_path)
    record(A / "closure.yaml")
    record(Path(__file__).resolve())
    count = 0
    historical = 0
    active = 0
    retired = 0
    new_count = 0
    reviews = []
    for path, rows in base["existing_annotation_rows"].items():
        p = ROOT / path
        d = yaml.safe_load(p.read_text())
        current = d.get("existing_annotations", [])
        assert [source_payload(x) for x in current] == rows, path
        count += len(current)
        reviews.append(p)
        for i in base["historical_new_rows"][path]:
            historical += 1
            assert current[i]["review"]["action"] == "NEW", (path, i)
            active += not current[i].get("retired", False)
        retired += sum(bool(r.get("retired")) for r in current)
    for seed in new["seeds"]:
        p = ROOT / seed["review"]
        d = yaml.safe_load(p.read_text())
        rows = d.get("existing_annotations", [])
        assert [source_payload(x) for x in rows] == [
            source_payload(x) for x in seed.get("rows", [])
        ], seed["review"]
        new_count += len(rows)
        reviews.append(p)
        retired += sum(bool(r.get("retired")) for r in rows)
    protected = []
    for source in [base, new]:
        for path, expected in source["source_files_sha256"].items():
            if (
                path.endswith(("-ai-review.yaml", "-review.yaml"))
                or path == PLAN["module"]
            ):
                continue
            p = ROOT / path
            assert sha(p) == expected, path
            record(p)
            protected.append(path)
    receipts = []
    supersession = json.loads((ROOT / PLAN["supersession_receipt"]).read_text())
    record(ROOT / PLAN["supersession_receipt"])
    overrides = {x["path"]: x for x in supersession["changes"]}
    assert len(overrides) == 3
    old_handoff = json.loads((ROOT / supersession["supersedes"]["path"]).read_text())
    assert (
        sha(ROOT / supersession["supersedes"]["path"])
        == supersession["supersedes"]["sha256"]
    )
    new_handoff = json.loads((ROOT / PLAN["supersession_handoff"]).read_text())
    for name, change in overrides.items():
        assert old_handoff["files"][name] == change["before_sha256"]
        assert new_handoff["files"][name] == change["after_sha256"]
    for item in PLAN["receipts"]:
        p = ROOT / item["path"]
        d = json.loads(p.read_text())
        record(p)
        if item.get("expected_sha256"):
            assert sha(p) == item["expected_sha256"], item["path"]
        for path, expected in d["files"].items():
            f = ROOT / item["path_base"] / path
            if item["path"] == supersession["supersedes"]["path"] and path in overrides:
                assert expected == overrides[path]["before_sha256"]
                expected = overrides[path]["after_sha256"]
            assert sha(f) == expected, str(f)
            record(f)
        receipts.append(
            {"path": item["path"], "sha256": sha(p), "files": len(d["files"])}
        )
    for path in PLAN["root_provenance"]:
        record(ROOT / path)
    module = ROOT / PLAN["module"]
    doc = yaml.safe_load(module.read_text())
    record(module)
    assert doc["status"] == "COMPLETE", (
        "Await final module COMPLETE before closure freeze"
    )
    html = ROOT / "pages/modules" / module.with_suffix(".html").name
    record(html)
    histories = list(
        (
            ROOT / "history/modules/bacterial_mla_intermembrane_phospholipid_transport"
        ).glob("*.yaml")
    )
    assert histories, "Missing module provenance"
    for p in histories:
        record(p)
    for p in reviews + [module]:
        record(p)
        for ref in reference_ids(yaml.safe_load(p.read_text())):
            if ref.startswith("PMID:"):
                source = ROOT / f"publications/PMID_{ref[5:]}.md"
            else:
                source = ROOT / ref[5:]
                if not source.is_file():
                    source = ROOT / "genes" / ref[5:]
            record(source)
    inputs = json.loads((A / "input-hashes.json").read_text())
    for path, expected in inputs.items():
        p = ROOT / path
        assert sha(p) == expected, path
        record(p)
    for p in [
        "src/ai_gene_review/render_modules.py",
        "src/ai_gene_review/module_gene_symbols.py",
        "src/ai_gene_review/module_qc.py",
    ]:
        record(ROOT / p)
    actual = {
        "existing_rows": count,
        "seeded_rows": new_count,
        "historical_NEW": historical,
        "active_historical_NEW": active,
        "added_rows": 0,
        "retired_rows": retired,
    }
    assert actual == PLAN["expected"], actual
    result = {
        "result": "PASS",
        "annotation_accounting": actual,
        "ordered_source_payloads_preserved": count + new_count,
        "baseline_protected_sources": len(set(protected)),
        "receipt_verification": receipts,
        "authorized_family_prose_supersessions": list(overrides),
        "module_sha256": sha(module),
        "closure_files": len(FILES),
        "scope": "Scientific inputs; project/full-corpus/publication metadata excluded.",
    }
    (A / "input-closure.json").write_text(
        json.dumps(dict(sorted(FILES.items())), indent=2) + "\n"
    )
    (A / "closure-result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
