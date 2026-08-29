"""Tests for deterministic residue-site validation of family reviews.

The point of the validator is to *contradict* a wrong claim, so most of these tests assert
failures. The sequence source is a local stub so the logic tests are deterministic and
offline; a separate integration test exercises the real UniProt fetch.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.family_residue_validator import (
    Outcome,
    SequenceCache,
    check_anchor_residues,
    check_controls,
    summarize,
    validate_family_review,
)


class StubCache:
    """Serves sequences from a dict instead of UniProt."""

    def __init__(self, seqs: dict[str, str]):
        self.seqs = seqs

    def get(self, accession: str) -> str:
        return self.seqs[accession.split(":")[-1]]


# A 12-residue toy protein:  positions 1..12
#                            1234567890 12
TOY = "MACDEFGHIKLC"
CACHE = StubCache({"P00001": TOY})


def _review(residues, *, motif=None, strength="REQUIRED", pos_ctl=None, neg_ctl=None):
    """Build a minimal family review dict around one residue site."""
    site = {
        "site_id": "test_site",
        "anchor": {"id": "UniProtKB:P00001"},
        "site_source": "UNIPROT_FEATURE",
        "residues": residues,
        "required_for": [
            {
                "term": {"id": "GO:0008745", "label": "x"},
                "strength": strength,
                "rationale": "test",
            }
        ],
        "positive_controls": pos_ctl if pos_ctl is not None else [{"id": "UniProtKB:P00002"}],
        "negative_controls": neg_ctl if neg_ctl is not None else [{"id": "UniProtKB:P00003"}],
    }
    if motif:
        site["motif"] = motif
    return {"family_id": "PANTHER:PTHR00001", "residue_sites": [site]}


@pytest.mark.parametrize(
    "position,expected,outcome",
    [
        (2, ["A"], Outcome.PASS),        # M-A-C-D... position 2 is A
        (3, ["C"], Outcome.PASS),
        (12, ["C"], Outcome.PASS),       # last residue
        (3, ["C", "U"], Outcome.PASS),   # multivalued: Sec-or-Cys style site
        (3, ["S"], Outcome.FAIL),        # wrong residue -- the core catch
        (2, ["C"], Outcome.FAIL),        # off-by-one style error
        (13, ["C"], Outcome.FAIL),       # beyond end of sequence
        (99, ["C"], Outcome.FAIL),       # invented position
    ],
)
def test_anchor_residue_outcomes(position, expected, outcome):
    """A curated position is checked against the anchor's actual sequence."""
    review = _review([{"position": position, "expected": expected}])
    results = check_anchor_residues(review, CACHE)
    assert len(results) == 1
    assert results[0].outcome is outcome
    assert results[0].observed == (TOY[position - 1] if position <= len(TOY) else None)


def test_wrong_residue_message_is_actionable():
    """A failure says what was expected and what is actually there."""
    review = _review([{"position": 3, "expected": ["S"]}])
    (result,) = check_anchor_residues(review, CACHE)
    assert result.outcome is Outcome.FAIL
    assert "expected S" in result.message
    assert "found C" in result.message


def test_site_without_any_anchor_is_unresolved_not_failed():
    """An incomplete claim is not the same as a contradicted one."""
    review = {
        "family_id": "PANTHER:PTHR00001",
        "residue_sites": [
            {"site_id": "s", "site_source": "UNIPROT_FEATURE",
             "residues": [{"position": 1, "expected": ["M"]}]}
        ],
    }
    (result,) = check_anchor_residues(review, CACHE)
    assert result.outcome is Outcome.UNRESOLVED


def test_falls_back_to_family_reference_protein():
    """A site with no anchor of its own uses the family reference_protein."""
    review = {
        "family_id": "PANTHER:PTHR00001",
        "reference_protein": {"id": "UniProtKB:P00001"},
        "residue_sites": [
            {"site_id": "s", "site_source": "UNIPROT_FEATURE",
             "residues": [{"position": 1, "expected": ["M"]}]}
        ],
    }
    (result,) = check_anchor_residues(review, CACHE)
    assert result.outcome is Outcome.PASS


@pytest.mark.parametrize(
    "pattern,start,end,outcome",
    [
        ("C..C", 3, 6, Outcome.FAIL),     # positions 3-6 are C,D,E,F
        ("CDEF", 3, 6, Outcome.PASS),
        ("C.{8}C", 3, 12, Outcome.PASS),  # C at 3 and C at 12, 8 between
        ("C..C", 3, 99, Outcome.FAIL),    # out of range
    ],
)
def test_motif_block_checking(pattern, start, end, outcome):
    """A CXXC-style block requirement is matched against the anchor sequence."""
    review = _review([], motif={"pattern_regex": pattern, "start": start, "end": end})
    results = check_anchor_residues(review, CACHE)
    assert results[-1].outcome is outcome


def test_required_site_without_controls_fails():
    """REQUIRED is the only strength that can contradict a gene review, so it needs controls."""
    review = _review([{"position": 1, "expected": ["M"]}], pos_ctl=[], neg_ctl=[])
    (result,) = check_controls(review, CACHE)
    assert result.outcome is Outcome.FAIL
    assert "needs both positive and negative controls" in result.message


def test_weaker_strength_does_not_require_controls():
    """ASSOCIATED records an observation and should not be held to the same bar."""
    review = _review(
        [{"position": 1, "expected": ["M"]}], strength="ASSOCIATED", pos_ctl=[], neg_ctl=[]
    )
    (result,) = check_controls(review, CACHE)
    assert result.outcome is Outcome.PASS


def test_protein_listed_as_both_control_types_fails():
    """Catches the mislabelled-control error that makes real enzymes look degenerate."""
    review = _review(
        [{"position": 1, "expected": ["M"]}],
        pos_ctl=[{"id": "UniProtKB:P00009"}],
        neg_ctl=[{"id": "UniProtKB:P00009"}],
    )
    (result,) = check_controls(review, CACHE)
    assert result.outcome is Outcome.FAIL
    assert "both positive and negative" in result.message


def test_summarize_counts_outcomes():
    review = _review(
        [{"position": 3, "expected": ["C"]}, {"position": 3, "expected": ["S"]}]
    )
    counts = summarize(check_anchor_residues(review, CACHE))
    assert counts == {"PASS": 1, "FAIL": 1, "UNRESOLVED": 0}


def test_sequence_cache_writes_and_reads_disk(tmp_path):
    """A cached sequence is reused without refetching."""
    cache = SequenceCache(tmp_path)
    (tmp_path / "P12345.seq").write_text("MACDEF")
    assert cache.get("UniProtKB:P12345") == "MACDEF"
    assert cache.get("P12345") == "MACDEF"


@pytest.mark.integration
def test_real_pgrp_family_review_validates():
    """The committed PGRP family review checks out against real UniProt sequences."""
    path = Path("interpro/panther/PTHR11022/PTHR11022-review.yaml")
    results = validate_family_review(path, Path(".cache/uniprot_seq"))
    failures = [r for r in results if r.outcome is Outcome.FAIL]
    assert not failures, f"unexpected failures: {[str(f) for f in failures]}"
    assert summarize(results)["PASS"] >= 4


@pytest.mark.integration
@pytest.mark.parametrize(
    "field,value",
    [
        ("position", 413),      # PGLYRP2 413 is Y, not H
        ("expected", ["W"]),    # no tryptophan at 410
    ],
)
def test_validator_catches_a_deliberately_wrong_claim(tmp_path, field, value):
    """Corrupting a curated claim makes the validator fail -- the property that matters."""
    src = Path("interpro/panther/PTHR11022/PTHR11022-review.yaml")
    review = yaml.safe_load(src.read_text())
    review["residue_sites"][0]["residues"][0][field] = value
    bad = tmp_path / "bad-review.yaml"
    bad.write_text(yaml.safe_dump(review))
    results = validate_family_review(bad, Path(".cache/uniprot_seq"))
    assert any(r.outcome is Outcome.FAIL for r in results)


def test_tandem_residues_hide_off_by_one_errors():
    """Documents a real blind spot: identity checking cannot see a shift within a repeat.

    PGLYRP2 carries a tandem His pair at 410-411, so citing 411 for the zinc ligand at 410
    still finds a histidine and passes. Residue-identity validation catches invented and
    wrong-residue positions; it cannot catch an off-by-one inside a run of the same amino
    acid. Only alignment- or structure-level checking distinguishes those.
    """
    cache = StubCache({"P00001": "MAHHKL"})   # tandem H at 3 and 4
    for position in (3, 4):
        review = {
            "family_id": "PANTHER:PTHR00001",
            "reference_protein": {"id": "UniProtKB:P00001"},
            "residue_sites": [
                {"site_id": "s", "site_source": "UNIPROT_FEATURE",
                 "residues": [{"position": position, "expected": ["H"]}]}
            ],
        }
        (result,) = check_anchor_residues(review, cache)
        assert result.outcome is Outcome.PASS


# --------------------------------------------------------------------------
# Node assessments: PTN claims checked against cached PAINT rows
# --------------------------------------------------------------------------


class FakePaintRow:
    """Stand-in for module_validator.PaintAnnotationRow."""

    def __init__(self, family: str, go_id: str):
        self.family = family
        self.go_id = go_id


PAINT = {
    "PANTHER:PTN000001": [
        FakePaintRow("PTHR00001", "GO:0008745"),
        FakePaintRow("PTHR00001", "GO:0016019"),
    ],
    # a node shared across families, as 283 real ones are
    "PANTHER:PTN000999": [FakePaintRow("PTHR99999", "GO:0008168")],
}


def _node_review(node, term, family="PANTHER:PTHR00001"):
    return {
        "family_id": family,
        "node_assessments": [
            {
                "node_id": node,
                "asserted_term": {"id": term, "label": "x"},
                "assessment": "SOUND",
                "assessment_reason": "test",
            }
        ],
    }


@pytest.mark.parametrize(
    "node,term,outcome,fragment",
    [
        ("PANTHER:PTN000001", "GO:0008745", Outcome.PASS, "PAINT records"),
        ("PANTHER:PTN000001", "GO:0016019", Outcome.PASS, "PAINT records"),
        # term not asserted at that node -- the invented-pairing case
        ("PANTHER:PTN000001", "GO:0004672", Outcome.FAIL, "does not record"),
        # node absent entirely -- the invented-node case
        ("PANTHER:PTN123456", "GO:0008745", Outcome.FAIL, "not found in any cached"),
        # node exists but under a different family -- PTNs are not family-unique
        ("PANTHER:PTN000999", "GO:0008168", Outcome.FAIL, "belongs to"),
    ],
)
def test_node_assessment_outcomes(node, term, outcome, fragment):
    """A node/term pairing is checked against the family's own PAINT rows."""
    from ai_gene_review.validation.family_residue_validator import check_node_assessments

    (result,) = check_node_assessments(_node_review(node, term), PAINT)
    assert result.outcome is outcome
    assert fragment in result.message


def test_cross_family_node_names_the_real_family():
    """The failure message tells the curator which family the node actually belongs to."""
    from ai_gene_review.validation.family_residue_validator import check_node_assessments

    (result,) = check_node_assessments(
        _node_review("PANTHER:PTN000999", "GO:0008168"), PAINT
    )
    assert "PTHR99999" in result.message


@pytest.mark.integration
def test_real_pgrp_node_assessments_check_out():
    """The committed PGRP node assessments match the cached PAINT slice."""
    results = validate_family_review(
        Path("interpro/panther/PTHR11022/PTHR11022-review.yaml"),
        Path(".cache/uniprot_seq"),
    )
    node_results = [r for r in results if r.accession.startswith("GO:")]
    assert len(node_results) == 2
    assert all(r.outcome is Outcome.PASS for r in node_results)


# --------------------------------------------------------------------------
# RESIDUE_DETERMINED term assessments must point at a real site
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "site,outcome",
    [("real_site", Outcome.PASS), ("no_such_site", Outcome.FAIL)],
)
def test_determined_by_site_must_resolve(site, outcome):
    """A RESIDUE_DETERMINED pointer that names no site is a dangling reference."""
    from ai_gene_review.validation.family_residue_validator import (
        check_term_assessment_site_refs,
    )

    review = {
        "family_id": "PANTHER:PTHR00001",
        "residue_sites": [{"site_id": "real_site"}],
        "term_assessments": [
            {
                "assessed_term": {"id": "GO:1", "label": "x"},
                "scope": "RESIDUE_DETERMINED",
                "determined_by_site": site,
            }
        ],
    }
    (result,) = check_term_assessment_site_refs(review)
    assert result.outcome is outcome


def test_non_residue_determined_assessments_are_ignored():
    from ai_gene_review.validation.family_residue_validator import (
        check_term_assessment_site_refs,
    )

    review = {
        "family_id": "PANTHER:PTHR00001",
        "term_assessments": [
            {"assessed_term": {"id": "GO:1"}, "scope": "FAMILY_WIDE"}
        ],
    }
    assert check_term_assessment_site_refs(review) == []


@pytest.mark.integration
def test_real_sephs_family_review_validates():
    """The SEPHS family review, including its RESIDUE_DETERMINED scoping."""
    results = validate_family_review(
        Path("interpro/panther/PTHR10256/PTHR10256-review.yaml"),
        Path(".cache/uniprot_seq"),
    )
    failures = [r for r in results if r.outcome is Outcome.FAIL]
    assert not failures, [str(f) for f in failures]
