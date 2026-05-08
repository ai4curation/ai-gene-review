"""Tests for PN mapping candidate suggestion heuristics."""

from pathlib import Path

from ai_gene_review.tools.report_pn_mapping_coverage import PNCodeRecord
from ai_gene_review.tools.report_pn_mapping_suggestions import (
    GOTerm,
    build_go_indexes,
    load_go_terms,
    rank_candidates_for_record,
)


def _term(curie: str, label: str) -> GOTerm:
    return GOTerm(
        curie=curie,
        label=label,
        normalized_label=label.lower(),
        tokens=frozenset(label.lower().split()),
    )


def test_rank_candidates_prefers_exact_alias_match() -> None:
    record = PNCodeRecord(
        level="type",
        code=(
            "Autophagy-Lysosome Pathway|Autophagy substrate selection|"
            "Selective autophagy receptor|ERphagy"
        ),
        branch="Autophagy-Lysosome Pathway",
        class_name="Autophagy substrate selection",
        group="Selective autophagy receptor",
        type_name="ERphagy",
        subtype="",
    )
    terms = [
        _term("GO:0061709", "reticulophagy"),
        _term("GO:0006914", "autophagy"),
    ]
    term_list, token_index, label_index = build_go_indexes(terms)

    ranked = rank_candidates_for_record(record, term_list, token_index, label_index)

    assert ranked
    assert ranked[0].term.curie == "GO:0061709"
    assert ranked[0].basis == "exact_alias_label"


def test_rank_candidates_prefers_exact_component_label() -> None:
    record = PNCodeRecord(
        level="type",
        code=(
            "Translation|Cytosolic translation|Translation initiation|"
            "eIF2 complex"
        ),
        branch="Translation",
        class_name="Cytosolic translation",
        group="Translation initiation",
        type_name="eIF2 complex",
        subtype="",
    )
    terms = [
        _term(
            "GO:0005850",
            "eukaryotic translation initiation factor 2 complex",
        ),
        _term("GO:0005852", "eukaryotic translation initiation factor 3 complex"),
    ]
    term_list, token_index, label_index = build_go_indexes(terms)

    ranked = rank_candidates_for_record(record, term_list, token_index, label_index)

    assert ranked
    assert ranked[0].term.curie == "GO:0005850"
    assert ranked[0].basis in {"exact_alias_label", "strong_lexical"}


def test_load_go_terms_reads_local_cache_shape(tmp_path: Path) -> None:
    cache_path = tmp_path / "go.tsv"
    cache_path.write_text(
        "\n".join(
            [
                "term_id\tlabel\tis_obsolete\tfetched_date",
                "GO:0005850\teukaryotic translation initiation factor 2 complex\tfalse\t2026-03-22",
                "GO:9999999\tobsolete fake term\ttrue\t2026-03-22",
            ]
        ),
        encoding="utf-8",
    )

    terms = load_go_terms(cache_path)

    assert len(terms) == 1
    assert terms[0].curie == "GO:0005850"
    assert terms[0].label == "eukaryotic translation initiation factor 2 complex"
