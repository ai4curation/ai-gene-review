"""The ND acceptance rule (projects/NO_DATA.md) must be machine-enforced."""

import pytest

from ai_gene_review.validation.nd_policy import iter_nd_policy_violations


SEARCH = "file:human/X/X-deep-research-falcon.md"


def nd(action, nd_case=None, term="GO:0003674", evidence="ND", searched=True):
    review = {"action": action}
    if searched:
        review["additional_reference_ids"] = [SEARCH]
    if nd_case:
        review["nd_case"] = nd_case
    return {"term": {"id": term}, "evidence_type": evidence, "review": review}


def fields(*annotations, **doc):
    data = {"existing_annotations": list(annotations), **doc}
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


@pytest.mark.parametrize("reference_id", [
    "PMID:12345", "DOI:10.1000/x", "PMC:PMC1", SEARCH,
    "file:DROME/CG42763/CG42763-notes.md",
    "file:human/X/X-deep-research-manual.md",
])
@pytest.mark.parametrize("slot", ["supported_by", "additional_reference_ids"])
def test_accept_citing_a_search_passes(reference_id, slot):
    row = nd("ACCEPT", searched=False)
    row["review"][slot] = (
        [{"reference_id": reference_id}] if slot == "supported_by" else [reference_id])
    assert fields(row) == []


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
