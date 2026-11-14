"""Verify the frozen read-only Mla preflight against its pinned Git snapshot."""

from pathlib import Path
import difflib
import hashlib
import json
import subprocess

P = Path(__file__).resolve().parent
ROOT = P.parents[2]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(name):
    return json.loads((P / name).read_text())


def git_bytes(path):
    return subprocess.check_output(
        ["git", "show", f"{snapshot['main_sha']}:{path}"], cwd=ROOT
    )


snapshot = read("main-snapshot.json")
assert len(snapshot["reviews"]) == 12
assert sum(x["rows"] for x in snapshot["reviews"].values()) == 105
assert len(snapshot["families"]) == 6
assert sha((P / "module.yaml").read_bytes()) == snapshot["module_sha256"]
assert git_bytes(snapshot["module"]) == (P / "module.yaml").read_bytes()
for path, record in snapshot["reviews"].items():
    data = (P / path.replace("/", "__")).read_bytes()
    assert sha(data) == record["sha256"] and data == git_bytes(path)
for path, record in snapshot["families"].items():
    data = (P / Path(path).name).read_bytes()
    assert sha(data) == record["sha256"] and data == git_bytes(path)
publication_copies = {}
for file in P.glob("main-PMID_*.md"):
    source = "publications/" + file.name.removeprefix("main-")
    assert file.read_bytes() == git_bytes(source)
    publication_copies[file.name] = {"source": source, "sha256": sha(file.read_bytes())}
for entry in read("source-ledger.json"):
    file = P / entry["source_file"]
    assert sha(file.read_bytes()) == entry["source_sha256"]
    assert entry["supporting_text"] in file.read_text()
overlap = read("expanded-overlap.json")
assert overlap["open_pr_count"] == 280
assert [x["number"] for x in overlap["hits"]] == [5076]
patch = read("pr5076-mla-file.json")[0]["patch"]
changes = [line for line in patch.splitlines() if line[:1] in {"+", "-"}]
assert len(changes) == 19
assert sum("preferred_term:" in line for line in changes) == 13
extra = [line[1:].strip() for line in changes if "preferred_term:" not in line]
assert extra == [
    "term:",
    "id: UniProtKB:P64602",
    "label: Intermembrane phospholipid transport system binding protein MlaB",
    "term:",
    "id: PANTHER:PTHR35849:SF1",
    "label: INTERMEMBRANE PHOSPHOLIPID TRANSPORT SYSTEM BINDING PROTEIN MLAB",
]
identities = read("identity-proof.json")
expected = ["Q7VT00", "Q7VSZ9", "Q7VSZ8", "Q7VSZ7", "Q7VSZ6"]
assert [x["accession"] for x in identities["BORPE_reference_panel"]] == expected
for entry in identities["BORPE_reference_panel"]:
    raw = read("uniprot-" + entry["locus"][2:] + ".json")["results"][0]
    assert raw["primaryAccession"] == entry["accession"]
    assert raw["organism"]["taxonId"] == 257313
    assert entry["locus"] in json.dumps(raw["genes"])
assert read("uniprot-B213.json")["results"] == []
ref = read("uniprot-PA4453.json")["results"][0]["sequence"]["value"]
construct = read("6HSY-entity1.json")["entity_poly"]["pdbx_seq_one_letter_code_can"]
match = difflib.SequenceMatcher(
    None, ref, construct, autojunk=False
).find_longest_match()
assert match.size == 193
assert ref[match.a : match.a + match.size] == construct[match.b : match.b + match.size]
pdf = (P / "36518166-supp-els.pdf").read_bytes()
assert pdf.startswith(b"%PDF")
assert pdf == (P / "36518166-supp-extracted.pdf").read_bytes()
assert "SmR derivative of Tohama I" in (P / "36518166-supp-els.txt").read_text()
paths = subprocess.check_output(
    ["git", "ls-tree", "-r", "--name-only", snapshot["main_sha"], "genes"],
    cwd=ROOT,
    text=True,
)
missing = [f"genes/BORPE/BP{x}/BP{x}-ai-review.yaml" for x in range(3757, 3762)]
missing += ["genes/PSEAE/ttg2D/ttg2D-ai-review.yaml"]
assert all(path not in paths.splitlines() for path in missing)
result = {
    "result": "PASS",
    "main_sha": snapshot["main_sha"],
    "original_reviews": 12,
    "original_rows": 105,
    "original_family_reviews": 6,
    "source_quotes": len(read("source-ledger.json")),
    "open_prs": 280,
    "overlapping_pr": 5076,
    "patch_changes": "six preferred_term substitutions plus ECOLI MlaB representative and PTHR35849:SF1 grounding",
    "new_review_paths_absent": missing,
    "publication_copy_receipt": publication_copies,
    "sequence_match": 193,
    "limitations": "B213 lineage/locus bridge is not experimental whole-protein sequence equality. Folder/PR scope is frozen at acquisition time.",
}
(P / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {
            "result": "PASS",
            "quotes": result["source_quotes"],
            "reviews": 12,
            "rows": 105,
            "open_prs": 280,
        }
    )
)
