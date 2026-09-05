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

import doctest
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

# The script lives under projects/, not in the installed package, so it is
# importable only via the sys.path insert above and mypy cannot resolve it.
from retrieval_recall import band, pmids_in  # type: ignore[import-not-found] # noqa: E402


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
    summary: dict, by_gene: dict[str, dict], writeup: str
) -> None:
    """No gene may be named as zero-recall in prose unless the data says so.

    The AGFG1 finding: the write-up listed it among the 0% genes while the table
    scored it 7% (1 hit of 14 novel references).

    Every symbol in the sentence is checked, not a hardcoded shortlist, and the
    anchor is required to match — an unfindable anchor fails rather than passing
    on an empty set.
    """
    named = genes_named(zero_recall_sentence(writeup)) & set(by_gene)
    assert named, "no known gene symbols parsed out of the 0%-recall sentence"
    assert named <= set(summary["zero_recall_genes"])


def zero_recall_sentence(writeup: str) -> str:
    """The parenthesised gene list naming the 0%-recall end.

    Raises rather than returning '' when the anchor cannot be found: a guard that
    silently disarms itself on a prose edit is worse than no guard, and prose
    edits are the side that produced the AGFG1 defect.
    """
    match = re.search(r"at the (?:0%|zero-recall) end \(([^)]*)\)", writeup)
    if match is None:
        raise AssertionError(
            "could not locate the 0%-recall sentence in paint-campaign.md, so the "
            "gene list is unverified — re-point the anchor pattern in this test"
        )
    return match.group(1)


def genes_named(fragment: str) -> set[str]:
    """Gene symbols in a prose fragment, expanding the 'AADACL2/3/4' shorthand.

    Written generically so a symbol newly mentioned in the sentence is checked
    without editing this test.

    >>> sorted(genes_named("AADACL2/3/4, ACP7, ACTL10"))
    ['AADACL2', 'AADACL3', 'AADACL4', 'ACP7', 'ACTL10']
    >>> sorted(genes_named("RAD51C, SLX4 and XRCC2"))
    ['RAD51C', 'SLX4', 'XRCC2']
    >>> genes_named("nothing but lower case")
    set()
    """
    found: set[str] = set()
    for prefix, numbers in re.findall(r"\b([A-Z][A-Z0-9]*?)(\d+(?:/\d+)+)\b", fragment):
        found.update(f"{prefix}{n}" for n in numbers.split("/"))
    found.update(re.findall(r"\b[A-Z][A-Z0-9]+\b", fragment))
    return found


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


def test_script_doctests_are_executed() -> None:
    """Run the script's doctests, which no other harness collects.

    ``just doctest`` is ``pytest --doctest-modules src`` and pytest's testpaths is
    ``["tests"]``, so nothing under ``projects/`` is collected. Without this call
    every doctest in ``retrieval_recall.py`` is documentation rather than a test.
    """
    import retrieval_recall

    results = doctest.testmod(retrieval_recall, verbose=False)
    assert results.failed == 0, f"{results.failed} doctest failure(s)"
    assert results.attempted > 0, "no doctests ran — did the module move?"


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
        # A separated short number is prose whether or not a colon is present.
        # This is the case that would catch a later "simplification" of the two
        # regex branches into PMID:?\s*(\d{4,9}).
        ("PMID 12345", set()),
    ],
)
def test_pmid_matching_keeps_citations_and_rejects_prose(
    tmp_path: Path, text: str, expected: set[str]
) -> None:
    path = tmp_path / "sample.md"
    path.write_text(text)
    assert pmids_in(path) == expected
