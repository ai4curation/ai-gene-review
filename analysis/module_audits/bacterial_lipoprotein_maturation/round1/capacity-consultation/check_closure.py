"""Additive closure with one exact payload exception and explicit changed-file chain."""

import copy
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

from check_capacity import BASE, EXPECTED_MODULE, HERE, OLD, ROOT, legacy, sha

GENE_RECEIPT_SHA = "89bf965e50a34a700a9eed24c9fa0ab33d2ab5dadb7c71ca33455848965318cd"
FAMILY_RECEIPT_SHA = "04f6e4b0087866217669082d451772e217e0a642669e5ca7ed9df19774123ccb"
EXCEPTION_PATH = "genes/BACCR/BC_1526/BC_1526-ai-review.yaml"


def norm(text):
    return " ".join(text.split())


def main():
    baseline_path = BASE / "round1/baseline.json"
    baseline = json.loads(baseline_path.read_text())
    inputs = {str(baseline_path.relative_to(ROOT)): sha(baseline_path)}
    manifests = []
    new_manifests = {}
    for name, expected in [("gene", GENE_RECEIPT_SHA), ("family", FAMILY_RECEIPT_SHA)]:
        path = BASE / f"round1/{name}-consultation/handoff.json"
        assert sha(path) == expected, path
        doc = json.loads(path.read_text())
        for filename, digest in doc["files"].items():
            assert sha(ROOT / filename) == digest, filename
            inputs[filename] = digest
        inputs[str(path.relative_to(ROOT))] = expected
        new_manifests[name] = doc
        manifests.append(
            {
                "name": name,
                "path": str(path.relative_to(ROOT)),
                "sha256": expected,
                "verified_files": len(doc["files"]),
            }
        )
    allowed = {"modules/bacterial_lipoprotein_maturation.yaml"}
    for path in new_manifests["gene"]["review_paths"]:
        folder = Path(path).parent
        stem = folder.name
        for suffix in ["ai-review.yaml", "ai-review.html", "notes.md"]:
            candidate = str(folder / f"{stem}-{suffix}")
            assert candidate in new_manifests["gene"]["files"]
            allowed.add(candidate)
    allowed.add("interpro/panther/PTHR38686/PTHR38686-review.yaml")
    assert (
        "interpro/panther/PTHR38686/PTHR38686-review.yaml"
        in new_manifests["family"]["files"]
    )
    old_inputs = json.loads((OLD / "final-input-hashes.json").read_text())
    deviations = []
    for path, before in old_inputs.items():
        after = sha(ROOT / path)
        if after != before:
            assert path in allowed, ("Unauthorized old-closure deviation", path)
            deviations.append(
                {
                    "path": path,
                    "published_sha256": before,
                    "round1_sha256": after,
                    "authority": "root module change"
                    if path.startswith("modules/")
                    else "frozen gene consultation"
                    if path.startswith("genes/")
                    else "frozen family consultation",
                }
            )
        inputs[path] = after
    assert len(deviations) == 29
    assert {d["path"] for d in deviations} == allowed
    project_provenance = json.loads(
        (HERE / "project-deviation-provenance.json").read_text()
    )
    assert (
        project_provenance["baseline_head"]
        == baseline["head"]
        == "209d07bd1efe2e5cd8e04fd8025d42b22662cef6"
    )
    project_paths = {r["path"] for r in project_provenance["files"]}
    assert project_paths == {
        "projects/MODULE_TAXON_AUDIT.md",
        "projects/MODULE_TAXON_AUDIT/inventory.json",
        "pages/projects/MODULE_TAXON_AUDIT.html",
        "pages/projects/MODULE_TAXON_AUDIT/inventory.json",
    }
    published_deviations = []
    historical_count = 0
    for path, expected in baseline["published_closure_sha256"].items():
        if path in project_paths:
            blob = subprocess.check_output(
                ["git", "show", f"{baseline['head']}:{path}"], cwd=ROOT
            )
            pinned_digest = hashlib.sha256(blob).hexdigest()
            recorded = next(r for r in project_provenance["files"] if r["path"] == path)
            assert recorded["HEAD_identical"]
            assert recorded["HEAD_sha256"] == pinned_digest
            assert recorded["baseline_head_sha256"] == pinned_digest
            assert recorded["current_sha256"] == pinned_digest
            assert recorded["published_science_manifest_sha256"] == expected
            published_deviations.append(
                {
                    "path": path,
                    "before": expected,
                    "after_at_round1_baseline": pinned_digest,
                    "kind": "Pre-existing science-manifest versus pinned publication-head difference; mutable project metadata excluded from scientific closure",
                }
            )
            continue
        actual = sha(ROOT / path)
        if path.startswith(("analysis/", "history/")):
            assert actual == expected, ("Historical receipt rewritten", path)
            historical_count += 1
        if actual != expected:
            assert (
                path in allowed
                or path == "pages/modules/bacterial_lipoprotein_maturation.html"
            ), path
            published_deviations.append(
                {
                    "path": path,
                    "before": expected,
                    "after": actual,
                    "kind": "Explicit round1 science edit or its root-rendered module HTML",
                }
            )
        inputs[path] = actual
    assert historical_count == 188 and len(published_deviations) == 34
    for path, expected in baseline["protected_sources_sha256"].items():
        assert sha(ROOT / path) == expected, path
        inputs[path] = expected
    rows = new_count = 0
    exceptions = []
    for path, frozen in baseline["reviews"].items():
        current = yaml.safe_load((ROOT / path).read_text())
        before = frozen["document"]["existing_annotations"]
        after = current["existing_annotations"]
        assert len(before) == len(after)
        for index, (a, b) in enumerate(zip(before, after, strict=True)):
            pa = {k: v for k, v in a.items() if k != "review"}
            pb = {k: v for k, v in b.items() if k != "review"}
            if pa != pb:
                assert path == EXCEPTION_PATH and index == 2
                assert (
                    pa["term"]["id"] == "GO:0005886"
                    and pa["original_reference_id"] == "PMID:34253723"
                )
                assert pa["evidence_type"] == "IDA" and pb["evidence_type"] == "IC"
                expected = copy.deepcopy(pa)
                expected["evidence_type"] = "IC"
                assert pb == expected
                assert a["review"]["action"] == b["review"]["action"] == "NEW"
                exceptions.append(
                    {
                        "path": path,
                        "index": index,
                        "field": "evidence_type",
                        "before": "IDA",
                        "after": "IC",
                        "reason": "Explicitly authorized correction of authored native-compartment inference; all other row fields and lifecycle preserved.",
                    }
                )
            assert (a["review"]["action"] == "NEW") == (b["review"]["action"] == "NEW")
            assert a.get("retired", False) == b.get("retired", False)
            if a["review"]["action"] == "NEW":
                assert not b.get("retired", False)
                new_count += 1
        rows += len(before)
        inputs[path] = sha(ROOT / path)
    assert rows == 88 and new_count == 16 and len(exceptions) == 1
    old_manifests = []
    for path in sorted(BASE.glob("*-consultation/handoff.*")):
        doc = yaml.safe_load(path.read_text())
        files = doc.get("files", doc.get("files_sha256", {}))
        assert files
        altered = []
        for filename, expected in files.items():
            if isinstance(expected, dict):
                expected = expected["sha256"]
            actual = sha(ROOT / filename)
            if actual != expected:
                assert filename in allowed, (path, filename)
                altered.append(filename)
            inputs[filename] = actual
        old_manifests.append(
            {
                "path": str(path.relative_to(ROOT)),
                "historical_manifest_sha256": sha(path),
                "files": len(files),
                "explicitly_superseded_files": altered,
            }
        )
    module = yaml.safe_load(legacy.MODULE.read_text())
    assert sha(legacy.MODULE) == EXPECTED_MODULE and module["status"] == "COMPLETE"
    references = []
    quote_count = 0
    for ref in module["references"]:
        source = legacy.resolve(ref["id"])
        text = source.read_text()
        meta = yaml.safe_load(text.split("---", 2)[1])
        assert norm(meta["title"]) == norm(ref["title"])
        assert ref.get("reference_review")
        for finding in ref.get("findings", []):
            if finding.get("supporting_text"):
                assert norm(finding["supporting_text"]) in norm(text)
                quote_count += 1
        references.append(
            {
                "id": ref["id"],
                "type": ref["publication_type"],
                "findings": len(ref.get("findings", [])),
                "sha256": sha(source),
            }
        )
        inputs[str(source.relative_to(ROOT))] = sha(source)
    assert len(references) == 11 and sum(r["type"] == "REVIEW" for r in references) == 3
    assert sum(r["type"] == "PRIMARY_RESEARCH" for r in references) == 8
    assert sum(r["findings"] for r in references) == 23
    old_closure = json.loads((OLD / "closure-results.json").read_text())
    for quote in old_closure["mechanistic_quotes"]:
        source = legacy.resolve(quote["reference_id"])
        assert sha(source) == quote["source_sha256"]
        assert norm(quote["supporting_text"]) in norm(source.read_text())
    for path, digest in json.loads((HERE / "source-hashes.json").read_text()).items():
        assert sha(ROOT / path) == digest
        inputs[path] = digest
    for path in [
        BASE / "round1/root-module-change.json",
        legacy.MODULE,
        ROOT / "pages/modules/bacterial_lipoprotein_maturation.html",
    ]:
        inputs[str(path.relative_to(ROOT))] = sha(path)
    assert not project_paths.intersection(inputs)
    receipt = {
        "result": "PASS",
        "module_sha256": EXPECTED_MODULE,
        "released_round1_handoffs": manifests,
        "published_input_count": len(old_inputs),
        "explicit_input_deviations": deviations,
        "unchanged_published_artifacts": historical_count,
        "published_manifest_paths": len(baseline["published_closure_sha256"]),
        "published_manifest_deviations": published_deviations,
        "preexisting_project_differences": project_provenance,
        "mutable_project_metadata_excluded": sorted(project_paths),
        "project_metadata_closure": "Root will separately freeze updated project metadata and its new history at science commit; no working-tree project equality to old HEAD is asserted on rerun.",
        "protected_source_count": len(baseline["protected_sources_sha256"]),
        "review_count": len(baseline["reviews"]),
        "ordered_rows": rows,
        "historical_NEW": new_count,
        "active_NEW": new_count,
        "retired_NEW": 0,
        "authorized_payload_exceptions": exceptions,
        "historical_manifests": old_manifests,
        "references": references,
        "module_reference_quotes": quote_count,
        "retained_mechanistic_quotes": len(old_closure["mechanistic_quotes"]),
        "current_input_count": len(inputs),
        "full_corpus_validation": False,
        "limits": "Old manifest hashes remain historical; only the listed exact scientific file changes supersede them. No blanket waiver of old source or payload mismatch. New native-flux or full-corpus claims are not made.",
    }
    (HERE / "closure-results.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (HERE / "final-input-hashes.json").write_text(json.dumps(inputs, indent=2) + "\n")
    print(
        json.dumps(
            {
                "result": "PASS",
                "ordered_rows": rows,
                "historical_NEW": new_count,
                "payload_exceptions": len(exceptions),
                "input_deviations": len(deviations),
                "preserved_old_artifacts": historical_count,
            }
        )
    )


if __name__ == "__main__":
    main()
