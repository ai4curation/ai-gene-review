"""Invariant checks over the EMITTED AGFG1 review YAML.

These are the checks that the repo validator and checkquotes.py cannot make, each
one written because the campaign has recorded a real defect of that shape:

A. duplicate YAML mapping keys - PyYAML keeps the LAST and silently discards the
   earlier one, so a quote that parsing removed cannot fail any gate that walks
   the parsed tree. Detected with a strict loader over the RAW text.
B. YAML anchors/aliases - legal, but they multiply a single object across rows so
   raw-vs-parsed counts stop meaning anything. Asserted absent.
C. row coverage - one existing_annotations entry per DISTINCT GOA row, plus the
   NEW proposals, reconciled explicitly rather than trusted.
D. supporting_entities built from the GOA WITH/FROM column, compared as SETS per
   (term, evidence, reference); hand-maintained lists have drifted on several genes.
E. every quote-bearing key in the raw text is reachable in the parsed walk, so a
   blind spot in checkquotes.py (which does not walk provenance) shows up as a
   count mismatch rather than as silence.
F. summary/action agreement in BOTH directions: no summary's opening clause may
   name an action other than its own row's, and every action must have a summary.
G. core_functions terms must be backed by an ACCEPT or NEW row, and every ACCEPT
   row's term must appear somewhere in core_functions - the direction that
   otherwise goes unwritten.

Usage:
    uv run python audit_review.py
    uv run python audit_review.py --self-test
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
GOA = HERE.parent / "AGFG1-goa.tsv"

# Opening-clause vocabulary -> the action it names.
OPENERS = {
    "accepted": "ACCEPT",
    "kept as non-core": "KEEP_AS_NON_CORE",
    "removed": "REMOVE",
    "modified": "MODIFY",
    "over-annotated": "MARK_AS_OVER_ANNOTATED",
    "undecided": "UNDECIDED",
    "proposed": "NEW",
}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise AssertionError(f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def walk_quotes(node, path=""):
    """Every (path, reference_id, supporting_text) in the parsed document, from
    supported_by, findings AND provenance - checkquotes.py omits the last."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield (
                            f"{path}.{k}[{i}]",
                            e.get("reference_id") or node.get("id"),
                            e["supporting_text"],
                        )
            else:
                yield from walk_quotes(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, e in enumerate(node):
            yield from walk_quotes(e, f"{path}[{i}]")


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def audit(text: str) -> list[str]:
    problems: list[str] = []

    # A. duplicate keys
    try:
        doc = yaml.load(text, Loader=StrictLoader)
    except AssertionError as exc:
        problems.append(f"A: {exc}")
        doc = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        problems.append(f"A: YAML parse error: {exc}")
        return problems

    # B. anchors / aliases
    anchors = re.findall(r"(?m)^\s*-?\s*&id\d+", text)
    aliases = re.findall(r"(?m)^\s*-?\s*\*id\d+", text)
    if anchors or aliases:
        problems.append(
            f"B: {len(anchors)} anchor(s) and {len(aliases)} alias(es) present; "
            "they multiply objects across rows and break raw-vs-parsed counts"
        )

    anns = doc.get("existing_annotations") or []
    if not anns:
        problems.append("B: no existing_annotations - a vacuous audit")
        return problems

    # C. row coverage
    rows = goa_rows()
    distinct = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"], r["QUALIFIER"])
        for r in rows
    }
    reviewed = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]
    new_rows = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    if len(reviewed) != len(distinct):
        problems.append(
            f"C: {len(reviewed)} non-NEW entries against {len(distinct)} distinct GOA "
            f"rows ({len(rows)} raw lines); {len(new_rows)} NEW proposals"
        )
    # Every GOA term must appear on some entry.
    goa_terms = {r["GO TERM"] for r in rows}
    entry_terms = {a["term"]["id"] for a in reviewed}
    missing = goa_terms - entry_terms
    if missing:
        problems.append(f"C: GOA terms with no review entry: {sorted(missing)}")

    # D. supporting_entities vs the GOA WITH/FROM column, as sets
    goa_wf: dict[tuple, set[str]] = defaultdict(set)
    for r in rows:
        if r["WITH/FROM"]:
            key = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"])
            goa_wf[key] = set(r["WITH/FROM"].split("|"))
    matched = 0
    for a in reviewed:
        se = set(a.get("supporting_entities") or [])
        if not se:
            continue
        key = None
        for k, v in goa_wf.items():
            if k[0] == a["term"]["id"] and k[2] == a["original_reference_id"] and v == se:
                key = k
                break
        if key is None:
            problems.append(
                f"D: supporting_entities for {a['term']['id']} / "
                f"{a['original_reference_id']} match no GOA WITH/FROM field: {sorted(se)}"
            )
        else:
            matched += 1
    if matched == 0:
        problems.append("D: zero supporting_entities lists checked - vacuous")

    # E. raw vs parsed quote counts
    raw = len(re.findall(r"(?m)^\s*-?\s*supporting_text:", text))
    parsed = len(list(walk_quotes(doc)))
    if raw != parsed:
        problems.append(f"E: {raw} raw supporting_text keys vs {parsed} reachable in the walk")

    # F. summary opener vs action, both directions
    for a in anns:
        rev = a.get("review") or {}
        action = rev.get("action")
        summary = (rev.get("summary") or "").strip()
        if not action:
            problems.append(f"F: entry for {a['term']['id']} has no action")
            continue
        if not summary:
            problems.append(f"F: {a['term']['id']} / {action} has no summary")
            continue
        low = summary.lower()
        for phrase, named in OPENERS.items():
            if low.startswith(phrase) and named != action:
                problems.append(
                    f"F: {a['term']['id']} summary opens '{phrase}' but action is {action}"
                )

    # G. core_functions terms vs kept rows, both directions
    kept_terms = {
        a["term"]["id"]
        for a in anns
        if (a.get("review") or {}).get("action") in ("ACCEPT", "NEW")
    }
    replacement_terms = {
        t["id"]
        for a in anns
        for t in ((a.get("review") or {}).get("proposed_replacement_terms") or [])
    }
    backed = kept_terms | replacement_terms
    cf_terms = set()
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            if cf.get(slot):
                cf_terms.add(cf[slot]["id"])
        for slot in ("directly_involved_in", "locations", "anatomical_locations", "substrates"):
            for t in cf.get(slot) or []:
                cf_terms.add(t["id"])
    if not cf_terms:
        problems.append("G: no core_functions terms - vacuous")
    for t in sorted(cf_terms - backed):
        problems.append(
            f"G: core_functions term {t} is not backed by an ACCEPT/NEW row or a "
            "proposed replacement term"
        )
    for t in sorted(
        {a["term"]["id"] for a in anns if (a.get("review") or {}).get("action") == "ACCEPT"}
        - cf_terms
    ):
        problems.append(f"G: ACCEPT row {t} does not appear in core_functions")

    # Same-term-same-action, except GO:0005515 where per-partner verdicts are allowed
    # (validator.py deliberately skips that term).
    by_term: dict[str, Counter] = defaultdict(Counter)
    for a in reviewed:
        by_term[a["term"]["id"]][(a.get("review") or {}).get("action")] += 1
    for term, actions in by_term.items():
        if term != "GO:0005515" and len(actions) > 1:
            problems.append(f"H: {term} has divergent actions {dict(actions)}")

    return problems


def self_test() -> None:
    """Each break-test asserts the mutation applied, that the guard fired, and that
    the message is the expected one."""
    text = REVIEW.read_text()
    assert audit(text) == [], f"baseline is not clean: {audit(text)}"

    def expect(mutated: str, marker: str, label: str) -> None:
        assert mutated != text, f"{label}: mutation did not change the document"
        probs = audit(mutated)
        assert any(p.startswith(marker) for p in probs), (
            f"{label}: guard {marker} did not fire; got {probs}"
        )

    # A: duplicate key
    expect(text.replace("status: COMPLETE", "status: COMPLETE\nstatus: COMPLETE", 1), "A", "dup key")

    # B: anchor
    expect(text.replace("existing_annotations:\n- term:", "existing_annotations:\n- &id001\n  term:", 1), "B", "anchor")

    # C: drop an entry - remove the last NEW block by truncating at core_functions
    #    and re-adding it minus one entry is fragile, so instead drop a GOA row's
    #    entry by deleting its term id, which breaks the coverage set.
    drop = text.replace("    id: GO:0045109\n    label: intermediate filament organization", "    id: GO:9999999\n    label: fake", 1)
    expect(drop, "C", "coverage")

    # D: corrupt a supporting_entities list
    expect(text.replace("  - PANTHER:PTN002353603\n", "", 1), "D", "supporting_entities")

    # F: opener contradicting the action
    expect(
        text.replace(
            "      Removed. The direction of the interaction is inverted",
            "      Accepted. The direction of the interaction is inverted",
            1,
        ),
        "F",
        "opener",
    )

    # G: a core_functions term with no backing row
    expect(
        text.replace(
            "  - id: GO:0005905\n    label: clathrin-coated pit\n  - id: GO:0030136",
            "  - id: GO:0000045\n    label: autophagosome assembly\n  - id: GO:0030136",
            1,
        ),
        "G",
        "core_functions",
    )

    # H: divergent actions on one non-GO:0005515 term
    expect(
        text.replace(
            "    reason: Clathrin recruiting PIK3C2A is not a step involving AGFG1.",
            "    reason: Clathrin recruiting PIK3C2A is not a step involving AGFG1.\n    x: y",
            1,
        ).replace("    action: KEEP_AS_NON_CORE\n    reason: Clathrin recruiting", "    action: REMOVE\n    reason: Clathrin recruiting", 1),
        "H",
        "same-term-same-action",
    )
    print("self-test OK (7 break-tests, each asserting mutation + firing)")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    problems = audit(REVIEW.read_text())
    for p in problems:
        print(p)
    print(f"\n{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
