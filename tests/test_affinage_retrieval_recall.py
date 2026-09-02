"""Guard the Affinage retrieval-recall write-up against its own generated data.

Both blocking findings in the review of this analysis were the same failure mode:
a hand-written claim in the narrative drifting from the generated table (a gene
listed at 0% recall that the table scored at 7%, and a summary field labelled as
one set while computing another). Neither was caught by running the script,
because the script was right and the prose was wrong.

These tests pin the narrative to `per-gene.json`, so a future edit to either side
that breaks the correspondence fails loudly.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = REPO_ROOT / "projects" / "AFFINAGE_EVALUATION"
RESULTS = PROJECT_DIR / "results" / "paint-campaign"
WRITEUP = PROJECT_DIR / "results" / "paint-campaign.md"

sys.path.insert(0, str(PROJECT_DIR))

from retrieval_recall import band, pmids_in  # noqa: E402


@pytest.fixture(scope="module")
def data() -> dict:
    return json.loads((RESULTS / "per-gene.json").read_text())


@pytest.fixture(scope="module")
def summary(data: dict) -> dict:
    return data["summary"]


@pytest.fixture(scope="module")
def by_gene(data: dict) -> dict[str, dict]:
    return {row["gene"]: row for row in data["genes"]}


@pytest.fixture(scope="module")
def writeup() -> str:
    return WRITEUP.read_text()


def test_goa_share_and_novel_partition_the_review_set(summary: dict) -> None:
    """The headline table must add up: GOA-supplied + novel == all review PMIDs.

    This is the invariant the `total_goa_pmids` fix was about. Deriving it as
    ``tot_rev - tot_novel`` makes it true by construction; asserting it here
    means a future reversion to ``sum(n_goa)`` fails the moment some review
    stops citing every one of its GOA references.
    """
    assert (
        summary["total_goa_pmids"] + summary["total_novel_pmids"]
        == summary["total_review_pmids"]
    )


def test_goa_is_subset_of_review_for_every_gene(by_gene: dict[str, dict]) -> None:
    """Per-gene form of the same invariant, which is what makes the totals equal."""
    violations = {
        name: (row["n_goa"], row["n_novel"], row["n_review"])
        for name, row in by_gene.items()
        if row["has_report"]
        and row["has_review"]
        and row["n_goa"] + row["n_novel"] != row["n_review"]
    }
    assert not violations


def test_zero_recall_genes_are_exactly_those_with_no_hits(
    summary: dict, by_gene: dict[str, dict]
) -> None:
    derived = sorted(
        name
        for name, row in by_gene.items()
        if row["has_report"]
        and row["has_review"]
        and row["n_novel"] > 0
        and row["n_hits"] == 0
    )
    assert summary["zero_recall_genes"] == derived


def test_narrative_zero_recall_list_matches_generated_data(
    summary: dict, writeup: str
) -> None:
    """No gene may be named as zero-recall in prose unless the data says so.

    The AGFG1 finding: the write-up listed it among the 0% genes while the table
    scored it 7% (1 hit of 14 novel references).
    """
    listed = set(re.findall(r"\b(?:AADACL[0-9]|AC[PT][A-Z0-9]*|AGFG[0-9])\b", writeup))
    claimed_zero = {
        name for name in listed if f"{name}" in _zero_recall_sentence(writeup)
    }
    assert claimed_zero <= set(summary["zero_recall_genes"])


def _zero_recall_sentence(writeup: str) -> str:
    """The paragraph naming the 0%-recall end, or '' if the phrasing changed."""
    match = re.search(r"at the 0% end \(([^)]*)\)", writeup)
    return match.group(1) if match else ""


@pytest.mark.parametrize(
    ("gene", "expected_goa", "expected_band"),
    [
        ("ACTR8", 12, "well-studied (10+)"),
        ("ACTR1B", 8, "medium (3-9)"),
    ],
)
def test_named_counterexamples_still_hold(
    by_gene: dict[str, dict], gene: str, expected_goa: int, expected_band: str
) -> None:
    """The write-up names these two as not-obscure zero-recall genes.

    They are the evidence for 'the dark-gene reading fails at both ends'; if the
    underlying counts move, the sentence stops being true.
    """
    assert by_gene[gene]["n_goa"] == expected_goa
    assert band(by_gene[gene]["n_goa"]) == expected_band
    assert by_gene[gene]["n_hits"] == 0


def test_stratification_covers_every_gene_with_a_novel_reference(
    summary: dict, by_gene: dict[str, dict]
) -> None:
    banded = sum(acc["genes"] for acc in summary["by_curation_depth"].values())
    eligible = sum(
        1
        for row in by_gene.values()
        if row["has_report"] and row["has_review"] and row["n_novel"] > 0
    )
    assert banded == eligible
    assert (
        sum(acc["novel"] for acc in summary["by_curation_depth"].values())
        == summary["total_novel_pmids"]
    )
    assert (
        sum(acc["hits"] for acc in summary["by_curation_depth"].values())
        == summary["total_hits"]
    )


def test_empty_reports_really_contain_no_pmids(summary: dict) -> None:
    """An empty return is a headline claim; confirm it is not a regex artifact."""
    for gene in summary["empty_reports"]:
        report = (
            REPO_ROOT / "genes" / "human" / gene / f"{gene}-deep-research-affinage.md"
        )
        assert pmids_in(report) == set()


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("PMID:12345678", {"12345678"}),
        ("PMID: 12345678", {"12345678"}),
        ("PMID 10824116", {"10824116"}),  # colon-less, used by NAGK and PSEPK reviews
        ("PMID:24417", {"24417"}),  # pre-1975 five-digit id
        ("PMID:4874", {"4874"}),  # four-digit id
        ("Queried by PMID: 3 annotations", set()),  # prose, not a citation
        ("Queried by PMID: 12 annotations", set()),  # ditto, two digits
    ],
)
def test_pmid_matching_keeps_citations_and_rejects_prose(
    tmp_path: Path, text: str, expected: set[str]
) -> None:
    path = tmp_path / "sample.md"
    path.write_text(text)
    assert pmids_in(path) == expected
