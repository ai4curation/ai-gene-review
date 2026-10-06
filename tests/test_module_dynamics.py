"""Tests for declarative activation logic and executable-model scenarios.

Covers the ``activation_logic`` slot (translation and its consistency checks
against the declared connections), the exhaustive asynchronous attractor search
in :mod:`ai_gene_review.module_dynamics`, the scenarios curated on the real ERK
cascade module, the blocking validator hook, and the browser payload.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml

from ai_gene_review.module_boolean import (
    activation_logic_findings,
    module_file_to_boolean,
    module_to_boolean,
)
from ai_gene_review.module_dynamics import (
    attractors,
    boolean_model_payload,
    boolean_models,
    run_declared_scenarios,
)
from ai_gene_review.validation.module_validator import validate_executable_models

ROOT = Path(__file__).resolve().parents[1]
ERK = ROOT / "modules/erk_cascade.yaml"
PST = ROOT / "modules/bacterial_pst_phosphate_uptake.yaml"


def _toy(logic: Any = None) -> dict[str, Any]:
    """Two activators and one inhibitor converging on ``t``."""
    t: dict[str, Any] = {"id": "t", "label": "Target"}
    if logic is not None:
        t["activation_logic"] = logic
    return {
        "id": "MODULE:toy",
        "module": {
            "id": "toy",
            "label": "Toy",
            "parts": [
                {"node": {"id": "a", "label": "A"}},
                {"node": {"id": "b", "label": "B"}},
                {"node": {"id": "i", "label": "I"}},
                {"node": t},
            ],
            "connections": [
                {"source": "a", "target": "t", "connection_type": "CAUSES"},
                {"source": "b", "target": "t", "connection_type": "CAUSES"},
                {
                    "source": "i",
                    "target": "t",
                    "connection_type": "NEGATIVELY_REGULATES",
                },
            ],
        },
    }


@pytest.mark.parametrize(
    "logic,expected",
    [
        (None, "(a | b) & !i"),
        (
            {
                "all_of": [
                    {"element": "a"},
                    {"element": "b"},
                    {"none_of": [{"element": "i"}]},
                ]
            },
            "a & b & !i",
        ),
        (
            # activator overrides the inhibitor: a alone suffices
            {
                "any_of": [
                    {"element": "a"},
                    {"all_of": [{"element": "b"}, {"none_of": [{"element": "i"}]}]},
                ]
            },
            "a | (b & !i)",
        ),
    ],
)
def test_activation_logic_becomes_the_rule(logic: Any, expected: str) -> None:
    doc = _toy(logic)
    assert activation_logic_findings(doc) == []
    assert module_to_boolean(doc).rules["t"] == expected


@pytest.mark.parametrize(
    "logic,message",
    [
        (
            {"all_of": [{"element": "a"}, {"element": "b"}, {"element": "i"}]},
            "names i, which has no activating connection into t",
        ),
        (
            {
                "all_of": [
                    {"none_of": [{"element": "a"}]},
                    {"element": "b"},
                    {"none_of": [{"element": "i"}]},
                ]
            },
            "names a, which has no inhibiting connection into t",
        ),
        (
            {"all_of": [{"element": "a"}, {"none_of": [{"element": "i"}]}]},
            "regulator b has a connection into t but is not used",
        ),
        (
            {
                "all_of": [
                    {"element": "a"},
                    {"element": "b"},
                    {"element": "zz"},
                    {"none_of": [{"element": "i"}]},
                ]
            },
            "unknown element zz",
        ),
        (
            {"element": "a", "any_of": [{"element": "b"}]},
            "exactly one of element/all_of/any_of/none_of",
        ),
    ],
)
def test_inconsistent_activation_logic_is_reported(logic: Any, message: str) -> None:
    doc = _toy(logic)
    findings = activation_logic_findings(doc)
    assert any(message in f for f in findings), findings
    with pytest.raises(ValueError):
        module_to_boolean(doc)
    assert validate_executable_models(doc)


def test_activation_logic_on_a_flattened_container_is_rejected() -> None:
    doc = {
        "module": {
            "id": "m",
            "label": "m",
            "parts": [
                {"node": {"id": "s", "label": "s"}},
                {
                    "node": {
                        "id": "box",
                        "label": "box",
                        "activation_logic": {"element": "s"},
                        "parts": [
                            {"node": {"id": "x", "label": "x"}},
                            {"node": {"id": "y", "label": "y"}},
                        ],
                        "connections": [
                            {"source": "x", "target": "y", "connection_type": "CAUSES"}
                        ],
                    }
                },
            ],
            "connections": [
                {"source": "s", "target": "box", "connection_type": "CAUSES"}
            ],
        }
    }
    assert any("container" in f for f in activation_logic_findings(doc))


def test_pst_transporter_needs_both_inputs() -> None:
    """The curated ABC-transporter logic: capture AND ATPase, not either."""
    doc = yaml.safe_load(PST.read_text())
    assert activation_logic_findings(doc) == []
    model = module_file_to_boolean(PST)
    assert model.rules["pstsacb_phosphate_translocation"] == (
        "psts_phosphate_capture & pstb_energy_coupling"
    )
    only_capture = attractors(
        model, {"psts_phosphate_capture": True, "pstb_energy_coupling": False}
    )
    assert only_capture[0].always_off == [
        "pstsacb_phosphate_translocation",
        "pstb_energy_coupling",
    ]


@pytest.mark.parametrize(
    "fixed,kinds",
    [
        ({"a": False, "b": False, "i": False}, ["FIXED_POINT"]),
        ({"a": True, "b": False, "i": False}, ["FIXED_POINT"]),
        ({"a": True, "b": True, "i": True}, ["FIXED_POINT"]),
        ({}, ["FIXED_POINT"] * 8),  # every input combination is its own steady state
    ],
)
def test_attractors_of_a_feedforward_network(
    fixed: dict[str, bool], kinds: list[str]
) -> None:
    model = module_to_boolean(_toy())
    assert [a.kind for a in attractors(model, fixed)] == kinds


def test_negative_feedback_loop_has_a_cyclic_attractor_and_cutting_it_locks_on() -> (
    None
):
    doc = _toy()
    doc["module"]["connections"].append(
        {"source": "t", "target": "i", "connection_type": "CAUSES"}
    )
    model = module_to_boolean(doc)
    (cycle,) = attractors(model, {"a": True, "b": False})
    assert cycle.kind == "CYCLIC"
    assert cycle.oscillating == ["i", "t"]
    cut = module_to_boolean(doc, removed_connections={("t", "i")})
    (fixed,) = attractors(cut, {"a": True, "b": False, "i": False})
    assert fixed.kind == "FIXED_POINT" and "t" in fixed.always_on


def test_attractor_search_rejects_unknown_variables() -> None:
    with pytest.raises(KeyError):
        attractors(module_to_boolean(_toy()), {"nope": True})


def test_erk_declares_a_derived_boolean_model() -> None:
    doc = yaml.safe_load(ERK.read_text())
    (model,) = boolean_models(doc)
    assert model["id"] == "erk_cascade_boolean"
    ids = [s["id"] for s in model["scenarios"]]
    assert {"unstimulated", "sustained_stimulus", "feedback_cut"} <= set(ids)


def test_erk_scenarios_hold() -> None:
    doc = yaml.safe_load(ERK.read_text())
    results = run_declared_scenarios(doc)
    assert results and all(r.passed for r in results), [
        (r.scenario_id, r.failures) for r in results if not r.passed
    ]
    by_id = {r.scenario_id: r for r in results}
    assert [a.kind for a in by_id["sustained_stimulus"].attractors] == ["CYCLIC"]
    assert [a.kind for a in by_id["feedback_cut"].attractors] == ["FIXED_POINT"]
    assert validate_executable_models(doc) == []


@pytest.mark.parametrize(
    "scenario_id,slot,value,message",
    [
        (
            "sustained_stimulus",
            "expected_attractor_kind",
            "FIXED_POINT",
            "expected every attractor to be FIXED_POINT",
        ),
        (
            "unstimulated",
            "expected_attractor_count",
            2,
            "expected 2 attractor(s), got 1",
        ),
        (
            "feedback_cut",
            "expected_active",
            ["mapk_negative_regulation"],
            "is not always on",
        ),
        ("unstimulated", "expected_inactive", ["not_a_node"], "not a model variable"),
    ],
)
def test_a_wrong_expectation_is_a_validation_error(
    scenario_id: str, slot: str, value: Any, message: str
) -> None:
    doc = copy.deepcopy(yaml.safe_load(ERK.read_text()))
    (model,) = boolean_models(doc)
    scenario = next(s for s in model["scenarios"] if s["id"] == scenario_id)
    scenario[slot] = value
    errors = validate_executable_models(doc)
    assert any(scenario_id in e and message in e for e in errors), errors


def test_removing_an_undeclared_connection_is_reported() -> None:
    doc = copy.deepcopy(yaml.safe_load(ERK.read_text()))
    (model,) = boolean_models(doc)
    model["scenarios"][0]["removed_connections"] = [
        {"source": "erk_mapk", "target": "adaptor_recruitment"}
    ]
    assert any("is not declared" in e for e in validate_executable_models(doc))


def test_browser_payload_carries_rules_and_scenario_overrides() -> None:
    doc = yaml.safe_load(ERK.read_text())
    (model,) = boolean_models(doc)
    payload = boolean_model_payload(doc, model)
    variables = {v["id"]: v for v in payload["variables"]}
    assert variables["adaptor_recruitment"]["input"] is True
    assert payload["rules"]["raf_map3k"]["tree"] == [
        "and",
        ["ras_active", ["not", ["or", ["erk_mapk", "sprouty_spred_feedback"]]]],
    ]
    cut = next(s for s in payload["scenarios"] if s["id"] == "feedback_cut")
    assert (
        cut["rule_overrides"]["raf_map3k"]["text"]
        == "ras_active & !sprouty_spred_feedback"
    )
    assert cut["rule_overrides"]["mapk_negative_regulation"] is None  # now an input
    assert ["erk_mapk", "raf_map3k", "-"] in cut["removed_edges"]
    assert cut["attractors"][0]["kind"] == "FIXED_POINT"


def test_exhaustive_search_agrees_with_biodivine_aeon() -> None:
    """Cross-check the pure-Python search against AEON's symbolic algorithm."""
    aeon = pytest.importorskip("biodivine_aeon")
    model = module_file_to_boolean(ERK)
    fixed = {"adaptor_recruitment": True, "rasgap_step": False}
    ours = sorted(len(a.states) for a in attractors(model, fixed))
    bn = aeon.BooleanNetwork.from_bnet(model.with_inputs(fixed).to_bnet())
    graph = aeon.AsynchronousGraph(bn)
    theirs = sorted(int(a.cardinality()) for a in aeon.Attractors.attractors(graph))
    assert ours == theirs
