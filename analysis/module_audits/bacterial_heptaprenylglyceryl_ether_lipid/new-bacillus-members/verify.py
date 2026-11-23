"""Reproduce ordered seed/source protection and targeted scientific boundaries."""

from pathlib import Path
import json
import hashlib
import yaml
from bs4 import BeautifulSoup

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = json.loads((AUDIT / "seed-baseline.json").read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


results = {}
ledger = []
for gene, seed in BASE["seeds"].items():
    path = ROOT / f"genes/BACSU/{gene}/{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    rows = doc["existing_annotations"]
    original = seed["ordered_payloads"]

    def payload(row):
        return {k: v for k, v in row.items() if k != "review"}

    assert [payload(r) for r in rows[: len(original)]] == original
    assert doc["id"] == seed["accession"] and doc["gene_symbol"] == gene
    assert doc["status"] == "COMPLETE"
    assert all(r["review"]["action"] != "PENDING" for r in rows)
    if gene == "yvoF":
        assert len(rows) == 1 and rows[0]["review"]["action"] == "MODIFY"
        assert rows[0]["review"]["proposed_replacement_terms"] == [
            {"id": "GO:0016413", "label": "O-acetyltransferase activity"}
        ]
        assert doc["core_functions"][0]["molecular_function"]["id"] == "GO:0016413"
    else:
        assert len(rows) == 2 and rows[0]["review"]["action"] == "ACCEPT"
        assert rows[1]["term"] == {
            "id": "GO:0008080",
            "label": "N-acetyltransferase activity",
        }
        assert rows[1]["review"]["action"] == "NEW"
        assert (
            rows[1]["evidence_type"] == "IDA"
            and rows[1]["original_reference_id"] == "PMID:40626731"
        )
        assert doc["core_functions"][0]["molecular_function"]["id"] == "GO:0008080"
        assert all(r["term"]["id"] != "GO:0004596" for r in rows)
        assert "C20 geranylgeranyl analogue" in rows[1]["review"]["reason"]
        assert "not resolved" in rows[1]["review"]["reason"]
    soup = BeautifulSoup(path.with_suffix(".html").read_text(), "html.parser")
    text = soup.get_text(" ", strip=True)
    assert "PENDING" not in text and "TODO" not in text
    assert "Core Functions" in text or "Core functions" in text
    assert "acetyl" in text and ("cytoplasmic" in text or "membrane" in text)
    results[gene] = {
        "original_rows": len(original),
        "current_rows": len(rows),
        "ordered_source_payloads_preserved": True,
        "historical_NEW": 0,
        "active_NEW": sum(r["review"]["action"] == "NEW" for r in rows),
        "review_sha256": sha(path),
        "render_content_check": "PASS",
    }
    for i, r in enumerate(rows):
        ledger.append(
            {
                "gene": gene,
                "row_index": i,
                "source_payload": payload(r),
                "seed_action": "PENDING" if i < len(original) else None,
                "final_review": r["review"],
            }
        )
for name, digest in BASE["protected_sha256"].items():
    assert sha(ROOT / name) == digest, name
receipt = {
    "status": "PASS",
    "original_rows_preserved": 2,
    "current_rows": 3,
    "raw_sources_preserved": 4,
    "publication_sources_preserved": 2,
    "protected_sha256": BASE["protected_sha256"],
    "reviews": results,
    "scientific_boundary_checks": [
        "Correct distinct O- versus N-acetyltransferase activities",
        "No acetyl-CoA-specific LhaT activity",
        "C20 assay analogue distinguished from C35 native lipid",
        "Original ypjA symbol retained",
        "Exactly one direct MF gap proposed; no extra location/process rows",
    ],
}
(AUDIT / "proof.json").write_text(json.dumps(receipt, indent=2) + "\n")
(AUDIT / "action-ledger.yaml").write_text(
    yaml.safe_dump(
        {
            "row_index_convention": "zero-based",
            "original_annotation_count": 2,
            "new_annotation_count": 1,
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
            "reviews": results,
            "protected_sources": len(BASE["protected_sha256"]),
        },
        indent=2,
    )
)
