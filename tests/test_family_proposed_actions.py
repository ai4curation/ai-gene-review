"""Tests for the structured PAINT ``proposed_action`` on family-review node assessments."""
from __future__ import annotations

import pytest

from ai_gene_review.validation.family_residue_validator import (
    Outcome,
    check_proposed_actions,
    proposed_action_problem,
)

# A small family tree: PTN1 is the root; PTN2 and PTN3 are its two internal children;
# PTN4 sits below PTN2. Leaves are L1..L5.
UNDER = {
    "PTN1": ["L1", "L2", "L3", "L4", "L5"],
    "PTN2": ["L1", "L2", "L3"],
    "PTN4": ["L1", "L2"],
    "PTN3": ["L4", "L5"],
}
LEAVES = {"L1", "L2", "L3", "L4", "L5"}


def _assessment(verdict: str, node: str, action: str | None = None,
                target: str | None = None) -> dict:
    """Build a node assessment with an optional proposed action."""
    a: dict = {"node_id": f"PANTHER:{node}", "asserted_term": {"id": "GO:0000001"},
               "assessment": verdict}
    if action:
        a["proposed_action"] = {"paint_action": action}
        if target:
            a["proposed_action"]["target_node_id"] = f"PANTHER:{target}"
    return a


@pytest.mark.parametrize(
    "verdict,node,action,target",
    [
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"),
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN4"),
        ("TOO_DEEP", "PTN1", "REMOVE_IBD", None),
        ("WRONG_NODE", "PTN2", "MOVE_IBD", "PTN3"),
        ("WRONG_NODE", "PTN2", "REMOVE_IBD", None),
        ("NEEDS_PRUNING", "PTN1", "ADD_IKR", "PTN3"),
        ("NEEDS_PRUNING", "PTN2", "ADD_IRD", "PTN4"),
        ("LOSS_CONTRADICTED", "PTN2", "REMOVE_LOSS", None),
        ("LOSS_STALE", "PTN2", "REMOVE_LOSS", None),
        ("LOSS_TOO_BROAD", "PTN2", "MOVE_LOSS", "PTN4"),
    ],
)
def test_valid_actions(verdict: str, node: str, action: str, target: str | None) -> None:
    """Actions that fit the verdict and the tree pass."""
    assert proposed_action_problem(_assessment(verdict, node, action, target), UNDER) is None


@pytest.mark.parametrize(
    "verdict,node,action,target,fragment",
    [
        # action does not fit the verdict
        ("SOUND", "PTN1", "MOVE_IBD", "PTN2", "takes no proposed action"),
        ("LOSS_SUPPORTED", "PTN2", "REMOVE_LOSS", None, "takes no proposed action"),
        ("TOO_DEEP", "PTN1", "ADD_IKR", "PTN2", "not allowed for verdict TOO_DEEP"),
        ("NEEDS_PRUNING", "PTN1", "MOVE_IBD", "PTN2", "not allowed for verdict NEEDS_PRUNING"),
        # target presence
        ("NEEDS_PRUNING", "PTN1", "ADD_IKR", None, "needs a target_node_id"),
        ("TOO_DEEP", "PTN1", "REMOVE_IBD", "PTN2", "takes no target_node_id"),
        # tree relation
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN1", "is the assessed node itself"),
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN99", "not an internal node"),
        ("TOO_DEEP", "PTN2", "MOVE_IBD", "PTN1", "is not below"),
        ("NEEDS_PRUNING", "PTN2", "ADD_IKR", "PTN3", "is not below"),
        ("LOSS_TOO_BROAD", "PTN2", "MOVE_LOSS", "PTN3", "is not below"),
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "L1", "not an internal node"),
    ],
)
def test_invalid_actions(verdict: str, node: str, action: str, target: str | None,
                         fragment: str) -> None:
    """Mismatched verdicts, missing or extra targets and bad tree relations are reported."""
    problem = proposed_action_problem(_assessment(verdict, node, action, target), UNDER)
    assert problem is not None
    assert fragment in problem


def test_no_action_means_no_check() -> None:
    """An assessment without a proposed action produces no result at all."""
    review = {"family_id": "PANTHER:PTHR1",
              "node_assessments": [_assessment("TOO_DEEP", "PTN1")]}
    assert check_proposed_actions(review, lambda fam: {"under": UNDER}) == []


def test_check_reports_pass_and_fail() -> None:
    """check_proposed_actions turns each proposed action into one PASS or FAIL result."""
    review = {"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"),
        _assessment("NEEDS_PRUNING", "PTN2", "ADD_IKR", "PTN3"),
    ]}
    results = check_proposed_actions(review, lambda fam: {"under": UNDER})
    assert [r.outcome for r in results] == [Outcome.PASS, Outcome.FAIL]
    assert all(r.kind == "NODE_PROPOSED_ACTION" for r in results)


def test_tree_unavailable_is_unresolved_but_verdict_fit_still_checked() -> None:
    """Without a tree, the verdict/action pairing is still enforced; the tree relation is UNRESOLVED."""
    review = {"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"),
        _assessment("SOUND", "PTN1", "MOVE_IBD", "PTN2"),
    ]}
    results = check_proposed_actions(review, lambda fam: None)
    assert [r.outcome for r in results] == [Outcome.UNRESOLVED, Outcome.FAIL]


def test_family_tree_loaded_once_and_only_when_needed() -> None:
    """The tree loader is called only for reviews that carry a proposed action, and once."""
    calls: list[str] = []

    def loader(fam: str) -> dict:
        calls.append(fam)
        return {"under": UNDER}

    check_proposed_actions({"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("TOO_DEEP", "PTN1")]}, loader)
    assert calls == []
    check_proposed_actions({"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"),
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN4")]}, loader)
    assert calls == ["PTHR1"]
