#!/usr/bin/env python
"""Translate a module document into a Boolean network, and calibrate its wiring.

:mod:`ai_gene_review.module_logic` reads a :class:`ModuleReview` document as a
*static, monotone* formula over steps (is the pathway wired up in this context?).
This module reads the same document as a *dynamic* system: the ``connections``
graph becomes a Boolean network in which every connection endpoint is a variable
and each variable's update rule is derived from the sign of its incoming edges.

Translation semantics
---------------------

* **Variables** are the elements (nodes or annotons) that appear as connection
  endpoints. Container nodes are *flattened*: an edge into a container activates
  the container's **entry** elements (children with no incoming internal
  activating edge, excluding pure inhibitors such as a GAP tier), and an edge out
  of a container originates from its **exit** elements (children with no outgoing
  internal activating edge, so a feedback inhibition from the last tier does not
  hide it). A node with no internal connections is atomic.
* **Sign**: ``CAUSES``, ``PRECEDES``, ``PROVIDES_INPUT_FOR``, ``HAS_INPUT``,
  ``HAS_OUTPUT`` and ``POSITIVELY_REGULATES`` are activating; ``NEGATIVELY_REGULATES``
  is inhibiting; ``PART_OF`` is structural and ignored.
* **Default update rule** follows the CaSQ convention (PMID:32403123 - "OR'ing
  the activators and AND'ing the NEGation of all inhibitors"):
  ``target = (a1 | a2 | ...) & !(i1 | i2 | ...)``. A variable with inhibitors only
  is constitutive unless inhibited. A variable with no incoming edge is an
  **input**.
* Rules can be overridden per variable (``logic`` argument), which prototypes the
  proposed ``update_rule`` slot on a module node, and inputs can be fixed to
  constants to define a simulation scenario.

Example: a three-tier relay with one inhibitor of the last tier.

>>> doc = {"module": {"id": "m", "parts": [
...   {"node": {"id": "a"}}, {"node": {"id": "b"}}, {"node": {"id": "c"}},
...   {"node": {"id": "phos"}}],
...   "connections": [
...     {"source": "a", "target": "b", "connection_type": "CAUSES"},
...     {"source": "b", "target": "c", "connection_type": "CAUSES"},
...     {"source": "phos", "target": "c", "connection_type": "NEGATIVELY_REGULATES"}]}}
>>> bn = module_to_boolean(doc)
>>> bn.inputs
['a', 'phos']
>>> bn.rules["c"]
'b & !phos'
>>> print(bn.to_bnet())
targets, factors
a, a
b, a
c, b & !phos
phos, phos
>>> sorted(str(e) for e in bn.edges)
['a -> b', 'b -> c', 'phos -| c']

The same signed-edge vocabulary is used to ingest an external Boolean network
(``.bnet``) or a SIGNOR pathway export, so a curated module and a published model
can be diffed edge-by-edge through a reviewed id-mapping.
"""

from __future__ import annotations

import csv
import itertools
import re
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator, Optional, Union

import yaml

from ai_gene_review.render_modules import as_list
from ai_gene_review.module_notation import iter_connections, iter_nodes


ACTIVATING = {
    "CAUSES",
    "PRECEDES",
    "PROVIDES_INPUT_FOR",
    "HAS_INPUT",
    "HAS_OUTPUT",
    "POSITIVELY_REGULATES",
}
INHIBITING = {"NEGATIVELY_REGULATES"}
STRUCTURAL = {"PART_OF"}


# --------------------------------------------------------------------------
# Signed edges
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class SignedEdge:
    """A signed regulatory/causal edge between two variables.

    >>> str(SignedEdge("ras", "raf", "+"))
    'ras -> raf'
    >>> str(SignedEdge("dusp", "erk", "-"))
    'dusp -| erk'
    """

    source: str
    target: str
    sign: str  # "+" | "-" | "?" (non-monotone / unknown)

    def __str__(self) -> str:
        arrow = {"+": "->", "-": "-|"}.get(self.sign, "-?")
        return f"{self.source} {arrow} {self.target}"


def _sign_of(connection_type: Optional[str]) -> Optional[str]:
    if connection_type in ACTIVATING:
        return "+"
    if connection_type in INHIBITING:
        return "-"
    return None


# --------------------------------------------------------------------------
# Module -> Boolean network
# --------------------------------------------------------------------------


@dataclass
class BooleanModel:
    """A Boolean network derived from a module (or parsed from a ``.bnet``)."""

    variables: list[str]
    rules: dict[str, str]
    edges: set[SignedEdge] = field(default_factory=set)
    source: Optional[str] = None

    @property
    def inputs(self) -> list[str]:
        """Variables with no update rule (no incoming edge)."""
        return [v for v in self.variables if v not in self.rules]

    def regulators(self, variable: str) -> list[str]:
        return sorted({e.source for e in self.edges if e.target == variable})

    def with_logic(self, logic: dict[str, str]) -> "BooleanModel":
        """Return a copy with per-variable rule overrides applied.

        Overrides prototype the proposed ``update_rule`` module slot: the expression
        replaces the default (OR-activators AND-NOT-inhibitors) rule. Variables
        named in an override are added if new; edges are re-derived from the
        expression's identifiers (sign ``?`` when not otherwise known).
        """
        rules = dict(self.rules)
        variables = list(self.variables)
        edges = set(self.edges)
        for var, expr in logic.items():
            if var not in variables:
                variables.append(var)
            rules[var] = expr
            edges = {e for e in edges if e.target != var}
            for reg in _identifiers(expr):
                if (
                    reg not in variables
                ):  # declare every referenced symbol, as parse_bnet does
                    variables.append(reg)
                sign = _monotone_sign(expr, reg)
                if sign == "0":  # not essential: no edge, matching parse_bnet
                    continue
                edges.add(SignedEdge(reg, var, sign))
        return BooleanModel(variables, rules, edges, self.source)

    def as_inputs(self, *names: str) -> "BooleanModel":
        """Return a copy in which ``names`` have no rule (free inputs).

        Their incoming edges are dropped too, so the regulatory graph and the
        rules stay consistent. Used to build counterfactuals ("what if this
        induced step were an external input, as the module once modelled it").

        >>> bn = parse_bnet("targets, factors\\na, a\\nb, a\\nc, b")
        >>> bn.as_inputs("b").inputs, sorted(map(str, bn.as_inputs("b").edges))
        (['a', 'b'], ['b -> c'])
        """
        rules = {k: v for k, v in self.rules.items() if k not in names}
        edges = {e for e in self.edges if e.target not in names}
        return BooleanModel(list(self.variables), rules, edges, self.source)

    def with_inputs(self, scenario: dict[str, bool]) -> "BooleanModel":
        """Return a copy with the given variables fixed to constants (a scenario).

        Constants are written as ``1``/``0``, which BoolNet, PyBoolNet and
        biodivine-aeon all read. Fixing a regulated variable (not only an input)
        is allowed and means a knock-in/knock-out of that step.
        """
        rules = dict(self.rules)
        for var, value in scenario.items():
            if var not in self.variables:
                raise KeyError(f"unknown variable {var!r}")
            rules[var] = "1" if value else "0"
        return BooleanModel(list(self.variables), rules, set(self.edges), self.source)

    def to_bnet(self, input_mode: str = "identity") -> str:
        """Serialise in BoolNet ``.bnet`` format.

        ``input_mode`` is ``identity`` (``x, x`` - the BoolNet convention, read by
        every tool) or ``free`` (inputs omitted; biodivine-aeon reads them as
        free parameters).
        """
        lines = ["targets, factors"]
        for var in self.variables:
            if var in self.rules:
                lines.append(f"{var}, {self.rules[var]}")
            elif input_mode == "identity":
                lines.append(f"{var}, {var}")
        return "\n".join(lines)


def _element_index(module: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Map every node and annoton id in the tree to its dict."""
    index: dict[str, dict[str, Any]] = {}
    for node in iter_nodes(module):
        nid = node.get("id")
        if nid:
            index[str(nid)] = node
        for annoton in as_list(node.get("annotons")):
            aid = annoton.get("id") if isinstance(annoton, dict) else None
            if aid:
                index[str(aid)] = annoton
    return index


def _children(node: dict[str, Any]) -> list[str]:
    """Direct child element ids of a node: part nodes, variant nodes, annotons."""
    ids: list[str] = []
    for part in as_list(node.get("parts")):
        child = part.get("node") if isinstance(part, dict) else None
        if isinstance(child, dict) and child.get("id"):
            ids.append(str(child["id"]))
    for vs in as_list(node.get("variant_sets")):
        if not isinstance(vs, dict):
            continue
        for variant in as_list(vs.get("variants")):
            if isinstance(variant, dict) and variant.get("id"):
                ids.append(str(variant["id"]))
    for annoton in as_list(node.get("annotons")):
        if isinstance(annoton, dict) and annoton.get("id"):
            ids.append(str(annoton["id"]))
    return ids


def _descendant_map(module: dict[str, Any]) -> dict[str, str]:
    """Map every element id to its direct parent node id."""
    parent: dict[str, str] = {}
    for node in iter_nodes(module):
        nid = str(node.get("id"))
        for child in _children(node):
            parent[child] = nid
    return parent


class _Flattener:
    """Resolve hierarchical connection endpoints to atomic variables."""

    def __init__(self, module: dict[str, Any]):
        self.module = module
        self.index = _element_index(module)
        self.parent = _descendant_map(module)
        self.connections = list(iter_connections(module))

    def _ancestor_child(self, element: str, container: str) -> Optional[str]:
        """The direct child of ``container`` that contains ``element`` (or is it)."""
        current: Optional[str] = element
        while current is not None:
            if self.parent.get(current) == container:
                return current
            current = self.parent.get(current)
        return None

    def _internal_edges(self, container: str) -> list[tuple[str, str, str]]:
        """Edges between direct children of ``container`` (resolved to children)."""
        out: list[tuple[str, str, str]] = []
        for conn in self.connections:
            sign = _sign_of(conn.get("connection_type"))
            if sign is None:
                continue
            s = self._ancestor_child(str(conn.get("source")), container)
            t = self._ancestor_child(str(conn.get("target")), container)
            if s is not None and t is not None and s != t:
                out.append((s, t, sign))
        return out

    def _endpoints(self) -> set[str]:
        return {str(c.get("source")) for c in self.connections} | {
            str(c.get("target")) for c in self.connections
        }

    def _descendants(
        self, element: str, _path: frozenset[str] = frozenset()
    ) -> set[str]:
        """All element ids below ``element``.

        The guard is per path: only a genuine cycle (an element that contains
        itself) raises. An id reachable from two sibling branches (a diamond, or a
        duplicated id) is merely collected once.
        """
        if element in _path:
            raise ValueError(f"cyclic module tree at {element!r}")
        node = self.index.get(element)
        out: set[str] = set()
        if node is None:
            return out
        for child in _children(node):
            out.add(child)
            out |= self._descendants(child, _path | {element})
        return out

    def _is_atomic(self, element: str) -> bool:
        node = self.index.get(element)
        if node is None:
            return True  # unknown id: treat as an opaque variable
        children = _children(node)
        if not children or "participant" in node:  # annoton or leaf node
            return True
        if self._internal_edges(element):
            return False
        # A container with no internal wiring is normally one lumped step. But if
        # any of its descendants is itself a connection endpoint, the container and
        # the child would both become variables (the child twice over), so the
        # container is expanded to its children instead.
        return not (self._descendants(element) & self._endpoints())

    def _unwired_children(self, element: str) -> Optional[list[str]]:
        """Children of a non-atomic container that has no internal edges, else None."""
        node = self.index[element]
        if self._internal_edges(element):
            return None
        return _children(node)

    def entries(self, element: str) -> list[str]:
        if self._is_atomic(element):
            return [element]
        unwired = self._unwired_children(element)
        if unwired is not None:
            return [x for child in unwired for x in self.entries(child)]
        node = self.index[element]
        children = _children(node)
        internal = self._internal_edges(element)
        incoming_act = {t for (_, t, sign) in internal if sign == "+"}
        outgoing: dict[str, set[str]] = {}
        for s, _, sign in internal:
            outgoing.setdefault(s, set()).add(sign)
        result: list[str] = []
        for child in children:
            if child in incoming_act:
                continue
            signs = outgoing.get(child, set())
            if signs and signs == {"-"}:
                continue  # a pure inhibitor tier (e.g. a GAP) is not an entry
            result.extend(self.entries(child))
        return result or [element]

    def exits(self, element: str) -> list[str]:
        if self._is_atomic(element):
            return [element]
        unwired = self._unwired_children(element)
        if unwired is not None:
            return [x for child in unwired for x in self.exits(child)]
        node = self.index[element]
        children = _children(node)
        internal = self._internal_edges(element)
        # Only forward (activating) internal edges disqualify an exit: a feedback
        # inhibition from the last tier back onto an earlier tier must not hide it.
        # A pure inhibitor tier (only inhibiting edges out, nothing in - e.g. a GAP)
        # is not an exit either; it is a side input of the bundle.
        with_outgoing_act = {s for (s, _, sign) in internal if sign == "+"}
        incoming_act = {t for (_, t, sign) in internal if sign == "+"}
        outgoing_inh = {s for (s, _, sign) in internal if sign == "-"}
        result: list[str] = []
        for child in children:
            if child in with_outgoing_act:
                continue
            if child in outgoing_inh and child not in incoming_act:
                continue
            result.extend(self.exits(child))
        return result or [element]

    def flat_edges(self) -> set[SignedEdge]:
        edges: set[SignedEdge] = set()
        for conn in self.connections:
            sign = _sign_of(conn.get("connection_type"))
            if sign is None:
                continue
            for s in self.exits(str(conn.get("source"))):
                for t in self.entries(str(conn.get("target"))):
                    if s != t:
                        edges.add(SignedEdge(s, t, sign))
        return edges


def _default_rule(activators: list[str], inhibitors: list[str]) -> str:
    """CaSQ-style default: OR of activators AND NOT (OR of inhibitors).

    >>> _default_rule(["a", "b"], ["i"])
    '(a | b) & !i'
    >>> _default_rule(["a"], [])
    'a'
    >>> _default_rule([], ["i", "j"])
    '!(i | j)'
    """
    act = " | ".join(activators)
    inh = " | ".join(inhibitors)
    if len(activators) > 1:
        act = f"({act})"
    if len(inhibitors) > 1:
        inh = f"({inh})"
    if activators and inhibitors:
        return f"{act} & !{inh}"
    if activators:
        return act
    return f"!{inh}"


def module_to_boolean(
    doc: dict[str, Any], logic: Optional[dict[str, str]] = None
) -> BooleanModel:
    """Compile a loaded :class:`ModuleReview` document into a :class:`BooleanModel`."""
    module = doc.get("module")
    if not isinstance(module, dict):
        raise ValueError("module document is missing a top-level 'module' mapping")
    flat = _Flattener(module)
    edges = flat.flat_edges()
    # Preserve document order for variables.
    order: list[str] = []
    for node in iter_nodes(module):
        nid = node.get("id")
        if nid:
            order.append(str(nid))
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                order.append(str(annoton["id"]))
    involved = {e.source for e in edges} | {e.target for e in edges}
    variables = [v for v in order if v in involved]
    variables += sorted(v for v in involved if v not in variables)
    rules: dict[str, str] = {}
    for var in variables:
        activators = sorted(
            {e.source for e in edges if e.target == var and e.sign == "+"}
        )
        inhibitors = sorted(
            {e.source for e in edges if e.target == var and e.sign == "-"}
        )
        if activators or inhibitors:
            rules[var] = _default_rule(activators, inhibitors)
    model = BooleanModel(
        variables, rules, edges, source=str(doc.get("id") or module.get("id"))
    )
    if logic:
        model = model.with_logic(logic)
    return model


def module_file_to_boolean(
    path: Union[str, Path], logic: Optional[dict[str, str]] = None
) -> BooleanModel:
    """Load a module YAML file and compile it into a :class:`BooleanModel`."""
    doc = yaml.safe_load(Path(path).read_text())
    return module_to_boolean(doc, logic)


# --------------------------------------------------------------------------
# Boolean expression parsing (bnet syntax) and monotonicity
# --------------------------------------------------------------------------

_TOKEN = re.compile(
    r"\s*(?:(\()|(\))|(&)|(\|)|(!)|([A-Za-z_][A-Za-z0-9_.]*)|([01])(?![A-Za-z0-9_.]))"
)


def _tokenize(expr: str) -> list[str]:
    """Tokenise a bnet expression (``&``, ``|``, ``!``, parentheses, identifiers, ``0``/``1``).

    >>> _tokenize("(a | b) & !c")
    ['(', 'a', '|', 'b', ')', '&', '!', 'c']
    >>> _tokenize("x, 1"[3:]), _tokenize("0")
    (['1'], ['0'])
    >>> _tokenize("a && b")
    Traceback (most recent call last):
    ...
    ValueError: '&&' / '||' are not bnet syntax (use single '&' / '|') in 'a && b'
    """
    if "&&" in expr or "||" in expr:
        raise ValueError(
            f"'&&' / '||' are not bnet syntax (use single '&' / '|') in {expr!r}"
        )
    tokens: list[str] = []
    pos = 0
    expr = expr.strip()
    while pos < len(expr):
        m = _TOKEN.match(expr, pos)
        if not m or m.end() == pos:
            raise ValueError(f"cannot tokenize {expr[pos : pos + 20]!r}")
        tokens.append(next(g for g in m.groups() if g is not None))
        pos = m.end()
    return tokens


def _parse(tokens: list[str]) -> Any:
    """Recursive-descent parse into nested tuples: ('var', x) | ('not', e) | ('and'|'or', [..])."""
    pos = 0

    def peek() -> Optional[str]:
        return tokens[pos] if pos < len(tokens) else None

    def take() -> str:
        nonlocal pos
        tok = tokens[pos]
        pos += 1
        return tok

    def atom() -> Any:
        tok = take()
        if tok == "(":
            e = disj()
            if take() != ")":
                raise ValueError("expected ')'")
            return e
        if tok == "!":
            return ("not", atom())
        return ("var", tok)

    def conj() -> Any:
        items = [atom()]
        while peek() == "&":
            take()
            items.append(atom())
        return items[0] if len(items) == 1 else ("and", items)

    def disj() -> Any:
        items = [conj()]
        while peek() == "|":
            take()
            items.append(conj())
        return items[0] if len(items) == 1 else ("or", items)

    tree = disj()
    if pos != len(tokens):
        raise ValueError(f"trailing tokens: {tokens[pos:]}")
    return tree


def _identifiers(expr: str) -> list[str]:
    """Identifiers used in a bnet expression, in order of first appearance.

    >>> _identifiers("(a | b) & !c & a")
    ['a', 'b', 'c']
    """
    seen: list[str] = []
    for tok in _tokenize(expr):
        if (
            tok not in {"(", ")", "&", "|", "!"}
            and tok not in ("true", "false", "1", "0")
            and tok not in seen
        ):
            seen.append(tok)
    return seen


def _evaluate(tree: Any, env: dict[str, bool]) -> bool:
    kind = tree[0]
    if kind == "var":
        name = tree[1]
        if name in ("true", "1"):
            return True
        if name in ("false", "0"):
            return False
        return env[name]
    if kind == "not":
        return not _evaluate(tree[1], env)
    if kind == "and":
        return all(_evaluate(t, env) for t in tree[1])
    return any(_evaluate(t, env) for t in tree[1])


def _monotone_sign(expr: str, regulator: str, max_regulators: int = 16) -> str:
    """Sign of ``regulator`` in ``expr`` by exhaustive evaluation.

    Returns ``+`` (activating), ``-`` (inhibiting), ``?`` (non-monotone) or ``0``
    (not essential). Exhaustive over the other identifiers, so capped.

    >>> _monotone_sign("(a | b) & !c", "a"), _monotone_sign("(a | b) & !c", "c")
    ('+', '-')
    >>> _monotone_sign("(a & !b) | (!a & b)", "a")
    '?'
    >>> _monotone_sign("a | (b & !b)", "b")
    '0'
    """
    tree = _parse(_tokenize(expr))
    others = [i for i in _identifiers(expr) if i != regulator]
    if regulator not in _identifiers(expr):
        return "0"
    if len(others) > max_regulators:
        return "?"
    up = down = False
    for values in itertools.product([False, True], repeat=len(others)):
        env = dict(zip(others, values))
        env[regulator] = False
        lo = _evaluate(tree, env)
        env[regulator] = True
        hi = _evaluate(tree, env)
        if hi and not lo:
            up = True
        elif lo and not hi:
            down = True
    if up and down:
        return "?"
    if up:
        return "+"
    if down:
        return "-"
    return "0"


def parse_bnet(text: str, source: Optional[str] = None) -> BooleanModel:
    """Parse BoolNet ``.bnet`` text into a :class:`BooleanModel` with signed edges.

    Identity rules (``x, x``) are read back as inputs. Regulator signs are
    inferred by exhaustive monotonicity evaluation.

    >>> bn = parse_bnet("targets, factors\\nin, in\\nx, in & !y\\ny, x")
    >>> bn.inputs, bn.rules["x"]
    (['in'], 'in & !y')
    >>> sorted(str(e) for e in bn.edges)
    ['in -> x', 'x -> y', 'y -| x']
    """
    variables: list[str] = []
    rules: dict[str, str] = {}
    edges: set[SignedEdge] = set()
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or line.lower().replace(" ", "") == "targets,factors":
            continue
        target, _, expr = line.partition(",")
        target = target.strip()
        expr = expr.strip()
        if not target:
            continue
        if target not in variables:
            variables.append(target)
        if expr == target:
            continue  # identity: an input
        rules[target] = expr
        for reg in _identifiers(expr):
            if reg not in variables:
                variables.append(reg)
            sign = _monotone_sign(expr, reg)
            if sign != "0":
                edges.add(SignedEdge(reg, target, sign))
    return BooleanModel(variables, rules, edges, source)


def parse_bnet_file(path: Union[str, Path]) -> BooleanModel:
    return parse_bnet(Path(path).read_text(), source=str(path))


# --------------------------------------------------------------------------
# SIGNOR ingest
# --------------------------------------------------------------------------


def signor_signed_edges(
    path: Union[str, Path],
    direct_only: bool = False,
    taxa: Optional[set[str]] = None,
) -> set[SignedEdge]:
    """Signed edges from a SIGNOR ``getPathwayData.php?...&relations=only`` TSV.

    Entities are keyed by SIGNOR ``entitya``/``entityb`` names; ``effect`` values
    beginning with ``up-regulates`` map to ``+``, ``down-regulates`` to ``-``, and
    other effects (``unknown``, ``form complex``) are skipped. SIGNOR pools
    relations across species and includes indirect ones: ``direct_only`` keeps
    rows whose ``direct`` flag is ``t``, and ``taxa`` keeps rows whose ``tax_id``
    is in the set (e.g. ``{"9606"}``; SIGNOR uses ``-1`` for unspecified).
    """
    edges: set[SignedEdge] = set()
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if direct_only and (row.get("direct") or "").strip().lower() != "t":
                continue
            if taxa is not None and (row.get("tax_id") or "").strip() not in taxa:
                continue
            effect = (row.get("effect") or "").strip()
            if effect.startswith("up-regulates"):
                sign = "+"
            elif effect.startswith("down-regulates"):
                sign = "-"
            else:
                continue
            a = (row.get("entitya") or "").strip()
            b = (row.get("entityb") or "").strip()
            if a and b:
                edges.add(SignedEdge(a, b, sign))
    return edges


# --------------------------------------------------------------------------
# Mapping + diff
# --------------------------------------------------------------------------


@dataclass
class Projection:
    """Result of renaming an edge set into a shared symbol namespace."""

    edges: set[SignedEdge] = field(default_factory=set)
    unmapped_ids: set[str] = field(default_factory=set)
    #: edges with exactly one mapped endpoint (kept with the mapped side renamed);
    #: these are the external regulators/targets the module does not name.
    partial: set[SignedEdge] = field(default_factory=set)


def project_edges(edges: set[SignedEdge], mapping: dict[str, str]) -> Projection:
    """Rename edge endpoints through ``mapping`` (id -> shared symbol).

    Fully mapped edges land in ``edges``; edges with one mapped endpoint land in
    ``partial`` (mapped side renamed, the other left as-is) so a calibration can
    list external regulators of a mapped element that the module does not name.
    Self-edges produced by the projection (two ids mapped to the same symbol) are
    dropped.

    >>> e = {SignedEdge("v_RAF", "v_MEK1_2", "+"), SignedEdge("v_AKT", "v_RAF", "-")}
    >>> proj = project_edges(e, {"v_RAF": "raf", "v_MEK1_2": "mek"})
    >>> sorted(str(x) for x in proj.edges), sorted(proj.unmapped_ids)
    (['raf -> mek'], ['v_AKT'])
    >>> sorted(str(x) for x in proj.partial)
    ['v_AKT -| raf']
    """
    out = Projection()
    for e in edges:
        s = mapping.get(e.source)
        t = mapping.get(e.target)
        if s is None:
            out.unmapped_ids.add(e.source)
        if t is None:
            out.unmapped_ids.add(e.target)
        if s is not None and t is not None:
            if s != t:
                out.edges.add(SignedEdge(s, t, e.sign))
        elif s is not None or t is not None:
            out.partial.add(SignedEdge(s or e.source, t or e.target, e.sign))
    return out


def find_paths(
    edges: set[SignedEdge],
    source: str,
    target: str,
    via: set[str],
    max_paths: int = 10_000,
) -> list[tuple[str, list[str]]]:
    """All simple directed paths ``source -> ... -> target`` whose interior lies in ``via``.

    Returns ``(net_sign, [interior vertices])`` pairs in a deterministic order
    (adjacency and results sorted), so callers are reproducible across runs.
    The search enumerates simple paths, which is exponential in the worst case;
    it is meant for the curated-module and published-model scale this project
    runs at (tens of variables, ``via`` sets of a few dozen), not for genome-scale
    graphs. ``max_paths`` bounds the enumeration as a safety valve; hitting it
    emits a :class:`RuntimeWarning` and :func:`path_sign` then answers ``?``
    (unknown) rather than a sign derived from a partial enumeration.

    >>> es = {SignedEdge("a", "b", "+"), SignedEdge("b", "d", "+"),
    ...       SignedEdge("a", "c", "-"), SignedEdge("c", "d", "+")}
    >>> find_paths(es, "a", "d", {"b", "c"})
    [('+', ['b']), ('-', ['c'])]
    """
    out: dict[str, list[SignedEdge]] = {}
    for e in sorted(edges, key=lambda e: (e.source, e.target, e.sign)):
        out.setdefault(e.source, []).append(e)
    found: list[tuple[str, list[str]]] = []
    stack: list[tuple[str, str, tuple[str, ...]]] = [(source, "+", ())]
    while stack:
        node, sign, interior = stack.pop()
        for e in out.get(node, []):
            if e.sign not in ("+", "-"):
                continue
            nsign = sign if e.sign == "+" else ("-" if sign == "+" else "+")
            if e.target == target:
                found.append((nsign, list(interior)))
                if len(found) >= max_paths:
                    warnings.warn(
                        f"find_paths({source!r} -> {target!r}) hit max_paths={max_paths}; "
                        "the enumeration is truncated",
                        RuntimeWarning,
                        stacklevel=2,
                    )
                    return sorted(found, key=lambda p: (len(p[1]), p[1], p[0]))
            elif e.target in via and e.target not in interior and e.target != source:
                stack.append((e.target, nsign, interior + (e.target,)))
    return sorted(found, key=lambda p: (len(p[1]), p[1], p[0]))


def path_sign(
    edges: set[SignedEdge],
    source: str,
    target: str,
    via: set[str],
    max_paths: int = 10_000,
) -> Optional[str]:
    """Net sign of the directed path(s) ``source -> ... -> target`` through ``via``.

    Used to recognise an external edge that the module expresses as a chain
    through intermediate tiers the external model does not name (tier
    compression). Returns ``+``/``-`` when every such path agrees, ``?`` when
    paths of both signs exist or the enumeration was truncated at ``max_paths``
    (a partial enumeration must not yield a definite sign), and ``None`` when
    there is no path.

    >>> es = {SignedEdge("a", "b", "+"), SignedEdge("b", "c", "+"), SignedEdge("c", "d", "-")}
    >>> path_sign(es, "a", "d", {"b", "c"}), path_sign(es, "a", "d", {"b"})
    ('-', None)
    >>> es |= {SignedEdge("a", "d", "+")}
    >>> path_sign(es, "a", "d", {"b", "c"})
    '?'
    """
    paths = find_paths(edges, source, target, via, max_paths=max_paths)
    if not paths:
        return None
    if len(paths) >= max_paths:
        return "?"
    signs = {sign for sign, _ in paths}
    return signs.pop() if len(signs) == 1 else "?"


@dataclass
class SignedEdgeDiff:
    agree: set[SignedEdge] = field(default_factory=set)
    sign_conflict: set[tuple[SignedEdge, SignedEdge]] = field(default_factory=set)
    left_only: set[SignedEdge] = field(default_factory=set)
    right_only: set[SignedEdge] = field(default_factory=set)

    @property
    def full_agreement(self) -> bool:
        return not (self.sign_conflict or self.left_only or self.right_only)


def diff_signed_edges(left: set[SignedEdge], right: set[SignedEdge]) -> SignedEdgeDiff:
    """Diff two signed-edge sets on a shared symbol namespace.

    >>> l = {SignedEdge("a", "b", "+"), SignedEdge("c", "b", "-")}
    >>> r = {SignedEdge("a", "b", "+"), SignedEdge("c", "b", "+"), SignedEdge("b", "a", "-")}
    >>> d = diff_signed_edges(l, r)
    >>> sorted(map(str, d.agree)), sorted(map(str, d.right_only)), len(d.sign_conflict)
    (['a -> b'], ['b -| a'], 1)
    """
    diff = SignedEdgeDiff()
    lpairs = {(e.source, e.target): e for e in left}
    rpairs = {(e.source, e.target): e for e in right}
    for key, le in lpairs.items():
        re_ = rpairs.get(key)
        if re_ is None:
            diff.left_only.add(le)
        elif re_.sign == le.sign or "?" in (re_.sign, le.sign):
            diff.agree.add(le)
        else:
            diff.sign_conflict.add((le, re_))
    for key, re_ in rpairs.items():
        if key not in lpairs:
            diff.right_only.add(re_)
    return diff


def format_signed_diff(diff: SignedEdgeDiff, left_label: str, right_label: str) -> str:
    """Human-readable diff report."""
    lines = [f"# {left_label} vs {right_label}"]
    total = (
        len(diff.agree)
        + len(diff.sign_conflict)
        + len(diff.left_only)
        + len(diff.right_only)
    )
    lines.append(
        f"agree={len(diff.agree)} conflict={len(diff.sign_conflict)} "
        f"{left_label}-only={len(diff.left_only)} {right_label}-only={len(diff.right_only)} (of {total})"
    )
    for e in sorted(diff.agree, key=str):
        lines.append(f"  = {e}")
    for le, re_ in sorted(diff.sign_conflict, key=lambda p: str(p[0])):
        lines.append(f"  ! {le}   vs   {re_}")
    for e in sorted(diff.left_only, key=str):
        lines.append(f"  < {e}")
    for e in sorted(diff.right_only, key=str):
        lines.append(f"  > {e}")
    return "\n".join(lines)


def load_mapping(path: Union[str, Path]) -> dict[str, Any]:
    """Load a reviewed id-mapping YAML (see models/boolean/README.md)."""
    data = yaml.safe_load(Path(path).read_text()) or {}
    if not isinstance(data, dict):
        raise ValueError("mapping file must be a YAML mapping")
    return data


def iter_mapping_pairs(section: Any) -> Iterator[tuple[str, str]]:
    """Yield ``(external_id, symbol)`` pairs from a mapping section.

    A section is ``{symbol: external_id | [external_id, ...]}``.

    >>> list(iter_mapping_pairs({"raf": ["v_RAF", "BRAF"], "mek": "v_MEK1_2"}))
    [('v_RAF', 'raf'), ('BRAF', 'raf'), ('v_MEK1_2', 'mek')]
    """
    if not isinstance(section, dict):
        return
    for symbol, ext in section.items():
        for ext_id in as_list(ext):
            if ext_id is not None:
                yield str(ext_id), str(symbol)
