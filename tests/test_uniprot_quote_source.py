"""Tests for checks on what kind of UniProt statement a supporting_text quotes.

Run against real UniProt flat files in the repository: P. putida serA (an
unreviewed entry whose name, function, pathway and keywords are ARBA-assigned),
M. extorquens serA (GO cross-references from ARBA and InterPro), P. putida gyrA
(function from a curated HAMAP rule, which is not flagged), mouse Abi2 (curated by-similarity and
experimental text), human TP53 (experimentally supported comments and
features), human APOC4 and AURKB (feature and reaction quotes), P. putida benC
([2Fe-2S] cofactor notation), A. thaliana FBL22 (protein existence "Predicted")
and human STK36 (a quote fragment whose only word also appears on the PE line).
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import ValidationSeverity, validate_gene_review
from ai_gene_review.validation.uniprot_quote_source import (
    UNVETTED_CHECK,
    EXISTENCE_CHECK,
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
ACRIF3 = "file:9CAUD/acrIF3/acrIF3-uniprot.txt"
APOC4 = "file:human/APOC4/APOC4-uniprot.txt"
AURKB = "file:human/AURKB/AURKB-uniprot.txt"
BENC = "file:PSEPK/benC/benC-uniprot.txt"
FBL22 = "file:ARATH/FBL22/FBL22-uniprot.txt"
STK36 = "file:human/STK36/STK36-uniprot.txt"


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
    unvetted, restating, _, statements = classify_quote(
        "Belongs to the Toll-like receptor family.", _path(TOLL9))
    assert [(s.field, s.topic) for s in statements] == [("CC", "SIMILARITY")]
    assert unvetted and not restating


def test_machine_generated_name_is_an_unvetted_prediction():
    """A ProtNLM name (ECO:0008006) is a model's guess, not evidence."""
    unvetted, restating, _, statements = classify_quote("RecName: Full=Phage protein", _path(ACRIF3))
    assert [s.field for s in statements] == ["DE"]
    assert unvetted and restating
    assert statements[0].unvetted_sources == ("machine-generated name",)


@pytest.mark.parametrize("reference_id,topic,tool", [
    (TOLL9, "TRANSMEM", "SAM:Phobius"),
    (ABI2, "REGION", "SAM:MobiDB-lite"),
])
def test_sequence_analysis_features_are_evidence(reference_id, topic, tool):
    """Phobius, SignalP, MobiDB-lite and Coils features are valid computational evidence."""
    features = [s for s in parse_uniprot_statements(_path(reference_id).read_text())
                if s.field == "FT" and s.topic == topic and s.evidence
                and all(tool in e for e in s.evidence)]
    assert features
    assert not any(s.is_unvetted for s in features)


def test_family_membership_is_not_flagged():
    """Family cross-references and "Belongs to" notes are classification evidence."""
    for quote in ["NCBIfam; NF008759; PRK11790.1; 1.", "InterPro; IPR006139; D-isomer_2_OHA_DH_cat_dom."]:
        unvetted, restating, _, _ = classify_quote(quote, _path(SERA_PSEPK))
        assert (unvetted, restating) == (False, False), quote


def test_ambiguous_quote_is_flagged_only_if_every_occurrence_is():
    """'NAD' is a keyword here, but also appears in a reaction comment (not a
    label) and in family cross-references with no evidence tag (not unvetted)."""
    unvetted, restating, _, _ = classify_quote("NAD", _path(SERA_METEA))
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


def test_snapshot_flatfile_quotes_keep_provenance_checks(tmp_path):
    source = tmp_path / 'genes/X/g/g-record-evidence.yaml'
    source.parent.mkdir(parents=True)
    source.write_text(yaml.safe_dump({
        'unisave_records': [{'record_text': (
            'DE   RecName: Full=Predicted kinase;\n'
            'CC   -!- FUNCTION: Binds unusual lipids. {ECO:0000256|ARBA:ARBA1}.\n'
            'CC   -!- ACTIVITY: Hydrolyzes ATP. {ECO:0000269|PubMed:1}.\n'
        )}],
        'observations': {'computed_note': 'Metadata is not a protein statement'},
    }))
    reference = 'file:X/g/g-record-evidence.yaml'
    data = _review([{'reference_id': reference, 'supporting_text': quote} for quote in [
        'RecName: Full=Predicted kinase', 'Binds unusual lipids', 'Hydrolyzes ATP',
        'Metadata is not a protein statement',
    ]])
    found = quote_source_findings(data, project_root=tmp_path)
    assert {(f.path, f.check_type) for f in found} == {
        ('core_functions[0].supported_by[0].supporting_text', FIELD_CHECK),
        ('core_functions[0].supported_by[1].supporting_text', UNVETTED_CHECK),
    }
    # A newer curated occurrence of the same statement prevents an all-unvetted flag.
    snapshot = yaml.safe_load(source.read_text())
    snapshot['unisave_records'].append({'record_text':
        'CC   -!- FUNCTION: Binds unusual lipids. {ECO:0000269|PubMed:2}.\n'})
    source.write_text(yaml.safe_dump(snapshot))
    assert not any(f.check_type == UNVETTED_CHECK for f in quote_source_findings(data, project_root=tmp_path))

@pytest.mark.parametrize("reference_id,quote,unvetted,restating", [
    (SERA_METEA, "DR   GO; GO:0009070; P:serine family amino acid biosynthetic process; IEA:UniProtKB-ARBA.",
     True, True),
    (SERA_PSEPK, "DR   InterPro; IPR006139; D-isomer_2_OHA_DH_cat_dom.", False, False),
])
def test_quote_with_line_code_is_located(reference_id, quote, unvetted, restating):
    """A quote copied with its flat-file line code is located, not skipped."""
    result = classify_quote(quote, _path(reference_id))
    assert result is not None
    assert result[:2] == (unvetted, restating)


def test_snapshot_inherits_line_code_and_protein_existence_checks(tmp_path):
    """The merged classifier applies upstream quote handling to archived entries too."""
    source = tmp_path / "genes/X/g/g-record-evidence.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(yaml.safe_dump({"unisave_records": [{"record_text": (
        "CC   -!- FUNCTION: Binds unusual lipids. {ECO:0000256|ARBA:ARBA1}.\n"
        "PE   4: Predicted;\n"
    )}]}))
    reference = "file:X/g/g-record-evidence.yaml"
    data = _review([
        {"reference_id": reference, "supporting_text": quote}
        for quote in ["CC   -!- FUNCTION: Binds unusual lipids.", "PE   4: Predicted;"]
    ])
    assert {(finding.path, finding.check_type) for finding in quote_source_findings(
        data, project_root=tmp_path
    )} == {
        ("core_functions[0].supported_by[0].supporting_text", UNVETTED_CHECK),
        ("core_functions[0].supported_by[1].supporting_text", EXISTENCE_CHECK),
    }


def test_quote_spanning_line_wrap_with_codes_is_located():
    quote = ("CC   -!- FUNCTION: Multifunctional transcription factor that induces cell cycle\n"
             "CC       arrest, DNA repair or apoptosis")
    statements = locate_quote(quote, _path(TP53))
    assert [(s.field, s.topic) for s in statements] == [("CC", "FUNCTION")]


@pytest.mark.parametrize("reference_id,quote,topic", [
    (TP53, "FT   DNA_BIND        102..292", "DNA_BIND"),
    (APOC4,
     'FT   SIGNAL          1..27\nFT                   /evidence="ECO:0000250|UniProtKB:P55057"', "SIGNAL"),
])
def test_feature_quote_with_key_and_location_is_located(reference_id, quote, topic):
    statements = locate_quote(quote, _path(reference_id))
    assert [(s.field, s.topic) for s in statements] == [("FT", topic)]


def test_editorial_bracket_is_a_gap():
    """[protein] is dropped as editorial; the words either side are not adjacent in the record."""
    quote = "CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +"
    statements = locate_quote(quote, _path(AURKB))
    assert {(s.field, s.topic) for s in statements} == {("CC", "CATALYTIC ACTIVITY")}


def test_literal_bracket_notation_stays_in_the_quote():
    """[2Fe-2S] is quoted text, not an editorial gap, so the quote stays in one statement."""
    statements = locate_quote("Name=[2Fe-2S] cluster", _path(BENC))
    assert [(s.field, s.topic) for s in statements] == [("CC", "COFACTOR")]



def _annotation(action: str, evidence_type: str = "ISM") -> dict:
    data = _review([])
    data["existing_annotations"] = [{
        "term": {"id": "GO:0005634", "label": "nucleus"},
        "evidence_type": evidence_type,
        "review": {"action": action, "supported_by": [
            {"reference_id": FBL22, "supporting_text": "PE   4: Predicted;"}]},
    }]
    return data


@pytest.mark.parametrize("action,flagged", [
    ("ACCEPT", True),
    ("NEW", True),
    ("MARK_AS_OVER_ANNOTATED", False),
    ("KEEP_AS_NON_CORE", False),
    ("MODIFY", False),
    ("UNDECIDED", False),
])
def test_protein_existence_cannot_support_accept(action, flagged):
    """PE says whether the protein exists, not what it does: fair to argue an annotation
    rests on prediction, never support for accepting one. It is not a restating label."""
    checks = [f.check_type for f in quote_source_findings(_annotation(action))]
    assert FIELD_CHECK not in checks
    assert (EXISTENCE_CHECK in checks) is flagged


def test_protein_existence_cannot_support_core_function():
    data = _review([{"reference_id": FBL22, "supporting_text": "PE   4: Predicted;"}])
    assert [f.check_type for f in quote_source_findings(data)] == [EXISTENCE_CHECK]


def test_nd_accept_backed_by_protein_existence_asks_for_a_literature_search(tmp_path):
    path = tmp_path / "TEST-ai-review.yaml"
    path.write_text(yaml.safe_dump(_annotation("ACCEPT", evidence_type="ND"), sort_keys=False))
    report = validate_gene_review(path, check_best_practices=True, check_goa=False, check_supporting_text=False)
    issues = [i for i in report.issues if i.check_type == EXISTENCE_CHECK]
    assert len(issues) == 1 and "literature was searched" in issues[0].suggestion


def test_word_also_outside_the_pe_line_is_not_protein_existence():
    """'/evidence="ECO:...' reduces to 'evidence', which first occurs on the PE line
    ('Evidence at protein level') but also in feature qualifiers: not a PE quote."""
    data = _review([{"reference_id": STK36, "supporting_text": '/evidence="ECO:0000250|UniProtKB:P23647,'}])
    assert EXISTENCE_CHECK not in [f.check_type for f in quote_source_findings(data)]
