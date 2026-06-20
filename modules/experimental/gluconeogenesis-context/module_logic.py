#!/usr/bin/env python
"""Compile a ``ModuleReview`` document into a boolean logic circuit.

A module is a monotone boolean formula over *step atoms*:

* a ``ModuleNode``'s ``parts`` and its own ``annotons`` are conjunctive  -> AND
* a ``variant_sets`` entry is disjunctive (at-least-one for satisfiability) -> OR
* a leaf ``annoton`` is an ATOM whose truth value, in this prototype, is
  "the participant gene is expressed in the context being evaluated"

This module only builds and reasons over the circuit (route enumeration,
per-context satisfiability, gate identification). The "is the atom satisfied"
predicate is supplied externally (e.g. by the GTEx oracle), so the logic layer
has no biological-data dependency and is fully unit-testable.

>>> circuit = compile_module_file("nonexistent")  # doctest: +SKIP
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterator, Optional

import yaml


def as_list(value) -> list:
    """Coerce a possibly-absent / possibly-scalar value into a list."""
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


@dataclass
class Atom:
    """A leaf step: a participant gene that may or may not be satisfied."""

    node_id: str
    label: str
    gene_symbol: Optional[str]
    uniprot: Optional[str]

    def __repr__(self) -> str:
        return f"Atom({self.gene_symbol or self.node_id})"


@dataclass
class And:
    """Conjunction: satisfied iff all children are satisfied."""

    node_id: str
    children: list = field(default_factory=list)


@dataclass
class Or:
    """Disjunction over variant branches (at-least-one for satisfiability)."""

    set_id: str
    selection: str
    children: list = field(default_factory=list)


Circuit = object  # Atom | And | Or


def _symbol_from_gene(gene: dict) -> Optional[str]:
    """Pull a HGNC-ish symbol out of a GeneDescriptor's preferred_term."""
    pref = gene.get("preferred_term") if gene else None
    if not pref:
        return None
    # preferred_term is authored as e.g. "PCK1 (cytosolic PEPCK)" -> "PCK1".
    return pref.split()[0].strip().rstrip(":")


def _uniprot_from_gene(gene: dict) -> Optional[str]:
    term = (gene or {}).get("term") or {}
    tid = term.get("id", "")
    if tid.startswith("UniProtKB:"):
        return tid.split(":", 1)[1]
    return None


def _atom_from_annoton(annoton: dict) -> Atom:
    participant = annoton.get("participant") or {}
    gene = participant.get("gene") or {}
    return Atom(
        node_id=annoton.get("id", "?"),
        label=annoton.get("label", annoton.get("id", "?")),
        gene_symbol=_symbol_from_gene(gene),
        uniprot=_uniprot_from_gene(gene),
    )


def compile_node(node: dict) -> And:
    """Compile a ModuleNode dict into an AND over its atoms, parts, and variant sets."""
    children: list = []
    for annoton in as_list(node.get("annotons")):
        children.append(_atom_from_annoton(annoton))
    for part in as_list(node.get("parts")):
        sub = compile_node(part["node"])
        if part.get("optional"):
            # optional part: an OR of (filled, empty) -> always satisfiable
            children.append(Or(set_id=f"opt:{part['node'].get('id','?')}",
                               selection="ZERO_OR_MORE", children=[sub, And("empty", [])]))
        else:
            children.append(sub)
    for vs in as_list(node.get("variant_sets")):
        branches = [compile_node(v) for v in as_list(vs.get("variants"))]
        children.append(Or(set_id=vs.get("id", "?"), selection=vs.get("selection", "ONE_OR_MORE"),
                           children=branches))
    return And(node_id=node.get("id", "?"), children=children)


def compile_module_file(path: str | Path) -> And:
    """Load a ModuleReview YAML file and compile its root module node."""
    data = yaml.safe_load(Path(path).read_text())
    return compile_node(data["module"])


def iter_atoms(circuit: Circuit) -> Iterator[Atom]:
    """Yield every Atom in the circuit."""
    if isinstance(circuit, Atom):
        yield circuit
    elif isinstance(circuit, (And, Or)):
        for c in circuit.children:
            yield from iter_atoms(c)


def enumerate_routes(circuit: Circuit) -> list[list[Atom]]:
    """Enumerate minimal satisfying routes.

    Each route picks exactly one branch per OR node and includes every atom on the
    conjunctive backbone. Returns a list of atom-lists (one per route).
    """
    if isinstance(circuit, Atom):
        return [[circuit]]
    if isinstance(circuit, And):
        routes: list[list[Atom]] = [[]]
        for child in circuit.children:
            child_routes = enumerate_routes(child)
            routes = [r + cr for r in routes for cr in child_routes]
        return routes
    if isinstance(circuit, Or):
        routes = []
        for child in circuit.children:
            routes.extend(enumerate_routes(child))
        return routes or [[]]
    raise TypeError(f"unknown circuit node: {circuit!r}")


def is_satisfied(circuit: Circuit, holds: Callable[[Atom], bool]) -> bool:
    """Evaluate the circuit given a per-atom truth predicate ``holds``."""
    if isinstance(circuit, Atom):
        return holds(circuit)
    if isinstance(circuit, And):
        return all(is_satisfied(c, holds) for c in circuit.children)
    if isinstance(circuit, Or):
        return any(is_satisfied(c, holds) for c in circuit.children) if circuit.children else True
    raise TypeError(f"unknown circuit node: {circuit!r}")


def core_atoms(circuit: Circuit) -> list[Atom]:
    """Atoms required by *every* route (the AND-core).

    If any core atom is unsatisfied, no route can succeed: these are the gate
    candidates.
    """
    routes = enumerate_routes(circuit)
    if not routes:
        return []
    common_ids = set(a.node_id for a in routes[0])
    for r in routes[1:]:
        common_ids &= set(a.node_id for a in r)
    seen: dict[str, Atom] = {}
    for a in iter_atoms(circuit):
        if a.node_id in common_ids:
            seen[a.node_id] = a
    return list(seen.values())


if __name__ == "__main__":
    import sys

    circ = compile_module_file(sys.argv[1])
    routes = enumerate_routes(circ)
    print(f"atoms: {sorted({a.gene_symbol for a in iter_atoms(circ) if a.gene_symbol})}")
    print(f"routes: {len(routes)}")
    for i, r in enumerate(routes, 1):
        print(f"  route {i}: {[a.gene_symbol for a in r if a.gene_symbol]}")
    print(f"AND-core (gate atoms): {[a.gene_symbol for a in core_atoms(circ)]}")
