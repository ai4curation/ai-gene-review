#!/usr/bin/env python
"""Run a module's executable Boolean model: attractors, scenarios, browser export.

:mod:`ai_gene_review.module_boolean` translates a module into a Boolean network.
This module *runs* it, without any third-party solver, so the scenarios a curator
declares under ``executable_models`` can be checked in ordinary validation and
tests:

* :func:`attractors` enumerates the asynchronous state-transition graph
  exhaustively and returns its terminal strongly connected components. That is
  exact, and cheap for module-sized networks (2^n states; capped at
  ``MAX_EXHAUSTIVE_VARIABLES``). For large networks use biodivine-aeon, as
  ``projects/BOOLEAN_MODELS/run_mapk_demo.py`` does.
* :func:`run_scenario` applies a ``ModelScenario`` (fixed elements, removed
  connections) and compares the attractors with its stated expectations.
* :func:`boolean_model_payload` exports the network, its rules as expression
  trees, and every scenario's result as JSON for the in-browser simulator.

Example: a stimulus that activates a kinase, which induces its own inhibitor.

>>> doc = {"module": {"id": "loop", "parts": [
...   {"node": {"id": "s", "label": "Stimulus"}},
...   {"node": {"id": "k", "label": "Kinase"}},
...   {"node": {"id": "p", "label": "Phosphatase"}}],
...   "connections": [
...     {"source": "s", "target": "k", "connection_type": "CAUSES"},
...     {"source": "k", "target": "p", "connection_type": "CAUSES"},
...     {"source": "p", "target": "k", "connection_type": "NEGATIVELY_REGULATES"}]}}
>>> model = module_to_boolean(doc)
>>> [a.kind for a in attractors(model, {"s": True})]
['CYCLIC']
>>> [a.kind for a in attractors(model, {"s": False})], attractors(model, {"s": False})[0].always_off
(['FIXED_POINT'], ['s', 'k', 'p'])
>>> cut = module_to_boolean(doc, removed_connections={("p", "k")})
>>> attractors(cut, {"s": True})[0].always_on
['s', 'k', 'p']
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ai_gene_review.module_boolean import (
    BooleanModel,
    _evaluate,
    _parse,
    _tokenize,
    module_to_boolean,
)
from ai_gene_review.module_notation import iter_nodes
from ai_gene_review.render_modules import as_list

MAX_EXHAUSTIVE_VARIABLES = 18


@dataclass
class Attractor:
    """A terminal strongly connected component of the asynchronous dynamics."""

    variables: list[str]
    states: list[int]

    @property
    def kind(self) -> str:
        return "FIXED_POINT" if len(self.states) == 1 else "CYCLIC"

    def _values(self, var: str) -> set[bool]:
        bit = 1 << self.variables.index(var)
        return {bool(s & bit) for s in self.states}

    @property
    def always_on(self) -> list[str]:
        return [v for v in self.variables if self._values(v) == {True}]

    @property
    def always_off(self) -> list[str]:
        return [v for v in self.variables if self._values(v) == {False}]

    @property
    def oscillating(self) -> list[str]:
        return [v for v in self.variables if self._values(v) == {False, True}]

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "size": len(self.states),
            "always_on": self.always_on,
            "always_off": self.always_off,
            "oscillating": self.oscillating,
        }


def _compile(model: BooleanModel, fixed: dict[str, bool]) -> list[Any]:
    """One update function per variable: a parse tree, a constant, or None (input)."""
    funcs: list[Any] = []
    for var in model.variables:
        if var in fixed:
            funcs.append(bool(fixed[var]))
        elif var in model.rules:
            funcs.append(_parse(_tokenize(model.rules[var])))
        else:
            funcs.append(None)  # free input: holds its value
    return funcs


def _successors(state: int, variables: list[str], funcs: list[Any]) -> list[int]:
    env = {v: bool(state >> i & 1) for i, v in enumerate(variables)}
    out: list[int] = []
    for i, f in enumerate(funcs):
        if f is None:
            continue
        target = f if isinstance(f, bool) else _evaluate(f, env)
        if target != env[variables[i]]:
            out.append(state ^ (1 << i))
    return out


def attractors(
    model: BooleanModel, fixed: Optional[dict[str, bool]] = None
) -> list[Attractor]:
    """All attractors of the asynchronous dynamics, by exhaustive enumeration.

    ``fixed`` holds variables at constants (a stimulus, a knockout). Inputs not
    in ``fixed`` keep whatever value they start with, so each of their settings
    contributes its own attractors.
    """
    fixed = dict(fixed or {})
    unknown = sorted(set(fixed) - set(model.variables))
    if unknown:
        raise KeyError(f"unknown variables {unknown}")
    n = len(model.variables)
    if n > MAX_EXHAUSTIVE_VARIABLES:
        raise ValueError(
            f"{n} variables exceeds the exhaustive limit ({MAX_EXHAUSTIVE_VARIABLES}); "
            "use biodivine-aeon"
        )
    funcs = _compile(model, fixed)
    succ = [_successors(s, model.variables, funcs) for s in range(1 << n)]

    # Iterative Tarjan; a component is terminal if no edge leaves it.
    index = [-1] * (1 << n)
    low = [0] * (1 << n)
    on_stack = [False] * (1 << n)
    stack: list[int] = []
    counter = 0
    result: list[Attractor] = []
    for root in range(1 << n):
        if index[root] != -1:
            continue
        work = [(root, 0)]
        while work:
            v, i = work.pop()
            if i == 0:
                index[v] = low[v] = counter
                counter += 1
                stack.append(v)
                on_stack[v] = True
            recurse = False
            while i < len(succ[v]):
                w = succ[v][i]
                i += 1
                if index[w] == -1:
                    work.append((v, i))
                    work.append((w, 0))
                    recurse = True
                    break
                if on_stack[w]:
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                comp: list[int] = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp.append(w)
                    if w == v:
                        break
                members = set(comp)
                if all(w in members for u in comp for w in succ[u]):
                    result.append(Attractor(list(model.variables), sorted(comp)))
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[v])
    result.sort(key=lambda a: a.states[0])
    return result


# --------------------------------------------------------------------------
# Scenarios declared under executable_models
# --------------------------------------------------------------------------


@dataclass
class ScenarioResult:
    model_id: str
    scenario_id: str
    label: str
    attractors: list[Attractor]
    failures: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.failures


def boolean_models(doc: dict[str, Any]) -> list[dict[str, Any]]:
    """The ``executable_models`` entries of type BOOLEAN derived from the module."""
    return [
        m
        for m in as_list(doc.get("executable_models"))
        if isinstance(m, dict)
        and m.get("model_type") == "BOOLEAN"
        and m.get("derivation") == "DERIVED_FROM_MODULE"
    ]


def _removed(scenario: dict[str, Any]) -> set[tuple[str, str]]:
    return {
        (str(r.get("source")), str(r.get("target")))
        for r in as_list(scenario.get("removed_connections"))
        if isinstance(r, dict)
    }


def _settings(scenario: dict[str, Any]) -> dict[str, bool]:
    return {
        str(s.get("element")): bool(s.get("active"))
        for s in as_list(scenario.get("settings"))
        if isinstance(s, dict)
    }


def run_scenario(
    doc: dict[str, Any], model_id: str, scenario: dict[str, Any]
) -> ScenarioResult:
    """Translate the module for ``scenario``, find its attractors, check expectations."""
    sid = str(scenario.get("id"))
    label = str(scenario.get("label") or sid)
    failures: list[str] = []
    removed = _removed(scenario)
    declared = {
        (str(c.get("source")), str(c.get("target")))
        for node in iter_nodes(doc.get("module") or {})
        for c in as_list(node.get("connections"))
        if isinstance(c, dict)
    }
    for pair in sorted(removed - declared):
        failures.append(f"removed connection {pair[0]} -> {pair[1]} is not declared")
    model = module_to_boolean(doc, removed_connections=removed)
    settings = _settings(scenario)
    bad = sorted(set(settings) - set(model.variables))
    if bad:
        failures.append(f"settings name elements that are not model variables: {bad}")
        return ScenarioResult(model_id, sid, label, [], failures)
    found = attractors(model, settings)

    kind = scenario.get("expected_attractor_kind")
    if kind and any(a.kind != kind for a in found):
        failures.append(
            f"expected every attractor to be {kind}, got {[a.kind for a in found]}"
        )
    count = scenario.get("expected_attractor_count")
    if count is not None and len(found) != int(count):
        failures.append(f"expected {count} attractor(s), got {len(found)}")
    for slot, attr in (
        ("expected_active", "always_on"),
        ("expected_inactive", "always_off"),
        ("expected_oscillating", "oscillating"),
    ):
        for element in as_list(scenario.get(slot)):
            element = str(element)
            if element not in model.variables:
                failures.append(
                    f"{slot} names {element}, which is not a model variable"
                )
                continue
            missing = [
                i for i, a in enumerate(found) if element not in getattr(a, attr)
            ]
            if missing:
                failures.append(
                    f"{element} is not {attr.replace('_', ' ')} in every attractor"
                )
    return ScenarioResult(model_id, sid, label, found, failures)


def run_declared_scenarios(doc: dict[str, Any]) -> list[ScenarioResult]:
    """Run every scenario of every derived Boolean model the module declares."""
    results: list[ScenarioResult] = []
    for model in boolean_models(doc):
        for scenario in as_list(model.get("scenarios")):
            if isinstance(scenario, dict):
                results.append(run_scenario(doc, str(model.get("id")), scenario))
    return results


# --------------------------------------------------------------------------
# Browser payload
# --------------------------------------------------------------------------


def _tree_json(tree: Any) -> Any:
    """Parse tree -> JSON-friendly nested lists, as read by the page's evaluator."""
    kind = tree[0]
    if kind == "var":
        name = tree[1]
        if name in ("1", "true"):
            return True
        if name in ("0", "false"):
            return False
        return name
    if kind == "not":
        return ["not", _tree_json(tree[1])]
    return [kind, [_tree_json(t) for t in tree[1]]]


def _rules_json(model: BooleanModel) -> dict[str, Any]:
    return {
        var: {"text": rule, "tree": _tree_json(_parse(_tokenize(rule)))}
        for var, rule in model.rules.items()
    }


def _labels(doc: dict[str, Any]) -> dict[str, str]:
    labels: dict[str, str] = {}
    for node in iter_nodes(doc.get("module") or {}):
        if node.get("id"):
            labels[str(node["id"])] = str(node.get("label") or node["id"])
        for annoton in as_list(node.get("annotons")):
            if isinstance(annoton, dict) and annoton.get("id"):
                labels[str(annoton["id"])] = str(
                    annoton.get("label")
                    or annoton.get("role_description")
                    or annoton["id"]
                )
    return labels


def _iter_elements(doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Every node and annoton mapping in the module tree."""
    out: list[dict[str, Any]] = []
    for node in iter_nodes(doc.get("module") or {}):
        out.append(node)
        out.extend(a for a in as_list(node.get("annotons")) if isinstance(a, dict))
    return out


def layered_layout(model: BooleanModel) -> dict[str, list[int]]:
    """``[rank, slot]`` per variable for a top-to-bottom drawing of the network.

    Rank is the longest activating path from the inputs once feedback (back
    edges found by depth-first search in variable order) is set aside, so a
    cascade reads downwards and its feedback loops point back up. An input sits
    one rank above the first element it regulates; slot orders the variables
    of a rank by document order.

    >>> m = module_to_boolean({"module": {"id": "m", "parts": [
    ...   {"node": {"id": "s"}}, {"node": {"id": "k"}}, {"node": {"id": "p"}},
    ...   {"node": {"id": "g"}}], "connections": [
    ...   {"source": "s", "target": "k", "connection_type": "CAUSES"},
    ...   {"source": "k", "target": "p", "connection_type": "CAUSES"},
    ...   {"source": "g", "target": "p", "connection_type": "NEGATIVELY_REGULATES"},
    ...   {"source": "p", "target": "k", "connection_type": "NEGATIVELY_REGULATES"}]}})
    >>> layered_layout(m)
    {'s': [0, 0], 'k': [1, 0], 'p': [2, 0], 'g': [1, 1]}
    """
    order = list(model.variables)
    out_edges: dict[str, list[str]] = {v: [] for v in order}
    for e in sorted(
        model.edges, key=lambda e: (order.index(e.source), order.index(e.target))
    ):
        out_edges[e.source].append(e.target)
    back: set[tuple[str, str]] = set()
    state: dict[str, int] = {}  # 1 = on stack, 2 = done

    def dfs(v: str) -> None:
        state[v] = 1
        for w in out_edges[v]:
            if state.get(w) == 1:
                back.add((v, w))
            elif w not in state:
                dfs(w)
        state[v] = 2

    for v in [x for x in order if x not in model.rules] + order:
        if v not in state:
            dfs(v)
    forward = [
        e for e in model.edges if (e.source, e.target) not in back and e.sign == "+"
    ]
    rank = {v: 0 for v in order}
    for _ in order:  # longest path by relaxation on the acyclic forward graph
        for e in forward:
            rank[e.target] = max(rank[e.target], rank[e.source] + 1)
    for v in order:
        targets = [rank[w] for w in out_edges[v] if (v, w) not in back]
        if v not in model.rules and targets:
            rank[v] = max(min(targets) - 1, 0)
    slots: dict[int, int] = {}
    layout: dict[str, list[int]] = {}
    for v in order:
        layout[v] = [rank[v], slots.get(rank[v], 0)]
        slots[rank[v]] = slots.get(rank[v], 0) + 1
    return layout


def boolean_model_payload(
    doc: dict[str, Any], model_entry: dict[str, Any]
) -> dict[str, Any]:
    """Everything the in-browser simulator needs for one derived Boolean model.

    The base network, plus for each scenario the rules that differ from the base
    (a removed connection changes its target's rule), the fixed settings, and
    the attractors computed here, so the page shows the committed result before
    the reader touches anything.
    """
    base = module_to_boolean(doc)
    labels = _labels(doc)
    scenarios: list[dict[str, Any]] = []
    for scenario in as_list(model_entry.get("scenarios")):
        if not isinstance(scenario, dict):
            continue
        variant = module_to_boolean(doc, removed_connections=_removed(scenario))
        overrides = {
            var: rule
            for var, rule in _rules_json(variant).items()
            if base.rules.get(var) != rule["text"]
        }
        overrides.update(
            {
                var: None  # became an input
                for var in base.rules
                if var not in variant.rules
            }
        )
        result = run_scenario(doc, str(model_entry.get("id")), scenario)
        scenarios.append(
            {
                "id": scenario.get("id"),
                "label": scenario.get("label") or scenario.get("id"),
                "description": scenario.get("description"),
                "settings": _settings(scenario),
                "removed": [list(p) for p in sorted(_removed(scenario))],
                "rule_overrides": overrides,
                "removed_edges": sorted(
                    [e.source, e.target, e.sign] for e in base.edges - variant.edges
                ),
                "attractors": [a.to_dict() for a in result.attractors],
                "failures": result.failures,
            }
        )
    return {
        "module_id": doc.get("id"),
        "title": doc.get("title"),
        "model_id": model_entry.get("id"),
        "model_title": model_entry.get("title"),
        "description": model_entry.get("description"),
        "variables": [
            {
                "id": v,
                "label": labels.get(v, v),
                "input": v not in base.rules,
            }
            for v in base.variables
        ],
        "edges": sorted([e.source, e.target, e.sign] for e in base.edges),
        "layout": layered_layout(base),
        "rules": _rules_json(base),
        "declared_logic": sorted(
            str(n.get("id"))
            for n in _iter_elements(doc)
            if n.get("activation_logic") and str(n.get("id")) in base.rules
        ),
        "bnet": base.to_bnet(),
        "scenarios": scenarios,
    }
