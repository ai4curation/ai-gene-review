"""Evaluate an ARBA rule's condition sets against AGFG1's own signature/taxon profile.

An ARBA rule fires when *every* condition inside *one* condition set is satisfied.
A set that merely mentions one of the subject's signatures does NOT fire, so a
"mentions" test would report a match that the rule does not actually make - this
script therefore evaluates full satisfaction and reports the two counts
separately.

Usage:
    uv run python parse_arba.py ARBA00026971
    uv run python parse_arba.py --self-test
"""

from __future__ import annotations

import json
import sys
import urllib.request

# AGFG1 (P52594) profile, transcribed from genes/human/AGFG1/AGFG1-uniprot.txt.
SUBJECT = "P52594"
SUBJECT_IPR = frozenset(
    {"IPR052248", "IPR037278", "IPR001164", "IPR038508"}
)  # DR InterPro lines
SUBJECT_FUNFAM = frozenset(
    {"1.10.220.150:FF:000005", "3.30.450.50:FF:000005"}
)  # DR FunFam lines
# OC lineage from the UniProt entry, plus the ranks ARBA uses as taxon conditions.
SUBJECT_TAXA = frozenset(
    {
        "Eukaryota",
        "Metazoa",
        "Chordata",
        "Craniata",
        "Vertebrata",
        "Euteleostomi",
        "Mammalia",
        "Eutheria",
        "Euarchontoglires",
        "Primates",
        "Haplorrhini",
        "Catarrhini",
        "Hominidae",
        "Homo",
    }
)

# Condition types this evaluator understands. Anything else makes the set
# undecidable rather than false, and that must be reported, not swallowed.
KNOWN_TYPES = {"InterPro id", "FunFam id", "taxon"}


def fetch(rule_id: str) -> dict:
    url = f"https://rest.uniprot.org/arba/{rule_id}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        return json.load(fh)


def satisfied(cond: dict, ipr: frozenset, funfam: frozenset, taxa: frozenset):
    """Return True/False, or None when the condition type is not understood."""
    vals = {v["value"] for v in cond["conditionValues"]}
    ctype = cond["type"]
    if ctype not in KNOWN_TYPES:
        return None
    if ctype == "InterPro id":
        present = bool(vals & ipr)
    elif ctype == "FunFam id":
        present = bool(vals & funfam)
    else:
        present = bool(vals & taxa)
    return (not present) if cond.get("isNegative") else present


def evaluate(sets: list[dict], ipr: frozenset, funfam: frozenset, taxa: frozenset):
    """Return (fires, mentions, undecidable) lists of (index, rendered) tuples."""
    fires, mentions, undecidable = [], [], []
    for i, s in enumerate(sets):
        parts, results = [], []
        touches = False
        for c in s["conditions"]:
            vals = [v["value"] for v in c["conditionValues"]]
            neg = " (NEG)" if c.get("isNegative") else ""
            parts.append(f"{c['type']}={'|'.join(vals)}{neg}")
            if c["type"] in ("InterPro id", "FunFam id") and (
                set(vals) & (ipr | funfam)
            ):
                touches = True
            results.append(satisfied(c, ipr, funfam, taxa))
        rendered = (i, " AND ".join(parts))
        if None in results:
            if touches:
                undecidable.append(rendered)
            continue
        if all(results):
            fires.append(rendered)
        elif touches:
            mentions.append(rendered)
    return fires, mentions, undecidable


def go_annotations(rule: dict) -> list[str]:
    out = []
    for a in rule["mainRule"].get("annotations", []):
        ref = a.get("dbReference", {})
        if ref.get("database") == "GO":
            out.append(ref["id"])
    return out


def self_test() -> None:
    """Break-tests. Each asserts the fixture differs from the real profile, that
    the evaluator's verdict changes, and which way it changes."""
    sets = [
        {
            "conditions": [
                {"type": "InterPro id", "conditionValues": [{"value": "IPR001164"}]},
                {"type": "InterPro id", "conditionValues": [{"value": "IPR037278"}]},
            ]
        },
        {
            "conditions": [
                {"type": "InterPro id", "conditionValues": [{"value": "IPR001164"}]},
                {"type": "InterPro id", "conditionValues": [{"value": "IPR051718"}]},
            ]
        },
        {
            "conditions": [
                {"type": "FunFam id", "conditionValues": [{"value": "9.9.9.9:FF:000001"}]},
            ]
        },
        {
            "conditions": [
                {"type": "InterPro id", "conditionValues": [{"value": "IPR001164"}]},
                {"type": "proteome", "conditionValues": [{"value": "whatever"}]},
            ]
        },
    ]
    fires, mentions, undecidable = evaluate(
        sets, SUBJECT_IPR, SUBJECT_FUNFAM, SUBJECT_TAXA
    )
    # 1. A set whose every InterPro condition is met fires.
    assert [i for i, _ in fires] == [0], f"fires={fires}"
    # 2. A set naming one held signature plus one absent one must NOT fire; it is
    #    the case a "mentions" test would wrongly report.
    assert [i for i, _ in mentions] == [1], f"mentions={mentions}"
    # 3. A set touching nothing of the subject's is neither fires nor mentions.
    assert 2 not in [i for i, _ in fires] + [i for i, _ in mentions]
    # 4. An unknown condition type makes the set undecidable, not false.
    assert [i for i, _ in undecidable] == [3], f"undecidable={undecidable}"

    # Break-test: removing IPR037278 from the profile must move set 0 out of
    # `fires`. Assert the mutation actually changed the profile first.
    mutated = frozenset(SUBJECT_IPR - {"IPR037278"})
    assert mutated != SUBJECT_IPR, "mutation did not change the profile"
    f2, m2, _ = evaluate(sets, mutated, SUBJECT_FUNFAM, SUBJECT_TAXA)
    assert [i for i, _ in f2] == [], f"expected no fires after mutation, got {f2}"
    assert 0 in [i for i, _ in m2], f"set 0 should now only be a mention: {m2}"

    # Break-test the taxon arm too, in its own direction.
    tax_sets = [
        {
            "conditions": [
                {"type": "InterPro id", "conditionValues": [{"value": "IPR001164"}]},
                {"type": "taxon", "conditionValues": [{"value": "Viridiplantae"}]},
            ]
        }
    ]
    f3, m3, _ = evaluate(tax_sets, SUBJECT_IPR, SUBJECT_FUNFAM, SUBJECT_TAXA)
    assert not f3 and [i for i, _ in m3] == [0], f"taxon arm: fires={f3} mentions={m3}"
    print("self-test OK (7 assertions, 3 break-tests)")


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        return
    rule_id = sys.argv[1]
    d = fetch(rule_id)
    assert d["uniRuleId"] == rule_id, f"got {d['uniRuleId']} when asking for {rule_id}"
    sets = d["mainRule"]["conditionSets"]
    fires, mentions, undecidable = evaluate(
        sets, SUBJECT_IPR, SUBJECT_FUNFAM, SUBJECT_TAXA
    )
    print(f"{rule_id}: {len(sets)} condition sets")
    print(f"GO annotations granted by the rule: {go_annotations(d)}")
    print(f"\nSets that FIRE for {SUBJECT}: {len(fires)}")
    for i, txt in fires:
        print(f"  [{i}] {txt}")
    print(
        f"\nSets that only MENTION one of {SUBJECT}'s signatures but do NOT fire: "
        f"{len(mentions)}"
    )
    for i, txt in mentions:
        print(f"  [{i}] {txt}")
    print(f"\nSets undecidable by this evaluator: {len(undecidable)}")
    for i, txt in undecidable:
        print(f"  [{i}] {txt}")


if __name__ == "__main__":
    main()
