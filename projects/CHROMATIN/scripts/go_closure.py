"""Minimal is_a/part_of closure over an OBO file, shared by the CHROMATIN analyses.

Reads only [Term] stanzas: names, alt_ids, is_a and part_of edges. Intended for
go-basic.obo, whose is_a/part_of graph is already reasoned.
"""

from __future__ import annotations

import collections
from dataclasses import dataclass, field
from typing import Dict, Set


@dataclass
class Graph:
    """Parent links (is_a + part_of), names and alt_id -> primary id map."""

    parents: Dict[str, Set[str]] = field(default_factory=lambda: collections.defaultdict(set))
    names: Dict[str, str] = field(default_factory=dict)
    alt: Dict[str, str] = field(default_factory=dict)

    def primary(self, curie: str) -> str:
        """Map an alt_id to its primary id; other ids pass through unchanged."""
        return self.alt.get(curie, curie)

    def ancestors(self, curie: str, parents: Dict[str, Set[str]] | None = None) -> Set[str]:
        """Reflexive ancestor set over is_a/part_of, optionally over an edited edge map."""
        edges = self.parents if parents is None else parents
        seen = {curie}
        stack = [curie]
        while stack:
            for parent in edges.get(stack.pop(), ()):
                if parent not in seen:
                    seen.add(parent)
                    stack.append(parent)
        return seen


def load(path: str) -> Graph:
    """Parse the term stanzas of an OBO file into a Graph."""
    graph = Graph()
    current: str | None = None
    in_term = False
    with open(path) as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line.startswith("["):
                in_term = line == "[Term]"
                current = None
                continue
            if not in_term:
                continue
            if line.startswith("id: "):
                current = line[4:]
            elif current is None:
                continue
            elif line.startswith("name: "):
                graph.names[current] = line[6:]
            elif line.startswith("alt_id: "):
                graph.alt[line[8:]] = current
            elif line.startswith("is_a: "):
                graph.parents[current].add(line.split()[1])
            elif line.startswith("relationship: part_of "):
                graph.parents[current].add(line.split()[2])
    return graph
