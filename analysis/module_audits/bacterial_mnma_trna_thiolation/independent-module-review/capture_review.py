"""Read-only input audit; writes only this consultation's new receipt artifacts."""

import hashlib
import json
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
BASE = A.parent
assert not (A / "handoff.json").exists(), "Frozen review must not be overwritten"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


module_path = ROOT / "modules/bacterial_mnma_trna_thiolation.yaml"
module_bytes = module_path.read_bytes()
module = yaml.safe_load(module_bytes)
inputs = {str(module_path.relative_to(ROOT)): digest(module_path)}
releases = {}
for relative in [
    "new-member-consultation/handoff.json",
    "existing-review-consultation/handoff.yaml",
    "family-consultation/handoff.json",
]:
    path = BASE / relative
    release = yaml.safe_load(path.read_text())
    for name, expected in release["files"].items():
        assert digest(ROOT / name) == expected, name
    releases[str(path.relative_to(ROOT))] = {
        "sha256": digest(path),
        "verified_files": len(release["files"]),
    }
    inputs[str(path.relative_to(ROOT))] = digest(path)
members = json.loads((BASE / "family-consultation/classification.json").read_text())[
    "members"
]
module_accessions = {
    obj["id"].split(":")[1]
    for obj in walk(module["module"])
    if str(obj.get("id", "")).startswith("UniProtKB:")
}
assert module_accessions == {m["accession"] for m in members}
rows = []
for member in members:
    organism, gene = member["organism"], member["gene"]
    folder = ROOT / "genes" / organism / gene
    review_path = folder / f"{gene}-ai-review.yaml"
    review = yaml.safe_load(review_path.read_text())
    assert review["id"] == member["accession"] and review["status"] == "COMPLETE"
    for suffix in ["ai-review.yaml", "uniprot.txt", "notes.md"]:
        path = folder / f"{gene}-{suffix}"
        if path.exists():
            inputs[str(path.relative_to(ROOT))] = digest(path)
    rows.append(
        {
            "accession": member["accession"],
            "organism": organism,
            "gene": gene,
            "description": review["description"],
            "core_functions": review["core_functions"],
            "review_sha256": digest(review_path),
            "assessment": "Consistent with assigned catalytic, carrier or structural module role; assay and inference limits assessed in findings.md.",
        }
    )
for path in sorted((ROOT / "interpro/panther").glob("PTHR*/PTHR*-review.yaml")):
    if path.parent.name in {
        "PTHR" + x
        for x in [
            "11601",
            "11933",
            "33279",
            "34874",
            "37010",
            "37526",
            "38780",
            "43586",
        ]
    }:
        inputs[str(path.relative_to(ROOT))] = digest(path)
for obj in walk(module):
    ref = obj.get("source_id", "")
    if ref.startswith("PMID:"):
        path = ROOT / "publications" / ("PMID_" + ref.split(":")[1] + ".md")
    elif ref.startswith("file:"):
        path = ROOT / ref[5:]
    else:
        continue
    assert path.exists(), path
    inputs[str(path.relative_to(ROOT))] = digest(path)
for relative in [
    "new-member-consultation/evidence.md",
    "existing-review-consultation/evidence.md",
    "family-consultation/README.md",
    "family-consultation/tree-scope.json",
    "family-consultation/classification.json",
]:
    path = BASE / relative
    inputs[str(path.relative_to(ROOT))] = digest(path)
assert module_path.read_bytes() == module_bytes
(A / "member-review.json").write_text(json.dumps(rows, indent=2) + "\n")
(A / "reviewed-inputs.json").write_text(
    json.dumps(
        {
            "reviewed_module_sha256": hashlib.sha256(module_bytes).hexdigest(),
            "module_status": module["status"],
            "files": dict(sorted(inputs.items())),
            "released_input_manifests": releases,
            "all19_members_consistent": True,
        },
        indent=2,
    )
    + "\n"
)
print(
    json.dumps(
        {
            "reviewed_module_sha256": hashlib.sha256(module_bytes).hexdigest(),
            "members": len(rows),
            "hashed_inputs": len(inputs),
            "verified_releases": releases,
        },
        indent=2,
    )
)
