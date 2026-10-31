#!/usr/bin/env python
"""Compile a module document into a boolean logic circuit and reason over it.

A :class:`ModuleReview` document describes a biological module (pathway/complex)
as a tree of nodes. Read as logic, that tree is a *monotone boolean formula* over
**step atoms**:

* a node's ``parts`` and its own ``annotons`` are conjunctive  -> :class:`And`
* a ``variant_sets`` entry is disjunctive (at-least-one for satisfiability)
  -> :class:`Or`
* a leaf ``annoton`` is an :class:`Atom` whose truth value is supplied externally
  by a per-context predicate (e.g. "is this participant gene expressed in this
  tissue / cell-zone?").
* a node with a ``module_ref`` is replaced by the compiled referenced module (or
  node), so an umbrella module is satisfied exactly when the modules it composes
  are. Atoms reached through a reference are namespaced ``<module>#<annoton>``.

Separating the *logic* (this module) from the *oracle* (the predicate) lets the
same engine resolve a module against any context source - microbial genome
presence, bulk-tissue expression, or single-cell zonation - without the logic
layer carrying any biological-data dependency. The engine can enumerate the
**routes** through a module (one branch per variant set), evaluate satisfiability
in a context, and identify the **gate** atoms required by every route.

Example: a tiny pathway with one required entry step and a two-way isozyme choice.

>>> doc = {
...   "module": {"id": "m", "parts": [
...     {"order": 1, "node": {"id": "entry", "annotons": [
...        {"id": "a_act", "participant": {"gene": {"preferred_term": "A",
...           "term": {"id": "UniProtKB:P1"}}}}]}},
...     {"order": 2, "node": {"id": "iso", "variant_sets": [
...        {"id": "vs", "selection": "ONE_OR_MORE", "variants": [
...           {"id": "b", "annotons": [{"id": "b_act", "participant": {"gene":
...              {"preferred_term": "B", "term": {"id": "UniProtKB:P2"}}}}]},
...           {"id": "c", "annotons": [{"id": "c_act", "participant": {"gene":
...              {"preferred_term": "C", "term": {"id": "UniProtKB:P3"}}}}]}]}]}},
...   ]}}
>>> circuit = compile_module(doc)
>>> [[a.gene_symbol for a in r] for r in enumerate_routes(circuit)]
[['A', 'B'], ['A', 'C']]
>>> [a.gene_symbol for a in core_atoms(circuit)]
['A']
>>> is_satisfied(circuit, lambda atom: atom.gene_symbol in {"A", "C"})
True
>>> is_satisfied(circuit, lambda atom: atom.gene_symbol in {"B", "C"})  # missing A
False
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterator, Literal, Optional, Union

import yaml

from ai_gene_review.render_modules import as_list
from ai_gene_review.module_gene_symbols import descriptor_symbol
from ai_gene_review.module_qc import DEFAULT_MODULES_DIR, resolve_template_node


@dataclass(frozen=True)
class Atom:
    """A leaf step: a participant gene whose truth value comes from an oracle."""

    node_id: str
    label: str
    gene_symbol: Optional[str]
    uniprot: Optional[str]
    representative_gene_symbols: tuple[str, ...] = ()
    representative_uniprots: tuple[str, ...] = ()
    #: GO molecular-function ids the step requires (annoton ``function`` and
    #: participant ``required_function``), for activity-based oracles.
    function_ids: tuple[str, ...] = ()
    #: Family ids of the participant selector (``family.term`` and
    #: ``family.family_terms``, e.g. PANTHER families), for oracles that scan a
    #: proteome with family models rather than look up named genes.
    family_ids: tuple[str, ...] = ()
    #: Domain ids of the participant selector (``domain`` and ``required_domain``).
    domain_ids: tuple[str, ...] = ()

    @property
    def gene_symbols(self) -> tuple[str, ...]:
        """Return every concrete symbol available for this step."""
        return tuple(dict.fromkeys(
            ([self.gene_symbol] if self.gene_symbol else [])
            + list(self.representative_gene_symbols)
        ))

    @property
    def is_grounded(self) -> bool:
        """True when some oracle could satisfy this step.

        An atom with no symbol, no accession and no required function cannot be
        satisfied by any genome-, expression- or activity-keyed predicate, so
        every route through it is dead and its module is unsatisfiable in every
        context -- silently, since nothing else reports it.

        >>> Atom("n", "l", "A", "P1").is_grounded
        True
        >>> Atom("n", "l", None, None).is_grounded
        False
        >>> Atom("n", "l", None, None, function_ids=("GO:0140911",)).is_grounded
        True
        """
        return bool(self.gene_symbols or self.uniprots or self.function_ids)

    @property
    def uniprots(self) -> tuple[str, ...]:
        """Return every concrete UniProt accession available for this step."""
        return tuple(dict.fromkeys(
            ([self.uniprot] if self.uniprot else [])
            + list(self.representative_uniprots)
        ))

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Atom({self.gene_symbol or self.node_id})"


@dataclass
class And:
    """Conjunction: satisfied iff every child is satisfied."""

    node_id: str
    children: list["Circuit"]


#: The two layers a variant set can belong to (schema ``VariantKindEnum``).
VariantKind = Literal["REALIZER", "ROUTE"]
_VARIANT_KINDS: tuple[VariantKind, ...] = ("REALIZER", "ROUTE")


@dataclass
class Or:
    """Disjunction over variant branches (at-least-one for satisfiability)."""

    set_id: str
    selection: str
    children: list["Circuit"]
    #: Rule layer of the alternatives (``REALIZER`` or ``ROUTE``, see
    #: :data:`VariantKind`), or None when unclassified or an optional part.
    kind: Optional[VariantKind] = None
    #: Whether ``kind`` was declared in the module or inferred by the compiler.
    kind_inferred: bool = False


Circuit = Union[Atom, And, Or]

#: A per-context predicate: does this atom hold (e.g. is its gene expressed)?
Predicate = Callable[[Atom], bool]


def _symbol_from_gene(gene: dict) -> Optional[str]:
    """Use the same conservative symbol-label rule as module validation.

    Ambiguous labels yield no symbol; the descriptor's accession is retained.

    >>> _symbol_from_gene({"preferred_term": "MetXS (PSEPK)"})
    'MetXS'
    >>> _symbol_from_gene({"preferred_term": "PSEPK MetXS"}) is None
    True
    """
    return descriptor_symbol(gene or {})


def _uniprot_from_gene(gene: dict) -> Optional[str]:
    """Return the bare UniProt accession from a GeneDescriptor, if present."""
    term = (gene or {}).get("term") or {}
    tid = term.get("id", "")
    if tid.startswith("UniProtKB:"):
        return tid.split(":", 1)[1]
    return None


def _atom_from_annoton(annoton: dict, namespace: str = "") -> Atom:
    """Build an :class:`Atom` from an annoton dict, prefixing its id with ``namespace#``."""
    participant = annoton.get("participant") or {}
    # A participant grounds through whichever descriptor its selector_type uses:
    # `gene` for a concrete gene, `gene_product` for an exemplar protein (as
    # ANY_WITH_FUNCTION steps carry). Both are Descriptors, so the same symbol
    # and accession rules apply. Reading only `gene` left every gene_product
    # step ungrounded, and an ungrounded atom no oracle can satisfy makes its
    # whole module silently unsatisfiable in every context.
    gene = participant.get("gene") or participant.get("gene_product") or {}
    representatives = ((participant.get("family") or {}).get("representative_members") or [])
    gene_symbol = _symbol_from_gene(gene)
    # An explicit gene supplies the canonical symbol. Family-only fallback
    # applies the same symbol-label rule; ambiguous prose never becomes a symbol.
    representative_symbols = tuple(
        symbol for member in representatives
        if (symbol := _symbol_from_gene(member))
    ) if not gene_symbol else ()
    representative_uniprots = tuple(
        accession for member in representatives
        if (accession := _uniprot_from_gene(member))
    )
    uniprot = _uniprot_from_gene(gene)
    annoton_id = annoton.get("id", "?")
    function_ids = tuple(dict.fromkeys(
        tid for descriptor in (annoton.get("function"), participant.get("required_function"))
        if (tid := ((descriptor or {}).get("term") or {}).get("id", "")).startswith("GO:")
    ))
    family = participant.get("family") or {}
    family_ids = _term_ids([family.get("term"), *as_list(family.get("family_terms"))])
    domain_ids = _term_ids([(participant.get(slot) or {}).get("term")
                            for slot in ("domain", "required_domain")])
    return Atom(
        node_id=f"{namespace}#{annoton_id}" if namespace else annoton_id,
        label=annoton.get("label", annoton.get("id", "?")),
        gene_symbol=gene_symbol or (representative_symbols[0] if representative_symbols else None),
        uniprot=uniprot or (representative_uniprots[0] if representative_uniprots else None),
        representative_gene_symbols=representative_symbols,
        representative_uniprots=representative_uniprots,
        function_ids=function_ids,
        family_ids=family_ids,
        domain_ids=domain_ids,
    )


def _term_ids(terms: list[Optional[dict]]) -> tuple[str, ...]:
    """Return the distinct non-empty ``id`` values of ``terms``, in order."""
    return tuple(dict.fromkeys(tid for term in terms if (tid := (term or {}).get("id"))))


def _variant_kind(variant_set: dict, branches: list[Circuit]) -> tuple[Optional[VariantKind], bool]:
    """Return a variant set's layer and whether it was inferred.

    A declared ``variant_kind`` wins. Otherwise the set is a REALIZER choice
    when every branch requires the same single molecular function (one
    activity, alternative carriers), and is left unclassified when the
    branches differ in function or carry none.

    >>> def branch(*mfs):
    ...     return And("v", [Atom(f"a{i}", "", None, None, function_ids=(mf,))
    ...                      for i, mf in enumerate(mfs)])
    >>> _variant_kind({}, [branch("GO:1"), branch("GO:1")])
    ('REALIZER', True)
    >>> _variant_kind({}, [branch("GO:1"), branch("GO:2")])
    (None, False)
    >>> _variant_kind({"variant_kind": "ROUTE"}, [branch("GO:1"), branch("GO:1")])
    ('ROUTE', False)
    """
    declared = variant_set.get("variant_kind")
    if declared:
        kind = next((k for k in _VARIANT_KINDS if k == declared), None)
        if kind is None:
            raise ValueError(f"variant set {variant_set.get('id')!r}: unknown variant_kind {declared!r}")
        return kind, False
    functions = [{f for atom in iter_atoms(b) for f in atom.function_ids} for b in branches]
    if len(functions) > 1 and all(len(f) == 1 for f in functions) and len(set.union(*functions)) == 1:
        return "REALIZER", True
    return None, False


def _compile_reference(
    node: dict, modules_dir: Path, chain: tuple[str, ...]
) -> And:
    """Compile a ``module_ref`` node as an AND wrapping the referenced module."""
    module_ref = str(node["module_ref"])
    if module_ref in chain:
        raise ValueError(f"module_ref cycle: {' -> '.join([*chain, module_ref])}")
    target = resolve_template_node(module_ref, modules_dir)
    if target is None:
        raise ValueError(f"module_ref '{module_ref}' of node {node.get('id')!r} not found")
    namespace = module_ref.partition("#")[0]
    sub = compile_node(target, modules_dir, (*chain, module_ref), namespace)
    return And(node_id=node.get("id", "?"), children=[sub])


def compile_node(
    node: dict,
    modules_dir: Path = DEFAULT_MODULES_DIR,
    chain: tuple[str, ...] = (),
    namespace: str = "",
) -> And:
    """Compile a ModuleNode dict into an AND over its atoms, parts, and variant sets.

    ``module_ref`` nodes are resolved against ``modules_dir``; ``chain`` holds
    the references being expanded (for cycle detection) and ``namespace`` the
    referenced module whose atoms are being compiled.
    """
    if node.get("module_ref"):
        return _compile_reference(node, Path(modules_dir), chain)
    children: list[Circuit] = []
    for annoton in as_list(node.get("annotons")):
        children.append(_atom_from_annoton(annoton, namespace))
    for part in as_list(node.get("parts")):
        sub = compile_node(part["node"], modules_dir, chain, namespace)
        if part.get("optional"):
            # An optional part is an OR of (filled, empty) -> always satisfiable.
            empty: Circuit = And(node_id="empty", children=[])
            children.append(Or(set_id=f"opt:{part['node'].get('id', '?')}",
                               selection="ZERO_OR_MORE", children=[sub, empty]))
        else:
            children.append(sub)
    for vs in as_list(node.get("variant_sets")):
        branches: list[Circuit] = [
            compile_node(v, modules_dir, chain, namespace) for v in as_list(vs.get("variants"))
        ]
        kind, inferred = _variant_kind(vs, branches)
        children.append(Or(set_id=vs.get("id", "?"),
                           selection=vs.get("selection", "ONE_OR_MORE"),
                           children=branches, kind=kind, kind_inferred=inferred))
    return And(node_id=node.get("id", "?"), children=children)


def compile_module(
    doc: dict,
    modules_dir: Union[str, Path] = DEFAULT_MODULES_DIR,
    stem: Optional[str] = None,
) -> And:
    """Compile a loaded ModuleReview document (its ``module``) into a circuit.

    ``module_ref`` nodes resolve against ``modules_dir``; ``stem`` (the
    document's own file stem) lets a reference back to it be caught as a cycle.
    """
    return compile_node(doc["module"], Path(modules_dir), (stem,) if stem else ())


def compile_module_file(path: Union[str, Path]) -> And:
    """Load a ModuleReview YAML file and compile its root module node.

    References resolve against the file's own directory.
    """
    path = Path(path)
    return compile_module(yaml.safe_load(path.read_text()), path.parent, path.stem)


def iter_atoms(circuit: Circuit) -> Iterator[Atom]:
    """Yield every :class:`Atom` in the circuit (depth-first)."""
    if isinstance(circuit, Atom):
        yield circuit
    else:
        for child in circuit.children:
            yield from iter_atoms(child)


#: Default cap on :func:`enumerate_routes`; umbrella modules multiply route counts.
DEFAULT_MAX_ROUTES = 10_000


def count_routes(circuit: Circuit) -> int:
    """Count the routes :func:`enumerate_routes` would return, without building them.

    >>> count_routes(Or("vs", "ONE_OR_MORE", [Atom("a", "a", "A", None), Atom("b", "b", "B", None)]))
    2
    """
    if isinstance(circuit, Atom):
        return 1
    if isinstance(circuit, And):
        total = 1
        for child in circuit.children:
            total *= count_routes(child)
        return total
    return sum(count_routes(c) for c in circuit.children) or 1


def enumerate_routes(circuit: Circuit, max_routes: int = DEFAULT_MAX_ROUTES) -> list[list[Atom]]:
    """Enumerate satisfying routes.

    Each route picks exactly one branch per :class:`Or` node and includes every
    atom on the conjunctive backbone, each atom once. Returns one atom-list per
    route.

    Route count is the Cartesian product of branch counts across all OR nodes,
    and ``module_ref`` inlining multiplies the counts of every referenced
    module, so this raises ``ValueError`` past ``max_routes``. For umbrella
    modules prefer :func:`is_satisfied`, :func:`unsatisfied_steps` and
    :func:`core_atoms`, which do not materialise routes. When two steps
    reference the same module, each copy's variant sets are enumerated
    independently, so routes may mix different branches of one referenced
    variant set; every such route is still a satisfying set, but routes are
    then not guaranteed minimal.
    """
    total = count_routes(circuit)
    if total > max_routes:
        raise ValueError(
            f"circuit has {total} routes, more than max_routes={max_routes}; "
            "use is_satisfied/unsatisfied_steps/core_atoms instead"
        )
    return _enumerate(circuit)


def _enumerate(circuit: Circuit) -> list[list[Atom]]:
    """Unguarded route enumeration behind :func:`enumerate_routes`."""
    if isinstance(circuit, Atom):
        return [[circuit]]
    if isinstance(circuit, And):
        routes: list[list[Atom]] = [[]]
        for child in circuit.children:
            child_routes = _enumerate(child)
            routes = [_merge_route(r, cr) for r in routes for cr in child_routes]
        return routes
    # Or
    routes = []
    for child in circuit.children:
        routes.extend(_enumerate(child))
    return routes or [[]]


def _merge_route(left: list[Atom], right: list[Atom]) -> list[Atom]:
    """Concatenate two partial routes, keeping each atom (by ``node_id``) once."""
    seen = {a.node_id for a in left}
    return left + [a for a in right if a.node_id not in seen]


def is_satisfied(circuit: Circuit, holds: Predicate) -> bool:
    """Evaluate the circuit given a per-atom truth predicate ``holds``."""
    if isinstance(circuit, Atom):
        return holds(circuit)
    if isinstance(circuit, And):
        return all(is_satisfied(c, holds) for c in circuit.children)
    # Or: an empty disjunction is vacuously satisfied.
    return any(is_satisfied(c, holds) for c in circuit.children) if circuit.children else True


def active_routes(circuit: Circuit, holds: Predicate) -> list[list[Atom]]:
    """Return the routes whose every atom holds under ``holds``."""
    return [r for r in enumerate_routes(circuit) if all(holds(a) for a in r)]


def core_atoms(circuit: Circuit) -> list[Atom]:
    """Atoms required by *every* route (the AND-core; gate candidates).

    If any core atom is unsatisfied no route can succeed, so these are exactly the
    atoms whose absence gates the whole module. Computed structurally (an AND
    unions its children's cores, an OR intersects them), so it does not
    enumerate routes and stays cheap for umbrella modules.
    """
    common = _core_ids(circuit)
    seen: dict[str, Atom] = {}
    for a in iter_atoms(circuit):
        if a.node_id in common:
            seen[a.node_id] = a
    return list(seen.values())


def _core_ids(circuit: Circuit) -> set[str]:
    """Return the ids of atoms present in every route of ``circuit``."""
    if isinstance(circuit, Atom):
        return {circuit.node_id}
    if isinstance(circuit, And):
        return set().union(*(_core_ids(c) for c in circuit.children))
    if not circuit.children:
        return set()
    return set.intersection(*(_core_ids(c) for c in circuit.children))


def step_id(circuit: Circuit) -> str:
    """Return the identifier of a circuit node (atom/AND node id, or OR set id)."""
    if isinstance(circuit, Or):
        return circuit.set_id
    return circuit.node_id


#: The closed set of abduction outcomes (see :func:`abduce`).
Classification = Literal[
    "CONSISTENT_ACTIVE", "CONSISTENT_INACTIVE", "ABDUCTION_TARGET", "OVERPREDICTION"
]


@dataclass
class Abduction:
    """Reconciliation of engine satisfiability with an independent activity claim.

    When a pathway is *independently known* to be active in a context (an organism
    grows without the end product; a flux is measured) but the engine finds it
    unsatisfiable, the unsatisfied steps are not a verdict that the pathway is
    impossible — they are an **abduction**: there must be an explanation the model
    does not yet capture. This object records that reconciliation.
    """

    classification: Classification
    consistent: bool               # engine agrees with the asserted activity
    asserted_active: bool
    satisfiable: bool
    gap_steps: list[str]           # ids of unsatisfied top-level steps
    gap_candidates: dict[str, list[str]]  # per gap step, symbols of the atoms that do not hold
    hypotheses: list[str]          # candidate explanations (when not consistent)
    gaps: list["Gap"] = field(default_factory=list)  # innermost gaps, labelled by layer


#: The layer a gap is reported at: a realizer variant set with no carrier present
#: (``REALIZER``), a route variant set with no route present (``ROUTE``), or a
#: gap whose layer the structure cannot tell (``UNCLASSIFIED``): a single-carrier
#: step, or a variant set with no declared or inferable kind.
GapLayer = Literal["REALIZER", "ROUTE", "UNCLASSIFIED"]


@dataclass(frozen=True)
class Gap:
    """The innermost unsatisfied element under a failed step, labelled by layer.

    ``path`` runs from the top-level step down to the gap, through any
    ``module_ref`` nodes and referenced modules, so a gap inside a composed
    module is located where it actually is. ``absent`` holds the atoms under
    the gap that do not hold in the context; ``candidates`` lists their gene
    symbols and can be empty when an absent atom is a family selector whose
    members yield no unambiguous symbol, so read ``absent`` to tell whether
    anything is missing.
    """

    path: tuple[str, ...]
    layer: GapLayer
    absent: tuple[Atom, ...]
    #: True when ``layer`` came from compiler inference, not a declared ``variant_kind``.
    layer_inferred: bool = False
    #: True when some atom under a failed variant set holds, i.e. at least one
    #: alternative is partly present (for example a complex missing one subunit).
    partial: bool = False

    @property
    def step(self) -> str:
        """Return the id of the gap itself (the last element of ``path``)."""
        return self.path[-1]

    @property
    def candidates(self) -> list[str]:
        """Return the sorted gene symbols of the absent atoms."""
        return sorted({symbol for atom in self.absent for symbol in atom.gene_symbols})


#: Explanations for a gap where the activity is required but no known carrier was found.
REALIZER_HYPOTHESES = [
    "non-orthologous / unannotated enzyme fills this step (candidate to identify by sequence/structure)",
]
#: Explanations for a gap where none of the modelled routes is present.
ROUTE_HYPOTHESES = [
    "an alternative route not represented in the module is used",
]
#: Explanations that apply to any gap.
GENERAL_HYPOTHESES = [
    "the pathway is not cell-autonomous here: a required intermediate is supplied by another "
    "cell type / organ (inter-organ transport) or by cross-feeding",
    "the activity assertion is incorrect for this context",
]
#: Every explanation emitted for a gap in a context where the pathway is known active.
GAP_HYPOTHESES = REALIZER_HYPOTHESES + ROUTE_HYPOTHESES + GENERAL_HYPOTHESES


def gap_report(circuit: Circuit, holds: Predicate) -> list[Gap]:
    """Return the innermost gaps under each unsatisfied step, labelled by layer.

    The report descends through failed conjunctions (including ``module_ref``
    nodes and the modules they reference) and stops at the element that
    actually fails:

    * an atom, a step with a single listed carrier. Its gap is ``UNCLASSIFIED``:
      the structure cannot tell an undetected carrier from an unmodelled route;
    * a variant set none of whose alternatives holds, labelled by its kind
      (declared or inferred), or ``UNCLASSIFIED``.

    >>> doc = {"module": {"id": "m", "parts": [
    ...   {"node": {"id": "s1", "annotons": [{"id": "a",
    ...      "participant": {"gene": {"preferred_term": "A"}}}]}},
    ...   {"node": {"id": "s2", "variant_sets": [{"id": "vs", "variant_kind": "ROUTE",
    ...      "variants": [{"id": "b", "annotons": [{"id": "b",
    ...                     "participant": {"gene": {"preferred_term": "B"}}}]},
    ...                   {"id": "c", "annotons": [{"id": "c",
    ...                     "participant": {"gene": {"preferred_term": "C"}}}]}]}]}}]}}
    >>> [(g.path, g.layer, g.candidates) for g in gap_report(compile_module(doc), lambda a: False)]
    [(('s1', 'a'), 'UNCLASSIFIED', ['A']), (('s2', 'vs'), 'ROUTE', ['B', 'C'])]
    """
    gaps: list[Gap] = []
    for step in unsatisfied_steps(circuit, holds):
        gaps.extend(_gaps(step, holds, ()))
    return gaps


def _gaps(circuit: Circuit, holds: Predicate, path: tuple[str, ...]) -> list[Gap]:
    """Return the innermost gaps under an unsatisfied ``circuit`` (see :func:`gap_report`)."""
    here = (*path, step_id(circuit))
    if isinstance(circuit, Atom):
        return [Gap(here, "UNCLASSIFIED", (circuit,))]
    if isinstance(circuit, Or):
        atoms = list(dict.fromkeys(iter_atoms(circuit)))
        absent = tuple(a for a in atoms if not holds(a))
        layer: GapLayer = circuit.kind or "UNCLASSIFIED"
        return [Gap(here, layer, absent, circuit.kind_inferred, partial=len(absent) < len(atoms))]
    found: list[Gap] = []
    for child in circuit.children:
        if not is_satisfied(child, holds):
            found.extend(_gaps(child, holds, here))
    return found


def _gap_hypotheses(gap: Gap) -> list[str]:
    """Return the layer-specific explanations for one gap.

    Only a declared layer narrows the explanations. A single-carrier step, an
    unclassified set or an inferred REALIZER set keeps both readings (inference
    from the modelled alternatives says nothing about unmodelled routes), and a
    declared ROUTE set with a partly present alternative also keeps the
    undetected-carrier reading.
    """
    if gap.layer == "UNCLASSIFIED" or gap.layer_inferred:
        return REALIZER_HYPOTHESES + ROUTE_HYPOTHESES
    if gap.layer == "REALIZER":
        return REALIZER_HYPOTHESES
    return ROUTE_HYPOTHESES + (REALIZER_HYPOTHESES if gap.partial else [])


def _hypotheses(gaps: list[Gap]) -> list[str]:
    """Return the explanations that fit ``gaps``, in the order of :data:`GAP_HYPOTHESES`."""
    wanted = {h for gap in gaps for h in _gap_hypotheses(gap)} | set(GENERAL_HYPOTHESES)
    return [h for h in GAP_HYPOTHESES if h in wanted]


def _memoized(holds: Predicate) -> Predicate:
    """Wrap ``holds`` so each atom is evaluated once (oracles may be expensive)."""
    cache: dict[Atom, bool] = {}

    def cached(atom: Atom) -> bool:
        if atom not in cache:
            cache[atom] = holds(atom)
        return cache[atom]

    return cached


def abduce(circuit: Circuit, holds: Predicate, asserted_active: bool) -> Abduction:
    """Reconcile circuit satisfiability against an independent activity assertion.

    Four outcomes:

    * ``CONSISTENT_ACTIVE`` - satisfiable and asserted active (pathway explained).
    * ``CONSISTENT_INACTIVE`` - unsatisfiable and asserted inactive (correctly predicts
      the absence, e.g. a known auxotrophy).
    * ``ABDUCTION_TARGET`` - asserted active but unsatisfiable: a real gap to explain
      (novel enzyme / unmodelled route / wrong assertion).
    * ``OVERPREDICTION`` - satisfiable but asserted inactive: encoded yet not realised
      (regulation/expression off, or the assertion is wrong).

    >>> doc = {"module": {"id": "m", "parts": [
    ...   {"order": 1, "node": {"id": "s1", "annotons": [{"id": "a",
    ...      "participant": {"gene": {"preferred_term": "A"}}}]}}]}}
    >>> circ = compile_module(doc)
    >>> abduce(circ, lambda atom: False, asserted_active=True).classification
    'ABDUCTION_TARGET'
    >>> abduce(circ, lambda atom: False, asserted_active=False).classification
    'CONSISTENT_INACTIVE'
    """
    holds = _memoized(holds)
    sat = is_satisfied(circuit, holds)
    steps = unsatisfied_steps(circuit, holds)
    gap_ids = [step_id(s) for s in steps]
    gap_candidates = {
        step_id(s): sorted({symbol for a in iter_atoms(s) if not holds(a) for symbol in a.gene_symbols})
        for s in steps
    }
    gaps = gap_report(circuit, holds)
    if sat and asserted_active:
        return Abduction("CONSISTENT_ACTIVE", True, True, True, gap_ids, gap_candidates, [], gaps)
    if not sat and not asserted_active:
        return Abduction("CONSISTENT_INACTIVE", True, False, False, gap_ids, gap_candidates, [], gaps)
    if not sat and asserted_active:
        return Abduction("ABDUCTION_TARGET", False, True, False, gap_ids, gap_candidates,
                         _hypotheses(gaps), gaps)
    return Abduction("OVERPREDICTION", False, False, True, gap_ids, gap_candidates,
                     ["pathway encoded but asserted inactive: regulation/expression off, or the assertion is wrong"],
                     gaps)


def unsatisfied_steps(circuit: Circuit, holds: Predicate) -> list[Circuit]:
    """Top-level conjuncts (pathway steps) that are not satisfied under ``holds``.

    For a pathway compiled as an AND over its steps, these are the **gaps**: the
    steps for which no variant/candidate is present in the context. This is the
    GapMind "which required step is missing" diagnostic, expressed on the circuit.

    >>> doc = {"module": {"id": "m", "parts": [
    ...   {"order": 1, "node": {"id": "s1", "annotons": [{"id": "a",
    ...      "participant": {"gene": {"preferred_term": "A"}}}]}},
    ...   {"order": 2, "node": {"id": "s2", "annotons": [{"id": "b",
    ...      "participant": {"gene": {"preferred_term": "B"}}}]}}]}}
    >>> circ = compile_module(doc)
    >>> [step_id(s) for s in unsatisfied_steps(circ, lambda atom: atom.gene_symbol == "A")]
    ['s2']
    """
    if isinstance(circuit, And):
        return [c for c in circuit.children if not is_satisfied(c, holds)]
    return [] if is_satisfied(circuit, holds) else [circuit]
