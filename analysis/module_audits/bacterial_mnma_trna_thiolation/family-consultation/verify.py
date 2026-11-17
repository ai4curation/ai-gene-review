"""Strict, read-only source/assertion preservation and quote verification."""

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
FAMILIES = [
    "PTHR" + x
    for x in ["11601", "11933", "33279", "34874", "37010", "37526", "38780", "43586"]
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return re.sub(r"\s+", " ", text)


def walk_quotes(value):
    if isinstance(value, dict):
        if "reference_id" in value and "supporting_text" in value:
            yield value
        for child in value.values():
            yield from walk_quotes(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_quotes(child)


def load_source(ref):
    if ref.startswith("PMID:"):
        path = ROOT / "publications" / ("PMID_" + ref.split(":")[1] + ".md")
    else:
        assert ref.startswith("file:"), ref
        path = ROOT / ref[5:]
        if not path.exists():
            path = ROOT / "genes" / ref[5:]
    assert path.exists(), path
    return path, path.read_text()


base = json.loads((A / "baseline.json").read_text())
raw_count = 0
for path, sha in base["files"].items():
    if not path.endswith("-review.yaml"):
        assert digest(ROOT / path) == sha, path
        raw_count += 1
old = yaml.safe_load(next(iter(base["original_reviews"].values())))
current = yaml.safe_load(
    (ROOT / "interpro/panther/PTHR11601/PTHR11601-review.yaml").read_text()
)
assert current["node_assessments"] == old["node_assessments"]
assert current["subfamilies"] == old["subfamilies"]
assert current["term_assessments"][0] == old["term_assessments"][0]
assert current["references"][: len(old["references"])] == old["references"]
assert (
    current["term_assessments"][1]["assessed_term"]
    == old["term_assessments"][1]["assessed_term"]
)
assert current["term_assessments"][1]["scope"] == "UNRESOLVED"
assert (
    current["term_assessments"][1]["supported_by"][
        : len(old["term_assessments"][1]["supported_by"])
    ]
    == old["term_assessments"][1]["supported_by"]
)
imported_nodes = 0
for family in ["PTHR34874", "PTHR37010", "PTHR37526", "PTHR38780"]:
    original = yaml.safe_load(
        (A.parent / "preflight" / f"PR5078-{family}-review.yaml").read_text()
    )
    current = yaml.safe_load(
        (ROOT / f"interpro/panther/{family}/{family}-review.yaml").read_text()
    )
    assert len(current["node_assessments"]) == len(original["node_assessments"])
    for before, after in zip(
        original["node_assessments"], current["node_assessments"], strict=True
    ):
        for key in [
            "node_id",
            "asserted_term",
            "node_taxon",
            "seeds",
            "paint_snapshot",
            "assessment",
        ]:
            assert before.get(key) == after.get(key), (family, key)
        assert (
            after["supported_by"][: len(before["supported_by"])]
            == before["supported_by"]
        )
        imported_nodes += 1
    for before, after in zip(
        original["term_assessments"], current["term_assessments"], strict=True
    ):
        for key in [
            "assessed_term",
            "scope",
            "applicable_subfamilies",
            "member_exceptions",
        ]:
            assert before.get(key) == after.get(key), (family, key)
    for before, after in zip(
        original["subfamilies"], current["subfamilies"], strict=True
    ):
        assert (
            before["representative_members"]
            == after["representative_members"][: len(before["representative_members"])]
        )
quotes = []
sources = {}
assertions = 0
for family in FAMILIES:
    path = ROOT / f"interpro/panther/{family}/{family}-review.yaml"
    review = yaml.safe_load(path.read_text())
    paint = path.with_name(family + "-paint.tsv")
    rows = list(csv.DictReader(paint.open(), delimiter="\t")) if paint.exists() else []
    for node in review.get("node_assessments", []):
        row = next(
            r
            for r in rows
            if r["node"] == node["node_id"].split(":")[1]
            and r["go_id"] == node["asserted_term"]["id"]
        )
        assert node["evidence"] == row["evidence"]
        assert node.get("negated", False) == (row["negated"] == "true")
        assert node["paint_snapshot"] == row["date"]
        assert [s["id"] for s in node["seeds"]] == row["seeds"].split("|")
        if row["taxon"] != "taxon:":
            assert node["node_taxon"]["id"] == row["taxon"].replace(
                "taxon:", "NCBITaxon:"
            )
        assertions += 1
    assert len(rows) == len(review.get("node_assessments", [])), family
    for quote in walk_quotes(review):
        source, text = load_source(quote["reference_id"])
        assert normalized(quote["supporting_text"]) in normalized(text), (family, quote)
        sources[str(source.relative_to(ROOT))] = digest(source)
        quotes.append(
            {
                "family": family,
                "reference": quote["reference_id"],
                "quote_sha256": hashlib.sha256(
                    quote["supporting_text"].encode()
                ).hexdigest(),
            }
        )
    for ref in review["references"]:
        if ref["id"].startswith("PMID:"):
            _, text = load_source(ref["id"])
            assert ref["title"] == yaml.safe_load(text.split("---", 2)[1])["title"], ref
history_paths = json.loads((A / "new-history-paths.json").read_text())
assert len(history_paths) == 8 and len(set(history_paths)) == 8
old_histories = subprocess.check_output(
    [
        "git",
        "ls-tree",
        "-r",
        "--name-only",
        "HEAD",
        *[f"history/other/{f}" for f in FAMILIES],
    ],
    cwd=ROOT,
    text=True,
).splitlines()
for path in old_histories:
    original = subprocess.check_output(["git", "show", "HEAD:" + path], cwd=ROOT)
    assert (ROOT / path).read_bytes() == original
inputs = json.loads((A / "input-closure.json").read_text())
for path, expected in inputs["files"].items():
    assert digest(ROOT / path) == expected, path
if (A / "handoff.json").exists():
    handoff = json.loads((A / "handoff.json").read_text())
    for path, sha in handoff["files"].items():
        assert digest(ROOT / path) == sha, path
print(
    json.dumps(
        {
            "status": "PASS",
            "original_raw_files_preserved": raw_count,
            "unchanged_current_Isc_nodes": len(old["node_assessments"]),
            "imported_PR5078_node_payloads_preserved": imported_nodes,
            "total_exact_PAINT_assertions": assertions,
            "supporting_quote_occurrences_checked": len(quotes),
            "new_history_count": len(history_paths),
            "old_histories_unchanged": len(old_histories),
            "quoted_source_hashes": sources,
            "frozen_handoff_verified": (A / "handoff.json").exists(),
        },
        indent=2,
    )
)
