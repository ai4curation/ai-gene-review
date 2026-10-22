"""Derive and simulate agent-based models (ABMs) from module definitions.

In intracellular trafficking and delivery pathways, cargo entities (receptors,
ligands, viral particles, lipid nanoparticles) move as discrete agents across
subcellular compartments and compete across branching sorting routes. Unlike
Boolean networks—where all downstream branches of an active sorting hub turn
``ON`` simultaneously—an agent-based model conserves discrete cargo particles
across compartments:

* **Flow connections** (``PROVIDES_INPUT_FOR``, ``PRECEDES``, ``CAUSES``,
  ``HAS_OUTPUT``) define directed cargo transport transitions between stages.
* **Branch competition & negative regulation** (``NEGATIVELY_REGULATES``,
  ``INHIBITS``, ``PREVENTS``):
  - When a competing flow stage :math:`w` negatively regulates stage :math:`v`
    (for example, Rab7-mediated late endosome maturation limiting endosomal
    dwell time and cytosolic escape), an active :math:`w` attenuates the
    per-step transition rate into :math:`v` (:math:`\\times 0.25`). Knocking
    out :math:`w` both closes flux into :math:`w` and lifts the attenuation on
    :math:`v`, diverting cargo into the competing route.
  - When a pure regulator :math:`r` (an element not itself carrying cargo flux,
    such as extracellular PCSK9 promoting LDLR degradation) negatively
    regulates stage :math:`v`, activating :math:`r` gates :math:`v` off.
* **Positive regulation** (``POSITIVELY_REGULATES``, ``ENABLES``,
  ``REGULATES``): an active positive regulator boosts flux into its target
  stage (:math:`\\times 1.35`), whereas inactivating a required positive
  regulator gates the target stage off.

Examples
--------
>>> doc = {
...     "id": "toy_trafficking",
...     "title": "Toy trafficking module",
...     "module": {
...         "id": "root",
...         "parts": [
...             {"order": 1, "node": {"id": "uptake", "label": "Uptake"}},
...             {"order": 2, "node": {"id": "sorting", "label": "Sorting endosome"}},
...             {"order": 3, "node": {"id": "degradation", "label": "Lysosome"}},
...             {"order": 4, "node": {"id": "escape", "label": "Cytosolic escape"}},
...         ],
...         "connections": [
...             {"source": "uptake", "target": "sorting", "connection_type": "PROVIDES_INPUT_FOR"},
...             {"source": "sorting", "target": "degradation", "connection_type": "PROVIDES_INPUT_FOR"},
...             {"source": "sorting", "target": "escape", "connection_type": "PROVIDES_INPUT_FOR"},
...             {"source": "degradation", "target": "escape", "connection_type": "NEGATIVELY_REGULATES"},
...         ],
...     },
... }
>>> abm = module_to_abm(doc)
>>> wt = simulate_abm(abm)
>>> wt.final_counts["degradation"] > wt.final_counts["escape"]
True
>>> ko = simulate_abm(abm, settings={"degradation": False})
>>> ko.final_counts["degradation"]
0
>>> ko.final_counts["escape"]
100
"""

from __future__ import annotations

from dataclasses import dataclass, field
import math
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.module_boolean import (
    _element_index,
    _Flattener,
)
from ai_gene_review.module_dynamics import (
    Attractor,
    ScenarioResult,
    _labels,
    _removed,
    _settings,
)
from ai_gene_review.module_notation import iter_connections, iter_nodes
from ai_gene_review.render_modules import as_list

FLOW_PREDICATES: frozenset[str] = frozenset(
    {
        "PROVIDES_INPUT_FOR",
        "PRECEDES",
        "CAUSES",
        "HAS_OUTPUT",
    }
)

POSITIVE_REG_PREDICATES: frozenset[str] = frozenset(
    {
        "POSITIVELY_REGULATES",
        "ENABLES",
        "REGULATES",
    }
)

INHIBITING_PREDICATES: frozenset[str] = frozenset(
    {
        "NEGATIVELY_REGULATES",
        "INHIBITS",
        "PREVENTS",
    }
)

DEFAULT_BASE_RATE: float = 0.45
DEFAULT_MAX_LEAVE_FRACTION: float = 0.85
COMPETING_INHIBITOR_FACTOR: float = 0.25
POSITIVE_REGULATOR_BOOST: float = 1.35
DEFAULT_N_AGENTS: int = 100
DEFAULT_N_STEPS: int = 24


@dataclass(frozen=True)
class ABMStage:
    """A stage (compartment/step) or regulator in a module-derived ABM."""

    id: str
    label: str
    kind: str  # "node" or "annoton"
    is_flow_stage: bool
    is_entry: bool
    is_terminal: bool
    default_active: bool
    location_label: str | None = None
    location_id: str | None = None
    gate_activators: tuple[str, ...] = ()
    gate_inhibitors: tuple[str, ...] = ()


@dataclass(frozen=True)
class ABMTransition:
    """A directed cargo-flow transition between two flow stages."""

    source: str
    target: str
    predicate: str
    base_rate: float = DEFAULT_BASE_RATE
    description: str | None = None
    competing_inhibitors: tuple[str, ...] = ()
    positive_modulators: tuple[str, ...] = ()
    gate_activators: tuple[str, ...] = ()
    gate_inhibitors: tuple[str, ...] = ()


@dataclass
class ABMModel:
    """An agent-based trafficking model derived from a module document."""

    module_id: str
    title: str
    stages: list[ABMStage]
    transitions: list[ABMTransition]
    entry_stages: list[str]
    terminal_stages: list[str]
    skipped_connections: list[tuple[str, str, str]] = field(default_factory=list)

    @property
    def variables(self) -> list[str]:
        return [s.id for s in self.stages]

    def stage_map(self) -> dict[str, ABMStage]:
        return {s.id: s for s in self.stages}


@dataclass
class ABMSimulation:
    """Result of simulating a module-derived ABM for a fixed number of steps."""

    n_agents: int
    n_steps: int
    settings: dict[str, bool]
    element_active: dict[str, bool]
    effective_rates: list[dict[str, Any]]
    trajectory: list[dict[str, int]]
    final_counts: dict[str, int]
    peak_counts: dict[str, int]


def _coerce_doc(doc_or_review: Any) -> dict[str, Any]:
    """Coerce a YAML path, ModuleReview, or dict into a raw module dict."""
    if isinstance(doc_or_review, dict):
        return doc_or_review
    if isinstance(doc_or_review, (Path, str)):
        return yaml.safe_load(Path(doc_or_review).read_text(encoding="utf-8"))
    if hasattr(doc_or_review, "model_dump"):
        return doc_or_review.model_dump(mode="json", exclude_none=True)
    raise TypeError(f"Unsupported module input type: {type(doc_or_review)!r}")


def _loc_from_descriptor(loc: Any) -> tuple[str | None, str | None]:
    if not isinstance(loc, dict):
        return None, None
    term = loc.get("term") if isinstance(loc.get("term"), dict) else {}
    label = loc.get("preferred_term") or term.get("label")
    term_id = term.get("id")
    return (str(label) if label else None, str(term_id) if term_id else None)


def _extract_location(elem_dict: dict[str, Any]) -> tuple[str | None, str | None]:
    """Extract a human-readable location label and term ID for a node or annoton dict."""
    for loc in as_list(elem_dict.get("locations")):
        label, term_id = _loc_from_descriptor(loc)
        if label or term_id:
            return label, term_id
    for ann in as_list(elem_dict.get("annotons")):
        if not isinstance(ann, dict):
            continue
        for loc in as_list(ann.get("locations")):
            label, term_id = _loc_from_descriptor(loc)
            if label or term_id:
                return label, term_id
    proc = elem_dict.get("process")
    if isinstance(proc, dict):
        for loc in as_list(proc.get("occurs_in")):
            label, term_id = _loc_from_descriptor(loc)
            if label or term_id:
                return label, term_id
    loc = elem_dict.get("location")
    if isinstance(loc, dict):
        return _loc_from_descriptor(loc)
    return None, None


def _normalize_removed(
    removed_connections: Any,
) -> frozenset[tuple[str, str]]:
    out: set[tuple[str, str]] = set()
    for ref in removed_connections or ():
        if isinstance(ref, tuple) and len(ref) == 2:
            out.add((str(ref[0]), str(ref[1])))
        elif isinstance(ref, dict):
            out.add((str(ref.get("source")), str(ref.get("target"))))
        elif hasattr(ref, "source") and hasattr(ref, "target"):
            out.add((str(ref.source), str(ref.target)))
    return frozenset(out)


def module_to_abm(
    doc_or_review: Any,
    removed_connections: Any = None,
) -> ABMModel:
    """Derive an :class:`ABMModel` from a module dict, ``ModuleReview``, or YAML path."""
    doc = _coerce_doc(doc_or_review)
    module = doc.get("module")
    if not isinstance(module, dict):
        raise ValueError("module document is missing a top-level 'module' mapping")

    removed = _normalize_removed(removed_connections)
    flat = _Flattener(module, removed)
    index = _element_index(module)
    labels = _labels(doc)

    # Preserve document order for elements.
    order: list[str] = []
    kinds: dict[str, str] = {}
    for node in iter_nodes(module):
        nid = node.get("id")
        if nid:
            s_nid = str(nid)
            order.append(s_nid)
            kinds[s_nid] = "node"
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                s_aid = str(annoton["id"])
                order.append(s_aid)
                kinds[s_aid] = "annoton"

    # Flatten connections across container boundaries using _Flattener.exits / .entries
    flat_conns: list[tuple[str, str, str, str | None]] = []
    skipped: list[tuple[str, str, str]] = []
    seen_flat: set[tuple[str, str, str]] = set()
    for conn in flat.connections:
        raw_pred = conn.get("connection_type")
        pred = (
            raw_pred.value
            if hasattr(raw_pred, "value")
            else str(raw_pred or "")
        )
        raw_src = str(conn.get("source") or "")
        raw_tgt = str(conn.get("target") or "")
        desc = str(conn.get("description")) if conn.get("description") else None
        if pred not in (FLOW_PREDICATES | POSITIVE_REG_PREDICATES | INHIBITING_PREDICATES):
            skipped.append((raw_src, pred, raw_tgt))
            continue
        for s in flat.exits(raw_src):
            for t in flat.entries(raw_tgt):
                if s != t and (s, t, pred) not in seen_flat:
                    seen_flat.add((s, t, pred))
                    flat_conns.append((s, t, pred, desc))

    involved = {s for s, _, _, _ in flat_conns} | {t for _, t, _, _ in flat_conns}
    variables = [v for v in order if v in involved]
    variables += sorted(v for v in involved if v not in variables)

    flow_conns: list[tuple[str, str, str, str | None]] = []
    pos_reg_by_target: dict[str, list[str]] = {eid: [] for eid in variables}
    neg_reg_by_target: dict[str, list[str]] = {eid: [] for eid in variables}
    outgoing_preds_by_source: dict[str, set[str]] = {eid: set() for eid in variables}
    incoming_by_target: dict[str, int] = {eid: 0 for eid in variables}

    flow_endpoints: set[str] = set()
    flow_incoming: dict[str, int] = {eid: 0 for eid in variables}
    flow_outgoing: dict[str, int] = {eid: 0 for eid in variables}

    for src, tgt, pred, desc in flat_conns:
        outgoing_preds_by_source[src].add(pred)
        incoming_by_target[tgt] += 1
        if pred in FLOW_PREDICATES:
            flow_conns.append((src, tgt, pred, desc))
            flow_endpoints.add(src)
            flow_endpoints.add(tgt)
            flow_outgoing[src] += 1
            flow_incoming[tgt] += 1
        elif pred in POSITIVE_REG_PREDICATES:
            if src not in pos_reg_by_target[tgt]:
                pos_reg_by_target[tgt].append(src)
        elif pred in INHIBITING_PREDICATES:
            if src not in neg_reg_by_target[tgt]:
                neg_reg_by_target[tgt].append(src)

    stages: list[ABMStage] = []
    for eid in variables:
        is_flow = eid in flow_endpoints
        is_entry = is_flow and flow_incoming[eid] == 0
        is_terminal = is_flow and flow_outgoing[eid] == 0
        elem_dict = index.get(eid) or {}
        loc_label, loc_id = _extract_location(elem_dict)

        out_preds = outgoing_preds_by_source.get(eid, set())
        if is_flow:
            default_active = True
        elif (
            out_preds
            and out_preds <= INHIBITING_PREDICATES
            and incoming_by_target[eid] == 0
        ):
            default_active = False
        else:
            default_active = True

        gate_acts = tuple(r for r in pos_reg_by_target[eid] if r not in flow_endpoints)
        gate_inhs = tuple(r for r in neg_reg_by_target[eid] if r not in flow_endpoints)

        stages.append(
            ABMStage(
                id=eid,
                label=labels.get(eid, eid),
                kind=kinds.get(eid, "node"),
                is_flow_stage=is_flow,
                is_entry=is_entry,
                is_terminal=is_terminal,
                default_active=default_active,
                location_label=loc_label,
                location_id=loc_id,
                gate_activators=gate_acts,
                gate_inhibitors=gate_inhs,
            )
        )

    entry_stages = [s.id for s in stages if s.is_entry]
    if not entry_stages:
        entry_stages = [s.id for s in stages if s.is_flow_stage][:1]
    terminal_stages = [s.id for s in stages if s.is_terminal]

    transitions: list[ABMTransition] = []
    for src, tgt, pred, desc in flow_conns:
        comp_inhs = tuple(
            r for r in neg_reg_by_target[tgt] if r in flow_endpoints and r != src
        )
        pos_mods = tuple(r for r in pos_reg_by_target[tgt] if r != src)
        gate_acts = tuple(r for r in pos_reg_by_target[tgt] if r not in flow_endpoints)
        gate_inhs = tuple(r for r in neg_reg_by_target[tgt] if r not in flow_endpoints)
        transitions.append(
            ABMTransition(
                source=src,
                target=tgt,
                predicate=pred,
                base_rate=DEFAULT_BASE_RATE,
                description=desc,
                competing_inhibitors=comp_inhs,
                positive_modulators=pos_mods,
                gate_activators=gate_acts,
                gate_inhibitors=gate_inhs,
            )
        )

    return ABMModel(
        module_id=str(doc.get("id") or module.get("id") or ""),
        title=str(doc.get("title") or doc.get("id") or ""),
        stages=stages,
        transitions=transitions,
        entry_stages=entry_stages,
        terminal_stages=terminal_stages,
        skipped_connections=skipped,
    )


def _resolve_element_active(
    model: ABMModel,
    settings: dict[str, bool],
) -> dict[str, bool]:
    """Determine which stages/regulators are active after applying settings and gates."""
    active: dict[str, bool] = {}
    for stage in model.stages:
        if stage.id in settings:
            active[stage.id] = bool(settings[stage.id])
        else:
            active[stage.id] = stage.default_active

    for _ in range(len(model.stages)):
        changed = False
        for stage in model.stages:
            if stage.id in settings:
                continue
            gated_off = False
            if any(not active.get(r, True) for r in stage.gate_activators):
                gated_off = True
            if any(active.get(r, False) for r in stage.gate_inhibitors):
                gated_off = True
            new_val = False if gated_off else stage.default_active
            if active[stage.id] != new_val:
                active[stage.id] = new_val
                changed = True
        if not changed:
            break
    return active


def _effective_transition_rate(
    t: ABMTransition,
    element_active: dict[str, bool],
) -> float:
    """Compute effective per-step transition rate for a flow transition."""
    if not element_active.get(t.source, False) or not element_active.get(t.target, False):
        return 0.0
    if any(not element_active.get(r, True) for r in t.gate_activators):
        return 0.0
    if any(element_active.get(r, False) for r in t.gate_inhibitors):
        return 0.0

    rate = t.base_rate
    for inh in t.competing_inhibitors:
        if element_active.get(inh, False):
            rate *= COMPETING_INHIBITOR_FACTOR
    for mod in t.positive_modulators:
        if element_active.get(mod, False):
            rate *= POSITIVE_REGULATOR_BOOST
        else:
            rate = 0.0
    return rate


def simulate_abm(
    model: ABMModel,
    settings: dict[str, bool] | None = None,
    n_agents: int = DEFAULT_N_AGENTS,
    n_steps: int = DEFAULT_N_STEPS,
) -> ABMSimulation:
    """Run a deterministic particle-conserving simulation of ``model``."""
    pinned = dict(settings or {})
    element_active = _resolve_element_active(model, pinned)

    counts: dict[str, int] = {s.id: 0 for s in model.stages}
    active_entries = [sid for sid in model.entry_stages if element_active.get(sid, False)]
    if active_entries and n_agents > 0:
        share = n_agents // len(active_entries)
        rem = n_agents % len(active_entries)
        for idx, sid in enumerate(active_entries):
            counts[sid] = share + (1 if idx < rem else 0)

    transitions_by_source: dict[str, list[tuple[int, ABMTransition, float]]] = {
        s.id: [] for s in model.stages
    }
    effective_rates: list[dict[str, Any]] = []
    for idx, t in enumerate(model.transitions):
        eff = _effective_transition_rate(t, element_active)
        effective_rates.append(
            {
                "source": t.source,
                "target": t.target,
                "predicate": t.predicate,
                "base_rate": t.base_rate,
                "effective_rate": round(eff, 6),
                "competing_inhibitors": list(t.competing_inhibitors),
                "positive_modulators": list(t.positive_modulators),
            }
        )
        if eff > 0.0:
            transitions_by_source[t.source].append((idx, t, eff))

    trajectory: list[dict[str, int]] = [dict(counts)]
    peak_counts: dict[str, int] = dict(counts)

    for _ in range(n_steps):
        next_counts = dict(counts)
        for stage in model.stages:
            u = stage.id
            current = counts[u]
            if current <= 0:
                continue
            outgoing = transitions_by_source.get(u, [])
            if not outgoing:
                continue
            sum_rates = sum(eff for _, _, eff in outgoing)
            if sum_rates <= 0.0:
                continue
            leave_frac = min(DEFAULT_MAX_LEAVE_FRACTION, sum_rates)
            total_leaving = min(current, int(math.ceil(current * leave_frac)))
            if total_leaving <= 0:
                continue

            exact_fluxes = [
                (idx, t, total_leaving * (eff / sum_rates))
                for idx, t, eff in outgoing
            ]
            int_fluxes = {idx: int(math.floor(val)) for idx, _, val in exact_fluxes}
            remainder = total_leaving - sum(int_fluxes.values())
            if remainder > 0:
                ranked = sorted(
                    exact_fluxes,
                    key=lambda item: (item[2] - int_fluxes[item[0]], -item[0]),
                    reverse=True,
                )
                for idx, _, _ in ranked[:remainder]:
                    int_fluxes[idx] += 1

            for idx, t, _ in exact_fluxes:
                moved = int_fluxes[idx]
                if moved > 0:
                    next_counts[u] -= moved
                    next_counts[t.target] += moved

        counts = next_counts
        trajectory.append(dict(counts))
        for sid, val in counts.items():
            if val > peak_counts[sid]:
                peak_counts[sid] = val

    return ABMSimulation(
        n_agents=n_agents,
        n_steps=n_steps,
        settings=pinned,
        element_active=element_active,
        effective_rates=effective_rates,
        trajectory=trajectory,
        final_counts=dict(counts),
        peak_counts=peak_counts,
    )


def abm_models(doc_or_review: Any) -> list[dict[str, Any]]:
    """The ``executable_models`` entries of type ``AGENT_BASED`` derived from the module."""
    doc = _coerce_doc(doc_or_review)
    return [
        m
        for m in as_list(doc.get("executable_models"))
        if isinstance(m, dict)
        and m.get("model_type") == "AGENT_BASED"
        and m.get("derivation") == "DERIVED_FROM_MODULE"
    ]


def run_abm_scenario(
    doc_or_review: Any,
    model_id: str,
    scenario_or_dict: Any,
    n_agents: int = DEFAULT_N_AGENTS,
    n_steps: int = DEFAULT_N_STEPS,
) -> ScenarioResult:
    """Run a single scenario against a module-derived ABM and check expectations."""
    doc = _coerce_doc(doc_or_review)
    if isinstance(scenario_or_dict, dict):
        scenario = scenario_or_dict
    elif hasattr(scenario_or_dict, "model_dump"):
        scenario = scenario_or_dict.model_dump(mode="json", exclude_none=True)
    else:
        raise TypeError(f"Unsupported scenario type: {type(scenario_or_dict)!r}")

    sid = str(scenario.get("id"))
    label = str(scenario.get("label") or sid)
    failures: list[str] = []

    removed = _removed(scenario)
    declared = {
        (str(c.get("source")), str(c.get("target")))
        for c in iter_connections(doc.get("module") or {})
    }
    for pair in sorted(removed - declared):
        failures.append(f"removed connection {pair[0]} -> {pair[1]} is not declared")

    abm = module_to_abm(doc, removed_connections=removed)
    stage_ids = set(abm.variables)
    stage_map = abm.stage_map()

    settings = _settings(scenario)
    bad = sorted(set(settings) - stage_ids)
    if bad:
        failures.append(f"settings name elements that are not model stages: {bad}")
        return ScenarioResult(model_id, sid, label, [], failures)

    sim = simulate_abm(abm, settings=settings, n_agents=n_agents, n_steps=n_steps)

    def is_stage_active(eid: str) -> bool:
        st = stage_map[eid]
        if st.is_flow_stage:
            return sim.element_active.get(eid, False) and sim.peak_counts.get(eid, 0) > 0
        return sim.element_active.get(eid, False)

    for eid in as_list(scenario.get("expected_active")):
        eid = str(eid)
        if eid not in stage_ids:
            failures.append(
                f"expected_active names {eid}, which is not a model stage"
            )
        elif not is_stage_active(eid):
            failures.append(
                f"expected {eid} to be active/reached "
                f"(peak_count={sim.peak_counts.get(eid, 0)}, "
                f"final_count={sim.final_counts.get(eid, 0)}, "
                f"enabled={sim.element_active.get(eid, False)})"
            )

    for eid in as_list(scenario.get("expected_inactive")):
        eid = str(eid)
        if eid not in stage_ids:
            failures.append(
                f"expected_inactive names {eid}, which is not a model stage"
            )
        elif is_stage_active(eid):
            failures.append(
                f"expected {eid} to be inactive/unreached "
                f"(peak_count={sim.peak_counts.get(eid, 0)}, "
                f"final_count={sim.final_counts.get(eid, 0)}, "
                f"enabled={sim.element_active.get(eid, False)})"
            )

    order_list = [str(e) for e in as_list(scenario.get("expected_outcome_order"))]
    unknown_order = [e for e in order_list if e not in stage_ids]
    for eid in unknown_order:
        failures.append(
            f"expected_outcome_order names {eid}, which is not a model stage"
        )
    if not unknown_order and len(order_list) >= 2:
        for higher, lower in zip(order_list, order_list[1:]):
            c_high = sim.final_counts.get(higher, 0)
            c_low = sim.final_counts.get(lower, 0)
            if not (c_high > c_low):
                failures.append(
                    f"expected_outcome_order violated: "
                    f"final_count[{higher}]={c_high} is not > "
                    f"final_count[{lower}]={c_low}"
                )

    mask = sum(
        (1 << idx)
        for idx, v in enumerate(abm.variables)
        if is_stage_active(v)
    )
    attr = Attractor(list(abm.variables), [mask])
    return ScenarioResult(model_id, sid, label, [attr], failures)


def run_declared_abm_scenarios(doc_or_review: Any) -> list[ScenarioResult]:
    """Run every scenario on every derived ``AGENT_BASED`` model the module declares."""
    doc = _coerce_doc(doc_or_review)
    results: list[ScenarioResult] = []
    for model in abm_models(doc):
        for scenario in as_list(model.get("scenarios")):
            if isinstance(scenario, dict):
                results.append(run_abm_scenario(doc, str(model.get("id")), scenario))
    return results


def abm_model_payload(
    doc_or_review: Any,
    model_entry: Any,
) -> dict[str, Any]:
    """Build a JSON-ready payload for the interactive ABM simulation page."""
    doc = _coerce_doc(doc_or_review)
    if not isinstance(model_entry, dict) and hasattr(model_entry, "model_dump"):
        model_entry = model_entry.model_dump(mode="json", exclude_none=True)

    base_abm = module_to_abm(doc)
    baseline_sim = simulate_abm(base_abm)
    model_id = str(model_entry.get("id") or "")

    scenarios_out: list[dict[str, Any]] = []
    for sc in as_list(model_entry.get("scenarios")):
        if not isinstance(sc, dict):
            continue
        result = run_abm_scenario(doc, model_id, sc)
        removed = _removed(sc)
        sc_abm = module_to_abm(doc, removed_connections=removed)
        settings = _settings(sc)
        sim = simulate_abm(sc_abm, settings=settings)
        scenarios_out.append(
            {
                "id": sc.get("id"),
                "label": sc.get("label") or sc.get("id"),
                "description": sc.get("description") or "",
                "settings": settings,
                "removed_connections": [
                    {"source": s, "target": t} for s, t in sorted(removed)
                ],
                "expected_active": [str(x) for x in as_list(sc.get("expected_active"))],
                "expected_inactive": [str(x) for x in as_list(sc.get("expected_inactive"))],
                "expected_outcome_order": [
                    str(x) for x in as_list(sc.get("expected_outcome_order"))
                ],
                "passed": result.passed,
                "failures": result.failures,
                "simulation": {
                    "n_agents": sim.n_agents,
                    "n_steps": sim.n_steps,
                    "element_active": sim.element_active,
                    "effective_rates": sim.effective_rates,
                    "trajectory": sim.trajectory,
                    "final_counts": sim.final_counts,
                    "peak_counts": sim.peak_counts,
                },
                "evidence": [
                    {
                        "source_id": ev.get("source_id"),
                        "supporting_text": ev.get("supporting_text") or "",
                        "notes": ev.get("notes") or "",
                    }
                    for ev in as_list(sc.get("evidence"))
                    if isinstance(ev, dict)
                ],
            }
        )

    return {
        "module_id": doc.get("id"),
        "title": doc.get("title"),
        "model_id": model_id,
        "model_title": model_entry.get("title")
        or f"{doc.get('title')} — agent-based trafficking model",
        "model_type": "AGENT_BASED",
        "derivation": "DERIVED_FROM_MODULE",
        "description": model_entry.get("description") or "",
        "notes": model_entry.get("notes") or "",
        "parameters": {
            "n_agents": DEFAULT_N_AGENTS,
            "n_steps": DEFAULT_N_STEPS,
            "base_rate": DEFAULT_BASE_RATE,
            "max_leave_fraction": DEFAULT_MAX_LEAVE_FRACTION,
            "competing_inhibitor_factor": COMPETING_INHIBITOR_FACTOR,
            "positive_regulator_boost": POSITIVE_REGULATOR_BOOST,
        },
        "stages": [
            {
                "id": s.id,
                "label": s.label,
                "kind": s.kind,
                "is_flow_stage": s.is_flow_stage,
                "is_entry": s.is_entry,
                "is_terminal": s.is_terminal,
                "default_active": s.default_active,
                "location_label": s.location_label or "",
                "location_id": s.location_id or "",
                "gate_activators": list(s.gate_activators),
                "gate_inhibitors": list(s.gate_inhibitors),
            }
            for s in base_abm.stages
        ],
        "transitions": [
            {
                "source": t.source,
                "target": t.target,
                "predicate": t.predicate,
                "base_rate": t.base_rate,
                "description": t.description or "",
                "competing_inhibitors": list(t.competing_inhibitors),
                "positive_modulators": list(t.positive_modulators),
                "gate_activators": list(t.gate_activators),
                "gate_inhibitors": list(t.gate_inhibitors),
            }
            for t in base_abm.transitions
        ],
        "entry_stages": list(base_abm.entry_stages),
        "terminal_stages": list(base_abm.terminal_stages),
        "baseline_simulation": {
            "n_agents": baseline_sim.n_agents,
            "n_steps": baseline_sim.n_steps,
            "element_active": baseline_sim.element_active,
            "effective_rates": baseline_sim.effective_rates,
            "trajectory": baseline_sim.trajectory,
            "final_counts": baseline_sim.final_counts,
            "peak_counts": baseline_sim.peak_counts,
        },
        "scenarios": scenarios_out,
    }
