#!/usr/bin/env python
"""Redundancy among ARBA keyword rules.

The keyword counterpart of ``rule_redundancy.py``, which covers GO rules only.
Reads every ARBA rule from the same cached UniProt download
(``.cache/arba/arba_rules.json``) and the UniProt keyword hierarchy
(``rest.uniprot.org/keywords/stream``, cached beside it), and applies the same
structural test to the rules that assert a keyword:

    A condition set of rule R (keyword K) is *covered* when another rule asserts
    a strict descendant of K from a condition set whose signatures are a subset
    of R's, with no negative conditions and either no taxon restriction or the
    same one.

One difference from GO matters when reading the numbers: UniProt keeps only the
most specific ARBA GO term on a protein, so a covered GO set emits nothing, but
keywords from different rules stack. A covered keyword set still emits its
keyword; it is redundant only if the parent keyword could be derived from the
child, which this script does not establish.

Writes ``keyword_redundancy.tsv`` (one row per ARBA keyword rule).

Usage::

    uv run python projects/ARBA_REVIEW/keyword_redundancy.py
"""

from __future__ import annotations

import collections
import csv
import json
from dataclasses import dataclass
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = Path(".cache/arba/arba_rules.json")
KEYWORD_CACHE = Path(".cache/arba/keywords.json")
ARBA_URL = "https://rest.uniprot.org/arba/stream?query=*&format=json"
KEYWORD_URL = "https://rest.uniprot.org/keywords/stream?query=*&format=json"
OUT = HERE / "keyword_redundancy.tsv"


@dataclass(frozen=True)
class ConditionSet:
    """Signatures (ANDed), taxon restrictions and negative conditions of one set."""

    signatures: frozenset[str]
    taxa: frozenset[str]
    negatives: frozenset[str]


@dataclass
class Rule:
    """An ARBA rule that asserts a keyword."""

    id: str
    keyword: str
    sets: list[ConditionSet]


def covers(specific: ConditionSet, general: ConditionSet) -> bool:
    """Whether every protein *general* matches is also matched by *specific*.

    >>> a = ConditionSet(frozenset({"IPR1"}), frozenset(), frozenset())
    >>> b = ConditionSet(frozenset({"IPR1", "IPR2"}), frozenset({"taxon:Fungi"}), frozenset())
    >>> covers(a, b), covers(b, a)
    (True, False)
    """
    if specific.negatives or not specific.signatures:
        return False
    if not specific.signatures <= general.signatures:
        return False
    return not specific.taxa or specific.taxa == general.taxa


def fetch(url: str, cache: Path) -> dict:
    """A cached JSON download."""
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(url, timeout=600)
        response.raise_for_status()
        cache.write_bytes(response.content)
    return json.loads(cache.read_text())


def load_rules() -> list[Rule]:
    """ARBA rules that assert a keyword, from the cached UniProt download."""
    rules = []
    for raw in fetch(ARBA_URL, CACHE)["results"]:
        keywords = [a["keyword"]["id"] for a in raw["mainRule"].get("annotations", []) if "keyword" in a]
        if not keywords:
            continue
        sets = []
        for cs in raw["mainRule"]["conditionSets"]:
            sig, tax, neg = set(), set(), set()
            for c in cs["conditions"]:
                values = [f"{c['type']}:{v['value']}" for v in c.get("conditionValues", [])]
                if c.get("isNegative"):
                    neg.update(values)
                elif c["type"] == "taxon":
                    tax.update(values)
                else:
                    sig.update(values)
            sets.append(ConditionSet(frozenset(sig), frozenset(tax), frozenset(neg)))
        for keyword in keywords:
            rules.append(Rule(raw["uniRuleId"], keyword, sets))
    return rules


def keyword_tables() -> tuple[dict[str, set[str]], dict[str, str]]:
    """Strict ancestors and names of every UniProt keyword."""
    parents: dict[str, set[str]] = {}
    names: dict[str, str] = {}
    for entry in fetch(KEYWORD_URL, KEYWORD_CACHE)["results"]:
        keyword = entry["keyword"]["id"]
        names[keyword] = entry["keyword"]["name"]
        parents[keyword] = {p["keyword"]["id"] for p in entry.get("parents", [])}

    def ancestors(keyword: str, seen: set[str]) -> set[str]:
        for parent in parents.get(keyword, ()):
            if parent not in seen:
                seen.add(parent)
                ancestors(parent, seen)
        return seen

    return {keyword: ancestors(keyword, set()) for keyword in parents}, names


def main() -> None:
    rules = load_rules()
    ancestors, names = keyword_tables()
    by_signature: dict[str, list[tuple[Rule, ConditionSet]]] = collections.defaultdict(list)
    for rule in rules:
        for condition_set in rule.sets:
            for signature in condition_set.signatures:
                by_signature[signature].append((rule, condition_set))
    descendants = collections.Counter(a for keyword in ancestors for a in ancestors[keyword])
    rows = []
    for rule in sorted(rules, key=lambda r: r.id):
        covered = 0
        by_keyword: collections.Counter[str] = collections.Counter()
        for condition_set in rule.sets:
            hits = {
                other.keyword
                for signature in condition_set.signatures
                for other, other_set in by_signature[signature]
                if other.id != rule.id
                and rule.keyword in ancestors.get(other.keyword, ())
                and covers(other_set, condition_set)
            }
            covered += bool(hits)
            by_keyword.update(hits)
        rows.append({
            "rule": rule.id,
            "keyword": rule.keyword,
            "name": names.get(rule.keyword, ""),
            "keyword_descendants": descendants[rule.keyword],
            "condition_sets": len(rule.sets),
            "covered_sets": covered,
            "covered_by_keywords": "|".join(f"{k}={n}" for k, n in by_keyword.most_common()),
        })
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} keyword rules; {sum(r['covered_sets'] > 0 for r in rows)} with a covered set -> {OUT}")


if __name__ == "__main__":
    main()
