"""Tests for the evidence-subtraction reporting engine.

These unit tests inject a small fake ancestor function so they exercise the
closure logic without loading a real ontology. A separate integration test
(marked) builds the OAK-backed GO closure.
"""

import pytest

from ai_gene_review.analysis.subtraction_report import (
    CORE_FUNCTION_TERM_SLOTS,
    SubtractionFilter,
    SubtractionReporter,
    core_function_rows,
    lost_annotation_rows,
    render_markdown,
    summarize,
    write_tsv_reports,
)


# Fake reflexive ancestor hierarchy:
#   GO:0002 (specific MF) is_a GO:0001 (general MF)
#   GO:0101 (mitochondrion) part_of GO:0100 (cytoplasm)
#   GO:0200 stands alone (used for an unsupported core term)
_ANCESTORS = {
    "GO:0001": {"GO:0001"},
    "GO:0002": {"GO:0002", "GO:0001"},
    "GO:0100": {"GO:0100"},
    "GO:0101": {"GO:0101", "GO:0100"},
    "GO:0200": {"GO:0200"},
}


def fake_ancestors(term: str) -> set:
    return _ANCESTORS.get(term, {term})


def _term(tid, label=None):
    return {"id": tid, "label": label or tid}


@pytest.fixture
def review():
    """A small review exercising closure in both directions.

    - GO:0002 specific MF, IBA  (subtracted; no survivor covers it)
    - GO:0001 general MF, IDA   (survives; does NOT cover specific GO:0002)
    - GO:0100 cytoplasm, IBA    (subtracted; survivor GO:0101 covers it)
    - GO:0101 mitochondrion, IDA (survives; covers GO:0100 via part_of)

    core_functions: MF GO:0002, locations [GO:0100, GO:0200]
    """
    return {
        "id": "P12345",
        "gene_symbol": "TESTG",
        "existing_annotations": [
            {
                "term": _term("GO:0002", "specific activity"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
            {
                "term": _term("GO:0001", "general activity"),
                "evidence_type": "IDA",
                "original_reference_id": "PMID:1",
                "review": {"action": "ACCEPT"},
            },
            {
                "term": _term("GO:0100", "cytoplasm"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
            {
                "term": _term("GO:0101", "mitochondrion"),
                "evidence_type": "IDA",
                "original_reference_id": "PMID:2",
                "review": {"action": "ACCEPT"},
            },
        ],
        "core_functions": [
            {
                "description": "core",
                "molecular_function": _term("GO:0002", "specific activity"),
                "locations": [_term("GO:0100", "cytoplasm"), _term("GO:0200", "novel")],
            }
        ],
    }


@pytest.fixture
def reporter():
    return SubtractionReporter(ancestors=fake_ancestors)


def test_filter_requires_some_criterion():
    with pytest.raises(ValueError):
        SubtractionFilter()


def test_filter_matches_evidence_and_reference():
    f = SubtractionFilter.create(evidence_codes=["IBA"])
    assert f.matches({"evidence_type": "IBA"})
    assert not f.matches({"evidence_type": "IDA"})

    f2 = SubtractionFilter.create(reference_ids=["GO_REF:0000033"])
    assert f2.matches({"original_reference_id": "GO_REF:0000033"})
    assert not f2.matches({"original_reference_id": "PMID:1"})


def test_filter_mode_all_requires_both():
    f = SubtractionFilter.create(
        reference_ids=["GO_REF:0000033"], evidence_codes=["IBA"], mode="all"
    )
    assert f.matches(
        {"original_reference_id": "GO_REF:0000033", "evidence_type": "IBA"}
    )
    assert not f.matches(
        {"original_reference_id": "GO_REF:0000033", "evidence_type": "IDA"}
    )


def test_filter_complement_inverts_match():
    """complement=True subtracts everything that does NOT match (keep-only)."""
    f = SubtractionFilter.create(evidence_codes=["IBA"], complement=True)
    assert not f.matches({"evidence_type": "IBA"})  # IBA is kept
    assert f.matches({"evidence_type": "IDA"})  # everything else subtracted
    assert f.matches({"evidence_type": None})
    assert "except" in f.describe().lower()


def test_keep_only_iba_loses_experimental_core_function(reporter):
    """Keeping only IBA: a non-IBA-grounded MF core function becomes LOST."""
    review = {
        "id": "P1",
        "gene_symbol": "G",
        "existing_annotations": [
            {
                "term": _term("GO:0002", "specific"),
                "evidence_type": "IDA",
                "original_reference_id": "PMID:1",
                "review": {"action": "ACCEPT"},
            },
            {
                "term": _term("GO:0100", "cytoplasm"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
        ],
        "core_functions": [
            {
                "description": "c",
                "molecular_function": _term("GO:0002"),
                "locations": [_term("GO:0100")],
            }
        ],
    }
    filt = SubtractionFilter.create(evidence_codes=["IBA"], complement=True)
    result = reporter.analyze_review(review, filt)

    # The experimental MF GO:0002 is subtracted (non-IBA) -> grounded only by it
    cov = {(c.slot, c.term_id): c for c in result.core_function_coverage}
    assert cov[("molecular_function", "GO:0002")].status == "LOST"
    # The IBA-grounded location survives
    assert cov[("locations", "GO:0100")].status == "RETAINED"
    # The endorsed experimental annotation is the loss
    assert [la.term_id for la in result.lost_annotations] == ["GO:0002"]


def test_subtract_iba_lost_annotations(review, reporter):
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)

    assert result.n_total_annotations == 4
    assert result.n_subtracted == 2

    lost = {la.term_id: la for la in result.lost_annotations}
    assert set(lost) == {"GO:0002", "GO:0100"}

    # GO:0002 specific MF: only general GO:0001 survives -> not covered -> unique loss
    assert lost["GO:0002"].redundant is False
    assert lost["GO:0002"].covered_by == ()

    # GO:0100 cytoplasm: surviving GO:0101 (mitochondrion) covers it via closure
    assert lost["GO:0100"].redundant is True
    assert lost["GO:0100"].covered_by == ("GO:0101",)

    assert result.n_uniquely_lost == 1


def test_subtract_iba_core_function_coverage(review, reporter):
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)

    cov = {(c.slot, c.term_id): c for c in result.core_function_coverage}

    # MF GO:0002 was grounded only by the subtracted IBA -> LOST
    mf = cov[("molecular_function", "GO:0002")]
    assert mf.status == "LOST"
    assert mf.subtracted_support == ("GO:0002",)

    # location GO:0100 still grounded by surviving GO:0101 -> RETAINED
    loc = cov[("locations", "GO:0100")]
    assert loc.status == "RETAINED"
    assert loc.retained_support == ("GO:0101",)

    # GO:0200 never grounded by any annotation -> UNSUPPORTED
    novel = cov[("locations", "GO:0200")]
    assert novel.status == "UNSUPPORTED"

    assert result.n_core_terms_lost == 1


def test_subtract_by_reference_id(review, reporter):
    filt = SubtractionFilter.create(reference_ids=["GO_REF:0000033"])
    result = reporter.analyze_review(review, filt)
    # Same two GO_REF:0000033/IBA annotations selected as by evidence code
    assert {la.term_id for la in result.lost_annotations} == {"GO:0002", "GO:0100"}


def test_modify_replacement_term_grounds_core_function(reporter):
    """A surviving MODIFY annotation grounds via its replacement term."""
    review = {
        "id": "P1",
        "gene_symbol": "G",
        "existing_annotations": [
            {
                "term": _term("GO:0001"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
            {
                # survives; MODIFY redirects general -> specific GO:0002
                "term": _term("GO:0001"),
                "evidence_type": "IDA",
                "original_reference_id": "PMID:1",
                "review": {
                    "action": "MODIFY",
                    "proposed_replacement_terms": [_term("GO:0002")],
                },
            },
        ],
        "core_functions": [
            {"description": "c", "molecular_function": _term("GO:0002")}
        ],
    }
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    mf = result.core_function_coverage[0]
    assert mf.status == "RETAINED"
    assert mf.retained_support == ("GO:0002",)


def test_negated_annotation_not_counted(reporter):
    review = {
        "id": "P1",
        "gene_symbol": "G",
        "existing_annotations": [
            {
                "term": _term("GO:0002"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "negated": True,
                "review": {"action": "ACCEPT"},
            }
        ],
        "core_functions": [],
    }
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    # negated annotation is not reported as a lost endorsement
    assert result.lost_annotations == []
    assert result.n_subtracted == 1


def test_excluded_branch_skips_terms():
    """exclude_branches drops core terms / lost annotations under a branch."""
    # GO:0500 is a 'binding' root; GO:0002 is_a GO:0500.
    anc = {
        "GO:0500": {"GO:0500"},
        "GO:0002": {"GO:0002", "GO:0500"},
        "GO:0100": {"GO:0100"},
    }

    def ancestors(t):
        return anc.get(t, {t})

    reporter = SubtractionReporter(
        ancestors=ancestors, exclude_branches=frozenset({"GO:0500"})
    )
    review = {
        "id": "P1",
        "gene_symbol": "G",
        "existing_annotations": [
            {
                "term": _term("GO:0002", "a binding term"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
            {
                "term": _term("GO:0100", "an activity"),
                "evidence_type": "IBA",
                "original_reference_id": "GO_REF:0000033",
                "review": {"action": "ACCEPT"},
            },
        ],
        "core_functions": [
            {
                "description": "c",
                "molecular_function": _term("GO:0002"),  # binding -> excluded
                "directly_involved_in": [_term("GO:0100")],
            }
        ],
    }
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)

    # The binding term GO:0002 is excluded from both reports.
    assert all(la.term_id != "GO:0002" for la in result.lost_annotations)
    assert all(c.term_id != "GO:0002" for c in result.core_function_coverage)
    # The non-binding activity term is still reported.
    assert any(la.term_id == "GO:0100" for la in result.lost_annotations)
    assert any(c.term_id == "GO:0100" for c in result.core_function_coverage)


def test_no_closure_means_exact_match_only(review):
    """Without an ancestor function, GO:0100 is no longer covered by GO:0101."""
    reporter = SubtractionReporter()  # identity ancestors
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    lost = {la.term_id: la for la in result.lost_annotations}
    assert lost["GO:0100"].redundant is False  # closure off -> not covered
    cov = {(c.slot, c.term_id): c for c in result.core_function_coverage}
    assert cov[("locations", "GO:0100")].status == "LOST"


def test_rows_and_summary(review, reporter):
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    summary = summarize([result], filt)
    assert summary["n_subtracted_annotations"] == 2
    assert summary["n_lost_endorsed"] == 2
    assert summary["n_lost_endorsed_unique"] == 1
    assert summary["n_lost_endorsed_redundant"] == 1
    assert summary["core_function_status_counts"] == {
        "RETAINED": 1,
        "LOST": 1,
        "UNSUPPORTED": 1,
    }

    lost_rows = lost_annotation_rows([result])
    assert len(lost_rows) == 2
    assert {r["loss_status"] for r in lost_rows} == {"UNIQUE", "REDUNDANT"}

    cf_rows = core_function_rows([result])
    assert len(cf_rows) == 3


def test_render_markdown_contains_key_sections(review, reporter):
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    md = render_markdown([result], filt)
    assert "Evidence subtraction report" in md
    assert "TESTG" in md
    assert "GO:0002" in md  # uniquely lost term shows in detail


def test_write_tsv_reports(review, reporter, tmp_path):
    filt = SubtractionFilter.create(evidence_codes=["IBA"])
    result = reporter.analyze_review(review, filt)
    lost_path, cf_path = write_tsv_reports([result], tmp_path / "iba")
    assert lost_path.exists() and cf_path.exists()
    lost_text = lost_path.read_text()
    assert "loss_status" in lost_text
    assert "GO:0002" in lost_text
    cf_text = cf_path.read_text()
    assert "status" in cf_text


def test_core_function_slots_constant():
    # Guard against accidental drift from the schema's GO-bearing slots.
    assert CORE_FUNCTION_TERM_SLOTS == (
        "molecular_function",
        "contributes_to_molecular_function",
        "directly_involved_in",
        "locations",
        "in_complex",
    )


@pytest.mark.integration
def test_go_ancestor_fn_real_closure():
    """Smoke test the OAK-backed closure on a known is_a/part_of pair."""
    from ai_gene_review.analysis.subtraction_report import make_go_ancestor_fn

    ancestors = make_go_ancestor_fn()
    # mitochondrion (GO:0005739) is part_of intracellular anatomical structure;
    # cytoplasm (GO:0005737) is a part_of ancestor of mitochondrion.
    anc = ancestors("GO:0005739")
    assert "GO:0005739" in anc  # reflexive
    assert "GO:0005737" in anc  # cytoplasm via part_of closure
