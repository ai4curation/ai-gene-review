"""Check the frozen E. coli payloads and sources; emit a review/action receipt."""

from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [
        {key: value for key, value in row.items() if key != "review"}
        for row in document["existing_annotations"]
    ]


def assert_preserved(before, after):
    assert payloads(before) == payloads(after), "Ordered original payload changed"
    old_new = [
        i for i, row in enumerate(before["existing_annotations"])
        if row["review"]["action"] == "NEW"
    ]
    new_new = [
        i for i, row in enumerate(after["existing_annotations"])
        if row["review"]["action"] == "NEW"
    ]
    assert old_new == new_new, "Historical NEW presence/action changed"
    assert not any(r.get("retired") for r in after["existing_annotations"])


def main():
    baseline = yaml.safe_load((HERE / "baseline.yaml").read_text())
    receipt = {"status": "PASS", "reviews": {}, "action_changes": []}
    totals = Counter()
    originals = 0
    inherited_new = 0
    for rel, frozen in baseline["reviews"].items():
        before = frozen["document"]
        after = yaml.safe_load((ROOT / rel).read_text())
        assert_preserved(before, after)
        originals += len(payloads(before))
        actions = Counter(row["review"]["action"] for row in after["existing_annotations"])
        inherited_new += actions["NEW"]
        totals.update(actions)
        receipt["reviews"][rel] = {
            "sha256": digest(ROOT / rel),
            "ordered_payloads": len(payloads(before)),
            "actions": dict(actions),
        }
        for i, (old, new) in enumerate(zip(before["existing_annotations"], after["existing_annotations"], strict=True)):
            if old["review"]["action"] != new["review"]["action"]:
                receipt["action_changes"].append({
                    "review": rel, "row_index": i, "term": old["term"]["id"],
                    "reference": old["original_reference_id"],
                    "before": old["review"]["action"], "after": new["review"]["action"],
                    "reason": new["review"]["reason"],
                })
    for rel, expected in baseline["protected"].items():
        assert digest(ROOT / rel) == expected, f"Protected source changed: {rel}"
    new_sources = yaml.safe_load((HERE / "additional-source-hashes.yaml").read_text())
    for rel, expected in new_sources.items():
        assert digest(ROOT / rel) == expected, f"Additional source changed: {rel}"
    # In-memory fault injection demonstrates that preservation checks reject damage.
    before = next(iter(baseline["reviews"].values()))["document"]
    rejected = []
    for name in ["deleted_row", "reordered_rows", "altered_qualifier", "new_proposal"]:
        bad = deepcopy(before)
        rows = bad["existing_annotations"]
        if name == "deleted_row":
            rows.pop()
        elif name == "reordered_rows":
            rows[0], rows[1] = rows[1], rows[0]
        elif name == "altered_qualifier":
            rows[0]["qualifier"] = "corrupted_for_sensitivity_check"
        else:
            rows[0]["review"]["action"] = "NEW"
        try:
            assert_preserved(before, bad)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError(f"Preservation guard failed sensitivity: {name}")
    receipt.update({
        "original_ordered_rows": originals,
        "original_GO_or_inherited_rows": originals,
        "inherited_NEW_retained": inherited_new,
        "new_rows_added": 0,
        "retirements": 0,
        "action_totals": dict(totals),
        "protected_original_files": len(baseline["protected"]),
        "additional_sources_hashed": len(new_sources),
        "sensitivity_faults_rejected": rejected,
        "limitations": "Checks preservation and accounting, not biological truth; manual source adjudication is in evidence.yaml and gene reviews.",
    })
    (HERE / "preservation-results.yaml").write_text(yaml.safe_dump(receipt, sort_keys=False, width=100))
    print(f"PASS: {originals} ordered rows, {inherited_new} inherited NEW, {len(baseline['protected'])} protected sources; {len(rejected)} injected faults rejected")


if __name__ == "__main__":
    main()
