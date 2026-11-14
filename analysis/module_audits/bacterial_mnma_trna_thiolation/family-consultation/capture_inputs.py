"""Capture immutable source inputs once, before release; never edit a frozen handoff."""

import csv
import hashlib
import json
import re
from pathlib import Path

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
assert not (A / "handoff.json").exists(), "Already frozen"
PANELS = {
    "ECOLI": {
        "iscS": ("P0A6B7", "11601:SF34"),
        "mnmA": ("P25745", "11933:SF5"),
        "tusA": ("P0A890", "33279:SF2"),
        "tusB": ("P45530", "37526:SF1"),
        "tusC": ("P45531", "38780:SF1"),
        "tusD": ("P45532", "34874:SF3"),
        "tusE": ("P0AB18", "37010:SF1"),
    },
    "PSEPK": {
        "iscS": ("Q88PK8", "11601:SF34"),
        "mnmA": ("Q88FR9", "11933:SF5"),
        "tusA": ("Q88L21", "33279:SF2"),
        "PP_3995": ("Q88FT7", "37526:SF1"),
        "PP_3994": ("Q88FT8", "38780:SF1"),
        "tusD": ("Q88FT9", "34874:SF3"),
        "tusE": ("Q88FT6", "37010:SF1"),
    },
    "BACSU": {"iscS1": ("O34599", "11601:SF34"), "mnmA": ("O35020", "11933:SF5")},
    "THET2": {
        "mnmA": ("Q72GX1", "11933:SF5"),
        "TT_C0087": ("Q72LH2", "11601:SF34"),
        "TT_C1373": ("Q72HV9", "43586:SF8"),
    },
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


index_path = next((ROOT / ".cache/panther").glob("panther-members-*.tsv"))
index = {
    r["uniprot_accession"]: r for r in csv.DictReader(index_path.open(), delimiter="\t")
}
files = {}
records = []
for organism, genes in PANELS.items():
    for gene, (accession, suffix) in genes.items():
        path = ROOT / f"genes/{organism}/{gene}/{gene}-uniprot.txt"
        text = path.read_text()
        assert re.search(r"^AC\s+" + accession + r";", text, re.M), path
        classification = "PTHR" + suffix
        official_lines = [
            line for line in text.splitlines() if line.startswith("DR   PANTHER;")
        ]
        assert any(classification in line for line in official_lines), (
            path,
            classification,
        )
        row = index.get(accession)
        if row is not None:
            assert classification in row.values(), (accession, row)
        records.append(
            {
                "organism": organism,
                "gene": gene,
                "accession": accession,
                "classification": classification,
                "official_record": str(path.relative_to(ROOT)),
                "official_panther_lines": official_lines,
                "member_index_row": row,
            }
        )
        for source in path.parent.glob("*"):
            if source.name.endswith(("-uniprot.txt", "-goa.tsv")):
                files[str(source.relative_to(ROOT))] = sha(source)
base = json.loads((A / "baseline.json").read_text())
for path, expected in base["files"].items():
    if not path.endswith("-review.yaml"):
        assert sha(ROOT / path) == expected
        files[path] = expected
preservation = json.loads(
    (
        ROOT
        / ".cache/module-audit-logs/mnma-20261107/family-consultation/preservation.json"
    ).read_text()
)
files.update(preservation["quoted_source_hashes"])
for path in (A.parent / "preflight").rglob("*"):
    if path.is_file():
        files[str(path.relative_to(ROOT))] = sha(path)
(A / "classification.json").write_text(
    json.dumps(
        {
            "status": "PASS",
            "members": records,
            "index_note": "Derived index rows validate classification only; they do not establish exact chemistry, cognate partners, or native flux. Official flatfiles and archived official trees are the cited sources.",
            "member_index_sha256_at_check": sha(index_path),
        },
        indent=2,
    )
    + "\n"
)
(A / "input-closure.json").write_text(
    json.dumps(
        {
            "status": "PASS",
            "files": dict(sorted(files.items())),
            "excluded": "Concurrent gene reviews, module, project and globally regenerated member index are not frozen by this family consultation.",
        },
        indent=2,
    )
    + "\n"
)
print(
    json.dumps({"status": "PASS", "members": len(records), "input_files": len(files)})
)
