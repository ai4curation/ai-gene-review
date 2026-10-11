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
from typing import Any, Dict, Iterator, List, Optional, Tuple

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


@dataclass(frozen=True)
class ConsistencyRule:
    """One row of the action-consistency table."""

    action_1: str
    action_2: str
    relation: Relation
    severity: Severity
    rationale: str

    def describe(self) -> str:
        """Render the rule as the sentence it encodes.

        >>> ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF,
        ...                 Severity.OK, "x").describe()
        "the TOO_GENERAL row's term is an ancestor of the ACCEPT row's term"
        """
        phrase = {
            Relation.SAME_TERM: "the same as",
            Relation.DESCENDANT_OF: "a descendant of",
            Relation.ANCESTOR_OF: "an ancestor of",
        }[self.relation]
        return (
            f"the {self.action_1} row's term is {phrase} the {self.action_2} row's term"
        )


@dataclass(frozen=True)
class Conflict:
    """A pair of rows whose actions match a non-OK rule."""

    rule: ConsistencyRule
    term_id: str
    term_label: Optional[str]
    index_1: int
    index_2: int


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
    seen: set[Tuple[str, ...]] = set()
    for i, row in enumerate(raw.get("rules") or []):
        expected = {"action_1", "relation", "action_2", "severity", "rationale"}
        if set(row) != expected:
            raise ValueError(f"rule {i}: expected keys {sorted(expected)}, got {sorted(row)}")
        for column in ("action_1", "action_2"):
            if row[column] not in valid_actions:
                raise ValueError(f"rule {i}: unknown action {row[column]!r}")
        rule = ConsistencyRule(
            action_1=row["action_1"],
            action_2=row["action_2"],
            relation=Relation(row["relation"]),
            severity=Severity(row["severity"]),
            rationale=" ".join(str(row["rationale"]).split()),
        )
        if rule.relation in HIERARCHICAL and rule.severity is not Severity.OK:
            raise ValueError(
                f"rule {i}: {rule.relation.value} rules are not evaluated yet; "
                "only OK is allowed"
            )
        key = _rule_key(rule)
        if key in seen:
            raise ValueError(f"rule {i}: duplicate rule for {key}")
        seen.add(key)
        rules.append(rule)
    return rules


def _rule_key(rule: ConsistencyRule) -> Tuple[str, ...]:
    """Canonical identity of a rule, so a rule and its mirror image collide.

    SAME_TERM is symmetric; "A ANCESTOR_OF B" is the same rule as "B DESCENDANT_OF A".

    >>> a = ConsistencyRule("TOO_GENERAL", "ACCEPT", Relation.ANCESTOR_OF, Severity.OK, "")
    >>> b = ConsistencyRule("ACCEPT", "TOO_GENERAL", Relation.DESCENDANT_OF, Severity.OK, "")
    >>> _rule_key(a) == _rule_key(b)
    True
    """
    if rule.relation is Relation.SAME_TERM:
        a, b = sorted((rule.action_1, rule.action_2))
        return (rule.relation.value, a, b)
    if rule.relation is Relation.ANCESTOR_OF:
        return (Relation.DESCENDANT_OF.value, rule.action_2, rule.action_1)
    return (rule.relation.value, rule.action_1, rule.action_2)


@lru_cache(maxsize=1)
def load_rules() -> Tuple[ConsistencyRule, ...]:
    """Load the packaged rules table."""
    with open(RULES_PATH) as fh:
        return tuple(parse_rules(yaml.safe_load(fh)))


def _comparable(ann_1: Dict[str, Any], ann_2: Dict[str, Any]) -> bool:
    """Rows on two different isoforms make independent claims and are not compared."""
    iso_1, iso_2 = ann_1.get("isoform"), ann_2.get("isoform")
    return not (iso_1 and iso_2 and iso_1 != iso_2)


def iter_conflicts(
    data: Dict[str, Any], rules: Optional[Tuple[ConsistencyRule, ...]] = None
) -> Iterator[Conflict]:
    """Yield each pair of rows whose actions match a non-OK SAME_TERM rule.

    >>> rule = ConsistencyRule("ACCEPT", "REMOVE", Relation.SAME_TERM,
    ...                        Severity.WARNING, "x")
    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:1"}, "evidence_type": "IBA", "review": {"action": "ACCEPT"}},
    ...     {"term": {"id": "GO:1"}, "evidence_type": "NAS", "review": {"action": "REMOVE"}},
    ...     {"term": {"id": "GO:2"}, "review": {"action": "REMOVE"}}]}
    >>> [(c.term_id, c.index_1, c.index_2) for c in iter_conflicts(doc, (rule,))]
    [('GO:1', 0, 1)]

    Negated rows make the opposite claim and are not compared with positive ones:

    >>> doc["existing_annotations"][1]["negated"] = True
    >>> list(iter_conflicts(doc, (rule,)))
    []
    """
    active = [
        r
        for r in (load_rules() if rules is None else rules)
        if r.relation is Relation.SAME_TERM and r.severity is not Severity.OK
    ]
    annotations = data.get("existing_annotations")
    if not active or not isinstance(annotations, list):
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
            for rule in active:
                if (act_a, act_b) == (rule.action_1, rule.action_2):
                    yield Conflict(rule, term_id, ann_a["term"].get("label"), i_a, i_b)
                elif (act_b, act_a) == (rule.action_1, rule.action_2):
                    yield Conflict(rule, term_id, ann_a["term"].get("label"), i_b, i_a)


def _describe_row(data: Dict[str, Any], index: int) -> str:
    """Short ``ACTION on row N (EVIDENCE, REF)`` description of one annotation row."""
    ann = data["existing_annotations"][index]
    bits = [b for b in (ann.get("evidence_type"), ann.get("original_reference_id")) if b]
    return f"{ann['review']['action']} on row {index} ({', '.join(bits) or 'no evidence'})"


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
