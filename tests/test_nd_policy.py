"""The ND acceptance rule (projects/NO_DATA.md) must be machine-enforced."""

import pytest

from ai_gene_review.validation.nd_policy import iter_nd_policy_violations


def nd(action, nd_case=None, term="GO:0003674", evidence="ND"):
    review = {"action": action}
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
