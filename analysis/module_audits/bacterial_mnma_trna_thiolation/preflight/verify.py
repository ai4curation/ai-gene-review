"""Read-only verification; emits JSON to stdout, never rewrites frozen artifacts."""

import hashlib
import json
import re
import subprocess
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text):
    return re.sub(r"\s+", " ", text)


base = json.loads((P / "final-baseline.json").read_text())
for path, expected in base["files"].items():
    raw = subprocess.check_output(
        ["git", "show", base["main_sha"] + ":" + path], cwd=ROOT
    )
    assert hashlib.sha256(raw).hexdigest() == expected, path
quotes = []
for item in json.loads((P / "source-ledger.json").read_text()):
    source = P / item["source"]
    assert source.exists()
    if "quote" in item:
        text = source.read_text()
        if source.suffix == ".json":
            obj = json.loads(text)
            if isinstance(obj, str):
                text = obj
        assert normalize(item["quote"]) in normalize(text), item["id"]
        assert len(item["quote"].split()) <= 25
        quotes.append(item["id"])
identities = json.loads((P / "candidate-identities.json").read_text())
expected = {
    "P0A890",
    "P45530",
    "P45531",
    "P45532",
    "P0AB18",
    "P25745",
    "O34599",
    "O35020",
    "Q72GX1",
    "Q72LH2",
    "Q72HV9",
}
assert expected <= {i["accession"] for i in identities}
for item in identities:
    assert sha(P / item["source"]) == item["source_sha256"]
    records = json.loads((P / item["source"]).read_text())["results"]
    raw = next(x for x in records if x["primaryAccession"] == item["accession"])
    assert raw["organism"] == item["taxon"]
    assert (
        hashlib.sha256(raw["sequence"]["value"].encode()).hexdigest()
        == item["sequence_sha256"]
    )
    assert [
        x for x in raw["uniProtKBCrossReferences"] if x["database"] == "PANTHER"
    ] == item["panther"]
prs = json.loads((P / "final-open-pr-files.json").read_text())
assert len(prs) == len({x["number"] for x in prs}) == 282
hits = json.loads((P / "final-overlap.json").read_text())["hits"]
for pr in hits:
    metadata = json.loads((P / f"PR{pr['number']}-metadata.json").read_text())
    assert metadata["state"] == "open"
    assert metadata["head"]["sha"] == pr["headRefOid"]
    current = next(x for x in prs if x["number"] == pr["number"])
    assert len(current["files"]) == metadata["changed_files"]
    for path in pr["overlap"]:
        assert path in current["files"]
        assert (P / f"PR{pr['number']}-{Path(path).name}").exists()
if (P / "handoff.json").exists():
    frozen = json.loads((P / "handoff.json").read_text())
    for path, expected_hash in frozen["files"].items():
        assert sha(P / path) == expected_hash, path
print(
    json.dumps(
        {
            "status": "PASS",
            "pinned_main": base["main_sha"],
            "protected_main_files": len(base["files"]),
            "verified_short_quotes": len(quotes),
            "official_identity_records": len(identities),
            "new_review_candidates": len(expected),
            "open_pr_file_lists": len(prs),
            "overlap_PRs": [x["number"] for x in hits],
            "frozen_handoff_checked": (P / "handoff.json").exists(),
        },
        indent=2,
    )
)
