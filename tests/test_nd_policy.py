"""The ND acceptance rule (projects/NO_DATA.md) must be machine-enforced."""

import pytest

from ai_gene_review.validation.nd_policy import cites_search, iter_nd_policy_violations


SEARCH = "file:human/X/X-deep-research-falcon.md"
GENE = {"gene_symbol": "X", "id": "P12345"}


def nd(action, nd_case=None, term="GO:0003674", evidence="ND", searched=True):
    review = {"action": action}
    if searched:
        review["additional_reference_ids"] = ["PMID:1"]
    if nd_case:
        review["nd_case"] = nd_case
    return {"term": {"id": term}, "evidence_type": evidence, "review": review}


def fields(*annotations, **doc):
    data = {**GENE, "existing_annotations": list(annotations), **doc}
    return [(i, f) for i, f, _, _ in iter_nd_policy_violations(data)]


@pytest.mark.parametrize("nd_case", [None, "INFERABLE", "NEGATIVE"])
def test_accept_conformant_nd_passes(nd_case):
    assert fields(nd("ACCEPT", nd_case)) == []


@pytest.mark.parametrize("action", ["KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL", "NEW"])
def test_non_nd_actions_are_reported(action):
    assert fields(nd(action)) == [(0, "action")]


@pytest.mark.parametrize("action", ["REMOVE", "MODIFY"])
def test_remove_or_modify_needs_literature_case(action):
    assert fields(nd(action)) == [(0, "nd_case")]
    assert fields(nd(action, "INFERABLE")) == [(0, "nd_case")]
    assert fields(nd(action, "STALE")) == []
    assert fields(nd(action, "ONTOLOGY_BLOCKED")) == []


def test_accept_contradicts_stale():
    assert fields(nd("ACCEPT", "STALE")) == [(0, "nd_case")]


@pytest.mark.parametrize(
    "term,dark,ok",
    [
        ("GO:0003674", "MF_DARK", True),
        ("GO:0003674", "BP_DARK", False),
        ("GO:0008150", "BP_DARK", True),
        ("GO:0005575", "CC_DARK", True),
        ("GO:0005575", "WHOLLY_DARK", True),
    ],
)
def test_true_gap_needs_matching_biology_gap(term, dark, ok):
    gap = {"gap_statement": "x", "gap_kind": ["BIOLOGY"], "dark_aspect": dark}
    found = fields(nd("ACCEPT", "TRUE_GAP", term=term), knowledge_gaps=[gap])
    assert (found == []) is ok


def test_gap_may_sit_on_core_function_or_row():
    gap = {"gap_statement": "x", "gap_kind": ["BIOLOGY"], "dark_aspect": "MF_DARK"}
    assert fields(nd("ACCEPT", "EXISTENCE"), core_functions=[{"knowledge_gaps": [gap]}]) == []
    row = nd("ACCEPT", "EXISTENCE")
    row["review"]["knowledge_gaps"] = [gap]
    assert fields(row) == []


def test_ontology_only_gap_does_not_count():
    gap = {"gap_statement": "x", "gap_kind": ["ONTOLOGY"], "dark_aspect": "MF_DARK"}
    assert fields(nd("ACCEPT", "TRUE_GAP"), knowledge_gaps=[gap]) == [(0, "nd_case")]


def test_nd_case_on_non_nd_row_is_reported():
    assert fields(nd("ACCEPT", "INFERABLE", term="GO:0016787", evidence="IBA")) == [(0, "nd_case")]


def test_accept_with_replacement_terms_is_reported():
    """An accepted ND keeps the root term, so proposing a replacement contradicts it."""
    row = nd("ACCEPT", "INFERABLE")
    row["review"]["proposed_replacement_terms"] = [{"id": "GO:0016787", "label": "hydrolase activity"}]
    assert fields(row) == [(0, "proposed_replacement_terms")]


@pytest.mark.parametrize("reference_id", ["PMID:12345", "DOI:10.1000/x", "PMC:PMC1"])
@pytest.mark.parametrize("slot", ["supported_by", "additional_reference_ids"])
def test_accept_citing_a_publication_passes(reference_id, slot):
    row = nd("ACCEPT", searched=False)
    row["review"][slot] = (
        [{"reference_id": reference_id}] if slot == "supported_by" else [reference_id])
    assert fields(row) == []


@pytest.mark.parametrize("reference_id,supporting_text,passes", [
    (SEARCH, "no study of X was found", True),
    ("file:DROME/X/X-notes.md", 'PubMed (esearch "X": 0 records)', True),
    ("file:human/X/X-deep-research-manual.md", "no study of X was found", True),
    ("file:human/P12345/P12345-notes.md", "no study of X was found", True),
    # a search file must be quoted, so the verbatim check confirms it records a search
    (SEARCH, None, False),
    (SEARCH, "  ", False),
    # and must be the gene's own
    ("file:human/Y/Y-deep-research-falcon.md", "no study of Y was found", False),
])
def test_search_file_must_be_quoted_and_the_genes_own(reference_id, supporting_text, passes):
    row = nd("ACCEPT", searched=False)
    support = {"reference_id": reference_id}
    if supporting_text is not None:
        support["supporting_text"] = supporting_text
    row["review"]["supported_by"] = [support]
    assert (fields(row) == []) is passes


def test_search_file_in_additional_reference_ids_does_not_count():
    """additional_reference_ids carry no quote, so a file there cannot show a search."""
    row = nd("ACCEPT", searched=False)
    row["review"]["additional_reference_ids"] = [SEARCH]
    assert fields(row) == [(0, "supported_by")]


@pytest.mark.parametrize("supported_by", [
    [],
    [{"reference_id": "file:human/X/X-uniprot.txt", "supporting_text": "PE   1: Evidence at protein level;"}],
])
def test_accept_without_a_search_is_reported(supported_by):
    """The UniProt record, or the protein's existence level, is not a literature search."""
    row = nd("ACCEPT", searched=False)
    row["review"]["supported_by"] = supported_by
    assert fields(row) == [(0, "supported_by")]


def test_search_rule_applies_only_to_accept():
    assert fields(nd("REMOVE", "STALE", searched=False)) == []


def test_search_rule_ignores_non_nd_rows():
    assert fields(nd("ACCEPT", term="GO:0016787", evidence="IBA", searched=False)) == []


@pytest.mark.parametrize("reference_id,passes", [
    ("file:CANAL/X/X-notes.md", True),
    ("file:genes/CANAL/X/X-notes.md", True),
    ("file:CANAL/Y/Y-notes.md", False),
    ("file:genes/CANAL/Y/Y-notes.md", False),
])
def test_both_file_path_forms(reference_id, passes):
    """file:ORG/GENE/... and file:genes/ORG/GENE/... name the same file."""
    row = nd("ACCEPT", searched=False)
    row["review"]["supported_by"] = [{"reference_id": reference_id, "supporting_text": "0 records"}]
    assert (fields(row) == []) is passes


def test_same_organism_gene_is_not_the_genes_own():
    """file:genes/ORG/GENE/... is read as the gene folder, so another gene of the organism fails."""
    doc = {"gene_symbol": "ALG14", "id": "Q1"}
    other = {"supported_by": [{"reference_id": "file:genes/CANAL/ERG9/ERG9-notes.md", "supporting_text": "x"}]}
    own = {"supported_by": [{"reference_id": "file:genes/CANAL/ALG14/ALG14-notes.md", "supporting_text": "x"}]}
    assert not cites_search(other, doc)
    assert cites_search(own, doc)


@pytest.mark.parametrize("gene_dir,passes", [("SCHPO/rhp51", True), ("SCHPO/rad3", False)])
def test_review_path_gives_the_exact_folder(gene_dir, passes):
    """With the review's folder known, a synonym-named folder is recognised exactly."""
    doc = {"gene_symbol": "rad51", "id": "P36601"}
    review = {"supported_by": [{"reference_id": "file:SCHPO/rhp51/rhp51-notes.md", "supporting_text": "x"}]}
    assert cites_search(review, doc, gene_dir) is passes


def test_fulltext_quote_does_not_count_for_a_search_file():
    """supporting_text_fulltext is never checked against the file, so it cannot show a search."""
    review = {"supported_by": [{"reference_id": "file:CANAL/X/X-notes.md", "supporting_text_fulltext": "0 records"}]}
    assert not cites_search(review, GENE)


def test_fallback_does_not_borrow_an_orthologs_folder():
    """With no path, a cited ortholog UniProt file does not make its folder the gene's own."""
    doc = {"gene_symbol": "Map2k4", "id": "Q6AXP2",
           "references": [{"id": "file:human/MAP2K4/MAP2K4-uniprot.txt"}]}
    review = {"supported_by": [{"reference_id": "file:human/MAP2K4/MAP2K4-notes.md", "supporting_text": "x"}]}
    assert not cites_search(review, doc)


def test_validator_uses_the_review_path_without_goa(tmp_path, monkeypatch):
    """check_goa=False must not drop the review path: the own-folder test stays exact."""
    import yaml
    from ai_gene_review.validation import validate_gene_review

    gene_dir = tmp_path / "genes" / "SCHPO" / "rhp51"
    gene_dir.mkdir(parents=True)
    (gene_dir / "rhp51-notes.md").write_text("No study of rhp51 was found.\n")
    review = gene_dir / "rhp51-ai-review.yaml"
    row = {"term": {"id": "GO:0003674", "label": "molecular_function"}, "evidence_type": "ND",
           "original_reference_id": "GO_REF:0000015",
           "review": {"action": "ACCEPT", "reason": "x", "supported_by": [
               {"reference_id": "file:SCHPO/rhp51/rhp51-notes.md",
                "supporting_text": "No study of rhp51 was found."}]}}
    review.write_text(yaml.safe_dump({"id": "P36601", "gene_symbol": "rad51",
                                      "taxon": {"id": "NCBITaxon:4896", "label": "S. pombe"},
                                      "existing_annotations": [row]}))
    monkeypatch.setattr("ai_gene_review.validation.local_source_text.PROJECT_ROOT", tmp_path)
    report = validate_gene_review(review, check_goa=False, check_supporting_text=False)
    assert not [i for i in report.issues if i.check_type == "nd_policy"
                and "literature was searched" in i.message]


@pytest.mark.parametrize("mod", ["sgd", "flybase", "wormbase"])
def test_mod_gene_description_is_not_a_search_record(mod):
    """MOD gene descriptions are curator-written summaries, not a record of a literature search."""
    row = nd("ACCEPT", searched=False)
    row["review"]["supported_by"] = [
        {"reference_id": f"file:yeast/X/X-deep-research-{mod}.md", "supporting_text": "Protein of unknown function"}]
    assert fields(row) == [(0, "supported_by")]
