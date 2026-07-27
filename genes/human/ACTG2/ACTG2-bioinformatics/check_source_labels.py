"""Guard: every accession named in the review's prose must match the computed record.

Why this exists. `analyze_actg2.py` asserts that the WITH/FROM *token* lists in the review
cannot drift from GOA, because they are built from the GOA field. That assertion says nothing
about the human-readable `source_label` strings wrapped around those tokens, which were typed.
On the first round of this review six residue counts in those labels disagreed with the values
the script had computed from UniProt (Candida ACT1, C. elegans act-5 and all four Dictyostelium
actins) - a detector and a mutator disagreeing on scope, which is exactly the failure the
campaign brief warns about. This closes it.

What is checked, over the whole YAML (not only `source_label`, because the same accessions are
also named in `summary`, `reason` and `comment` prose):

  1. Every `(ACCESSION, N aa)` pair anywhere in the file matches `canonical_source_labels`
     in results.json. A mismatched residue count is an error.
  2. Every `(ACCESSION, Swiss-Prot|TrEMBL)` pair anywhere in the file matches the computed
     reviewed status.
  3. Every `source_entities[].source_id` that names a UniProt accession, and every
     WITH/FROM-derived accession, is one the analysis actually resolved - so a source cannot be
     silently invented or relabelled.
  4. Presence, not just consistency: every accession the analysis resolved as a donor for a
     reviewed row must appear somewhere in the YAML. A guard that only validates on match is
     defeatable by deleting the thing it guards.

Run `--self-test` to exercise the guard against deliberately broken copies. A self-test proves
the guards that were thought of fire; it cannot show which guard was not written, so the
mutations below are kept explicit and each asserts its target string is present *before*
mutating, so a drifted anchor is an error rather than a silent pass.

Usage:
  uv run python check_source_labels.py
  uv run python check_source_labels.py --self-test
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ACTG2-ai-review.yaml"
RESULTS = HERE / "results.json"

ACC_RE = r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}"
# NB: the window must NOT exclude ")", or labels of the form
# "... A0A1D8PFR4, TrEMBL (unreviewed), 376 aa)" are invisible to the guard - the closing
# paren of "(unreviewed)" sits between the accession and the residue count. That scope bug
# hid two of the six drifted lengths on the first run of this guard, which is the same
# detector/mutator scope mismatch the guard was written to catch.
LENGTH_RE = re.compile(rf"\b({ACC_RE})\b[^\n]{{0,80}}?\b(\d+) aa\b")
STATUS_RE = re.compile(rf"\b({ACC_RE})\b[^\n]{{0,60}}?\b(Swiss-Prot|TrEMBL)\b")


def load(review_text: str | None = None) -> tuple[str, dict]:
    if not REVIEW.exists():
        raise FileNotFoundError(f"missing {REVIEW}\n  regenerate with: just fetch-gene human ACTG2")
    if not RESULTS.exists():
        raise FileNotFoundError(f"missing {RESULTS}\n  regenerate with: uv run python analyze_actg2.py")
    text = review_text if review_text is not None else REVIEW.read_text()
    results = json.loads(RESULTS.read_text())
    if "canonical_source_labels" not in results:
        raise RuntimeError(
            "results.json has no canonical_source_labels; re-run analyze_actg2.py"
        )
    return text, results


def parse_canonical(labels: dict[str, str]) -> dict[str, dict]:
    out = {}
    for acc, label in labels.items():
        m = re.search(r", (Swiss-Prot|TrEMBL)[^,]*, (\d+) aa\)$", label)
        if not m:
            raise RuntimeError(f"canonical label for {acc} is not in the expected form: {label!r}")
        out[acc] = {"reviewed": m.group(1), "length": int(m.group(2)), "label": label}
    return out


def check(review_text: str | None = None) -> list[str]:
    text, results = load(review_text)
    canon = parse_canonical(results["canonical_source_labels"])
    problems: list[str] = []

    # 1. residue counts
    for acc, n in LENGTH_RE.findall(text):
        if acc not in canon:
            problems.append(f"length claim for unknown accession {acc} ({n} aa)")
        elif int(n) != canon[acc]["length"]:
            problems.append(
                f"{acc}: YAML says {n} aa, computed record says {canon[acc]['length']} aa"
            )

    # 2. reviewed status
    for acc, status in STATUS_RE.findall(text):
        if acc in canon and status != canon[acc]["reviewed"]:
            problems.append(
                f"{acc}: YAML says {status}, computed record says {canon[acc]['reviewed']}"
            )

    # 3. no invented UniProt source_ids
    for acc in re.findall(rf"source_id: UniProtKB:({ACC_RE})", text):
        if acc not in canon:
            problems.append(f"source_id UniProtKB:{acc} was never resolved by the analysis")

    # 4. presence: every resolved donor must be named somewhere in the review
    for acc in canon:
        if acc not in text:
            problems.append(f"resolved donor {acc} ({canon[acc]['label']}) is absent from the review")

    return problems


SELF_TEST_MUTATIONS = [
    # (description, anchor that must be present, replacement, substring expected in the error)
    (
        "wrong residue count",
        "A0A1D8PFR4, TrEMBL (unreviewed), 376 aa",
        "A0A1D8PFR4, TrEMBL (unreviewed), 375 aa",
        "A0A1D8PFR4: YAML says 375 aa",
    ),
    (
        "unreviewed entry promoted to Swiss-Prot",
        "O45815, TrEMBL (unreviewed), 375 aa",
        "O45815, Swiss-Prot, 375 aa",
        "O45815: YAML says Swiss-Prot",
    ),
    (
        "invented source_id",
        "source_id: UniProtKB:P68137",
        "source_id: UniProtKB:P99999",
        "UniProtKB:P99999 was never resolved",
    ),
    # The presence check (4) needs its own mutation. Relabelling a single source_id does NOT
    # exercise it, because the accession usually survives elsewhere in the row's prose - the
    # first version of this self-test asserted the wrong expectation and the guard "failed"
    # while behaving correctly. Removing every occurrence is what tests deletion.
    (
        "donor removed entirely",
        "Q553U6",
        "QZZZZZ9",
        "resolved donor Q553U6",
    ),
]


def self_test() -> int:
    text = REVIEW.read_text()
    base = check(text)
    if base:
        print("self-test cannot run: the unmutated review already has problems:")
        for p in base:
            print("  -", p)
        return 1
    failures = 0
    for desc, anchor, replacement, expected in SELF_TEST_MUTATIONS:
        if anchor not in text:
            print(f"SELF-TEST BROKEN [{desc}]: anchor not present in the review: {anchor!r}")
            failures += 1
            continue
        # "donor removed entirely" must replace every occurrence, not just the first, or the
        # presence check cannot fire; the others are single-site by design.
        count = -1 if desc == "donor removed entirely" else 1
        mutated = text.replace(anchor, replacement, count)
        if mutated == text:
            print(f"SELF-TEST BROKEN [{desc}]: mutation was a no-op")
            failures += 1
            continue
        problems = check(mutated)
        if not any(expected in p for p in problems):
            print(f"SELF-TEST FAILED [{desc}]: guard did not report {expected!r}; got {problems}")
            failures += 1
        else:
            print(f"self-test ok: {desc}")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    problems = check()
    for p in problems:
        print("PROBLEM:", p)
    print(f"\n{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
