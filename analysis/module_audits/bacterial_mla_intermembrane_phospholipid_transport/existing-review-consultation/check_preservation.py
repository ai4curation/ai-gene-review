"""Verify original Mla rows, lifecycle, source bytes, notes and structural mapping."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
AUDIT = HERE.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_payload(row: dict) -> dict:
    return {key: value for key, value in row.items() if key != "review"}


def lifecycle(row: dict) -> dict:
    return {
        "action": row.get("review", {}).get("action"),
        "retired": row.get("retired", False),
        "review_retired": row.get("review", {}).get("retired", False),
    }


def check() -> dict:
    before = yaml.safe_load((HERE / "before.yaml").read_text())
    baseline = yaml.safe_load((AUDIT / "baseline.yaml").read_text())
    notes = yaml.safe_load((HERE / "notes-baseline.yaml").read_text())
    histories = yaml.safe_load((HERE / "histories.yaml").read_text())
    sources = dict(before["protected_sha256"])
    for name, value in baseline["source_files_sha256"].items():
        if not name.endswith("-review.yaml") and not name.startswith("modules/"):
            assert sources.get(name, value) == value, name
            sources[name] = value
    for name, value in sources.items():
        assert digest(ROOT / name) == value, f"Protected source changed: {name}"
    counts = Counter()
    ledger = []
    reviews = {}
    for name, old in before["reviews"].items():
        current = yaml.safe_load((ROOT / name).read_text())
        original_rows = old["existing_annotations"]
        rows = current["existing_annotations"]
        assert len(rows) == len(original_rows), f"Row count changed: {name}"
        assert [source_payload(row) for row in rows] == baseline[
            "existing_annotation_rows"
        ][name], f"Ordered baseline payload mismatch: {name}"
        assert [source_payload(row) for row in rows] == [
            source_payload(row) for row in original_rows
        ], f"Ordered pre-edit payload mismatch: {name}"
        assert current["status"] == "COMPLETE", name
        for index, (previous, row) in enumerate(zip(original_rows, rows, strict=True)):
            if previous["review"]["action"] == "NEW":
                assert lifecycle(row) == lifecycle(previous), (name, index)
                counts["historical_new"] += 1
                counts["active_historical_new"] += not row.get("retired", False)
            else:
                counts["machine_rows"] += 1
            counts["rows"] += 1
            counts["action_changes"] += (
                previous["review"]["action"] != row["review"]["action"]
            )
            ledger.append(
                {
                    "review": name,
                    "index": index,
                    "term": row["term"]["id"],
                    "original_action": previous["review"]["action"],
                    "current_action": row["review"]["action"],
                    "claim_adjudication": row["review"]["reason"],
                }
            )
        reviews[name] = digest(ROOT / name)
        assert (ROOT / histories[name]).is_file(), histories[name]
    for name, data in notes["notes"].items():
        assert (ROOT / name).read_text().startswith(data["original_text"]), name
    for item in yaml.safe_load((HERE / "api-provenance.yaml").read_text()):
        assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
    entity = json.loads((HERE / "5UWB.json").read_text())
    uniprot = (ROOT / "genes/PSEPK/ttg2D/ttg2D-uniprot.txt").read_text()
    sequence = "".join(uniprot.split("SQ   ")[1].splitlines()[1:]).replace(" ", "")
    sequence = sequence.replace("//", "")
    assert len(sequence) == 215
    assert (
        entity["entity_poly"]["pdbx_seq_one_letter_code_can"] == sequence + "LEHHHHHH"
    )
    assert entity["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"] == "160488"
    assert counts["rows"] == 105 and counts["historical_new"] == 16
    assert counts["machine_rows"] == 89
    return {
        "status": "PASS",
        "baseline_sha256": digest(AUDIT / "baseline.yaml"),
        "pre_edit_capture_sha256": digest(HERE / "before.yaml"),
        "counts": dict(counts),
        "added_rows": 0,
        "protected_sources": sources,
        "protected_source_count": len(sources),
        "review_sha256": reviews,
        "historical_notes_append_only": len(notes["notes"]),
        "ttg2d_sequence_bridge": "215/215 canonical residues plus LEHHHHHH; MSE normalized",
        "row_review_ledger": ledger,
        "limitations": [
            "PAINT leaves unavailable for the six PSEPK targets in the frozen gene source/tree combination; no loss-free inference made.",
            "Experimental source inaccessible in full remains explicitly bounded; no curator claim is rejected from abstract silence.",
            "No native KT2440 net lipid flux, porin compatibility, or measured target ATP-coupling kinetics inferred from E. coli reconstitution.",
            "No full-corpus validation performed; root-owned module/family/project content is outside this preservation receipt.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()
    result = check()
    if args.write_results:
        (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {key: result[key] for key in ["status", "counts", "protected_source_count"]}
        )
    )


if __name__ == "__main__":
    main()
