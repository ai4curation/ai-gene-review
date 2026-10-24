"""Tests for residue numbers that a finding reports on a non-displayed isoform.

The motivating case is RASAL2: PMID:33563064 reports an AMPK site at "S351" and
PMID:33096593 a site at "Ser237". Neither is a serine in the displayed sequence
(Q9UJF2, where 351 is Asp and 237 is Lys); both are serines in isoform 2
(Q9UJF2-2), whose N-terminal extension shifts numbering by +148. A
``residue_mappings`` entry records the residue as reported and as it sits in the
displayed sequence, and these tests check that each side is resolved against
its own sequence.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.finding_residue_mappings import (
    check_mapping,
    validate_finding_residue_mappings,
)
from ai_gene_review.validation.gene_residue_claims import ClaimOutcome


class StubCache:
    """In-memory sequences keyed by accession, in place of UniProt."""

    def __init__(self, seqs: dict[str, str]):
        self.seqs = seqs

    def get(self, accession: str) -> str:
        return self.seqs[accession.split(":")[-1]]


#                        position: 123456789
CACHE = StubCache({"P1": "MAKSDEFGH", "P1-2": "MQQQAKSDEFGH"})  # isoform 2 is +3


def _pos(acc: str, position: int, residue: str) -> dict:
    return {"accession": f"UniProtKB:{acc}", "position": position, "residue": residue}


def _outcomes(results, kind):
    return [r.outcome for r in results if r.kind == kind]


def test_correct_isoform_mapping_passes_every_check():
    mapping = {"as_reported": _pos("P1-2", 7, "S"), "canonical": _pos("P1", 4, "S")}
    results = check_mapping(mapping, "P1", "G", "PMID:1", CACHE)
    assert results
    assert all(r.outcome is ClaimOutcome.PASS for r in results), [str(r) for r in results]


def test_number_read_on_the_wrong_sequence_is_caught():
    """The RASAL2 error: a paper's isoform-2 number read on the displayed sequence."""
    mapping = {"as_reported": _pos("P1", 7, "S")}
    results = check_mapping(mapping, "P1", "G", "PMID:1", CACHE)
    assert _outcomes(results, "AS_REPORTED") == [ClaimOutcome.FAIL]
    detail = next(r.detail for r in results if r.kind == "AS_REPORTED")
    assert "claimed S but the sequence has F" in detail


def test_wrong_canonical_position_is_caught():
    mapping = {"as_reported": _pos("P1-2", 7, "S"), "canonical": _pos("P1", 5, "S")}
    results = check_mapping(mapping, "P1", "G", "PMID:1", CACHE)
    assert _outcomes(results, "CANONICAL") == [ClaimOutcome.FAIL]


def test_mapping_between_different_amino_acids_is_caught():
    """Both sides can each be right about their own sequence and still not be one residue."""
    mapping = {"as_reported": _pos("P1-2", 6, "K"), "canonical": _pos("P1", 4, "S")}
    results = check_mapping(mapping, "P1", "G", "PMID:1", CACHE)
    assert _outcomes(results, "SAME_RESIDUE") == [ClaimOutcome.FAIL]


@pytest.mark.parametrize("canonical_acc", ["P1-2", "OTHER"])
def test_canonical_must_be_this_reviews_displayed_sequence(canonical_acc):
    """canonical names the review's own entry; an isoform id or another protein is not it."""
    seqs = {**CACHE.seqs, "OTHER": "MAKSDEFGH"}
    mapping = {
        "as_reported": _pos("P1-2", 7, "S"),
        "canonical": _pos(canonical_acc, 4 if canonical_acc == "OTHER" else 7, "S"),
    }
    results = check_mapping(mapping, "P1", "G", "PMID:1", StubCache(seqs))
    assert _outcomes(results, "CANONICAL_IDENTITY") == [ClaimOutcome.FAIL]


def test_mapping_without_canonical_checks_only_the_reported_side():
    mapping = {"as_reported": _pos("P1-2", 7, "S")}
    results = check_mapping(mapping, "P1", "G", "PMID:1", CACHE)
    assert [r.kind for r in results] == ["AS_REPORTED"]
    assert results[0].outcome is ClaimOutcome.PASS


def test_review_file_walks_reference_findings(tmp_path: Path):
    review = {
        "id": "P1",
        "gene_symbol": "G",
        "references": [
            {
                "id": "PMID:1",
                "title": "t",
                "findings": [
                    {
                        "statement": "phosphorylated at S7 (isoform 2 numbering)",
                        "residue_mappings": [
                            {"as_reported": _pos("P1-2", 7, "S"), "canonical": _pos("P1", 4, "S")}
                        ],
                    },
                    {"statement": "no residues named"},
                ],
            },
            {"id": "PMID:2", "title": "t2"},
        ],
    }
    path = tmp_path / "G-ai-review.yaml"
    path.write_text(yaml.safe_dump(review, allow_unicode=True))
    results = validate_finding_residue_mappings(path, CACHE)
    assert {r.kind for r in results} == {
        "AS_REPORTED", "CANONICAL_IDENTITY", "CANONICAL", "SAME_RESIDUE"
    }
    assert all(r.outcome is ClaimOutcome.PASS for r in results)
    assert all(r.term == "PMID:1" for r in results)
