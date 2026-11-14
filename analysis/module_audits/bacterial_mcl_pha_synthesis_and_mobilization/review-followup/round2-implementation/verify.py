"""Read-only exact preservation and bounded-source checks for PR6194 round two."""

import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    return " ".join(text.split())


def load(path):
    return yaml.safe_load(path.read_text())


def clean_sections(value):
    if isinstance(value, dict):
        return {k: clean_sections(v) for k, v in value.items() if k != "record_section"}
    if isinstance(value, list):
        return [clean_sections(v) for v in value]
    return value


def verify():
    baseline = json.loads((HERE / "baseline.json").read_text())
    old = {p: row["document"] for p, row in baseline["documents"].items()}
    new = {p: load(ROOT / p) for p in old}
    rows = historical = retired = 0
    for path in old:
        if not path.startswith("genes/"):
            continue
        a, b = old[path], new[path]
        assert len(a["existing_annotations"]) == len(b["existing_annotations"])
        for i, (before, after) in enumerate(
            zip(a["existing_annotations"], b["existing_annotations"])
        ):
            assert {k: v for k, v in before.items() if k != "review"} == {
                k: v for k, v in after.items() if k != "review"
            }, (path, i)
            expected = (
                "MODIFY"
                if path == "genes/ECTOL/phaZ/phaZ-ai-review.yaml" and i == 1
                else before["review"]["action"]
            )
            assert after["review"]["action"] == expected, (path, i)
            rows += 1
            if before["review"]["action"] == "NEW":
                assert before == after or path == "genes/PSEAE/phaG/phaG-ai-review.yaml"
                historical += 1
                retired += bool(before.get("retired"))
        assert clean_sections(a.get("core_functions")) == clean_sections(
            b.get("core_functions")
        ), path
    # Compare whole documents after permitting only exact scoped fields.
    for path in old:
        a, b = copy.deepcopy(old[path]), copy.deepcopy(new[path])
        if path == "genes/ECTOL/phaZ/phaZ-ai-review.yaml":
            r = b["existing_annotations"][1]["review"]
            assert r["proposed_replacement_terms"] == [
                {
                    "id": "GO:0042620",
                    "label": "poly(3-hydroxyalkanoate) metabolic process",
                }
            ]
            for field in ("action", "reason", "proposed_replacement_terms"):
                a["existing_annotations"][1]["review"].pop(field, None)
                b["existing_annotations"][1]["review"].pop(field, None)
            a["proposed_new_terms"][0].pop("proposed_definition")
            b["proposed_new_terms"][0].pop("proposed_definition")
        elif path == "genes/PSEPK/phaZ/phaZ-ai-review.yaml":
            a["proposed_new_terms"][0].pop("justification")
            b["proposed_new_terms"][0].pop("justification")
        elif path == "genes/PSEAE/phaG/phaG-ai-review.yaml":
            assert b["existing_annotations"][2]["review"]["reason"].startswith(
                a["existing_annotations"][2]["review"]["reason"]
            )
            a["existing_annotations"][2]["review"].pop("reason")
            b["existing_annotations"][2]["review"].pop("reason")
        elif path.startswith("genes/ECTOL/phaC"):
            assert clean_sections(a) == clean_sections(b)
            assert "CC:FUNCTION" in str(b)
            a, b = clean_sections(a), clean_sections(b)
        elif path.endswith("PTHR43194-review.yaml"):
            for index, term in (
                (0, "GO:0016787"),
                (3, "GO:0090499"),
                (4, "GO:0009102"),
            ):
                assert a["node_assessments"][index]["asserted_term"]["id"] == term
                a["node_assessments"][index].pop("assessment_reason")
                b["node_assessments"][index].pop("assessment_reason")
            assert (
                b["node_assessments"][4]["supported_by"][:-2]
                == a["node_assessments"][4]["supported_by"]
            )
            b["node_assessments"][4]["supported_by"] = b["node_assessments"][4][
                "supported_by"
            ][:-2]
            assert [r["id"] for r in b["references"][-2:]] == [
                "PMID:40434073",
                "PMID:20693992",
            ]
            b["references"] = b["references"][:-2]
        elif path.endswith("PTHR43798-review.yaml"):
            assert b["node_assessments"][2]["assessment"] == "UNRESOLVED"
            assert a["node_assessments"][2]["node_id"] == "PANTHER:PTN000863140"
            a["node_assessments"][2]["assessment"] = "UNRESOLVED"
            a["node_assessments"][2].pop("assessment_reason")
            b["node_assessments"][2].pop("assessment_reason")
        elif path.startswith("modules/"):
            gaps = a["module"]["knowledge_gaps"]
            assert gaps[4]["gap_kind"] == ["ONTOLOGY"]
            assert "GO0050527" in gaps[4]["gap_statement"]
            gaps.pop(4)
        assert a == b, path
    assert (
        new["genes/ECTOL/phaZ/phaZ-ai-review.yaml"]["proposed_new_terms"][0][
            "proposed_definition"
        ]
        == new["genes/PSEPK/phaZ/phaZ-ai-review.yaml"]["proposed_new_terms"][0][
            "proposed_definition"
        ]
    )
    for section in ("protected_sources", "prior_audit_artifacts"):
        for path, expected in baseline[section].items():
            assert sha(ROOT / path) == expected, path
    for path, before in baseline["notes"].items():
        assert (ROOT / path).read_text().startswith(before["text"].rstrip() + "\n\n"), (
            path
        )
    # Fresh bounded quotes and metadata: no source refresh or online dependency.
    family = new["interpro/panther/PTHR43194/PTHR43194-review.yaml"]
    for support in family["node_assessments"][4]["supported_by"][-2:]:
        pmid = support["reference_id"].split(":")[1]
        source = (ROOT / "publications" / f"PMID_{pmid}.md").read_text()
        assert normalized(support["supporting_text"]) in normalized(source), pmid
        title = next(
            r["title"]
            for r in family["references"]
            if r["id"] == support["reference_id"]
        )
        assert normalized(title) in normalized(source), pmid
    # Raw PAINT assertions and curated seed/date fields are covered by exact
    # full-node comparisons above after only the named reason/verdict deltas.
    h = json.loads((HERE / "histories.json").read_text())
    assert len(h) == len(old) == 8
    for path in h:
        record = load(ROOT / path)
        assert record["session"]["actors"][0]["name"] == "codex"
        assert record["target"]["path"] in old
    for path in old:
        assert (ROOT / path).read_bytes() != baseline["documents"][path][
            "text"
        ].encode()
    return {
        "status": "PASS",
        "changed_curated_files": len(old),
        "appended_notes": len(baseline["notes"]),
        "generated_histories": len(h),
        "ordered_annotation_payloads_preserved": rows,
        "historical_NEW_preserved": historical,
        "historical_retired_preserved": retired,
        "new_rows": 0,
        "protected_sources_unchanged": len(baseline["protected_sources"]),
        "prior_audit_artifacts_unchanged": len(baseline["prior_audit_artifacts"]),
        "new_quotes_verified": 2,
        "action_changes": [
            {
                "gene": "ECTOL/phaZ",
                "index": 1,
                "term": "GO:0046464",
                "before": "MARK_AS_OVER_ANNOTATED",
                "after": "MODIFY",
                "replacement": "GO:0042620",
            }
        ],
        "limitations": [
            "No render/full-corpus/ontology-network run in this disk-constrained phase.",
            "AcoC ledger remains unenforced by production family crosscheck.",
            "17170116 full-text results rely on preserved scoped excerpts and prior acquisition provenance, not a newly downloaded full text.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
