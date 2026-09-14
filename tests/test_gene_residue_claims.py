"""Tests for gene-level residue-claim validation.

The headline case is ``test_intact_site_claimed_as_lost_is_caught``: that is the CASP12 /
LPA / AZIN1 / HSPA13 error, where a review asserts residue loss for a protein whose site
is fully intact. Four of seventeen such claims in this repo were wrong that way, so the
validator earns its place by contradicting them.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.gene_residue_claims import (
    ClaimOutcome,
    check_claim,
    load_family_sites,
    validate_gene_residue_claims,
)


class StubCache:
    def __init__(self, seqs: dict[str, str]):
        self.seqs = seqs

    def get(self, accession: str) -> str:
        return self.seqs[accession.split(":")[-1]]


#            positions: 1234567890
CACHE = StubCache({"ANCHOR1": "MAHKCDEFGH", "TARGET1": "MAAKSDEFGH", "TARGET2": "MAHKCDEFGH"})
SITES = {"PANTHER:PTHR00001#site_a": {3, 5}}


def _claim(claim_type, a_pos, a_res, t_pos, t_res, *, target_acc="TARGET1", site=None):
    c = {
        "claim_type": claim_type,
        "method": "MSA",
        "anchor": {"accession": "UniProtKB:ANCHOR1", "position": a_pos, "residue": a_res},
    }
    if t_pos is not None:
        c["target"] = {
            "accession": f"UniProtKB:{target_acc}", "position": t_pos, "residue": t_res
        }
    if site:
        c["site_ref"] = site
    return c


def _outcomes(results, kind):
    return [r.outcome for r in results if r.kind == kind]


def test_valid_loss_claim_passes_every_check():
    results = check_claim(
        _claim("LOST", 3, "H", 3, "A", site="PANTHER:PTHR00001#site_a"),
        "UniProtKB:TARGET1", "G", "GO:1", CACHE, SITES,
    )
    assert all(r.outcome is ClaimOutcome.PASS for r in results), [str(r) for r in results]


def test_intact_site_claimed_as_lost_is_caught():
    """The CASP12/LPA error: claim says LOST, the residue is still there."""
    results = check_claim(
        _claim("LOST", 3, "H", 3, "H", target_acc="TARGET2"),
        "UniProtKB:TARGET2", "G", "GO:1", CACHE,
    )
    assert _outcomes(results, "CLAIM_CONSISTENCY") == [ClaimOutcome.FAIL]
    msg = next(r.detail for r in results if r.kind == "CLAIM_CONSISTENCY")
    assert "the site is intact" in msg


def test_retained_claim_contradicted_by_a_substitution():
    results = check_claim(
        _claim("RETAINED", 3, "H", 3, "A"), "UniProtKB:TARGET1", "G", "GO:1", CACHE
    )
    assert _outcomes(results, "CLAIM_CONSISTENCY") == [ClaimOutcome.FAIL]


@pytest.mark.parametrize(
    "a_pos,a_res,kind",
    [
        (3, "W", "ANCHOR"),    # wrong residue at a real position
        (99, "H", "ANCHOR"),   # invented position
    ],
)
def test_wrong_anchor_is_caught(a_pos, a_res, kind):
    results = check_claim(
        _claim("LOST", a_pos, a_res, 3, "A"), "UniProtKB:TARGET1", "G", "GO:1", CACHE
    )
    assert ClaimOutcome.FAIL in _outcomes(results, kind)


def test_wrong_target_residue_is_caught():
    results = check_claim(
        _claim("LOST", 3, "H", 3, "W"), "UniProtKB:TARGET1", "G", "GO:1", CACHE
    )
    assert _outcomes(results, "TARGET") == [ClaimOutcome.FAIL]


def test_claim_about_a_different_protein_is_caught():
    """A claim's target must be this gene, or it is silently about something else."""
    results = check_claim(
        _claim("LOST", 3, "H", 3, "A", target_acc="TARGET1"),
        "UniProtKB:SOMEONE_ELSE", "G", "GO:1", CACHE,
    )
    assert _outcomes(results, "TARGET_IDENTITY") == [ClaimOutcome.FAIL]


def test_missing_target_is_unresolved_not_failed():
    """An unalignable region yields a weaker claim, not a contradicted one."""
    results = check_claim(
        _claim("LOST", 3, "H", None, None), "UniProtKB:TARGET1", "G", "GO:1", CACHE
    )
    assert _outcomes(results, "TARGET") == [ClaimOutcome.UNRESOLVED]


@pytest.mark.parametrize(
    "site,anchor_pos,expected",
    [
        ("PANTHER:PTHR00001#site_a", 3, ClaimOutcome.PASS),
        ("PANTHER:PTHR00001#site_a", 4, ClaimOutcome.FAIL),   # position not in the site
        ("PANTHER:PTHR00001#no_such", 3, ClaimOutcome.FAIL),  # site does not exist
    ],
)
def test_site_ref_cross_file_check(site, anchor_pos, expected):
    """The claim's anchor position must be one the cited family site declares."""
    residue = {3: "H", 4: "K"}[anchor_pos]
    results = check_claim(
        _claim("LOST", anchor_pos, residue, 3, "A", site=site),
        "UniProtKB:TARGET1", "G", "GO:1", CACHE, SITES,
    )
    assert _outcomes(results, "SITE_REF") == [expected]


def test_site_ref_unresolved_when_no_family_reviews_loaded():
    results = check_claim(
        _claim("LOST", 3, "H", 3, "A", site="PANTHER:PTHR00001#site_a"),
        "UniProtKB:TARGET1", "G", "GO:1", CACHE, None,
    )
    assert _outcomes(results, "SITE_REF") == [ClaimOutcome.UNRESOLVED]


def test_review_without_claims_yields_nothing(tmp_path):
    """Forward-only: an existing review with no residue_claims is silent, not failing."""
    p = tmp_path / "x-ai-review.yaml"
    p.write_text(yaml.safe_dump({
        "id": "UniProtKB:TARGET1", "gene_symbol": "X",
        "existing_annotations": [
            {"term": {"id": "GO:1"}, "review": {"action": "REMOVE",
                                                "reason": "lacks the catalytic cysteine"}}
        ],
    }))
    assert validate_gene_residue_claims(p, CACHE, SITES) == []


# --------------------------------------------------------------------------
# Against the real corpus
# --------------------------------------------------------------------------


@pytest.mark.integration
def test_real_pgrplc_claims_all_pass():
    """The committed PGRPLC residue claims resolve against real UniProt sequences."""
    from ai_gene_review.validation.family_residue_validator import SequenceCache

    sites = load_family_sites(Path("interpro/panther"))
    results = validate_gene_residue_claims(
        Path("genes/ANOGA/PGRPLC/PGRPLC-ai-review.yaml"),
        SequenceCache(Path(".cache/uniprot_seq")),
        sites,
    )
    assert len(results) == 12, [str(r) for r in results]
    failures = [r for r in results if r.outcome is not ClaimOutcome.PASS]
    assert not failures, [str(f) for f in failures]


@pytest.mark.integration
def test_real_site_ref_resolves_to_the_family_review():
    """The gene's site_ref really points at the curated PTHR11022 site."""
    sites = load_family_sites(Path("interpro/panther"))
    assert sites["PANTHER:PTHR11022#zn_triad"] == {410, 522, 530}


@pytest.mark.integration
def test_corrupting_a_real_claim_is_caught(tmp_path):
    """Flip PGRPLC's retained His to a LOST claim; the consistency check must fire."""
    from ai_gene_review.validation.family_residue_validator import SequenceCache

    src = Path("genes/ANOGA/PGRPLC/PGRPLC-ai-review.yaml")
    doc = yaml.safe_load(src.read_text())
    flipped = 0
    for ann in doc["existing_annotations"]:
        pr = (ann.get("review") or {}).get("propagation_review") or {}
        for claim in pr.get("residue_claims") or []:
            if claim["claim_type"] == "RETAINED":
                claim["claim_type"] = "LOST"
                flipped += 1
    assert flipped == 1
    bad = tmp_path / "bad-ai-review.yaml"
    bad.write_text(yaml.safe_dump(doc))
    results = validate_gene_residue_claims(
        bad, SequenceCache(Path(".cache/uniprot_seq")),
        load_family_sites(Path("interpro/panther")),
    )
    bad_consistency = [
        r for r in results
        if r.kind == "CLAIM_CONSISTENCY" and r.outcome is ClaimOutcome.FAIL
    ]
    assert len(bad_consistency) == 1
    assert "the site is intact" in bad_consistency[0].detail


# --------------------------------------------------------------------------
# Sequence-version drift
# --------------------------------------------------------------------------


class VersionedStubCache(StubCache):
    """Stub that also reports a sequence version, like the real cache does."""

    def __init__(self, seqs, versions):
        super().__init__(seqs)
        self.versions = versions

    def sequence_version(self, accession):
        return self.versions.get(accession.split(":")[-1])


VCACHE = VersionedStubCache(
    {"ANCHOR1": "MAHKCDEFGH", "TARGET1": "MAAKSDEFGH"},
    {"ANCHOR1": 3, "TARGET1": 2},
)


def _versioned_claim(a_ver=None, t_ver=None):
    c = _claim("LOST", 3, "H", 3, "A")
    if a_ver is not None:
        c["anchor"]["sequence_version"] = a_ver
    if t_ver is not None:
        c["target"]["sequence_version"] = t_ver
    return c


def test_matching_sequence_version_is_silent():
    """A pinned version that still matches adds no noise."""
    results = check_claim(
        _versioned_claim(a_ver=3, t_ver=2), "UniProtKB:TARGET1", "G", "GO:1", VCACHE
    )
    assert all(r.outcome is ClaimOutcome.PASS for r in results)
    assert not any("sequence version has moved" in r.detail for r in results)


def test_drifted_sequence_version_is_reported_even_when_the_residue_still_matches():
    """The residue is right, but the claim was made against an older sequence."""
    results = check_claim(
        _versioned_claim(a_ver=1), "UniProtKB:TARGET1", "G", "GO:1", VCACHE
    )
    anchor = next(r for r in results if r.kind == "ANCHOR")
    assert anchor.outcome is ClaimOutcome.PASS
    assert "sequence version has moved 1 -> 3" in anchor.detail


def test_drift_annotates_a_residue_mismatch_so_the_failure_is_actionable():
    """A wrong residue plus a moved version usually means the sequence changed under it."""
    claim = _claim("LOST", 3, "W", 3, "A")          # W is wrong at anchor position 3
    claim["anchor"]["sequence_version"] = 1
    results = check_claim(claim, "UniProtKB:TARGET1", "G", "GO:1", VCACHE)
    anchor = next(r for r in results if r.kind == "ANCHOR")
    assert anchor.outcome is ClaimOutcome.FAIL
    assert "sequence version has moved 1 -> 3" in anchor.detail


def test_unversioned_claim_is_not_penalised():
    """sequence_version is optional; omitting it must not produce noise."""
    results = check_claim(
        _versioned_claim(), "UniProtKB:TARGET1", "G", "GO:1", VCACHE
    )
    assert not any("sequence version" in r.detail for r in results)


@pytest.mark.integration
def test_real_claims_pin_current_sequence_versions():
    """The committed claims record the versions UniProt currently serves."""
    from ai_gene_review.validation.family_residue_validator import SequenceCache

    cache = SequenceCache(Path(".cache/uniprot_seq"))
    for path in ["genes/ANOGA/PGRPLC/PGRPLC-ai-review.yaml",
                 "genes/human/SEPHS1/SEPHS1-ai-review.yaml"]:
        results = validate_gene_residue_claims(
            Path(path), cache, load_family_sites(Path("interpro/panther"))
        )
        drifted = [r for r in results if "sequence version has moved" in r.detail]
        assert not drifted, [str(d) for d in drifted]


def test_motif_only_site_can_be_cited(tmp_path):
    """A motif-defined site covers its whole block, so a claim inside it resolves.

    Regression: previously load_family_sites returned an empty position set for a
    motif-only site, so every site_ref citing one failed -- a site that existed but
    could never be referenced.
    """
    d = tmp_path / "PTHR00001"
    d.mkdir()
    (d / "PTHR00001-review.yaml").write_text(yaml.safe_dump({
        "family_id": "PANTHER:PTHR00001",
        "residue_sites": [
            {"site_id": "cxxc",
             "motif": {"pattern_regex": "C..C", "start": 10, "end": 13}}
        ],
    }))
    sites = load_family_sites(tmp_path)
    assert sites["PANTHER:PTHR00001#cxxc"] == {10, 11, 12, 13}


def test_residue_and_motif_positions_are_unioned(tmp_path):
    d = tmp_path / "PTHR00002"
    d.mkdir()
    (d / "PTHR00002-review.yaml").write_text(yaml.safe_dump({
        "family_id": "PANTHER:PTHR00002",
        "residue_sites": [
            {"site_id": "mixed",
             "residues": [{"position": 5, "expected": ["C"]}],
             "motif": {"pattern_regex": "C.C", "start": 20, "end": 22}}
        ],
    }))
    assert load_family_sites(tmp_path)["PANTHER:PTHR00002#mixed"] == {5, 20, 21, 22}
