"""Unit tests for ai_gene_review.classifier."""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from ai_gene_review.classifier import (
    ANNOTATION_ACTION_CHOICES,
    ANNOTATION_ACTION_INSTRUCTION,
    COARSE_ACTION_CHOICES,
    DEFAULT_BASE_URL,
    EVIDENCE_CLAIM_CHOICES,
    ClassificationTask,
    TypeSafeClassifier,
    annotation_action_aspect_paths,
    annotation_action_aspects_task,
    annotation_action_coarse_task,
    annotation_action_task,
    claim_aspect_paths,
    coarse_action,
    derive_annotation_review_target,
    encode_pointer,
    extract_annotation_case,
    extract_claim,
    parse_pointer,
    render_prompt,
    resolve_pointer,
    response_schema,
    structured_evidence_claim_aspects_task,
    structured_evidence_claim_match_task,
)
from ai_gene_review.classifier.typesafe import _probabilities, extract_schema_answers


@pytest.fixture(scope="module")
def sample_gene_doc() -> dict[str, Any]:
    """Self-contained pinned GeneReview fixture (decoupled from live curation files)."""
    return {
        "id": "Q9BRQ4",
        "gene_symbol": "CFAP300",
        "product_type": "PROTEIN",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Curator synthesis that must be stripped from de-leaked cases.",
        "references": [
            {
                "id": "PMID:36246608",
                "title": "CFAP300 localization study",
                "publication_type": "JOURNAL_ARTICLE",
                "full_text_unavailable": True,
                "is_invalid": False,
                "findings": [
                    {
                        "statement": "CFAP300 localizes to the cytoplasm.",
                        "supporting_text": "CFAP300 localized in the cytoplasm",
                    }
                ],
                "reference_review": {"summary": "Curator note to strip"},
            },
            {
                "id": "PMID:29727692",
                "title": "Human CFAP300 variants cause primary ciliary dyskinesia",
                "publication_type": "JOURNAL_ARTICLE",
                "is_invalid": True,
                "findings": [
                    {
                        "statement": "Human CFAP300 variants cause combined loss of outer and inner dynein arms.",
                        "supporting_text": "combined loss",
                    }
                ],
            },
            {
                "id": "PMID:29727693",
                "title": "C11orf70 dynein arm assembly",
                "publication_type": "JOURNAL_ARTICLE",
            },
        ],
        "core_functions": [
            {
                "description": "Dynein arm preassembly factor.",
                "directly_involved_in": [
                    {
                        "id": "GO:0036158",
                        "label": "outer dynein arm assembly",
                    }
                ],
                "locations": [{"id": "GO:0005737", "label": "cytoplasm"}],
                "supported_by": [
                    {
                        "reference_id": "PMID:29727693",
                        "supporting_text": "C11orf70 is involved in cytoplasmic assembly of dynein arms",
                    }
                ],
            }
        ],
        "existing_annotations": [
            {
                "term": {"id": "GO:0005737", "label": "cytoplasm"},
                "qualifier": "located_in",
                "evidence_type": "IEA",
                "original_reference_id": "PMID:36246608",
                "review": {
                    "action": "ACCEPT",
                    "summary": "Core cytoplasmic localization.",
                    "reason": "Curator rationale that must not leak.",
                    "supported_by": [
                        {
                            "reference_id": "PMID:36246608",
                            "supporting_text": "CFAP300 localized in the cytoplasm",
                        }
                    ],
                },
            },
            {
                "term": {"id": "GO:0005856", "label": "cytoskeleton"},
                "qualifier": "located_in",
                "evidence_type": "IDA",
                "original_reference_id": "PMID:29727693",
                "review": {"action": "KEEP_AS_NON_CORE"},
            },
            {
                "term": {"id": "GO:0005515", "label": "protein binding"},
                "qualifier": "enables",
                "evidence_type": "IPI",
                "original_reference_id": "PMID:29727692",
                "review": {"action": "REMOVE"},
            },
            {
                "term": {"id": "GO:0036158", "label": "outer dynein arm assembly"},
                "qualifier": "involved_in",
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {
                    "action": "ACCEPT",
                    "propagation_review": {"root_cause": "NO_FAILURE_CORE"},
                },
            },
            {
                "term": {"id": "GO:0036159", "label": "inner dynein arm assembly"},
                "qualifier": "involved_in",
                "evidence_type": "IMP",
                "original_reference_id": "PMID:29727692",
                "review": {"action": "NEW"},
            },
        ],
    }


def _http_response(body: dict[str, Any]) -> httpx.Response:
    return httpx.Response(
        200,
        json=body,
        request=httpx.Request("POST", DEFAULT_BASE_URL),
    )


def test_pointer_helpers(sample_gene_doc: dict[str, Any]) -> None:
    tokens = parse_pointer("/existing_annotations/0")
    assert tokens == ["existing_annotations", "0"]
    assert encode_pointer(tokens) == "/existing_annotations/0"
    steps = resolve_pointer(sample_gene_doc, tokens)
    assert steps[-1][1]["term"]["id"] == "GO:0005737"


def test_extract_claim_from_core_functions(sample_gene_doc: dict[str, Any]) -> None:
    claim = extract_claim(sample_gene_doc, "/core_functions/0/supported_by/0")
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


def test_extract_claim_from_existing_annotations(
    sample_gene_doc: dict[str, Any],
) -> None:
    claim = extract_claim(
        sample_gene_doc, "/existing_annotations/0/review/supported_by/0"
    )
    assert claim["origin"]["assertion_path"] == "/existing_annotations/0"
    assert claim["assertion"]["term"] == {"id": "GO:0005737", "label": "cytoplasm"}
    assert claim["assertion"]["review"]["action"] == "ACCEPT"
    assert "supported_by" not in claim["assertion"].get("review", {})
    assert "reason" not in claim["assertion"].get("review", {})
    assert claim["selected_evidence"]["reference_id"] == "PMID:36246608"


def test_extract_claim_from_reference_findings(sample_gene_doc: dict[str, Any]) -> None:
    claim = extract_claim(sample_gene_doc, "/references/1/findings/0")
    assert claim["origin"]["section"] == "references"
    assert claim["selected_evidence"]["reference_id"] == "PMID:29727692"
    assert claim["selected_evidence"]["supporting_text"] == "combined loss"
    assert "Human CFAP300 variants" in claim["assertion"]["statement"]


def test_extract_annotation_case_strips_all_curator_leakage(
    sample_gene_doc: dict[str, Any],
) -> None:
    case = extract_annotation_case(sample_gene_doc, "/existing_annotations/0")
    assert case["about"]["gene"]["gene_symbol"] == "CFAP300"
    assert case["target_annotation"]["term"] == {
        "id": "GO:0005737",
        "label": "cytoplasm",
    }
    assert case["target_annotation"]["evidence_type"] == "IEA"
    assert "review" not in case["target_annotation"]
    assert "core_functions" not in case
    assert "description" not in case
    # Supporting excerpts from review.supported_by are excluded by default to prevent leakage
    assert "supporting_excerpts" not in case

    # Opt-in supporting_excerpts preserves primary quotes when explicitly requested
    case_with_excerpts = extract_annotation_case(
        sample_gene_doc,
        "/existing_annotations/0",
        include_supporting_excerpts=True,
    )
    assert case_with_excerpts["supporting_excerpts"] == [
        {
            "reference_id": "PMID:36246608",
            "supporting_text": "CFAP300 localized in the cytoplasm",
        },
    ]

    # Sibling annotations exclude action=NEW rows and GO:0005515, strip review blocks, and collapse
    assert case["sibling_raw_count"] == 2
    assert len(case["sibling_annotations"]) == 2
    for sib in case["sibling_annotations"]:
        assert "review" not in sib
        assert "count" in sib
        assert "evidence_types" in sib
        assert sib["term"]["id"] not in ("GO:0005515", "GO:0036159")

    # Reviewer-authored reference flags must be stripped from references_metadata
    refs = case.get("references_metadata", [])
    assert len(refs) == 1
    assert refs[0]["id"] == "PMID:36246608"
    for forbidden in (
        "findings",
        "reference_review",
        "full_text_unavailable",
        "is_invalid",
    ):
        assert forbidden not in refs[0]

    target = derive_annotation_review_target(sample_gene_doc, "/existing_annotations/0")
    assert target["action"] == "ACCEPT"
    assert target["coarse_action"] == "KEEP"
    assert target["is_core"] == "CORE"

    # Fail-fast pointer shape validation on derive_annotation_review_target
    with pytest.raises(ValueError, match="annotation_path must be"):
        derive_annotation_review_target(sample_gene_doc, "/")

    # Generic GO:0005515 protein binding is rejected as a benchmark target by default
    with pytest.raises(ValueError, match="GO:0005515"):
        extract_annotation_case(sample_gene_doc, "/existing_annotations/2")


def test_extract_annotation_case_rejects_new_rows(
    sample_gene_doc: dict[str, Any],
) -> None:
    with pytest.raises(ValueError, match="action='NEW'"):
        extract_annotation_case(sample_gene_doc, "/existing_annotations/4")


def test_rubric_includes_mandatory_policy_carve_outs() -> None:
    assert "GO_REF:0000015" in ANNOTATION_ACTION_INSTRUCTION
    assert "GO:0005739" in ANNOTATION_ACTION_INSTRUCTION
    assert "negated: true" in ANNOTATION_ACTION_INSTRUCTION


def test_classification_task_validates_output_schema_enums() -> None:
    with pytest.raises(ValueError, match="must define a non-empty 'enum' list"):
        ClassificationTask(
            instruction="Judge",
            context="Context",
            output_schema={
                "type": "object",
                "properties": {"/": {"type": "string"}},
            },
        )


def test_tasks_and_typesafe_single_label_roundtrip(
    sample_gene_doc: dict[str, Any],
) -> None:
    claim = extract_claim(sample_gene_doc, "/core_functions/0/supported_by/0")
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

    ann_case = extract_annotation_case(sample_gene_doc, "/existing_annotations/0")
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

    def fake_post(*args: Any, **kwargs: Any) -> httpx.Response:
        return _http_response(
            {
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
        )

    clf = TypeSafeClassifier(api_key="test-key", post=fake_post)
    res = clf.classify(act_task)
    assert res.label == "ACCEPT"
    assert res.confidence is not None and res.confidence > 0.9
    assert res.usage["input_tokens"] == 120


def test_typesafe_output_schema_multi_token_and_property_anchoring(
    sample_gene_doc: dict[str, Any],
) -> None:
    """Multi-token enum KEEP_AS_NON_CORE must not bleed into /coarse_action."""
    ann_case = extract_annotation_case(sample_gene_doc, "/existing_annotations/3")
    aspects_task = annotation_action_aspects_task(ann_case)
    assert aspects_task.output_schema is not None

    parsed_output = {
        "/": "KEEP_AS_NON_CORE",
        "/coarse_action": "KEEP",
        "/is_core": "NON_CORE",
        "/propagation_root_cause": "NO_FAILURE_NON_CORE",
    }
    # Simulate BPE splitting KEEP_AS_NON_CORE into KEEP + _AS + _NON + _CORE,
    # where the first KEEP token has different logprobs than /coarse_action's KEEP.
    logprobs = [
        {"token": '{"/"', "logprob": 0.0, "top_logprobs": []},
        {"token": ': "', "logprob": 0.0, "top_logprobs": []},
        {
            "token": "KEEP",
            "logprob": -0.5,
            "top_logprobs": [
                {"token": "KEEP", "logprob": -0.5},
                {"token": "REJECT", "logprob": -0.5},
            ],
        },
        {"token": "_AS", "logprob": 0.0, "top_logprobs": []},
        {"token": "_NON", "logprob": 0.0, "top_logprobs": []},
        {"token": "_CORE", "logprob": 0.0, "top_logprobs": []},
        {"token": '", "/coarse_action": "', "logprob": 0.0, "top_logprobs": []},
        {
            "token": "KEEP",
            "logprob": -0.01,
            "top_logprobs": [
                {"token": "KEEP", "logprob": -0.01},
                {"token": "REFINE", "logprob": -5.0},
            ],
        },
        {"token": '", "/is_core": "', "logprob": 0.0, "top_logprobs": []},
        {"token": "NON", "logprob": 0.0, "top_logprobs": []},
        {"token": "_CORE", "logprob": 0.0, "top_logprobs": []},
        {
            "token": '", "/propagation_root_cause": "',
            "logprob": 0.0,
            "top_logprobs": [],
        },
        {"token": "NO_FAILURE_NON_CORE", "logprob": -0.2, "top_logprobs": []},
        {"token": '"}', "logprob": 0.0, "top_logprobs": []},
    ]

    def fake_post(*args: Any, **kwargs: Any) -> httpx.Response:
        return _http_response(
            {
                "model": "jev-1.13.0",
                "output": json.dumps(parsed_output),
                "usage": {"input_tokens": 200, "output_tokens": 20},
                "logprobs": logprobs,
            }
        )

    clf = TypeSafeClassifier(api_key="test-key", post=fake_post)
    res = clf.classify(aspects_task)
    assert res.label == "KEEP_AS_NON_CORE"
    # Multi-token KEEP_AS_NON_CORE falls back cleanly to one-hot (confidence 1.0)
    assert res.probabilities["KEEP_AS_NON_CORE"] == 1.0
    assert res.confidence == 1.0
    # /coarse_action must use its own anchored KEEP token (~0.99), NOT the 50/50 KEEP fragment from /
    coarse_probs = res.answers["/coarse_action"]["probabilities"]
    assert coarse_probs["KEEP"] > 0.98
    assert coarse_probs["REFINE"] < 0.02
    assert res.answers["/is_core"]["label"] == "NON_CORE"
    assert res.answers["/is_core"]["probabilities"]["NON_CORE"] == 1.0
    assert res.answers["/propagation_root_cause"]["label"] == "NO_FAILURE_NON_CORE"
    assert (
        res.answers["/propagation_root_cause"]["probabilities"]["NO_FAILURE_NON_CORE"]
        == 1.0
    )


def test_typesafe_probabilities_missing_logprob_falls_back_to_one_hot() -> None:
    probs = _probabilities(
        {"token": "ACCEPT", "top_logprobs": []},
        ["ACCEPT", "REMOVE"],
        "ACCEPT",
    )
    assert probs == {"ACCEPT": 1.0, "REMOVE": 0.0}

    # Unanchored synthetic stream: single-alternative fallback must pick the FIRST match,
    # not candidates[-1], so later fields are not starved.
    schema = {
        "type": "object",
        "properties": {
            "/": {"type": "string", "enum": ["MATCH", "MISMATCH"]},
            "/about/gene": {"type": "string", "enum": ["MATCH", "MISMATCH"]},
        },
    }
    answers = extract_schema_answers(
        {
            "logprobs": [
                {"token": "MATCH", "logprob": -0.1, "top_logprobs": []},
                {"token": "MISMATCH", "logprob": -0.2, "top_logprobs": []},
            ]
        },
        schema,
        {"/": "MATCH", "/about/gene": "MISMATCH"},
    )
    assert answers["/"]["probabilities"] == {"MATCH": 1.0, "MISMATCH": 0.0}
    assert answers["/about/gene"]["probabilities"] == {"MATCH": 0.0, "MISMATCH": 1.0}
