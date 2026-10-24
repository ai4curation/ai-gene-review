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
    omitted_regulators,
)
from ai_gene_review.module_dynamics import (
    MAX_EXHAUSTIVE_VARIABLES,
    attractors,
    boolean_model_payload,
    boolean_models,
    run_declared_scenarios,
    run_scenario,
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
    assert validate_executable_models(doc, ROOT)[0]


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
    assert validate_executable_models(doc, ROOT) == ([], [])


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
        (
            "unstimulated",
            "expected_oscillating",
            ["erk_mapk"],
            "erk_mapk is not oscillating in every attractor",
        ),
    ],
)
def test_a_wrong_expectation_is_a_validation_error(
    scenario_id: str, slot: str, value: Any, message: str
) -> None:
    doc = copy.deepcopy(yaml.safe_load(ERK.read_text()))
    (model,) = boolean_models(doc)
    scenario = next(s for s in model["scenarios"] if s["id"] == scenario_id)
    scenario[slot] = value
    errors, _ = validate_executable_models(doc, ROOT)
    assert any(scenario_id in e and message in e for e in errors), errors


def test_removing_an_undeclared_connection_is_reported() -> None:
    doc = copy.deepcopy(yaml.safe_load(ERK.read_text()))
    (model,) = boolean_models(doc)
    model["scenarios"][0]["removed_connections"] = [
        {"source": "erk_mapk", "target": "adaptor_recruitment"}
    ]
    errors, _ = validate_executable_models(doc, ROOT)
    assert any("is not declared" in e for e in errors)


def _toy_with_scenario(scenario: dict[str, Any], logic: Any = None) -> dict[str, Any]:
    doc = _toy(logic)
    doc["executable_models"] = [
        {
            "id": "toy_boolean",
            "model_type": "BOOLEAN",
            "derivation": "DERIVED_FROM_MODULE",
            "scenarios": [scenario],
        }
    ]
    return doc


def test_removing_a_connection_named_by_activation_logic_is_reported_not_raised() -> (
    None
):
    logic = {
        "all_of": [{"element": "a"}, {"element": "b"}, {"none_of": [{"element": "i"}]}]
    }
    doc = _toy_with_scenario(
        {"id": "cut_b", "removed_connections": [{"source": "b", "target": "t"}]},
        logic,
    )
    errors, _ = validate_executable_models(doc, ROOT)
    assert any(
        "cut_b" in e
        and "removed_connections break an activation_logic" in e
        and "names b, which has no activating connection into t" in e
        for e in errors
    ), errors


def test_a_model_too_large_to_enumerate_is_reported_not_raised() -> None:
    ids = [f"n{i}" for i in range(MAX_EXHAUSTIVE_VARIABLES + 1)]
    doc = {
        "module": {
            "id": "chain",
            "label": "chain",
            "parts": [{"node": {"id": n, "label": n}} for n in ids],
            "connections": [
                {"source": a, "target": b, "connection_type": "CAUSES"}
                for a, b in zip(ids, ids[1:])
            ],
        },
        "executable_models": [
            {
                "id": "chain_boolean",
                "model_type": "BOOLEAN",
                "derivation": "DERIVED_FROM_MODULE",
                "scenarios": [{"id": "go", "expected_attractor_kind": "FIXED_POINT"}],
            }
        ],
    }
    errors, _ = validate_executable_models(doc, ROOT)
    assert any("exceeds the exhaustive limit" in e for e in errors), errors


def test_scenarios_on_an_external_model_warn_and_missing_files_error() -> None:
    doc = copy.deepcopy(yaml.safe_load(ERK.read_text()))
    external = next(
        m for m in doc["executable_models"] if m["derivation"] == "EXTERNAL"
    )
    external["scenarios"] = [{"id": "unchecked", "expected_attractor_kind": "CYCLIC"}]
    external["files"].append("models/boolean/no_such_model.bnet")
    errors, warnings = validate_executable_models(doc, ROOT)
    assert errors == [
        f"Executable model {external['id']}: file "
        "models/boolean/no_such_model.bnet does not exist"
    ]
    assert warnings == [
        f"Executable model {external['id']}: its scenarios are not checked "
        "(only module-derived Boolean models are simulated)"
    ]


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


def test_a_document_without_a_module_mapping_is_left_to_schema_validation() -> None:
    assert validate_executable_models({"id": "MODULE:x"}, ROOT) == ([], [])


def test_model_files_resolve_against_the_project_root_not_the_cwd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from ai_gene_review.validation.module_validator import validate_module_file

    monkeypatch.chdir(tmp_path)  # nothing under models/ exists here
    result = validate_module_file(
        ERK, resolver=lambda curie: ("unavailable", None, set())
    )
    assert not [e for e in result.errors if "does not exist" in e], result.errors


@pytest.mark.parametrize(
    "omitted,message",
    [
        (None, "regulator b has a connection into t but is not used"),
        (["b"], None),
        (["a"], "omitted_regulators names a, which its activation_logic uses"),
        (["zz"], "omitted_regulators names unknown element zz"),
    ],
)
def test_a_regulator_left_out_must_be_declared(omitted: Any, message: Any) -> None:
    """Leaving a modulator out is allowed only as a stated claim."""
    doc = _toy({"all_of": [{"element": "a"}, {"none_of": [{"element": "i"}]}]})
    if omitted is not None:
        doc["module"]["parts"][3]["node"]["omitted_regulators"] = omitted
    findings = activation_logic_findings(doc)
    if message is None:
        assert findings == []
        assert module_to_boolean(doc).rules["t"] == "a & !i"
        assert validate_executable_models(doc, ROOT) == ([], [])
    else:
        assert any(message in f for f in findings), findings


def test_omitted_regulators_without_activation_logic_is_an_error() -> None:
    doc = _toy()
    doc["module"]["parts"][3]["node"]["omitted_regulators"] = ["b"]
    assert activation_logic_findings(doc) == [
        "t: omitted_regulators without activation_logic"
    ]


def _modules_with_derived_boolean_models() -> list[Path]:
    paths = []
    for p in sorted((ROOT / "modules").glob("*.yaml")):
        text = p.read_text()
        if "DERIVED_FROM_MODULE" in text and "executable_models:" in text:
            paths.append(p)
    return paths


@pytest.mark.parametrize(
    "path", _modules_with_derived_boolean_models(), ids=lambda p: p.stem
)
def test_every_curated_scenario_holds(path: Path) -> None:
    doc = yaml.safe_load(path.read_text())
    results = run_declared_scenarios(doc)
    assert results, f"{path.stem} declares a derived Boolean model without scenarios"
    assert [(r.scenario_id, r.failures) for r in results if not r.passed] == []


def test_jak_stat_negative_regulators_act_where_the_module_says() -> None:
    """SOCS and PTPs on JAK; PTP and PIAS on nuclear STATs; ERK only tunes.

    The placement comes from child-level connections, so JAK activation needs
    no activation_logic and the drawn graph matches the rules.
    """
    doc = yaml.safe_load((ROOT / "modules/jak_stat_signaling.yaml").read_text())
    model = module_to_boolean(doc)
    assert model.rules["jak_activation"] == (
        "ligand_receptor_engagement & !(ptp_dephosphorylation | socs_feedback)"
    )
    inhibitors = {(e.source, e.target) for e in model.edges if e.sign == "-"}
    assert ("pias_restraint", "jak_activation") not in inhibitors
    assert ("socs_feedback", "stat_transcription") not in inhibitors
    assert model.rules["stat_transcription"] == (
        "stat_dimerization_import & !(ptp_dephosphorylation | pias_restraint)"
    )


def test_removing_an_omitted_regulator_does_not_break_the_logic() -> None:
    """An ERK-less counterfactual: the logic never used ERK, so cutting it is fine."""
    doc = yaml.safe_load((ROOT / "modules/jak_stat_signaling.yaml").read_text())
    model = boolean_models(doc)[0]
    sustained = next(s for s in model["scenarios"] if s["id"] == "sustained_cytokine")
    scenario = {
        **copy.deepcopy(sustained),
        "id": "erk_cut",
        "removed_connections": [
            {"source": "mapk_branch_interface", "target": "stat_transcription"}
        ],
    }
    removed = {("mapk_branch_interface", "stat_transcription")}
    assert activation_logic_findings(doc, removed_connections=removed) == []
    result = run_scenario(doc, "jak_stat_signaling_boolean", scenario)
    assert result.failures == []


def test_browser_payload_marks_omitted_regulators() -> None:
    doc = yaml.safe_load((ROOT / "modules/jak_stat_signaling.yaml").read_text())
    assert omitted_regulators(doc) == {"stat_transcription": ["mapk_branch_interface"]}
    payload = boolean_model_payload(doc, boolean_models(doc)[0])
    assert payload["omitted"] == {"stat_transcription": ["mapk_branch_interface"]}
    assert ["mapk_branch_interface", "stat_transcription", "+"] in payload["edges"]
