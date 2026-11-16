"""Additive closure: explicit fifteen-file supersession, no old receipt writes."""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
OLD = AUDIT / "capacity-consultation"
IMPL = HERE.parent / "implementation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k not in {"review", "retired"}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", action="store_true")
    args = parser.parse_args()
    old = json.loads((OLD / "input-closure.json").read_text())
    implementation = json.loads((IMPL / "handoff.json").read_text())
    assert sha(IMPL / "handoff.json") == "f7f29cf77e74763212fc72e73ba5e958913e65e9d8498038f74db96d8f885f33"
    inputs = {}
    superseded = []
    for path, original in old["files"].items():
        current = sha(ROOT / path)
        if current != original:
            assert implementation["files"].get(path) == current, path
            superseded.append({"path": path, "previous_sha256": original,
                               "current_sha256": current, "authorized_by": str((IMPL / "handoff.json").relative_to(ROOT))})
        inputs[path] = current
    assert len(superseded) == 15
    # Every original input remains in the new closure; no exclusion list silently
    # shrinks the published scientific closure or waives raw-file verification.
    assert set(old["files"]).issubset(inputs)
    for path, expected in implementation["files"].items():
        assert sha(ROOT / path) == expected, path
        inputs[path] = expected
    inputs[str((IMPL / "handoff.json").relative_to(ROOT))] = sha(IMPL / "handoff.json")
    for f in OLD.rglob("*"):
        if f.is_file() and "__pycache__" not in f.parts:
            inputs[str(f.relative_to(ROOT))] = sha(f)
    # Recheck original machine payloads, existing and added NEW lifecycle, and raw
    # sources independently of the newer implementation receipt.
    ordered = historical = added = retired = 0
    protected = {}
    for name in ["baseline.json", "additional-seed-baseline.json", "cupnh-seed-baseline.json"]:
        baseline = json.loads((AUDIT / name).read_text())
        for path, expected in baseline["protected_files_sha256"].items():
            assert sha(ROOT / path) == expected, path
            protected[path] = expected
        for path, prior in baseline.get("reviews", baseline.get("genes", {})).items():
            before = prior["document"]["existing_annotations"]
            review = yaml.safe_load((ROOT / path).read_text())
            assert review["status"] == "COMPLETE"
            after = review["existing_annotations"]
            assert [payload(r) for r in before] == [payload(r) for r in after[:len(before)]], path
            ordered += len(before)
            for index, (x, y) in enumerate(zip(before, after, strict=False)):
                if x["review"]["action"] == "NEW":
                    historical += 1
                    assert y["review"]["action"] == "NEW"
                if bool(y.get("retired")) != bool(x.get("retired")):
                    assert path == "genes/PSEPK/phaZ/phaZ-ai-review.yaml" and index == 2 and y["retired"]
                retired += bool(y.get("retired"))
            extra = after[len(before):]
            if extra:
                assert path == "genes/PSEAE/phaG/phaG-ai-review.yaml" and len(extra) == 1
                assert extra[0]["term"]["id"] == "GO:0016747"
                assert extra[0]["evidence_type"] == "IC" and extra[0]["review"]["action"] == "NEW"
                assert not extra[0].get("retired")
            added += len(extra)
    assert (ordered, historical, added, retired) == (23, 5, 1, 1)
    quotes = 0
    for entry in yaml.safe_load((AUDIT / "literature-consultation/reference-ledger.yaml").read_text()):
        path = ROOT / entry["source_path"]
        assert sha(path) == entry["source_sha256"]
        text = " ".join(path.read_text().split())
        for finding in entry["findings"]:
            assert " ".join(finding["supporting_text"].split()) in text, entry["id"]
            quotes += 1
    for pmid, quote in [("10612741", "These data strongly suggested that R. eutropha PHA synthase accepts"),
                        ("35341893", "without any synthase modification")]:
        assert quote in " ".join((ROOT / f"publications/PMID_{pmid}.md").read_text().split())
        quotes += 1
    closure = {"inputs": dict(sorted(inputs.items())), "superseded": superseded,
               "old_closure_sha256": sha(OLD / "input-closure.json")}
    snapshot = HERE / "input-closure.json"
    if args.capture:
        assert not snapshot.exists(), "Never overwrite captured closure"
        snapshot.write_text(json.dumps(closure, indent=2, sort_keys=True) + "\n")
    else:
        assert json.loads(snapshot.read_text()) == closure, "Frozen input closure changed"
    result = {"status": "PASS", "old_input_count": len(old["files"]), "new_input_count": len(inputs),
              "superseded_files": len(superseded), "all_original_inputs_retained": True,
              "original_ordered_rows": ordered, "historical_new": historical,
              "added_new": added, "retired_historical_new": retired,
              "protected_sources": len(protected), "original_quotes_rechecked": quotes,
              "module_unchanged": True, "closure_sha256": sha(snapshot)}
    (HERE / "closure-results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
