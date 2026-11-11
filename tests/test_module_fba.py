"""Tests for module-derived constraint-based metabolic models (FBA / pFBA / E-Flux).

Covers :mod:`ai_gene_review.module_fba`, its integration with
:func:`ai_gene_review.module_dynamics.run_declared_scenarios` and
:func:`ai_gene_review.validation.module_validator.validate_executable_models`,
curated FBA scenarios on ``glycerol_metabolism``, ``alcoholic_fermentation``,
and ``pdh_bypass_acetyl_coa_synthesis``, and parity with COBRApy LP solving.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml

from ai_gene_review.module_dynamics import (
    run_declared_scenarios,
    unchecked_scenario_models,
)
from ai_gene_review.module_fba import (
    DEFAULT_UPPER_BOUND,
    DEFAULT_UPTAKE_RATE,
    OPTIONAL_BRANCH_UPPER_BOUND,
    fba_model_payload,
    fba_models,
    module_to_fba,
    run_declared_fba_scenarios,
    run_fba_scenario,
    simulate_fba,
)
from ai_gene_review.validation.module_validator import validate_executable_models

ROOT = Path(__file__).resolve().parents[1]
GLYCEROL = ROOT / "modules/glycerol_metabolism.yaml"
FERMENTATION = ROOT / "modules/alcoholic_fermentation.yaml"
PDH_BYPASS = ROOT / "modules/pdh_bypass_acetyl_coa_synthesis.yaml"


@pytest.mark.parametrize(
    "path",
    [GLYCEROL, FERMENTATION, PDH_BYPASS],
    ids=lambda p: p.stem,
)
def test_curated_fba_modules_pass_all_scenarios(path: Path) -> None:
    doc = yaml.safe_load(path.read_text())
    assert unchecked_scenario_models(doc) == []
    fba_results = run_declared_fba_scenarios(doc)
    assert fba_results
    assert [(r.scenario_id, r.failures) for r in fba_results if not r.passed] == []
    all_results = run_declared_scenarios(doc)
    assert [(r.scenario_id, r.failures) for r in all_results if not r.passed] == []
    assert validate_executable_models(doc, ROOT) == ([], [])


def test_glycerol_metabolism_mass_balance_and_gut2_rerouting() -> None:
    doc = yaml.safe_load(GLYCEROL.read_text())
    model = module_to_fba(doc)
    rxn_by_id = model.reaction_map()
    assert set(rxn_by_id) == {
        "g3p_nad_dehydrogenase_step",
        "g3p_phosphatase_step",
        "glycerol_kinase_step",
        "g3p_quinone_dehydrogenase_step",
        "glycerol_dehydrogenase_step",
        "dihydroxyacetone_kinase_step",
    }
    # Shared metabolite inference across reaction transitions
    tx_by_pair = {(t.source, t.target): t for t in model.transitions}
    assert "sn-glycerol 3-phosphate" in tx_by_pair[
        ("g3p_nad_dehydrogenase_step", "g3p_phosphatase_step")
    ].shared_metabolites
    assert "dihydroxyacetone" in tx_by_pair[
        ("glycerol_dehydrogenase_step", "dihydroxyacetone_kinase_step")
    ].shared_metabolites

    # Baseline steady-state conservation: total uptake == total export, zero residuals
    wt = simulate_fba(model)
    assert wt.total_uptake_flux == pytest.approx(DEFAULT_UPTAKE_RATE)
    assert wt.total_export_flux == pytest.approx(DEFAULT_UPTAKE_RATE)
    assert all(abs(v) < 1e-6 for v in wt.mass_balance_residuals.values())
    assert wt.reaction_fluxes["g3p_quinone_dehydrogenase_step"] == pytest.approx(50.0)
    assert wt.reaction_fluxes["dihydroxyacetone_kinase_step"] == pytest.approx(50.0)

    # Knocking out terminal GUT2 forces upstream GUT1 (glycerol_kinase_step) to 0 at steady state
    gut2_ko = simulate_fba(model, settings={"g3p_quinone_dehydrogenase_step": False})
    assert gut2_ko.reaction_fluxes["g3p_quinone_dehydrogenase_step"] == 0.0
    assert gut2_ko.reaction_fluxes["glycerol_kinase_step"] == 0.0
    assert gut2_ko.reaction_fluxes["glycerol_dehydrogenase_step"] == pytest.approx(
        DEFAULT_UPTAKE_RATE
    )
    assert gut2_ko.reaction_fluxes["dihydroxyacetone_kinase_step"] == pytest.approx(
        DEFAULT_UPTAKE_RATE
    )
    assert all(abs(v) < 1e-6 for v in gut2_ko.mass_balance_residuals.values())


def test_alcoholic_fermentation_gpr_complex_and_overflow_routing() -> None:
    doc = yaml.safe_load(FERMENTATION.read_text())
    model = module_to_fba(doc)
    rxn_by_id = model.reaction_map()
    assert rxn_by_id["pdc_step"].upper_bound == pytest.approx(DEFAULT_UPPER_BOUND)
    assert rxn_by_id["pdc_carboligation_variant"].is_optional_branch is True
    assert rxn_by_id["pdc_carboligation_variant"].upper_bound == pytest.approx(
        OPTIONAL_BRANCH_UPPER_BOUND
    )

    # Carassius E1alpha3/E1beta2 complex is compiled as all_of (AND / min capacity)
    assert "carassius_alpha3 & carassius_beta2" in rxn_by_id["pdc_step"].gpr_rule_text

    # When canonical PDC is off, having both E1alpha3 and E1beta2 keeps pdc_step active
    both_subunits = simulate_fba(
        model,
        settings={
            "canonical_pdc_variant": False,
            "catabolic_als_step": False,
            "carassius_alpha3": True,
            "carassius_beta2": True,
        },
    )
    assert both_subunits.reaction_fluxes["pdc_step"] > 0.0
    assert both_subunits.reaction_fluxes["adh_step"] > both_subunits.reaction_fluxes["bdh_step"]

    # Knocking out a single complex subunit (carassius_alpha3) collapses pdc_step to 0
    one_subunit_ko = simulate_fba(
        model,
        settings={
            "canonical_pdc_variant": False,
            "catabolic_als_step": False,
            "carassius_alpha3": False,
            "carassius_beta2": True,
        },
    )
    assert one_subunit_ko.gpr_capacities["carassius_pdc_variant"] == 0.0
    assert one_subunit_ko.reaction_fluxes["pdc_step"] == 0.0
    assert one_subunit_ko.reaction_fluxes["adh_step"] == 0.0

    # Continuous E-Flux attenuation (50% expression on adh_step) scales UB_adh to 50.0
    eflux_half = simulate_fba(
        model,
        settings={"adh_step": 0.5, "catabolic_als_step": False},
    )
    assert eflux_half.reaction_bounds["adh_step"] == pytest.approx(50.0)
    assert eflux_half.reaction_fluxes["adh_step"] == pytest.approx(50.0)
    assert eflux_half.reaction_fluxes["bdh_step"] == pytest.approx(
        OPTIONAL_BRANCH_UPPER_BOUND
    )


def test_pdh_bypass_payload_and_acs_bottleneck() -> None:
    doc = yaml.safe_load(PDH_BYPASS.read_text())
    (entry,) = fba_models(doc)
    payload = fba_model_payload(doc, entry)
    assert payload["model_type"] == "CONSTRAINT_BASED"
    assert [r["id"] for r in payload["reactions"]] == [
        "acetaldehyde_supply",
        "acetaldehyde_dehydrogenase_step",
        "acetyl_coa_synthetase_step",
    ]
    assert all(s["failures"] == [] for s in payload["scenarios"])


@pytest.mark.parametrize(
    "scenario_patch,expected_msg",
    [
        (
            {
                "expected_active": ["g3p_quinone_dehydrogenase_step"],
                "settings": [
                    {"element": "g3p_quinone_dehydrogenase_step", "active": False}
                ],
            },
            "expected g3p_quinone_dehydrogenase_step to carry positive steady-state flux",
        ),
        (
            {"expected_inactive": ["g3p_quinone_dehydrogenase_step"]},
            "expected g3p_quinone_dehydrogenase_step to carry zero steady-state flux",
        ),
        (
            {
                "expected_outcome_order": [
                    "dihydroxyacetone_kinase_step",
                    "g3p_quinone_dehydrogenase_step",
                ],
                "settings": [
                    {"element": "glda_glycerol_dehydrogenase_activity", "active": False}
                ],
            },
            "expected_outcome_order violated",
        ),
        (
            {"expected_active": ["nonexistent_reaction"]},
            "expected_active names nonexistent_reaction, which is not a model reaction or GPR element",
        ),
        (
            {"settings": [{"element": "unknown_gene", "active": False}]},
            "settings name elements that are not model reactions or GPR elements",
        ),
        (
            {"expected_attractor_kind": "FIXED_POINT"},
            "expected_attractor_kind is not supported on CONSTRAINT_BASED scenarios",
        ),
        (
            {"expected_outcome_order": ["g3p_quinone_dehydrogenase_step"]},
            "expected_outcome_order requires at least 2 reactions to compare",
        ),
    ],
)
def test_fba_scenario_failure_diagnostics(
    scenario_patch: dict[str, Any], expected_msg: str
) -> None:
    doc = copy.deepcopy(yaml.safe_load(GLYCEROL.read_text()))
    scenario = {"id": "bad_fba_scenario", **scenario_patch}
    res = run_fba_scenario(doc, "glycerol_metabolism_fba", scenario)
    assert not res.passed
    assert any(expected_msg in f for f in res.failures), res.failures


def test_pure_python_fba_agrees_with_cobrapy_lp() -> None:
    """Cross-check pure-Python steady-state FBA solver against COBRApy LP optimization."""
    cobra = pytest.importorskip("cobra")
    doc = yaml.safe_load(PDH_BYPASS.read_text())
    fba_model = module_to_fba(doc)

    for settings in [
        {},
        {"ethanol_oxidation_variant": False},
        {"cytosolic_aldh_variant": False},
        {"acetyl_coa_synthetase_step": False},
    ]:
        ours = simulate_fba(fba_model, settings=settings)

        # Build equivalent stoichiometric LP in COBRApy
        cb = cobra.Model("pdh_bypass_check")
        mets_in = {
            r.id: cobra.Metabolite(f"{r.id}_in", compartment="c")
            for r in fba_model.reactions
        }
        mets_out = {
            r.id: cobra.Metabolite(f"{r.id}_out", compartment="c")
            for r in fba_model.reactions
        }
        for r in fba_model.reactions:
            rxn = cobra.Reaction(r.id)
            rxn.lower_bound = 0.0
            rxn.upper_bound = ours.reaction_bounds[r.id]
            rxn.add_metabolites({mets_in[r.id]: -1.0, mets_out[r.id]: 1.0})
            cb.add_reactions([rxn])

        for idx, t in enumerate(fba_model.transitions):
            edge_rxn = cobra.Reaction(f"edge_{idx}_{t.source}_to_{t.target}")
            edge_rxn.lower_bound = 0.0
            edge_rxn.upper_bound = ours.transition_fluxes[idx]["upper_bound"]
            edge_rxn.add_metabolites(
                {mets_out[t.source]: -1.0, mets_in[t.target]: 1.0}
            )
            cb.add_reactions([edge_rxn])

        for eid in fba_model.entry_reactions:
            ex_in = cobra.Reaction(f"EX_in_{eid}")
            ex_in.lower_bound = 0.0
            ex_in.upper_bound = DEFAULT_UPTAKE_RATE
            ex_in.add_metabolites({mets_in[eid]: 1.0})
            cb.add_reactions([ex_in])

        export_rxns = []
        for tid in fba_model.effective_terminals:
            ex_out = cobra.Reaction(f"EX_out_{tid}")
            ex_out.lower_bound = 0.0
            ex_out.upper_bound = 1000.0
            ex_out.add_metabolites({mets_out[tid]: -1.0})
            cb.add_reactions([ex_out])
            export_rxns.append(ex_out)

        cb.objective = {rxn: 1.0 for rxn in export_rxns}
        sol = cb.optimize()
        assert sol.status == "optimal"
        assert ours.total_export_flux == pytest.approx(sol.objective_value, abs=1e-4)
        for r in fba_model.reactions:
            assert ours.reaction_fluxes[r.id] == pytest.approx(
                sol.fluxes[r.id], abs=1e-4
            )
