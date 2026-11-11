#!/usr/bin/env python
"""Derive and simulate a steady-state Constraint-Based Model (FBA / pFBA / E-Flux) from a module.

While :mod:`ai_gene_review.module_boolean` and :mod:`ai_gene_review.module_dynamics`
compile a module into an asynchronous Boolean network, and
:mod:`ai_gene_review.module_abm` compiles a trafficking module into a discrete
particle-conserving agent-based model, this module compiles a metabolic module
(``model_type: CONSTRAINT_BASED``, ``derivation: DERIVED_FROM_MODULE``) into a
steady-state **Flux Balance Analysis (FBA / parsimonious FBA / E-Flux)** model:

* **Reactions & Stoichiometric Flow**: Flattened flow stages represent metabolic
  reaction steps :math:`r \\in \\mathcal{R}`, connected by metabolite handoff
  transitions :math:`e = (u \\to w) \\in \\mathcal{E}_{\\text{flow}}`. Internal
  metabolite junctions enforce strict steady-state mass conservation
  (:math:`\\mathbf{S}\\mathbf{v} = \\mathbf{0}`: total incoming flux equals
  reaction flux, which equals total outgoing flux at every non-terminal reaction).
  Unlike transient ABM particle simulations where cargo piles up behind a blocked
  step, blocking a mandatory downstream enzyme in steady-state FBA forces the
  entire unbranched upstream segment to zero steady-state flux and diverts flux
  at upstream branch points into alternative open routes.
* **AST-Based GPR & E-Flux Capacity Bounds**: Each reaction step extracts its
  hierarchical Gene-Protein-Reaction (GPR) tree from nested ``variant_sets``,
  ``annotons``, and ``protein_complex.active_units``:

  - ``all_of`` (heteromeric ``PROTEIN_COMPLEX`` subunits): evaluated via
    :math:`\\min` capacity (knocking out any required subunit collapses complex
    capacity to zero).
  - ``any_of`` (isozyme ``annotons`` or alternative ``variants``): evaluated via
    additive isozyme capacity :math:`\\frac{1}{k}\\sum_{i=1}^k c_i` (knocking out
    one isozyme attenuates upper bound capacity :math:`UB_r` while preserving
    flux through remaining isozymes; knocking out all isozymes blocks the step).
* **Parsimonious Flux Allocation (pFBA)**: At metabolic branch points, steady-state
  flux is allocated across open downstream branches by capacity-constrained
  water-filling weighted by downstream capacity and inverse parsimony path cost
  (shorter core routes carry higher flux per unit enzyme cost than multi-step or
  ``optional: true`` side branches).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from ai_gene_review.module_abm import (
    COMPETING_INHIBITOR_FACTOR,
    FLOW_PREDICATES,
    INHIBITING_PREDICATES,
    POSITIVE_REG_PREDICATES,
    POSITIVE_REGULATOR_BOOST,
    STRUCTURAL_PREDICATES,
    _coerce_doc,
    _extract_location,
    _labels,
    _normalize_logic_expr,
    _normalize_removed,
    _removed,
)
from ai_gene_review.module_boolean import (
    _element_index,
    _Flattener,
    activation_logic_findings,
    omitted_regulators,
)
from ai_gene_review.module_dynamics import Attractor, ScenarioResult
from ai_gene_review.module_notation import iter_connections, iter_nodes
from ai_gene_review.render_modules import as_list

DEFAULT_UPPER_BOUND = 100.0
OPTIONAL_BRANCH_UPPER_BOUND = 15.0
DEFAULT_UPTAKE_RATE = 100.0
FLUX_EPSILON = 1e-6


@dataclass(frozen=True)
class FBAGPRElement:
    """An enzyme variant, isozyme annoton, or complex subunit inside a reaction step."""

    id: str
    label: str
    kind: str  # "variant" | "annoton" | "subunit"
    reaction_id: str
    default_active: bool = True
    function_id: str | None = None
    function_label: str | None = None
    representative_genes: tuple[str, ...] = ()


@dataclass(frozen=True)
class FBAReaction:
    """A reaction step (or regulatory node) in a module-derived constraint-based model."""

    id: str
    label: str
    kind: str  # "reaction" | "regulator" | "annoton"
    is_flow_stage: bool
    is_entry: bool
    is_terminal: bool
    is_optional_branch: bool
    default_active: bool
    upper_bound: float
    location_label: str | None = None
    location_id: str | None = None
    function_id: str | None = None
    function_label: str | None = None
    substrates: tuple[str, ...] = ()
    products: tuple[str, ...] = ()
    cofactors: tuple[str, ...] = ()
    representative_genes: tuple[str, ...] = ()
    gpr_logic: dict[str, Any] | None = None
    gpr_rule_text: str = ""
    gate_activators: tuple[str, ...] = ()
    gate_inhibitors: tuple[str, ...] = ()
    activation_logic: dict[str, Any] | None = None
    flow_inputs: tuple[str, ...] = ()
    competing_inhibitors: tuple[str, ...] = ()
    positive_modulators: tuple[str, ...] = ()


@dataclass(frozen=True)
class FBATransition:
    """A stoichiometric metabolite handoff edge between two reaction steps."""

    source: str
    target: str
    predicate: str
    shared_metabolites: tuple[str, ...] = ()
    description: str | None = None
    is_optional_branch: bool = False
    competing_inhibitors: tuple[str, ...] = ()
    positive_modulators: tuple[str, ...] = ()
    gate_activators: tuple[str, ...] = ()
    gate_inhibitors: tuple[str, ...] = ()
    activation_logic: dict[str, Any] | None = None
    flow_inputs: tuple[str, ...] = ()


@dataclass
class FBAModel:
    """A constraint-based metabolic model derived from a module document."""

    module_id: str
    title: str
    reactions: list[FBAReaction]
    gpr_elements: list[FBAGPRElement]
    transitions: list[FBATransition]
    entry_reactions: list[str]
    terminal_reactions: list[str]
    effective_terminals: list[str]
    skipped_connections: list[tuple[str, str, str]] = field(default_factory=list)
    removed_connections: list[tuple[str, str]] = field(default_factory=list)
    invalid_activation_logic: list[str] = field(default_factory=list)

    @property
    def variables(self) -> list[str]:
        return [r.id for r in self.reactions]

    @property
    def controllable_ids(self) -> set[str]:
        return {r.id for r in self.reactions} | {g.id for g in self.gpr_elements}

    def reaction_map(self) -> dict[str, FBAReaction]:
        return {r.id: r for r in self.reactions}

    def gpr_map(self) -> dict[str, FBAGPRElement]:
        return {g.id: g for g in self.gpr_elements}


@dataclass
class FBASimulation:
    """Steady-state flux distribution and capacity bounds of an FBA/pFBA simulation."""

    uptake_rate: float
    settings: dict[str, bool | float]
    element_active: dict[str, bool]
    gpr_capacities: dict[str, float]
    reaction_bounds: dict[str, float]
    downstream_capacities: dict[str, float]
    reaction_fluxes: dict[str, float]
    transition_fluxes: list[dict[str, Any]]
    mass_balance_residuals: dict[str, float]
    total_uptake_flux: float
    total_export_flux: float
    total_l1_flux: float
    converged: bool


def _fba_settings(scenario: dict[str, Any]) -> dict[str, bool | float]:
    """Extract element settings from a scenario (boolean active/inactive or numeric E-Flux)."""
    out: dict[str, bool | float] = {}
    for s in as_list(scenario.get("settings")):
        if isinstance(s, dict) and s.get("element") is not None:
            eid = str(s["element"])
            raw = s.get("active")
            if isinstance(raw, bool):
                out[eid] = raw
            elif isinstance(raw, (int, float)):
                out[eid] = float(raw)
            else:
                out[eid] = bool(raw)
    return out


def _optional_elements(module: dict[str, Any]) -> set[str]:
    """Return all node and annoton IDs that lie inside an ``optional: true`` module part."""
    optional_ids: set[str] = set()

    def _mark_subtree(node: dict[str, Any]) -> None:
        nid = node.get("id")
        if nid:
            optional_ids.add(str(nid))
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                optional_ids.add(str(annoton["id"]))
        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                _mark_subtree(part["node"])
        for vs in as_list(node.get("variant_sets")):
            if isinstance(vs, dict):
                for variant in as_list(vs.get("variants")):
                    if isinstance(variant, dict):
                        _mark_subtree(variant)

    def _walk(node: dict[str, Any]) -> None:
        for part in as_list(node.get("parts")):
            if not isinstance(part, dict):
                continue
            child = part.get("node")
            if not isinstance(child, dict):
                continue
            if part.get("optional") is True:
                _mark_subtree(child)
            else:
                _walk(child)
        for vs in as_list(node.get("variant_sets")):
            if isinstance(vs, dict):
                for variant in as_list(vs.get("variants")):
                    if isinstance(variant, dict):
                        _walk(variant)

    _walk(module)
    return optional_ids


def _extract_participant_genes(participant: Any) -> list[str]:
    """Extract representative gene/protein labels from a ParticipantSelector."""
    if not isinstance(participant, dict):
        return []
    genes: list[str] = []
    for slot in ("gene", "gene_product"):
        gp = participant.get(slot)
        if isinstance(gp, dict):
            pref = gp.get("preferred_term")
            if pref:
                genes.append(str(pref))
    fam = participant.get("family")
    if isinstance(fam, dict):
        for rep in as_list(fam.get("representative_members")):
            if isinstance(rep, dict) and rep.get("preferred_term"):
                genes.append(str(rep["preferred_term"]))
    pc = participant.get("protein_complex")
    if isinstance(pc, dict):
        for unit in as_list(pc.get("active_units")):
            if isinstance(unit, dict):
                genes.extend(_extract_participant_genes(unit.get("participant")))
    seen: set[str] = set()
    deduped: list[str] = []
    for g in genes:
        if g not in seen:
            seen.add(g)
            deduped.append(g)
    return deduped


def _extract_function_info(
    annoton: dict[str, Any],
) -> tuple[str | None, str | None, list[str], list[str], list[str]]:
    """Return ``(func_id, func_label, substrates, products, cofactors)`` from an annoton."""
    fn = annoton.get("function")
    if not isinstance(fn, dict):
        return None, None, [], [], []
    raw_term = fn.get("term")
    term: dict[str, Any] = raw_term if isinstance(raw_term, dict) else {}
    func_id = str(term.get("id")) if term.get("id") else None
    func_label = (
        str(term.get("label") or fn.get("preferred_term"))
        if (term.get("label") or fn.get("preferred_term"))
        else None
    )
    substrates = [
        str(s["preferred_term"])
        for s in as_list(fn.get("substrates"))
        if isinstance(s, dict) and s.get("preferred_term")
    ]
    products = [
        str(p["preferred_term"])
        for p in as_list(fn.get("products"))
        if isinstance(p, dict) and p.get("preferred_term")
    ]
    cofactors = [
        str(c["preferred_term"])
        for c in as_list(fn.get("cofactors"))
        if isinstance(c, dict) and c.get("preferred_term")
    ]
    return func_id, func_label, substrates, products, cofactors


def _build_reaction_gpr_and_chemistry(
    reaction_id: str,
    elem_dict: dict[str, Any],
) -> tuple[
    dict[str, Any] | None,
    str,
    list[FBAGPRElement],
    str | None,
    str | None,
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...],
    tuple[str, ...],
]:
    """Extract GPR AST, human-readable GPR rule, GPR elements, and chemistry for a reaction step."""
    gpr_elements: list[FBAGPRElement] = []
    seen_gpr: set[str] = set()
    all_substrates: list[str] = []
    all_products: list[str] = []
    all_cofactors: list[str] = []
    all_genes: list[str] = []
    first_func_id: str | None = None
    first_func_label: str | None = None

    def _add_unique(target: list[str], items: list[str]) -> None:
        for item in items:
            if item not in target:
                target.append(item)

    def _compile_annoton(annoton: dict[str, Any]) -> dict[str, Any] | None:
        nonlocal first_func_id, first_func_label
        aid = str(annoton.get("id") or "")
        if not aid:
            return None
        alabel = str(annoton.get("label") or aid)
        fid, flabel, subs, prods, cofs = _extract_function_info(annoton)
        if first_func_id is None and fid:
            first_func_id = fid
        if first_func_label is None and flabel:
            first_func_label = flabel
        _add_unique(all_substrates, subs)
        _add_unique(all_products, prods)
        _add_unique(all_cofactors, cofs)

        participant = annoton.get("participant")
        genes = _extract_participant_genes(participant)
        _add_unique(all_genes, genes)

        if aid != reaction_id and aid not in seen_gpr:
            seen_gpr.add(aid)
            gpr_elements.append(
                FBAGPRElement(
                    id=aid,
                    label=alabel,
                    kind="annoton",
                    reaction_id=reaction_id,
                    default_active=True,
                    function_id=fid,
                    function_label=flabel,
                    representative_genes=tuple(genes),
                )
            )

        # Check for PROTEIN_COMPLEX active_units (AND rule over subunits)
        if isinstance(participant, dict):
            pc = participant.get("protein_complex")
            if isinstance(pc, dict):
                unit_exprs: list[dict[str, Any]] = []
                for unit in as_list(pc.get("active_units")):
                    if isinstance(unit, dict) and unit.get("id"):
                        uid = str(unit["id"])
                        ulabel = str(unit.get("label") or uid)
                        ugenes = _extract_participant_genes(unit.get("participant"))
                        _add_unique(all_genes, ugenes)
                        if uid not in seen_gpr:
                            seen_gpr.add(uid)
                            gpr_elements.append(
                                FBAGPRElement(
                                    id=uid,
                                    label=ulabel,
                                    kind="subunit",
                                    reaction_id=reaction_id,
                                    default_active=True,
                                    function_id=fid,
                                    function_label=flabel,
                                    representative_genes=tuple(ugenes),
                                )
                            )
                        unit_exprs.append({"element": uid})
                if unit_exprs:
                    sub_ast = (
                        unit_exprs[0]
                        if len(unit_exprs) == 1
                        else {"all_of": unit_exprs}
                    )
                    if aid != reaction_id:
                        return {"element": aid, "sub_logic": sub_ast}
                    return sub_ast

        if aid != reaction_id:
            return {"element": aid}
        return None

    def _compile_node(node: dict[str, Any], is_root: bool = False) -> dict[str, Any] | None:
        nid = str(node.get("id") or "")

        # If this node is itself an annoton
        if "participant" in node or "function" in node:
            return _compile_annoton(node)

        branch_exprs: list[dict[str, Any]] = []

        # Collect annotons directly on this node (OR across isozyme annotons)
        annoton_exprs: list[dict[str, Any]] = []
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict):
                a_expr = _compile_annoton(annoton)
                if a_expr is not None:
                    annoton_exprs.append(a_expr)
        if len(annoton_exprs) == 1:
            branch_exprs.append(annoton_exprs[0])
        elif len(annoton_exprs) > 1:
            branch_exprs.append({"any_of": annoton_exprs})

        # Collect variant_sets (OR across variants within each variant_set)
        for vs in as_list(node.get("variant_sets")):
            if not isinstance(vs, dict):
                continue
            v_exprs: list[dict[str, Any]] = []
            for variant in as_list(vs.get("variants")):
                if isinstance(variant, dict) and variant.get("id"):
                    vid = str(variant["id"])
                    vlabel = str(variant.get("label") or vid)
                    v_sub = _compile_node(variant, is_root=False)
                    v_genes: list[str] = []
                    for ann in as_list(variant.get("annotons")):
                        if isinstance(ann, dict):
                            v_genes.extend(
                                _extract_participant_genes(ann.get("participant"))
                            )
                    if vid not in seen_gpr:
                        seen_gpr.add(vid)
                        gpr_elements.append(
                            FBAGPRElement(
                                id=vid,
                                label=vlabel,
                                kind="variant",
                                reaction_id=reaction_id,
                                default_active=True,
                                function_id=first_func_id,
                                function_label=first_func_label,
                                representative_genes=tuple(dict.fromkeys(v_genes)),
                            )
                        )
                    if v_sub is not None:
                        v_exprs.append({"element": vid, "sub_logic": v_sub})
                    else:
                        v_exprs.append({"element": vid})
            if len(v_exprs) == 1:
                branch_exprs.append(v_exprs[0])
            elif len(v_exprs) > 1:
                branch_exprs.append({"any_of": v_exprs})

        # Collect nested parts on an atomic reaction container (AND across parts)
        part_exprs: list[dict[str, Any]] = []
        for part in as_list(node.get("parts")):
            if isinstance(part, dict) and isinstance(part.get("node"), dict):
                c_node = part["node"]
                p_sub = _compile_node(c_node, is_root=False)
                if p_sub is not None:
                    part_exprs.append(p_sub)
        if len(part_exprs) == 1:
            branch_exprs.append(part_exprs[0])
        elif len(part_exprs) > 1:
            branch_exprs.append({"all_of": part_exprs})

        if not branch_exprs:
            return None if is_root else {"element": nid}
        if len(branch_exprs) == 1:
            return branch_exprs[0]
        return {"any_of": branch_exprs}

    gpr_ast = _compile_node(elem_dict, is_root=True)
    gpr_text = _format_gpr_rule(gpr_ast) if gpr_ast is not None else reaction_id
    return (
        gpr_ast,
        gpr_text,
        gpr_elements,
        first_func_id,
        first_func_label,
        tuple(all_substrates),
        tuple(all_products),
        tuple(all_cofactors),
        tuple(all_genes),
    )


def _format_gpr_rule(expr: dict[str, Any] | None) -> str:
    """Format a GPR AST as a concise human-readable boolean/capacity expression."""
    if not expr or not isinstance(expr, dict):
        return ""
    if "element" in expr:
        el = str(expr["element"])
        sub = expr.get("sub_logic")
        if isinstance(sub, dict):
            sub_txt = _format_gpr_rule(sub)
            if sub_txt and sub_txt != el:
                return f"{el}[{sub_txt}]"
        return el
    if "all_of" in expr:
        parts = [_format_gpr_rule(s) for s in as_list(expr["all_of"]) if isinstance(s, dict)]
        parts = [p for p in parts if p]
        if len(parts) == 1:
            return parts[0]
        return "(" + " & ".join(parts) + ")"
    if "any_of" in expr:
        parts = [_format_gpr_rule(s) for s in as_list(expr["any_of"]) if isinstance(s, dict)]
        parts = [p for p in parts if p]
        if len(parts) == 1:
            return parts[0]
        return "(" + " | ".join(parts) + ")"
    return ""


def _eval_gpr_ast(
    expr: dict[str, Any] | None,
    raw_levels: dict[str, float],
    resolved_out: dict[str, float],
) -> float:
    """Evaluate a GPR AST quantitatively and populate ``resolved_out`` for each element."""
    if not expr or not isinstance(expr, dict):
        return 1.0
    if "element" in expr:
        eid = str(expr["element"])
        direct = raw_levels.get(eid, 1.0)
        sub = expr.get("sub_logic")
        sub_cap = _eval_gpr_ast(sub, raw_levels, resolved_out) if isinstance(sub, dict) else 1.0
        val = max(0.0, direct * sub_cap)
        resolved_out[eid] = val
        return val
    if "all_of" in expr:
        subs = [
            _eval_gpr_ast(s, raw_levels, resolved_out)
            for s in as_list(expr["all_of"])
            if isinstance(s, dict)
        ]
        return min(subs) if subs else 1.0
    if "any_of" in expr:
        subs = [
            _eval_gpr_ast(s, raw_levels, resolved_out)
            for s in as_list(expr["any_of"])
            if isinstance(s, dict)
        ]
        return (sum(subs) / len(subs)) if subs else 1.0
    return 1.0


def _infer_shared_metabolites(
    src_products: tuple[str, ...],
    tgt_substrates: tuple[str, ...],
) -> tuple[str, ...]:
    """Find shared metabolites between an upstream reaction's products and downstream substrates."""
    CURRENCY = {
        "atp",
        "adp",
        "amp",
        "nad+",
        "nad(+)",
        "nadh",
        "nadp+",
        "nadp(+)",
        "nadph",
        "h2o",
        "water",
        "h+",
        "phosphate",
        "diphosphate",
        "co2",
        "coenzyme a",
        "fad",
        "fadh2",
        "ubiquinone",
        "ubiquinol",
    }
    tgt_lower = {s.lower(): s for s in tgt_substrates}
    shared: list[str] = []
    for p in src_products:
        pl = p.lower()
        if pl in tgt_lower and pl not in CURRENCY:
            shared.append(p)
    if shared:
        return tuple(shared)
    # Also check substring match for stereochemical refinements (e.g. acetoin vs (R)-acetoin)
    for p in src_products:
        pl = p.lower()
        if pl in CURRENCY:
            continue
        for tl, orig_t in tgt_lower.items():
            if tl in CURRENCY:
                continue
            if pl in tl or tl in pl:
                shared.append(orig_t)
                break
    return tuple(dict.fromkeys(shared))


def _eval_fba_logic(
    expr: dict[str, Any],
    active: dict[str, bool],
    flow_inputs: tuple[str, ...] = (),
    competing_inhibitors: tuple[str, ...] = (),
) -> bool:
    """Evaluate a declarative ``LogicExpression`` dict against ``active``."""
    if "element" in expr and expr["element"] is not None:
        v = str(expr["element"])
        if v in competing_inhibitors:
            return False
        if v in flow_inputs:
            return True
        return bool(active.get(v, False))
    op = next((k for k in ("all_of", "any_of", "none_of") if expr.get(k)), None)
    if op is None:
        return True
    subs = [
        _eval_fba_logic(
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


def module_to_fba(
    doc_or_review: Any,
    removed_connections: Any = None,
) -> FBAModel:
    """Derive an :class:`FBAModel` from a module dict, ``ModuleReview``, or YAML path."""
    doc = _coerce_doc(doc_or_review)
    module = doc.get("module")
    if not isinstance(module, dict):
        raise ValueError("module document is missing a top-level 'module' mapping")

    removed = _normalize_removed(removed_connections)
    base_flat = _Flattener(module, frozenset())
    index = _element_index(module)
    labels = _labels(doc)
    optional_set = _optional_elements(module)
    omitted_by_target = {k: set(v) for k, v in omitted_regulators(doc).items()}

    removed_leaf_pairs: set[tuple[str, str]] = set()
    for raw_src, raw_tgt in removed:
        for s in base_flat.exits(raw_src):
            for t in base_flat.entries(raw_tgt):
                if s != t:
                    removed_leaf_pairs.add((s, t))

    order: list[str] = []
    kinds: dict[str, str] = {}
    for node in iter_nodes(module):
        nid = node.get("id")
        if nid:
            s_nid = str(nid)
            order.append(s_nid)
            kinds[s_nid] = "reaction"
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                s_aid = str(annoton["id"])
                order.append(s_aid)
                kinds[s_aid] = "annoton"

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
        desc = (
            str(conn.get("description") or conn.get("chaining_note"))
            if (conn.get("description") or conn.get("chaining_note"))
            else None
        )
        if pred in STRUCTURAL_PREDICATES:
            continue
        if pred not in (
            FLOW_PREDICATES | POSITIVE_REG_PREDICATES | INHIBITING_PREDICATES
        ):
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
    active_flow_outgoing: dict[str, int] = {eid: 0 for eid in variables}

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
            active_flow_outgoing[src] += 1
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

    reactions: list[FBAReaction] = []
    all_gpr_elements: list[FBAGPRElement] = []
    variable_set = set(variables)

    for eid in variables:
        is_flow = eid in base_flow_endpoints
        is_entry = is_flow and base_flow_incoming[eid] == 0
        is_terminal = is_flow and base_flow_outgoing[eid] == 0
        is_opt = eid in optional_set
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
        pos_mods_stage = tuple(r for r in pos_reg_by_target[eid])

        if is_flow:
            (
                gpr_ast,
                gpr_text,
                rxn_gprs,
                func_id,
                func_label,
                substrates,
                products,
                cofactors,
                rep_genes,
            ) = _build_reaction_gpr_and_chemistry(eid, elem_dict)
            for g in rxn_gprs:
                if g.id not in variable_set:
                    all_gpr_elements.append(g)
        else:
            gpr_ast = None
            gpr_text = ""
            func_id = None
            func_label = None
            substrates = ()
            products = ()
            cofactors = ()
            rep_genes = ()

        ub = (
            (OPTIONAL_BRANCH_UPPER_BOUND if is_opt else DEFAULT_UPPER_BOUND)
            if is_flow
            else 0.0
        )
        reactions.append(
            FBAReaction(
                id=eid,
                label=labels.get(eid, eid),
                kind="reaction" if is_flow else "regulator",
                is_flow_stage=is_flow,
                is_entry=is_entry,
                is_terminal=is_terminal,
                is_optional_branch=is_opt,
                default_active=default_active,
                upper_bound=ub,
                location_label=loc_label,
                location_id=loc_id,
                function_id=func_id,
                function_label=func_label,
                substrates=substrates,
                products=products,
                cofactors=cofactors,
                representative_genes=rep_genes,
                gpr_logic=gpr_ast,
                gpr_rule_text=gpr_text,
                gate_activators=gate_acts,
                gate_inhibitors=gate_inhs,
                activation_logic=logic_by_target.get(eid),
                flow_inputs=tuple(flow_inputs_by_target[eid]),
                competing_inhibitors=comp_inhs_stage,
                positive_modulators=pos_mods_stage,
            )
        )

    entry_reactions = [r.id for r in reactions if r.is_entry]
    if not entry_reactions:
        entry_reactions = [r.id for r in reactions if r.is_flow_stage][:1]
    terminal_reactions = [r.id for r in reactions if r.is_terminal]

    # Effective terminals: base terminals PLUS any flow reaction whose outgoing
    # connections were all explicitly severed via removed_connections.
    effective_terminals = [
        r.id
        for r in reactions
        if r.is_flow_stage
        and (r.is_terminal or active_flow_outgoing.get(r.id, 0) == 0)
    ]

    rxn_by_id = {r.id: r for r in reactions}
    transitions: list[FBATransition] = []
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
        shared_mets = _infer_shared_metabolites(
            rxn_by_id[src].products, rxn_by_id[tgt].substrates
        )
        transitions.append(
            FBATransition(
                source=src,
                target=tgt,
                predicate=pred,
                shared_metabolites=shared_mets,
                description=desc,
                is_optional_branch=rxn_by_id[tgt].is_optional_branch,
                competing_inhibitors=comp_inhs,
                positive_modulators=pos_mods,
                gate_activators=gate_acts,
                gate_inhibitors=gate_inhs,
                activation_logic=logic_by_target.get(tgt),
                flow_inputs=tuple(flow_inputs_by_target[tgt]),
            )
        )

    return FBAModel(
        module_id=str(doc.get("id") or module.get("id") or ""),
        title=str(doc.get("title") or doc.get("id") or ""),
        reactions=reactions,
        gpr_elements=all_gpr_elements,
        transitions=transitions,
        entry_reactions=entry_reactions,
        terminal_reactions=terminal_reactions,
        effective_terminals=effective_terminals,
        skipped_connections=skipped,
        removed_connections=sorted(removed_leaf_pairs),
        invalid_activation_logic=invalid_logic,
    )


def _resolve_fba_active(
    model: FBAModel,
    settings: Mapping[str, bool | float],
    gpr_capacities: Mapping[str, float],
) -> tuple[dict[str, bool], bool]:
    """Determine which reactions/regulators are active after applying settings, GPR, and gates."""
    active: dict[str, bool] = {}
    for rxn in model.reactions:
        if rxn.id in settings:
            val = settings[rxn.id]
            active[rxn.id] = bool(val) if isinstance(val, bool) else (float(val) > FLUX_EPSILON)
        elif rxn.is_flow_stage and gpr_capacities.get(rxn.id, 1.0) <= FLUX_EPSILON:
            active[rxn.id] = False
        else:
            active[rxn.id] = rxn.default_active

    converged = False
    for _ in range(len(model.reactions) + 1):
        changed = False
        for rxn in model.reactions:
            if rxn.id in settings:
                continue
            if rxn.is_flow_stage and gpr_capacities.get(rxn.id, 1.0) <= FLUX_EPSILON:
                new_val = False
            else:
                gated_off = False
                if rxn.activation_logic is not None:
                    gated_off = not _eval_fba_logic(
                        rxn.activation_logic,
                        active,
                        flow_inputs=rxn.flow_inputs,
                        competing_inhibitors=rxn.competing_inhibitors,
                    )
                else:
                    if any(not active.get(r, True) for r in rxn.gate_activators):
                        gated_off = True
                    if any(active.get(r, False) for r in rxn.gate_inhibitors):
                        gated_off = True
                new_val = False if gated_off else rxn.default_active
            if active[rxn.id] != new_val:
                active[rxn.id] = new_val
                changed = True
        if not changed:
            converged = True
            break
    return active, converged


def _waterfill_allocate(
    total_to_allocate: float,
    caps: list[float],
    weights: list[float],
) -> list[float]:
    """Allocate ``total_to_allocate`` across branches respecting upper ``caps`` and ``weights``."""
    n = len(caps)
    alloc = [0.0] * n
    rem = min(total_to_allocate, sum(max(0.0, c) for c in caps))
    if rem <= FLUX_EPSILON or n == 0:
        return alloc

    open_idxs = [i for i in range(n) if caps[i] > FLUX_EPSILON and weights[i] > 0.0]
    while rem > FLUX_EPSILON and open_idxs:
        w_sum = sum(weights[i] for i in open_idxs)
        if w_sum <= 0.0:
            break
        saturated_any = False
        shares: dict[int, float] = {}
        for i in open_idxs:
            room = caps[i] - alloc[i]
            desire = rem * (weights[i] / w_sum)
            if desire >= room - 1e-12:
                alloc[i] = caps[i]
                rem -= room
                saturated_any = True
            else:
                shares[i] = desire
        if saturated_any:
            open_idxs = [
                i for i in open_idxs if (caps[i] - alloc[i]) > FLUX_EPSILON
            ]
        else:
            for i, d in shares.items():
                alloc[i] += d
            rem = 0.0
            break
    return alloc


def simulate_fba(
    model: FBAModel,
    settings: Mapping[str, bool | float] | None = None,
    uptake_rate: float = DEFAULT_UPTAKE_RATE,
) -> FBASimulation:
    """Solve steady-state Parsimonious FBA / E-Flux on ``model``."""
    pinned = dict(settings or {})

    # 1. Evaluate GPR AST capacities for all GPR sub-elements and parent reactions
    raw_gpr_levels: dict[str, float] = {}
    for g in model.gpr_elements:
        if g.id in pinned:
            v = pinned[g.id]
            raw_gpr_levels[g.id] = (1.0 if v else 0.0) if isinstance(v, bool) else max(0.0, float(v))
        else:
            raw_gpr_levels[g.id] = 1.0 if g.default_active else 0.0

    gpr_capacities: dict[str, float] = {}
    for rxn in model.reactions:
        if not rxn.is_flow_stage:
            continue
        if rxn.gpr_logic is not None:
            cap = _eval_gpr_ast(rxn.gpr_logic, raw_gpr_levels, gpr_capacities)
        else:
            cap = 1.0
        if rxn.id in pinned:
            v = pinned[rxn.id]
            pin_factor = (1.0 if v else 0.0) if isinstance(v, bool) else max(0.0, float(v))
            cap *= pin_factor
        gpr_capacities[rxn.id] = round(cap, 6)

    for g in model.gpr_elements:
        if g.id not in gpr_capacities:
            gpr_capacities[g.id] = round(raw_gpr_levels[g.id], 6)

    # 2. Resolve regulatory gates
    element_active, converged = _resolve_fba_active(model, pinned, gpr_capacities)

    # 3. Compute effective upper bounds UB_r for every reaction and transition
    reaction_bounds: dict[str, float] = {}
    for rxn in model.reactions:
        if not rxn.is_flow_stage or not element_active.get(rxn.id, False):
            reaction_bounds[rxn.id] = 0.0
            continue
        ub = rxn.upper_bound * gpr_capacities.get(rxn.id, 1.0)
        for inh in rxn.competing_inhibitors:
            if element_active.get(inh, False):
                ub *= COMPETING_INHIBITOR_FACTOR
        for mod in rxn.positive_modulators:
            if element_active.get(mod, False):
                ub *= POSITIVE_REGULATOR_BOOST
            elif rxn.activation_logic is None:
                ub = 0.0
        reaction_bounds[rxn.id] = max(0.0, ub)

    outgoing_by_src: dict[str, list[tuple[int, FBATransition, float]]] = {
        r.id: [] for r in model.reactions
    }
    incoming_by_tgt: dict[str, list[int]] = {r.id: [] for r in model.reactions}
    edge_ubs: list[float] = []

    for idx, t in enumerate(model.transitions):
        if not element_active.get(t.source, False) or not element_active.get(
            t.target, False
        ):
            edge_ubs.append(0.0)
            continue
        if t.activation_logic is not None:
            if not _eval_fba_logic(
                t.activation_logic,
                element_active,
                flow_inputs=t.flow_inputs,
                competing_inhibitors=t.competing_inhibitors,
            ):
                edge_ubs.append(0.0)
                continue
        else:
            if any(not element_active.get(r, True) for r in t.gate_activators):
                edge_ubs.append(0.0)
                continue
            if any(element_active.get(r, False) for r in t.gate_inhibitors):
                edge_ubs.append(0.0)
                continue

        e_ub = min(reaction_bounds[t.source], reaction_bounds[t.target])
        for inh in t.competing_inhibitors:
            if element_active.get(inh, False):
                e_ub *= COMPETING_INHIBITOR_FACTOR
        for mod in t.positive_modulators:
            if element_active.get(mod, False):
                e_ub *= POSITIVE_REGULATOR_BOOST
            elif t.activation_logic is None:
                e_ub = 0.0
        e_ub = max(0.0, e_ub)
        edge_ubs.append(e_ub)
        if e_ub > FLUX_EPSILON:
            outgoing_by_src[t.source].append((idx, t, e_ub))
            incoming_by_tgt[t.target].append(idx)

    # 4. Backward Pass: Compute steady-state sink-reachable capacity C_down(r)
    #    and parsimony path cost L(r) (steps to terminal sink).
    eff_term_set = set(model.effective_terminals)
    flow_rxns = [r for r in model.reactions if r.is_flow_stage]
    downstream_cap: dict[str, float] = {}
    parsimony_cost: dict[str, float] = {}

    for r in flow_rxns:
        if r.id in eff_term_set:
            downstream_cap[r.id] = reaction_bounds[r.id]
            parsimony_cost[r.id] = 1.0 + (2.0 if r.is_optional_branch else 0.0)
        else:
            downstream_cap[r.id] = 0.0
            parsimony_cost[r.id] = 1e6

    for _ in range(len(flow_rxns) + 2):
        changed = False
        for r in reversed(flow_rxns):
            if r.id in eff_term_set:
                continue
            outs = outgoing_by_src.get(r.id, [])
            if not outs:
                new_cap = 0.0
                new_cost = 1e6
            else:
                edge_caps = [
                    min(e_ub, downstream_cap.get(t.target, 0.0))
                    for _idx, t, e_ub in outs
                ]
                new_cap = min(reaction_bounds[r.id], sum(edge_caps))
                open_costs = [
                    parsimony_cost[t.target]
                    for (_idx, t, _e_ub), ec in zip(outs, edge_caps)
                    if ec > FLUX_EPSILON
                ]
                step_penalty = 1.0 + (2.0 if r.is_optional_branch else 0.0)
                new_cost = (
                    (step_penalty + min(open_costs)) if open_costs else 1e6
                )
            if (
                abs(downstream_cap[r.id] - new_cap) > 1e-9
                or abs(parsimony_cost[r.id] - new_cost) > 1e-9
            ):
                downstream_cap[r.id] = new_cap
                parsimony_cost[r.id] = new_cost
                changed = True
        if not changed:
            break

    # 5. Forward Pass: Allocate steady-state flux from entry_reactions to terminals
    #    preserving Kirchhoff mass balance (sum_in == v_r == sum_out) at every node.
    rxn_flux: dict[str, float] = {r.id: 0.0 for r in model.reactions}
    edge_flux: list[float] = [0.0] * len(model.transitions)

    entry_ids = [
        eid
        for eid in model.entry_reactions
        if downstream_cap.get(eid, 0.0) > FLUX_EPSILON
    ]
    if entry_ids and uptake_rate > 0.0:
        entry_caps = [downstream_cap[eid] for eid in entry_ids]
        entry_weights = [
            downstream_cap[eid] / max(1.0, parsimony_cost.get(eid, 1.0))
            for eid in entry_ids
        ]
        entry_alloc = _waterfill_allocate(uptake_rate, entry_caps, entry_weights)
        for eid, val in zip(entry_ids, entry_alloc):
            rxn_flux[eid] = val

    # Propagate forward through the network until steady-state convergence
    entry_set = set(model.entry_reactions)
    for _ in range(len(flow_rxns) + 2):
        prev_edge_flux = list(edge_flux)
        # Recompute incoming flux for non-entry reactions and allocate outgoing flux
        # Track remaining downstream capacity on target nodes during this pass
        target_allocated: dict[str, float] = {r.id: 0.0 for r in flow_rxns}
        for r in flow_rxns:
            if r.id not in entry_set:
                inc_edges = incoming_by_tgt.get(r.id, [])
                rxn_flux[r.id] = min(
                    downstream_cap.get(r.id, 0.0),
                    sum(edge_flux[idx] for idx in inc_edges),
                )
            u_flux = rxn_flux[r.id]
            if r.id in eff_term_set:
                continue
            outs = outgoing_by_src.get(r.id, [])
            if not outs or u_flux <= FLUX_EPSILON:
                for idx, _t, _e_ub in outs:
                    edge_flux[idx] = 0.0
                continue

            caps: list[float] = []
            weights: list[float] = []
            for idx, t, e_ub in outs:
                rem_tgt = max(
                    0.0,
                    downstream_cap.get(t.target, 0.0)
                    - target_allocated.get(t.target, 0.0),
                )
                c = min(e_ub, rem_tgt)
                caps.append(c)
                w = c / max(1.0, parsimony_cost.get(t.target, 1.0))
                weights.append(w)

            alloc = _waterfill_allocate(u_flux, caps, weights)
            for (idx, t, _e_ub), f_val in zip(outs, alloc):
                edge_flux[idx] = f_val
                target_allocated[t.target] = (
                    target_allocated.get(t.target, 0.0) + f_val
                )
            # Tight backward correction if downstream convergence capped total outflux
            actual_out = sum(alloc)
            if actual_out < u_flux - 1e-9:
                rxn_flux[r.id] = actual_out

        if max(
            (abs(a - b) for a, b in zip(edge_flux, prev_edge_flux)), default=0.0
        ) < 1e-9:
            break

    # Final backward consistency sweep so upstream reactions match actual downstream flow
    for _ in range(len(flow_rxns)):
        for r in reversed(flow_rxns):
            if r.id not in eff_term_set:
                outs = outgoing_by_src.get(r.id, [])
                rxn_flux[r.id] = sum(edge_flux[idx] for idx, _t, _e_ub in outs)
            if r.id not in entry_set:
                inc = incoming_by_tgt.get(r.id, [])
                in_sum = sum(edge_flux[idx] for idx in inc)
                if in_sum > rxn_flux[r.id] + 1e-9 and in_sum > 0:
                    scale = rxn_flux[r.id] / in_sum
                    for idx in inc:
                        edge_flux[idx] *= scale

    # Compute steady-state mass-balance residuals (S*v = 0 check at internal nodes)
    residuals: dict[str, float] = {}
    for r in flow_rxns:
        inc_sum = (
            rxn_flux[r.id]
            if r.id in entry_set
            else sum(edge_flux[idx] for idx in incoming_by_tgt.get(r.id, []))
        )
        out_sum = (
            rxn_flux[r.id]
            if r.id in eff_term_set
            else sum(edge_flux[idx] for idx, _t, _e in outgoing_by_src.get(r.id, []))
        )
        residuals[r.id] = round(inc_sum - out_sum, 6)

    rounded_rxn_flux = {k: round(v, 4) for k, v in rxn_flux.items()}
    rounded_bounds = {k: round(v, 4) for k, v in reaction_bounds.items()}
    rounded_down = {k: round(v, 4) for k, v in downstream_cap.items()}

    transition_fluxes: list[dict[str, Any]] = []
    for idx, t in enumerate(model.transitions):
        transition_fluxes.append(
            {
                "source": t.source,
                "target": t.target,
                "predicate": t.predicate,
                "shared_metabolites": list(t.shared_metabolites),
                "upper_bound": round(edge_ubs[idx], 4),
                "flux": round(edge_flux[idx], 4),
                "is_optional_branch": t.is_optional_branch,
                "competing_inhibitors": list(t.competing_inhibitors),
                "positive_modulators": list(t.positive_modulators),
            }
        )

    total_uptake = round(
        sum(rxn_flux.get(eid, 0.0) for eid in model.entry_reactions), 4
    )
    total_export = round(
        sum(rxn_flux.get(tid, 0.0) for tid in model.effective_terminals), 4
    )
    total_l1 = round(sum(rxn_flux.values()), 4)

    return FBASimulation(
        uptake_rate=uptake_rate,
        settings=pinned,
        element_active=element_active,
        gpr_capacities=gpr_capacities,
        reaction_bounds=rounded_bounds,
        downstream_capacities=rounded_down,
        reaction_fluxes=rounded_rxn_flux,
        transition_fluxes=transition_fluxes,
        mass_balance_residuals=residuals,
        total_uptake_flux=total_uptake,
        total_export_flux=total_export,
        total_l1_flux=total_l1,
        converged=converged,
    )


def fba_models(doc_or_review: Any) -> list[dict[str, Any]]:
    """The ``executable_models`` entries of type ``CONSTRAINT_BASED`` derived from the module."""
    doc = _coerce_doc(doc_or_review)
    return [
        m
        for m in as_list(doc.get("executable_models"))
        if isinstance(m, dict)
        and m.get("model_type") == "CONSTRAINT_BASED"
        and m.get("derivation") == "DERIVED_FROM_MODULE"
    ]


def _run_fba_scenario_with_sim(
    doc: dict[str, Any],
    model_id: str,
    scenario_or_dict: Any,
    uptake_rate: float = DEFAULT_UPTAKE_RATE,
) -> tuple[ScenarioResult, FBASimulation, FBAModel]:
    """Run a single CONSTRAINT_BASED scenario and return ``(result, simulation, fba_model)``."""
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
                f"{boolean_only_slot} is not supported on CONSTRAINT_BASED scenarios"
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

    fba = module_to_fba(doc, removed_connections=removed)
    for raw_src, pred, raw_tgt in fba.skipped_connections:
        failures.append(
            f"unsupported connection_type {pred!r} on {raw_src} -> {raw_tgt}"
        )
    for bad_logic in fba.invalid_activation_logic:
        if not any(bad_logic in f for f in failures):
            failures.append(f"invalid activation_logic: {bad_logic}")

    controllable = fba.controllable_ids
    rxn_map = fba.reaction_map()
    gpr_map = fba.gpr_map()

    settings = _fba_settings(scenario)
    bad = sorted(set(settings) - controllable)
    if bad:
        failures.append(
            f"settings name elements that are not model reactions or GPR elements: {bad}"
        )
        valid_settings = {k: v for k, v in settings.items() if k in controllable}
        sim = simulate_fba(fba, settings=valid_settings, uptake_rate=uptake_rate)
        return ScenarioResult(model_id, sid, label, [], failures), sim, fba

    sim = simulate_fba(fba, settings=settings, uptake_rate=uptake_rate)
    if not sim.converged:
        failures.append(
            "regulator gating did not converge (oscillating regulator loop)"
        )

    def is_element_active(eid: str) -> bool:
        if eid in rxn_map:
            rxn = rxn_map[eid]
            if rxn.is_flow_stage:
                return sim.reaction_fluxes.get(eid, 0.0) > FLUX_EPSILON
            return sim.element_active.get(eid, False)
        if eid in gpr_map:
            parent_id = gpr_map[eid].reaction_id
            return (
                sim.gpr_capacities.get(eid, 0.0) > FLUX_EPSILON
                and sim.reaction_fluxes.get(parent_id, 0.0) > FLUX_EPSILON
            )
        return False

    for eid in as_list(scenario.get("expected_active")):
        eid = str(eid)
        if eid not in controllable:
            failures.append(
                f"expected_active names {eid}, which is not a model reaction or GPR element"
            )
        elif not is_element_active(eid):
            flux_val = sim.reaction_fluxes.get(
                eid,
                sim.reaction_fluxes.get(
                    gpr_map[eid].reaction_id if eid in gpr_map else "", 0.0
                ),
            )
            ub_val = sim.reaction_bounds.get(eid, sim.gpr_capacities.get(eid, 0.0))
            failures.append(
                f"expected {eid} to carry positive steady-state flux "
                f"(flux={flux_val}, bound={ub_val}, "
                f"enabled={sim.element_active.get(eid, True)})"
            )

    for eid in as_list(scenario.get("expected_inactive")):
        eid = str(eid)
        if eid not in controllable:
            failures.append(
                f"expected_inactive names {eid}, which is not a model reaction or GPR element"
            )
        elif is_element_active(eid):
            flux_val = sim.reaction_fluxes.get(
                eid,
                sim.reaction_fluxes.get(
                    gpr_map[eid].reaction_id if eid in gpr_map else "", 0.0
                ),
            )
            ub_val = sim.reaction_bounds.get(eid, sim.gpr_capacities.get(eid, 0.0))
            failures.append(
                f"expected {eid} to carry zero steady-state flux "
                f"(flux={flux_val}, bound={ub_val}, "
                f"enabled={sim.element_active.get(eid, True)})"
            )

    order_list = [str(e) for e in as_list(scenario.get("expected_outcome_order"))]
    if 0 < len(order_list) < 2:
        failures.append(
            "expected_outcome_order requires at least 2 reactions to compare"
        )
    unknown_order = [e for e in order_list if e not in rxn_map]
    for eid in unknown_order:
        failures.append(
            f"expected_outcome_order names {eid}, which is not a model reaction"
        )
    if not unknown_order and len(order_list) >= 2:
        for higher, lower in zip(order_list, order_list[1:]):
            f_high = sim.reaction_fluxes.get(higher, 0.0)
            f_low = sim.reaction_fluxes.get(lower, 0.0)
            if not (f_high > f_low + FLUX_EPSILON):
                failures.append(
                    f"expected_outcome_order violated: "
                    f"flux[{higher}]={f_high} is not > "
                    f"flux[{lower}]={f_low}"
                )

    mask = sum(
        (1 << idx)
        for idx, v in enumerate(fba.variables)
        if is_element_active(v)
    )
    attr = Attractor(list(fba.variables), [mask])
    return ScenarioResult(model_id, sid, label, [attr], failures), sim, fba


def run_fba_scenario(
    doc_or_review: Any,
    model_id: str,
    scenario_or_dict: Any,
    uptake_rate: float = DEFAULT_UPTAKE_RATE,
) -> ScenarioResult:
    """Run a single scenario against a module-derived FBA model and check expectations."""
    doc = _coerce_doc(doc_or_review)
    result, _sim, _fba = _run_fba_scenario_with_sim(
        doc, model_id, scenario_or_dict, uptake_rate=uptake_rate
    )
    return result


def run_declared_fba_scenarios(doc_or_review: Any) -> list[ScenarioResult]:
    """Run every scenario on every derived ``CONSTRAINT_BASED`` model the module declares."""
    doc = _coerce_doc(doc_or_review)
    results: list[ScenarioResult] = []
    for model in fba_models(doc):
        for scenario in as_list(model.get("scenarios")):
            if isinstance(scenario, dict):
                results.append(run_fba_scenario(doc, str(model.get("id")), scenario))
    return results


def fba_model_payload(
    doc_or_review: Any,
    model_entry: Any,
) -> dict[str, Any]:
    """Build a JSON-ready payload for the interactive browser FBA / E-Flux simulation page."""
    doc = _coerce_doc(doc_or_review)
    if not isinstance(model_entry, dict) and hasattr(model_entry, "model_dump"):
        model_entry = model_entry.model_dump(mode="json", exclude_none=True)

    base_fba = module_to_fba(doc)
    baseline_sim = simulate_fba(base_fba)
    model_id = str(model_entry.get("id") or "")

    scenarios_out: list[dict[str, Any]] = []
    for sc in as_list(model_entry.get("scenarios")):
        if not isinstance(sc, dict):
            continue
        result, sim, sc_fba = _run_fba_scenario_with_sim(doc, model_id, sc)
        settings = _fba_settings(sc)
        scenarios_out.append(
            {
                "id": sc.get("id"),
                "label": sc.get("label") or sc.get("id"),
                "description": sc.get("description") or "",
                "settings": settings,
                "removed_connections": [
                    {"source": s, "target": t} for s, t in sc_fba.removed_connections
                ],
                "expected_active": [str(x) for x in as_list(sc.get("expected_active"))],
                "expected_inactive": [
                    str(x) for x in as_list(sc.get("expected_inactive"))
                ],
                "expected_outcome_order": [
                    str(x) for x in as_list(sc.get("expected_outcome_order"))
                ],
                "passed": result.passed,
                "failures": result.failures,
                "simulation": {
                    "uptake_rate": sim.uptake_rate,
                    "element_active": sim.element_active,
                    "gpr_capacities": sim.gpr_capacities,
                    "reaction_bounds": sim.reaction_bounds,
                    "downstream_capacities": sim.downstream_capacities,
                    "reaction_fluxes": sim.reaction_fluxes,
                    "transition_fluxes": sim.transition_fluxes,
                    "mass_balance_residuals": sim.mass_balance_residuals,
                    "total_uptake_flux": sim.total_uptake_flux,
                    "total_export_flux": sim.total_export_flux,
                    "total_l1_flux": sim.total_l1_flux,
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
        or f"{doc.get('title')} — constraint-based flux model",
        "model_type": "CONSTRAINT_BASED",
        "derivation": "DERIVED_FROM_MODULE",
        "description": model_entry.get("description") or "",
        "notes": model_entry.get("notes") or "",
        "parameters": {
            "uptake_rate": DEFAULT_UPTAKE_RATE,
            "default_upper_bound": DEFAULT_UPPER_BOUND,
            "optional_branch_upper_bound": OPTIONAL_BRANCH_UPPER_BOUND,
            "competing_inhibitor_factor": COMPETING_INHIBITOR_FACTOR,
            "positive_regulator_boost": POSITIVE_REGULATOR_BOOST,
        },
        "reactions": [
            {
                "id": r.id,
                "label": r.label,
                "kind": r.kind,
                "is_flow_stage": r.is_flow_stage,
                "is_entry": r.is_entry,
                "is_terminal": r.is_terminal,
                "is_optional_branch": r.is_optional_branch,
                "default_active": r.default_active,
                "upper_bound": r.upper_bound,
                "location_label": r.location_label or "",
                "location_id": r.location_id or "",
                "function_id": r.function_id or "",
                "function_label": r.function_label or "",
                "substrates": list(r.substrates),
                "products": list(r.products),
                "cofactors": list(r.cofactors),
                "representative_genes": list(r.representative_genes),
                "gpr_logic": r.gpr_logic,
                "gpr_rule_text": r.gpr_rule_text,
                "gate_activators": list(r.gate_activators),
                "gate_inhibitors": list(r.gate_inhibitors),
                "activation_logic": r.activation_logic,
                "flow_inputs": list(r.flow_inputs),
                "competing_inhibitors": list(r.competing_inhibitors),
                "positive_modulators": list(r.positive_modulators),
            }
            for r in base_fba.reactions
        ],
        "gpr_elements": [
            {
                "id": g.id,
                "label": g.label,
                "kind": g.kind,
                "reaction_id": g.reaction_id,
                "default_active": g.default_active,
                "function_id": g.function_id or "",
                "function_label": g.function_label or "",
                "representative_genes": list(g.representative_genes),
            }
            for g in base_fba.gpr_elements
        ],
        "transitions": [
            {
                "source": t.source,
                "target": t.target,
                "predicate": t.predicate,
                "shared_metabolites": list(t.shared_metabolites),
                "description": t.description or "",
                "is_optional_branch": t.is_optional_branch,
                "competing_inhibitors": list(t.competing_inhibitors),
                "positive_modulators": list(t.positive_modulators),
                "gate_activators": list(t.gate_activators),
                "gate_inhibitors": list(t.gate_inhibitors),
                "activation_logic": t.activation_logic,
                "flow_inputs": list(t.flow_inputs),
            }
            for t in base_fba.transitions
        ],
        "entry_reactions": list(base_fba.entry_reactions),
        "terminal_reactions": list(base_fba.terminal_reactions),
        "baseline_simulation": {
            "uptake_rate": baseline_sim.uptake_rate,
            "element_active": baseline_sim.element_active,
            "gpr_capacities": baseline_sim.gpr_capacities,
            "reaction_bounds": baseline_sim.reaction_bounds,
            "downstream_capacities": baseline_sim.downstream_capacities,
            "reaction_fluxes": baseline_sim.reaction_fluxes,
            "transition_fluxes": baseline_sim.transition_fluxes,
            "mass_balance_residuals": baseline_sim.mass_balance_residuals,
            "total_uptake_flux": baseline_sim.total_uptake_flux,
            "total_export_flux": baseline_sim.total_export_flux,
            "total_l1_flux": baseline_sim.total_l1_flux,
        },
        "scenarios": scenarios_out,
    }
