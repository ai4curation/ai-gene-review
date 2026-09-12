"""Tests for ai_gene_review.validation.goa_validator.referenced_pmids."""

import pytest

from ai_gene_review.validation.goa_validator import (
    EXPERIMENTAL_EVIDENCE_CODES,
    GOAAnnotation,
    referenced_pmids,
)


def _row(go_id: str, evidence: str, reference: str) -> GOAAnnotation:
    return GOAAnnotation.from_tsv_row(
        [
            "UniProtKB", "O43837", "IDH3B", "", go_id, "some term",
            "biological_process", "ECO:0000314", evidence, reference, "",
            "9606", "Homo sapiens", "UniProt", "IDH3B", "20200101",
        ]
    )


def test_extracts_pmids_with_evidence_codes():
    anns = [
        _row("GO:0006099", "IDA", "PMID:111"),
        _row("GO:0006099", "IMP", "PMID:111"),
        _row("GO:0005739", "IBA", "PMID:222"),
    ]
    result = referenced_pmids(anns)
    assert result == {"PMID:111": {"IDA", "IMP"}, "PMID:222": {"IBA"}}


def test_ignores_non_pmid_references():
    anns = [
        _row("GO:0006099", "IEA", "GO_REF:0000120"),
        _row("GO:0006099", "TAS", "Reactome:R-HSA-70967"),
        _row("GO:0006099", "IDA", "PMID:333"),
    ]
    assert referenced_pmids(anns) == {"PMID:333": {"IDA"}}


def test_evidence_code_filter():
    anns = [
        _row("GO:0006099", "IDA", "PMID:111"),
        _row("GO:0005739", "IBA", "PMID:222"),
    ]
    exp = referenced_pmids(anns, evidence_codes=EXPERIMENTAL_EVIDENCE_CODES)
    assert exp == {"PMID:111": {"IDA"}}


def test_pipe_separated_references():
    anns = [_row("GO:0006099", "IDA", "PMID:111|PMID:222")]
    assert referenced_pmids(anns) == {"PMID:111": {"IDA"}, "PMID:222": {"IDA"}}


@pytest.mark.parametrize("evidence", sorted(EXPERIMENTAL_EVIDENCE_CODES))
def test_all_experimental_codes_recognized(evidence: str):
    anns = [_row("GO:0006099", evidence, "PMID:999")]
    assert referenced_pmids(anns, evidence_codes=EXPERIMENTAL_EVIDENCE_CODES) == {
        "PMID:999": {evidence}
    }
