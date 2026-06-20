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

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Optional, Union

import yaml

from ai_gene_review.render_modules import as_list


@dataclass(frozen=True)
class Atom:
    """A leaf step: a participant gene whose truth value comes from an oracle."""

    node_id: str
    label: str
    gene_symbol: Optional[str]
    uniprot: Optional[str]

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Atom({self.gene_symbol or self.node_id})"


@dataclass
class And:
    """Conjunction: satisfied iff every child is satisfied."""

    node_id: str
    children: list["Circuit"]


@dataclass
class Or:
    """Disjunction over variant branches (at-least-one for satisfiability)."""

    set_id: str
    selection: str
    children: list["Circuit"]


Circuit = Union[Atom, And, Or]

#: A per-context predicate: does this atom hold (e.g. is its gene expressed)?
Predicate = Callable[[Atom], bool]


def _symbol_from_gene(gene: dict) -> Optional[str]:
    """Pull a leading gene symbol out of a GeneDescriptor's ``preferred_term``.

    >>> _symbol_from_gene({"preferred_term": "PCK1 (cytosolic PEPCK)"})
    'PCK1'
    """
    pref = gene.get("preferred_term") if gene else None
    if not pref:
        return None
    return pref.split()[0].strip().rstrip(":")


def _uniprot_from_gene(gene: dict) -> Optional[str]:
    """Return the bare UniProt accession from a GeneDescriptor, if present."""
    term = (gene or {}).get("term") or {}
    tid = term.get("id", "")
    if tid.startswith("UniProtKB:"):
        return tid.split(":", 1)[1]
    return None


def _atom_from_annoton(annoton: dict) -> Atom:
    """Build an :class:`Atom` from an annoton dict."""
    gene = (annoton.get("participant") or {}).get("gene") or {}
    return Atom(
        node_id=annoton.get("id", "?"),
        label=annoton.get("label", annoton.get("id", "?")),
        gene_symbol=_symbol_from_gene(gene),
        uniprot=_uniprot_from_gene(gene),
    )


def compile_node(node: dict) -> And:
    """Compile a ModuleNode dict into an AND over its atoms, parts, and variant sets."""
    children: list[Circuit] = []
    for annoton in as_list(node.get("annotons")):
        children.append(_atom_from_annoton(annoton))
    for part in as_list(node.get("parts")):
        sub = compile_node(part["node"])
        if part.get("optional"):
            # An optional part is an OR of (filled, empty) -> always satisfiable.
            empty: Circuit = And(node_id="empty", children=[])
            children.append(Or(set_id=f"opt:{part['node'].get('id', '?')}",
                               selection="ZERO_OR_MORE", children=[sub, empty]))
        else:
            children.append(sub)
    for vs in as_list(node.get("variant_sets")):
        branches: list[Circuit] = [compile_node(v) for v in as_list(vs.get("variants"))]
        children.append(Or(set_id=vs.get("id", "?"),
                           selection=vs.get("selection", "ONE_OR_MORE"),
                           children=branches))
    return And(node_id=node.get("id", "?"), children=children)


def compile_module(doc: dict) -> And:
    """Compile a loaded ModuleReview document (its ``module``) into a circuit."""
    return compile_node(doc["module"])


def compile_module_file(path: Union[str, Path]) -> And:
    """Load a ModuleReview YAML file and compile its root module node."""
    return compile_module(yaml.safe_load(Path(path).read_text()))


def iter_atoms(circuit: Circuit) -> Iterator[Atom]:
    """Yield every :class:`Atom` in the circuit (depth-first)."""
    if isinstance(circuit, Atom):
        yield circuit
    else:
        for child in circuit.children:
            yield from iter_atoms(child)


def enumerate_routes(circuit: Circuit) -> list[list[Atom]]:
    """Enumerate minimal satisfying routes.

    Each route picks exactly one branch per :class:`Or` node and includes every
    atom on the conjunctive backbone. Returns one atom-list per route.
    """
    if isinstance(circuit, Atom):
        return [[circuit]]
    if isinstance(circuit, And):
        routes: list[list[Atom]] = [[]]
        for child in circuit.children:
            child_routes = enumerate_routes(child)
            routes = [r + cr for r in routes for cr in child_routes]
        return routes
    # Or
    routes = []
    for child in circuit.children:
        routes.extend(enumerate_routes(child))
    return routes or [[]]


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
    atoms whose absence gates the whole module.
    """
    routes = enumerate_routes(circuit)
    if not routes:
        return []
    common: set[str] = set(a.node_id for a in routes[0])
    for r in routes[1:]:
        common &= set(a.node_id for a in r)
    seen: dict[str, Atom] = {}
    for a in iter_atoms(circuit):
        if a.node_id in common:
            seen[a.node_id] = a
    return list(seen.values())
