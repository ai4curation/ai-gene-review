#!/usr/bin/env python
"""Project a module YAML document into a compact, human-readable notation.

This is a *read-only* projection (a view), not a second source of truth: the
module YAML (and GO-CAM YAML) remains canonical and machine-checkable, while this
notation gives a scannable ``symbol -> symbol`` rendering plus a legend mapping
each symbol to its grounded entity.

The notation has three blocks, mirroring the layers we care about:

* **Legend** - ``symbol := GROUNDING  label`` for enzymes (GO MF), grounded
  metabolite effector pools (ChEBI), and the pathway (GO BP).
* **Reactions** - ``enzyme: substrates -> products    # GO id``.
* **Regulation** - ``effector -o|-| enzyme   [mechanism]   # SBO id`` where the
  arrow encodes sign (``-o`` activation, ``-|`` inhibition, borrowed from
  Antimony) and the bracketed tag encodes the *mechanism* (competitive vs
  allosteric) grounded to SBO - the distinction GO cannot express.

Symbols are derived from the document-scoped element ids (a known suffix such as
``_activity``/``_pool``/``_step`` is stripped), so the projection stays faithful
to - and loosely reversible against - the YAML.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, Optional

import yaml

from ai_gene_review.render_modules import as_list


# Connection types that represent regulation (the layer GO cannot express).
_REGULATORY = {"POSITIVELY_REGULATES": "-o", "NEGATIVELY_REGULATES": "-|"}

# Suffixes stripped from element ids to make short, readable symbols.
_SUFFIXES = ("_activity", "_pool", "_step", "_route", "_form", "_node", "_pathway")


@dataclass
class _Symbol:
    """A resolved symbol for one document-scoped module element."""

    element_id: str
    symbol: str
    kind: str  # "activity" | "metabolite" | "pathway" | "step"
    term_id: Optional[str] = None
    term_label: Optional[str] = None
    preferred_label: Optional[str] = None
    function: Optional[dict[str, Any]] = None


@dataclass
class _Registry:
    """Lookup tables built from one module document."""

    by_id: dict[str, _Symbol] = field(default_factory=dict)
    metabolite_alias: dict[str, str] = field(default_factory=dict)

    def symbol_for(self, element_id: Any) -> str:
        """Return the short symbol for an id, falling back to the raw id."""
        if element_id is None:
            return "?"
        entry = self.by_id.get(str(element_id))
        return entry.symbol if entry else str(element_id)


def _base_symbol(element_id: str) -> str:
    """Strip a known trailing role suffix to make a short symbol.

    >>> _base_symbol("mat1_activity")
    'mat1'
    >>> _base_symbol("amet_pool")
    'amet'
    >>> _base_symbol("plain")
    'plain'
    """
    for suffix in _SUFFIXES:
        if element_id.endswith(suffix) and len(element_id) > len(suffix):
            return element_id[: -len(suffix)]
    return element_id


def _term(holder: Any) -> dict[str, Any]:
    """Return the ``term`` mapping of a descriptor-like holder, or empty."""
    if isinstance(holder, dict) and isinstance(holder.get("term"), dict):
        return holder["term"]
    return {}


def iter_nodes(node: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Yield a node and all descendant nodes (parts and variants)."""
    yield node
    for part in as_list(node.get("parts")):
        child = part.get("node") if isinstance(part, dict) else None
        if isinstance(child, dict):
            yield from iter_nodes(child)
    for variant_set in as_list(node.get("variant_sets")):
        if not isinstance(variant_set, dict):
            continue
        for variant in as_list(variant_set.get("variants")):
            if isinstance(variant, dict):
                yield from iter_nodes(variant)


def _node_concept(node: dict[str, Any]) -> dict[str, Any]:
    """Return the first concept descriptor of a node, or empty."""
    for concept in as_list(node.get("concepts")):
        if isinstance(concept, dict):
            return concept
    return {}


def _is_metabolite_pool(node: dict[str, Any]) -> bool:
    """A node that is an effector/metabolite pool.

    True if it grounds to ChEBI, or its id is a ``*_pool`` leaf carrying a concept
    but no catalytic annotons/children (so ungrounded effectors still appear in
    the legend and alias map).
    """
    concept = _node_concept(node)
    if str(_term(concept).get("id", "")).startswith("CHEBI:"):
        return True
    is_leaf = (
        not as_list(node.get("annotons"))
        and not as_list(node.get("parts"))
        and not as_list(node.get("variant_sets"))
    )
    return bool(str(node.get("id", "")).endswith("_pool") and concept and is_leaf)


def build_registry(data: dict[str, Any]) -> _Registry:
    """Build symbol lookup tables for a module document.

    Symbols are assigned with priority so that the *interesting* lines (reactions
    and regulation) get clean short symbols: enzymes (annotons) and metabolite
    pools are assigned first; container/step nodes take what is left, reusing a
    single contained annoton's symbol where possible.
    """
    module = data.get("module")
    if not isinstance(module, dict):
        return _Registry()

    registry = _Registry()
    used: set[str] = set()

    def claim(preferred: str, element_id: str) -> str:
        symbol = preferred
        n = 2
        while symbol in used:
            symbol = f"{preferred}{n}"
            n += 1
        used.add(symbol)
        return symbol

    # Pass 1: enzymes (annotons with a function) and metabolite pools.
    for node in iter_nodes(module):
        for annoton in as_list(node.get("annotons")):
            if not isinstance(annoton, dict) or not annoton.get("id"):
                continue
            function = (
                annoton.get("function")
                if isinstance(annoton.get("function"), dict)
                else None
            )
            term = _term(function)
            element_id = str(annoton["id"])
            symbol = claim(_base_symbol(element_id), element_id)
            registry.by_id[element_id] = _Symbol(
                element_id=element_id,
                symbol=symbol,
                kind="activity",
                term_id=term.get("id"),
                term_label=term.get("label"),
                preferred_label=(function or {}).get("preferred_term"),
                function=function,
            )

    for node in iter_nodes(module):
        if not node.get("id") or not _is_metabolite_pool(node):
            continue
        concept = _node_concept(node)
        term = _term(concept)
        element_id = str(node["id"])
        symbol = claim(_base_symbol(element_id), element_id)
        registry.by_id[element_id] = _Symbol(
            element_id=element_id,
            symbol=symbol,
            kind="metabolite",
            term_id=term.get("id"),
            term_label=term.get("label"),
            preferred_label=concept.get("preferred_term"),
        )
        # Alias map so reaction substrates/products render with the same symbol.
        for key in (term.get("id"), concept.get("preferred_term"), term.get("label")):
            if key:
                registry.metabolite_alias.setdefault(_norm(str(key)), symbol)

    # Pass 2: remaining nodes (pathway + container/step nodes).
    module_id = str(module.get("id"))
    for node in iter_nodes(module):
        raw_id = node.get("id")
        if not raw_id or str(raw_id) in registry.by_id:
            continue
        element_id = str(raw_id)
        annotons = [
            a
            for a in as_list(node.get("annotons"))
            if isinstance(a, dict) and a.get("id")
        ]
        no_children = not as_list(node.get("parts")) and not as_list(
            node.get("variant_sets")
        )
        if len(annotons) == 1 and no_children:
            # A thin wrapper around a single activity: reuse the activity symbol.
            inner = registry.by_id.get(str(annotons[0]["id"]))
            if inner:
                registry.by_id[element_id] = _Symbol(
                    element_id=element_id, symbol=inner.symbol, kind="step"
                )
                continue
        kind = "pathway" if element_id == module_id else "step"
        concept = _node_concept(node)
        term = _term(concept)
        symbol = claim(_base_symbol(element_id), element_id)
        registry.by_id[element_id] = _Symbol(
            element_id=element_id,
            symbol=symbol,
            kind=kind,
            term_id=term.get("id"),
            term_label=term.get("label"),
            preferred_label=concept.get("preferred_term"),
        )

    return registry


def _norm(text: str) -> str:
    """Normalise a metabolite name for alias matching."""
    return " ".join(text.lower().split())


def _render_descriptor_list(descriptors: Any, registry: _Registry) -> str:
    """Render substrates/products, substituting pool symbols where grounded."""
    parts: list[str] = []
    for descriptor in as_list(descriptors):
        if not isinstance(descriptor, dict):
            continue
        term = _term(descriptor)
        alias = None
        for key in (
            term.get("id"),
            descriptor.get("preferred_term"),
            term.get("label"),
        ):
            if key and _norm(str(key)) in registry.metabolite_alias:
                alias = registry.metabolite_alias[_norm(str(key))]
                break
        parts.append(
            alias or descriptor.get("preferred_term") or term.get("label") or "?"
        )
    return " + ".join(parts)


def _mechanism_tag(predicate: Any) -> Optional[str]:
    """Extract a short mechanism tag (e.g. ``competitive``) from a predicate."""
    if not isinstance(predicate, dict):
        return None
    text = _norm(
        str(predicate.get("preferred_term") or _term(predicate).get("label") or "")
    )
    for tag in (
        "competitive",
        "allosteric",
        "non-competitive",
        "uncompetitive",
        "mixed",
    ):
        if tag in text:
            return tag
    return text or None


def iter_connections(module: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Yield every connection declared anywhere in the module tree."""
    for node in iter_nodes(module):
        for connection in as_list(node.get("connections")):
            if isinstance(connection, dict):
                yield connection


def render_module_notation(data: dict[str, Any]) -> str:
    """Render a module YAML document (as a dict) into the compact notation.

    Returns the notation as a single string. This is a faithful projection of the
    canonical YAML; it does not validate and is not parsed back.
    """
    module = data.get("module")
    if not isinstance(module, dict):
        raise ValueError("module document is missing a top-level 'module' mapping")

    registry = build_registry(data)
    title = data.get("title") or module.get("label") or module.get("id") or "module"

    lines: list[str] = [f"# {title}", ""]

    # ---- Legend -------------------------------------------------------------
    lines.append("# ── Legend (symbol := grounding) ──")

    def legend_line(symbol: str, term_id: Optional[str], label: str) -> str:
        grounding = f"{term_id}  " if term_id else ""
        return f"{symbol} := {grounding}{label}".rstrip()

    pathway = registry.by_id.get(str(module.get("id")))
    if pathway and (pathway.term_id or pathway.preferred_label):
        lines.append(
            legend_line(
                "pathway",
                pathway.term_id,
                pathway.preferred_label or pathway.term_label or "",
            )
        )

    enzymes = [s for s in registry.by_id.values() if s.kind == "activity"]
    metabolites = [s for s in registry.by_id.values() if s.kind == "metabolite"]
    for sym in sorted(enzymes, key=lambda s: s.symbol):
        lines.append(
            legend_line(
                sym.symbol, sym.term_id, sym.preferred_label or sym.term_label or ""
            )
        )
    for sym in sorted(metabolites, key=lambda s: s.symbol):
        lines.append(
            legend_line(
                sym.symbol, sym.term_id, sym.preferred_label or sym.term_label or ""
            )
        )

    # ---- Reactions ----------------------------------------------------------
    reaction_lines: list[str] = []
    for sym in enzymes:
        function = sym.function or {}
        substrates = _render_descriptor_list(function.get("substrates"), registry)
        products = _render_descriptor_list(function.get("products"), registry)
        if not substrates and not products:
            continue
        comment = f"   # {sym.term_id}" if sym.term_id else ""
        reaction_lines.append(f"{sym.symbol}: {substrates} -> {products}{comment}")
    if reaction_lines:
        lines.extend(["", "# ── Reactions (enzyme: substrates -> products) ──"])
        lines.extend(reaction_lines)

    # ---- Regulation ---------------------------------------------------------
    regulation_lines: list[str] = []
    flow_lines: list[str] = []
    for connection in iter_connections(module):
        ctype = connection.get("connection_type")
        source = registry.symbol_for(connection.get("source"))
        target = registry.symbol_for(connection.get("target"))
        if ctype in _REGULATORY:
            arrow = _REGULATORY[ctype]
            mechanism = _mechanism_tag(connection.get("predicate"))
            sbo = _term(connection.get("predicate")).get("id")
            tag = f"   [{mechanism}]" if mechanism else ""
            comment = f"   # {sbo}" if sbo else ""
            regulation_lines.append(f"{source} {arrow} {target}{tag}{comment}")
        else:
            flow_lines.append(f"{source} -> {target}   # {ctype}")
    if regulation_lines:
        lines.extend(["", "# ── Regulation (effector -o|-| enzyme [mechanism]) ──"])
        lines.extend(regulation_lines)
    if flow_lines:
        lines.extend(["", "# ── Flow (topology) ──"])
        lines.extend(flow_lines)

    return "\n".join(lines) + "\n"


def render_module_notation_file(yaml_path: Path) -> str:
    """Load a module YAML file and render its notation."""
    data = yaml.safe_load(Path(yaml_path).read_text())
    if not isinstance(data, dict):
        raise ValueError(f"Module YAML must contain a mapping: {yaml_path}")
    return render_module_notation(data)
