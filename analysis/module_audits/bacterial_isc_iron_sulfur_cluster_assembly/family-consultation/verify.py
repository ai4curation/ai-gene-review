"""Preserve raw evidence and all judgments outside two bounded reconciliations."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = json.loads((OUT / "baseline.json").read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    receipts = {}
    for name, before in BASE["reviews"].items():
        after = yaml.safe_load((ROOT / name).read_text())
        expected = copy.deepcopy(before)
        family = before["family_id"]
        for key in [
            "summary",
            "coherence_reason",
            "notes",
            "review_date",
            "reviewed_by",
        ]:
            expected[key] = after[key]
        if family == "PANTHER:PTHR10093":
            expected["preferred_name"] = after["preferred_name"]
            allowed_nodes = {"GO:0008198", "GO:0006879"}
            for i, original in enumerate(before["node_assessments"]):
                if original["asserted_term"]["id"] in allowed_nodes:
                    changed = after["node_assessments"][i]
                    assert changed["assessment"] == "UNRESOLVED"
                    for field in ["assessment", "assessment_reason", "supported_by"]:
                        expected["node_assessments"][i][field] = changed[field]
                    assert (
                        changed["supported_by"][: len(original["supported_by"])]
                        == original["supported_by"]
                    )
            term_id = "GO:0140132"
            new_refs = [
                "20097860",
                "24321018",
                "29292548",
                "32131593",
                "36605734",
                "38452854",
            ]
        else:
            assert family == "PANTHER:PTHR19375"
            for i, original in enumerate(before["subfamilies"]):
                if original.get("subfamily_id") == "PANTHER:PTHR19375:SF176":
                    changed = after["subfamilies"][i]
                    for field in [
                        "description",
                        "divergence_description",
                        "supported_by",
                    ]:
                        expected["subfamilies"][i][field] = changed[field]
                    assert (
                        changed["supported_by"][: len(original["supported_by"])]
                        == original["supported_by"]
                    )
            term_id = "GO:0140662"
            new_refs = ["22782893", "9852006", "18986169"]
        for i, original in enumerate(before["term_assessments"]):
            if original["assessed_term"]["id"] == term_id:
                changed = after["term_assessments"][i]
                assert changed["scope"] == "UNRESOLVED"
                for field in ["scope", "scope_reason", "supported_by"]:
                    expected["term_assessments"][i][field] = changed[field]
                assert (
                    changed["supported_by"][: len(original["supported_by"])]
                    == original["supported_by"]
                )
                if family == "PANTHER:PTHR19375":
                    archive = json.loads(
                        (OUT / "hsp110-exception-baseline.json").read_text()
                    )
                    assert original["member_exceptions"] == archive["member_exceptions"]
                    assert len(archive["member_exceptions"]) == 1
                    exc = archive["member_exceptions"][0]
                    assert exc["member"]["id"] == "UniProtKB:Q92598"
                    assert "member_exceptions" not in changed
                    assert exc["exception_reason"] in after["notes"]
                    assert exc["supported_by"][0] in changed["supported_by"]
                    expected["term_assessments"][i].pop("member_exceptions")
                else:
                    assert changed.get("member_exceptions") == original.get(
                        "member_exceptions"
                    )
        additions = after["references"][len(before["references"]) :]
        assert [r["id"] for r in additions] == [f"PMID:{n}" for n in new_refs]
        expected["references"] += additions
        assert after == expected, f"Unexpected change: {name}"
        receipts[name] = {
            "sha256": sha(ROOT / name),
            "immutable_node_ids_terms_seeds_and_metadata": "unchanged",
            "unrelated_PAINT_localization_residue_and_member_judgments": "unchanged",
        }
    for name, digest in BASE["sources"].items():
        assert sha(ROOT / name) == digest, f"Protected source changed: {name}"
    result = {
        "status": "PASS",
        "families": receipts,
        "protected_sources_sha256": BASE["sources"],
        "allowed_verdict_deltas": {
            "PTHR10093 GO0140132": "FAMILY_WIDE -> UNRESOLVED",
            "PTHR10093 PTN000009661 GO0008198": "TOO_DEEP -> UNRESOLVED",
            "PTHR19375 GO0140662": "FAMILY_WIDE -> UNRESOLVED",
        },
        "new_member_exceptions_or_loss_claims": 0,
    }
    (OUT / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"PASS: 2 family reconciliations; {len(BASE['sources'])} protected sources unchanged"
    )


if __name__ == "__main__":
    verify()
