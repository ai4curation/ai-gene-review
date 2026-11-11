"""Check immutable family inputs, original PAINT payloads and all local quotes."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text):
    text = re.sub(r"(?m)^(?:CC|FT|DE)\s+", "", text)
    return " ".join(text.split())


def supports(value):
    if isinstance(value, dict):
        if "reference_id" in value and "supporting_text" in value:
            yield value
        for item in value.values():
            yield from supports(item)
    elif isinstance(value, list):
        for item in value:
            yield from supports(item)


def main():
    baseline = json.loads((HERE / "baseline.json").read_text())
    failures = []
    for path, digest in baseline["protected"].items():
        if sha(ROOT / path) != digest:
            failures.append(f"Protected source changed: {path}")
    tree_snapshot = json.loads((HERE / "tree-inspection.json").read_text())
    for family, snapshot in tree_snapshot.items():
        tree = ROOT / ".cache" / "panther_trees" / f"{family}.json.gz"
        if sha(tree) != snapshot["tree_cache_sha256"]:
            failures.append(f"Cached tree changed: {family}")
    assertion_count = 0
    quote_count = 0
    reviews = {}
    judgement_fields = {"assessment", "assessment_reason", "supported_by"}
    for path, old in baseline["reviews"].items():
        current = yaml.safe_load((ROOT / path).read_text())
        before = old["document"]["node_assessments"]
        after = current["node_assessments"]

        def payload(row):
            return {k: v for k, v in row.items() if k not in judgement_fields}

        if [payload(row) for row in before] != [payload(row) for row in after]:
            failures.append(f"Ordered ancestral assertion payload changed: {path}")
        assertion_count += len(before)
        for entry in supports(current):
            ref = entry["reference_id"]
            if ref.startswith("file:"):
                source = ROOT / ref.removeprefix("file:")
                if not source.exists():
                    source = ROOT / "genes" / ref.removeprefix("file:")
            elif ref.startswith("PMID:"):
                source = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            else:
                failures.append(f"Unvalidated reference {ref}")
                continue
            if normalize(entry["supporting_text"]) not in normalize(source.read_text()):
                failures.append(f"Quote mismatch: {path} / {ref}")
            quote_count += 1
        reviews[path] = sha(ROOT / path)
    result = {
        "status": "PASS" if not failures else "FAIL",
        "ordered_original_assertions": assertion_count,
        "protected_files": len(baseline["protected"]),
        "quotes_checked": quote_count,
        "tree_snapshots_unchanged": len(tree_snapshot),
        "review_sha256": reviews,
        "failures": failures,
    }
    (HERE / "preservation-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
