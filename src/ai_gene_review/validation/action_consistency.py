"""Table-driven consistency checks between review actions within one gene review.

A gene review judges claims about the gene, not evidence codes. Two GOA rows to the
same term are two pieces of evidence for one claim; they may reinforce each other, but
the review's actions on them must not contradict each other (e.g. ACCEPT on the IBA row
and REMOVE on the NAS row, or keeping both a term and a NOT annotation to it). Which
combinations count as contradictions, and how severe each is, lives in
``schema/action_consistency.yaml`` so strictness can be ratcheted one row at a time.

A review row can carry ``review.consistency_exception`` (with a reason) for the very
rare case where an apparent contradiction is correct: its conflicts are then reported
at INFO with the reason, and an exception that matches no conflict is flagged.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

import yaml

from ai_gene_review.datamodel.gene_review_model import ActionEnum

RULES_PATH = Path(__file__).parent.parent / "schema" / "action_consistency.yaml"


class Relation(str, Enum):
    """How the action_1 row's term relates to the action_2 row's term.

    A rule reads as a sentence: "the <action_1> row's term is <relation> the
    <action_2> row's term". Ancestry is strict and follows is_a/part_of.
    """

    SAME_TERM = "SAME_TERM"
    DESCENDANT_OF = "DESCENDANT_OF"
    ANCESTOR_OF = "ANCESTOR_OF"


#: Relations that need the ontology; evaluated only when an ancestor lookup is given
#: (``ai-gene-review validate --terms`` or ``--ontology-checks``).
HIERARCHICAL = frozenset({Relation.DESCENDANT_OF, Relation.ANCESTOR_OF})


class Severity(str, Enum):
    """Rule severity; OK documents a combination as consistent and reports nothing."""

    OK = "OK"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class MatchMode(str, Enum):
    """How a term filter matches a row's term id."""

    EXACT = "exact"
    #: The term itself or any is_a/part_of descendant; needs the ontology, so it is
    #: reserved but not evaluated yet.
    SELF_OR_DESCENDANT = "self_or_descendant"


@dataclass(frozen=True)
class TermFilter:
    """Restricts one side of a rule to rows whose term matches any of ``ids``."""

    mode: MatchMode
    ids: FrozenSet[str]

    def matches(self, term_id: str) -> bool:
        """Whether *term_id* satisfies this filter.

        >>> TermFilter(MatchMode.EXACT, frozenset({"GO:0005515"})).matches("GO:0005515")
        True
        >>> TermFilter(MatchMode.EXACT, frozenset({"GO:0005515"})).matches("GO:0019899")
        False
        """
        if self.mode is not MatchMode.EXACT:
            raise NotImplementedError(
                f"{self.mode.value} term filters are not evaluated yet"
            )
        return term_id in self.ids

    def describe(self) -> str:
        """Short human-readable form, e.g. ``exactly GO:0005515``."""
        ids = " or ".join(sorted(self.ids))
        if self.mode is MatchMode.EXACT:
            return f"exactly {ids}"
        return f"{ids} or a descendant"


@dataclass(frozen=True)
class Side:
    """One side of a rule: which actions, on rows of which polarity."""

    actions: FrozenSet[str]
    negated: bool = False

    def matches(self, action: str, negated: bool) -> bool:
        """Whether a row with *action* and *negated* polarity falls on this side."""
        return action in self.actions and negated == self.negated

    def overlaps(self, other: "Side") -> bool:
        """Whether some row could fall on both sides."""
        return self.negated == other.negated and bool(self.actions & other.actions)

    def describe(self) -> str:
        """E.g. ``NOT-row ACCEPT or KEEP_AS_NON_CORE``."""
        acts = " or ".join(sorted(self.actions))
        return f"{acts} NOT" if self.negated else acts


def _actions(value: Union[str, Iterable[str]]) -> FrozenSet[str]:
    """Normalise one action or a collection of actions to a frozenset."""
    return frozenset([value]) if isinstance(value, str) else frozenset(value)


@dataclass(frozen=True)
class ConsistencyRule:
    """One row of the action-consistency table.

    ``action_1``/``action_2`` may each be one action or several (any of them).
    ``negated_1``/``negated_2`` select NOT rows. ``term_1``/``term_2`` optionally
    restrict the rule to rows whose terms match; a filtered rule is an exception to
    (takes precedence over) a less filtered one.
    """

    action_1: Union[str, FrozenSet[str]]
    action_2: Union[str, FrozenSet[str]]
    relation: Relation
    severity: Severity
    rationale: str
    term_1: Optional[TermFilter] = None
    term_2: Optional[TermFilter] = None
    negated_1: bool = False
    negated_2: bool = False
    side_1: Side = field(init=False)
    side_2: Side = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "side_1", Side(_actions(self.action_1), self.negated_1)
        )
        object.__setattr__(
            self, "side_2", Side(_actions(self.action_2), self.negated_2)
        )

    @property
    def specificity(self) -> int:
        """Number of filtered sides; the most specific matching rule wins."""
        return (self.term_1 is not None) + (self.term_2 is not None)

    def describe(self) -> str:
        """Render the rule as the sentence it encodes.

        >>> ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF,
        ...                 Severity.OK, "x").describe()
        "the TOO_GENERAL row's term is an ancestor of the ACCEPT row's term"
        >>> ConsistencyRule(frozenset({"ACCEPT", "KEEP_AS_NON_CORE"}), "ACCEPT",
        ...     Relation.SAME_TERM, Severity.WARNING, "x", negated_1=True).describe()
        "the ACCEPT or KEEP_AS_NON_CORE NOT row's term is the same as the ACCEPT row's term"
        """
        phrase = {
            Relation.SAME_TERM: "the same as",
            Relation.DESCENDANT_OF: "a descendant of",
            Relation.ANCESTOR_OF: "an ancestor of",
        }[self.relation]

        def side(s: Side, term: Optional[TermFilter]) -> str:
            text = f"the {s.describe()} row's term"
            return text + (f" ({term.describe()})" if term else "")

        return (
            f"{side(self.side_1, self.term_1)} is {phrase} "
            f"{side(self.side_2, self.term_2)}"
        )


@dataclass(frozen=True)
class Conflict:
    """A pair of rows whose actions match a non-OK rule."""

    rule: ConsistencyRule
    term_id: str
    term_label: Optional[str]
    index_1: int
    index_2: int
    #: For hierarchical rules, the term of the index_2 row (term_id is index_1's).
    term_id_2: Optional[str] = None
    term_label_2: Optional[str] = None


REQUIRED_KEYS = {"action_1", "relation", "action_2", "severity", "rationale"}
OPTIONAL_KEYS = {"term_1", "term_2", "negated_1", "negated_2"}


def parse_term_filter(where: str, raw: Any) -> TermFilter:
    """Parse ``{exact: ID}`` / ``{exact: [ID, ...]}``; a list means any of the ids.

    >>> parse_term_filter("x", {"exact": ["GO:0003674", "GO:0008150"]}).ids == {
    ...     "GO:0003674", "GO:0008150"}
    True
    >>> parse_term_filter("x", {"self_or_descendant": "GO:0005488"})
    Traceback (most recent call last):
    ...
    ValueError: x: self_or_descendant term filters are not evaluated yet
    """
    if not isinstance(raw, dict) or len(raw) != 1:
        raise ValueError(f"{where}: expected one of {{exact: ...}}, got {raw!r}")
    ((mode_name, ids),) = raw.items()
    try:
        mode = MatchMode(mode_name)
    except ValueError:
        raise ValueError(f"{where}: unknown match mode {mode_name!r}") from None
    if mode is not MatchMode.EXACT:
        raise ValueError(f"{where}: {mode.value} term filters are not evaluated yet")
    id_list = [ids] if isinstance(ids, str) else ids
    if (
        not isinstance(id_list, list)
        or not id_list
        or not all(isinstance(i, str) and ":" in i for i in id_list)
    ):
        raise ValueError(f"{where}: expected a CURIE or a non-empty list of CURIEs")
    return TermFilter(mode, frozenset(id_list))


def _parse_actions(where: str, raw: Any, valid: Set[str]) -> FrozenSet[str]:
    """Parse one action or a non-empty list of actions, rejecting unknown values."""
    values = [raw] if isinstance(raw, str) else raw
    if not isinstance(values, list) or not values:
        raise ValueError(f"{where}: expected an action or a non-empty list of actions")
    for value in values:
        if value not in valid:
            raise ValueError(f"{where}: unknown action {value!r}")
    return frozenset(values)


def _parse_flag(where: str, raw: Any) -> bool:
    """Parse a strict YAML boolean."""
    if not isinstance(raw, bool):
        raise ValueError(f"{where}: expected true or false, got {raw!r}")
    return raw


def parse_rules(raw: Dict[str, Any]) -> List[ConsistencyRule]:
    """Parse and validate the rules table, failing fast on anything malformed.

    >>> rules = parse_rules({"rules": [{"action_1": "ACCEPT", "action_2": "REMOVE",
    ...     "relation": "SAME_TERM", "severity": "WARNING", "rationale": "x"}]})
    >>> rules[0].severity.value
    'WARNING'

    Unknown actions are rejected rather than silently never matching:

    >>> parse_rules({"rules": [{"action_1": "ACEPT", "action_2": "REMOVE",
    ...     "relation": "SAME_TERM", "severity": "WARNING", "rationale": "x"}]})
    Traceback (most recent call last):
    ...
    ValueError: rule 0 action_1: unknown action 'ACEPT'
    """
    valid_actions = {a.value for a in ActionEnum}
    rules: List[ConsistencyRule] = []
    for i, row in enumerate(raw.get("rules") or []):
        keys = set(row)
        if not REQUIRED_KEYS <= keys or not keys <= REQUIRED_KEYS | OPTIONAL_KEYS:
            raise ValueError(
                f"rule {i}: expected keys {sorted(REQUIRED_KEYS)} plus optional "
                f"{sorted(OPTIONAL_KEYS)}, got {sorted(row)}"
            )
        rule = ConsistencyRule(
            action_1=_parse_actions(
                f"rule {i} action_1", row["action_1"], valid_actions
            ),
            action_2=_parse_actions(
                f"rule {i} action_2", row["action_2"], valid_actions
            ),
            relation=Relation(row["relation"]),
            severity=Severity(row["severity"]),
            rationale=" ".join(str(row["rationale"]).split()),
            term_1=parse_term_filter(f"rule {i} term_1", row["term_1"])
            if "term_1" in row
            else None,
            term_2=parse_term_filter(f"rule {i} term_2", row["term_2"])
            if "term_2" in row
            else None,
            negated_1=_parse_flag(f"rule {i} negated_1", row.get("negated_1", False)),
            negated_2=_parse_flag(f"rule {i} negated_2", row.get("negated_2", False)),
        )
        if rule.relation is Relation.SAME_TERM and rule.term_2 is not None:
            raise ValueError(
                f"rule {i}: SAME_TERM rows share one term; filter it with term_1"
            )
        for j, other in enumerate(rules):
            _check_pair(i, rule, j, other)
        rules.append(rule)
    return rules


#: (side, filter) for each end of a rule, oriented so a DESCENDANT_OF reading holds.
Oriented = Tuple[Tuple[Side, Optional[TermFilter]], Tuple[Side, Optional[TermFilter]]]


def _orientations(rule: ConsistencyRule) -> List[Oriented]:
    """The ways a rule's two ends can be lined up against another rule's.

    ANCESTOR_OF is flipped into DESCENDANT_OF form; SAME_TERM is symmetric, so both
    orders are returned (its single filter applies to the shared term, i.e. both ends).
    """
    end_1, end_2 = (rule.side_1, rule.term_1), (rule.side_2, rule.term_2)
    if rule.relation is Relation.SAME_TERM:
        end_1, end_2 = (rule.side_1, rule.term_1), (rule.side_2, rule.term_1)
        return [(end_1, end_2), (end_2, end_1)]
    if rule.relation is Relation.ANCESTOR_OF:
        return [(end_2, end_1)]
    return [(end_1, end_2)]


def _family(rule: ConsistencyRule) -> Relation:
    """Relation family; ANCESTOR_OF and DESCENDANT_OF are mirror images."""
    return Relation.DESCENDANT_OF if rule.relation in HIERARCHICAL else rule.relation


def _may_overlap(f: Optional[TermFilter], g: Optional[TermFilter]) -> bool:
    """Whether some term could satisfy both filters (None matches everything).

    Conservative for non-exact filters: they are assumed to overlap.
    """
    if f is None or g is None:
        return True
    if f.mode is MatchMode.EXACT and g.mode is MatchMode.EXACT:
        return bool(f.ids & g.ids)
    return True


def _check_pair(i: int, rule: ConsistencyRule, j: int, other: ConsistencyRule) -> None:
    """Reject duplicates, and equally specific rules that could both match and disagree.

    >>> a = ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF, Severity.OK, "")
    >>> b = ConsistencyRule("ACCEPT", "TOO_GENERAL", Relation.DESCENDANT_OF, Severity.OK, "")
    >>> _check_pair(1, b, 0, a)
    Traceback (most recent call last):
    ...
    ValueError: rule 1: duplicate of rule 0 (the ACCEPT row's term is a descendant of the TOO_GENERAL row's term)
    """
    if _family(rule) is not _family(other):
        return
    mine = _orientations(rule)[0]
    for theirs in _orientations(other):
        if mine == theirs:
            raise ValueError(f"rule {i}: duplicate of rule {j} ({rule.describe()})")
    for theirs in _orientations(other):
        overlap = all(
            s.overlaps(o) and _may_overlap(f, g) for (s, f), (o, g) in zip(mine, theirs)
        )
        if (
            overlap
            and rule.specificity == other.specificity
            and rule.severity is not other.severity
        ):
            raise ValueError(
                f"rule {i}: ambiguous with rule {j}: equally specific, can match the "
                f"same rows, and disagree on severity ({rule.severity.value} vs "
                f"{other.severity.value})"
            )


@lru_cache(maxsize=1)
def load_rules() -> Tuple[ConsistencyRule, ...]:
    """Load the packaged rules table."""
    with open(RULES_PATH) as fh:
        return tuple(parse_rules(yaml.safe_load(fh)))


#: Maps a term id to its strict is_a/part_of ancestors.
Ancestors = Callable[[str], FrozenSet[str]]

#: is_a and part_of: a positive annotation to a term entails both kinds of ancestor.
GO_PREDICATES = ("rdfs:subClassOf", "BFO:0000050")


class GoAncestors:
    """Lazy, cached GO ancestor lookup over is_a and part_of.

    Fails fast: any problem building or querying the adapter raises, so a run that
    asked for ontology checks never silently skips them. Call :meth:`load` before a
    batch to fail before any file is validated.
    """

    #: A known part_of edge (axoneme part_of cilium) used to sanity-check the database.
    PROBE = ("GO:0005930", "GO:0005929")

    def __init__(self, adapter_string: str = "sqlite:obo:go"):
        self.adapter_string = adapter_string
        self._adapter: Any = None
        self._cache: Dict[str, FrozenSet[str]] = {}

    def load(self) -> "GoAncestors":
        """Build the adapter and check it returns a known ancestor; raise otherwise."""
        if self._adapter is None:
            from oaklib import get_adapter

            self._adapter = get_adapter(self.adapter_string)
            child, parent = self.PROBE
            if parent not in self(child):
                raise RuntimeError(
                    f"GO ancestor lookup via {self.adapter_string} is broken: "
                    f"{parent} is not an ancestor of {child}"
                )
        return self

    def __call__(self, term_id: str) -> FrozenSet[str]:
        if term_id not in self._cache:
            if self._adapter is None:
                self.load()
            found = self._adapter.ancestors(
                term_id, predicates=list(GO_PREDICATES), reflexive=False
            )
            self._cache[term_id] = frozenset(found) - {term_id}
        return self._cache[term_id]


@lru_cache(maxsize=1)
def go_ancestors() -> GoAncestors:
    """The shared GO ancestor lookup (loaded on first use)."""
    return GoAncestors()


def _comparable(ann_1: Dict[str, Any], ann_2: Dict[str, Any]) -> bool:
    """Rows on two different isoforms make independent claims and are not compared."""
    iso_1, iso_2 = ann_1.get("isoform"), ann_2.get("isoform")
    return not (iso_1 and iso_2 and iso_1 != iso_2)


#: (row index, annotation, action, negated)
Row = Tuple[int, Dict[str, Any], str, bool]


def _governing_rule(
    rules: List[ConsistencyRule], a: Row, b: Row, term_id: str
) -> Optional[Tuple[ConsistencyRule, bool]]:
    """The most specific SAME_TERM rule matching two rows, and whether row a is side 1.

    Parsing guarantees that equally specific matches agree on severity.
    """
    matching = []
    for rule in rules:
        if rule.term_1 is not None and not rule.term_1.matches(term_id):
            continue
        if rule.side_1.matches(a[2], a[3]) and rule.side_2.matches(b[2], b[3]):
            matching.append((rule, True))
        elif rule.side_1.matches(b[2], b[3]) and rule.side_2.matches(a[2], a[3]):
            matching.append((rule, False))
    return max(matching, key=lambda m: m[0].specificity, default=None)


def _governing_hierarchical_rule(
    rules: List[ConsistencyRule], specific: Row, general: Row, terms: Tuple[str, str]
) -> Optional[ConsistencyRule]:
    """The most specific hierarchical rule matching a (descendant, ancestor) row pair."""
    matching = []
    for rule in rules:
        ((spec_side, spec_filter), (gen_side, gen_filter)) = _orientations(rule)[0]
        if not spec_side.matches(specific[2], specific[3]):
            continue
        if not gen_side.matches(general[2], general[3]):
            continue
        if spec_filter is not None and not spec_filter.matches(terms[0]):
            continue
        if gen_filter is not None and not gen_filter.matches(terms[1]):
            continue
        matching.append(rule)
    return max(matching, key=lambda r: r.specificity, default=None)


def _collect_rows(data: Dict[str, Any]) -> List[Tuple[str, Row]]:
    """(term id, row) for every annotation with a term id and an action."""
    rows = []
    annotations = data.get("existing_annotations")
    for index, ann in enumerate(annotations if isinstance(annotations, list) else []):
        if not isinstance(ann, dict):
            continue
        term = ann.get("term")
        review = ann.get("review")
        if not isinstance(term, dict) or not isinstance(review, dict):
            continue
        term_id, action = term.get("id"), review.get("action")
        if isinstance(term_id, str) and isinstance(action, str):
            rows.append((term_id, (index, ann, action, bool(ann.get("negated")))))
    return rows


def _iter_hierarchical_conflicts(
    rows: List[Tuple[str, Row]], rules: List[ConsistencyRule], ancestors: Ancestors
) -> Iterator[Conflict]:
    """Conflicts between rows whose terms are in a strict ancestor relationship."""
    for (t_spec, spec), (t_gen, gen) in permutations(rows, 2):
        if t_spec == t_gen or t_gen not in ancestors(t_spec):
            continue
        if not _comparable(spec[1], gen[1]):
            continue
        rule = _governing_hierarchical_rule(rules, spec, gen, (t_spec, t_gen))
        if rule is None or rule.severity is Severity.OK:
            continue
        # index_1 is always the action_1 row as the rule is written.
        first, second = (
            (spec, gen) if rule.relation is Relation.DESCENDANT_OF else (gen, spec)
        )
        yield Conflict(
            rule,
            first[1]["term"]["id"],
            first[1]["term"].get("label"),
            first[0],
            second[0],
            term_id_2=second[1]["term"]["id"],
            term_label_2=second[1]["term"].get("label"),
        )


def iter_conflicts(
    data: Dict[str, Any],
    rules: Optional[Tuple[ConsistencyRule, ...]] = None,
    ancestors: Optional[Ancestors] = None,
) -> Iterator[Conflict]:
    """Yield each pair of rows whose governing rule is not OK.

    SAME_TERM rules are always evaluated; DESCENDANT_OF/ANCESTOR_OF rules only when
    an *ancestors* lookup is given.

    >>> rule = ConsistencyRule("ACCEPT", "REMOVE", Relation.SAME_TERM,
    ...                        Severity.WARNING, "x")
    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:1"}, "evidence_type": "IBA", "review": {"action": "ACCEPT"}},
    ...     {"term": {"id": "GO:1"}, "evidence_type": "NAS", "review": {"action": "REMOVE"}},
    ...     {"term": {"id": "GO:2"}, "review": {"action": "REMOVE"}}]}
    >>> [(c.term_id, c.index_1, c.index_2) for c in iter_conflicts(doc, (rule,))]
    [('GO:1', 0, 1)]

    A more specific OK rule is an exception:

    >>> exempt = ConsistencyRule("ACCEPT", "REMOVE", Relation.SAME_TERM, Severity.OK, "x",
    ...     term_1=TermFilter(MatchMode.EXACT, frozenset({"GO:1"})))
    >>> list(iter_conflicts(doc, (rule, exempt)))
    []

    Polarity is part of a rule: a positive-only rule ignores NOT rows.

    >>> doc["existing_annotations"][1]["negated"] = True
    >>> list(iter_conflicts(doc, (rule,)))
    []

    Hierarchical rules need an ancestor lookup (here a toy one: GO:2 is_a GO:1):

    >>> not_up = ConsistencyRule("ACCEPT", "ACCEPT", Relation.ANCESTOR_OF,
    ...     Severity.WARNING, "x", negated_1=True)
    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:2"}, "review": {"action": "ACCEPT"}},
    ...     {"term": {"id": "GO:1"}, "negated": True, "review": {"action": "ACCEPT"}}]}
    >>> toy = {"GO:2": frozenset({"GO:1"})}
    >>> list(iter_conflicts(doc, (not_up,)))
    []
    >>> [(c.term_id, c.term_id_2) for c in iter_conflicts(doc, (not_up,), toy.get)]
    [('GO:1', 'GO:2')]
    """
    all_rules = load_rules() if rules is None else rules
    same_term = [r for r in all_rules if r.relation is Relation.SAME_TERM]
    hierarchical = [r for r in all_rules if r.relation in HIERARCHICAL]
    rows = _collect_rows(data)
    if ancestors is not None and any(
        r.severity is not Severity.OK for r in hierarchical
    ):
        lookup = ancestors

        def strict_ancestors(term_id: str) -> FrozenSet[str]:
            return lookup(term_id) or frozenset()

        yield from _iter_hierarchical_conflicts(rows, hierarchical, strict_ancestors)
    if not any(r.severity is not Severity.OK for r in same_term):
        return
    by_term: Dict[str, List[Row]] = {}
    for term_id, row in rows:
        by_term.setdefault(term_id, []).append(row)
    for term_id, rows_for_term in by_term.items():
        for a, b in combinations(rows_for_term, 2):
            if not _comparable(a[1], b[1]):
                continue
            governing = _governing_rule(same_term, a, b, term_id)
            if governing is None or governing[0].severity is Severity.OK:
                continue
            rule, a_first = governing
            i_1, i_2 = (a[0], b[0]) if a_first else (b[0], a[0])
            yield Conflict(rule, term_id, a[1]["term"].get("label"), i_1, i_2)


def _describe_row(data: Dict[str, Any], index: int) -> str:
    """Short ``ACTION on row N (EVIDENCE, REF)`` description of one annotation row."""
    ann = data["existing_annotations"][index]
    bits = [
        b for b in (ann.get("evidence_type"), ann.get("original_reference_id")) if b
    ]
    polarity = " NOT" if ann.get("negated") else ""
    return (
        f"{ann['review']['action']}{polarity} on row {index} "
        f"({', '.join(bits) or 'no evidence'})"
    )


def _exception_reason(data: Dict[str, Any], index: int) -> Optional[str]:
    """The row's ``review.consistency_exception.reason``, if it declares one."""
    review = data["existing_annotations"][index].get("review") or {}
    exception = review.get("consistency_exception")
    if isinstance(exception, dict) and exception.get("reason"):
        return " ".join(str(exception["reason"]).split())
    return None


def iter_negated_too_general(data: Dict[str, Any]) -> Iterator[int]:
    """Yield indices of NOT rows marked TOO_GENERAL.

    A NOT on a broad term is the strongest negative claim, not an uninformative one.

    >>> list(iter_negated_too_general({"existing_annotations": [
    ...     {"negated": True, "review": {"action": "TOO_GENERAL"}},
    ...     {"review": {"action": "TOO_GENERAL"}}]}))
    [0]
    """
    for index, ann in enumerate(data.get("existing_annotations") or []):
        if isinstance(ann, dict) and ann.get("negated"):
            if (ann.get("review") or {}).get("action") == "TOO_GENERAL":
                yield index


#: Actions whose (positive) term counts as asserted when justifying TOO_GENERAL.
_ASSERTING = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "NEW"})


def iter_unjustified_too_general(
    data: Dict[str, Any], ancestors: Ancestors
) -> Iterator[int]:
    """Yield indices of TOO_GENERAL rows with no asserted, more specific term.

    TOO_GENERAL means "entailed by a more specific term asserted in this review":
    some positive ACCEPT, KEEP_AS_NON_CORE or NEW row, or a MODIFY replacement term,
    must be a strict descendant of the row's term.

    >>> toy = {"GO:C": frozenset({"GO:A"})}.get
    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:A"}, "review": {"action": "TOO_GENERAL"}},
    ...     {"term": {"id": "GO:B"}, "review": {"action": "TOO_GENERAL"}},
    ...     {"term": {"id": "GO:X"}, "review": {"action": "MODIFY",
    ...      "proposed_replacement_terms": [{"id": "GO:C"}]}}]}
    >>> list(iter_unjustified_too_general(doc, lambda t: toy(t) or frozenset()))
    [1]
    """
    asserted: Set[str] = set()
    annotations = data.get("existing_annotations") or []
    for ann in annotations:
        if not isinstance(ann, dict) or ann.get("negated"):
            continue
        review = ann.get("review") or {}
        action = review.get("action")
        term_id = (ann.get("term") or {}).get("id")
        if action in _ASSERTING and isinstance(term_id, str):
            asserted.add(term_id)
        if action == "MODIFY":
            for repl in review.get("proposed_replacement_terms") or []:
                repl_id = repl.get("id") if isinstance(repl, dict) else None
                if isinstance(repl_id, str) and repl_id.startswith("GO:"):
                    asserted.add(repl_id)
    for index, ann in enumerate(annotations):
        if not isinstance(ann, dict) or ann.get("negated"):
            continue
        if (ann.get("review") or {}).get("action") != "TOO_GENERAL":
            continue
        term_id = (ann.get("term") or {}).get("id")
        if not any(term_id in ancestors(other) for other in asserted):
            yield index


def _hierarchical_rules_active() -> bool:
    """Whether the packaged table has any reportable hierarchical rule."""
    return any(
        r.relation in HIERARCHICAL and r.severity is not Severity.OK
        for r in load_rules()
    )


def check_action_consistency(
    data: Dict[str, Any], report, ancestors: Optional[Ancestors] = None
) -> None:
    """Report action conflicts at the table's severity, honouring row exceptions.

    Hierarchical rules run only when *ancestors* is given; without it, exceptions
    that could be explained by a hierarchical conflict are not flagged as stale.
    A failing *ancestors* lookup raises: ontology checks are never silently skipped.
    """
    from ai_gene_review.validation.validation_report import ValidationSeverity

    used: Set[int] = set()
    for c in iter_conflicts(data, ancestors=ancestors):
        reasons = {
            i: r for i in (c.index_1, c.index_2) if (r := _exception_reason(data, i))
        }
        used.update(reasons)
        where = f"{c.term_id} ({c.term_label or 'unknown'})"
        if c.term_id_2 is not None:
            where += f" and {c.term_id_2} ({c.term_label_2 or 'unknown'})"
        message = (
            f"Contradictory review actions for {where}: "
            f"{_describe_row(data, c.index_1)} vs {_describe_row(data, c.index_2)}"
            f" [{c.rule.describe()}]"
        )
        if reasons:
            severity = ValidationSeverity.INFO
            message += " -- allowed by consistency_exception: " + "; ".join(
                reasons.values()
            )
        else:
            severity = ValidationSeverity[c.rule.severity.value]
        report.add_issue(
            severity,
            message,
            path=f"existing_annotations[{c.index_2}].review.action",
            suggestion=c.rule.rationale,
            validation_category="BestPractices",
            check_type="action_consistency",
        )
    can_judge_staleness = ancestors is not None or not _hierarchical_rules_active()
    for index, ann in enumerate(data.get("existing_annotations") or []):
        if not isinstance(ann, dict) or not can_judge_staleness:
            continue
        if _exception_reason(data, index) and index not in used:
            report.add_issue(
                ValidationSeverity.WARNING,
                f"existing_annotations[{index}] declares a consistency_exception but "
                "is not in any action-consistency conflict",
                path=f"existing_annotations[{index}].review.consistency_exception",
                suggestion="Remove the stale exception.",
                validation_category="BestPractices",
                check_type="action_consistency",
            )
    if ancestors is not None:
        for index in iter_unjustified_too_general(data, ancestors):
            report.add_issue(
                ValidationSeverity.WARNING,
                "TOO_GENERAL but no more specific term is asserted in this review "
                "(ACCEPT, KEEP_AS_NON_CORE, NEW or a MODIFY replacement)",
                path=f"existing_annotations[{index}].review.action",
                suggestion=(
                    "TOO_GENERAL means the term is entailed by a more specific asserted "
                    "term. If none exists, the broad term is the gene's only statement "
                    "of this claim: use ACCEPT or KEEP_AS_NON_CORE (or MODIFY to a "
                    "better term)."
                ),
                validation_category="BestPractices",
                check_type="action_consistency",
            )
    for index in iter_negated_too_general(data):
        report.add_issue(
            ValidationSeverity.ERROR,
            "TOO_GENERAL on a NOT annotation: a negative claim on a broad term is the "
            "strongest such claim, not an uninformative one",
            path=f"existing_annotations[{index}].review.action",
            suggestion="Use ACCEPT, KEEP_AS_NON_CORE, REMOVE or UNDECIDED.",
            validation_category="BestPractices",
            check_type="action_consistency",
        )
