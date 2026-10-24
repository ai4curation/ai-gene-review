"""Tests for ``record_section``: which section of a UniProt record a quote comes from.

Run against the real human TP53 flat file in the repository, which has
curated FUNCTION and CAUTION comments, features, Pfam cross-references and a
protein name, and the Arabidopsis AOP2 UniSave snapshot, whose archived entry
has a CAUTION comment.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.tools.backfill_record_sections import backfill_text
from ai_gene_review.validation import ValidationSeverity, validate_gene_review
from ai_gene_review.validation.uniprot_quote_source import (
    AMBIGUOUS,
    LOCATED,
    PROJECT_ROOT,
    UNLOCATED,
    UNSEARCHABLE,
    RECORD_SECTION_CHECK,
    locate_sections,
    record_section_findings,
    record_sections,
)

TP53 = "file:human/TP53/TP53-uniprot.txt"
TP53_PATH = PROJECT_ROOT / "genes" / "human" / "TP53" / "TP53-uniprot.txt"
CAUTION_QUOTE = (
    "Interaction with BANP was reported to enhance phosphorylation on Ser-15"
)
FUNCTION_QUOTE = "Multifunctional transcription factor that induces cell cycle"


@pytest.mark.parametrize(
    "quote,expected",
    [
        (CAUTION_QUOTE, ["CC:CAUTION"]),
        (FUNCTION_QUOTE, ["CC:FUNCTION"]),
        # quoted with the flat-file line prefix
        ("CC   -!- CAUTION: Interaction with BANP was reported", ["CC:CAUTION"]),
        ("Pfam; PF00870; P53; 1.", ["DR:Pfam"]),
        ('/note="Interaction with HRMT1L2"', ["FT:REGION"]),
        ("RecName: Full=Cellular tumor antigen p53", ["DE"]),
        # parts from two sections, listed once each, in quote order
        (f"{FUNCTION_QUOTE} ... {CAUTION_QUOTE}", ["CC:FUNCTION", "CC:CAUTION"]),
        (f"{CAUTION_QUOTE} ... publication has been retracted", ["CC:CAUTION"]),
    ],
)
def test_record_sections(quote, expected):
    assert record_sections(quote, TP53_PATH) == expected


def test_record_sections_unlocated_quote_is_none():
    assert record_sections("this sentence is not in the TP53 record", TP53_PATH) is None


def _doc(**item) -> dict:
    return {
        "id": "P04637",
        "gene_symbol": "TP53",
        "core_functions": [
            {"description": "x", "supported_by": [dict(reference_id=TP53, **item)]}
        ],
    }


@pytest.mark.parametrize(
    "item,flagged",
    [
        ({"supporting_text": CAUTION_QUOTE, "record_section": ["CC:CAUTION"]}, False),
        ({"supporting_text": CAUTION_QUOTE}, False),  # absent: nothing to check
        ({"supporting_text": CAUTION_QUOTE, "record_section": ["CC:FUNCTION"]}, True),
        (
            {
                "supporting_text": f"{FUNCTION_QUOTE} ... {CAUTION_QUOTE}",
                "record_section": ["CC:CAUTION"],
            },
            True,
        ),
        # an unlocated quote is left to the verbatim check
        (
            {"supporting_text": "not in the record", "record_section": ["CC:CAUTION"]},
            False,
        ),
    ],
)
def test_record_section_findings(item, flagged):
    findings = record_section_findings(_doc(**item))
    assert bool(findings) == flagged
    if flagged:
        assert findings[0].path == "core_functions[0].supported_by[0]"


def test_record_section_on_non_record_source_is_flagged():
    doc = {
        "references": [
            {
                "id": "file:human/TP53/TP53-notes.md",
                "findings": [
                    {"supporting_text": "x", "record_section": ["CC:CAUTION"]}
                ],
            }
        ]
    }
    findings = record_section_findings(doc)
    assert [f.expected for f in findings] == [None]


def test_validate_gene_review_warns_on_wrong_record_section(tmp_path: Path):
    doc = {
        "id": "P04637",
        "gene_symbol": "TP53",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Tumor suppressor.",
        "references": [
            {
                "id": TP53,
                "title": "UniProt entry",
                "findings": [
                    {
                        "statement": "retracted BANP claim",
                        "supporting_text": CAUTION_QUOTE,
                        "record_section": ["CC:FUNCTION"],
                    }
                ],
            }
        ],
    }
    path = tmp_path / "TP53-ai-review.yaml"
    path.write_text(yaml.safe_dump(doc))
    report = validate_gene_review(path, check_goa=False, check_supporting_text=False)
    issues = [i for i in report.issues if i.check_type == RECORD_SECTION_CHECK]
    assert len(issues) == 1
    assert issues[0].severity == ValidationSeverity.WARNING
    assert "CC:CAUTION" in issues[0].message


SUPPORTED_BY = f"""\
id: P04637
core_functions:
- description: x
  supported_by:
  - reference_id: {TP53}
    supporting_text: >-
      Interaction with BANP was reported to
      enhance phosphorylation on Ser-15
  - reference_id: PMID:123
    supporting_text: not a record
"""

FINDING_FIRST_KEY = f"""\
references:
- id: {TP53}
  findings:
  - supporting_text: '{FUNCTION_QUOTE}'
    statement: function
"""


@pytest.mark.parametrize(
    "text,expected_sections",
    [(SUPPORTED_BY, [["CC:CAUTION"]]), (FINDING_FIRST_KEY, [["CC:FUNCTION"]])],
)
def test_backfill_text_adds_sections_and_preserves_everything_else(
    text, expected_sections
):
    result = backfill_text(text)
    assert result.added == len(expected_sections)
    before, after = yaml.safe_load(text), yaml.safe_load(result.text)
    items = [i for p, r, i in _items(after)]
    assert [i["record_section"] for i in items] == expected_sections
    for i in items:
        del i["record_section"]
    assert after == before
    # only the new lines differ
    assert set(text.splitlines()) <= set(result.text.splitlines()) | {
        line
        for line in text.splitlines()
        if line.lstrip().startswith("- supporting_text")
    }


def test_backfill_text_is_idempotent_and_reports_mismatches():
    once = backfill_text(SUPPORTED_BY).text
    assert backfill_text(once).added == 0
    assert backfill_text(once).text == once
    wrong = once.replace("[CC:CAUTION]", "[CC:FUNCTION]")
    result = backfill_text(wrong)
    assert result.added == 0
    assert result.text == wrong
    assert result.mismatched == 1


def _items(doc):
    from ai_gene_review.validation.local_source_text import iter_local_quote_items

    return [
        (p, r, i)
        for p, r, i in iter_local_quote_items(doc)
        if r.endswith("-uniprot.txt")
    ]


def test_backfill_text_fix_rewrites_wrong_values_only():
    once = backfill_text(SUPPORTED_BY).text
    wrong = once.replace("[CC:CAUTION]", "[CC:FUNCTION]")
    result = backfill_text(wrong, fix=True)
    assert (result.fixed, result.mismatched) == (1, 0)
    assert result.text == once


AOP2 = "file:ARATH/AOP2/AOP2-record-evidence.yaml"
AOP2_PATH = PROJECT_ROOT / "genes" / "ARATH" / "AOP2" / "AOP2-record-evidence.yaml"
AOP2_CAUTION = "5-bp deletion that leads to a non-functional protein"


def test_record_sections_reads_unisave_snapshots():
    """An archived UniProt entry is a database record too."""
    assert record_sections(AOP2_CAUTION, AOP2_PATH) == ["CC:CAUTION"]
    doc = {
        "core_functions": [
            {
                "supported_by": [
                    {
                        "reference_id": AOP2,
                        "supporting_text": AOP2_CAUTION,
                        "record_section": ["CC:CAUTION"],
                    }
                ]
            }
        ]
    }
    assert record_section_findings(doc) == []
    text = f"core_functions:\n- supported_by:\n  - reference_id: {AOP2}\n    supporting_text: {AOP2_CAUTION}\n"
    result = backfill_text(text)
    assert result.added == 1
    assert "record_section: [CC:CAUTION]" in result.text


def test_ambiguous_quote_gets_no_section():
    """'Nucleus' is both a keyword and a subcellular location: the section is not established."""
    assert locate_sections("Nucleus", TP53_PATH) == (AMBIGUOUS, [])
    assert record_sections("Nucleus", TP53_PATH) is None
    text = f"core_functions:\n- supported_by:\n  - reference_id: {TP53}\n    supporting_text: Nucleus\n"
    result = backfill_text(text)
    assert (result.added, result.ambiguous) == (0, 1)
    assert result.text == text
    # and a stated value on such a quote is not second-guessed
    assert (
        record_section_findings(_doc(supporting_text="Nucleus", record_section=["KW"]))
        == []
    )


@pytest.mark.parametrize(
    "stated",
    [
        # block sequence: the value does not start on the key's line
        "record_section:\n    - CC:FUNCTION\n    - CC:CAUTION\n",
        # flow sequence wrapped over two lines
        "record_section: [CC:FUNCTION,\n      CC:CAUTION]\n",
        # trailing comment would be lost
        "record_section: [CC:FUNCTION]  # checked\n",
    ],
)
def test_fix_leaves_values_it_cannot_rewrite_on_one_line(stated):
    text = (
        f"core_functions:\n- supported_by:\n  - reference_id: {TP53}\n"
        f"    {stated}    supporting_text: {CAUTION_QUOTE}\n"
    )
    result = backfill_text(text, fix=True)
    assert (result.fixed, result.mismatched) == (0, 1)
    assert result.text == text


CEM1_PATH = PROJECT_ROOT / "genes" / "SCHPO" / "cem1" / "cem1-uniprot.txt"


@pytest.mark.parametrize(
    "quote,expected",
    [
        # a feature key with a single position: nothing searchable is left after
        # normalisation, so it is matched against the parsed features
        ("FT   ACT_SITE        170", (LOCATED, ["FT:ACT_SITE"])),
        ("FT   ACT_SITE 311", (LOCATED, ["FT:ACT_SITE"])),
        # the key exists but not at that position
        ("FT   ACT_SITE        999", (UNLOCATED, [])),
        # a bare number cannot be attributed to any section
        ("170", (UNSEARCHABLE, [])),
    ],
)
def test_single_position_feature_quotes(quote, expected):
    assert locate_sections(quote, CEM1_PATH) == expected


def test_backfill_counts_an_aliased_quote_once():
    """A quote reused through a YAML alias gets one inserted line and one count."""
    text = (
        "core_functions:\n"
        "- supported_by:\n"
        f"  - &q\n    reference_id: {TP53}\n    supporting_text: {CAUTION_QUOTE}\n"
        "- supported_by:\n"
        "  - *q\n"
    )
    result = backfill_text(text)
    assert result.added == 1
    assert result.text.count("record_section:") == 1
    after = yaml.safe_load(result.text)
    assert [
        c["supported_by"][0]["record_section"] for c in after["core_functions"]
    ] == [
        ["CC:CAUTION"],
        ["CC:CAUTION"],
    ]


@pytest.mark.parametrize(
    "quote,path,expected",
    [
        # a feature key quoted without the FT line code
        ("TRANSIT         1..64", "yeast/ALT1/ALT1-uniprot.txt", ["FT:TRANSIT"]),
        ("ZN_FING         290..371", "SCHPO/pli1/pli1-uniprot.txt", ["FT:ZN_FING"]),
        ("CHAIN           1..316", "SCHPO/cab4/cab4-uniprot.txt", ["FT:CHAIN"]),
        # ... followed by a qualifier of the same feature
        (
            'BINDING         572..580 /ligand="ATP"',
            "SCHPO/ppk18/ppk18-uniprot.txt",
            ["FT:BINDING"],
        ),
        ("FT   TRANSIT         1..18", "SCHPO/cem1/cem1-uniprot.txt", ["FT:TRANSIT"]),
    ],
)
def test_feature_quotes_with_or_without_line_code(quote, path, expected):
    assert record_sections(quote, PROJECT_ROOT / "genes" / path) == expected


def test_feature_quote_with_a_qualifier_of_another_feature_is_not_located():
    path = PROJECT_ROOT / "genes" / "SCHPO" / "ppk18" / "ppk18-uniprot.txt"
    assert locate_sections('BINDING         572..580 /ligand="GTP"', path) == (
        UNLOCATED,
        [],
    )


def test_multiline_feature_quote_with_qualifiers():
    """A feature quoted with its continuation lines, as copied from the flat file."""
    path = PROJECT_ROOT / "genes" / "SCHPO" / "plo1" / "plo1-uniprot.txt"
    quote = 'FT   BINDING         47..55\nFT                   /ligand="ATP"'
    assert record_sections(quote, path) == ["FT:BINDING"]


def test_quote_spanning_two_features():
    path = PROJECT_ROOT / "genes" / "human" / "LRP2BP" / "LRP2BP-uniprot.txt"
    quote = 'FT   REPEAT          59..92\nFT                   /note="TPR"\nFT   REPEAT          93..125\n'
    assert record_sections(quote, path) == ["FT:REPEAT"]


def test_signal_peptide_quote_is_the_feature_not_the_keyword():
    """'SIGNAL 1..18' once matched across the KW line and the first feature."""
    path = PROJECT_ROOT / "genes" / "human" / "ADM5" / "ADM5-uniprot.txt"
    assert record_sections("SIGNAL          1..18", path) == ["FT:SIGNAL"]
