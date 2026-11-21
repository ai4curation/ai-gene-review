"""Unit tests for ai_gene_review.classifier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from ai_gene_review.classifier import (
    ANNOTATION_ACTION_CHOICES,
    COARSE_ACTION_CHOICES,
    EVIDENCE_CLAIM_CHOICES,
    TypeSafeClassifier,
    annotation_action_aspect_paths,
    annotation_action_aspects_task,
    annotation_action_coarse_task,
    annotation_action_task,
    claim_aspect_paths,
    coarse_action,
    derive_annotation_review_target,
    extract_annotation_case,
    extract_claim,
    render_prompt,
    response_schema,
    structured_evidence_claim_aspects_task,
    structured_evidence_claim_match_task,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
CFAP300_PATH = REPO_ROOT / "genes" / "human" / "CFAP300" / "CFAP300-ai-review.yaml"


@pytest.fixture(scope="module")
def cfap300_doc() -> dict[str, Any]:
    return yaml.safe_load(CFAP300_PATH.read_text(encoding="utf-8"))


def test_extract_claim_from_core_functions(cfap300_doc: dict[str, Any]) -> None:
    claim = extract_claim(cfap300_doc, "/core_functions/0/supported_by/0")
    assert claim["about"]["gene"]["gene_symbol"] == "CFAP300"
    assert claim["about"]["gene"]["id"] == "Q9BRQ4"
    assert claim["origin"] == {
        "assertion_path": "/core_functions/0",
        "evidence_path": "/core_functions/0/supported_by/0",
        "section": "core_functions",
    }
    assert "supported_by" not in claim["assertion"]
    assert claim["assertion"]["directly_involved_in"][0]["id"] == "GO:0036158"
    assert claim["selected_evidence"]["reference_id"] == "PMID:29727693"
    assert (
        claim["selected_evidence"]["supporting_text"]
        == "C11orf70 is involved in cytoplasmic assembly of dynein arms"
    )
    assert (
        claim["selected_evidence"]["snippet"]
        == "C11orf70 is involved in cytoplasmic assembly of dynein arms"
    )
    paths = claim_aspect_paths(claim)
    assert "/" in paths
    assert "/about/gene" in paths
    assert "/assertion/directly_involved_in" in paths
    assert "/assertion/locations" in paths


def test_extract_claim_from_existing_annotations(cfap300_doc: dict[str, Any]) -> None:
    claim = extract_claim(cfap300_doc, "/existing_annotations/0/review/supported_by/0")
    assert claim["origin"]["assertion_path"] == "/existing_annotations/0"
    assert claim["assertion"]["term"] == {"id": "GO:0005737", "label": "cytoplasm"}
    assert claim["assertion"]["review"]["action"] == "ACCEPT"
    assert "supported_by" not in claim["assertion"].get("review", {})
    assert "reason" not in claim["assertion"].get("review", {})
    assert claim["selected_evidence"]["reference_id"] == "PMID:36246608"


def test_extract_claim_from_reference_findings(cfap300_doc: dict[str, Any]) -> None:
    claim = extract_claim(cfap300_doc, "/references/2/findings/0")
    assert claim["origin"]["section"] == "references"
    assert claim["selected_evidence"]["reference_id"] == "PMID:29727692"
    assert claim["selected_evidence"]["supporting_text"] == "combined loss"
    assert "Human CFAP300 variants" in claim["assertion"]["statement"]


def test_extract_annotation_case_strips_all_curator_leakage(
    cfap300_doc: dict[str, Any],
) -> None:
    case = extract_annotation_case(cfap300_doc, "/existing_annotations/0")
    assert case["about"]["gene"]["gene_symbol"] == "CFAP300"
    assert case["target_annotation"]["term"] == {
        "id": "GO:0005737",
        "label": "cytoplasm",
    }
    assert case["target_annotation"]["evidence_type"] == "IEA"
    assert "review" not in case["target_annotation"]
    assert "core_functions" not in case
    assert "description" not in case
    # Primary supporting excerpts are preserved without leaking internal agent files
    assert case["supporting_excerpts"] == [
        {
            "reference_id": "PMID:36246608",
            "supporting_text": "CFAP300 localized in the cytoplasm",
        },
    ]
    # Sibling annotations must exclude action=NEW rows and GO:0005515, strip review blocks, and collapse duplicate terms
    assert case["sibling_raw_count"] == 3
    assert len(case["sibling_annotations"]) == 3
    for sib in case["sibling_annotations"]:
        assert "review" not in sib
        assert "count" in sib
        assert "evidence_types" in sib
        assert sib["term"]["id"] not in ("GO:0005515", "GO:0036158", "GO:0036159")
    for ref in case.get("references_metadata", []):
        assert "findings" not in ref
        assert "reference_review" not in ref

    target = derive_annotation_review_target(cfap300_doc, "/existing_annotations/0")
    assert target["action"] == "ACCEPT"
    assert target["coarse_action"] == "KEEP"
    assert target["is_core"] == "CORE"

    # Generic GO:0005515 protein binding is rejected as a benchmark target by default
    with pytest.raises(ValueError, match="GO:0005515"):
        extract_annotation_case(cfap300_doc, "/existing_annotations/2")


def test_extract_annotation_case_rejects_new_rows(
    cfap300_doc: dict[str, Any],
) -> None:
    with pytest.raises(ValueError, match="action='NEW'"):
        extract_annotation_case(cfap300_doc, "/existing_annotations/5")


def test_tasks_and_typesafe_classifier_roundtrip(cfap300_doc: dict[str, Any]) -> None:
    claim = extract_claim(cfap300_doc, "/core_functions/0/supported_by/0")
    match_task = structured_evidence_claim_match_task(
        claim,
        source_text="# Title\nC11orf70 is involved in cytoplasmic assembly of dynein arms.",
    )
    assert [c.value for c in match_task.choices] == [
        c.value for c in EVIDENCE_CLAIM_CHOICES
    ]
    prompt = render_prompt(match_task)
    assert "CFAP300" in prompt
    assert response_schema(match_task)["properties"]["label"]["enum"] == [
        "MATCH",
        "PARTIAL",
        "MISMATCH",
    ]

    aspects_task = structured_evidence_claim_aspects_task(claim)
    assert aspects_task.output_schema is not None
    assert "/" in aspects_task.output_schema["properties"]
    assert "/assertion/directly_involved_in" in aspects_task.output_schema["properties"]

    ann_case = extract_annotation_case(cfap300_doc, "/existing_annotations/0")
    act_task = annotation_action_task(
        ann_case,
        reference_texts={"PMID:36246608": "CFAP300 localized in the cytoplasm."},
    )
    assert [c.value for c in act_task.choices] == [
        c.value for c in ANNOTATION_ACTION_CHOICES
    ]
    coarse_task = annotation_action_coarse_task(ann_case)
    assert [c.value for c in coarse_task.choices] == [
        c.value for c in COARSE_ACTION_CHOICES
    ]
    ann_aspects = annotation_action_aspects_task(ann_case)
    assert ann_aspects.output_schema is not None
    assert set(ann_aspects.output_schema["properties"]) == {
        "/",
        "/coarse_action",
        "/is_core",
        "/propagation_root_cause",
    }
    assert annotation_action_aspect_paths(ann_case) == [
        "/",
        "/coarse_action",
        "/is_core",
        "/propagation_root_cause",
    ]
    assert coarse_action("MARK_AS_OVER_ANNOTATED") == "REJECT"
    assert coarse_action("TOO_GENERAL") == "REFINE"

    # Mock HTTP response for TypeSafeClassifier
    class DummyResponse:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict[str, Any]:
            return {
                "model": "jev-1.13.0",
                "output": json.dumps({"label": "ACCEPT"}),
                "usage": {"input_tokens": 120, "output_tokens": 5},
                "logprobs": [
                    {
                        "token": "ACCEPT",
                        "logprob": -0.05,
                        "top_logprobs": [
                            {"token": "ACCEPT", "logprob": -0.05},
                            {"token": "KEEP_AS_NON_CORE", "logprob": -3.1},
                        ],
                    }
                ],
            }

    clf = TypeSafeClassifier(api_key="test-key", post=lambda *a, **kw: DummyResponse())
    res = clf.classify(act_task)
    assert res.label == "ACCEPT"
    assert res.confidence is not None and res.confidence > 0.9
    assert res.usage["input_tokens"] == 120
