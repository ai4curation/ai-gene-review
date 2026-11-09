"""Verify scoped Isc curation preserves every original annotation and source."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
LOCAL = json.loads((OUT / "baseline.json").read_text())
SEED = json.loads((OUT.parent / "baseline.json").read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    results = {}
    ledger = []
    for name, before in LOCAL["reviews"].items():
        after = yaml.safe_load((ROOT / name).read_text())
        expected_rows = SEED["members"][name]["ordered_annotation_payloads"]
        assert len(after["existing_annotations"]) == len(expected_rows)
        for i, (original, row, frozen) in enumerate(
            zip(
                before["existing_annotations"],
                after["existing_annotations"],
                expected_rows,
                strict=True,
            )
        ):
            payload = {k: v for k, v in row.items() if k != "review"}
            old_payload = {k: v for k, v in original.items() if k != "review"}
            assert old_payload == frozen, f"Independent baseline mismatch: {name}:{i}"
            if name == "genes/PSEPK/hscA/hscA-ai-review.yaml" and i == 4:
                assert frozen == {
                    "term": {
                        "id": "GO:0140662",
                        "label": "ATP-dependent protein folding chaperone",
                    },
                    "evidence_type": "ISS",
                    "original_reference_id": "file:PSEPK/hscA/hscA-uniprot.txt",
                    "qualifier": "enables",
                }
                assert payload.pop("retired") is True
                assert row["review"]["action"] == "NEW"
            assert payload == frozen, f"Source payload/order changed: {name}:{i}"
            assert row["review"]["action"] != "PENDING"
            if (original["review"]["action"], original.get("retired", False)) != (
                row["review"]["action"],
                row.get("retired", False),
            ):
                ledger.append(
                    {
                        "gene": after["gene_symbol"],
                        "index": i,
                        "term": row["term"]["id"],
                        "from": original["review"]["action"],
                        "to": row["review"]["action"],
                        "retired_before": original.get("retired", False),
                        "retired_after": row.get("retired", False),
                    }
                )
        original_new = [
            i
            for i, row in enumerate(before["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        current_new = [
            i
            for i, row in enumerate(after["existing_annotations"])
            if row["review"]["action"] == "NEW"
        ]
        assert (
            current_new
            == original_new
            == SEED["members"][name]["historical_new_indices"]
        )
        results[name] = {
            "rows": len(expected_rows),
            "historical_NEW": len(current_new),
            "active_NEW": sum(
                not after["existing_annotations"][i].get("retired") for i in current_new
            ),
            "sha256": sha(ROOT / name),
        }
    protected = dict(LOCAL["sources"])
    protected.update(
        {
            k: v
            for k, v in SEED["sources_sha256"].items()
            if k.startswith("genes/PSEPK/")
        }
    )
    for name, expected in protected.items():
        assert sha(ROOT / name) == expected, f"Protected source modified: {name}"
    hsc = yaml.safe_load((ROOT / "genes/PSEPK/hscA/hscA-ai-review.yaml").read_text())
    assert hsc["core_functions"][0]["molecular_function"]["id"] == "GO:0016887"
    receipt = {
        "status": "PASS",
        "rows": sum(v["rows"] for v in results.values()),
        "genes": results,
        "protected_sha256": protected,
        "only_payload_delta": "hscA original index4 GO0140662 retired:true",
        "historical_NEW": sum(v["historical_NEW"] for v in results.values()),
        "active_NEW": sum(v["active_NEW"] for v in results.values()),
    }
    (OUT / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        f"PASS: {receipt['rows']} rows; {len(protected)} protected sources; "
        f"{receipt['historical_NEW']} historical NEW, {receipt['active_NEW']} active NEW"
    )


if __name__ == "__main__":
    verify()
