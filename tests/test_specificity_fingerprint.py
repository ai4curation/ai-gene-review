"""Tests for curated substrate-specificity fingerprints (Kinateder et al. 2024)."""

from pathlib import Path

import pytest

from ai_gene_review.validation.family_residue_validator import SequenceCache
from ai_gene_review.validation.specificity_fingerprint import (
    DEFAULT_FINGERPRINTS,
    Fingerprint,
    call_residues,
    check,
    load_fingerprints,
    reference_mismatches,
    verdict_for,
)

REPO = Path(__file__).resolve().parents[1]
FINGERPRINTS = load_fingerprints(REPO / DEFAULT_FINGERPRINTS)

# A toy fingerprint: D at 3 and Y at 6 indicate the function; E and M the contrast.
TOY = Fingerprint.from_dict(
    {
        "id": "toy",
        "function": {"go": "GO:0000001", "label": "toy activity"},
        "contrast_function": {"go": "GO:0000002", "label": "other activity"},
        "reference": {"accession": "P00000"},
        "min_identity": 0.5,
        "source": {"reference_id": "PMID:1", "supporting_text": []},
        "positions": [
            {
                "position": 3,
                "residues": ["D"],
                "role": "required",
                "contrast_residues": ["E"],
            },
            {
                "position": 6,
                "residues": ["Y"],
                "role": "required",
                "contrast_residues": ["M"],
            },
            {"position": 9, "residues": ["T"], "role": "supporting"},
        ],
    }
)
TOY_REF = "MKDLAYWGTRHKLA"


@pytest.mark.parametrize(
    "query,expected",
    [
        (TOY_REF, "PRESENT"),
        ("MKELAMWGTRHKLA", "CONTRAST"),
        ("MKDLAMWGTRHKLA", "PARTIAL"),
        ("MKALAFWGTRHKLA", "ABSENT"),
        # a supporting-position change alone does not alter the verdict
        ("MKDLAYWGARHKLA", "PRESENT"),
        # extra N-terminal residues shift numbering; the alignment absorbs them
        ("GGGMKDLAYWGTRHKLA", "PRESENT"),
        # unrelated sequence: identity below min_identity
        ("WWWWWWWWWWWWWW", "LOW_IDENTITY"),
    ],
)
def test_toy_verdicts(query, expected):
    calls, identity = call_residues(TOY, TOY_REF, query)
    assert verdict_for(calls, identity, TOY.min_identity) == expected


def test_insertion_keeps_fingerprint_positions():
    """An insertion before a fingerprint position must not shift the residue read."""
    query = "MKDLAPPPPYWGTRHKLA"
    calls, _ = call_residues(TOY, TOY_REF, query)
    assert [c.query_residue for c in calls] == ["D", "Y", "T"]


@pytest.mark.parametrize("fp", FINGERPRINTS.values(), ids=lambda fp: fp.id)
def test_fingerprint_quotes_are_verbatim(fp):
    """Every supporting_text must be a substring of the cached publication."""
    pmid = fp.source["reference_id"].split(":")[1]
    text = (REPO / "publications" / f"PMID_{pmid}.md").read_text()
    for quote in fp.source["supporting_text"]:
        assert quote in text, quote


@pytest.mark.parametrize("fp", FINGERPRINTS.values(), ids=lambda fp: fp.id)
def test_fingerprint_positions_are_well_formed(fp):
    assert any(p.role == "required" for p in fp.positions)
    assert all(p.role in {"required", "supporting"} for p in fp.positions)
    assert 0 < fp.min_identity < 1


@pytest.fixture(scope="module")
def cache(tmp_path_factory):
    return SequenceCache(tmp_path_factory.mktemp("uniprot_seq"))


@pytest.mark.integration
@pytest.mark.vcr_skip
@pytest.mark.parametrize("fp", FINGERPRINTS.values(), ids=lambda fp: fp.id)
def test_reference_carries_its_own_fingerprint(fp, cache):
    """Catches a wrong reference accession or an off-by-one in the curated numbering."""
    assert reference_mismatches(fp, cache) == []


@pytest.mark.integration
@pytest.mark.vcr_skip
@pytest.mark.parametrize(
    "accession,expected",
    [
        ("Q88CN3", "PRESENT"),  # P. putida PP_5147, 68% identical to paHisN
        ("Q58989", "LOW_IDENTITY"),  # M. jannaschii SerB, the paper's PSPase reference
    ],
)
def test_holpase_fingerprint(accession, expected, cache):
    report = check(accession, FINGERPRINTS["holpase_hisn_pseudomonas"], cache)
    assert report.verdict == expected
