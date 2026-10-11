"""Table-driven consistency checks between review actions within one gene review.

A gene review judges claims about the gene, not evidence codes. Two GOA rows to the
same term are two pieces of evidence for one claim; they may reinforce each other, but
the review's actions on them must not contradict each other (e.g. ACCEPT on the IBA row
and REMOVE on the NAS row). Which combinations count as contradictions, and how severe
each is, lives in ``schema/action_consistency.yaml`` so strictness can be ratcheted one
row at a time.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, FrozenSet, Iterator, List, Optional, Tuple

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


#: Relations that need the ontology; not evaluated yet, so only OK is allowed.
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
    #: parsed for documentation but not evaluated yet.
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
        return (
            f"exactly {ids}"
            if self.mode is MatchMode.EXACT
            else f"{ids} or a descendant"
        )


@dataclass(frozen=True)
class ConsistencyRule:
    """One row of the action-consistency table.

    ``term_1`` and ``term_2`` optionally restrict the rule to rows whose terms match;
    a filtered rule is an exception to (takes precedence over) a less filtered one.
    """

    action_1: str
    action_2: str
    relation: Relation
    severity: Severity
    rationale: str
    term_1: Optional[TermFilter] = None
    term_2: Optional[TermFilter] = None

    @property
    def specificity(self) -> int:
        """Number of filtered sides; the most specific matching rule wins."""
        return (self.term_1 is not None) + (self.term_2 is not None)

    def describe(self) -> str:
        """Render the rule as the sentence it encodes.

        >>> ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF,
        ...                 Severity.OK, "x").describe()
        "the TOO_GENERAL row's term is an ancestor of the ACCEPT row's term"
        >>> pb = TermFilter(MatchMode.EXACT, frozenset({"GO:0005515"}))
        >>> ConsistencyRule("ACCEPT", "REMOVE", Relation.SAME_TERM, Severity.OK, "x",
        ...                 term_1=pb).describe()
        "the ACCEPT row's term (exactly GO:0005515) is the same as the REMOVE row's term"
        """
        phrase = {
            Relation.SAME_TERM: "the same as",
            Relation.DESCENDANT_OF: "a descendant of",
            Relation.ANCESTOR_OF: "an ancestor of",
        }[self.relation]

        def side(action: str, term: Optional[TermFilter]) -> str:
            return f"the {action} row's term" + (
                f" ({term.describe()})" if term else ""
            )

        return f"{side(self.action_1, self.term_1)} is {phrase} {side(self.action_2, self.term_2)}"


@dataclass(frozen=True)
class Conflict:
    """A pair of rows whose actions match a non-OK rule."""

    rule: ConsistencyRule
    term_id: str
    term_label: Optional[str]
    index_1: int
    index_2: int


REQUIRED_KEYS = {"action_1", "relation", "action_2", "severity", "rationale"}
OPTIONAL_KEYS = {"term_1", "term_2"}


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
    ValueError: rule 0: unknown action 'ACEPT'
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
        for column in ("action_1", "action_2"):
            if row[column] not in valid_actions:
                raise ValueError(f"rule {i}: unknown action {row[column]!r}")
        rule = ConsistencyRule(
            action_1=row["action_1"],
            action_2=row["action_2"],
            relation=Relation(row["relation"]),
            severity=Severity(row["severity"]),
            rationale=" ".join(str(row["rationale"]).split()),
            term_1=parse_term_filter(f"rule {i} term_1", row["term_1"])
            if "term_1" in row
            else None,
            term_2=parse_term_filter(f"rule {i} term_2", row["term_2"])
            if "term_2" in row
            else None,
        )
        if rule.relation is Relation.SAME_TERM and rule.term_2 is not None:
            raise ValueError(
                f"rule {i}: SAME_TERM rows share one term; filter it with term_1"
            )
        if rule.relation in HIERARCHICAL and rule.severity is not Severity.OK:
            raise ValueError(
                f"rule {i}: {rule.relation.value} rules are not evaluated yet; "
                "only OK is allowed"
            )
        for j, other in enumerate(rules):
            _check_pair(i, rule, j, other)
        rules.append(rule)
    return rules


Canonical = Tuple[str, str, str, Optional[TermFilter], Optional[TermFilter]]


def _canonical(rule: ConsistencyRule) -> Canonical:
    """Orientation-free form, so a rule and its mirror image compare equal.

    SAME_TERM is symmetric (its one filter applies to the shared term);
    "A ANCESTOR_OF B" is the same rule as "B DESCENDANT_OF A", filters included.

    >>> a = ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF, Severity.OK, "")
    >>> b = ConsistencyRule("ACCEPT", "TOO_GENERAL", Relation.DESCENDANT_OF, Severity.OK, "")
    >>> _canonical(a) == _canonical(b)
    True
    """
    if rule.relation is Relation.SAME_TERM:
        a, b = sorted((rule.action_1, rule.action_2))
        return (rule.relation.value, a, b, rule.term_1, None)
    if rule.relation is Relation.ANCESTOR_OF:
        return (
            Relation.DESCENDANT_OF.value,
            rule.action_2,
            rule.action_1,
            rule.term_2,
            rule.term_1,
        )
    return (rule.relation.value, rule.action_1, rule.action_2, rule.term_1, rule.term_2)


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
    """Reject duplicates, and equally specific rules that could both match and disagree."""
    (rel, a1, a2, f1, f2), (o_rel, o_a1, o_a2, g1, g2) = (
        _canonical(rule),
        _canonical(other),
    )
    if (rel, a1, a2) != (o_rel, o_a1, o_a2):
        return
    if (f1, f2) == (g1, g2):
        raise ValueError(f"rule {i}: duplicate of rule {j} ({rule.describe()})")
    if (
        rule.specificity == other.specificity
        and rule.severity is not other.severity
        and _may_overlap(f1, g1)
        and _may_overlap(f2, g2)
    ):
        raise ValueError(
            f"rule {i}: ambiguous with rule {j}: equally specific, can match the same "
            f"rows, and disagree on severity ({rule.severity.value} vs {other.severity.value})"
        )


@lru_cache(maxsize=1)
def load_rules() -> Tuple[ConsistencyRule, ...]:
    """Load the packaged rules table."""
    with open(RULES_PATH) as fh:
        return tuple(parse_rules(yaml.safe_load(fh)))


def _comparable(ann_1: Dict[str, Any], ann_2: Dict[str, Any]) -> bool:
    """Rows on two different isoforms make independent claims and are not compared."""
    iso_1, iso_2 = ann_1.get("isoform"), ann_2.get("isoform")
    return not (iso_1 and iso_2 and iso_1 != iso_2)


def _governing_rule(
    rules: List[ConsistencyRule], act_a: str, act_b: str, term_id: str
) -> Optional[Tuple[ConsistencyRule, bool]]:
    """The most specific SAME_TERM rule matching two rows, and whether row a is action_1.

    Parsing guarantees that equally specific matches agree on severity.
    """
    matching = []
    for rule in rules:
        if rule.term_1 is not None and not rule.term_1.matches(term_id):
            continue
        if (act_a, act_b) == (rule.action_1, rule.action_2):
            matching.append((rule, True))
        elif (act_b, act_a) == (rule.action_1, rule.action_2):
            matching.append((rule, False))
    return max(matching, key=lambda m: m[0].specificity, default=None)


def iter_conflicts(
    data: Dict[str, Any], rules: Optional[Tuple[ConsistencyRule, ...]] = None
) -> Iterator[Conflict]:
    """Yield each pair of same-term rows whose governing rule is not OK.

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

    Negated rows make the opposite claim and are not compared with positive ones:

    >>> doc["existing_annotations"][1]["negated"] = True
    >>> list(iter_conflicts(doc, (rule,)))
    []
    """
    same_term = [
        r
        for r in (load_rules() if rules is None else rules)
        if r.relation is Relation.SAME_TERM
    ]
    annotations = data.get("existing_annotations")
    if not any(r.severity is not Severity.OK for r in same_term) or not isinstance(
        annotations, list
    ):
        return
    by_term: Dict[str, List[Tuple[int, Dict[str, Any], str]]] = {}
    for index, ann in enumerate(annotations):
        if not isinstance(ann, dict) or ann.get("negated"):
            continue
        term = ann.get("term")
        review = ann.get("review")
        if not isinstance(term, dict) or not isinstance(review, dict):
            continue
        term_id, action = term.get("id"), review.get("action")
        if isinstance(term_id, str) and isinstance(action, str):
            by_term.setdefault(term_id, []).append((index, ann, action))
    for term_id, rows in by_term.items():
        for (i_a, ann_a, act_a), (i_b, ann_b, act_b) in combinations(rows, 2):
            if not _comparable(ann_a, ann_b):
                continue
            governing = _governing_rule(same_term, act_a, act_b, term_id)
            if governing is None or governing[0].severity is Severity.OK:
                continue
            rule, a_first = governing
            i_1, i_2 = (i_a, i_b) if a_first else (i_b, i_a)
            yield Conflict(rule, term_id, ann_a["term"].get("label"), i_1, i_2)


def _describe_row(data: Dict[str, Any], index: int) -> str:
    """Short ``ACTION on row N (EVIDENCE, REF)`` description of one annotation row."""
    ann = data["existing_annotations"][index]
    bits = [
        b for b in (ann.get("evidence_type"), ann.get("original_reference_id")) if b
    ]
    return (
        f"{ann['review']['action']} on row {index} ({', '.join(bits) or 'no evidence'})"
    )


def check_action_consistency(data: Dict[str, Any], report) -> None:
    """Add one issue per conflicting row pair, at the severity the rules table sets."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    for c in iter_conflicts(data):
        severity = ValidationSeverity[c.rule.severity.value]
        report.add_issue(
            severity,
            f"Contradictory review actions for {c.term_id} ({c.term_label or 'unknown'}): "
            f"{_describe_row(data, c.index_1)} vs {_describe_row(data, c.index_2)}",
            path=f"existing_annotations[{c.index_2}].review.action",
            suggestion=c.rule.rationale,
            validation_category="BestPractices",
            check_type="action_consistency",
        )
