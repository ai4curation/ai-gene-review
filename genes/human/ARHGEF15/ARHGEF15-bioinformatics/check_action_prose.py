"""An action changed without its reason leaves a machine-readable field its prose denies.

Nothing in this repository compares `review.action` to the verbs in `review.reason` and
`review.summary`, so a row whose action was flipped in a later round can keep arguing for the
action it used to have. That is invisible to `just validate` and to every ontology check.

Rules encoded here, per action:
  REMOVE                 must not use retention verbs about the annotation
  ACCEPT / KEEP_AS_NON_CORE must not say the annotation is removed or discarded
  MODIFY                 must actually propose a replacement term

Usage:
    uv run --no-project --with pyyaml python check_action_prose.py
    uv run --no-project --with pyyaml python check_action_prose.py --self-test
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "ARHGEF15-ai-review.yaml"

# Verbs that assert the annotation is being kept. Matched case-insensitively on word
# boundaries.
#
# The first version of this list omitted 'remains', 'preserved' and 'untouched' -- which made
# ALL FOUR entries of RETENTION_EXEMPT below unreachable, since none of the exempt phrases
# contained any word the alternation matched. The exemptions were inert, and the mutation test
# that was supposed to prove them ("a REMOVE row using only exempted phrasings is NOT caught")
# passed vacuously: it passed because nothing in that sentence was a retention verb at all,
# not because the exemption suppressed anything. A test that would pass with the feature
# deleted is not testing the feature. `exempt_is_load_bearing` below now asserts the
# difference directly.
RETENTION = (
    r"\b(retain(?:ed|s)?|keep(?:s|ing)?|kept|left as|not removed|stays?|stayed"
    r"|remain(?:s|ed|ing)?|preserv(?:e|ed|es)|untouched)\b"
)
REMOVAL = r"\b(remov(?:e|ed|al)|discard(?:ed|s)?|delet(?:e|ed))\b"

# Phrases that legitimately use a retention verb on a REMOVE row because they are about
# something other than the annotation. Each must be specific enough not to be a loophole,
# and each must actually contain a RETENTION match or it is dead weight (asserted below).
RETENTION_EXEMPT = [
    r"the IntAct record is untouched",
    r"partner identity is preserved",
    r"the row remains a bare screen hit",
    r"it remains a single two-hybrid observation",
]


def rows(doc: dict) -> list[tuple[int, dict]]:
    return list(enumerate(doc["existing_annotations"]))


def check(doc: dict) -> list[str]:
    problems = []
    for i, a in rows(doc):
        rev = a.get("review") or {}
        action = rev.get("action")
        term = a["term"]["id"]
        prose = re.sub(r"\s+", " ", f"{rev.get('summary', '')} {rev.get('reason', '')}")
        label = f"row {i} {term} ({action})"

        if action == "REMOVE":
            scan = prose
            for ex in RETENTION_EXEMPT:
                scan = re.sub(ex, "", scan, flags=re.I)
            for m in re.finditer(RETENTION, scan, flags=re.I):
                ctx = scan[max(0, m.start() - 60) : m.end() + 60]
                problems.append(f"{label}: retention verb {m.group(0)!r} in prose :: ...{ctx}...")

        if action in {"ACCEPT", "KEEP_AS_NON_CORE"}:
            for m in re.finditer(REMOVAL, prose, flags=re.I):
                ctx = prose[max(0, m.start() - 60) : m.end() + 60]
                # 'merged away', 'not removed', 'is not removed' are fine on a kept row.
                if re.search(r"(not|never|rather than) remov", ctx, flags=re.I):
                    continue
                problems.append(f"{label}: removal verb {m.group(0)!r} in prose :: ...{ctx}...")

        if action == "MODIFY" and not rev.get("proposed_replacement_terms"):
            problems.append(f"{label}: MODIFY with no proposed_replacement_terms")

    return problems


def self_test() -> int:
    failures = []

    def expect(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    doc = yaml.safe_load(REVIEW.read_text())
    problems = check(doc)
    expect("the real document is clean", not problems, "; ".join(problems[:3]))
    expect("something was actually scanned", len(rows(doc)) == 31, str(len(rows(doc))))

    print("mutation tests:")

    def mutate(action: str, summary: str, reason: str, **extra) -> dict:
        return {
            "existing_annotations": [
                {"term": {"id": "GO:0005515"},
                 "review": {"action": action, "summary": summary, "reason": reason, **extra}}
            ]
        }

    cases = [
        ("REMOVE row saying the annotation is retained is caught",
         mutate("REMOVE", "", "The annotation is retained because the hit is reproducible."), True),
        ("REMOVE row saying 'kept' is caught",
         mutate("REMOVE", "This row is kept as a screen observation.", ""), True),
        ("REMOVE row using only exempted phrasings is NOT caught",
         mutate("REMOVE", "", "Removed; the IntAct record is untouched and the partner "
                              "identity is preserved in this document."), False),
        ("ACCEPT row saying the annotation is removed is caught",
         mutate("ACCEPT", "", "This annotation is removed as uninformative."), True),
        ("ACCEPT row saying 'rather than removed' is NOT caught",
         mutate("ACCEPT", "", "Kept rather than removed, because the donor row is an IDA."), False),
        ("MODIFY with no replacement term is caught",
         mutate("MODIFY", "", "Should be something better."), True),
        ("MODIFY with a replacement term is NOT caught",
         mutate("MODIFY", "", "Better term available.",
                proposed_replacement_terms=[{"id": "GO:0046875"}]), False),
    ]
    for name, d, should_fire in cases:
        got = bool(check(d))
        expect(name, got == should_fire, f"fired={got}")

    # Every exemption must be reachable: it has to contain something RETENTION matches, or it
    # suppresses nothing and is dead weight. This is the check that was missing.
    dead = [e for e in RETENTION_EXEMPT if not re.search(RETENTION, e, flags=re.I)]
    expect("every RETENTION_EXEMPT entry is reachable", not dead, str(dead))

    # And each exemption must be load-bearing: the same sentence must fire without it.
    def fires_without_exemptions(sentence: str) -> bool:
        scan = sentence
        return bool(re.search(RETENTION, scan, flags=re.I))

    for e in RETENTION_EXEMPT:
        sentence = f"Removed. {e.replace(chr(92), '')} and nothing else."
        suppressed = not bool(check(mutate("REMOVE", "", sentence)))
        expect(
            f"exemption is load-bearing: {e[:40]!r} suppresses a match that would otherwise fire",
            suppressed and fires_without_exemptions(sentence),
            f"suppressed={suppressed} would_fire={fires_without_exemptions(sentence)}",
        )

    print()
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = check(yaml.safe_load(REVIEW.read_text()))
    for p in problems:
        print(f"  {p}")
    print(f"action/prose contradictions: {len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
