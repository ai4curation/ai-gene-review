"""Strict read-only verification of the authorized PR6190 evidence/prose deltas."""

import copy
import hashlib
import json
import re
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[4]
BASE = json.loads((A / "baseline.json").read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_identity(obj):
    if isinstance(obj, dict):
        if (
            obj.get("supporting_text")
            == "Sequence identity supports protein-role transfer in a matched biological context."
        ):
            obj["supporting_text"] = (
                "All three matches are exact and unique among 2,423 translated CDSs."
            )
        for child in obj.values():
            replace_identity(child)
    elif isinstance(obj, list):
        for child in obj:
            replace_identity(child)


def quotes(obj):
    if isinstance(obj, dict):
        if obj.get("supporting_text") and obj.get("reference_id"):
            yield obj
        for child in obj.values():
            yield from quotes(child)
    elif isinstance(obj, list):
        for child in obj:
            yield from quotes(child)


def normalize(text):
    return re.sub(r"\s+", " ", re.sub(r"(?m)^CC\s{3}", "", text))


for path, expected in BASE["protected"].items():
    assert sha(ROOT / path) == expected, path
rows = 0
historical_new = 0
for path, original in BASE["documents"].items():
    expected = copy.deepcopy(original)
    current = yaml.safe_load((ROOT / path).read_text())
    if path.startswith("genes/"):
        rows += len(original["existing_annotations"])
        historical_new += sum(
            a["review"]["action"] == "NEW" for a in original["existing_annotations"]
        )
        if path in [
            "genes/ECOLI/lptM/lptM-ai-review.yaml",
            "genes/ECOLI/yedD/yedD-ai-review.yaml",
            "genes/NEIMB/lptE/lptE-ai-review.yaml",
        ]:
            expected["description"] = current["description"]
        if path.startswith("genes/NEIMB/"):
            replace_identity(expected)
        if path == "genes/NEIMH/lptD/lptD-ai-review.yaml":
            expected["existing_annotations"][0]["review"]["supported_by"][1][
                "supporting_text"
            ] = "Imp itself is an OMP, as shown by its presence in purified Neisserial (this study) and E. coli ( 6 ) OMs"
        if path == "genes/ECOLI/lptE/lptE-ai-review.yaml":
            entry = next(
                s
                for s in expected["core_functions"][0]["supported_by"]
                if s["reference_id"] == "PMID:41285762"
            )
            entry["supporting_text"] = (
                "with an internal lumen partially occluded by the lipoprotein LptE"
            )
    elif "PTHR45772" in path:
        expected["term_assessments"][0]["scope_reason"] = current["term_assessments"][
            0
        ]["scope_reason"]
    else:
        expected["summary"] = current["summary"]
        if "PTHR30189" in path:
            title = yaml.safe_load(
                (ROOT / "publications/PMID_41285762.md").read_text().split("---", 2)[1]
            )["title"]
            expected["references"].append({"id": "PMID:41285762", "title": title})
    assert current == expected, path
for org, gene in BASE["genes"]:
    name = f"genes/{org}/{gene}/{gene}-notes.md"
    original = BASE["original_text"][name]
    if org == "PSEPK":
        original = original.replace(
            f".cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-{gene}.log",
            f"analysis/module_audits/bacterial_lps_transport/psepk-consultation/provider-attempts/falcon-{gene}.log",
        )
    current = (ROOT / name).read_text()
    assert current.startswith(
        original + "\n\n## PR6190 evidence/prose follow-up\n\n"
    ), name
# New or changed support snippets only: historical sources remain protected above.
source_hashes = {}
new_quotes = 0
for path, original in BASE["documents"].items():
    before = {(q["reference_id"], q["supporting_text"]) for q in quotes(original)}
    current = yaml.safe_load((ROOT / path).read_text())
    for q in quotes(current):
        if (q["reference_id"], q["supporting_text"]) in before and q[
            "supporting_text"
        ] != "All three matches are exact and unique among 2,423 translated CDSs.":
            continue
        ref = q["reference_id"]
        if ref.startswith("PMID:"):
            source = ROOT / ("publications/PMID_" + ref.split(":")[1] + ".md")
        else:
            assert ref.startswith("file:")
            source = ROOT / ref[5:]
            if not source.exists():
                source = ROOT / "genes" / ref[5:]
        assert normalize(q["supporting_text"]) in normalize(source.read_text()), (
            path,
            q,
        )
        source_hashes[str(source.relative_to(ROOT))] = sha(source)
        new_quotes += 1
histories = json.loads((A / "new-history-paths.json").read_text())
assert len(histories) == 16 and len(set(histories)) == 16
for path in histories:
    assert (ROOT / path).exists()
for path, expected in json.loads((A / "source-dependencies.json").read_text())[
    "files"
].items():
    assert sha(ROOT / path) == expected, path
if (A / "handoff.json").exists():
    for path, expected in json.loads((A / "handoff.json").read_text())["files"].items():
        assert sha(ROOT / path) == expected, path
print(
    json.dumps(
        {
            "status": "PASS",
            "protected_sources_and_old_histories": len(BASE["protected"]),
            "ordered_annotation_payloads_actions_lifecycle_preserved": rows,
            "historical_NEW_preserved": historical_new,
            "families_PAINT_and_scopes_unchanged": 3,
            "new_histories": len(histories),
            "targeted_quote_occurrences_verified": new_quotes,
            "changed_quote_source_hashes": source_hashes,
        },
        indent=2,
        sort_keys=True,
    )
)
