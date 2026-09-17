"""Tests for the file: supporting_text verbatim check."""

from pathlib import Path

from ai_gene_review.validation.file_supporting_text import (
    check_file_supporting_text,
    looks_like_narration,
    quote_is_present,
    _source_variants,
)

UNIPROT = (
    "DE   RecName: Full=Urease subunit alpha;\n"
    "DE            EC=3.5.1.5;\n"
    "CC   catalyze the primary light-\n"
    "CC   induced photochemical processes\n"
)


def _uniprot(tmp_path: Path) -> list[str]:
    p = tmp_path / "x-uniprot.txt"
    p.write_text(UNIPROT, encoding="utf-8")
    return _source_variants(p)


def test_trailing_punctuation_is_tolerated(tmp_path):
    # Source ends the line with ';', the curator typed '.'
    assert quote_is_present(
        "RecName: Full=Urease subunit alpha; EC=3.5.1.5.", _uniprot(tmp_path)
    )


def test_uniprot_line_prefix_either_way(tmp_path):
    body = _uniprot(tmp_path)
    assert quote_is_present("DE RecName: Full=Urease subunit alpha;", body)
    assert quote_is_present("RecName: Full=Urease subunit alpha;", body)


def test_word_hyphenated_across_a_line_break(tmp_path):
    assert quote_is_present(
        "the primary light-induced photochemical", _uniprot(tmp_path)
    )


def test_ellipsis_marks_elision_and_respects_order(tmp_path):
    body = _uniprot(tmp_path)
    assert quote_is_present("RecName: Full=Urease ... EC=3.5.1.5", body)
    # Reversed order must not match, even across the prefixed/stripped variants.
    assert not quote_is_present("EC=3.5.1.5 ... RecName: Full=Urease", body)


def test_absent_text_is_rejected(tmp_path):
    assert not quote_is_present("purple elephant transporter", _uniprot(tmp_path))


def test_narration_detected_but_real_quotes_are_not():
    assert looks_like_narration("Falcon synthesis supports MTCH2 as an insertase")
    assert looks_like_narration("Falcon report summarizes ABI1 as a clade A PP2C")
    assert not looks_like_narration(
        "we have demonstrated that MTCH2 is a defining member of a family"
    )


def test_check_flags_narration_and_missing_file(tmp_path):
    (tmp_path / "genes").mkdir()
    src = tmp_path / "genes" / "g-deep-research-falcon.md"
    src.write_text("MTCH2 is a defining member of a family of insertases.\n")
    data = {
        "existing_annotations": [
            {
                "review": {
                    "supported_by": [
                        {
                            "reference_id": "file:g-deep-research-falcon.md",
                            "supporting_text": "Falcon synthesis supports MTCH2 as an insertase",
                        },
                        {
                            "reference_id": "file:g-deep-research-falcon.md",
                            "supporting_text": "MTCH2 is a defining member of a family",
                        },
                        {
                            "reference_id": "file:nope/missing.md",
                            "supporting_text": "anything",
                        },
                    ]
                }
            }
        ]
    }
    res = check_file_supporting_text(data, tmp_path, genes_root=tmp_path / "genes")
    assert res.checked == 3
    kinds = sorted(i.kind for i in res.issues)
    assert kinds == ["missing_file", "narration"]
