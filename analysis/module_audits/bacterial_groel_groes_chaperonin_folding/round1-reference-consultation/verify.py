"""Verify the narrow PR 6164 PSEPK reference follow-up against its frozen HEAD."""

import copy
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
BASELINE = json.loads((AUDIT / "baseline.json").read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    results = {}
    for name, before in BASELINE["reviews"].items():
        path = ROOT / name
        head = yaml.safe_load(
            subprocess.check_output(
                ["git", "show", f"{BASELINE['head']}:{name}"], cwd=ROOT, text=True
            )
        )
        assert before == head, f"Baseline differs from frozen HEAD: {name}"
        after = yaml.safe_load(path.read_text())
        assert after["existing_annotations"] == before["existing_annotations"], name
        gene = after["gene_symbol"]
        wrong, right = (
            ("38987603", "39169181") if gene == "groEL" else ("38092042", "38064510")
        )
        added = after["references"][0]
        assert added["id"] == f"PMID:{wrong}"
        assert added["reference_review"]["correctness"] == "WRONG_IDENTIFIER"
        assert (
            added["reference_review"]["replacement"]["reference_id"] == f"PMID:{right}"
        )
        assert added["reference_review"]["replacement"]["reason"] == "WRONG_IDENTIFIER"
        assert not added.get("is_invalid")
        assert added["findings"] == []
        assert after["references"][1:] == before["references"]
        expected = copy.deepcopy(before)
        expected["references"] = after["references"]
        if gene == "groEL":
            expected["description"] = after["description"]
            expected["core_functions"][0]["description"] = after["core_functions"][0][
                "description"
            ]
        else:
            expected["core_functions"][0]["in_complex"] = {
                "id": "GO:1990220",
                "label": "GroEL-GroES complex",
            }
        assert after == expected, f"Unapproved curated change: {name}"
        rows = before["existing_annotations"]
        results[gene] = {
            "ordered_rows_unchanged": len(rows),
            "actions_unchanged": True,
            "historical_NEW": sum(r["review"]["action"] == "NEW" for r in rows),
            "active_NEW": sum(
                r["review"]["action"] == "NEW" and not r.get("retired") for r in rows
            ),
            "sha256": digest(path),
        }
    for name, sha in BASELINE["sources"].items():
        assert digest(ROOT / name) == sha, f"Protected source modified: {name}"
    return {
        "status": "PASS",
        "baseline_head": BASELINE["head"],
        "genes": results,
        "protected_source_count": len(BASELINE["sources"]),
        "protected_source_sha256": BASELINE["sources"],
        "allowed_deltas": [
            "groEL description and core description",
            "one wrong-identifier reference per gene",
            "groES core in_complex GO:1990220",
        ],
    }


if __name__ == "__main__":
    result = verify()
    (AUDIT / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
