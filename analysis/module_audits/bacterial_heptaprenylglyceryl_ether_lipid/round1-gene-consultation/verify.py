"""Check exact source payloads/actions and the bounded PR6167 review changes."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[3]
BASE = json.loads((AUDIT / "baseline.json").read_text())
ledger = []
rows = 0
historical_new = 0
active_new = 0
for name, before in BASE["reviews"].items():
    after = yaml.safe_load((ROOT / name).read_text())
    assert len(before["existing_annotations"]) == len(after["existing_annotations"])
    for index, (old, new) in enumerate(
        zip(before["existing_annotations"], after["existing_annotations"], strict=True)
    ):
        assert {k: v for k, v in old.items() if k != "review"} == {
            k: v for k, v in new.items() if k != "review"
        }, (name, index, "source payload changed")
        assert old["review"]["action"] == new["review"]["action"], (name, index)
        old_review = copy.deepcopy(old["review"])
        new_review = copy.deepcopy(new["review"])
        for field in ("reason", "supported_by", "source_defects"):
            old_review.pop(field, None)
            new_review.pop(field, None)
        assert old_review == new_review, (name, index, "non-evidence review change")
        if "source_defects" in old["review"]:
            a = copy.deepcopy(old["review"]["source_defects"])
            b = copy.deepcopy(new["review"]["source_defects"])
            for defect in a + b:
                defect.pop("supported_by", None)
            assert a == b
        rows += 1
        historical_new += old["review"]["action"] == "NEW"
        active_new += new["review"]["action"] == "NEW" and not new.get("retired", False)
        ledger.append(
            {
                "path": name,
                "index": index,
                "term": old["term"]["id"],
                "evidence": old["evidence_type"],
                "before_action": old["review"]["action"],
                "after_action": new["review"]["action"],
                "review_changed": old["review"] != new["review"],
            }
        )
    b = copy.deepcopy(before)
    a = copy.deepcopy(after)
    b.pop("existing_annotations")
    a.pop("existing_annotations")
    if "FLAJ1" in name:
        for obj in (a, b):
            obj["core_functions"][0].pop("supported_by")
            obj["knowledge_gaps"][0].pop("boundary")
        assert (ROOT / name).read_text().count("The I90A mutant clearly accepted") == 3
        for row in after["existing_annotations"]:
            if row["term"]["id"] not in {"GO:0047294"}:
                assert "I90A mutant clearly" not in json.dumps(row["review"])
    else:
        assert a["references"][:-1] == b["references"]
        assert a["references"][-1]["id"] == "file:" + str(
            (AUDIT / "comparator-adjudication.md").relative_to(ROOT)
        )
        a["references"].pop()
        for obj in (a, b):
            obj["core_functions"][0].pop("description")
    assert a == b, (name, "unexpected top-level or functional assertion change")
for name, digest in BASE["protected"].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name


def verify_evidence_lists(obj):
    """Duplicated support within a block must not inflate a single observation."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "supported_by":
                fingerprints = [json.dumps(item, sort_keys=True) for item in value]
                assert len(fingerprints) == len(set(fingerprints))
            verify_evidence_lists(value)
    elif isinstance(obj, list):
        for value in obj:
            verify_evidence_lists(value)


flaj = yaml.safe_load(
    (ROOT / "genes/FLAJ1/Fjoh_1584/Fjoh_1584-ai-review.yaml").read_text()
)
verify_evidence_lists(flaj)
for left, right in (
    ("ether-parents.json", "GO:0046474"),
    ("glycerophospholipid-parents.json", "GO:0008611"),
):
    assert (
        right not in json.loads((AUDIT / left).read_text())["results"][0]["ancestors"]
    )
assert json.loads((AUDIT / "bacteria-exact.json").read_text())["numberOfHits"] == 17
receipt = {
    "baseline_head": BASE["head"],
    "original_ordered_payloads_preserved": rows,
    "original_actions_preserved": rows,
    "historical_new": historical_new,
    "active_new": active_new,
    "added_or_retired_rows": 0,
    "protected_source_files": len(BASE["protected"]),
    "flaj_mutation_quote_occurrences_before": 24,
    "flaj_mutation_quote_occurrences_after": 3,
    "functional_term_assertions_unchanged": True,
    "scope": "Two owned gene reviews only; exact non-review payload and source checks.",
}
(AUDIT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
(AUDIT / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
