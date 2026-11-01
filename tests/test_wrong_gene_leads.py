"""Tests for wrong-gene lead detection from UniProt reference membership.

The offline tests run the detector over real gene folders with a fixed map of
citing entries, so they need no network. One integration test exercises the
UniProt lookup against a recorded cassette.
"""

from pathlib import Path

import pytest

from ai_gene_review.tools.wrong_gene_leads import (
    CitingEntry,
    GeneRecord,
    candidate_rows,
    fetch_citing_entries,
    find_leads,
    score_lead,
)

GENES = Path(__file__).resolve().parents[1] / "genes"

CHSY1 = CitingEntry("Q86X52", "CHSY1", "9606", frozenset({"PTHR12369"}))
ARHGDIG = CitingEntry("Q99819", "ARHGDIG", "9606", frozenset({"PTHR10980"}))
CITING = {"11514575": [CHSY1], "9113980": [ARHGDIG], "20172994": []}


@pytest.fixture(scope="module")
def leads():
    """Leads for the three motivating genes, with UniProt citations fixed."""
    dirs = [
        GENES / "human" / "CSGALNACT1",
        GENES / "human" / "ARHGDIB",
        GENES / "ECOLI" / "traB",
    ]
    return find_leads(dirs, citing=CITING)


@pytest.mark.parametrize(
    "gene,pmid,citing_acc,abstract_reason",
    [
        # CHSY1 cloning paper; the abstract never names CSGALNACT1.
        (
            "human/CSGALNACT1",
            "PMID:11514575",
            "Q86X52",
            "gene_not_named_in_abstract",
        ),
        # RhoGDIgamma paper; its abstract also mentions GDI/D4 (ARHGDIB), so the
        # lead is kept but penalised.
        ("human/ARHGDIB", "PMID:9113980", "Q99819", "gene_named_in_abstract"),
    ],
)
def test_motivating_cases_are_flagged(leads, gene, pmid, citing_acc, abstract_reason):
    """Rows citing a paralog's paper are flagged as same-species paralog leads."""
    hits = [r for r in leads if r["gene"] == gene and r["reference"] == pmid]
    assert hits
    assert all(citing_acc in r["citing_entries"] for r in hits)
    assert all("same_taxon_paralog" in r["reasons"] for r in hits)
    assert all(abstract_reason in r["reasons"] for r in hits)


def test_csgalnact1_outranks_arhgdib(leads):
    """An abstract that never names the annotated gene ranks above one that does."""
    top = {r["gene"]: r["score"] for r in leads}
    assert top["human/CSGALNACT1"] > top["human/ARHGDIB"]


def test_same_gene_entry_is_not_a_lead(tmp_path):
    """A reviewed entry for the same gene in the same species is not a wrong gene."""
    gene = tmp_path / "DROME" / "loqs"
    gene.mkdir(parents=True)
    (gene / "loqs-uniprot.txt").write_text(
        "AC   X2J5X6;\nGN   Name=loqs;\nOX   NCBI_TaxID=7227;\n"
    )
    header = "\t".join(
        [
            "GENE PRODUCT DB",
            "GENE PRODUCT ID",
            "SYMBOL",
            "QUALIFIER",
            "GO TERM",
            "GO NAME",
            "GO ASPECT",
            "ECO ID",
            "GO EVIDENCE CODE",
            "REFERENCE",
            "WITH/FROM",
            "TAXON ID",
            "TAXON NAME",
            "ASSIGNED BY",
            "GENE NAME",
            "DATE",
        ]
    )
    row = "\t".join(
        [
            "UniProtKB",
            "X2J5X6",
            "loqs",
            "involved_in",
            "GO:0030422",
            "x",
            "P",
            "ECO:0000315",
            "IMP",
            "PMID:15918770",
            "",
            "7227",
            "fly",
            "FlyBase",
            "x",
            "20200101",
        ]
    )
    (gene / "loqs-goa.tsv").write_text(header + "\n" + row + "\n")
    citing = {"15918770": [CitingEntry("Q9VJY9", "loqs", "7227", frozenset())]}
    assert find_leads([gene], citing=citing, publications_dir=tmp_path) == []


def test_leads_join_existing_review(leads):
    """The CSGALNACT1 rows already carry WRONG_GENE_PRODUCT defects from review."""
    rows = [r for r in leads if r["gene"] == "human/CSGALNACT1"]
    assert any(r["wrong_gene_defect"] for r in rows)
    assert all(r["review_action"] for r in rows)


def test_trab_is_a_known_miss(leads):
    """F-plasmid TraB is not flagged: the pKM101 TraB entry does not cite the paper.

    Its wrong-gene IDA (PMID:20172994) is a candidate row, but no reviewed UniProt
    entry cites the paper, so this detector cannot see it.
    """
    own, rows = candidate_rows(GENES / "ECOLI" / "traB")
    assert any(r["REFERENCE"] == "PMID:20172994" for r in rows)
    assert not [r for r in leads if r["gene"] == "ECOLI/traB"]


@pytest.mark.parametrize(
    "others,named,expected",
    [
        (
            [CitingEntry("P2", "X", "10090", frozenset())],
            None,
            (1, "few_citing_entries"),
        ),
        (
            [CitingEntry("P2", "ABC1", "10090", frozenset())],
            False,
            (
                5,
                "same_gene_other_species;few_citing_entries;gene_not_named_in_abstract",
            ),
        ),
        (
            [CitingEntry("P2", "X", "9606", frozenset())],
            True,
            (0, "same_taxon_other_gene;few_citing_entries;gene_named_in_abstract"),
        ),
        (
            [CitingEntry(f"P{i}", "X", "10090", frozenset()) for i in range(5)],
            None,
            (0, ""),
        ),
    ],
)
def test_score_lead(others, named, expected):
    """Each signal adds to the score; naming the gene in the abstract subtracts."""
    own = GeneRecord(
        "P1", "9606", frozenset({"PTHR1"}), frozenset({"ABC1"}), frozenset()
    )
    assert score_lead(own, others, named) == expected


@pytest.mark.integration
def test_fetch_citing_entries_from_uniprot(tmp_path):
    """UniProt reports CHSY1 and ARHGDIG as citing the motivating papers."""
    citing = fetch_citing_entries(["11514575", "9113980"], cache_dir=tmp_path)
    assert "Q86X52" in {c.accession for c in citing["11514575"]}
    assert "Q99819" in {c.accession for c in citing["9113980"]}
