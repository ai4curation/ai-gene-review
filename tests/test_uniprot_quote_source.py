"""Tests for checks on what kind of UniProt statement a supporting_text quotes.

Run against real UniProt flat files in the repository: P. putida serA (an
unreviewed entry whose name, function, pathway and keywords are ARBA-assigned),
M. extorquens serA (GO cross-references from ARBA and InterPro), P. putida gyrA
(function from a curated HAMAP rule, which is not flagged), mouse Abi2 (curated by-similarity and
experimental text) and human TP53 (experimentally supported comments and
features).
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import ValidationSeverity, validate_gene_review
from ai_gene_review.validation.uniprot_quote_source import (
    UNVETTED_CHECK,
    classify_quote,
    FIELD_CHECK,
    PROJECT_ROOT,
    locate_quote,
    parse_uniprot_statements,
    quote_source_findings,
)

SERA_PSEPK = "file:PSEPK/serA/serA-uniprot.txt"
SERA_METEA = "file:METEA/serA/serA-uniprot.txt"
TP53 = "file:human/TP53/TP53-uniprot.txt"
GYRA = "file:PSEPK/gyrA/gyrA-uniprot.txt"
ABI2 = "file:mouse/Abi2/Abi2-uniprot.txt"
TOLL9 = "file:ANOGA/TOLL9/TOLL9-uniprot.txt"


def _path(reference_id: str) -> Path:
    return PROJECT_ROOT / "genes" / reference_id.split(":", 1)[1]


@pytest.mark.parametrize(
    "reference_id,quote,field,topic,unvetted,sources",
    [
        (SERA_PSEPK, "RecName: Full=D-3-phosphoglycerate dehydrogenase", "DE", "", True, {"ARBA"}),
        (SERA_PSEPK, "Amino-acid biosynthesis; L-serine biosynthesis; L-serine from", "CC", "PATHWAY", True, {"ARBA"}),
        (SERA_PSEPK, "the first step of the phosphorylated L- serine biosynthesis pathway", "CC", "FUNCTION", True, {"ARBA"}),
        (SERA_METEA, "GO:0009070; P:serine family amino acid biosynthetic process", "DR", "GO", True, {"ARBA", "electronic GO"}),
        # imported from the submitter's record
        (SERA_METEA, "Reference proteome", "KW", "", True, {"imported"}),
        # ARBA plus a curated UniRule (RuleBase) source: supported
        (SERA_METEA, "Oxidoreductase {ECO:0000256|ARBA:ARBA00023002,", "KW", "", False, set()),
        # a HAMAP rule: curated family-based function, supported
        (GYRA, "A type II topoisomerase that negatively supercoils closed", "CC", "FUNCTION", False, set()),
        # curated: by similarity plus experimental
        (ABI2, "required for nascent adherens junction assembly in epithelial cells", "CC", "FUNCTION", False, set()),
        # curated text in a reviewed entry
        (TP53, "Multifunctional transcription factor that induces cell cycle", "CC", "FUNCTION", False, set()),
    ],
)
def test_locate_quote_finds_field_and_evidence(reference_id, quote, field, topic, unvetted, sources):
    statements = locate_quote(quote, _path(reference_id))
    assert statements, f"quote not located: {quote}"
    assert {s.field for s in statements} == {field}
    assert {s.topic for s in statements} == {topic}
    assert all(s.is_unvetted for s in statements) is unvetted
    if unvetted:
        assert {label for s in statements for label in s.unvetted_sources} == sources


def test_arba_only_family_note_is_an_unvetted_prediction():
    """A "Belongs to" note is classification evidence unless ARBA alone asserts it."""
    unvetted, restating, statements = classify_quote(
        "Belongs to the Toll-like receptor family.", _path(TOLL9))
    assert [(s.field, s.topic) for s in statements] == [("CC", "SIMILARITY")]
    assert unvetted and not restating


def test_family_membership_is_not_flagged():
    """Family cross-references and "Belongs to" notes are classification evidence."""
    for quote in ["NCBIfam; NF008759; PRK11790.1; 1.", "InterPro; IPR006139; D-isomer_2_OHA_DH_cat_dom."]:
        unvetted, restating, _ = classify_quote(quote, _path(SERA_PSEPK))
        assert (unvetted, restating) == (False, False), quote


def test_ambiguous_quote_is_flagged_only_if_every_occurrence_is():
    """'NAD' is a keyword here, but also appears in a reaction comment (not a
    label) and in family cross-references with no evidence tag (not unvetted)."""
    unvetted, restating, _ = classify_quote("NAD", _path(SERA_METEA))
    assert not unvetted
    assert not restating

    assert locate_quote("text that is not in the record at all", _path(TP53)) == []


def test_feature_evidence_is_read_from_evidence_qualifier():
    statements = parse_uniprot_statements(_path(TP53).read_text())
    dna_bind = [s for s in statements if s.field == "FT" and s.topic == "DNA_BIND"]
    assert dna_bind
    assert any("ECO:0000269" in e for e in dna_bind[0].evidence)


def _review(supported_by: list) -> dict:
    return {
        "id": "Q00000",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene.",
        "references": [],
        "core_functions": [{"description": "x", "supported_by": supported_by}],
    }


def test_findings_flag_unvetted_and_restating_fields():
    data = _review([
        {"reference_id": SERA_PSEPK, "supporting_text": "RecName: Full=D-3-phosphoglycerate dehydrogenase"},
        {"reference_id": SERA_PSEPK, "supporting_text": "Amino-acid biosynthesis; L-serine biosynthesis; L-serine from"},
        {"reference_id": TP53, "supporting_text": "Multifunctional transcription factor that induces cell cycle"},
        {"reference_id": "PMID:1", "supporting_text": "not a UniProt quote"},
    ])
    found = quote_source_findings(data)
    by_check = {}
    for f in found:
        by_check.setdefault(f.check_type, []).append(f.path)
    assert sorted(by_check) == sorted([UNVETTED_CHECK, FIELD_CHECK])
    assert by_check[UNVETTED_CHECK] == [
        "core_functions[0].supported_by[0].supporting_text",
        "core_functions[0].supported_by[1].supporting_text",
    ]
    assert by_check[FIELD_CHECK] == ["core_functions[0].supported_by[0].supporting_text"]


def test_validation_reports_both_checks_as_warnings(tmp_path):
    data = _review([
        {"reference_id": SERA_PSEPK, "supporting_text": "RecName: Full=D-3-phosphoglycerate dehydrogenase"},
    ])
    path = tmp_path / "TEST-ai-review.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    report = validate_gene_review(path, check_best_practices=True, check_goa=False, check_supporting_text=False)
    issues = [i for i in report.issues if i.check_type in (UNVETTED_CHECK, FIELD_CHECK)]
    assert sorted(i.check_type for i in issues) == sorted([UNVETTED_CHECK, FIELD_CHECK])
    assert all(i.severity == ValidationSeverity.WARNING.value for i in issues)
