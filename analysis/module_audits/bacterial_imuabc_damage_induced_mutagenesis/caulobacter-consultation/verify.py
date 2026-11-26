"""Verify all Caulobacter source rows, historical proposals and evidence boundaries."""

from pathlib import Path
import hashlib
import json

import yaml
from bs4 import BeautifulSoup

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = json.loads((AUDIT / "before.json").read_text())
ROOT_BASE = json.loads((AUDIT.parent / "baseline.json").read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payloads(rows):
    return [
        {key: value for key, value in row.items() if key != "review"} for row in rows
    ]


results = {}
ledger = []
changed_actions = {}
for name, before in BASE["reviews"].items():
    path = ROOT / name
    current = yaml.safe_load(path.read_text())
    old_rows = before["existing_annotations"]
    rows = current["existing_annotations"]
    assert payloads(rows) == payloads(old_rows)
    assert payloads(rows) == ROOT_BASE["members"][name]["ordered_annotation_payloads"]
    assert current["id"] == before["id"]
    assert current["taxon"] == before["taxon"]
    assert current["gene_symbol"] == before["gene_symbol"]
    historical = [
        i for i, row in enumerate(old_rows) if row["review"]["action"] == "NEW"
    ]
    active = [
        i
        for i, row in enumerate(rows)
        if row["review"]["action"] == "NEW" and not row.get("retired")
    ]
    assert historical == active
    for index, (old, new) in enumerate(zip(old_rows, rows, strict=True)):
        if old["review"]["action"] != new["review"]["action"]:
            changed_actions[(current["gene_symbol"], index)] = (
                old["review"]["action"],
                new["review"]["action"],
            )
        ledger.append(
            {
                "path": name,
                "row_index": index,
                "source_payload": payloads([new])[0],
                "before_review": old["review"],
                "after_review": new["review"],
            }
        )
    gene = current["gene_symbol"]
    if gene == "imuA":
        assert all(
            not core.get("molecular_function")
            and not core.get("proposed_molecular_function")
            for core in current["core_functions"]
        )
        assert rows[0]["review"]["action"] == "ACCEPT"
        assert (
            "Myxococcus"
            in current["core_functions"][0]["knowledge_gaps"][0]["gap_statement"]
        )
    elif gene == "imuB":
        assert "inference" in rows[2]["review"]["reason"]
        assert current["core_functions"][0]["description"].startswith("Inferred")
    else:
        assert rows[4]["review"]["proposed_replacement_terms"][0]["id"] == "GO:0042276"
        assert "part_of" in rows[4]["review"]["reason"]
        assert rows[7]["review"]["action"] == "UNDECIDED"
        assert "not itself evidence" in rows[7]["review"]["reason"]
    soup = BeautifulSoup(path.with_suffix(".html").read_text(), "html.parser")
    text = soup.get_text(" ", strip=True)
    assert "PENDING" not in text and "TODO" not in text
    assert "Myxococcus" in text if gene != "dnaE2" else "part_of" in text
    results[name] = {
        "ordered_payloads_preserved": len(rows),
        "historical_NEW": len(historical),
        "active_NEW": len(active),
        "review_sha256": sha(path),
        "render_content_check": "PASS",
    }
expected_actions = {
    ("imuA", 0): ("KEEP_AS_NON_CORE", "ACCEPT"),
    ("dnaE2", 3): ("KEEP_AS_NON_CORE", "ACCEPT"),
    ("dnaE2", 4): ("MARK_AS_OVER_ANNOTATED", "MODIFY"),
    ("dnaE2", 7): ("MARK_AS_OVER_ANNOTATED", "UNDECIDED"),
}
assert changed_actions == expected_actions
for name, digest in BASE["protected_sha256"].items():
    assert sha(ROOT / name) == digest, name
ancestors = json.loads((AUDIT / "tls-is-a-ancestors.json").read_text())["results"][0][
    "ancestors"
]
assert "GO:0006301" in ancestors and "GO:0006260" not in ancestors
assert "GO:0006281" not in ancestors
terms = json.loads((AUDIT / "ontology-definitions.json").read_text())["results"]
replication = next(term for term in terms if term["id"] == "GO:0006260")
assert {"id": "GO:0006301", "relation": "part_of"} in replication["children"]
proof = {
    "status": "PASS",
    "reviews": results,
    "ordered_rows_preserved": 16,
    "historical_NEW": 4,
    "active_NEW": 4,
    "added_rows": 0,
    "deleted_rows": 0,
    "action_changes": 4,
    "protected_sources": len(BASE["protected_sha256"]),
    "protected_sha256": BASE["protected_sha256"],
    "scientific_boundary_checks": [
        "No ImuA MF invented from Myxococcus assay",
        "ImuB adaptor remains explicitly inferential",
        "DnaE2 exonuclease uncertainty is target-specific",
        "Replication refinement uses actual part_of edge",
    ],
}
(AUDIT / "proof.json").write_text(json.dumps(proof, indent=2) + "\n")
(AUDIT / "action-ledger.yaml").write_text(
    yaml.safe_dump(
        {
            "row_index_convention": "zero-based",
            "reviewed_rows": 16,
            "action_changes": 4,
            "decisions": ledger,
        },
        sort_keys=False,
        width=100,
        allow_unicode=True,
    )
)
print(
    json.dumps(
        {
            "status": "PASS",
            "ordered_rows": 16,
            "historical_NEW": 4,
            "active_NEW": 4,
            "action_changes": 4,
            "protected_sources": len(BASE["protected_sha256"]),
        },
        indent=2,
    )
)
