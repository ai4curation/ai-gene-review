"""Reference remapping and cross-paper finding evidence preserve source identity."""

from pathlib import Path
import subprocess
import sys

import pytest
from pydantic import ValidationError
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from ai_gene_review.datamodel.gene_review_model import GeneReview, ReferenceReview
from ai_gene_review.validation import validate_gene_review
from ai_gene_review.utils.pmid_utils import mark_invalid_pmids
import yaml


SCHEMA = Path(__file__).parents[1] / "src/ai_gene_review/schema/gene_review.yaml"


def review_data():
    """Synthetic records distinguish original, canonical, and contradicting sources."""
    return {
        "id": "TEST", "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Synthetic fixture for reference metadata.",
        "references": [
            {"id": "PMID:1", "title": "Deleted duplicate", "is_invalid": True, "reference_review": {
                "replacement": {"reference_id": "PMID:2", "reason": "DUPLICATE_RECORD"},
                "review_notes": "Synthetic verified duplicate mapping.",
            }},
            {"id": "PMID:2", "title": "Original study", "findings": [{
                "statement": "Activity occurs without a cofactor.",
                "finding_review": {
                    "finding_status": "DISPUTED", "superseded_by": ["PMID:3"],
                    "supported_by": [{"reference_id": "PMID:3", "supporting_text": "A cofactor was required."}],
                },
            }]},
            {"id": "PMID:3", "title": "Follow-up study"},
        ],
        "existing_annotations": [{
            "term": {"id": "GO:0005515", "label": "protein binding"},
            "evidence_type": "IPI", "original_reference_id": "PMID:1",
            "review": {"action": "UNDECIDED", "supported_by": [
                {"reference_id": "PMID:2", "supporting_text": "An interaction was observed."},
            ]},
        }],
    }


def test_metadata_roundtrip_preserves_each_source():
    data = GeneReview.model_validate(review_data()).model_dump(mode="json", exclude_none=True)
    assert data["existing_annotations"][0]["original_reference_id"] == "PMID:1"
    assert data["existing_annotations"][0]["review"]["supported_by"][0]["reference_id"] == "PMID:2"
    assert data["references"][0]["reference_review"]["replacement"]["reference_id"] == "PMID:2"
    evidence = data["references"][1]["findings"][0]["finding_review"]["supported_by"][0]
    assert evidence == {"reference_id": "PMID:3", "supporting_text": "A cofactor was required."}
    assert data["references"][0]["is_invalid"] is True


def test_invalid_pmid_tool_preserves_curated_replacement(tmp_path):
    """An invalid source record and its valid replacement coexist without churn."""
    data = review_data()
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump(data))
    assert mark_invalid_pmids(path, ["PMID:1"]) == 0
    assert yaml.safe_load(path.read_text()) == data


@pytest.mark.parametrize("replacement", [
    {"reason": "DUPLICATE_RECORD"},
    {"reference_id": "PMID:2"},
    {"reference_id": "PMID:2", "reason": "RETRACTED"},
])
def test_incomplete_or_invalid_replacement_rejected(replacement):
    with pytest.raises(ValidationError):
        ReferenceReview(replacement=replacement)


def test_schema_exposes_cross_paper_evidence_to_lrv():
    sv = SchemaView(str(SCHEMA))
    assert sv.induced_slot("replacement", "ReferenceReview").range == "ReferenceReplacement"
    assert sv.induced_slot("reference_id", "ReferenceReplacement").required
    assert sv.induced_slot("supported_by", "FindingReview").range == "SupportingTextInReference"
    assert sv.induced_slot("supported_by", "FindingReview").multivalued


@pytest.mark.parametrize("target,expected", [("PMID:1", "itself"), ("PMID:9", "non-existent")])
def test_replacement_target_integrity(tmp_path, target, expected):
    data = review_data()
    data["references"][0]["reference_review"]["replacement"]["reference_id"] = target
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump(data))
    report = validate_gene_review(path, check_goa=False, check_supporting_text=False)
    assert any(i.is_error() and expected in i.message for i in report.issues)


def test_replacement_cycle_rejected(tmp_path):
    data = review_data()
    data["references"][1]["reference_review"] = {
        "replacement": {"reference_id": "PMID:1", "reason": "DUPLICATE_RECORD"},
    }
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump(data))
    report = validate_gene_review(path, check_goa=False, check_supporting_text=False)
    assert any(i.is_error() and "cycle" in i.message for i in report.issues)


@pytest.mark.parametrize("quote,valid", [
    ("A cofactor was required.", True),
    ("An interaction was observed.", False),
])
def test_lrv_checks_finding_review_quote_against_explicit_source(tmp_path, quote, valid):
    """Run real LRV offline: a quote from P2 must not pass when attributed to P3."""
    data = review_data()
    data["references"][1]["findings"][0]["finding_review"]["supported_by"][0]["supporting_text"] = quote
    cache = tmp_path / "publications"
    cache.mkdir()
    texts = ["Duplicate record.", "An interaction was observed.", "A cofactor was required."]
    for ref, text in zip(data["references"], texts):
        metadata = {"pmid": ref["id"].split(":")[1], "title": ref["title"], "full_text_available": True}
        (cache / (ref["id"].replace(":", "_") + ".md")).write_text(
            "---\n" + yaml.safe_dump(metadata) + "---\n\n" + text + "\n"
        )
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump(data))
    config = tmp_path / "config.yaml"
    config.write_text(yaml.safe_dump({"cache_dir": str(cache)}))
    result = subprocess.run(
        [str(Path(sys.executable).with_name("linkml-reference-validator")),
         "validate", "data", str(path), "--schema", str(SCHEMA),
         "--target-class", "GeneReview", "--config", str(config)],
        capture_output=True, text=True, check=False,
    )
    output = result.stdout + result.stderr
    assert (result.returncode == 0) == valid, output
    if not valid:
        assert "finding_review.supported_by" in output
        assert "PMID:3" in output
