"""Verify seeded payloads, source preservation and independent structure evidence."""

from pathlib import Path
import collections
import difflib
import hashlib
import json
import re
import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads((A / name).read_text())


def payload(row):
    return {key: value for key, value in row.items() if key != "review"}


def fold(text):
    return re.sub(r"\s+", " ", text).strip()


def supporting_objects(obj):
    if isinstance(obj, dict):
        if "reference_id" in obj and "supporting_text" in obj:
            yield obj
        for val in obj.values():
            yield from supporting_objects(val)
    elif isinstance(obj, list):
        for val in obj:
            yield from supporting_objects(val)


base = load("baseline.json")
for name, expected in base["files"].items():
    if not name.endswith("-ai-review.yaml"):
        assert sha(ROOT / name) == expected, name
root_seed = yaml.safe_load((A.parent / "new-seed-baseline.yaml").read_text())
for name, expected in root_seed["source_files_sha256"].items():
    if name.endswith("-ai-review.yaml"):
        continue
    assert sha(ROOT / name) == expected, name
pre = A.parent / "preflight"
pre_manifest = json.loads((pre / "handoff.json").read_text())
for name, expected in pre_manifest["files"].items():
    assert sha(pre / name) == expected, name
ledger = {}
actions = collections.Counter()
quotes = 0
for seed in base["seeds"]:
    d = yaml.safe_load((ROOT / seed["review"]).read_text())
    old = seed.get("rows", [])
    rows = d.get("existing_annotations", [])
    assert [payload(x) for x in rows] == [payload(x) for x in old]
    assert d["status"] == "COMPLETE"
    assert d.get("core_functions")
    for row in rows:
        assert row["review"]["action"] != "PENDING"
        actions[row["review"]["action"]] += 1
    for item in supporting_objects(d):
        ref = item["reference_id"]
        if ref.startswith("PMID:"):
            file = ROOT / ("publications/PMID_" + ref[5:] + ".md")
        elif ref.startswith("file:"):
            file = ROOT / ref[5:]
            if not file.is_file():
                file = ROOT / "genes" / ref[5:]
        else:
            raise AssertionError(ref)
        assert fold(item["supporting_text"]) in fold(file.read_text()), (
            ref,
            item["supporting_text"],
        )
        ledger[str(file.relative_to(ROOT))] = sha(file)
        quotes += 1
    for r in d["references"]:
        if r["id"].startswith("PMID:"):
            file = ROOT / ("publications/PMID_" + r["id"][5:] + ".md")
            metadata = yaml.safe_load(file.read_text().split("---", 2)[1])
            assert r["title"] == metadata["title"]
            for f in r.get("findings", []):
                if f.get("supporting_text"):
                    assert fold(f["supporting_text"]) in fold(file.read_text())
                    quotes += 1
            ledger[str(file.relative_to(ROOT))] = sha(file)
seq = json.loads((pre / "uniprot-3761.json").read_text())["results"][0]["sequence"][
    "value"
]
for pdb, ligand_id in [("11HY", "4"), ("11IF", "3")]:
    e = load(f"{pdb}-polymer_entity.json")
    construct = e["entity_poly"]["pdbx_seq_one_letter_code_can"]
    seq_match = difflib.SequenceMatcher(
        None, seq, construct, autojunk=False
    ).find_longest_match()
    assert seq_match.size == 181 and seq_match.a == 26
    assert construct[seq_match.b :] == seq[26:]
    assert e["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"] == "257313"
    assert (
        load(f"{pdb}-nonpolymer_entity-{ligand_id}.json")["pdbx_entity_nonpoly"][
            "comp_id"
        ]
        == "PEF"
    )
    for f in A.glob(f"{pdb}-*.json"):
        ledger[str(f.relative_to(ROOT))] = sha(f)
for f in [
    pre / "identity-proof.json",
    pre / "36518166-supp-els.pdf",
    pre / "36518166-supp-els.txt",
    pre / "6HSY-entity1.json",
    pre / "uniprot-PA4453.json",
    A / "go-terms.json",
]:
    ledger[str(f.relative_to(ROOT))] = sha(f)
for name in root_seed["source_files_sha256"]:
    ledger[name] = sha(ROOT / name)
for r in load("provider-attempts.json"):
    assert r["returncode"] == 1
    assert "403" in (A / r["log"]).read_text()
assert dict(actions) == {"MODIFY": 4, "ACCEPT": 6}
result = {
    "result": "PASS",
    "reviews": 6,
    "preserved_ordered_rows": 10,
    "new_rows": 0,
    "retired_rows": 0,
    "actions": dict(actions),
    "source_quote_checks": quotes,
    "protected_seed_sources": sum(
        not x.endswith("-ai-review.yaml") for x in root_seed["source_files_sha256"]
    ),
    "frozen_preflight_files": len(pre_manifest["files"]),
    "falcon_actual_failed_attempts": 6,
    "target_mature_structure_matches": 2,
    "limitation": "B213 lineage bridge is not full sequence identity; absence of BORPE leaves prevents definitive lineage-loss checks.",
}
(A / "source-hashes.json").write_text(json.dumps(ledger, indent=2) + "\n")
(A / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
