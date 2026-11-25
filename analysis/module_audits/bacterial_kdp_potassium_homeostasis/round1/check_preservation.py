"""Verify PR6179 published payloads, immutable inputs and bounded member guards."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    failures, changes = [], []
    original_rows = historical_new = retired = nodes = 0
    for rel, frozen in baseline["reviews"].items():
        current = yaml.safe_load((ROOT / rel).read_text())
        rows = current["existing_annotations"]
        original_rows += len(rows)
        payloads = [{k: v for k, v in row.items() if k != "review"} for row in rows]
        if payloads != frozen["ordered_payloads"]:
            failures.append("Ordered payload mismatch: " + rel)
        for index, (old, new) in enumerate(
            zip(frozen["document"]["existing_annotations"], rows, strict=True)
        ):
            before, after = old["review"]["action"], new["review"]["action"]
            historical_new += before == "NEW"
            retired += bool(old.get("retired") or old["review"].get("retired"))
            if before == "NEW" and before != after:
                failures.append("Historical NEW action changed: " + rel)
            if old["review"].get("retired") != new["review"].get("retired"):
                failures.append("Review retirement changed: " + rel)
            if before != after:
                changes.append(
                    {
                        "path": rel,
                        "index": index,
                        "term": old["term"]["id"],
                        "before": before,
                        "after": after,
                    }
                )
    for rel, frozen in baseline["families"].items():
        current = yaml.safe_load((ROOT / rel).read_text())

        def payload(row):
            return {
                k: v
                for k, v in row.items()
                if k not in {"assessment", "assessment_reason", "supported_by"}
            }

        old = [payload(n) for n in frozen["document"].get("node_assessments", [])]
        new = [payload(n) for n in current.get("node_assessments", [])]
        nodes += len(old)
        if old != new:
            failures.append("PAINT assertion payload mismatch: " + rel)
    for rel, expected in baseline["protected"].items():
        if digest(ROOT / rel) != expected:
            failures.append("Protected file changed: " + rel)
    historical = json.loads(
        (HERE.parent / "family-consultation/historical-scope.json").read_text()
    )
    guards = yaml.safe_load((HERE / "member-guards.yaml").read_text())
    assert (
        guards["historical_GO0000155_member_exceptions"]
        == historical["PTHR45569_GO0000155"]["member_exceptions"]
    )
    for guard in guards["current_member_guards"]:
        accession = guard["accession"]
        record = json.loads(
            (HERE.parent / "family-consultation" / (accession + ".json")).read_text()
        )
        xrefs = {x["id"] for x in record.get("uniProtKBCrossReferences", [])}
        assert not {"PF00512", "PF02518"} & xrefs, accession
        assert {"PTHR45569", "PTHR45569:SF1"} & xrefs, accession
    # The measured Dgeo serine kinase must not become a canonical histidine kinase.
    dgeo = yaml.safe_load(
        (ROOT / "genes/DEIGD/Dgeo_2852/Dgeo_2852-ai-review.yaml").read_text()
    )
    assert all(
        c.get("molecular_function", {}).get("id") != "GO:0000155"
        for c in dgeo["core_functions"]
    )
    assert any(
        c.get("molecular_function", {}).get("id") == "GO:0106310"
        for c in dgeo["core_functions"]
    )
    assert all(
        a["review"]["action"] == "UNDECIDED"
        for a in dgeo["existing_annotations"]
        if a["term"]["id"] in {"GO:0005737", "GO:0005886", "GO:0016020"}
    )
    result = {
        "status": "FAIL" if failures else "PASS",
        "reviews": len(baseline["reviews"]),
        "ordered_payloads": original_rows,
        "historical_NEW": historical_new,
        "retired_rows": retired,
        "families": len(baseline["families"]),
        "PAINT_assertions": nodes,
        "protected_files": len(baseline["protected"]),
        "named_member_guards": 3,
        "exact_archived_exceptions": 2,
        "action_changes": changes,
        "failures": failures,
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
