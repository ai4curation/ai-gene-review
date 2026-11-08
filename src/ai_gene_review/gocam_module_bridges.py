"""Explain GO-CAM causal edges with module paths.

A GO-CAM edge such as "JAK1 kinase activity (plasma membrane) directly
positively regulates STAT3 transcription factor activity (nucleus)" is
compressed: the steps between (STAT dimerization, nuclear import) are not in the
model. A module can spell them out. When both ends of the edge are pinned to
module elements through ``gocam_associations``, and the module's
``connections`` lead from the upstream element to the downstream one through a
``TRANSPORT_STEP`` node, the module explains how the edge crosses compartments.

Pins are explicit and curated: a ``GoCamAssociation`` with an ``activity`` on a
module node or annoton. Nothing here matches genes to modules automatically.

Example with an in-memory module:

>>> module = {
...     "module": {
...         "id": "m", "label": "m",
...         "parts": [
...             {"order": 1, "node": {"id": "kinase_step", "label": "k",
...               "annotons": [{"id": "jak", "label": "JAK",
...                 "gocam_associations": [{"model": "gomodel:M", "activity": "gomodel:M/a"}]}]}},
...             {"order": 2, "node": {"id": "import", "label": "i",
...               "module_type": "TRANSPORT_STEP", "module_ref": "nuclear_import"}},
...             {"order": 3, "node": {"id": "tf_step", "label": "t",
...               "gocam_associations": [{"model": "gomodel:M", "activity": "gomodel:M/b"}]}},
...         ],
...         "connections": [
...             {"source": "kinase_step", "target": "import", "connection_type": "PRECEDES"},
...             {"source": "import", "target": "tf_step", "connection_type": "PROVIDES_INPUT_FOR"},
...         ],
...     }
... }
>>> index = ModuleBridgeIndex([ModuleGraph.from_dict("m", module)])
>>> e = index.explain("gomodel:M/a", "gomodel:M/b")
>>> e.path, e.bridges, e.via_modules
(('kinase_step', 'import', 'tf_step'), ('import',), ('nuclear_import',))
>>> index.explain("gomodel:M/b", "gomodel:M/a") is None
True
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional

import yaml

#: Connection types that do not carry the signal forward.
NON_PROPAGATING_CONNECTIONS = frozenset({"NEGATIVELY_REGULATES"})

#: Module node type that bridges compartments.
BRIDGE_MODULE_TYPE = "TRANSPORT_STEP"


@dataclass(frozen=True)
class ModuleExplanation:
    """A module path that spells out the steps behind a GO-CAM edge."""

    module: str
    upstream_element: str
    downstream_element: str
    path: tuple[str, ...]
    bridges: tuple[str, ...]
    via_modules: tuple[str, ...] = ()
    bridge_locations: tuple[str, ...] = ()
    """GO cellular component ids declared at or below the bridge nodes, and
    by the modules they include. The compartment check uses these to decide
    whether the transport step spans the edge being explained."""

    def to_dict(self) -> dict[str, Any]:
        """Return a YAML-friendly dict."""
        d: dict[str, Any] = {
            "module": self.module,
            "upstream_element": self.upstream_element,
            "downstream_element": self.downstream_element,
            "path": list(self.path),
            "bridges": list(self.bridges),
        }
        if self.via_modules:
            d["via_modules"] = list(self.via_modules)
        if self.bridge_locations:
            d["bridge_locations"] = list(self.bridge_locations)
        return d


@dataclass
class ModuleGraph:
    """Nodes, containment, connections and GO-CAM pins of one module."""

    stem: str
    parent: dict[str, Optional[str]] = field(default_factory=dict)
    node_type: dict[str, Optional[str]] = field(default_factory=dict)
    edges: dict[str, set[str]] = field(default_factory=dict)
    pins: dict[str, set[str]] = field(default_factory=dict)
    module_ref: dict[str, str] = field(default_factory=dict)
    node_locations: dict[str, set[str]] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, stem: str, doc: dict[str, Any]) -> "ModuleGraph":
        """Build the graph from a parsed ModuleReview document."""
        g = cls(stem=stem)
        g._walk_node(doc["module"], None)
        return g

    @classmethod
    def from_file(cls, path: Path) -> "ModuleGraph":
        """Build the graph from a module YAML file."""
        return cls.from_dict(path.stem, yaml.safe_load(path.read_text()))

    def _pin(self, element: str, assocs: Optional[list[dict[str, Any]]]) -> None:
        for a in assocs or []:
            act = a.get("activity")
            if act:
                self.pins.setdefault(normalize_activity(act), set()).add(element)

    def _walk_node(self, node: dict[str, Any], parent: Optional[str]) -> None:
        nid = node["id"]
        self.parent[nid] = parent
        self.node_type[nid] = node.get("module_type")
        if node.get("module_ref"):
            self.module_ref[nid] = node["module_ref"]
        self._pin(nid, node.get("gocam_associations"))
        locs = self.node_locations.setdefault(nid, set())
        locs |= _term_ids((node.get("context") or {}).get("cellular_components"))
        for ann in node.get("annotons") or []:
            self.parent[ann["id"]] = nid
            self._pin(ann["id"], ann.get("gocam_associations"))
            locs |= _term_ids(ann.get("locations"))
        for part in node.get("parts") or []:
            self._walk_node(part["node"], nid)
        for vs in node.get("variant_sets") or []:
            for variant in vs.get("variants") or []:
                self._walk_node(variant, nid)
        for conn in node.get("connections") or []:
            if conn.get("connection_type") in NON_PROPAGATING_CONNECTIONS:
                continue
            self.edges.setdefault(conn["source"], set()).add(conn["target"])

    @property
    def connected(self) -> set[str]:
        """Elements that appear as a source or target of some connection."""
        out = set(self.edges)
        for targets in self.edges.values():
            out |= targets
        return out

    def lift(self, element: str) -> Optional[str]:
        """Nearest element at or above ``element`` that takes part in a connection."""
        connected = self.connected
        cur: Optional[str] = element
        while cur is not None:
            if cur in connected:
                return cur
            cur = self.parent.get(cur)
        return None

    def path(self, source: str, target: str) -> Optional[tuple[str, ...]]:
        """Shortest directed path between two connected elements, if any."""
        if source == target:
            return (source,)
        prev: dict[str, str] = {}
        queue: deque[str] = deque([source])
        seen = {source}
        while queue:
            cur = queue.popleft()
            for nxt in sorted(self.edges.get(cur, ())):
                if nxt in seen:
                    continue
                prev[nxt] = cur
                if nxt == target:
                    out = [target]
                    while out[-1] != source:
                        out.append(prev[out[-1]])
                    return tuple(reversed(out))
                seen.add(nxt)
                queue.append(nxt)
        return None

    def explain(self, upstream: str, downstream: str) -> Optional[ModuleExplanation]:
        """Explain a GO-CAM edge between two pinned activities, if this module can."""
        for ue in sorted(self.pins.get(upstream, ())):
            for de in sorted(self.pins.get(downstream, ())):
                lu, ld = self.lift(ue), self.lift(de)
                if lu is None or ld is None:
                    continue
                p = self.path_via_bridge(lu, ld)
                if p is None:
                    continue
                bridges = tuple(
                    n for n in p if self.node_type.get(n) == BRIDGE_MODULE_TYPE
                )
                return ModuleExplanation(
                    self.stem,
                    ue,
                    de,
                    p,
                    bridges,
                    self.referenced_under(bridges),
                    tuple(sorted(self.locations_under(bridges))),
                )
        return None

    def locations_under(self, nodes: Iterable[str]) -> set[str]:
        """GO location ids declared at or below any of ``nodes``."""
        roots = list(nodes)
        return {
            loc
            for nid, locs in self.node_locations.items()
            if any(self.is_under(nid, r) for r in roots)
            for loc in locs
        }

    @property
    def all_locations(self) -> set[str]:
        """Every GO location id declared anywhere in the module."""
        return {loc for locs in self.node_locations.values() for loc in locs}

    def path_via_bridge(self, source: str, target: str) -> Optional[tuple[str, ...]]:
        """Shortest directed path from ``source`` to ``target`` through a transport node.

        The overall shortest path may bypass the transport step (for example
        through a side branch that only tunes the target), so each connected
        transport node is tried as a waypoint.
        """
        best: Optional[tuple[str, ...]] = None
        for b in sorted(self.connected):
            if self.node_type.get(b) != BRIDGE_MODULE_TYPE:
                continue
            first, second = self.path(source, b), self.path(b, target)
            if first is None or second is None:
                continue
            candidate = first + second[1:]
            if best is None or len(candidate) < len(best):
                best = candidate
        return best

    def is_under(self, element: str, ancestor: str) -> bool:
        """True if ``element`` is ``ancestor`` or contained in it."""
        cur: Optional[str] = element
        while cur is not None:
            if cur == ancestor:
                return True
            cur = self.parent.get(cur)
        return False

    def referenced_under(self, nodes: Iterable[str]) -> tuple[str, ...]:
        """Modules included by module_ref at or below any of ``nodes``."""
        roots = list(nodes)
        return tuple(
            sorted(
                {
                    ref
                    for nid, ref in self.module_ref.items()
                    if any(self.is_under(nid, r) for r in roots)
                }
            )
        )


def normalize_activity(activity: str) -> str:
    """Return a GO-CAM activity id in ``gomodel:<model>/<individual>`` form.

    >>> normalize_activity("568b0f9600000284/57ec3a7e00000079")
    'gomodel:568b0f9600000284/57ec3a7e00000079'
    >>> normalize_activity("gomodel:568b0f9600000284/57ec3a7e00000079")
    'gomodel:568b0f9600000284/57ec3a7e00000079'
    """
    return activity if activity.startswith("gomodel:") else f"gomodel:{activity}"


def _term_ids(descriptors: Optional[list[dict[str, Any]]]) -> set[str]:
    """Ontology ids of a list of descriptors (those with a ``term``)."""
    return {
        d["term"]["id"]
        for d in descriptors or []
        if isinstance(d, dict)
        and isinstance(d.get("term"), dict)
        and d["term"].get("id")
    }


class ModuleBridgeIndex:
    """Look up module explanations for GO-CAM edges across many modules.

    With ``modules_dir``, an explanation's ``bridge_locations`` also include
    the locations declared in modules that a bridge node includes by
    ``module_ref``.
    """

    def __init__(
        self, graphs: Iterable[ModuleGraph], modules_dir: Optional[Path] = None
    ):
        self.modules_dir = modules_dir
        self._ref_locations: dict[str, set[str]] = {}
        self.graphs = [g for g in graphs if g.pins]
        self._by_activity: dict[str, list[ModuleGraph]] = {}
        for g in self.graphs:
            for act in g.pins:
                self._by_activity.setdefault(act, []).append(g)

    @classmethod
    def from_dir(cls, modules_dir: Path) -> "ModuleBridgeIndex":
        """Index every module under ``modules_dir`` that pins a GO-CAM activity."""
        return cls(
            (ModuleGraph.from_file(p) for p in iter_pinning_modules(modules_dir)),
            modules_dir,
        )

    def referenced_locations(self, ref: str) -> set[str]:
        """Locations declared in a module named by ``module_ref`` (``stem`` or ``stem#node``)."""
        if ref not in self._ref_locations:
            stem, _, node = ref.partition("#")
            path = self.modules_dir / f"{stem}.yaml" if self.modules_dir else None
            if path is None or not path.exists():
                self._ref_locations[ref] = set()
            else:
                g = ModuleGraph.from_file(path)
                self._ref_locations[ref] = (
                    g.locations_under([node]) if node else g.all_locations
                )
        return self._ref_locations[ref]

    def explain(self, upstream: str, downstream: str) -> Optional[ModuleExplanation]:
        """Return the first module explanation for an edge, or None."""
        up, down = normalize_activity(upstream), normalize_activity(downstream)
        for g in self._by_activity.get(up, []):
            if down in g.pins:
                e = g.explain(up, down)
                if e:
                    extra: set[str] = set()
                    for ref in e.via_modules:
                        extra |= self.referenced_locations(ref)
                    return replace(
                        e,
                        bridge_locations=tuple(sorted(set(e.bridge_locations) | extra)),
                    )
        return None


def iter_pinning_modules(modules_dir: Path) -> Iterator[Path]:
    """Yield module files that contain a GO-CAM activity pin."""
    for p in sorted(modules_dir.glob("*.yaml")):
        text = p.read_text()
        if "gocam_associations" in text and "activity:" in text:
            yield p
