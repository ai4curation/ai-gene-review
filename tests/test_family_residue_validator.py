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
    assert not [r for r in check_controls(review, CACHE) if r.outcome is Outcome.FAIL]


def test_protein_listed_as_both_control_types_fails():
    """Catches the mislabelled-control error that makes real enzymes look degenerate."""
    review = _review(
        [{"position": 1, "expected": ["M"]}],
        pos_ctl=[{"id": "UniProtKB:P00009"}],
        neg_ctl=[{"id": "UniProtKB:P00009"}],
    )
    results = check_controls(review, CACHE)
    assert any("both positive and negative" in r.message for r in results
               if r.outcome is Outcome.FAIL)


# --- controls are now resolved, not merely counted -------------------------

CTL_CACHE = StubCache({
    "P00001": TOY,            # MACDEFGHIKLC -- position 3 is C
    "GOOD01": "MACDEFGHIKLC",  # C at 3  -> valid positive control
    "BAD001": "MASDEFGHIKLC",  # S at 3  -> valid negative control
})


def _ctl_review(pos_ctl, neg_ctl, expected=("C",)):
    return {
        "family_id": "PANTHER:PTHR00001",
        "residue_sites": [{
            "site_id": "s",
            "anchor": {"id": "UniProtKB:P00001"},
            "site_source": "UNIPROT_FEATURE",
            "residues": [{"position": 3, "expected": list(expected)}],
            "required_for": [{"term": {"id": "GO:1"}, "strength": "REQUIRED",
                              "rationale": "t"}],
            "positive_controls": pos_ctl,
            "negative_controls": neg_ctl,
        }],
    }


def test_positive_control_lacking_the_site_is_caught():
    """A 'catalytic' control that does not have the site -- the PGRP-LE mistake."""
    review = _ctl_review(
        [{"id": "UniProtKB:GOOD01", "control_position": 3, "control_residue": "C"},
         {"id": "UniProtKB:BAD001", "control_position": 3, "control_residue": "S"}],
        [{"id": "UniProtKB:BAD001", "control_position": 3, "control_residue": "S"}],
    )
    results = check_controls(review, CTL_CACHE)
    bad = [r for r in results if r.outcome is Outcome.FAIL
           and "does not have the site" in r.message]
    assert len(bad) == 1


def test_negative_control_that_has_the_site_is_caught():
    review = _ctl_review(
        [{"id": "UniProtKB:GOOD01", "control_position": 3, "control_residue": "C"}],
        [{"id": "UniProtKB:GOOD01", "control_position": 3, "control_residue": "C"}],
    )
    results = check_controls(review, CTL_CACHE)
    assert any("cannot serve as a negative control" in r.message for r in results)


def test_control_with_a_wrong_declared_residue_is_caught():
    review = _ctl_review(
        [{"id": "UniProtKB:GOOD01", "control_position": 3, "control_residue": "W"}],
        [{"id": "UniProtKB:BAD001", "control_position": 3, "control_residue": "S"}],
    )
    results = check_controls(review, CTL_CACHE)
    assert any("but the sequence has C" in r.message for r in results)


def test_control_without_a_position_is_unresolved():
    review = _ctl_review(
        [{"id": "UniProtKB:GOOD01"}],
        [{"id": "UniProtKB:BAD001", "control_position": 3, "control_residue": "S"}],
    )
    results = check_controls(review, CTL_CACHE)
    assert any(r.outcome is Outcome.UNRESOLVED and "unchecked" in r.message
               for r in results)


def test_anchor_as_its_only_positive_control_is_rejected():
    """Asserting the anchor has the positions that define it proves nothing."""
    review = _ctl_review(
        [{"id": "UniProtKB:P00001", "control_position": 3, "control_residue": "C"}],
        [{"id": "UniProtKB:BAD001", "control_position": 3, "control_residue": "S"}],
    )
    results = check_controls(review, CTL_CACHE)
    assert any("tautological" in r.message for r in results)


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
    # two node/term pairings plus a seed check for each
    assert len(node_results) == 4, [str(r) for r in node_results]
    assert all(r.outcome is Outcome.PASS for r in node_results)
    assert sum("seed" in r.message for r in node_results) == 2


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


# --- node_assessment seeds must appear in PAINT's with-list ----------------


class FakeRow:
    def __init__(self, family, go_id, seeds=""):
        self.family, self.go_id, self.seeds = family, go_id, seeds


def _seed_review(seed_ids):
    return {
        "family_id": "PANTHER:PTHR00001",
        "node_assessments": [{
            "node_id": "PANTHER:PTN000001",
            "asserted_term": {"id": "GO:1", "label": "x"},
            "assessment": "SOUND",
            "assessment_reason": "t",
            "seeds": [{"id": s} for s in seed_ids],
        }],
    }


SEED_PAINT = {
    "PANTHER:PTN000001": [
        FakeRow("PTHR00001", "GO:1", "UniProtKB:P11111|FB:FBgn0000001|ZFIN:ZDB-1")
    ]
}


@pytest.mark.parametrize(
    "seeds,outcome",
    [
        (["UniProtKB:P11111"], Outcome.PASS),                       # subset is fine
        (["UniProtKB:P11111", "FB:FBgn0000001"], Outcome.PASS),
        (["UniProtKB:P99999"], Outcome.FAIL),                       # invented seed
    ],
)
def test_declared_seeds_are_checked_against_paint(seeds, outcome):
    """A curated seed list may be a subset, but not a fabrication."""
    from ai_gene_review.validation.family_residue_validator import check_node_assessments

    results = check_node_assessments(_seed_review(seeds), SEED_PAINT)
    seed_results = [r for r in results if "seed" in r.message]
    assert [r.outcome for r in seed_results] == [outcome]


# --- PANTHER id / label / membership ---------------------------------------


PANTHER_LABELS = {
    "PANTHER:PTHR00001": "SOME FAMILY",
    "PANTHER:PTHR00001:SF1": "A SUBFAMILY",
}
PANTHER_MEMBERS = {"P00001": "PTHR00001:SF1", "P00002": "PTHR00001:SF9"}


def _panther_review(family_label="SOME FAMILY", sf_label="A SUBFAMILY",
                    sf_id="PANTHER:PTHR00001:SF1", members=("P00001",)):
    return {
        "family_id": "PANTHER:PTHR00001",
        "family_name": family_label,
        "subfamilies": [{
            "subfamily_id": sf_id,
            "label": sf_label,
            "representative_members": [{"id": f"UniProtKB:{m}"} for m in members],
        }],
    }


def _panther(review):
    from ai_gene_review.validation.family_residue_validator import check_panther_ids
    return check_panther_ids(review, PANTHER_LABELS, PANTHER_MEMBERS)


def test_panther_ids_and_labels_pass_when_correct():
    assert all(r.outcome is Outcome.PASS for r in _panther(_panther_review()))


def test_wrong_panther_label_is_caught():
    """A plausible label on a real id is how a wrong family stays hidden."""
    results = _panther(_panther_review(sf_label="PLAUSIBLE BUT WRONG"))
    bad = [r for r in results if r.outcome is Outcome.FAIL]
    assert bad and "official name" in bad[0].message


def test_unresolvable_panther_id_is_caught():
    results = _panther(_panther_review(sf_id="PANTHER:PTHR00001:SF99"))
    assert any(r.outcome is Outcome.FAIL and "does not resolve" in r.message
               for r in results)


def test_member_in_the_wrong_subfamily_is_caught():
    """The check that separates a mis-grounded family from a merely mislabelled one."""
    results = _panther(_panther_review(members=("P00002",)))
    bad = [r for r in results if r.outcome is Outcome.FAIL]
    assert bad and "is classified PTHR00001:SF9" in bad[0].message


def test_unindexed_member_is_unresolved_not_failed():
    """Coverage of panther-members.tsv is partial, so absence is not evidence."""
    results = _panther(_panther_review(members=("P99999",)))
    assert any(r.outcome is Outcome.UNRESOLVED for r in results)


def test_ptn_nodes_are_not_label_checked():
    """PTN ids are not in panther.obo; they are checked against PAINT instead."""
    review = _panther_review()
    review["subfamilies"][0]["clade_node_id"] = "PANTHER:PTN000123"
    assert not [r for r in _panther(review) if "PTN" in r.accession]


@pytest.mark.integration
def test_sf0_really_contains_both_seld_and_sps1():
    """The committed basis for RESIDUE_DETERMINED, checked from committed data.

    PTHR10256:SF0 holding both the active E. coli SelD and the arginine-substituted
    Drosophila Sps1 is why that term cannot be scoped by subfamily. Asserted here so
    the justification is not prose-only.
    """
    from ai_gene_review.validation.family_residue_validator import load_panther_members

    members = load_panther_members(Path("interpro/panther/panther-members.tsv"))
    assert members["P16456"] == "PTHR10256:SF0"   # SelD, catalytic
    assert members["O18373"] == "PTHR10256:SF0"   # Sps1, arginine-substituted
    assert members["Q99611"] == "PTHR10256:SF1"   # SEPHS2, the catalytic branch


# --- controls on a motif-only site -----------------------------------------


def _motif_site_review(control_residue):
    """A site defined by a motif, so it declares no per-residue expectations."""
    return {
        "family_id": "PANTHER:PTHR00001",
        "residue_sites": [{
            "site_id": "cxxc",
            "anchor": {"id": "UniProtKB:P00001"},
            "site_source": "UNIPROT_FEATURE",
            "motif": {"pattern_regex": "C..C", "start": 3, "end": 6},
            "required_for": [{"term": {"id": "GO:1"}, "strength": "CONTRIBUTES",
                              "rationale": "t"}],
            "positive_controls": [{
                "id": "UniProtKB:GOOD01", "control_position": 3,
                "control_residue": control_residue,
            }],
            "negative_controls": [],
        }],
    }


def test_motif_site_control_with_a_correct_residue_is_unresolved_not_failed():
    """Membership is undecidable from a pattern, so this must not be a rejection.

    Regression: the guard for this originally sat above the residue comparison and
    returned UNRESOLVED for every control of a motif-only site.
    """
    results = check_controls(_motif_site_review("C"), CTL_CACHE)
    residue = [r for r in results if r.kind == "CONTROL_RESIDUE"]
    assert [r.outcome for r in residue] == [Outcome.UNRESOLVED]
    assert "cannot be decided" in residue[0].message


def test_motif_site_control_with_a_wrong_residue_still_fails():
    """The residue identity is self-contained and must be checked regardless.

    This is the case the mispositioned guard silently accepted: a control could
    declare a residue the sequence does not have and be reported UNRESOLVED without
    the sequence ever being read.
    """
    results = check_controls(_motif_site_review("W"), CTL_CACHE)
    residue = [r for r in results if r.kind == "CONTROL_RESIDUE"]
    assert [r.outcome for r in residue] == [Outcome.FAIL]
    assert "but the sequence has C" in residue[0].message
