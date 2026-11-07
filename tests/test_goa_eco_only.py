"""Preserve a real ECO-only source assertion through fetch, seed and validation."""

from unittest.mock import Mock, patch

import pytest
import yaml
from pydantic import ValidationError

from ai_gene_review.datamodel.gene_review_model import ExistingAnnotation
from ai_gene_review.etl.gene import fetch_goa_data
from ai_gene_review.validation.goa_validator import GOAAnnotation, GOAValidator


def source_row(go_code=None):
    """Shape returned by QuickGO for A5FI22 on 2026-11-07."""
    return {
        "geneProductId": "UniProtKB:A5FI22",
        "symbol": "Fjoh_2111",
        "qualifier": "acts_upstream_of_or_within_positive_effect",
        "goId": "GO:0042953",
        "goName": "lipoprotein transport",
        "goEvidence": go_code,
        "goAspect": "biological_process",
        "evidenceCode": "ECO:0007744",
        "reference": "PMID:40050408",
        "withFrom": [{"connectedXrefs": [{"db": "UniProtKB", "id": "P61316"}]}],
        "taxonId": 376686,
        "taxonName": None,
        "assignedBy": "CACAO",
        "name": None,
        "date": "20250407",
    }


def downloaded_tsv(row):
    response = Mock()
    response.json.return_value = {"results": [row], "numberOfHits": 1}
    with patch("ai_gene_review.etl.gene.requests.get", return_value=response):
        return fetch_goa_data("A5FI22")


def test_null_go_code_preserves_raw_eco_and_empty_columns():
    fields = downloaded_tsv(source_row()).splitlines()[1].split("\t")
    assert len(fields) == 16
    assert fields[7:9] == ["ECO:0007744", ""]
    assert fields[12] == fields[14] == ""
    parsed = GOAAnnotation.from_tsv_row(fields)
    assert parsed.evidence_code == parsed.evidence_type == "ECO:0007744"
    assert parsed.qualifier == "acts_upstream_of_or_within_positive_effect"
    assert parsed.reference == "PMID:40050408"
    assert parsed.with_from == "UniProtKB:P61316"


def test_go_shorthand_still_takes_precedence():
    row = source_row("IDA")
    row["evidenceCode"] = "ECO:0000314"
    fields = downloaded_tsv(row).splitlines()[1].split("\t")
    parsed = GOAAnnotation.from_tsv_row(fields)
    assert parsed.evidence_code == "IDA"
    assert parsed.evidence_type == "ECO:0000314"


def test_eco_only_seed_is_schema_valid_idempotent_and_strictly_matched(tmp_path):
    raw = downloaded_tsv(source_row())
    goa = tmp_path / "Fjoh_2111-goa.tsv"
    goa.write_text(raw)
    review = tmp_path / "Fjoh_2111-ai-review.yaml"
    review.write_text(yaml.safe_dump({
        "id": "A5FI22", "gene_symbol": "Fjoh_2111",
        "taxon": {"id": "NCBITaxon:376686", "label": "Flavobacterium johnsoniae UW101"},
        "description": "A lipoprotein carrier.",
    }))
    validator = GOAValidator(strict_mode=True)
    assert validator.seed_missing_annotations(review, goa)[0] == 1
    document = yaml.safe_load(review.read_text())
    annotation = document["existing_annotations"][0]
    assert annotation["evidence_type"] == "ECO:0007744"
    assert annotation["qualifier"] == "acts_upstream_of_or_within_positive_effect"
    assert annotation["supporting_entities"] == ["UniProtKB:P61316"]
    ExistingAnnotation.model_validate(annotation)
    assert validator.validate_against_goa(review, goa).is_valid
    before = review.read_bytes()
    assert validator.seed_missing_annotations(review, goa)[0] == 0
    assert review.read_bytes() == before
    assert goa.read_text() == raw
    annotation["evidence_type"] = "IMP"
    review.write_text(yaml.safe_dump(document))
    assert not validator.validate_against_goa(review, goa).is_valid


def test_unknown_evidence_is_not_silently_accepted():
    with pytest.raises(ValidationError):
        ExistingAnnotation.model_validate({
            "term": {"id": "GO:0042953", "label": "lipoprotein transport"},
            "evidence_type": "ECO:9999999",
            "original_reference_id": "PMID:40050408",
        })
