"""Derive and simulate agent-based models (ABMs) from module definitions.

In intracellular trafficking and delivery pathways, cargo entities (receptors,
ligands, viral particles, lipid nanoparticles) move as discrete agents across
subcellular compartments and compete across branching sorting routes. Unlike
Boolean networks—where all downstream branches of an active sorting hub turn
``ON`` simultaneously—an agent-based model conserves discrete cargo particles
across compartments:

* **Flow connections** (``PROVIDES_INPUT_FOR``, ``PRECEDES``, ``CAUSES``,
  ``HAS_INPUT``, ``HAS_OUTPUT``) define directed cargo transport transitions
  between stages.
* **Branch competition & negative regulation** (``NEGATIVELY_REGULATES``):
  - When a competing flow stage :math:`w` negatively regulates stage :math:`v`
    (for example, Rab7-mediated late endosome maturation limiting endosomal
    dwell time and cytosolic escape), an active :math:`w` attenuates the
    per-step transition rate into :math:`v` (:math:`\\times 0.25`). Knocking
    out :math:`w` both closes flux into :math:`w` and lifts the attenuation on
    :math:`v`, diverting cargo into the competing route.
  - When a pure regulator :math:`r` (an element not itself carrying cargo flux,
    such as extracellular PCSK9 promoting LDLR degradation) negatively
    regulates stage :math:`v`, activating :math:`r` gates :math:`v` off.
* **Positive regulation** (``POSITIVELY_REGULATES``): an active positive
  regulator boosts flux into its target stage (:math:`\\times 1.35`), whereas
  inactivating a required positive regulator gates the target stage off.
* **Structural connections** (``PART_OF``) are ignored during ABM derivation.

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
    _logic_operator,
    activation_logic_findings,
    omitted_regulators,
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
        "HAS_INPUT",
        "HAS_OUTPUT",
    }
)

POSITIVE_REG_PREDICATES: frozenset[str] = frozenset(
    {
        "POSITIVELY_REGULATES",
    }
)

INHIBITING_PREDICATES: frozenset[str] = frozenset(
    {
        "NEGATIVELY_REGULATES",
    }
)

STRUCTURAL_PREDICATES: frozenset[str] = frozenset(
    {
        "PART_OF",
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
    activation_logic: dict[str, Any] | None = None
    flow_inputs: tuple[str, ...] = ()
    competing_inhibitors: tuple[str, ...] = ()


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
    activation_logic: dict[str, Any] | None = None
    flow_inputs: tuple[str, ...] = ()


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
    removed_connections: list[tuple[str, str]] = field(default_factory=list)
    invalid_activation_logic: list[str] = field(default_factory=list)

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
    converged: bool = True


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
    term_raw = loc.get("term")
    term: dict[str, Any] = term_raw if isinstance(term_raw, dict) else {}
    label = loc.get("preferred_term") or term.get("label")
    term_id = term.get("id")
    return (str(label) if label else None, str(term_id) if term_id else None)


def _extract_location(elem_dict: dict[str, Any]) -> tuple[str | None, str | None]:
    """Extract a human-readable location label and term ID for a node or annoton dict."""
    for loc in as_list(elem_dict.get("locations")):
        label, term_id = _loc_from_descriptor(loc)
        if label or term_id:
            return label, term_id
    ctx = elem_dict.get("context")
    if isinstance(ctx, dict):
        for loc in as_list(ctx.get("cellular_components")):
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


def _normalize_logic_expr(
    expr: Any, base_flat: _Flattener
) -> dict[str, Any] | None:
    if not isinstance(expr, dict):
        return None
    try:
        op = _logic_operator(expr)
    except ValueError:
        return None
    if op == "element":
        leaf = str(expr["element"])
        exits = base_flat.exits(leaf)
        if len(exits) == 1:
            return {"element": exits[0]}
        return {"any_of": [{"element": x} for x in exits]}
    subs: list[dict[str, Any]] = []
    for sub in as_list(expr[op]):
        norm_sub = _normalize_logic_expr(sub, base_flat)
        if norm_sub is None:
            return None
        subs.append(norm_sub)
    return {op: subs}


def _eval_abm_logic(
    expr: dict[str, Any],
    active: dict[str, bool],
    flow_inputs: tuple[str, ...] = (),
    competing_inhibitors: tuple[str, ...] = (),
) -> bool:
    op = _logic_operator(expr)
    if op == "element":
        v = str(expr["element"])
        if v in competing_inhibitors:
            return False
        if v in flow_inputs:
            return True
        return active.get(v, False)
    subs = [
        _eval_abm_logic(
            sub,
            active,
            flow_inputs=flow_inputs,
            competing_inhibitors=competing_inhibitors,
        )
        for sub in as_list(expr[op])
        if isinstance(sub, dict)
    ]
    if op == "none_of":
        return not any(subs)
    if op == "all_of":
        return all(subs)
    return any(subs)


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
    base_flat = _Flattener(module, frozenset())
    index = _element_index(module)
    labels = _labels(doc)
    omitted_by_target = {
        k: set(v) for k, v in omitted_regulators(doc).items()
    }

    # Expand removed_connections across container boundaries so both Python and
    # browser simulation see the leaf stage pairs that were severed.
    removed_leaf_pairs: set[tuple[str, str]] = set()
    for raw_src, raw_tgt in removed:
        for s in base_flat.exits(raw_src):
            for t in base_flat.entries(raw_tgt):
                if s != t:
                    removed_leaf_pairs.add((s, t))

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

    # Flatten all unperturbed connections first to fix the stage inventory and
    # baseline entry/terminal/regulator classification, then filter out removed
    # connections for transitions and regulatory gates.
    base_flat_conns: list[tuple[str, str, str, str | None]] = []
    active_flat_conns: list[tuple[str, str, str, str | None]] = []
    skipped: list[tuple[str, str, str]] = []
    seen_base: set[tuple[str, str, str]] = set()
    seen_active: set[tuple[str, str, str]] = set()
    for conn in base_flat.connections:
        raw_pred = conn.get("connection_type")
        pred = str(getattr(raw_pred, "value", raw_pred) or "")
        raw_src = str(conn.get("source") or "")
        raw_tgt = str(conn.get("target") or "")
        desc = str(conn.get("description")) if conn.get("description") else None
        if pred in STRUCTURAL_PREDICATES:
            continue
        if pred not in (FLOW_PREDICATES | POSITIVE_REG_PREDICATES | INHIBITING_PREDICATES):
            if (raw_src, raw_tgt) not in removed:
                skipped.append((raw_src, pred, raw_tgt))
            continue
        raw_removed = (raw_src, raw_tgt) in removed
        for s in base_flat.exits(raw_src):
            for t in base_flat.entries(raw_tgt):
                if s == t:
                    continue
                if (s, t, pred) not in seen_base:
                    seen_base.add((s, t, pred))
                    base_flat_conns.append((s, t, pred, desc))
                if (
                    not raw_removed
                    and (s, t) not in removed_leaf_pairs
                    and (s, t, pred) not in seen_active
                ):
                    seen_active.add((s, t, pred))
                    active_flat_conns.append((s, t, pred, desc))

    involved = {s for s, _, _, _ in base_flat_conns} | {
        t for _, t, _, _ in base_flat_conns
    }
    variables = [v for v in order if v in involved]
    variables += sorted(v for v in involved if v not in variables)

    base_outgoing_preds_by_source: dict[str, set[str]] = {eid: set() for eid in variables}
    base_incoming_by_target: dict[str, int] = {eid: 0 for eid in variables}
    base_flow_endpoints: set[str] = set()
    base_flow_incoming: dict[str, int] = {eid: 0 for eid in variables}
    base_flow_outgoing: dict[str, int] = {eid: 0 for eid in variables}

    for src, tgt, pred, _desc in base_flat_conns:
        base_outgoing_preds_by_source[src].add(pred)
        base_incoming_by_target[tgt] += 1
        if pred in FLOW_PREDICATES:
            base_flow_endpoints.add(src)
            base_flow_endpoints.add(tgt)
            base_flow_outgoing[src] += 1
            base_flow_incoming[tgt] += 1

    flow_conns: list[tuple[str, str, str, str | None]] = []
    flow_inputs_by_target: dict[str, list[str]] = {eid: [] for eid in variables}
    pos_reg_by_target: dict[str, list[str]] = {eid: [] for eid in variables}
    neg_reg_by_target: dict[str, list[str]] = {eid: [] for eid in variables}

    for src, tgt, pred, desc in active_flat_conns:
        if pred in FLOW_PREDICATES:
            flow_conns.append((src, tgt, pred, desc))
            if src not in flow_inputs_by_target[tgt]:
                flow_inputs_by_target[tgt].append(src)
        elif pred in POSITIVE_REG_PREDICATES:
            if (
                src not in omitted_by_target.get(tgt, set())
                and src not in pos_reg_by_target[tgt]
            ):
                pos_reg_by_target[tgt].append(src)
        elif pred in INHIBITING_PREDICATES:
            if (
                src not in omitted_by_target.get(tgt, set())
                and src not in neg_reg_by_target[tgt]
            ):
                neg_reg_by_target[tgt].append(src)

    logic_by_target: dict[str, dict[str, Any] | None] = {}
    invalid_logic: list[str] = []
    for eid in variables:
        elem_dict = index.get(eid) or {}
        raw_logic = elem_dict.get("activation_logic")
        if raw_logic is not None:
            norm_logic = _normalize_logic_expr(raw_logic, base_flat)
            if norm_logic is None:
                invalid_logic.append(f"{eid}: invalid activation_logic {raw_logic!r}")
            logic_by_target[eid] = norm_logic
        else:
            logic_by_target[eid] = None

    stages: list[ABMStage] = []
    for eid in variables:
        is_flow = eid in base_flow_endpoints
        is_entry = is_flow and base_flow_incoming[eid] == 0
        is_terminal = is_flow and base_flow_outgoing[eid] == 0
        elem_dict = index.get(eid) or {}
        loc_label, loc_id = _extract_location(elem_dict)

        out_preds = base_outgoing_preds_by_source.get(eid, set())
        if is_flow:
            default_active = True
        elif (
            out_preds
            and out_preds <= INHIBITING_PREDICATES
            and base_incoming_by_target[eid] == 0
        ):
            default_active = False
        else:
            default_active = True

        gate_acts = tuple(
            r for r in pos_reg_by_target[eid] if r not in base_flow_endpoints
        )
        gate_inhs = tuple(
            r for r in neg_reg_by_target[eid] if r not in base_flow_endpoints
        )
        comp_inhs_stage = tuple(
            r for r in neg_reg_by_target[eid] if r in base_flow_endpoints
        )

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
                activation_logic=logic_by_target.get(eid),
                flow_inputs=tuple(flow_inputs_by_target[eid]),
                competing_inhibitors=comp_inhs_stage,
            )
        )

    entry_stages = [s.id for s in stages if s.is_entry]
    if not entry_stages:
        entry_stages = [s.id for s in stages if s.is_flow_stage][:1]
    terminal_stages = [s.id for s in stages if s.is_terminal]

    transitions: list[ABMTransition] = []
    for src, tgt, pred, desc in flow_conns:
        comp_inhs = tuple(
            r for r in neg_reg_by_target[tgt] if r in base_flow_endpoints and r != src
        )
        pos_mods = tuple(r for r in pos_reg_by_target[tgt] if r != src)
        gate_acts = tuple(
            r for r in pos_reg_by_target[tgt] if r not in base_flow_endpoints
        )
        gate_inhs = tuple(
            r for r in neg_reg_by_target[tgt] if r not in base_flow_endpoints
        )
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
                activation_logic=logic_by_target.get(tgt),
                flow_inputs=tuple(flow_inputs_by_target[tgt]),
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
        removed_connections=sorted(removed_leaf_pairs),
        invalid_activation_logic=invalid_logic,
    )


def _resolve_element_active(
    model: ABMModel,
    settings: dict[str, bool],
) -> tuple[dict[str, bool], bool]:
    """Determine which stages/regulators are active after applying settings and gates."""
    active: dict[str, bool] = {}
    for stage in model.stages:
        if stage.id in settings:
            active[stage.id] = bool(settings[stage.id])
        else:
            active[stage.id] = stage.default_active

    converged = False
    for _ in range(len(model.stages) + 1):
        changed = False
        for stage in model.stages:
            if stage.id in settings:
                continue
            gated_off = False
            if stage.activation_logic is not None:
                gated_off = not _eval_abm_logic(
                    stage.activation_logic,
                    active,
                    flow_inputs=stage.flow_inputs,
                    competing_inhibitors=stage.competing_inhibitors,
                )
            else:
                if any(not active.get(r, True) for r in stage.gate_activators):
                    gated_off = True
                if any(active.get(r, False) for r in stage.gate_inhibitors):
                    gated_off = True
            new_val = False if gated_off else stage.default_active
            if active[stage.id] != new_val:
                active[stage.id] = new_val
                changed = True
        if not changed:
            converged = True
            break
    return active, converged


def _effective_transition_rate(
    t: ABMTransition,
    element_active: dict[str, bool],
) -> float:
    """Compute effective per-step transition rate for a flow transition."""
    if not element_active.get(t.source, False) or not element_active.get(t.target, False):
        return 0.0
    if t.activation_logic is not None:
        if not _eval_abm_logic(
            t.activation_logic,
            element_active,
            flow_inputs=t.flow_inputs,
            competing_inhibitors=t.competing_inhibitors,
        ):
            return 0.0
    else:
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
        elif t.activation_logic is None:
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
    element_active, converged = _resolve_element_active(model, pinned)

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
        converged=converged,
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


def _run_abm_scenario_with_sim(
    doc: dict[str, Any],
    model_id: str,
    scenario_or_dict: Any,
    n_agents: int = DEFAULT_N_AGENTS,
    n_steps: int = DEFAULT_N_STEPS,
) -> tuple[ScenarioResult, ABMSimulation, ABMModel]:
    """Run a single ABM scenario and return ``(result, simulation, abm_model)``."""
    if isinstance(scenario_or_dict, dict):
        scenario = scenario_or_dict
    elif hasattr(scenario_or_dict, "model_dump"):
        scenario = scenario_or_dict.model_dump(mode="json", exclude_none=True)
    else:
        raise TypeError(f"Unsupported scenario type: {type(scenario_or_dict)!r}")

    sid = str(scenario.get("id"))
    label = str(scenario.get("label") or sid)
    failures: list[str] = []

    for boolean_only_slot in (
        "expected_oscillating",
        "expected_attractor_kind",
        "expected_attractor_count",
    ):
        val = scenario.get(boolean_only_slot)
        if val is not None and val != [] and val != "":
            failures.append(
                f"{boolean_only_slot} is not supported on AGENT_BASED scenarios"
            )

    removed = _removed(scenario)
    declared = {
        (str(c.get("source")), str(c.get("target")))
        for c in iter_connections(doc.get("module") or {})
    }
    for pair in sorted(removed - declared):
        failures.append(f"removed connection {pair[0]} -> {pair[1]} is not declared")

    logic_problems = activation_logic_findings(doc, removed_connections=removed)
    if logic_problems:
        failures.extend(
            f"removed_connections break an activation_logic: {p}"
            for p in logic_problems
        )

    abm = module_to_abm(doc, removed_connections=removed)
    for raw_src, pred, raw_tgt in abm.skipped_connections:
        failures.append(
            f"unsupported connection_type {pred!r} on {raw_src} -> {raw_tgt}"
        )
    for bad_logic in abm.invalid_activation_logic:
        if not any(bad_logic in f for f in failures):
            failures.append(f"invalid activation_logic: {bad_logic}")

    stage_ids = set(abm.variables)
    stage_map = abm.stage_map()

    settings = _settings(scenario)
    bad = sorted(set(settings) - stage_ids)
    if bad:
        failures.append(f"settings name elements that are not model stages: {bad}")
        valid_settings = {k: v for k, v in settings.items() if k in stage_ids}
        sim = simulate_abm(
            abm, settings=valid_settings, n_agents=n_agents, n_steps=n_steps
        )
        return ScenarioResult(model_id, sid, label, [], failures), sim, abm

    sim = simulate_abm(abm, settings=settings, n_agents=n_agents, n_steps=n_steps)
    if not sim.converged:
        failures.append(
            "regulator gating did not converge (oscillating regulator loop)"
        )

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
    if 0 < len(order_list) < 2:
        failures.append(
            "expected_outcome_order requires at least 2 stages to compare"
        )
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
    return ScenarioResult(model_id, sid, label, [attr], failures), sim, abm


def run_abm_scenario(
    doc_or_review: Any,
    model_id: str,
    scenario_or_dict: Any,
    n_agents: int = DEFAULT_N_AGENTS,
    n_steps: int = DEFAULT_N_STEPS,
) -> ScenarioResult:
    """Run a single scenario against a module-derived ABM and check expectations."""
    doc = _coerce_doc(doc_or_review)
    result, _sim, _abm = _run_abm_scenario_with_sim(
        doc, model_id, scenario_or_dict, n_agents=n_agents, n_steps=n_steps
    )
    return result


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
        result, sim, sc_abm = _run_abm_scenario_with_sim(doc, model_id, sc)
        settings = _settings(sc)
        scenarios_out.append(
            {
                "id": sc.get("id"),
                "label": sc.get("label") or sc.get("id"),
                "description": sc.get("description") or "",
                "settings": settings,
                "removed_connections": [
                    {"source": s, "target": t} for s, t in sc_abm.removed_connections
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
                "activation_logic": s.activation_logic,
                "flow_inputs": list(s.flow_inputs),
                "competing_inhibitors": list(s.competing_inhibitors),
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
                "activation_logic": t.activation_logic,
                "flow_inputs": list(t.flow_inputs),
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
