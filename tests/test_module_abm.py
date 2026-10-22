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
