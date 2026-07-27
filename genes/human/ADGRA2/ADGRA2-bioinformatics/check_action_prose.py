#!/usr/bin/env python3
"""Assert that every annotation's prose names the action the annotation actually has,
and that no reason argues the same point twice.

Why this exists. Four separate rounds on this gene hit the same shape: a change landed on
the structured field but not on every sentence describing it.

  round 1  the two GDB `TAS` rows were recalibrated MARK_AS_OVER_ANNOTATED -> REMOVE ...
  round 4  ... but both still carried "Marked over-annotated rather than removed because
           the 7TM plus GAIN-B architecture is genuine", so a curator reading a REMOVE
           row's justification was told the action was over-annotation.

The root cause is structural, not clerical: one shared prose constant (`GPCR_REASON`) was
appended to rows with *different* actions, and it ended with an action-specific sentence.
Re-reading the prose is exactly how this kept being missed. **Select on the stable entity**
-- iterate `review.action`, then test the prose of that block -- so a new row inherits the
check automatically and cannot be skipped by wording drift.

The second check catches the other half of the same round: a superseding paragraph inserted
without deleting the one it supersedes, so each REMOVE reason made the same argument twice.

Run:  python3 check_action_prose.py [--self-test]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "ADGRA2-ai-review.yaml"

# A phrase that names an action, and the action it implies. Matched case-insensitively
# against summary + reason. Keep these keyed to how a *verdict* is announced, not to any
# incidental mention of another row's action -- see ATTRIBUTION_SUBJECT below.
ACTION_PHRASES: dict[str, str] = {
    "marked over-annotated rather than removed": "MARK_AS_OVER_ANNOTATED",
    "marked as over-annotated rather than removed": "MARK_AS_OVER_ANNOTATED",
    "removed rather than marked over-annotated": "REMOVE",
    "this row is removed": "REMOVE",
    "accepted as core": "ACCEPT",
}

# A reason may legitimately discuss ANOTHER row's action, e.g. "The InterPro rows ... are
# marked over-annotated". Such mentions are attributed and must not trip the guard.
#
# The exemption is scoped to the SENTENCE containing the phrase, via the sentences() helper
# below. An earlier version used a regex ending in `[^.]{0,200}?` -- a lazy, zero-length-
# matchable quantifier, so it succeeded on the bare subject anywhere in a 220-character
# lookbehind window regardless of sentence boundaries, silently widening the exemption to
# roughly "an attribution appeared somewhere nearby". Sentence scope is both narrower and
# actually the thing meant.
ATTRIBUTION_SUBJECT = re.compile(
    r"\b(the\s+)?(interpro(2go)?\s+rows?|iea\s+rows?|those\s+rows?|other\s+rows?"
    r"|two\s+removed\s+rows?|sibling\s+review|ADGRA[13]\b[^.]{0,40}review)", re.I
)

# Snippets that must appear at most once per reason -- these are distinctive fragments, not
# whole sentences, chosen so a reworded restatement still collides. A superseding edit that
# forgets to delete what it supersedes shows up here.
NO_DUPLICATE_SNIPPETS = [
    "a paper cannot make 25 gene-specific author statements",
    "abstract-only in the cache",
    "Its abstract describes genome-database searching",
    "membrane localisation is directly demonstrated for ADGRA2",
]


def sentences(text: str) -> list[str]:
    return re.split(r"(?<=[.;])\s+", text or "")


def check(review: Path = REVIEW, verbose: bool = True) -> list[str]:
    doc = yaml.safe_load(review.read_text())
    anns = doc["existing_annotations"]
    assert anns, "no existing_annotations parsed -- the guard would pass vacuously"

    problems: list[str] = []
    checked = 0

    for i, a in enumerate(anns):
        r = a.get("review") or {}
        action = r.get("action")
        assert action, f"annotation[{i}] has no action -- cannot reconcile prose against it"
        term, ev = a["term"]["id"], a["evidence_type"]
        label = f"[{i}] {term} {ev} action={action}"
        blob = f"{r.get('summary', '')} {r.get('reason', '')}"
        checked += 1

        # 1. Prose must not announce a different action than the block actually has.
        for phrase, implied in ACTION_PHRASES.items():
            for m in re.finditer(re.escape(phrase), blob, re.I):
                if implied == action:
                    continue
                # Allow an explicitly attributed mention of another row's action, scoped to
                # the sentence the phrase actually sits in -- not to a fixed-width window.
                host = next((sent for sent in sentences(blob)
                             if phrase.lower() in sent.lower()), "")
                if ATTRIBUTION_SUBJECT.search(host):
                    continue
                problems.append(
                    f"{label}: prose says {phrase!r}, which names {implied}, "
                    f"but this block's action is {action}"
                )

        # 2. No reason should argue the same point twice.
        for snip in NO_DUPLICATE_SNIPPETS:
            n = (r.get("reason") or "").count(snip)
            if n > 1:
                problems.append(f"{label}: reason repeats {snip!r} {n} times")

    if verbose:
        print(f"checked {checked} annotations against their own action field")
        by = {}
        for a in anns:
            by[a["review"]["action"]] = by.get(a["review"]["action"], 0) + 1
        print("actions:", dict(sorted(by.items())))
    return problems


def self_test() -> None:
    import tempfile

    base = REVIEW.read_text()

    # Happy path FIRST. An agreement check that fails on perfect agreement is a defect this
    # campaign has actually seen, so the clean case is exercised explicitly.
    assert check(verbose=False) == [], f"guard fires on the clean file: {check(verbose=False)}"

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        # 1. The exact round-4 defect must be detected: an over-annotation sentence on a
        #    REMOVE row, unattributed.
        d = yaml.safe_load(base)
        tgt = next(a for a in d["existing_annotations"] if a["review"]["action"] == "REMOVE")
        tgt["review"]["reason"] += " Marked over-annotated rather than removed because the fold is genuine."
        p = td / "wrongaction.yaml"
        p.write_text(yaml.safe_dump(d, sort_keys=False))
        probs = check(p, verbose=False)
        assert any("names MARK_AS_OVER_ANNOTATED" in x for x in probs), probs

        # 2. The SAME sentence, explicitly attributed to another row, must NOT fire --
        #    otherwise the guard forbids legitimate cross-referencing and would be worked
        #    around rather than obeyed.
        d2 = yaml.safe_load(base)
        tgt2 = next(a for a in d2["existing_annotations"] if a["review"]["action"] == "REMOVE")
        tgt2["review"]["reason"] += (
            " The InterPro rows carrying the same term are marked over-annotated rather than removed,"
            " because the fold really is present there."
        )
        p2 = td / "attributed.yaml"
        p2.write_text(yaml.safe_dump(d2, sort_keys=False))
        assert check(p2, verbose=False) == [], check(p2, verbose=False)

        # 3. A duplicated argument must be detected.
        d3 = yaml.safe_load(base)
        tgt3 = next(a for a in d3["existing_annotations"] if a["review"]["action"] == "REMOVE")
        tgt3["review"]["reason"] += " Again: a paper cannot make 25 gene-specific author statements about coupling."
        p3 = td / "dup.yaml"
        p3.write_text(yaml.safe_dump(d3, sort_keys=False))
        probs = check(p3, verbose=False)
        assert any("repeats" in x for x in probs), probs

        # 4. A missing action must fail loudly rather than be skipped -- the "guard
        #    defeatable by deleting the thing it guards" failure mode.
        d4 = yaml.safe_load(base)
        d4["existing_annotations"][0]["review"].pop("action")
        p4 = td / "noaction.yaml"
        p4.write_text(yaml.safe_dump(d4, sort_keys=False))
        try:
            check(p4, verbose=False)
        except AssertionError:
            pass
        else:
            raise AssertionError("a block with no action was silently skipped")

        # 5. An empty annotation list must fail loudly, not pass vacuously.
        d5 = yaml.safe_load(base)
        d5["existing_annotations"] = []
        p5 = td / "empty.yaml"
        p5.write_text(yaml.safe_dump(d5, sort_keys=False))
        try:
            check(p5, verbose=False)
        except AssertionError:
            pass
        else:
            raise AssertionError("an empty review passed vacuously")

    print("self-test OK: 5 directions exercised (clean file passes; unattributed wrong-action "
          "sentence detected; attributed cross-reference allowed; duplicated argument detected; "
          "missing action and empty list both fail loudly)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        sys.exit(0)
    found = check()
    print()
    if found:
        for p in found:
            print("PROBLEM:", p)
        sys.exit(1)
    print("OK: every annotation's prose names its own action, and no reason argues a point twice")
