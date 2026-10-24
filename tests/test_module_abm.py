"""Tests for module-derived agent-based trafficking models (ABM).

Covers :mod:`ai_gene_review.module_abm`, its integration with
:func:`ai_gene_review.module_dynamics.run_declared_scenarios` and
:func:`ai_gene_review.validation.module_validator.validate_executable_models`,
and the curated endosomal routing and LDLR endocytosis ABM scenarios.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml

from ai_gene_review.module_abm import (
    DEFAULT_BASE_RATE,
    DEFAULT_N_AGENTS,
    DEFAULT_N_STEPS,
    abm_model_payload,
    abm_models,
    module_to_abm,
    run_abm_scenario,
    run_declared_abm_scenarios,
    simulate_abm,
)
from ai_gene_review.module_dynamics import (
    run_declared_scenarios,
    run_scenario,
    unchecked_scenario_models,
)
from ai_gene_review.validation.module_validator import validate_executable_models

ROOT = Path(__file__).resolve().parents[1]
ENDOSOMAL = ROOT / "modules/endosomal_trafficking_routing.yaml"
LDLR = ROOT / "modules/ldl_receptor_mediated_endocytosis.yaml"


def _toy_trafficking_doc() -> dict[str, Any]:
    """Toy trafficking module with uptake -> early -> (recycling | late | escape) and a pure regulator."""
    return {
        "id": "MODULE:toy_trafficking",
        "title": "Toy Trafficking",
        "module": {
            "id": "toy_trafficking",
            "label": "Toy Trafficking",
            "parts": [
                {"node": {"id": "uptake", "label": "Receptor uptake"}},
                {"node": {"id": "early_endosome", "label": "Early endosome"}},
                {"node": {"id": "erc_recycling", "label": "ERC recycling"}},
                {"node": {"id": "late_endosome", "label": "Late endosome maturation"}},
                {"node": {"id": "cytosol_escape", "label": "Cytosol escape"}},
                {"node": {"id": "lysosome_sink", "label": "Lysosome degradation"}},
                {"node": {"id": "endocytosis_inhibitor", "label": "Uptake inhibitor"}},
            ],
            "connections": [
                {
                    "source": "uptake",
                    "target": "early_endosome",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {
                    "source": "early_endosome",
                    "target": "erc_recycling",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {
                    "source": "early_endosome",
                    "target": "late_endosome",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {
                    "source": "early_endosome",
                    "target": "cytosol_escape",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {
                    "source": "late_endosome",
                    "target": "lysosome_sink",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {
                    "source": "late_endosome",
                    "target": "cytosol_escape",
                    "connection_type": "NEGATIVELY_REGULATES",
                },
                {
                    "source": "endocytosis_inhibitor",
                    "target": "early_endosome",
                    "connection_type": "NEGATIVELY_REGULATES",
                },
            ],
        },
    }


def test_module_to_abm_extracts_stages_and_transitions() -> None:
    doc = _toy_trafficking_doc()
    model = module_to_abm(doc)
    by_id = model.stage_map()
    assert by_id["uptake"].is_entry is True
    assert by_id["erc_recycling"].is_terminal is True
    assert by_id["cytosol_escape"].is_terminal is True
    assert by_id["lysosome_sink"].is_terminal is True
    assert by_id["endocytosis_inhibitor"].is_flow_stage is False
    assert by_id["endocytosis_inhibitor"].default_active is False

    tx_by_pair = {(t.source, t.target): t for t in model.transitions}
    assert tx_by_pair[("early_endosome", "erc_recycling")].base_rate == pytest.approx(
        DEFAULT_BASE_RATE
    )
    assert tx_by_pair[("early_endosome", "cytosol_escape")].competing_inhibitors == (
        "late_endosome",
    )
    assert tx_by_pair[("uptake", "early_endosome")].gate_inhibitors == (
        "endocytosis_inhibitor",
    )


def test_simulate_abm_conserves_particles_and_diverts_flux_on_branch_ko() -> None:
    model = module_to_abm(_toy_trafficking_doc())
    wt = simulate_abm(model)
    assert len(wt.trajectory) == DEFAULT_N_STEPS + 1
    for counts in wt.trajectory:
        assert sum(counts.values()) == DEFAULT_N_AGENTS

    ko_late = simulate_abm(model, settings={"late_endosome": False})
    for counts in ko_late.trajectory:
        assert sum(counts.values()) == DEFAULT_N_AGENTS
    assert ko_late.final_counts["lysosome_sink"] == 0
    assert (
        ko_late.final_counts["cytosol_escape"]
        > wt.final_counts["cytosol_escape"] * 3
    )


def test_pure_regulator_blocks_target_transition_when_locked_on() -> None:
    model = module_to_abm(_toy_trafficking_doc())
    sim = simulate_abm(model, settings={"endocytosis_inhibitor": True})
    assert sim.final_counts["uptake"] == DEFAULT_N_AGENTS
    assert sim.final_counts["early_endosome"] == 0


def test_run_abm_scenario_rejects_unknown_stage_in_settings() -> None:
    doc = _toy_trafficking_doc()
    res = run_abm_scenario(
        doc,
        "toy_abm",
        {"id": "bad_setting", "settings": [{"element": "no_such_stage", "active": False}]},
    )
    assert not res.passed
    assert any("settings name elements that are not model stages" in f for f in res.failures)


@pytest.mark.parametrize("path", [ENDOSOMAL, LDLR], ids=lambda p: p.stem)
def test_curated_abm_modules_pass_all_scenarios(path: Path) -> None:
    doc = yaml.safe_load(path.read_text())
    assert unchecked_scenario_models(doc) == []
    abm_results = run_declared_abm_scenarios(doc)
    assert abm_results
    assert [(r.scenario_id, r.failures) for r in abm_results if not r.passed] == []
    all_results = run_declared_scenarios(doc)
    assert [(r.scenario_id, r.failures) for r in all_results if not r.passed] == []
    assert validate_executable_models(doc, ROOT) == ([], [])


def test_endosomal_trafficking_rab7_loss_boosts_cytosolic_escape() -> None:
    doc = yaml.safe_load(ENDOSOMAL.read_text())
    model = module_to_abm(ENDOSOMAL)
    wt = simulate_abm(model)
    rab7_ko = simulate_abm(model, settings={"escrt_rab7_late_endosome": False})

    assert wt.final_counts["ehd1_recycling_branch"] > wt.final_counts["cytosolic_cargo_escape"]
    assert wt.final_counts["ctsd_lysosomal_degradation"] > wt.final_counts["cytosolic_cargo_escape"]
    assert wt.final_counts["cytosolic_cargo_escape"] == 10

    assert rab7_ko.final_counts["ctsd_lysosomal_degradation"] == 0
    assert (
        rab7_ko.final_counts["cytosolic_cargo_escape"]
        >= wt.final_counts["cytosolic_cargo_escape"] * 4
    )

    (abm_entry,) = abm_models(doc)
    payload = abm_model_payload(doc, abm_entry)
    assert payload["model_type"] == "AGENT_BASED"
    assert len(payload["stages"]) == 7
    assert len(payload["scenarios"]) == 6
    assert all(s["failures"] == [] for s in payload["scenarios"])


@pytest.mark.parametrize(
    "scenario_patch,expected_msg",
    [
        (
            {
                "expected_active": ["ctsd_lysosomal_degradation"],
                "settings": [
                    {"element": "clathrin_ap2_internalization", "active": False}
                ],
            },
            "expected ctsd_lysosomal_degradation to be active/reached",
        ),
        (
            {"expected_inactive": ["ehd1_recycling_branch"]},
            "expected ehd1_recycling_branch to be inactive/unreached",
        ),
        (
            {
                "expected_outcome_order": [
                    "cytosolic_cargo_escape",
                    "ehd1_recycling_branch",
                ]
            },
            "expected_outcome_order violated",
        ),
        (
            {"expected_active": ["nonexistent_stage"]},
            "expected_active names nonexistent_stage, which is not a model stage",
        ),
    ],
)
def test_abm_scenario_failure_diagnostics(
    scenario_patch: dict[str, Any], expected_msg: str
) -> None:
    doc = copy.deepcopy(yaml.safe_load(ENDOSOMAL.read_text()))
    scenario = {"id": "bad_scenario", **scenario_patch}
    res = run_abm_scenario(doc, "endosomal_trafficking_abm", scenario)
    assert not res.passed
    assert any(expected_msg in f for f in res.failures), res.failures


def test_removed_connections_preserves_stage_topology_and_expands_containers() -> None:
    doc = {
        "id": "MODULE:container_trafficking",
        "title": "Container Trafficking",
        "module": {
            "id": "container_trafficking",
            "label": "Container Trafficking",
            "parts": [
                {"node": {"id": "entry", "label": "Entry"}},
                {"node": {"id": "mid", "label": "Mid"}},
                {"node": {"id": "booster", "label": "Booster"}},
                {
                    "node": {
                        "id": "sink_group",
                        "label": "Sink Group",
                        "parts": [
                            {"node": {"id": "sink_a", "label": "Sink A"}},
                            {"node": {"id": "sink_b", "label": "Sink B"}},
                        ],
                    }
                },
            ],
            "connections": [
                {"source": "entry", "target": "mid", "connection_type": "PROVIDES_INPUT_FOR"},
                {"source": "mid", "target": "sink_group", "connection_type": "PROVIDES_INPUT_FOR"},
                {"source": "booster", "target": "sink_a", "connection_type": "POSITIVELY_REGULATES"},
            ],
        },
        "executable_models": [
            {
                "id": "container_abm",
                "model_type": "AGENT_BASED",
                "derivation": "DERIVED_FROM_MODULE",
                "scenarios": [
                    {
                        "id": "sever_entry_to_mid",
                        "removed_connections": [{"source": "entry", "target": "mid"}],
                        "expected_active": ["entry"],
                        "expected_inactive": ["mid", "sink_a", "sink_b"],
                    },
                    {
                        "id": "sever_container_edge",
                        "removed_connections": [{"source": "mid", "target": "sink_group"}],
                        "expected_active": ["entry", "mid"],
                        "expected_inactive": ["sink_a", "sink_b"],
                    },
                ],
            }
        ],
    }
    results = run_declared_abm_scenarios(doc)
    assert len(results) == 2
    assert [(r.scenario_id, r.failures) for r in results if not r.passed] == []

    # Removing entry -> mid must not promote mid to an entry stage or drop entry from stages
    abm_cut = module_to_abm(doc, removed_connections=[("entry", "mid")])
    assert abm_cut.entry_stages == ["entry"]
    assert "entry" in abm_cut.stage_map()
    assert "mid" in abm_cut.stage_map()

    # Container-level removed_connections expand to leaf pairs in payload
    payload = abm_model_payload(doc, doc["executable_models"][0])
    sc_by_id = {s["id"]: s for s in payload["scenarios"]}
    assert sc_by_id["sever_container_edge"]["removed_connections"] == [
        {"source": "mid", "target": "sink_a"},
        {"source": "mid", "target": "sink_b"},
    ]


def test_omitted_regulators_and_activation_logic_in_abm() -> None:
    doc = {
        "id": "MODULE:logic_trafficking",
        "title": "Logic Trafficking",
        "module": {
            "id": "logic_trafficking",
            "label": "Logic Trafficking",
            "parts": [
                {"node": {"id": "uptake", "label": "Uptake"}},
                {"node": {"id": "mod_a", "label": "Modulator A"}},
                {"node": {"id": "mod_b", "label": "Modulator B"}},
                {"node": {"id": "mod_omitted", "label": "Omitted Modulator"}},
                {
                    "node": {
                        "id": "target_compartment",
                        "label": "Target",
                        "omitted_regulators": ["mod_omitted"],
                        "activation_logic": {
                            "all_of": [
                                {"element": "uptake"},
                                {"any_of": [{"element": "mod_a"}, {"element": "mod_b"}]},
                            ]
                        },
                    }
                },
            ],
            "connections": [
                {"source": "uptake", "target": "target_compartment", "connection_type": "PROVIDES_INPUT_FOR"},
                {"source": "mod_a", "target": "target_compartment", "connection_type": "POSITIVELY_REGULATES"},
                {"source": "mod_b", "target": "target_compartment", "connection_type": "POSITIVELY_REGULATES"},
                {"source": "mod_omitted", "target": "target_compartment", "connection_type": "NEGATIVELY_REGULATES"},
            ],
        },
    }
    # With OR activation_logic on (mod_a, mod_b) and mod_omitted declared in omitted_regulators,
    # locking mod_a ON (while mod_b is OFF and mod_omitted is ON) still opens target_compartment.
    res = run_abm_scenario(
        doc,
        "logic_abm",
        {
            "id": "or_gate_open",
            "settings": [
                {"element": "mod_a", "active": True},
                {"element": "mod_b", "active": False},
                {"element": "mod_omitted", "active": True},
            ],
            "expected_active": ["uptake", "mod_a", "mod_omitted", "target_compartment"],
            "expected_inactive": ["mod_b"],
        },
    )
    assert res.passed, res.failures


def test_oscillating_regulator_loop_reports_non_convergence() -> None:
    doc = {
        "id": "MODULE:osc_reg",
        "title": "Oscillating Regulators",
        "module": {
            "id": "osc_reg",
            "label": "Oscillating Regulators",
            "parts": [
                {"node": {"id": "cargo_entry", "label": "Entry"}},
                {"node": {"id": "reg_a", "label": "Reg A"}},
                {"node": {"id": "reg_b", "label": "Reg B"}},
            ],
            "connections": [
                {"source": "cargo_entry", "target": "reg_a", "connection_type": "POSITIVELY_REGULATES"},
                {"source": "reg_a", "target": "reg_b", "connection_type": "POSITIVELY_REGULATES"},
                {"source": "reg_b", "target": "reg_a", "connection_type": "NEGATIVELY_REGULATES"},
            ],
        },
    }
    res = run_abm_scenario(doc, "osc_abm", {"id": "osc_check"})
    assert not res.passed
    assert any("did not converge" in f for f in res.failures), res.failures


def test_cross_model_scenario_slots_rejected() -> None:
    doc = _toy_trafficking_doc()
    abm_res = run_abm_scenario(
        doc,
        "toy_abm",
        {
            "id": "boolean_slots_on_abm",
            "expected_attractor_kind": "FIXED_POINT",
            "expected_attractor_count": 1,
            "expected_oscillating": ["uptake"],
        },
    )
    assert not abm_res.passed
    assert any("is not supported on AGENT_BASED scenarios" in f for f in abm_res.failures)

    bool_res = run_scenario(
        doc,
        "toy_bool",
        {
            "id": "abm_slot_on_boolean",
            "expected_outcome_order": ["erc_recycling", "cytosol_escape"],
        },
    )
    assert not bool_res.passed
    assert any("expected_outcome_order is not supported on BOOLEAN scenarios" in f for f in bool_res.failures)

