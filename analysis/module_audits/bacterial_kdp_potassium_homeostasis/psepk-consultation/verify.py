"""Reproduce scoped PSEPK payload, source, action and core-preservation checks."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = json.loads((AUDIT / "baseline.json").read_text())
ROOT_BASE = json.loads((AUDIT.parent / "baseline.json").read_text())
EXPECTED = {
    ("kdpB", 1): ("KEEP_AS_NON_CORE", "ACCEPT"),
    ("kdpC", 0): ("MARK_AS_OVER_ANNOTATED", "UNDECIDED"),
    ("kdpC", 3): ("MARK_AS_OVER_ANNOTATED", "ACCEPT"),
    ("kdpE", 8): ("KEEP_AS_NON_CORE", "ACCEPT"),
    ("kdpF", 1): ("MARK_AS_OVER_ANNOTATED", "ACCEPT"),
    ("kdpF", 2): ("KEEP_AS_NON_CORE", "ACCEPT"),
}
ledger = []
changes = {}
row_count = 0
historical_new = 0
active_new = 0
for name, old in BASE["reviews"].items():
    assert old == ROOT_BASE["reviews"][name]["document"]
    new = yaml.safe_load((ROOT / name).read_text())
    gene = old["gene_symbol"]
    for field in ("id", "gene_symbol", "taxon", "product_type", "status"):
        assert old[field] == new[field]
    assert len(old["existing_annotations"]) == len(new["existing_annotations"])
    for i, (a, b) in enumerate(
        zip(old["existing_annotations"], new["existing_annotations"], strict=True)
    ):
        payload_a = {k: v for k, v in a.items() if k != "review"}
        payload_b = {k: v for k, v in b.items() if k != "review"}
        assert payload_a == payload_b, (gene, i, "payload changed")
        act_a = a["review"]["action"]
        act_b = b["review"]["action"]
        if act_a != act_b:
            changes[(gene, i)] = (act_a, act_b)
        historical_new += act_a == "NEW"
        active_new += act_b == "NEW" and not b.get("retired", False)
        row_count += 1
        assert a["review"].get("proposed_replacement_terms") == b["review"].get(
            "proposed_replacement_terms"
        )
        ledger.append(
            {
                "gene": gene,
                "index": i,
                "term": a["term"],
                "evidence": a["evidence_type"],
                "original_reference_id": a["original_reference_id"],
                "before": act_a,
                "after": act_b,
                "reason": b["review"]["reason"],
            }
        )
    # All original source identities and titles remain in the same order.
    assert [(r["id"], r["title"]) for r in old["references"]] == [
        (r["id"], r["title"]) for r in new["references"][: len(old["references"])]
    ]
    a = copy.deepcopy(old["core_functions"])
    b = copy.deepcopy(new["core_functions"])
    for core in a + b:
        core.pop("description", None)
        core.pop("supported_by", None)
    if gene == "kdpF":
        assert b[0].pop("contributes_to_molecular_function") == {
            "id": "GO:0008556",
            "label": "P-type potassium transmembrane transporter activity",
        }
        assert b[0].pop("directly_involved_in") == [
            {
                "id": "GO:0071805",
                "label": "potassium ion transmembrane transport",
            }
        ]
    assert a == b, (gene, "unexpected core assertion change")
assert changes == EXPECTED
for name, digest in BASE["protected"].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
for name, data in json.loads(
    (AUDIT / "additional-source-receipt.json").read_text()
).items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == data["sha256"], (
        name
    )
# Claimed target residues are checked directly from immutable UniProt sequences.
for gene, claim in json.loads((AUDIT / "sequence-checks.json").read_text()).items():
    raw = (ROOT / f"genes/PSEPK/{gene}/{gene}-uniprot.txt").read_text()
    sequence = "".join(raw.split("SQ   ", 1)[1].split("\n", 1)[1].split())
    sequence = sequence.replace("//", "")
    assert len(sequence) == claim["length"]
    if gene == "kdpA":
        assert sequence[233:238] == "TNGGG"
    if gene == "kdpB":
        assert sequence[310:315] == "DKTGT"
    if gene == "kdpE":
        assert sequence[54] == "D"
receipt = {
    "original_ordered_payloads": row_count,
    "payloads_identical_to_root_baseline": True,
    "review_action_changes": len(changes),
    "historical_new": historical_new,
    "active_new": active_new,
    "new_or_retired_rows": 0,
    "protected_original_source_files": len(BASE["protected"]),
    "additional_source_receipts": 5,
    "original_reference_identity_order_preserved": True,
    "core_delta": "KdpF adds contribution8556 and process71805 already present as original rows; other term assertions unchanged.",
}
(AUDIT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
(AUDIT / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
