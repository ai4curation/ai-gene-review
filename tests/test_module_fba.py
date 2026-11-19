"""Tests for module-derived constraint-based metabolic models (FBA / pFBA / E-Flux).

Covers :mod:`ai_gene_review.module_fba`, its integration with
:func:`ai_gene_review.module_dynamics.run_declared_scenarios` and
:func:`ai_gene_review.validation.module_validator.validate_executable_models`,
curated FBA scenarios on ``glycerol_metabolism``, ``alcoholic_fermentation``,
and ``pdh_bypass_acetyl_coa_synthesis``, parity of the exact solver with the
pFBA linear program solved by scipy (HiGHS) and COBRApy, and conformance of the
browser solver ``templates/fba_solver.js`` with the Python one.
"""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

import cobra  # type: ignore[import-untyped]
import pytest
import yaml
from scipy.optimize import linprog

from ai_gene_review.module_dynamics import (
    run_declared_scenarios,
    unchecked_scenario_models,
)
from ai_gene_review.module_fba import (
    CORE_FLUX_COST,
    DEFAULT_UPPER_BOUND,
    DEFAULT_UPTAKE_RATE,
    OPTIONAL_BRANCH_FLUX_COST,
    OPTIONAL_BRANCH_UPPER_BOUND,
    FBAModel,
    FBASimulation,
    _fba_settings,
    _removed,
    fba_model_json,
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
CURATED = [GLYCEROL, FERMENTATION, PDH_BYPASS]
FBA_SOLVER_JS = ROOT / "src/ai_gene_review/templates/fba_solver.js"


@pytest.mark.parametrize("path", CURATED, ids=lambda p: p.stem)
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
    # The PRECEDES link between the synthesis and utilisation arms is an ordering
    # statement, not a metabolite handoff: it carries no flux, so the arms are
    # independent and each has its own entry and terminal.
    assert model.ordering_connections == [
        ("g3p_phosphatase_step", "PRECEDES", "glycerol_utilisation")
    ]
    assert ("g3p_phosphatase_step", "glycerol_kinase_step") not in tx_by_pair
    assert set(model.entry_reactions) == {
        "g3p_nad_dehydrogenase_step",
        "glycerol_kinase_step",
        "glycerol_dehydrogenase_step",
    }
    assert "g3p_phosphatase_step" in model.terminal_reactions

    # Baseline steady-state conservation: total uptake == total export, zero residuals
    wt = simulate_fba(model)
    assert wt.total_uptake_flux == pytest.approx(DEFAULT_UPTAKE_RATE)
    assert wt.total_export_flux == pytest.approx(DEFAULT_UPTAKE_RATE)
    assert all(abs(v) < 1e-6 for v in wt.mass_balance_residuals.values())
    # The three two-step routes are equally cheap and share one uptake budget;
    # the pFBA optimum is not unique and the first declared route takes all of it
    # (one vertex of the optimal face, as an LP solver returns). Scenarios
    # therefore state which arm they feed instead of relying on this order.
    assert wt.reaction_fluxes["g3p_phosphatase_step"] == pytest.approx(100.0)
    assert wt.reaction_fluxes["g3p_quinone_dehydrogenase_step"] == 0.0

    # Feeding only the utilisation arm, GUT1-GUT2 is the first declared route.
    catabolic = {"g3p_nad_dehydrogenase_step": False}
    wt_cat = simulate_fba(model, settings=catabolic)
    assert wt_cat.reaction_fluxes["g3p_quinone_dehydrogenase_step"] == pytest.approx(
        100.0
    )
    assert wt_cat.reaction_fluxes["dihydroxyacetone_kinase_step"] == 0.0

    # Knocking out terminal GUT2 forces upstream GUT1 (glycerol_kinase_step) to 0 at steady state
    gut2_ko = simulate_fba(
        model, settings={**catabolic, "g3p_quinone_dehydrogenase_step": False}
    )
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
            {"expected_inactive": ["g3p_phosphatase_step"]},
            "expected g3p_phosphatase_step to carry zero steady-state flux",
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


def _module_doc(module: dict[str, Any]) -> dict[str, Any]:
    """Wrap a synthetic module in a ModuleReview-shaped document."""
    return {"id": "synthetic", "title": "Synthetic", "module": module}


def _step(nid: str, **extra: Any) -> dict[str, Any]:
    return {"node": {"id": nid, "label": nid, **extra}}


def _flow(src: str, tgt: str) -> dict[str, str]:
    return {"source": src, "target": tgt, "connection_type": "PROVIDES_INPUT_FOR"}


RECONVERGING = _module_doc(
    {
        "id": "reconverging",
        "parts": [_step(n) for n in ("a", "x", "y", "t1", "t2")],
        "connections": [
            _flow("a", "x"),
            _flow("a", "y"),
            _flow("x", "t1"),
            _flow("x", "t2"),
            _flow("y", "t2"),
        ],
    }
)


def test_reconverging_routes_reach_the_lp_optimum() -> None:
    """X can use T1 or T2, Y only T2: the optimum sends X to T1 and Y to T2.

    A greedy split that divides X's flux between T1 and T2 without knowing Y also
    needs T2 strands Y's flux and exports less than the optimum.
    """
    model = module_to_fba(RECONVERGING)
    sim = simulate_fba(model, settings={"t1": 0.5, "t2": 0.5})
    assert sim.reaction_bounds["t1"] == pytest.approx(50.0)
    assert sim.reaction_bounds["t2"] == pytest.approx(50.0)
    assert sim.total_export_flux == pytest.approx(100.0)
    assert sim.total_export_flux == pytest.approx(_lp_max_export(model, sim))
    assert all(abs(v) < 1e-6 for v in sim.mass_balance_residuals.values())


def test_closed_cycle_is_a_model_failure_not_zero_flux() -> None:
    cycle = _module_doc(
        {
            "id": "cycle",
            "parts": [_step(n) for n in ("a", "b", "c")],
            "connections": [_flow("a", "b"), _flow("b", "c"), _flow("c", "a")],
        }
    )
    model = module_to_fba(cycle)
    assert model.entry_reactions == []
    assert len(model.structure_problems) == 2
    res = run_fba_scenario(cycle, "cycle_fba", {"id": "wt", "expected_active": ["a"]})
    assert any("no entry reaction" in f for f in res.failures)
    assert any("no terminal reaction" in f for f in res.failures)


def _isozyme_module(variants: list[dict[str, Any]]) -> dict[str, Any]:
    return _module_doc(
        {
            "id": "isozymes",
            "parts": [
                _step("supply"),
                _step("enzyme_step", variant_sets=[{"id": "vs", "variants": variants}]),
            ],
            "connections": [_flow("supply", "enzyme_step")],
        }
    )


def test_losing_one_redundant_isozyme_keeps_full_capacity() -> None:
    model = module_to_fba(
        _isozyme_module(
            [{"id": f"iso{i}", "label": f"iso{i}"} for i in (1, 2, 3)]
        )
    )
    one_lost = simulate_fba(model, settings={"iso3": False})
    assert one_lost.reaction_bounds["enzyme_step"] == pytest.approx(DEFAULT_UPPER_BOUND)
    all_lost = simulate_fba(
        model, settings={"iso1": False, "iso2": False, "iso3": False}
    )
    assert all_lost.reaction_fluxes["enzyme_step"] == 0.0
    partial = simulate_fba(
        model, settings={"iso1": 0.2, "iso2": 0.3, "iso3": False}
    )
    assert partial.reaction_bounds["enzyme_step"] == pytest.approx(50.0)


def test_leaf_variant_eflux_level_is_not_squared() -> None:
    model = module_to_fba(_isozyme_module([{"id": "only", "label": "only"}]))
    sim = simulate_fba(model, settings={"only": 0.5})
    assert sim.gpr_capacities["only"] == pytest.approx(0.5)
    assert sim.reaction_bounds["enzyme_step"] == pytest.approx(50.0)


def _cases() -> list[tuple[str, FBAModel, dict[str, bool | float]]]:
    """Every curated scenario plus knockouts of each reaction and GPR element."""
    out: list[tuple[str, FBAModel, dict[str, bool | float]]] = []
    for path in CURATED:
        doc = yaml.safe_load(path.read_text())
        base = module_to_fba(doc)
        out.append((f"{path.stem}:baseline", base, {}))
        for eid in sorted(base.controllable_ids):
            out.append((f"{path.stem}:ko:{eid}", base, {eid: False}))
            out.append((f"{path.stem}:half:{eid}", base, {eid: 0.5}))
        for entry in fba_models(doc):
            for sc in entry["scenarios"]:
                model = module_to_fba(doc, removed_connections=_removed(sc))
                out.append((f"{path.stem}:{sc['id']}", model, _fba_settings(sc)))
    out.append(
        ("reconverging", module_to_fba(RECONVERGING), {"t1": 0.5, "t2": 0.5})
    )
    return out


CASES = _cases()


def _lp_data(
    model: FBAModel, sim: FBASimulation
) -> tuple[list[str], list[tuple[str, str, float]], list[list[float]], list[float]]:
    """Variables (reaction then edge fluxes) and steady-state equalities of the pFBA LP."""
    rxns = [r.id for r in model.reactions if r.is_flow_stage]
    edges = [
        (t["source"], t["target"], t["upper_bound"]) for t in sim.transition_fluxes
    ]
    n = len(rxns) + len(edges)
    entries, terminals = set(model.entry_reactions), set(model.effective_terminals)
    a_eq: list[list[float]] = []
    for k, rid in enumerate(rxns):
        if rid not in entries:
            row = [0.0] * n
            row[k] = 1.0
            for j, (_s, t, _ub) in enumerate(edges):
                if t == rid:
                    row[len(rxns) + j] -= 1.0
            a_eq.append(row)
        if rid not in terminals:
            row = [0.0] * n
            row[k] = 1.0
            for j, (src, _t, _ub) in enumerate(edges):
                if src == rid:
                    row[len(rxns) + j] -= 1.0
            a_eq.append(row)
    return rxns, edges, a_eq, [0.0] * len(a_eq)


def _lp_max_export(model: FBAModel, sim: FBASimulation) -> float:
    rxns, edges, a_eq, b_eq = _lp_data(model, sim)
    entries, terminals = set(model.entry_reactions), set(model.effective_terminals)
    c = [-1.0 if rid in terminals else 0.0 for rid in rxns] + [0.0] * len(edges)
    uptake_row = [1.0 if rid in entries else 0.0 for rid in rxns] + [0.0] * len(edges)
    bounds = [(0.0, sim.reaction_bounds[rid]) for rid in rxns] + [
        (0.0, ub) for _s, _t, ub in edges
    ]
    res = linprog(
        c,
        A_ub=[uptake_row],
        b_ub=[sim.uptake_rate],
        A_eq=a_eq or None,
        b_eq=b_eq or None,
        bounds=bounds,
        method="highs",
    )
    assert res.status == 0, res.message
    return -float(res.fun)


def _weighted_l1(model: FBAModel, fluxes: dict[str, float]) -> float:
    return sum(
        fluxes[r.id]
        * (OPTIONAL_BRANCH_FLUX_COST if r.is_optional_branch else CORE_FLUX_COST)
        for r in model.reactions
        if r.is_flow_stage
    )


@pytest.mark.parametrize("case", CASES, ids=lambda c: c[0])
def test_exact_solver_matches_scipy_pfba_lp(
    case: tuple[str, FBAModel, dict[str, bool | float]],
) -> None:
    """Both pFBA stages agree with the LP: maximum export, then minimum weighted L1.

    Fluxes are compared through the two objectives, not reaction by reaction,
    because a pFBA optimum need not be unique.
    """
    _name, model, settings = case
    sim = simulate_fba(model, settings=settings)
    max_export = _lp_max_export(model, sim)
    assert sim.total_export_flux == pytest.approx(max_export, abs=1e-3)
    assert all(abs(v) < 1e-6 for v in sim.mass_balance_residuals.values())

    rxns, edges, a_eq, b_eq = _lp_data(model, sim)
    entries, terminals = set(model.entry_reactions), set(model.effective_terminals)
    cost = [
        OPTIONAL_BRANCH_FLUX_COST if r.is_optional_branch else CORE_FLUX_COST
        for r in model.reactions
        if r.is_flow_stage
    ] + [0.0] * len(edges)
    uptake_row = [1.0 if rid in entries else 0.0 for rid in rxns] + [0.0] * len(edges)
    export_row = [-1.0 if rid in terminals else 0.0 for rid in rxns] + [0.0] * len(
        edges
    )
    bounds = [(0.0, sim.reaction_bounds[rid]) for rid in rxns] + [
        (0.0, ub) for _s, _t, ub in edges
    ]
    res = linprog(
        cost,
        A_ub=[uptake_row, export_row],
        b_ub=[sim.uptake_rate, -(max_export - 1e-7)],
        A_eq=a_eq or None,
        b_eq=b_eq or None,
        bounds=bounds,
        method="highs",
    )
    assert res.status == 0, res.message
    assert _weighted_l1(model, sim.reaction_fluxes) == pytest.approx(
        float(res.fun), abs=1e-3
    )


@pytest.mark.parametrize(
    "case",
    [c for c in CASES if c[0].endswith(":baseline") or ":ko:" not in c[0]],
    ids=lambda c: c[0],
)
def test_exact_solver_matches_cobrapy(
    case: tuple[str, FBAModel, dict[str, bool | float]],
) -> None:
    """Maximum export agrees with the same network built and optimized in COBRApy."""
    name, model, settings = case
    sim = simulate_fba(model, settings=settings)
    cb = cobra.Model(name.replace(":", "_"))
    flow = [r for r in model.reactions if r.is_flow_stage]
    mets_in = {r.id: cobra.Metabolite(f"{r.id}_in", compartment="c") for r in flow}
    mets_out = {r.id: cobra.Metabolite(f"{r.id}_out", compartment="c") for r in flow}
    uptake_pool = cobra.Metabolite("uptake_pool", compartment="c")
    supply = cobra.Reaction("EX_supply", lower_bound=0.0, upper_bound=sim.uptake_rate)
    supply.add_metabolites({uptake_pool: 1.0})
    cb.add_reactions([supply])
    for r in flow:
        rxn = cobra.Reaction(r.id, lower_bound=0.0, upper_bound=sim.reaction_bounds[r.id])
        rxn.add_metabolites({mets_in[r.id]: -1.0, mets_out[r.id]: 1.0})
        cb.add_reactions([rxn])
    for idx, t in enumerate(sim.transition_fluxes):
        edge = cobra.Reaction(f"edge_{idx}", lower_bound=0.0, upper_bound=t["upper_bound"])
        edge.add_metabolites({mets_out[t["source"]]: -1.0, mets_in[t["target"]]: 1.0})
        cb.add_reactions([edge])
    for eid in model.entry_reactions:
        feed = cobra.Reaction(f"feed_{eid}", lower_bound=0.0, upper_bound=1000.0)
        feed.add_metabolites({uptake_pool: -1.0, mets_in[eid]: 1.0})
        cb.add_reactions([feed])
    exports = []
    for tid in model.effective_terminals:
        ex = cobra.Reaction(f"EX_{tid}", lower_bound=0.0, upper_bound=1000.0)
        ex.add_metabolites({mets_out[tid]: -1.0})
        cb.add_reactions([ex])
        exports.append(ex)
    cb.objective = {rxn: 1.0 for rxn in exports}
    sol = cb.optimize()
    assert sol.status == "optimal"
    assert sim.total_export_flux == pytest.approx(sol.objective_value, abs=1e-4)


def test_browser_solver_matches_python_solver() -> None:
    """``fba_solver.js`` run under Node reproduces ``simulate_fba`` on every case."""
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to execute the browser FBA solver")
    glycerol = yaml.safe_load(GLYCEROL.read_text())
    params = fba_model_payload(glycerol, fba_models(glycerol)[0])["parameters"]
    cases = [
        {"model": fba_model_json(model), "settings": settings}
        for _name, model, settings in CASES
    ]
    script = FBA_SOLVER_JS.read_text() + (
        "\nconst input = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
        "const out = input.cases.map(c => simulateFba(c.model, input.params, "
        "c.settings, input.params.uptake_rate));\n"
        "process.stdout.write(JSON.stringify(out));\n"
    )
    proc = subprocess.run(
        [node, "-e", script],
        input=json.dumps({"params": params, "cases": cases}),
        capture_output=True,
        text=True,
        check=True,
    )
    js_results = json.loads(proc.stdout)
    for (name, model, settings), js in zip(CASES, js_results, strict=True):
        py = simulate_fba(model, settings=settings)
        assert js["elementActive"] == py.element_active, name
        assert js["converged"] == py.converged, name
        for key, py_map in (
            ("gprCapacities", py.gpr_capacities),
            ("reactionBounds", py.reaction_bounds),
            ("reactionFluxes", py.reaction_fluxes),
        ):
            assert set(js[key]) == set(py_map), (name, key)
            for k, v in py_map.items():
                assert js[key][k] == pytest.approx(v, abs=1e-3), (name, key, k)
        assert [t["flux"] for t in js["transitionFluxes"]] == pytest.approx(
            [t["flux"] for t in py.transition_fluxes], abs=1e-3
        ), name
