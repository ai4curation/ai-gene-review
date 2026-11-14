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
    MAX_CITING_ENTRIES,
    MAX_RANGE,
    SHARED_ANNOTATION_GENES,
    candidate_rows,
    fetch_citing_entries,
    find_leads,
    gene_specific_names,
    named_in_abstract,
    pombase_names,
    score_lead,
    shared_annotation_counts,
    token_forms,
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


GOA_HEADER = "\t".join(
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


def _gene_folder(root, uniprot, acc="P00001", pmid="1", taxon="9606"):
    """A minimal gene folder with one IDA row citing ``pmid``."""
    gene = root / "human" / "ABC1"
    gene.mkdir(parents=True)
    (gene / "ABC1-uniprot.txt").write_text(uniprot)
    row = "\t".join(
        ["UniProtKB", acc, "ABC1", "enables", "GO:0003674", "x", "F", "ECO:0000314"]
        + ["IDA", f"PMID:{pmid}", "", taxon, "x", "UniProt", "x", "20200101"]
    )
    (gene / "ABC1-goa.tsv").write_text(GOA_HEADER + "\n" + row + "\n")
    return gene


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


def test_same_gene_filter_ignores_symbol_case(tmp_path):
    """A same-species entry whose symbol differs only in case is the same gene."""
    gene = _gene_folder(
        tmp_path, "AC   P00001;\nGN   Name=ABC1;\nOX   NCBI_TaxID=9606;\n"
    )
    citing = {"1": [CitingEntry("P00002", "Abc1", "9606", frozenset())]}
    assert find_leads([gene], citing=citing, publications_dir=tmp_path) == []


@pytest.mark.parametrize(
    "n_citing,flagged", [(MAX_CITING_ENTRIES, True), (MAX_CITING_ENTRIES + 1, False)]
)
def test_large_scale_papers_are_skipped(tmp_path, n_citing, flagged):
    """A paper cited by more than MAX_CITING_ENTRIES other entries is skipped."""
    gene = _gene_folder(
        tmp_path, "AC   P00001;\nGN   Name=ABC1;\nOX   NCBI_TaxID=9606;\n"
    )
    entries = [
        CitingEntry(f"Q{i:05d}", f"X{i}", "10090", frozenset()) for i in range(n_citing)
    ]
    leads = find_leads([gene], citing={"1": entries}, publications_dir=tmp_path)
    assert bool(leads) is flagged


def test_shared_family_name_does_not_cancel_paralog_signal(tmp_path):
    """A family name shared with the citing paralog is not evidence the gene was studied.

    TUA1-like case: both paralogs are "Tubulin alpha chain", so an abstract using
    that phrase does not name the annotated paralog.
    """
    gene = _gene_folder(
        tmp_path,
        "AC   P00001;\nDE   RecName: Full=Tubulin alpha chain;\nGN   Name=ABC1;\n"
        "OX   NCBI_TaxID=9606;\nDR   PANTHER; PTHR11588; X; 1.\n",
    )
    pubs = tmp_path / "publications"
    pubs.mkdir()
    (pubs / "PMID_1.md").write_text(
        "title: T\n## Abstract\nWe purified tubulin alpha chain from TUA2 cells.\n"
    )
    paralog = CitingEntry(
        "P00002",
        "TUA2",
        "9606",
        frozenset({"PTHR11588"}),
        frozenset({"Tubulin alpha chain"}),
    )
    (lead,) = find_leads([gene], citing={"1": [paralog]}, publications_dir=pubs)
    assert "same_taxon_paralog" in lead["reasons"]
    assert "gene_not_named_in_abstract" in lead["reasons"]


def test_cached_pmids_are_not_requeried(tmp_path):
    """Cached PMIDs, including ones with no citing entries, are served from the cache.

    Only the requested PMIDs are returned, not the whole cache.
    """
    import json

    cache = tmp_path / "citing-entries-v2.json"
    entry = {
        "accession": "Q86X52",
        "gene": "CHSY1",
        "taxon": "9606",
        "panther": ["PTHR12369"],
        "protein_names": ["Chondroitin sulfate synthase 1"],
    }
    cache.write_text(json.dumps({"11514575": [entry], "1": [], "2": [entry]}))
    out = fetch_citing_entries(["11514575", "1"], cache_dir=tmp_path)
    assert set(out) == {"11514575", "1"}
    assert out["1"] == []
    assert out["11514575"][0].protein_names == {"Chondroitin sulfate synthase 1"}


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
        # UniProt writes mouse symbols in title case.
        (
            [CitingEntry("P2", "Abc1", "10090", frozenset())],
            None,
            (3, "same_gene_other_species;few_citing_entries"),
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


def test_gene_names_wrapping_across_gn_lines_are_parsed():
    """Synonyms continued on a later GN line are read (NLRP3's NALP3, PYPAF1)."""
    from ai_gene_review.tools.wrong_gene_leads import parse_uniprot_flatfile

    text = (GENES / "human" / "NLRP3" / "NLRP3-uniprot.txt").read_text()
    assert {"NLRP3", "NALP3", "PYPAF1", "CIAS1"} <= parse_uniprot_flatfile(
        text
    ).gene_names


def test_protein_name_in_abstract_penalises_aurkc_lead():
    """The Aurora A review names "aurora kinases A, B, and C", so AURKC is named.

    Before protein names were matched, this TAS citation of a review covering all
    three Aurora kinases ranked in the top tier.
    """
    aurka = CitingEntry("O14965", "AURKA", "9606", frozenset({"PTHR24350"}))
    rows = find_leads([GENES / "human" / "AURKC"], citing={"19774610": [aurka]})
    hits = [r for r in rows if r["reference"] == "PMID:19774610"]
    assert hits
    assert all("gene_named_in_abstract" in r["reasons"] for r in hits)


@pytest.mark.parametrize(
    "pmid,present,absent",
    [
        # Abstract under "## Abstract": authors and affiliations are dropped.
        ("9771708", ["ATPSK2", "brachymorphic"], ["Cohn DH", "Cedars-Sinai", "PMID:"]),
        # Abstract-only record whose abstract sits under "## Content".
        ("20237237", ["ENaC", "Nedd4-2"], ["McDonald FJ", "University of Otago"]),
        # Full text under "## Content" that opens with the PubMed block: the
        # abstract is read up to the block's DOI/PMID trailer, not the body.
        (
            "10339610",
            ["CcmABCDEFGH", "heme chaperone"],
            ["Schulz H", "Zürich", "PMCID"],
        ),
        # A byline with a generational suffix ("Wharton KA Jr") is still a byline.
        ("11274052", ["dishevelled"], ["Wharton", "Nusse R", "Cadigan KM"]),
        # NCBI's "New Collective Author" placeholder ends the byline, and a
        # "Collaborators:" paragraph follows it.
        ("9634588", ["IBC6", "cytokinin"], ["Brandstatter", "Kieber JJ", "Evans ML"]),
        # A group author after a semicolon ends a long consortium byline.
        ("24190013", ["ovarian"], ["Brooks-Wilson", "Pharoah PD", "Ramus SJ"]),
    ],
)
def test_abstract_text_reads_abstract_without_bibliography(pmid, present, absent):
    """The name check sees the title and abstract, not author lists or affiliations.

    A symbol that is also a surname or an institution word would otherwise read as
    the gene being named.
    """
    from ai_gene_review.tools.wrong_gene_leads import PUBLICATIONS_DIR, abstract_text

    text = abstract_text(PUBLICATIONS_DIR / f"PMID_{pmid}.md")
    assert all(p in text for p in present)
    assert not any(a in text for a in absent)


def test_undelimited_full_text_contributes_title_only():
    """Full text under "## Content" with no PubMed block gives the title only.

    Nothing marks where the abstract ends, and reading the body would make the
    check a full-text check.
    """
    from ai_gene_review.tools.wrong_gene_leads import PUBLICATIONS_DIR, abstract_text

    assert (
        abstract_text(PUBLICATIONS_DIR / "PMID_10357231.md")
        == "Glutamate synthase: a complex iron-sulfur flavoprotein."
    )


@pytest.mark.parametrize(
    "paragraph,expected",
    [
        # Ordinary words are not group authors unless capitalised.
        ("In the pilot study, cells were analyzed by FACS.", False),
        ("The network model, inputs were scaled by CNTF.", False),
        # A lowercase group word counts only after a semicolon, as in PubMed.
        ("In the consortium analysis, samples were typed by PCR.", False),
        # Unambiguous group words match in any case.
        ("Harold D, Lambert JC; GERAD consortium.", True),
        ("Earp MA(1), Kelemen LE; Australian Cancer Study; Lu Y.", True),
    ],
)
def test_group_author_matching_does_not_swallow_sentences(paragraph, expected):
    """Only unambiguous group words are case-insensitive, so prose is not a byline."""
    from ai_gene_review.tools.wrong_gene_leads import _is_author_list

    assert _is_author_list(paragraph) is expected


PUBLICATIONS = GENES.parent / "publications"


@pytest.mark.parametrize(
    "gene, pmid",
    [
        ("DROME/spz", "19018662"),  # "Spätzle": diacritic, name is "Protein spatzle"
        ("DROME/btl", "16831830"),  # "Breathless": name is "Protein breathless"
        ("SCHPO/cds1", "11027263"),  # "Cds1p-dependent": yeast protein suffix
        ("SCHPO/fas2", "9693066"),  # "lsd1+/fas2+": allele mark, slash pair
        ("SCHPO/idh1", "7903653"),  # "glu3": old name only PomBase lists
        ("human/ABL1", "18280240"),  # "c-Abl": cellular-homolog prefix
        ("human/AKR1C4", "21851338"),  # "AKR1C1-AKR1C4": a range
        ("human/ACADVL", "16020546"),  # "very-long-chain acyl-CoA dehydrogenase"
    ],
)
def test_name_forms_found_in_fourth_lead_batch(gene, pmid):
    """Each paper names the gene in a form the fourth lead review found missed."""
    own, _ = candidate_rows(GENES / gene)
    assert named_in_abstract(pmid, own.gene_names, PUBLICATIONS, own.protein_names)


@pytest.mark.parametrize(
    "gene, pmid",
    [
        ("human/ADAM17", "24990881"),  # "ADAM proteases" only
        ("human/ALDOB", "6696436"),  # muscle aldolase (ALDOA)
        ("DROME/rl", "8946916"),  # DJNK/basket
        ("mouse/Rbpj", "23571214"),  # BEND6
    ],
)
def test_confirmed_leads_stay_unnamed(gene, pmid):
    """Papers found to be about another gene must still not name the annotated one."""
    own, _ = candidate_rows(GENES / gene)
    assert (
        named_in_abstract(pmid, own.gene_names, PUBLICATIONS, own.protein_names)
        is False
    )


@pytest.mark.parametrize(
    "text, names, expected",
    [
        ("proteins (AKR1C1-AKR1C3) were assayed", {"AKR1C4"}, False),
        ("proteins (AKR1C1-AKR1C3) were assayed", {"AKR1C2"}, True),
        ("isoforms AKR1C1-4 were assayed", {"AKR1C4"}, True),
        ("phosphorylation by c-Abl", {"ABL2"}, False),
        ("phosphorylation by c-Abl", {"ABL"}, True),
        ("Rad21p was cleaved", {"RAD21"}, True),
        ("the Hsp70 chaperone", {"HSP7"}, False),
        ("GFP-tagged GDI/D4 was diffuse", {"GDID4"}, True),
    ],
)
def test_token_name_forms(tmp_path, text, names, expected):
    """Ranges, prefixes and suffixes are expanded without matching neighbours."""
    (tmp_path / "PMID_1.md").write_text(f"title: X\n## Abstract\n{text}\n")
    assert named_in_abstract("1", names, tmp_path) is expected


@pytest.mark.parametrize(
    "shared, expected",
    [
        (1, (1, "few_citing_entries")),
        (SHARED_ANNOTATION_GENES - 1, (1, "few_citing_entries")),
        (SHARED_ANNOTATION_GENES, (-1, "few_citing_entries;shared_by_many_genes")),
    ],
)
def test_rows_shared_by_many_genes_are_down_weighted(shared, expected):
    """A row its source gave to many genes (a complex, a proteomics list) ranks lower."""
    own = GeneRecord("P1", "9606", frozenset(), frozenset({"ABC1"}), frozenset())
    others = [CitingEntry("P2", "X", "10090", frozenset())]
    assert score_lead(own, others, None, shared) == expected


def test_shared_annotation_counts_real_complex_rows():
    """ComplexPortal's bBAF rows reach several local subunits; ALDOB's row does not."""
    dirs = list(GENES.glob("human/*"))
    counts = shared_annotation_counts(dirs)
    assert (
        counts[("PMID:12192000", "GO:0000785", "ComplexPortal")]
        >= SHARED_ANNOTATION_GENES
    )
    assert (
        1
        <= counts[("PMID:6696436", "GO:0004332", "Reactome")]
        < SHARED_ANNOTATION_GENES
    )
    assert (
        1
        <= counts[("PMID:24990881", "GO:0004175", "UniProt")]
        < SHARED_ANNOTATION_GENES
    )


def test_paralog_sharing_a_base_name_does_not_cancel_the_lead(tmp_path):
    """MDH1 and MDH2 differ only in their location qualifier, so the base name is shared."""
    own, _ = candidate_rows(GENES / "human/MDH2")
    mdh1 = CitingEntry(
        "P40925",
        "MDH1",
        "9606",
        frozenset(),
        frozenset({"Malate dehydrogenase, cytoplasmic"}),
    )
    (tmp_path / "PMID_1.md").write_text(
        "title: X\n## Abstract\nCytosolic malate dehydrogenase was purified.\n"
    )
    forms = gene_specific_names(own, [mdh1])
    assert named_in_abstract("1", own.gene_names, tmp_path, forms) is False


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Similar results were seen. Levels were similar in mutants.", False),
        ("We find that Similar binds Tango in the nucleus.", True),
    ],
)
def test_one_word_short_name_needs_a_capitalised_mention(tmp_path, text, expected):
    """DROME/sima is "Protein similar": prose "similar" must not name it."""
    own, _ = candidate_rows(GENES / "DROME/sima")
    (tmp_path / "PMID_1.md").write_text(f"title: X\n## Abstract\n{text}\n")
    assert (
        named_in_abstract("1", own.gene_names, tmp_path, own.protein_names) is expected
    )


def test_pombase_names_union_genes_sharing_an_accession():
    """Three histone H4 genes share P09322; every name must be kept."""
    names = pombase_names()["P09322"]
    assert {"hhf1", "hhf2", "hhf3", "h4.1", "h4.3"} <= names


@pytest.mark.parametrize("token, expanded", [("X1-X20", True), ("X1-X21", False)])
def test_range_expansion_is_capped(token, expanded):
    """A range is expanded only when it names at most MAX_RANGE (20) genes."""
    assert MAX_RANGE == 20
    assert ("X10" in token_forms(token)) is expanded


def test_short_name_that_cannot_be_prose_matches_case_insensitively(tmp_path):
    """rat/Jag1 is "Protein jagged-1": a hyphenated, numbered name needs no capital."""
    own, _ = candidate_rows(GENES / "rat/Jag1")
    (tmp_path / "PMID_1.md").write_text(
        "title: X\n## Abstract\nNotch signalling requires jagged-1 in the ear.\n"
    )
    assert named_in_abstract("1", own.gene_names, tmp_path, own.protein_names)


def test_title_case_title_does_not_name_a_one_word_gene():
    """DROME/tub is "Protein Tube"; "Polar Tube Proteins" in a Title-Case title is not it.

    Only the protein-name path is tested: tub also has the gene synonym "tube",
    which the gene-name token check matches in "polar tube" (a known limitation).
    """
    own, _ = candidate_rows(GENES / "DROME/tub")
    assert named_in_abstract("28031263", [], PUBLICATIONS, own.protein_names) is False
