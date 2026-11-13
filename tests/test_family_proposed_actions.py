"""Tests for the structured PAINT ``proposed_action`` on family-review node assessments."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.family_residue_validator import (
    ALLOWED_PAINT_ACTIONS,
    TARGETED_PAINT_ACTIONS,
    Outcome,
    check_proposed_actions,
    evaluate_proposed_action,
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
        # leaf targets: a loss or a move to a single gene
        ("NEEDS_PRUNING", "PTN1", "ADD_IKR", "L4"),
        ("NEEDS_PRUNING", "PTN2", "ADD_IRD", "L3"),
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "L1"),
        ("LOSS_TOO_BROAD", "PTN2", "MOVE_LOSS", "L1"),
        ("WRONG_NODE", "PTN2", "MOVE_IBD", "L5"),
    ],
)
def test_valid_actions(verdict: str, node: str, action: str, target: str | None) -> None:
    """Actions that fit the verdict and the tree pass, including leaf targets."""
    assert proposed_action_problem(
        _assessment(verdict, node, action, target), UNDER, LEAVES) is None


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
        ("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN99", "not a node of this family"),
        ("WRONG_NODE", "PTN2", "MOVE_IBD", "L99", "not a node of this family"),
        ("TOO_DEEP", "PTN2", "MOVE_IBD", "PTN1", "is not below"),
        ("NEEDS_PRUNING", "PTN2", "ADD_IKR", "PTN3", "is not below"),
        ("LOSS_TOO_BROAD", "PTN2", "MOVE_LOSS", "PTN3", "is not below"),
        # a leaf outside the assessed clade is not below it
        ("NEEDS_PRUNING", "PTN2", "ADD_IKR", "L4", "is not below"),
        # nothing lies below a leaf
        ("TOO_DEEP", "L1", "MOVE_IBD", "PTN2", "nothing lies below it"),
    ],
)
def test_invalid_actions(verdict: str, node: str, action: str, target: str | None,
                         fragment: str) -> None:
    """Mismatched verdicts, missing or extra targets and bad tree relations are reported."""
    problem = proposed_action_problem(
        _assessment(verdict, node, action, target), UNDER, LEAVES)
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


def test_single_child_chain_is_unresolved_not_fail() -> None:
    """Two nodes of a single-child chain share every leaf, so their order is undecidable.

    ``compact_tree`` keeps unary internal nodes, giving a parent and child identical leaf
    sets. A correct move along such a chain must not be rejected.
    """
    under = {"PTN1": ["L1", "L2"], "PTN2": ["L1", "L2"]}
    outcome, message = evaluate_proposed_action(
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"), under
    )
    assert outcome is Outcome.UNRESOLVED
    assert "single-child chain" in message
    assert proposed_action_problem(
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2"), under) is None


def test_action_table_matches_schema_enums() -> None:
    """ALLOWED_PAINT_ACTIONS covers every verdict and uses only declared PAINT actions.

    The table duplicates knowledge held in the schema; this pins the two together so a new
    verdict or action cannot silently fall through to "takes no proposed action".
    """
    schema = yaml.safe_load(Path("src/ai_gene_review/schema/family_review.yaml").read_text())
    verdicts = set(schema["enums"]["NodeAssessmentEnum"]["permissible_values"])
    actions = set(schema["enums"]["PaintActionEnum"]["permissible_values"])
    no_action = {"SOUND", "LOSS_SUPPORTED", "UNRESOLVED"}
    assert set(ALLOWED_PAINT_ACTIONS) | no_action == verdicts
    assert not set(ALLOWED_PAINT_ACTIONS) & no_action
    assert set().union(*ALLOWED_PAINT_ACTIONS.values()) == actions
    assert TARGETED_PAINT_ACTIONS <= actions


@pytest.mark.integration
def test_real_pthr24416_proposed_actions_check_out() -> None:
    """The committed PTHR24416 actions sit correctly in the real PANTHER tree.

    Fails, rather than going UNRESOLVED, if the tree cannot be fetched, so the claim that
    PTN007801558 is below PTN002400507 and PTN002400510 below PTN001230349 stays checkable.
    """
    from ai_gene_review.etl.panther_trees import load_family

    review = yaml.safe_load(
        Path("interpro/panther/PTHR24416/PTHR24416-review.yaml").read_text())
    results = check_proposed_actions(review, load_family)
    assert len(results) == 3, [str(r) for r in results]
    assert all(r.outcome is Outcome.PASS for r in results), [str(r) for r in results]


def test_leaf_known_only_from_leaf_table() -> None:
    """A leaf target needs the leaf table: without it, the leaf cannot be told from an
    id outside the family, so the check falls back to "not a node of this family"."""
    assessment = _assessment("NEEDS_PRUNING", "PTN1", "ADD_IKR", "L4")
    assert proposed_action_problem(assessment, UNDER, LEAVES) is None
    assert "not a node of this family" in (proposed_action_problem(assessment, UNDER) or "")


def test_check_passes_leaf_table_through() -> None:
    """check_proposed_actions uses the tree's leaf table, so a leaf target passes."""
    review = {"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("NEEDS_PRUNING", "PTN1", "ADD_IKR", "L4")]}
    tree = {"under": UNDER, "leaves": {leaf: {} for leaf in LEAVES}}
    results = check_proposed_actions(review, lambda fam: tree)
    assert [r.outcome for r in results] == [Outcome.PASS]


def test_tree_without_internal_nodes_is_unresolved() -> None:
    """A tree that parses but has no internal nodes is treated as unavailable."""
    review = {"family_id": "PANTHER:PTHR1", "node_assessments": [
        _assessment("TOO_DEEP", "PTN1", "MOVE_IBD", "PTN2")]}
    results = check_proposed_actions(review, lambda fam: {"under": {}, "leaves": {}})
    assert [r.outcome for r in results] == [Outcome.UNRESOLVED]
