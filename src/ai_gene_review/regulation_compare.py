#!/usr/bin/env python
"""Compare regulatory wiring across a curated module and a 3rd-party source.

A :class:`RegEdge` is the canonical, source-agnostic unit of regulation:
``(effector, enzyme, sign, mechanism)``. Curated modules and ingested models are
each reduced to a set of these, then diffed. This is the regulation-layer analogue
of the EC-discrepancy mining in the METABOLIC_MODEL_ANALYSIS project: instead of
comparing GO MF / EC, it compares *who regulates whom, with what sign and
mechanism* — the layer GO cannot express.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_gene_review.module_notation import (
    REGULATORY,
    mechanism_tag,
    build_registry,
    iter_connections,
)


_SIGN = {"POSITIVELY_REGULATES": "+", "NEGATIVELY_REGULATES": "-"}


@dataclass(frozen=True)
class RegEdge:
    """A single regulatory relationship, normalised across sources.

    >>> str(RegEdge("amet", "mat1", "-", "competitive"))
    'amet -| mat1 [competitive]'
    >>> str(RegEdge("amet", "mat3", "+", "allosteric"))
    'amet -o mat3 [allosteric]'
    """

    effector: str
    enzyme: str
    sign: str  # "+" (activates) or "-" (inhibits)
    mechanism: str  # "allosteric" | "competitive" | "unspecified" | ...

    @property
    def key(self) -> tuple[str, str]:
        """The (effector, enzyme) pair the edge is keyed on for diffing."""
        return (self.effector, self.enzyme)

    def __str__(self) -> str:
        arrow = "-o" if self.sign == "+" else "-|"
        return f"{self.effector} {arrow} {self.enzyme} [{self.mechanism}]"


def module_regulatory_edges(data: dict[str, Any]) -> set[RegEdge]:
    """Extract regulatory edges from a curated module YAML document.

    Symbols match the module-notation projection (so the edges are human-readable
    and align with an ingested source mapped to the same symbols).
    """
    module = data.get("module")
    if not isinstance(module, dict):
        return set()
    registry = build_registry(data)
    edges: set[RegEdge] = set()
    for connection in iter_connections(module):
        ctype = connection.get("connection_type")
        if ctype not in REGULATORY:
            continue
        edges.add(
            RegEdge(
                effector=registry.symbol_for(connection.get("source")),
                enzyme=registry.symbol_for(connection.get("target")),
                sign=_SIGN[ctype],
                mechanism=mechanism_tag(connection.get("predicate")) or "unspecified",
            )
        )
    return edges


@dataclass
class EdgeDiff:
    """The result of comparing a ``left`` (curated) and ``right`` (source) edge set."""

    agreements: list[RegEdge] = field(default_factory=list)
    only_in_left: list[RegEdge] = field(default_factory=list)
    only_in_right: list[RegEdge] = field(default_factory=list)
    sign_conflicts: list[tuple[RegEdge, RegEdge]] = field(default_factory=list)
    mechanism_conflicts: list[tuple[RegEdge, RegEdge]] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        """True when the two sources fully agree on the regulatory wiring."""
        return not (
            self.only_in_left
            or self.only_in_right
            or self.sign_conflicts
            or self.mechanism_conflicts
        )


def diff_edges(left: set[RegEdge], right: set[RegEdge]) -> EdgeDiff:
    """Diff two regulatory-edge sets, keyed on (effector, enzyme).

    ``left`` is treated as the curated reference and ``right`` as the ingested
    source. Same key with differing sign is a ``sign_conflict``; same key and sign
    with differing mechanism is a ``mechanism_conflict``.
    """
    left_by_key = {edge.key: edge for edge in left}
    right_by_key = {edge.key: edge for edge in right}
    diff = EdgeDiff()
    for key, left_edge in sorted(left_by_key.items()):
        right_edge = right_by_key.get(key)
        if right_edge is None:
            diff.only_in_left.append(left_edge)
        elif left_edge.sign != right_edge.sign:
            diff.sign_conflicts.append((left_edge, right_edge))
        elif left_edge.mechanism != right_edge.mechanism:
            diff.mechanism_conflicts.append((left_edge, right_edge))
        else:
            diff.agreements.append(left_edge)
    for key, right_edge in sorted(right_by_key.items()):
        if key not in left_by_key:
            diff.only_in_right.append(right_edge)
    return diff


def format_edge_diff(diff: EdgeDiff, left_label: str, right_label: str) -> str:
    """Render an :class:`EdgeDiff` as a readable report."""
    lines = [f"# Regulation diff: {left_label} (curated) vs {right_label} (source)", ""]
    lines.append(
        f"agree={len(diff.agreements)}  "
        f"curated_only={len(diff.only_in_left)}  "
        f"source_only={len(diff.only_in_right)}  "
        f"sign_conflicts={len(diff.sign_conflicts)}  "
        f"mechanism_conflicts={len(diff.mechanism_conflicts)}"
    )
    if diff.is_clean:
        lines.append(
            "\n✓ full agreement — curated module matches the source regulatory wiring."
        )
    for left_edge, right_edge in diff.sign_conflicts:
        lines.append(f"\n✗ SIGN  {left_edge}   (curated)  vs   {right_edge}   (source)")
    for left_edge, right_edge in diff.mechanism_conflicts:
        lines.append(f"\n~ MECH  {left_edge}   (curated)  vs   {right_edge}   (source)")
    for edge in diff.only_in_left:
        lines.append(f"\n- curated-only   {edge}")
    for edge in diff.only_in_right:
        lines.append(f"\n+ source-only    {edge}")
    return "\n".join(lines) + "\n"
