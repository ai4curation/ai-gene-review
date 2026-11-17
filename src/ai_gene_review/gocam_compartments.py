"""Spatial compartment QC for cached GO-CAM models.

A GO-CAM activity says where it happens through ``occurs_in``. This module
checks two things about those locations:

1. **Every location can be placed in a cell.** The ``occurs_in`` term is walked
   up its ``is_a`` / ``part_of`` ancestors until it reaches one of a fixed set of
   pairwise-disjoint compartments (cytosol, nuclear lumen, plasma membrane,
   extracellular region, an organelle lumen or membrane, ...). A term that
   reaches no compartment is *unresolved*: GO itself does not say where it is.
   ``chromatin`` is the standard example: GO places it under ``chromosome``,
   which is not part of the nucleus, so a model that puts a transcription factor
   "in chromatin" never says the activity is nuclear. A term that only reaches a
   union of compartments (``cytoplasm``, ``mitochondrion``) is *coarse*.

2. **Causally connected activities are in the same or adjacent compartments.**
   Adjacent means sharing a boundary: a membrane and the space on either side of
   it. An edge from a cytosolic caspase directly to an extracellular cytokine
   activity skips the plasma membrane, which usually means a step (secretion,
   nuclear import, release from an organelle) is missing from the model, or an
   ``occurs_in`` is wrong.

The compartment set, the unions, the adjacency pairs and the context hints are
data, in ``data/gocam_compartments.yaml``. The ontology is reached through a
function returning the reflexive ``is_a``/``part_of`` ancestors of a term, which
by default comes from an oaklib adapter (``sqlite:obo:go``).

Example with a hand-written ancestor table (cytosol and plasma membrane
resolve; extracellular region is two steps from cytosol):

>>> cm = CompartmentModel.load()
>>> anc = {
...     "GO:0005829": {"GO:0005829"},
...     "GO:0005576": {"GO:0005576"},
...     "GO:0000785": {"GO:0000785", "GO:0005694"},
...     "GO:0005694": {"GO:0005694"},
... }
>>> r = cm.resolve("GO:0005829", lambda t: anc[t])
>>> r.status.value, sorted(r.compartments)
('RESOLVED', ['CYTOSOL'])
>>> cm.distance({"CYTOSOL"}, {"EXTRACELLULAR"})
2
>>> u = cm.resolve("GO:0000785", lambda t: anc[t])
>>> u.status.value, u.hint["usual"]
('UNRESOLVED', 'NUCLEAR_LUMEN')
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, Optional

import yaml

#: Default location of the compartment model.
DEFAULT_COMPARTMENTS_PATH = Path(__file__).parent / "data" / "gocam_compartments.yaml"

#: Causal predicates used in GO-CAM, with labels and whether they assert direct
#: (physical / same-reaction) action. A non-adjacent direct edge is a stronger
#: signal than a non-adjacent indirect one, which may legitimately span a
#: transport step that the model chose not to show.
CAUSAL_PREDICATES: dict[str, tuple[str, bool]] = {
    "RO:0002629": ("directly positively regulates", True),
    "RO:0002630": ("directly negatively regulates", True),
    "RO:0002413": ("directly provides input for", True),
    "RO:0012010": ("removes input for", True),
    "RO:0002407": ("indirectly positively regulates", False),
    "RO:0002409": ("indirectly negatively regulates", False),
    "RO:0002304": ("causally upstream of, positive effect", False),
    "RO:0002305": ("causally upstream of, negative effect", False),
    "RO:0002411": ("causally upstream of", False),
    "RO:0012009": ("constitutively upstream of", False),
    "RO:0002578": ("directly regulates", True),
    "RO:0002212": ("negatively regulates", False),
    "RO:0002418": ("causally upstream of or within", False),
    "RO:0004047": ("causally upstream of or within, positive effect", False),
}

#: Predicates that pass material (a product used by the next activity) rather
#: than regulate. A material-flow edge that skips compartments needs a transport
#: step; a regulation edge may instead act on a protein that then relocates.
INPUT_PREDICATES = frozenset({"RO:0002413", "RO:0012010"})

AncestorFn = Callable[[str], Iterable[str]]

#: Given a GO-CAM gene product id, the compartments it is known to occupy.
ProteinLocationFn = Callable[[str], frozenset[str]]

#: Given upstream and downstream activity ids, a module explanation (or None).
EdgeExplainer = Callable[[str, str], Optional[Any]]

#: Gene-review actions that reject an annotated location.
REJECTING_ACTIONS = frozenset({"REMOVE", "MARK_AS_OVER_ANNOTATED"})
#: Gene-review actions that keep an annotated location.
KEEPING_ACTIONS = frozenset(
    {"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "TOO_GENERAL", "NEW"}
)

#: Hint attached when ``occurs_in`` is a cell type rather than a cellular component.
CELL_TYPE_HINT = (
    "occurs_in names a cell type (CL), which says which cell but not where in it; "
    "add a cellular component."
)


class EdgeKind(str, Enum):
    """What a causal edge passes from one activity to the next."""

    REGULATION = "REGULATION"
    INPUT = "INPUT"
    OTHER = "OTHER"


def edge_kind(predicate: str) -> EdgeKind:
    """Classify a causal predicate.

    >>> edge_kind("RO:0002413").value, edge_kind("RO:0002629").value, edge_kind("RO:9").value
    ('INPUT', 'REGULATION', 'OTHER')
    """
    if predicate in INPUT_PREDICATES:
        return EdgeKind.INPUT
    if predicate in CAUSAL_PREDICATES:
        return EdgeKind.REGULATION
    return EdgeKind.OTHER


class ResolutionStatus(str, Enum):
    """How well an ``occurs_in`` term places an activity in a compartment."""

    RESOLVED = "RESOLVED"
    """The term lies inside exactly one compartment."""
    COARSE = "COARSE"
    """The term spans several compartments (e.g. cytoplasm, mitochondrion)."""
    AMBIGUOUS = "AMBIGUOUS"
    """The term reaches more than one unrelated compartment anchor."""
    UNRESOLVED = "UNRESOLVED"
    """No is_a/part_of path from the term reaches any compartment."""
    MISSING = "MISSING"
    """The activity has no occurs_in."""


class EdgeStatus(str, Enum):
    """Spatial relation between the two ends of a causal edge."""

    SAME = "SAME"
    ADJACENT = "ADJACENT"
    BRIDGED = "BRIDGED"
    """Two membranes bordering the same space (contact site, vesicle docking)."""
    NONADJACENT = "NONADJACENT"
    EXPLAINED = "EXPLAINED"
    """Non-adjacent, but a module path through a transport step spells out the gap,
    and that step's declared locations touch the compartments at both ends."""
    RELOCATING = "RELOCATING"
    """Non-adjacent regulation of a protein known to occupy a compartment next to the regulator."""
    INDETERMINATE = "INDETERMINATE"
    """At least one end has no resolvable location."""


@dataclass(frozen=True)
class Resolution:
    """The compartment(s) an ``occurs_in`` term places an activity in."""

    term: Optional[str]
    status: ResolutionStatus
    compartments: frozenset[str] = frozenset()
    via: tuple[str, ...] = ()
    hint: Optional[dict[str, Any]] = None


@dataclass
class CompartmentModel:
    """A disjoint compartment set with GO anchors, unions and adjacency."""

    compartments: dict[str, dict[str, Any]]
    unions: dict[str, dict[str, Any]]
    adjacency: dict[str, set[str]]
    context_hints: dict[str, dict[str, Any]] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path = DEFAULT_COMPARTMENTS_PATH) -> "CompartmentModel":
        """Load and sanity-check a compartment model YAML.

        >>> cm = CompartmentModel.load()
        >>> "CYTOSOL" in cm.adjacency["PLASMA_MEMBRANE"]
        True
        >>> "NUCLEAR_LUMEN" in cm.adjacency["CYTOSOL"]
        False
        """
        data = yaml.safe_load(path.read_text())
        compartments = data["compartments"]
        adjacency: dict[str, set[str]] = {c: set() for c in compartments}
        for a, b in data["adjacency"]:
            if a not in compartments or b not in compartments:
                raise ValueError(f"adjacency names unknown compartment: {a}, {b}")
            adjacency[a].add(b)
            adjacency[b].add(a)
        unions = data.get("unions") or {}
        for term, u in unions.items():
            unknown = set(u["members"]) - set(compartments)
            if unknown:
                raise ValueError(f"union {term} names unknown compartments {unknown}")
        anchors = [a for c in compartments.values() for a in c["anchors"]]
        if len(anchors) != len(set(anchors)):
            raise ValueError("a GO anchor is used by more than one compartment")
        return cls(
            compartments=compartments,
            unions=unions,
            adjacency=adjacency,
            context_hints=data.get("context_hints") or {},
        )

    @property
    def anchor_index(self) -> dict[str, str]:
        """Map each GO anchor id to its compartment key."""
        return {a: k for k, c in self.compartments.items() for a in c["anchors"]}

    def resolve(self, term: Optional[str], ancestors: AncestorFn) -> Resolution:
        """Place a cellular component term in the compartment model.

        Anchors that are ancestors of another matching anchor are dropped, so
        the most specific compartment wins.
        """
        if not term:
            return Resolution(None, ResolutionStatus.MISSING)
        anc = set(ancestors(term)) | {term}
        index = self.anchor_index
        hits = [a for a in anc if a in index]
        # keep only the most specific anchors
        specific = [
            a for a in hits if not any(b != a and a in set(ancestors(b)) for b in hits)
        ]
        if specific:
            comps = frozenset(index[a] for a in specific)
            status = (
                ResolutionStatus.RESOLVED
                if len(comps) == 1
                else ResolutionStatus.AMBIGUOUS
            )
            return Resolution(term, status, comps, tuple(sorted(specific)))
        union_hits = [u for u in anc if u in self.unions]
        if union_hits:
            # the narrowest union is the one with fewest members
            best = min(union_hits, key=lambda u: (len(self.unions[u]["members"]), u))
            return Resolution(
                term,
                ResolutionStatus.COARSE,
                frozenset(self.unions[best]["members"]),
                (best,),
            )
        return Resolution(
            term, ResolutionStatus.UNRESOLVED, hint=self._hint(term, anc, ancestors)
        )

    def _hint(
        self, term: str, anc: set[str], ancestors: AncestorFn
    ) -> Optional[dict[str, Any]]:
        """Return the most specific context hint for an unresolved term."""
        if term.startswith("CL:"):
            return {"note": CELL_TYPE_HINT}
        candidates = [h for h in anc if h in self.context_hints]
        if not candidates:
            return None
        best = max(candidates, key=lambda h: (len(set(ancestors(h))), h))
        return {"term": best, **self.context_hints[best]}

    def distance(self, a: Iterable[str], b: Iterable[str]) -> Optional[int]:
        """Fewest boundary crossings between any compartment in ``a`` and in ``b``.

        >>> cm = CompartmentModel.load()
        >>> cm.distance({"NUCLEAR_LUMEN"}, {"PLASMA_MEMBRANE"})
        3
        >>> cm.distance({"CYTOSOL", "ER_LUMEN"}, {"CYTOSOL"})
        0
        """
        targets = set(b)
        start = set(a)
        if not start or not targets:
            return None
        seen = set(start)
        queue: deque[tuple[str, int]] = deque((c, 0) for c in start)
        while queue:
            node, d = queue.popleft()
            if node in targets:
                return d
            for nxt in sorted(self.adjacency[node]):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, d + 1))
        return None

    def edge_status(
        self, a: Resolution, b: Resolution
    ) -> tuple[EdgeStatus, Optional[int]]:
        """Classify the spatial relation between two resolved locations.

        For coarse locations the closest pair of members is used, so an edge is
        only called NONADJACENT when no reading of the coarse term makes it
        adjacent.
        """
        if not a.compartments or not b.compartments:
            return EdgeStatus.INDETERMINATE, None
        d = self.distance(a.compartments, b.compartments)
        if d is None:
            return EdgeStatus.INDETERMINATE, None
        if d == 0:
            return EdgeStatus.SAME, 0
        if d == 1:
            return EdgeStatus.ADJACENT, 1
        if d == 2 and self._bridged(a.compartments, b.compartments):
            return EdgeStatus.BRIDGED, 2
        return EdgeStatus.NONADJACENT, d

    def is_membrane(self, compartment: str) -> bool:
        """True if the compartment is a membrane or envelope."""
        return self.compartments[compartment].get("kind") == "membrane"

    def _bridged(self, a: Iterable[str], b: Iterable[str]) -> bool:
        """True if both ends are membranes and some pair borders a common space.

        Both locations must be membranes in every reading: a coarse term such
        as nucleus (envelope plus lumen) does not count, because the activity
        may be in the lumen.

        >>> cm = CompartmentModel.load()
        >>> cm._bridged({"ER_MEMBRANE"}, {"GOLGI_MEMBRANE"})
        True
        >>> cm._bridged({"CYTOSOL"}, {"EXTRACELLULAR"})
        False
        >>> cm._bridged({"PLASMA_MEMBRANE"}, {"NUCLEAR_ENVELOPE", "NUCLEAR_LUMEN"})
        False
        """
        a, b = set(a), set(b)
        if not all(self.is_membrane(c) for c in a | b):
            return False
        for x in a:
            for y in b:
                shared = self.adjacency[x] & self.adjacency[y]
                if any(not self.is_membrane(z) for z in shared):
                    return True
        return False


@dataclass
class LocationFinding:
    """Compartment resolution of one activity's ``occurs_in``."""

    activity_id: str
    gene_product: Optional[str]
    gene_label: Optional[str]
    occurs_in: Optional[str]
    occurs_in_label: Optional[str]
    status: ResolutionStatus
    compartments: list[str]
    hint: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        """Return a YAML-friendly dict."""
        d: dict[str, Any] = {
            "activity_id": self.activity_id,
            "gene_product": self.gene_product,
            "gene_label": self.gene_label,
            "occurs_in": self.occurs_in,
            "occurs_in_label": self.occurs_in_label,
            "status": self.status.value,
            "compartments": self.compartments,
        }
        if self.hint:
            d["hint"] = self.hint
        return d


@dataclass
class EdgeFinding:
    """Spatial relation across one causal edge."""

    upstream: str
    upstream_label: Optional[str]
    downstream: str
    downstream_label: Optional[str]
    predicate: str
    predicate_label: Optional[str]
    direct: Optional[bool]
    upstream_compartments: list[str]
    downstream_compartments: list[str]
    status: EdgeStatus
    distance: Optional[int]
    kind: EdgeKind = EdgeKind.OTHER
    explanation: Optional[dict[str, Any]] = None
    downstream_protein_compartments: Optional[list[str]] = None

    def to_dict(self) -> dict[str, Any]:
        """Return a YAML-friendly dict."""
        d: dict[str, Any] = {
            "upstream": self.upstream,
            "upstream_label": self.upstream_label,
            "downstream": self.downstream,
            "downstream_label": self.downstream_label,
            "predicate": self.predicate,
            "predicate_label": self.predicate_label,
            "direct": self.direct,
            "upstream_compartments": self.upstream_compartments,
            "downstream_compartments": self.downstream_compartments,
            "status": self.status.value,
            "distance": self.distance,
            "kind": self.kind.value,
        }
        if self.explanation:
            d["explanation"] = self.explanation
        if self.downstream_protein_compartments:
            d["downstream_protein_compartments"] = self.downstream_protein_compartments
        return d


@dataclass
class ModelCompartmentReport:
    """Compartment QC for one GO-CAM model."""

    model_id: str
    title: Optional[str]
    locations: list[LocationFinding]
    edges: list[EdgeFinding]

    @property
    def unresolved(self) -> list[LocationFinding]:
        """Activities whose location reaches no compartment."""
        return [
            loc for loc in self.locations if loc.status == ResolutionStatus.UNRESOLVED
        ]

    @property
    def bridged(self) -> list[EdgeFinding]:
        """Causal edges between two membranes that face the same space."""
        return [e for e in self.edges if e.status == EdgeStatus.BRIDGED]

    @property
    def nonadjacent(self) -> list[EdgeFinding]:
        """Causal edges that skip at least one compartment, with no explanation."""
        return [e for e in self.edges if e.status == EdgeStatus.NONADJACENT]

    @property
    def explained(self) -> list[EdgeFinding]:
        """Non-adjacent edges that a module path spells out."""
        return [e for e in self.edges if e.status == EdgeStatus.EXPLAINED]

    @property
    def relocating(self) -> list[EdgeFinding]:
        """Non-adjacent regulation of a protein that can sit next to the regulator."""
        return [e for e in self.edges if e.status == EdgeStatus.RELOCATING]

    def to_dict(self, all_rows: bool = False) -> dict[str, Any]:
        """Return a YAML-friendly dict; by default only the rows worth reading."""
        locs = self.locations if all_rows else self.unresolved
        edges = (
            self.edges
            if all_rows
            else self.nonadjacent + self.relocating + self.explained
        )
        return {
            "model": self.model_id,
            "title": self.title,
            "n_activities": len(self.locations),
            "n_causal_edges": len(self.edges),
            "n_unresolved_locations": len(self.unresolved),
            "n_nonadjacent_edges": len(self.nonadjacent),
            "n_bridged_edges": len(self.bridged),
            "n_relocating_edges": len(self.relocating),
            "n_explained_edges": len(self.explained),
            "locations": [loc.to_dict() for loc in locs],
            "edges": [e.to_dict() for e in edges],
        }


def check_model(
    model: dict[str, Any],
    cm: CompartmentModel,
    ancestors: AncestorFn,
    explainer: Optional[EdgeExplainer] = None,
    protein_locations: Optional[ProteinLocationFn] = None,
) -> ModelCompartmentReport:
    """Run compartment QC over one cached GO-CAM model (gocam-py YAML as dict).

    A non-adjacent edge is then refined, in this order:

    1. ``EXPLAINED`` when ``explainer`` finds a module path through a transport
       step between the two activities, and the step's declared locations
       (with those of any module it includes) touch both ends of the edge
       (:func:`bridge_span`). Otherwise the edge stays ``NONADJACENT`` and
       the explanation is kept with ``spans_edge: false``;
    2. ``RELOCATING`` when the edge is a direct regulation (not material flow,
       and not an indirect edge such as transcriptional control, which reaches
       its target through gene expression) and ``protein_locations`` places the
       downstream protein in a compartment the same as or adjacent to the
       upstream activity: the regulator can reach the protein, which then does
       its job elsewhere.

    >>> cm = CompartmentModel.load()
    >>> anc = {t: {t} for t in ["GO:0005829", "GO:0005576"]}
    >>> model = {
    ...     "id": "gomodel:X",
    ...     "objects": [{"id": "GO:0005829", "label": "cytosol"}],
    ...     "activities": [
    ...         {"id": "a", "enabled_by": {"term": "P1"},
    ...          "occurs_in": {"term": "GO:0005829"},
    ...          "causal_associations": [
    ...              {"predicate": "RO:0002629", "downstream_activity": "b"}]},
    ...         {"id": "b", "enabled_by": {"term": "P2"},
    ...          "occurs_in": {"term": "GO:0005576"}},
    ...     ],
    ... }
    >>> r = check_model(model, cm, lambda t: anc[t])
    >>> [(e.status.value, e.distance, e.direct) for e in r.nonadjacent]
    [('NONADJACENT', 2, True)]

    If P2 is known to occur in the plasma membrane, it can meet P1 there:

    >>> r = check_model(model, cm, lambda t: anc[t],
    ...                 protein_locations=lambda gp: frozenset({"PLASMA_MEMBRANE"}))
    >>> [(e.status.value, e.downstream_protein_compartments) for e in r.relocating]
    [('RELOCATING', ['PLASMA_MEMBRANE'])]
    """
    labels = {o["id"]: o.get("label") for o in model.get("objects") or []}
    resolutions: dict[str, Resolution] = {}
    locations: list[LocationFinding] = []
    gene_of: dict[str, Optional[str]] = {}
    for act in model.get("activities") or []:
        aid = act["id"]
        gp = (act.get("enabled_by") or {}).get("term")
        gene_of[aid] = gp
        cc = (act.get("occurs_in") or {}).get("term")
        res = cm.resolve(cc, ancestors)
        resolutions[aid] = res
        locations.append(
            LocationFinding(
                activity_id=aid,
                gene_product=gp,
                gene_label=labels.get(gp) if gp else None,
                occurs_in=cc,
                occurs_in_label=labels.get(cc) if cc else None,
                status=res.status,
                compartments=sorted(res.compartments),
                hint=res.hint,
            )
        )
    edges: list[EdgeFinding] = []
    for act in model.get("activities") or []:
        up = act["id"]
        for ca in act.get("causal_associations") or []:
            down = ca.get("downstream_activity")
            if down not in resolutions:
                continue
            pred = ca.get("predicate", "")
            plabel, direct = CAUSAL_PREDICATES.get(pred, (None, None))
            status, dist = cm.edge_status(resolutions[up], resolutions[down])
            ug, dg = gene_of.get(up), gene_of.get(down)
            kind = edge_kind(pred)
            explanation = None
            near: Optional[list[str]] = None
            if status == EdgeStatus.NONADJACENT and explainer:
                found = explainer(up, down)
                if found is not None:
                    span = bridge_span(
                        cm,
                        ancestors,
                        getattr(found, "bridge_locations", ()),
                        resolutions[up].compartments,
                        resolutions[down].compartments,
                    )
                    explanation = {**found.to_dict(), **span}
                    if span["spans_edge"]:
                        status = EdgeStatus.EXPLAINED
            if (
                status == EdgeStatus.NONADJACENT
                and kind == EdgeKind.REGULATION
                and direct
                and protein_locations
                and dg
            ):
                reachable = [
                    c
                    for c in sorted(protein_locations(dg))
                    if _within_one(cm.distance(resolutions[up].compartments, {c}))
                ]
                if reachable:
                    status = EdgeStatus.RELOCATING
                    near = reachable
            edges.append(
                EdgeFinding(
                    upstream=up,
                    upstream_label=labels.get(ug) if ug else None,
                    downstream=down,
                    downstream_label=labels.get(dg) if dg else None,
                    predicate=pred,
                    predicate_label=plabel,
                    direct=direct,
                    upstream_compartments=sorted(resolutions[up].compartments),
                    downstream_compartments=sorted(resolutions[down].compartments),
                    status=status,
                    distance=dist,
                    kind=kind,
                    explanation=explanation,
                    downstream_protein_compartments=near,
                )
            )
    return ModelCompartmentReport(
        model_id=model.get("id", ""),
        title=model.get("title"),
        locations=locations,
        edges=edges,
    )


def bridge_span(
    cm: CompartmentModel,
    ancestors: AncestorFn,
    bridge_locations: Iterable[str],
    upstream: Iterable[str],
    downstream: Iterable[str],
) -> dict[str, Any]:
    """Does a module's transport step reach the compartments at both ends of an edge?

    The bridge's declared GO locations are placed in the compartment model
    (single or coarse); the step spans the edge when they touch, or share, a
    compartment of each end. A module path through a transport step that
    happens elsewhere (say, a vesicle step offered for a plasma membrane to
    nucleus edge) does not explain the edge.

    >>> cm = CompartmentModel.load()
    >>> anc = lambda t: {t}
    >>> nuclear_import = ["GO:0005829", "GO:0005635", "GO:0005654"]
    >>> bridge_span(cm, anc, nuclear_import, {"PLASMA_MEMBRANE"},
    ...             {"NUCLEAR_ENVELOPE", "NUCLEAR_LUMEN"})["spans_edge"]
    True
    >>> golgi = ["GO:0000139"]
    >>> r = bridge_span(cm, anc, golgi, {"PLASMA_MEMBRANE"}, {"NUCLEAR_LUMEN"})
    >>> r["spans_edge"], r["bridge_compartments"]
    (False, ['GOLGI_MEMBRANE'])
    >>> bridge_span(cm, anc, [], {"CYTOSOL"}, {"EXTRACELLULAR"})["spans_edge"]
    False
    """
    comps: set[str] = set()
    for term in bridge_locations:
        res = cm.resolve(term, ancestors)
        if res.status in (
            ResolutionStatus.RESOLVED,
            ResolutionStatus.COARSE,
            ResolutionStatus.AMBIGUOUS,
        ):
            comps |= res.compartments
    up, down = set(upstream), set(downstream)
    spans = bool(comps) and all(
        _within_one(cm.distance(end, comps)) for end in (up, down) if end
    )
    return {"bridge_compartments": sorted(comps), "spans_edge": spans}


def _within_one(distance: Optional[int]) -> bool:
    """True for a known distance of 0 or 1.

    >>> _within_one(0), _within_one(1), _within_one(2), _within_one(None)
    (True, True, False, False)
    """
    return distance is not None and distance <= 1


def oak_ancestor_fn(handle: str = "sqlite:obo:go") -> AncestorFn:
    """Return a cached reflexive is_a/part_of ancestor function from an oaklib adapter."""
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A, PART_OF

    adapter = get_adapter(handle)

    @lru_cache(maxsize=None)
    def _anc(term: str) -> frozenset[str]:
        return frozenset(
            adapter.ancestors(term, predicates=[IS_A, PART_OF], reflexive=True)
        )

    return _anc


def iter_cached_models(cache_dir: Path) -> Iterator[Path]:
    """Yield cached ``<id>-src.yaml`` paths under a GO-CAM cache directory."""
    yield from sorted(cache_dir.glob("*/*-src.yaml"))


def check_cached_models(
    paths: Iterable[Path],
    ancestors: AncestorFn,
    cm: Optional[CompartmentModel] = None,
    explainer: Optional[EdgeExplainer] = None,
    protein_locations: Optional[ProteinLocationFn] = None,
) -> list[ModelCompartmentReport]:
    """Run :func:`check_model` over cached model files."""
    cm = cm or CompartmentModel.load()
    return [
        check_model(
            yaml.safe_load(p.read_text()), cm, ancestors, explainer, protein_locations
        )
        for p in paths
    ]


class ProteinLocationIndex:
    """Where gene products are known to be, from their gene folders.

    Uses the cellular-component rows of ``<GENE>-goa.tsv`` (not NOT-qualified),
    dropping any term that the gene's review rejects (REMOVE or
    MARK_AS_OVER_ANNOTATED, with no row keeping it). Each remaining term is
    placed with :meth:`CompartmentModel.resolve`; only terms that resolve to a
    single compartment count, so a broad term such as cytoplasm cannot make a
    protein look adjacent to everything. Gene products without a gene folder
    have no known location.
    """

    def __init__(self, genes_dir: Path, cm: CompartmentModel, ancestors: AncestorFn):
        self.genes_dir = genes_dir
        self.cm = cm
        self.ancestors = ancestors
        self._paths: Optional[dict[str, Path]] = None
        self._cache: dict[str, frozenset[str]] = {}

    def _goa_paths(self) -> dict[str, Path]:
        if self._paths is None:
            self._paths = {}
            for p in sorted(self.genes_dir.glob("*/*/*-goa.tsv")):
                with p.open() as fh:
                    fh.readline()
                    row = fh.readline().split("\t")
                if len(row) > 1 and row[1]:
                    self._paths.setdefault(row[1], p)
        return self._paths

    def _rejected_terms(self, goa_path: Path) -> set[str]:
        review = goa_path.with_name(
            goa_path.name.replace("-goa.tsv", "-ai-review.yaml")
        )
        if not review.exists():
            return set()
        doc = yaml.safe_load(review.read_text()) or {}
        rejected: set[str] = set()
        kept: set[str] = set()
        for ann in doc.get("existing_annotations") or []:
            tid = (ann.get("term") or {}).get("id")
            action = (ann.get("review") or {}).get("action")
            if not isinstance(tid, str) or not tid or ann.get("negated"):
                continue
            if action in REJECTING_ACTIONS:
                rejected.add(tid)
            elif action in KEEPING_ACTIONS:
                kept.add(tid)
        return rejected - kept

    def __call__(self, gene_product: str) -> frozenset[str]:
        """Return the single compartments a gene product is known to occupy."""
        acc = gene_product.split(":", 1)[-1]
        if acc in self._cache:
            return self._cache[acc]
        paths = self._goa_paths()
        # an isoform accession (P40763-1) shares its gene folder with the entry
        path = paths.get(acc) or paths.get(acc.split("-", 1)[0])
        out: set[str] = set()
        if path is not None:
            rejected = self._rejected_terms(path)
            with path.open() as fh:
                header = fh.readline().rstrip("\n").split("\t")
                col = {name: i for i, name in enumerate(header)}
                for line in fh:
                    row = line.rstrip("\n").split("\t")
                    if row[col["GO ASPECT"]] != "cellular_component":
                        continue
                    if row[col["QUALIFIER"]].startswith("NOT"):
                        continue
                    term = row[col["GO TERM"]]
                    if term in rejected:
                        continue
                    res = self.cm.resolve(term, self.ancestors)
                    if res.status == ResolutionStatus.RESOLVED:
                        out |= res.compartments
        self._cache[acc] = frozenset(out)
        return self._cache[acc]


def summarize(reports: list[ModelCompartmentReport]) -> dict[str, Any]:
    """Corpus-level counts, plus the most frequent unresolved terms."""
    unresolved_terms: dict[str, dict[str, Any]] = {}
    for r in reports:
        for loc in r.unresolved:
            key = loc.occurs_in or ""
            row = unresolved_terms.setdefault(
                key, {"term": key, "label": loc.occurs_in_label, "n_activities": 0}
            )
            row["n_activities"] += 1
    status_counts: dict[str, int] = {}
    for r in reports:
        for loc in r.locations:
            status_counts[loc.status.value] = status_counts.get(loc.status.value, 0) + 1
    edge_counts: dict[str, int] = {}
    for r in reports:
        for e in r.edges:
            edge_counts[e.status.value] = edge_counts.get(e.status.value, 0) + 1
    return {
        "n_models": len(reports),
        "n_models_with_unresolved": sum(1 for r in reports if r.unresolved),
        "n_models_with_nonadjacent": sum(1 for r in reports if r.nonadjacent),
        "n_nonadjacent_direct_edges": sum(
            1 for r in reports for e in r.nonadjacent if e.direct
        ),
        "n_models_with_relocating": sum(1 for r in reports if r.relocating),
        "n_models_with_explained": sum(1 for r in reports if r.explained),
        "location_status": dict(sorted(status_counts.items())),
        "edge_status": dict(sorted(edge_counts.items())),
        "unresolved_terms": sorted(
            unresolved_terms.values(), key=lambda x: (-x["n_activities"], x["term"])
        ),
    }
