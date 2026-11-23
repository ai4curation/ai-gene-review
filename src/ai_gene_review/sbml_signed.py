#!/usr/bin/env python
"""Read signed regulatory edges out of an SBML kinetic model and compare them with a module.

A curated module asserts a signed causal graph (``CAUSES``, ``NEGATIVELY_REGULATES``
and so on), and :mod:`ai_gene_review.module_boolean` already compares that graph with
published Boolean models and SIGNOR through a reviewed mapping. This module adds
kinetic (ODE) models, in SBML, as a further source of the same kind of evidence.

How an edge is read from a kinetic model
----------------------------------------
Species are grouped into **entities** (the phosphoforms of one kinase are one entity)
and each species has an **activity level**, how far that form is along the
activation path (0 for the inactive form). Both come from a reviewed mapping, because
neither can be inferred reliably from the SBML.

For each reaction:

1. The reaction's **effect** on an entity is the change in that entity's activity
   mass: the sum of ``level x stoichiometry`` over its products minus the same over
   its reactants. A phosphorylation of S to S-P raises the activity of S (effect
   ``+``); a dephosphorylation lowers it (``-``). Entities whose activity does not
   change are not targets.
2. Every other species that appears in the rate law (or is listed as a modifier) is
   an **effector**. Its sign is the sign of the partial derivative of the rate with
   respect to it, evaluated at the model's own parameter values over a log-uniform
   sample of species concentrations. If the derivative is positive at some sample
   points and negative at others, the sign is ``?``.
3. The edge ``effector -> target`` has the product of the two signs: an activator of
   a deactivating reaction (a phosphatase) is an inhibitor of the target.

An inactive form (level 0) that appears in a rate law is reported, not counted: its
effect on the rate is not an effect of the entity's activity. Reactions between
complexes, rules and events are outside this first version and are listed in the
extraction notes rather than silently dropped.

The model is evidence, not truth: the comparison reports agreements and
disagreements for a curator to adjudicate and never edits a module.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Union

from ai_gene_review.module_boolean import (
    SignedEdge,
    SignedEdgeDiff,
    diff_signed_edges,
    iter_mapping_pairs,
    load_mapping,
    module_file_to_boolean,
    path_sign,
    project_edges,
)

PathLike = Union[str, Path]

#: Biological qualifiers whose resources identify what a species is.
_IDENTITY_QUALIFIERS = {"is", "isVersionOf", "hasVersion", "isEncodedBy"}


@dataclass
class SbmlEntityMap:
    """Reviewed grouping of SBML species into entities, with activity levels.

    Species not listed in ``entity_of`` are their own entity; species not listed in
    ``level_of`` have activity level 1 (an active form).

    >>> m = SbmlEntityMap(entity_of={"S": "SUB", "S_P": "SUB"}, level_of={"S": 0, "S_P": 1})
    >>> m.entity("S_P"), m.entity("other"), m.level("S"), m.level("other")
    ('SUB', 'other', 0, 1)
    """

    entity_of: dict[str, str] = field(default_factory=dict)
    level_of: dict[str, int] = field(default_factory=dict)

    def entity(self, species_id: str) -> str:
        """The entity a species belongs to (itself when unmapped)."""
        return self.entity_of.get(species_id, species_id)

    def level(self, species_id: str) -> int:
        """The activity level of a species form (1 when not listed)."""
        return self.level_of.get(species_id, 1)

    @classmethod
    def from_mapping(cls, mapping: dict[str, Any]) -> "SbmlEntityMap":
        """Build from a mapping document's ``external`` and ``activity_levels`` sections."""
        entity_of = dict(iter_mapping_pairs(mapping.get("external") or {}))
        levels = mapping.get("activity_levels") or {}
        return cls(
            entity_of=entity_of, level_of={str(k): int(v) for k, v in levels.items()}
        )

    @classmethod
    def from_mapping_file(cls, path: PathLike) -> "SbmlEntityMap":
        """Build from a reviewed mapping YAML file (see ``models/kinetic/README.md``)."""
        return cls.from_mapping(load_mapping(path))


@dataclass
class SbmlEdgeResult:
    """Signed edges read from an SBML model, with what the reader could not use."""

    edges: set[SignedEdge] = field(default_factory=set)
    notes: list[str] = field(default_factory=list)
    #: entity -> identifiers.org URIs annotated on its species (for checking the mapping)
    annotations: dict[str, set[str]] = field(default_factory=dict)
    #: (source, target) -> reaction ids the edge was read from
    provenance: dict[tuple[str, str], set[str]] = field(default_factory=dict)


def _combine(signs: set[str]) -> str:
    """Combine the signs one edge receives from several reactions.

    >>> _combine({"+"}), _combine({"+", "-"}), _combine({"-", "?"})
    ('+', '?', '?')
    """
    if len(signs) == 1:
        return next(iter(signs))
    return "?"


def _flip(sign: str, effect: int) -> str:
    """Multiply a derivative sign by a reaction's effect (+1 or -1).

    >>> _flip("+", -1), _flip("-", -1), _flip("?", -1), _flip("-", 1)
    ('-', '+', '?', '-')
    """
    if sign == "?" or effect > 0:
        return sign
    return "+" if sign == "-" else "-"


def _read_document(path: PathLike) -> Any:
    """Read an SBML file, failing on errors, with function definitions expanded."""
    import libsbml  # type: ignore[import-untyped]  # via cobra; imported lazily

    doc = libsbml.readSBMLFromFile(str(path))
    errors = [
        doc.getError(i).getMessage()
        for i in range(doc.getNumErrors())
        if doc.getError(i).getSeverity() >= libsbml.LIBSBML_SEV_ERROR
    ]
    if errors or doc.getModel() is None:
        raise ValueError(f"cannot read SBML model {path}: {errors[:3]}")
    props = libsbml.ConversionProperties()
    props.addOption("expandFunctionDefinitions", True)
    if doc.convert(props) != libsbml.LIBSBML_OPERATION_SUCCESS:
        raise ValueError(f"cannot expand function definitions in {path}")
    return doc


def _identity_uris(species: Any) -> set[str]:
    """identifiers.org URIs in a species' identity qualifiers (is, isVersionOf, ...)."""
    import libsbml  # type: ignore[import-untyped]

    uris: set[str] = set()
    for i in range(species.getNumCVTerms()):
        cv = species.getCVTerm(i)
        if cv.getQualifierType() != libsbml.BIOLOGICAL_QUALIFIER:
            continue
        name = libsbml.BiolQualifierType_toString(cv.getBiologicalQualifierType())
        if name not in _IDENTITY_QUALIFIERS:
            continue
        uris.update(cv.getResourceURI(j) for j in range(cv.getNumResources()))
    return uris


def _rate_expression(formula: str, identifiers: set[str]) -> Any:
    """Parse an L3 infix rate law into a sympy expression over model identifiers."""
    import sympy  # type: ignore[import-untyped]
    from sympy.parsing.sympy_parser import (  # type: ignore[import-untyped]
        convert_xor,
        parse_expr,
        standard_transformations,
    )

    local: dict[str, Any] = {name: sympy.Symbol(name) for name in identifiers}
    local.setdefault("time", sympy.Symbol("time"))
    local.update(
        {"ln": sympy.log, "exp": sympy.exp, "pow": sympy.Pow, "sqrt": sympy.sqrt}
    )
    return parse_expr(
        formula,
        local_dict=local,
        transformations=standard_transformations + (convert_xor,),
        evaluate=True,
    )


def _derivative_sign(
    expr: Any,
    variable: Any,
    species_symbols: set[Any],
    values: dict[Any, Optional[float]],
    rng: random.Random,
    samples: int,
) -> Optional[str]:
    """Sign of d(expr)/d(variable) over sampled species concentrations.

    Species concentrations are drawn log-uniformly from [1e-3, 1e3]; other symbols
    take their model values, or are sampled the same way when the model gives none.
    Returns ``+``, ``-``, ``?`` (both signs occur) or ``None`` (no dependence).
    """
    import sympy  # type: ignore[import-untyped]

    derivative = sympy.diff(expr, variable)
    if derivative == 0:
        return None
    symbols = sorted(derivative.free_symbols, key=lambda s: s.name)
    func = sympy.lambdify(symbols, derivative, modules="math")
    signs: set[str] = set()
    for _ in range(samples):
        point: list[float] = []
        for sym in symbols:
            fixed = values.get(sym)
            if sym in species_symbols or fixed is None:
                point.append(10 ** rng.uniform(-3.0, 3.0))
            else:
                point.append(float(fixed))
        try:  # numeric evaluation of arbitrary model maths
            value = float(func(*point))
        except (ZeroDivisionError, OverflowError, ValueError):
            continue
        if math.isnan(value) or value == 0.0:
            continue
        signs.add("+" if value > 0 else "-")
    if not signs:
        return None
    return _combine(signs)


def sbml_signed_edges(
    sbml_path: PathLike,
    entity_map: SbmlEntityMap,
    samples: int = 64,
    seed: int = 0,
) -> SbmlEdgeResult:
    """Read signed ``effector -> target`` edges between entities from an SBML model.

    See the module docstring for the reading rule. ``seed`` makes the derivative
    sampling reproducible.
    """
    import libsbml  # type: ignore[import-untyped]

    doc = _read_document(sbml_path)
    model = doc.getModel()
    rng = random.Random(seed)
    result = SbmlEdgeResult()

    species_ids = [s.getId() for s in model.getListOfSpecies()]
    for s in model.getListOfSpecies():
        uris = _identity_uris(s)
        if uris:
            result.annotations.setdefault(entity_map.entity(s.getId()), set()).update(
                uris
            )

    global_values: dict[str, Optional[float]] = {}
    for c in model.getListOfCompartments():
        global_values[c.getId()] = c.getSize() if c.isSetSize() else None
    for p in model.getListOfParameters():
        global_values[p.getId()] = p.getValue() if p.isSetValue() else None
    for i in range(model.getNumRules()):
        rule = model.getRule(i)
        if rule.getVariable():
            result.notes.append(
                f"rule for {rule.getVariable()} is not evaluated; its value is sampled"
            )
            global_values[rule.getVariable()] = None
    if model.getNumEvents():
        result.notes.append(f"{model.getNumEvents()} event(s) ignored")

    signs: dict[tuple[str, str], set[str]] = {}
    for reaction in model.getListOfReactions():
        rid = reaction.getId()
        law = reaction.getKineticLaw()
        if law is None or law.getMath() is None:
            result.notes.append(f"{rid}: no kinetic law; skipped")
            continue

        delta: dict[str, float] = {}
        for refs, side in (
            (reaction.getListOfReactants(), -1),
            (reaction.getListOfProducts(), 1),
        ):
            for ref in refs:
                sid = ref.getSpecies()
                stoich = ref.getStoichiometry() if ref.isSetStoichiometry() else 1.0
                ent = entity_map.entity(sid)
                delta[ent] = delta.get(ent, 0.0) + side * stoich * entity_map.level(sid)
        targets = {ent: (1 if d > 0 else -1) for ent, d in delta.items() if d != 0}
        converted = set(delta)
        if not targets:
            result.notes.append(f"{rid}: changes no entity's activity; skipped")
            continue

        values: dict[str, Optional[float]] = dict(global_values)
        for local_list in (law.getListOfParameters(), law.getListOfLocalParameters()):
            for p in local_list:
                values[p.getId()] = p.getValue() if p.isSetValue() else None
        identifiers = set(values) | set(species_ids)
        formula = libsbml.formulaToL3String(law.getMath())
        try:  # SBML rate laws are external input; record what cannot be parsed
            expr = _rate_expression(formula, identifiers)
        except (SyntaxError, TypeError, ValueError) as exc:
            result.notes.append(
                f"{rid}: rate law not parsed ({exc.__class__.__name__}): {formula}"
            )
            continue
        symbol_of = {sym.name: sym for sym in expr.free_symbols}
        species_symbols = {symbol_of[s] for s in species_ids if s in symbol_of}
        numeric = {symbol_of[k]: v for k, v in values.items() if k in symbol_of}

        effectors = {s for s in species_ids if s in symbol_of}
        effectors |= {m.getSpecies() for m in reaction.getListOfModifiers()}
        for sid in sorted(effectors):
            ent = entity_map.entity(sid)
            if ent in converted:
                continue  # the converted entity's own forms: mass action, not regulation
            if sid not in symbol_of:
                result.notes.append(
                    f"{rid}: modifier {sid} does not appear in the rate law"
                )
                continue
            if entity_map.level(sid) == 0:
                result.notes.append(
                    f"{rid}: inactive form {sid} of {ent} appears in the rate law; not counted"
                )
                continue
            d_sign = _derivative_sign(
                expr, symbol_of[sid], species_symbols, numeric, rng, samples
            )
            if d_sign is None:
                continue
            for target, effect in sorted(targets.items()):
                if target == ent:
                    continue
                key = (ent, target)
                signs.setdefault(key, set()).add(_flip(d_sign, effect))
                result.provenance.setdefault(key, set()).add(rid)

    for (source, target), found in sorted(signs.items()):
        sign = _combine(found)
        if sign == "?" and found != {"?"}:
            reactions = ", ".join(sorted(result.provenance[(source, target)]))
            result.notes.append(
                f"{source} -> {target}: opposite signs across reactions ({reactions})"
            )
        result.edges.add(SignedEdge(source, target, sign))
    return result


# ---------------------------------------------------------------------------
# Comparison with a curated module
# ---------------------------------------------------------------------------


@dataclass
class ModuleSbmlComparison:
    """Result of comparing a module's signed graph with an SBML model's."""

    module_label: str
    model_label: str
    symbols: set[str]
    diff: SignedEdgeDiff
    extraction: SbmlEdgeResult
    #: edge -> explanation, for module-only and model-only edges
    readings: dict[SignedEdge, str] = field(default_factory=dict)
    #: model edges with an endpoint the module mapping does not name
    out_of_scope: set[SignedEdge] = field(default_factory=set)


def compare_module_to_sbml(
    module_path: PathLike,
    sbml_path: PathLike,
    mapping_path: PathLike,
    module_key: Optional[str] = None,
    seed: int = 0,
) -> ModuleSbmlComparison:
    """Diff a module's signed causal graph with the signed edges of an SBML model.

    Both sides are put in the mapping's shared symbol namespace: the module through
    ``modules.<module_key>`` (default: the module file stem), the model through
    ``external`` and ``activity_levels``. Only edges between symbols the module
    mapping names are compared; model edges reaching other entities are reported
    as out of scope.
    """
    module_path = Path(module_path)
    mapping = load_mapping(mapping_path)
    key = module_key or module_path.stem
    section = (mapping.get("modules") or {}).get(key)
    if not section:
        raise ValueError(f"mapping {mapping_path} has no modules.{key} section")
    module_map = dict(iter_mapping_pairs(section))
    symbols = set(module_map.values())

    bn = module_file_to_boolean(module_path)
    module_edges = project_edges(bn.edges, module_map).edges
    extraction = sbml_signed_edges(
        sbml_path, SbmlEntityMap.from_mapping(mapping), seed=seed
    )
    in_scope = {
        e for e in extraction.edges if e.source in symbols and e.target in symbols
    }
    diff = diff_signed_edges(module_edges, in_scope)

    comparison = ModuleSbmlComparison(
        module_label=module_path.name,
        model_label=Path(sbml_path).name,
        symbols=symbols,
        diff=diff,
        extraction=extraction,
        out_of_scope=extraction.edges - in_scope,
    )
    elements_of: dict[str, set[str]] = {}
    for element, symbol in module_map.items():
        elements_of.setdefault(symbol, set()).add(element)
    modelled = set(SbmlEntityMap.from_mapping(mapping).entity_of.values())

    for edge in diff.right_only:
        comparison.readings[edge] = _read_model_only(edge, bn.edges, elements_of)
    for edge in diff.left_only:
        missing = [s for s in (edge.source, edge.target) if s not in modelled]
        if missing:
            comparison.readings[edge] = (
                f"{', '.join(missing)} has no species in the model"
            )
            continue
        hidden = {e.source for e in extraction.edges} | {
            e.target for e in extraction.edges
        }
        hidden -= {edge.source, edge.target}
        route = path_sign(extraction.edges, edge.source, edge.target, hidden)
        if route == edge.sign:
            comparison.readings[edge] = "the model routes it through other entities"
        else:
            comparison.readings[edge] = "absent from the model"
    return comparison


def _read_model_only(
    edge: SignedEdge, module_edges: set[SignedEdge], elements_of: dict[str, set[str]]
) -> str:
    """Explain a model-only edge in terms of the module's own element graph."""
    sources = elements_of.get(edge.source, set())
    targets = elements_of.get(edge.target, set())
    nodes = {e.source for e in module_edges} | {e.target for e in module_edges}
    hidden = nodes - sources - targets
    forward = {
        path_sign(module_edges, s, t, hidden) for s in sources for t in targets
    } - {None}
    if forward == {edge.sign}:
        return "collapsed path: the module expresses it through intermediate steps"
    backward = {
        path_sign(module_edges, t, s, hidden) for s in sources for t in targets
    } - {None}
    if backward:
        return "feedback absent from the module"
    return "not in the module"


def format_comparison(comparison: ModuleSbmlComparison) -> str:
    """Render a :class:`ModuleSbmlComparison` as a readable report."""
    diff = comparison.diff
    lines = [
        f"# {comparison.module_label} (module) vs {comparison.model_label} (SBML model)",
        "",
        f"shared symbols: {', '.join(sorted(comparison.symbols))}",
        f"agree={len(diff.agree)}  sign_conflicts={len(diff.sign_conflict)}  "
        f"module_only={len(diff.left_only)}  model_only={len(diff.right_only)}",
        "",
    ]
    for edge in sorted(diff.agree, key=str):
        reactions = ", ".join(
            sorted(comparison.extraction.provenance.get((edge.source, edge.target), ()))
        )
        lines.append(f"  = {edge}   (model reactions: {reactions})")
    for left, right in sorted(diff.sign_conflict, key=lambda p: str(p[0])):
        lines.append(f"  ! {left} (module)   vs   {right} (model)")
    for edge in sorted(diff.left_only, key=str):
        lines.append(f"  < {edge}   module only: {comparison.readings.get(edge, '')}")
    for edge in sorted(diff.right_only, key=str):
        lines.append(f"  > {edge}   model only: {comparison.readings.get(edge, '')}")
    if comparison.out_of_scope:
        lines.append("")
        lines.append("model edges outside the mapped symbols:")
        lines.extend(f"  {edge}" for edge in sorted(comparison.out_of_scope, key=str))
    if comparison.extraction.annotations:
        lines.append("")
        lines.append("species annotations per symbol (check against the mapping):")
        for entity, uris in sorted(comparison.extraction.annotations.items()):
            lines.append(f"  {entity}: {', '.join(sorted(uris))}")
    if comparison.extraction.notes:
        lines.append("")
        lines.append("extraction notes:")
        lines.extend(f"  - {note}" for note in comparison.extraction.notes)
    return "\n".join(lines) + "\n"
