from pathlib import Path

import pytest
import yaml

from scripts.gogpt_predict import (
    CONFIDENCE_BY_ASSESSMENT,
    MANUAL_ASSESSMENT_MARKER,
    ONTOLOGY_LABEL_AUDIT_MARKER,
    build_prediction_entry,
    deterministic_assessment,
    filter_to_leaf_terms,
    parse_bioreason_go_terms,
    prediction_review_status,
    validate_leaf_terms,
)


class FakeGOAdapter:
    def __init__(self, labels=None):
        self.labels = labels or {}

    def label(self, go_id):
        return self.labels.get(go_id)


def term(go_id, label, aspect):
    return {
        "id": go_id,
        "raw_label": label,
        "aspect": aspect,
        "type": {"MF": "GO_MF", "BP": "GO_BP", "CC": "GO_CC"}[aspect],
    }


def test_parse_bioreason_go_terms_preserves_raw_malformed_labels():
    markdown = """
### GO Terms
**Molecular Function:** oxidoreductase activity, acting on NADP (`GO:0000001`), GO:1234567 (`GO:0000002`)
**Biological Process:** example process (`GO:0000003`)
**Cellular Component:** example component (`GO:0000004`)
"""

    parsed = parse_bioreason_go_terms(markdown)

    assert parsed == [
        term("GO:0000001", "oxidoreductase activity, acting on NADP", "MF"),
        term("GO:0000002", "GO:1234567", "MF"),
        term("GO:0000003", "example process", "BP"),
        term("GO:0000004", "example component", "CC"),
    ]


def test_leaf_filter_removes_ancestors_generics_and_duplicates():
    terms = [
        term("GO:0003674", "molecular_function", "MF"),
        term("GO:0003824", "catalytic activity", "MF"),
        term("GO:0004146", "dihydrofolate reductase activity", "MF"),
        term("GO:0004146", "dihydrofolate reductase activity", "MF"),
        term("GO:0005622", "intracellular anatomical structure", "CC"),
        term("GO:0005737", "cytoplasm", "CC"),
    ]
    ancestors = {
        "GO:0003674": {"GO:0003674"},
        "GO:0003824": {"GO:0003674", "GO:0003824"},
        "GO:0004146": {"GO:0003674", "GO:0003824", "GO:0004146"},
        "GO:0005622": {"GO:0005622"},
        "GO:0005737": {"GO:0005575", "GO:0005737"},
    }

    leaves = filter_to_leaf_terms(terms, lambda go_id: ancestors[go_id])

    assert [(item["id"], item["aspect"]) for item in leaves] == [
        ("GO:0004146", "MF"),
        ("GO:0005737", "CC"),
    ]
    validate_leaf_terms(leaves, lambda go_id: ancestors[go_id])


def test_leaf_validation_rejects_retained_ancestor():
    retained = [
        term("GO:0003824", "catalytic activity", "MF"),
        term("GO:0004146", "dihydrofolate reductase activity", "MF"),
    ]
    ancestors = {
        "GO:0003824": {"GO:0003674", "GO:0003824"},
        "GO:0004146": {"GO:0003674", "GO:0003824", "GO:0004146"},
    }

    with pytest.raises(ValueError, match="retains ancestors"):
        validate_leaf_terms(retained, lambda go_id: ancestors[go_id])


@pytest.mark.parametrize(
    ("actions", "assessment", "confidence"),
    [
        ({"ACCEPT"}, "CNN", 2),
        ({"KEEP_AS_NON_CORE"}, "CNN", 2),
        ({"ACCEPT", "REMOVE"}, "CNN", 2),
        ({"REMOVE"}, "NPI", 0),
        ({"MARK_AS_OVER_ANNOTATED"}, "NPI", 0),
        ({"NOT:ACCEPT"}, "NPI", 0),
        ({"REMOVE", "PENDING"}, "UNC", 1),
        ({"MODIFY"}, "UNC", 1),
        (set(), "UNC", 1),
    ],
)
def test_deterministic_assessment_uses_only_exact_aigr_actions(
    actions, assessment, confidence
):
    actual, summary = deterministic_assessment("GO:0004146", {"GO:0004146": actions})

    assert actual == assessment
    assert CONFIDENCE_BY_ASSESSMENT[actual] == confidence
    assert (MANUAL_ASSESSMENT_MARKER in summary) is (assessment == "UNC")


def test_prediction_entry_normalizes_malformed_raw_label_and_confidence():
    adapter = FakeGOAdapter({"GO:0005515": "protein binding"})
    existing = {
        "review": {
            "assessment": "NPI",
            "confidence_score": 2,
            "summary": "Manual review found this prediction incorrect.",
        }
    }

    prediction = build_prediction_entry(
        term("GO:0005515", "GO:0005515", "MF"),
        {},
        {},
        adapter,
        "test-version",
        existing,
    )

    assert prediction["predicted_term"]["label"] == "protein binding"
    assert prediction["review"]["assessment"] == "NPI"
    assert prediction["review"]["confidence_score"] == 0
    assert "malformed" in prediction["review"]["summary"]
    assert ONTOLOGY_LABEL_AUDIT_MARKER in prediction["review"]["summary"]


def test_document_is_draft_until_all_placeholders_are_resolved():
    unresolved = [
        {"review": {"summary": f"Prediction unresolved. {MANUAL_ASSESSMENT_MARKER}."}}
    ]
    resolved = [{"review": {"summary": "Manual review completed."}}]

    assert prediction_review_status(unresolved) == "DRAFT"
    assert prediction_review_status(resolved) == "COMPLETE"


def test_committed_gogpt_leaf_reviews_are_not_false_complete():
    repo_root = Path(__file__).resolve().parents[1]
    paths = sorted(repo_root.glob("genes/*/*/*-gogpt-leaf-predictions.yaml"))
    assert len(paths) == 139

    dfrp_assessment = None
    cts2_assessment = None
    cts2_description = None
    for path in paths:
        document = yaml.safe_load(path.read_text())
        if path.parent.name == "cts2":
            cts2_description = document["description"]
        summaries = []
        for prediction in document.get("predictions", []):
            predicted_term = prediction["predicted_term"]
            review = prediction["review"]
            summaries.append(review["summary"])

            assert predicted_term["label"] not in {"", "Unknown"}
            assert not all(
                part.startswith("GO:") for part in predicted_term["label"].split()
            )
            assert review["confidence_score"] == CONFIDENCE_BY_ASSESSMENT[
                review["assessment"]
            ]

            if path.parent.name == "dfrP" and predicted_term["id"] == "GO:0004146":
                dfrp_assessment = review["assessment"]
            if path.parent.name == "cts2" and predicted_term["id"] == "GO:0004568":
                cts2_assessment = review["assessment"]

        if any(MANUAL_ASSESSMENT_MARKER in summary for summary in summaries):
            assert document["status"] == "DRAFT"
        for source in document.get("source_documents", []):
            assert (path.parent / source).exists()

    assert dfrp_assessment == "CNN"
    assert cts2_assessment == "NPI"
    assert ONTOLOGY_LABEL_AUDIT_MARKER in cts2_description
    assert "GO:0044237 <- 'GO:0071554'" in cts2_description
