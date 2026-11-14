"""Tests for the Schnoes-style trusted-cutoff check of enzyme annotations."""

import pytest

from ai_gene_review.validation.enzyme_family_cutoff import (
    FamilyScore,
    check,
    classify_hit,
    is_complete_ec,
    verdict_for,
)

TC = (300.0, 300.0)
NC = (200.0, 200.0)


def score(
    seq: float | None,
    *,
    target: bool = True,
    family_type: str = "equivalog",
    acc: str = "TIGR00001.1",
) -> FamilyScore:
    """A FamilyScore whose domain score equals its sequence score."""
    return FamilyScore(
        accession=acc,
        product_name=f"family {acc}",
        family_type=family_type,
        ec_numbers=[],
        go_terms=[],
        is_target=target,
        seq_score=seq,
        dom_score=seq,
        tc=TC,
        nc=NC,
    )


@pytest.mark.parametrize(
    "seq,dom,expected",
    [
        (None, None, "NO_HIT"),
        (350.0, 350.0, "ABOVE_TC"),
        (300.0, 300.0, "ABOVE_TC"),
        # --cut_tc semantics: a strong full-sequence score with a weak best domain fails
        (350.0, 250.0, "BETWEEN_NC_TC"),
        (250.0, 250.0, "BETWEEN_NC_TC"),
        (150.0, 150.0, "BELOW_NC"),
    ],
)
def test_classify_hit(seq, dom, expected):
    assert classify_hit(seq, dom, TC, NC) == expected


@pytest.mark.parametrize(
    "scores,expected_verdict,expected_better",
    [
        ([], "NO_MODEL", 0),
        ([score(500.0, target=False)], "NO_MODEL", 1),
        ([score(500.0)], "ABOVE_TC", 0),
        # overlapping families for different reactions both pass: reported, not ranked
        ([score(500.0), score(600.0, target=False, acc="TIGR00002.1")], "ABOVE_TC", 1),
        ([score(250.0)], "BETWEEN_NC_TC", 0),
        # Schnoes's mandelate-racemase case: below the annotated family, above another
        ([score(60.0), score(550.0, target=False, acc="TIGR00002.1")], "BTC", 1),
        ([score(None), score(400.0, target=False, acc="TIGR00002.1")], "SFA", 1),
        ([score(None)], "NO_TARGET_HIT", 0),
        # a domain-level model passing TC does not establish the reaction
        ([score(500.0, family_type="domain")], "BETWEEN_NC_TC", 0),
        # nor does a domain-level competitor count as a better-fitting family
        ([score(60.0), score(550.0, target=False, family_type="domain")], "BTC", 0),
    ],
)
def test_verdict_for(scores, expected_verdict, expected_better):
    verdict, _note, better = verdict_for(scores)
    assert verdict == expected_verdict
    assert len(better) == expected_better


@pytest.mark.parametrize(
    "ec,expected",
    [("4.2.1.11", True), ("1.1.1.-", False), ("1.-.-.-", False), ("3.5.1", False)],
)
def test_is_complete_ec(ec, expected):
    assert is_complete_ec(ec) is expected


@pytest.fixture(scope="module")
def cache_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("cutoff_cache")


@pytest.mark.integration
@pytest.mark.vcr_skip  # NCBIfam table and HMMs are large binary-ish downloads
def test_enolase_passes_trusted_cutoff(cache_dir):
    """E. coli enolase is the positive control from Schnoes's own superfamily."""
    report = check("P0A6P9", ["4.2.1.11"], [], cache_dir)
    assert report.verdict == "ABOVE_TC"


@pytest.mark.integration
@pytest.mark.vcr_skip
def test_prpb_isocitrate_lyase_is_below_cutoff(cache_dir):
    """P. putida PrpB is a methylisocitrate lyase that IEA calls an isocitrate lyase."""
    report = check("Q88KF6", [], ["GO:0004451"], cache_dir)
    assert report.verdict == "BTC"
    assert any("methylisocitrate lyase" in f for f in report.better_fitting_families)
