"""Structural lint rules for GO-CAM models.

The linter reads cached ``gocam-py`` models (``gocams/<id>/<id>-src.yaml``)
and reports structural anomalies that a curator should look at. It does not
judge whether the biology is true; it finds graph shapes that are impossible,
redundant or ambiguous, so that reviews (``GoCamReview``) can start from a
short list of suspicious places.

Rules come in three kinds:

* **graph rules** need only the model itself (same-gene chains, duplicate
  activities, contradictory edges, orphans, disconnected components);
* **ontology rules** need GO (compartment topology for causal edges,
  transcription-factor edges, receptor ``has input``, generic or binding MFs);
* **corpus rules** compare models with one another (near-duplicate models).

Every finding carries a ``rule`` id, a ``severity`` and, where one fits, the
``GoCamQcFlagEnum`` value a reviewer would record. See ``docs/gocam_lint.md``.

Compartment topology
--------------------
A direct causal edge (for example ``directly positively regulates``) asserts a
single step. If the upstream activity occurs in the cytosol and the downstream
one in the extracellular region, at least one membrane-crossing step
(secretion, transport, translocation) has been left out. Each cellular
component term is mapped to the topological *spaces* it touches:

>>> sorted(faces_of_anchor("GO:0005886"))  # plasma membrane: a boundary
['C', 'E', 'P']
>>> sorted(faces_of_anchor("GO:0005829"))  # cytosol
['C']

Two activities can be linked by a direct edge only if their face sets
intersect:

>>> classify_crossing(frozenset({"C"}), frozenset({"E"}))
'ERROR'
>>> classify_crossing(frozenset({"C"}), frozenset({"C", "E", "P"})) is None
True
>>> classify_crossing(frozenset({"L"}), frozenset({"E"}))
'INFO'
"""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Callable, Iterable, Iterator, Optional, Protocol

import yaml
from gocam.datamodel import Activity, Model

# ---------------------------------------------------------------------------
# Relations
# ---------------------------------------------------------------------------

#: Causal predicates that assert a single, direct step.
DIRECT_PREDICATES: dict[str, str] = {
    "RO:0002629": "directly positively regulates",
    "RO:0002630": "directly negatively regulates",
    "RO:0002413": "directly provides input for",
    "RO:0012010": "removes input for",
    "RO:0012009": "constitutively upstream of",
}

#: Causal predicates with a positive sign.
POSITIVE_PREDICATES: frozenset[str] = frozenset(
    {"RO:0002629", "RO:0002407", "RO:0002304", "RO:0002213"}
)

#: Causal predicates with a negative sign.
NEGATIVE_PREDICATES: frozenset[str] = frozenset(
    {"RO:0002630", "RO:0002409", "RO:0002305", "RO:0002212", "RO:0012010"}
)

#: Regulation predicates (signed, direct) used by the transcription rule.
DIRECT_REGULATION_PREDICATES: frozenset[str] = frozenset({"RO:0002629", "RO:0002630"})

HAS_INPUT = "RO:0002233"
HAS_OUTPUT = "RO:0002234"

# ---------------------------------------------------------------------------
# Compartment topology
# ---------------------------------------------------------------------------

#: Topological spaces. C = cytosolic space (cytosol and nucleus, joined by
#: nuclear pores); E = extracellular; P = periplasm; L = lumen of the secretory
#: and endocytic system (topologically outside); M = mitochondrial matrix;
#: I = mitochondrial intermembrane space; X = peroxisomal matrix;
#: S = plastid stroma; T = thylakoid lumen.
SPACE_LABELS: dict[str, str] = {
    "C": "cytosolic space",
    "E": "extracellular",
    "P": "periplasm",
    "L": "secretory/endocytic lumen",
    "M": "mitochondrial matrix",
    "I": "mitochondrial intermembrane space",
    "X": "peroxisomal matrix",
    "S": "plastid stroma",
    "T": "thylakoid lumen",
}

_INTRACELLULAR = frozenset({"C", "M", "I", "L", "X", "S", "T"})

#: Anchor cellular-component terms -> (label, faces). A membrane touches both
#: of its sides; an organelle root touches its outside and all its insides;
#: a generic intracellular term touches every intracellular space.
COMPARTMENT_ANCHORS: dict[str, tuple[str, frozenset[str]]] = {
    "GO:0005576": ("extracellular region", frozenset({"E"})),
    "GO:0005618": ("cell wall", frozenset({"E"})),
    "GO:0009986": ("cell surface", frozenset({"C", "E"})),
    "GO:0005886": ("plasma membrane", frozenset({"C", "E", "P"})),
    "GO:0009897": ("external side of plasma membrane", frozenset({"E", "P"})),
    "GO:0098562": ("cytoplasmic side of membrane", frozenset({"C"})),
    "GO:0042597": ("periplasmic space", frozenset({"P"})),
    "GO:0009279": ("cell outer membrane", frozenset({"P", "E"})),
    "GO:0005829": ("cytosol", frozenset({"C"})),
    "GO:0005634": ("nucleus", frozenset({"C"})),
    "GO:0005694": ("chromosome", frozenset({"C"})),
    "GO:0005737": ("cytoplasm", _INTRACELLULAR),
    "GO:0005622": ("intracellular anatomical structure", _INTRACELLULAR),
    "GO:0005739": ("mitochondrion", frozenset({"C", "I", "M"})),
    "GO:0005741": ("mitochondrial outer membrane", frozenset({"C", "I"})),
    "GO:0005758": ("mitochondrial intermembrane space", frozenset({"I"})),
    "GO:0005743": ("mitochondrial inner membrane", frozenset({"I", "M"})),
    "GO:0005759": ("mitochondrial matrix", frozenset({"M"})),
    "GO:0005783": ("endoplasmic reticulum", frozenset({"C", "L"})),
    "GO:0005789": ("endoplasmic reticulum membrane", frozenset({"C", "L"})),
    "GO:0005788": ("endoplasmic reticulum lumen", frozenset({"L"})),
    "GO:0005794": ("Golgi apparatus", frozenset({"C", "L"})),
    "GO:0000139": ("Golgi membrane", frozenset({"C", "L"})),
    "GO:0005796": ("Golgi lumen", frozenset({"L"})),
    "GO:0005768": ("endosome", frozenset({"C", "L"})),
    "GO:0010008": ("endosome membrane", frozenset({"C", "L"})),
    "GO:0031904": ("endosome lumen", frozenset({"L"})),
    "GO:0005764": ("lysosome", frozenset({"C", "L"})),
    "GO:0005765": ("lysosomal membrane", frozenset({"C", "L"})),
    "GO:0043202": ("lysosomal lumen", frozenset({"L"})),
    "GO:0005773": ("vacuole", frozenset({"C", "L"})),
    "GO:0005774": ("vacuolar membrane", frozenset({"C", "L"})),
    "GO:0005775": ("vacuolar lumen", frozenset({"L"})),
    "GO:0031410": ("cytoplasmic vesicle", frozenset({"C", "L"})),
    "GO:0030659": ("cytoplasmic vesicle membrane", frozenset({"C", "L"})),
    "GO:0031983": ("vesicle lumen", frozenset({"L"})),
    "GO:0005777": ("peroxisome", frozenset({"C", "X"})),
    "GO:0005778": ("peroxisomal membrane", frozenset({"C", "X"})),
    "GO:0005782": ("peroxisomal matrix", frozenset({"X"})),
    "GO:0009507": ("chloroplast", frozenset({"C", "S", "T"})),
    "GO:0009941": ("chloroplast envelope", frozenset({"C", "S"})),
    "GO:0009570": ("chloroplast stroma", frozenset({"S"})),
    "GO:0009535": ("chloroplast thylakoid membrane", frozenset({"S", "T"})),
    "GO:0031977": ("thylakoid lumen", frozenset({"T"})),
}

#: Generic intracellular anchors. They only apply when no more specific anchor
#: matches: ``microvillus membrane`` is part_of the actin cytoskeleton, hence
#: intracellular, but it is a plasma membrane region.
WEAK_ANCHORS: frozenset[str] = frozenset({"GO:0005737", "GO:0005622"})

#: Terms under these roots describe a host cell of a symbiont; a symbiont
#: effector reaching them crosses organisms, which the topology does not model.
HOST_ROOTS: frozenset[str] = frozenset({"GO:0018995"})


def faces_of_anchor(anchor_id: str) -> frozenset[str]:
    """Return the topological faces of a compartment anchor term.

    >>> sorted(faces_of_anchor("GO:0005743"))
    ['I', 'M']
    """
    return COMPARTMENT_ANCHORS[anchor_id][1]


def faces_from_ancestors(term_id: str, ancestors: Iterable[str]) -> Optional[frozenset[str]]:
    """Compute faces for a term from its reflexive is_a/part_of ancestors.

    The most specific matching anchors win (an anchor is dropped when another
    matched anchor has it as an ancestor, which callers signal by listing it in
    that anchor's ancestors). The faces of the remaining anchors are
    intersected, so ``cytoplasmic side of ER membrane`` (anchors: cytoplasmic
    side of membrane, ER membrane) resolves to the cytosolic face only. Returns
    None for host-cell terms and for terms with no anchor (``membrane``,
    ``cell``, protein complexes), which the crossing rule then skips.

    >>> faces_from_ancestors("GO:0005759", ["GO:0005759", "GO:0005739", "GO:0005737"])
    frozenset({'M'})
    >>> faces_from_ancestors("GO:0016020", ["GO:0016020"]) is None
    True
    """
    anc = set(ancestors) | {term_id}
    if anc & HOST_ROOTS:
        return None
    matched = [a for a in COMPARTMENT_ANCHORS if a in anc]
    if not matched:
        return None
    if any(a not in WEAK_ANCHORS for a in matched):
        matched = [a for a in matched if a not in WEAK_ANCHORS]
    minimal = [a for a in matched if not any(_anchor_above(b, a) for b in matched if b != a)]
    faces = frozenset.intersection(*(faces_of_anchor(a) for a in minimal))
    if not faces:
        faces = frozenset.union(*(faces_of_anchor(a) for a in minimal))
    return faces


#: Static partial order among anchors (anchor -> anchors that are its
#: is_a/part_of ancestors), generated from GO so that face resolution does not
#: depend on the ontology version at run time. test_anchor_parents_match_go
#: checks it against the current GO build.
_ANCHOR_PARENTS: dict[str, frozenset[str]] = {
    "GO:0005618": frozenset({"GO:0005576"}),  # cell wall
    "GO:0009897": frozenset({"GO:0005886", "GO:0009986"}),  # external side of plasma membrane
    "GO:0042597": frozenset({"GO:0005576"}),  # periplasmic space
    "GO:0009279": frozenset({"GO:0005576"}),  # cell outer membrane
    "GO:0005829": frozenset({"GO:0005622", "GO:0005737"}),  # cytosol
    "GO:0005634": frozenset({"GO:0005622"}),  # nucleus
    "GO:0005694": frozenset({"GO:0005622"}),  # chromosome
    "GO:0005737": frozenset({"GO:0005622"}),  # cytoplasm
    "GO:0005739": frozenset({"GO:0005622", "GO:0005737"}),  # mitochondrion
    "GO:0005741": frozenset({"GO:0005622", "GO:0005737", "GO:0005739"}),  # mitochondrial outer membrane
    "GO:0005758": frozenset({"GO:0005622", "GO:0005737", "GO:0005739"}),  # mitochondrial intermembrane space
    "GO:0005743": frozenset({"GO:0005622", "GO:0005737", "GO:0005739"}),  # mitochondrial inner membrane
    "GO:0005759": frozenset({"GO:0005622", "GO:0005737", "GO:0005739"}),  # mitochondrial matrix
    "GO:0005783": frozenset({"GO:0005622", "GO:0005737"}),  # endoplasmic reticulum
    "GO:0005789": frozenset({"GO:0005622", "GO:0005737", "GO:0005783"}),  # endoplasmic reticulum membrane
    "GO:0005788": frozenset({"GO:0005622", "GO:0005737", "GO:0005783"}),  # endoplasmic reticulum lumen
    "GO:0005794": frozenset({"GO:0005622", "GO:0005737"}),  # Golgi apparatus
    "GO:0000139": frozenset({"GO:0005622", "GO:0005737", "GO:0005794"}),  # Golgi membrane
    "GO:0005796": frozenset({"GO:0005622", "GO:0005737", "GO:0005794"}),  # Golgi lumen
    "GO:0005768": frozenset({"GO:0005622", "GO:0005737", "GO:0031410"}),  # endosome
    "GO:0010008": frozenset({"GO:0005622", "GO:0005737", "GO:0005768", "GO:0030659", "GO:0031410"}),  # endosome membrane
    "GO:0031904": frozenset({"GO:0005622", "GO:0005737", "GO:0005768", "GO:0031410"}),  # endosome lumen
    "GO:0005764": frozenset({"GO:0005622", "GO:0005737", "GO:0005773"}),  # lysosome
    "GO:0005765": frozenset({"GO:0005622", "GO:0005737", "GO:0005764", "GO:0005773", "GO:0005774"}),  # lysosomal membrane
    "GO:0043202": frozenset({"GO:0005622", "GO:0005737", "GO:0005764", "GO:0005773", "GO:0005775"}),  # lysosomal lumen
    "GO:0005773": frozenset({"GO:0005622", "GO:0005737"}),  # vacuole
    "GO:0005774": frozenset({"GO:0005622", "GO:0005737", "GO:0005773"}),  # vacuolar membrane
    "GO:0005775": frozenset({"GO:0005622", "GO:0005737", "GO:0005773"}),  # vacuolar lumen
    "GO:0031410": frozenset({"GO:0005622", "GO:0005737"}),  # cytoplasmic vesicle
    "GO:0030659": frozenset({"GO:0005622", "GO:0005737", "GO:0031410"}),  # cytoplasmic vesicle membrane
    "GO:0005777": frozenset({"GO:0005622", "GO:0005737"}),  # peroxisome
    "GO:0005778": frozenset({"GO:0005622", "GO:0005737", "GO:0005777"}),  # peroxisomal membrane
    "GO:0005782": frozenset({"GO:0005622", "GO:0005737", "GO:0005777"}),  # peroxisomal matrix
    "GO:0009507": frozenset({"GO:0005622", "GO:0005737"}),  # chloroplast
    "GO:0009941": frozenset({"GO:0005622", "GO:0005737", "GO:0009507"}),  # chloroplast envelope
    "GO:0009570": frozenset({"GO:0005622", "GO:0005737", "GO:0009507"}),  # chloroplast stroma
    "GO:0009535": frozenset({"GO:0005622", "GO:0005737", "GO:0009507"}),  # chloroplast thylakoid membrane
    "GO:0031977": frozenset({"GO:0005622"}),  # thylakoid lumen
}


def _anchor_above(lower: str, upper: str) -> bool:
    """True if anchor ``upper`` is an ancestor of anchor ``lower``.

    >>> _anchor_above("GO:0005759", "GO:0005739")
    True
    >>> _anchor_above("GO:0005739", "GO:0005759")
    False
    """
    return upper in _ANCHOR_PARENTS.get(lower, frozenset())


#: Severity for a direct edge between two disjoint face sets, by the pair of
#: spaces involved. Interior <-> exterior is impossible as one step; lumen <->
#: extracellular is topologically continuous (vesicular traffic) and only noted.
def classify_crossing(up: frozenset[str], down: frozenset[str]) -> Optional[str]:
    """Return the severity of a direct edge between two face sets, or None.

    The least severe pairing of faces decides: an ER or Golgi activity
    (faces C and L) acting on an extracellular one is lumen-to-outside,
    which is topologically continuous.

    >>> classify_crossing(frozenset({"C"}), frozenset({"M"}))
    'WARNING'
    >>> classify_crossing(frozenset({"C", "L"}), frozenset({"E"}))
    'INFO'
    """
    if up & down:
        return None
    return min((_pair_severity(u, d) for u in up for d in down), key=lambda s: SEVERITY_RANK[s])


SEVERITY_RANK = {"INFO": 0, "WARNING": 1, "ERROR": 2}
_OUTSIDE = frozenset({"E", "P"})
_TOPOLOGICALLY_OUTSIDE = frozenset({"E", "P", "L"})


def _pair_severity(u: str, d: str) -> str:
    """Severity of a direct step from space ``u`` to a different space ``d``.

    >>> _pair_severity("C", "E"), _pair_severity("M", "C"), _pair_severity("L", "E")
    ('ERROR', 'WARNING', 'INFO')
    """
    pair = {u, d}
    if pair <= _TOPOLOGICALLY_OUTSIDE:
        return "INFO"
    if pair & _OUTSIDE and pair & (_INTRACELLULAR - {"L"}):
        return "ERROR"
    return "WARNING"


# ---------------------------------------------------------------------------
# Ontology access
# ---------------------------------------------------------------------------


class TermOracle(Protocol):
    """Minimal ontology interface the ontology rules need."""

    def ancestors(self, term_id: str) -> frozenset[str]:
        """Reflexive is_a/part_of ancestors."""
        ...

    def is_a_ancestors(self, term_id: str) -> frozenset[str]:
        """Reflexive is_a-only ancestors."""
        ...

    def label(self, term_id: str) -> str:
        """Term label, or the id itself if unknown."""
        ...


@dataclass
class OakOracle:
    """TermOracle backed by an oaklib adapter (default: GO SQLite build).

    The first use downloads ``sqlite:obo:go`` (~300 MB compressed) into the
    oaklib cache.
    """

    selector: str = "sqlite:obo:go"
    _adapter: object = field(default=None, init=False, repr=False)

    def _get(self):  # noqa: ANN202 - oaklib adapter type
        if self._adapter is None:
            from oaklib import get_adapter

            self._adapter = get_adapter(self.selector)
        return self._adapter

    @lru_cache(maxsize=None)  # noqa: B019 - oracle lives for the whole run
    def ancestors(self, term_id: str) -> frozenset[str]:
        from oaklib.datamodels.vocabulary import IS_A, PART_OF

        return frozenset(self._get().ancestors(term_id, [IS_A, PART_OF])) | {term_id}

    @lru_cache(maxsize=None)  # noqa: B019
    def is_a_ancestors(self, term_id: str) -> frozenset[str]:
        from oaklib.datamodels.vocabulary import IS_A

        return frozenset(self._get().ancestors(term_id, [IS_A])) | {term_id}

    @lru_cache(maxsize=None)  # noqa: B019
    def label(self, term_id: str) -> str:
        return self._get().label(term_id) or term_id

    def __hash__(self) -> int:
        return hash(self.selector)


# ---------------------------------------------------------------------------
# Model view
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    """A causal edge between two activities of one model."""

    source: str
    predicate: str
    target: str
    has_evidence: bool
    references: frozenset[str] = frozenset()


@dataclass
class ModelView:
    """Indexed, read-only view of a GO-CAM model for rule evaluation."""

    model: Model
    activities: dict[str, Activity]
    edges: list[Edge]
    labels: dict[str, str]

    @classmethod
    def from_model(cls, model: Model) -> "ModelView":
        """Index a gocam-py model."""
        acts = {a.id: a for a in (model.activities or [])}
        edges = [
            Edge(a.id, c.predicate, c.downstream_activity, bool(c.evidence),
                 frozenset(ev.reference for ev in (c.evidence or []) if ev.reference))
            for a in acts.values()
            for c in (a.causal_associations or [])
            if c.downstream_activity in acts
        ]
        labels = {o.id: (o.label or o.id) for o in (model.objects or [])}
        return cls(model=model, activities=acts, edges=edges, labels=labels)

    @property
    def model_id(self) -> str:
        """Bare model id."""
        return self.model.id.split(":")[-1]

    def gene(self, act_id: str) -> Optional[str]:
        """Enabler (gene product or complex) of an activity."""
        eb = self.activities[act_id].enabled_by
        return eb.term if eb else None

    def mf(self, act_id: str) -> Optional[str]:
        """Molecular function term of an activity."""
        mf = self.activities[act_id].molecular_function
        return mf.term if mf else None

    def cc(self, act_id: str) -> Optional[str]:
        """occurs_in term of an activity."""
        oc = self.activities[act_id].occurs_in
        return oc.term if oc else None

    def bp(self, act_id: str) -> Optional[str]:
        """part_of term of an activity."""
        po = self.activities[act_id].part_of
        return po.term if po else None

    def molecules(self, act_id: str, predicate: str) -> list[str]:
        """Terms of the molecules linked to an activity by ``predicate``."""
        mol_terms = {m.id: m.term for m in (self.model.molecules or [])}
        return [
            mol_terms.get(ma.molecule, ma.molecule)
            for ma in self.activities[act_id].molecular_associations or []
            if ma.predicate == predicate
        ]

    def has_inputs(self, act_id: str) -> list[str]:
        """Terms of the molecules an activity has as input."""
        return self.molecules(act_id, HAS_INPUT)

    def flow_pairs(self) -> list[tuple[str, str]]:
        """Activity pairs linked by a causal edge or by molecule flow.

        Metabolic models often chain steps only through a shared metabolite
        (A has output X, B has input X), so connectivity rules count both.
        """
        pairs = [(e.source, e.target) for e in self.edges]
        producers: dict[str, set[str]] = defaultdict(set)
        for a in self.activities:
            for m in self.molecules(a, HAS_OUTPUT):
                producers[m].add(a)
        for b in self.activities:
            for m in self.has_inputs(b):
                pairs.extend((a, b) for a in producers.get(m, ()) if a != b)
        return pairs

    @property
    def is_gene_centric(self) -> bool:
        """True when every activity is enabled by one gene product.

        Such models (e.g. MGI/SGD gene-centric imports) list one gene's
        activities and are not expected to be connected.
        """
        return len({self.gene(a) for a in self.activities}) <= 1

    def enabled_by_references(self, act_id: str) -> frozenset[str]:
        """References supporting the enabled_by of an activity."""
        eb = self.activities[act_id].enabled_by
        return frozenset(ev.reference for ev in ((eb.evidence if eb else None) or []) if ev.reference)

    def label(self, term: Optional[str]) -> str:
        """Model-local label for a term."""
        return self.labels.get(term or "", term or "-")

    def describe(self, act_id: str) -> str:
        """Short human description of an activity."""
        return f"{self.label(self.gene(act_id))} {self.label(self.mf(act_id))}"


# ---------------------------------------------------------------------------
# Findings and rule registry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Finding:
    """One lint finding."""

    rule: str
    severity: str
    model_id: str
    message: str
    activity_ids: tuple[str, ...] = ()
    qc_flag: Optional[str] = None


RuleFn = Callable[[ModelView, Optional[TermOracle]], Iterator[Finding]]


@dataclass(frozen=True)
class Rule:
    """A registered model-level rule."""

    id: str
    description: str
    needs_ontology: bool
    fn: RuleFn


RULES: dict[str, Rule] = {}


def rule(rule_id: str, description: str, needs_ontology: bool = False):
    """Register a model-level rule function."""

    def deco(fn: RuleFn) -> RuleFn:
        RULES[rule_id] = Rule(rule_id, description, needs_ontology, fn)
        return fn

    return deco


def _f(view: ModelView, rule_id: str, severity: str, message: str,
       acts: Iterable[str] = (), qc_flag: Optional[str] = None) -> Finding:
    return Finding(rule_id, severity, view.model_id, message, tuple(acts), qc_flag)


# --- graph rules -----------------------------------------------------------


@rule("contradictory_edges", "Same activity pair linked with both a positive and a negative edge.")
def contradictory_edges(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Same source and target with opposite-sign predicates."""
    by_pair: dict[tuple[str, str], set[str]] = defaultdict(set)
    for e in view.edges:
        by_pair[(e.source, e.target)].add(e.predicate)
    for (s, t), preds in by_pair.items():
        if preds & POSITIVE_PREDICATES and preds & NEGATIVE_PREDICATES:
            yield _f(view, "contradictory_edges", "WARNING",
                     f"{view.describe(s)} -> {view.describe(t)} is both positive and negative",
                     (s, t))


@rule("self_loop", "Activity causally linked to itself.")
def self_loop(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """An edge whose source and target are the same activity."""
    for e in view.edges:
        if e.source == e.target:
            yield _f(view, "self_loop", "WARNING",
                     f"{view.describe(e.source)} regulates itself ({e.predicate})", (e.source,))


@rule("same_gene_chain", "Causally chained activities enabled by the same gene product.")
def same_gene_chain(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """Maximal runs of activities of one gene product joined by causal edges.

    Repeats with different MFs may encode activation states or distinct
    steps (INFO); repeats with the same MF and location are redundant
    (WARNING). Repeats in different compartments usually encode translocation.
    """
    groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for e in view.edges:
        g = view.gene(e.source)
        if g and g == view.gene(e.target) and e.source != e.target:
            groups[g].append((e.source, e.target))
    for g, pairs in groups.items():
        for comp in _components({a for p in pairs for a in p}, pairs):
            mfs = {view.mf(a) for a in comp}
            ccs = {view.cc(a) for a in comp}
            redundant = len(mfs) < len(comp) and len(ccs) == 1
            sev = "WARNING" if redundant else "INFO"
            why = ("repeated MF in one location" if redundant else
                   f"{len(mfs)} distinct MFs, {len(ccs)} locations")
            yield _f(view, "same_gene_chain", sev,
                     f"{view.label(g)} appears as a chain of {len(comp)} activities ({why})",
                     sorted(comp))


@rule("duplicate_activity", "Same gene product and MF in more than one activity node.")
def duplicate_activity(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Pseudo-duplicate nodes: same enabler and MF.

    Fully identical annotons (same occurs_in and part_of) are WARNING; ones
    differing only in context are INFO (they often encode a state the model
    cannot otherwise express).
    """
    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for a in view.activities:
        g, m = view.gene(a), view.mf(a)
        if g and m:
            groups[(g, m)].append(a)
    for (g, m), acts in groups.items():
        if len(acts) < 2:
            continue
        ctx = {(view.cc(a), view.bp(a)) for a in acts}
        sev = "WARNING" if len(ctx) == 1 else "INFO"
        yield _f(view, "duplicate_activity", sev,
                 f"{view.label(g)} {view.label(m)} occurs {len(acts)} times"
                 + (" with identical context" if len(ctx) == 1 else " in different contexts"),
                 sorted(acts))


@rule("opposite_sign_fanout",
      "One activity positively regulates one node of a gene and negatively another node of it.")
def opposite_sign_fanout(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Opposite-sign edges from one source to two copies of the same gene."""
    out: dict[str, list[Edge]] = defaultdict(list)
    for e in view.edges:
        out[e.source].append(e)
    for s, es in out.items():
        pos = [e for e in es if e.predicate in POSITIVE_PREDICATES]
        neg = [e for e in es if e.predicate in NEGATIVE_PREDICATES]
        for p, n in itertools.product(pos, neg):
            if p.target != n.target and view.gene(p.target) and view.gene(p.target) == view.gene(n.target):
                yield _f(view, "opposite_sign_fanout", "WARNING",
                         f"{view.describe(s)} activates one {view.label(view.gene(p.target))} node "
                         "and inhibits another",
                         (s, p.target, n.target))


@rule("orphan_activity", "Activity with no causal edges in a multi-activity model.")
def orphan_activity(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Activities not touched by any causal edge."""
    if len(view.activities) < 2 or view.is_gene_centric:
        return
    touched = {a for pair in view.flow_pairs() for a in pair}
    for a in view.activities:
        if a not in touched:
            yield _f(view, "orphan_activity", "WARNING",
                     f"{view.describe(a)} has no causal edges", (a,), "ORPHAN_ACTIVITY")


@rule("disconnected_components", "Model splits into several causal components.")
def disconnected_components(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Several non-trivial components; isomorphic gene sets suggest a choice or variants."""
    if view.is_gene_centric:
        return
    comps = [c for c in _components(set(view.activities), view.flow_pairs()) if len(c) > 1]
    if len(comps) < 2:
        return
    gene_sets = [{view.gene(a) for a in c} for c in comps]
    parallel = any(
        len(x & y) / len(x | y) >= 0.5 for x, y in itertools.combinations(gene_sets, 2)
    )
    if parallel:
        yield _f(view, "disconnected_components", "WARNING",
                 f"{len(comps)} components, of which some repeat the same genes "
                 "(possible switch/choice or variant paths)",
                 sorted(a for c in comps for a in c))
    else:
        yield _f(view, "disconnected_components", "INFO",
                 f"{len(comps)} disconnected causal components",
                 sorted(a for c in comps for a in c))


@rule("duplicate_edge", "Same causal edge asserted more than once.")
def duplicate_edge(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Identical (source, predicate, target) triples.

    These usually carry different evidence bundles (merged curation), so they
    are noted rather than warned about.
    """
    counts = Counter((e.source, e.predicate, e.target) for e in view.edges)
    for (s, p, t), n in counts.items():
        if n > 1:
            yield _f(view, "duplicate_edge", "INFO",
                     f"{view.describe(s)} -> {view.describe(t)} asserted {n} times ({p})", (s, t))


@rule("edge_evidence_copied",
      "Causal edge cites exactly the references of its upstream enabled_by.")
def edge_evidence_copied(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Edge evidence that merely repeats the evidence for the upstream gene product.

    A paper that shows a protein has an activity rarely also shows that the
    activity regulates the next one; identical reference sets suggest the
    edge was evidenced by copying.
    """
    for e in view.edges:
        eb_refs = view.enabled_by_references(e.source)
        if e.references and len(e.references) > 1 and e.references == eb_refs:
            yield _f(view, "edge_evidence_copied", "INFO",
                     f"{view.describe(e.source)} -> {view.describe(e.target)} cites the same "
                     f"{len(e.references)} references as the upstream enabled_by",
                     (e.source, e.target))


@rule("missing_evidence", "Causal edge with no evidence.")
def missing_evidence(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Causal edges lacking any evidence."""
    for e in view.edges:
        if not e.has_evidence:
            yield _f(view, "missing_evidence", "WARNING",
                     f"{view.describe(e.source)} -> {view.describe(e.target)} has no evidence",
                     (e.source, e.target), "MISSING_EVIDENCE")


@rule("missing_location", "Activity with no occurs_in.")
def missing_location(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Activities without a location."""
    for a in view.activities:
        if view.cc(a) is None:
            yield _f(view, "missing_location", "INFO", f"{view.describe(a)} has no occurs_in",
                     (a,), "MISSING_LOCATION")


@rule("small_model", "Model with two or fewer activities.")
def small_model(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """Very small models carry little causal structure."""
    n = len(view.activities)
    if n <= 2:
        yield _f(view, "small_model", "INFO", f"model has {n} activit{'y' if n == 1 else 'ies'}")


@rule("no_narrative", "Model has no curator comment beyond automated changes.")
def no_narrative(view: ModelView, _o: Optional[TermOracle]) -> Iterator[Finding]:
    """No free-text comment to explain the model's intent."""
    comments = [c for c in (view.model.comments or []) if not c.startswith("Automated change")]
    if not comments:
        yield _f(view, "no_narrative", "INFO", "no curator comment explains the model")


# --- ontology rules --------------------------------------------------------


@rule("compartment_crossing",
      "Direct causal edge between activities in topologically separated compartments.",
      needs_ontology=True)
def compartment_crossing(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """A one-step edge whose two activities are on opposite sides of a membrane."""
    assert oracle is not None
    for e in view.edges:
        if e.predicate not in DIRECT_PREDICATES:
            continue
        up_cc, down_cc = view.cc(e.source), view.cc(e.target)
        if not up_cc or not down_cc:
            continue
        up = faces_from_ancestors(up_cc, oracle.ancestors(up_cc))
        down = faces_from_ancestors(down_cc, oracle.ancestors(down_cc))
        if up is None or down is None:
            continue
        sev = classify_crossing(up, down)
        if sev == "WARNING" and e.predicate in METABOLITE_FLOW_PREDICATES and (up | down) <= _PORIN_PERMEABLE:
            sev = "INFO"  # small molecules cross the outer mitochondrial membrane via porins
        if sev:
            yield _f(view, "compartment_crossing", sev,
                     f"{view.describe(e.source)} [{oracle.label(up_cc)}] "
                     f"{DIRECT_PREDICATES[e.predicate]} {view.describe(e.target)} "
                     f"[{oracle.label(down_cc)}]: no membrane-crossing step",
                     (e.source, e.target), "DIRECT_VS_INDIRECT_CAUSAL")


#: Predicates that pass a metabolite from one activity to the next.
METABOLITE_FLOW_PREDICATES: frozenset[str] = frozenset({"RO:0002413", "RO:0012009"})

#: Spaces joined for small molecules by porins in the outer mitochondrial membrane.
_PORIN_PERMEABLE = frozenset({"C", "I"})

#: DNA-binding transcription factors act on other proteins through expression.
#: Co-regulators (the rest of GO:0140110) recruit cofactors directly, so they
#: are not checked as upstream activities.
DNA_BINDING_TF = "GO:0003700"
TF_ROOTS = frozenset({DNA_BINDING_TF, "GO:0140110"})


@rule("transcription_direct_edge",
      "Transcription regulator directly regulates a non-transcriptional activity.",
      needs_ontology=True)
def transcription_direct_edge(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """A TF acts on another protein's activity through its expression: indirect.

    WARNING when the model itself names the downstream gene as the TF's input
    (a target gene); INFO otherwise, since a regulator may also act directly on
    transcription machinery or recruit a cofactor.
    """
    assert oracle is not None
    for e in view.edges:
        if e.predicate not in DIRECT_REGULATION_PREDICATES:
            continue
        up_mf, down_mf = view.mf(e.source), view.mf(e.target)
        if not up_mf or not down_mf or view.gene(e.source) == view.gene(e.target):
            continue
        if DNA_BINDING_TF in oracle.is_a_ancestors(up_mf) and not oracle.is_a_ancestors(down_mf) & TF_ROOTS:
            target = view.gene(e.target) in view.has_inputs(e.source)
            yield _f(view, "transcription_direct_edge", "WARNING" if target else "INFO",
                     f"{view.describe(e.source)} {DIRECT_PREDICATES[e.predicate]} "
                     f"{view.describe(e.target)}; a transcription regulator acts through expression",
                     (e.source, e.target), "DIRECT_VS_INDIRECT_CAUSAL")


RECEPTOR_ROOT = "GO:0038023"


@rule("receptor_ligand_input",
      "Receptor has as input the gene product of an upstream (ligand) activity.",
      needs_ontology=True)
def receptor_ligand_input(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """Ligands belong upstream on a causal edge, not as a receptor's input."""
    assert oracle is not None
    upstream: dict[str, set[str]] = defaultdict(set)
    for e in view.edges:
        g = view.gene(e.source)
        if g:
            upstream[e.target].add(g)
    for a in view.activities:
        mf = view.mf(a)
        if not mf or RECEPTOR_ROOT not in oracle.is_a_ancestors(mf):
            continue
        for inp in view.has_inputs(a):
            if inp in upstream[a]:
                yield _f(view, "receptor_ligand_input", "WARNING",
                         f"{view.describe(a)} has input {view.label(inp)}, which acts upstream of it",
                         (a,), "HAS_INPUT_MISUSE")


#: MF terms too general to say what a gene product does.
GENERIC_MFS: frozenset[str] = frozenset({
    "GO:0003674", "GO:0003824", "GO:0005488", "GO:0016301", "GO:0016787",
    "GO:0016740", "GO:0140096", "GO:0098772", "GO:0060089",
})


@rule("generic_mf", "Molecular function is a generic grouping term.", needs_ontology=True)
def generic_mf(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """Generic MFs (kinase activity, catalytic activity, binding...)."""
    assert oracle is not None
    for a in view.activities:
        mf = view.mf(a)
        if mf in GENERIC_MFS:
            yield _f(view, "generic_mf", "WARNING",
                     f"{view.label(view.gene(a))} is typed {oracle.label(mf)}", (a,), "GENERIC_MF")


BINDING_ROOT = "GO:0005488"


@rule("binding_mf", "Molecular function is a binding term.", needs_ontology=True)
def binding_mf(view: ModelView, oracle: Optional[TermOracle]) -> Iterator[Finding]:
    """Binding MFs do not say what the binding achieves (protein binding is WARNING)."""
    assert oracle is not None
    for a in view.activities:
        mf = view.mf(a)
        if not mf or mf in GENERIC_MFS or BINDING_ROOT not in oracle.is_a_ancestors(mf):
            continue
        sev = "WARNING" if mf == "GO:0005515" else "INFO"
        yield _f(view, "binding_mf", sev,
                 f"{view.label(view.gene(a))} is typed {oracle.label(mf)}", (a,),
                 "BINDING_AS_FUNCTION")


# ---------------------------------------------------------------------------
# Corpus rule
# ---------------------------------------------------------------------------


def near_duplicate_models(views: list[ModelView], threshold: float = 0.6,
                          min_shared: int = 2) -> Iterator[Finding]:
    """Pairs of models whose (gene, MF) activity signatures largely overlap.

    Uses Jaccard similarity over the set of (enabler, MF) pairs, compared only
    between models sharing at least ``min_shared`` pairs. Cloned variant paths
    and fragmentations of one paper across models show up here.
    """
    sigs = {v.model_id: frozenset((v.gene(a), v.mf(a)) for a in v.activities) for v in views}
    index: dict[tuple, set[str]] = defaultdict(set)
    for mid, s in sigs.items():
        for item in s:
            index[item].add(mid)
    seen: set[tuple[str, str]] = set()
    for mid, s in sigs.items():
        shared = Counter(o for item in s for o in index[item] if o != mid)
        for other, n in shared.items():
            first, second = sorted((mid, other))
            pair = (first, second)
            if n < min_shared or pair in seen:
                continue
            seen.add(pair)
            jac = n / len(s | sigs[other])
            if jac >= threshold:
                yield Finding("near_duplicate_models", "INFO", pair[0],
                              f"shares {n} (gene, MF) activities with {pair[1]} (Jaccard {jac:.2f})",
                              (), None)


# ---------------------------------------------------------------------------
# Running
# ---------------------------------------------------------------------------


def _components(nodes: set[str], pairs: Iterable[tuple[str, str]]) -> list[set[str]]:
    """Weakly connected components.

    >>> sorted(map(sorted, _components({"a", "b", "c"}, [("a", "b")])))
    [['a', 'b'], ['c']]
    """
    parent = {n: n for n in nodes}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in pairs:
        if a in parent and b in parent:
            parent[find(a)] = find(b)
    comps: dict[str, set[str]] = defaultdict(set)
    for n in nodes:
        comps[find(n)].add(n)
    return list(comps.values())


def load_model(path: Path) -> Model:
    """Load a cached ``-src.yaml`` with the C YAML loader."""
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    return Model(**yaml.load(path.read_text(), Loader=loader))


def lint_model(model: Model, oracle: Optional[TermOracle] = None,
               rules: Optional[Iterable[str]] = None) -> list[Finding]:
    """Run model-level rules; ontology rules are skipped without an oracle."""
    view = ModelView.from_model(model)
    selected = [RULES[r] for r in rules] if rules else list(RULES.values())
    out: list[Finding] = []
    for r in selected:
        if r.needs_ontology and oracle is None:
            continue
        out.extend(r.fn(view, oracle))
    return out


def lint_paths(paths: Iterable[Path], oracle: Optional[TermOracle] = None,
               rules: Optional[Iterable[str]] = None, corpus: bool = True) -> list[Finding]:
    """Lint several cached models, plus the corpus rule when ``corpus`` is set."""
    rules = list(rules) if rules else None
    views, findings = [], []
    for p in sorted(paths):
        model = load_model(p)
        findings.extend(lint_model(model, oracle, rules))
        views.append(ModelView.from_model(model))
    if corpus and (rules is None or "near_duplicate_models" in rules):
        findings.extend(near_duplicate_models(views))
    return findings


SEVERITY_ORDER = {"ERROR": 0, "WARNING": 1, "INFO": 2}

TSV_COLUMNS = ("model_id", "severity", "rule", "qc_flag", "activity_ids", "message")


def write_findings_tsv(findings: Iterable[Finding], path: Path) -> None:
    """Write findings as a TSV with a header row."""
    import csv

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(TSV_COLUMNS)
        for f in findings:
            w.writerow([f.model_id, f.severity, f.rule, f.qc_flag or "",
                        ",".join(f.activity_ids), f.message])
