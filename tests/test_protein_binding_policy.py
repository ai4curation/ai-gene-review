"""The generic-protein-binding action policy must be machine-enforced.

Two reviews merged with deviations that four rounds of review did not catch, because
nothing checked it: a grep for ``0005515`` in the compliance module returned nothing.
"""

import pytest

from ai_gene_review.validation.protein_binding_policy import (
    PROTEIN_BINDING,
    iter_protein_binding_violations,
)


def doc(*actions: str, term: str = PROTEIN_BINDING) -> dict:
    return {
        "existing_annotations": [
            {"term": {"id": term}, "review": {"action": a}} for a in actions
        ]
    }


@pytest.mark.parametrize("action", ["MODIFY", "REMOVE", "UNDECIDED", "PENDING"])
def test_compliant_actions_pass(action):
    assert not list(iter_protein_binding_violations(doc(action)))


@pytest.mark.parametrize(
    "action", ["MARK_AS_OVER_ANNOTATED", "KEEP_AS_NON_CORE", "ACCEPT", "NEW"]
)
def test_non_compliant_actions_are_reported(action):
    (index, reported, explanation) = next(iter(iter_protein_binding_violations(doc(action))))
    assert (index, reported) == (0, action)
    assert explanation


def test_mark_as_over_annotated_message_names_the_policy_reason():
    """The policy excludes this action *by name*, so the message should say why."""
    (_, _, explanation) = next(
        iter(iter_protein_binding_violations(doc("MARK_AS_OVER_ANNOTATED")))
    )
    assert "not a claim exceeding the evidence" in explanation


def test_other_terms_are_untouched():
    """The policy is about GO:0005515 only.

    MARK_AS_OVER_ANNOTATED is entirely legitimate on other terms -- ARFGEF3 used it for a
    dead Sec7 domain that could still bind ARF -- so firing on them would be wrong.
    """
    assert not list(
        iter_protein_binding_violations(doc("MARK_AS_OVER_ANNOTATED", term="GO:0005096"))
    )


def test_reports_every_offending_row_with_its_index():
    violations = list(
        iter_protein_binding_violations(doc("REMOVE", "KEEP_AS_NON_CORE", "ACCEPT"))
    )
    assert [(i, a) for i, a, _ in violations] == [(1, "KEEP_AS_NON_CORE"), (2, "ACCEPT")]


@pytest.mark.parametrize(
    "malformed",
    [
        {},
        {"existing_annotations": None},
        {"existing_annotations": ["not a dict"]},
        {"existing_annotations": [{"term": None, "review": {"action": "ACCEPT"}}]},
        {"existing_annotations": [{"term": {"id": PROTEIN_BINDING}, "review": None}]},
        {"existing_annotations": [{"term": {"id": PROTEIN_BINDING}, "review": {}}]},
    ],
)
def test_malformed_documents_do_not_raise(malformed):
    """A lint rule must never be the thing that crashes validation."""
    assert list(iter_protein_binding_violations(malformed)) == []


def test_new_proposing_bare_protein_binding_is_flagged():
    """``NEW`` differs in kind from the others and is still not compliant.

    The other flagged actions mislabel an annotation GOA already made; ``NEW`` proposes a
    *fresh* bare protein-binding annotation, which CLAUDE.md rules out. Only three rows
    repo-wide do this, so the legacy-backlog argument for leniency does not apply.
    """
    (_, action, explanation) = next(iter(iter_protein_binding_violations(doc("NEW"))))
    assert action == "NEW"
    assert "more informative MF term" in explanation
