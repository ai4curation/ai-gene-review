#!/usr/bin/env python3
"""Check every supporting_text in the review against its cached publication.

Why this is not redundant with `just validate`: for a reference whose cache is
abstract-only, `validator.py` downgrades a non-matching quote from ERROR to
**WARNING** (see the `declared_unavailable or cache_has_full_text is False`
branch). Six of this review's references are abstract-only, so a paraphrase there
would not fail the build -- it would pass with a warning that is easy to miss in a
run that already carries an unrelated warning.

This script fails loudly instead, and reports the abstract-only subset separately
so the weaker-gated quotes are visible as a group.

Matching uses the same normalisation the repo's validator uses (case, whitespace,
punctuation, and Greek letters spelled out), so it neither invents failures the
validator would not see nor hides ones it would.

Run:  uv run python verify_quotes.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)


def repo_root() -> Path:
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in (base, *base.parents):
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit("repo root not found")


ROOT = repo_root()
REVIEW = ROOT / "genes/human/ARGLU1/ARGLU1-ai-review.yaml"
PUBS = ROOT / "publications"

norm = SupportingTextValidator.normalize_text


def collect(doc) -> list[tuple[str, str, str]]:
    """Yield (path, reference_id, supporting_text) for every quote in the document."""
    out: list[tuple[str, str, str]] = []

    def walk(node, path="root"):
        if isinstance(node, dict):
            ref = node.get("reference_id")
            txt = node.get("supporting_text")
            if isinstance(ref, str) and isinstance(txt, str) and txt.strip():
                out.append((path, ref, txt))
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")

    walk(doc)
    return out


def check(doc) -> tuple[list[str], int, int, list[str], int]:
    quotes = collect(doc)
    if not quotes:
        raise SystemExit("no supporting_text found -- collector is wrong; a zero "
                         "here would read as a pass.")

    problems: list[str] = []
    checked = skipped = 0
    abstract_only: list[str] = []

    for path, ref, txt in quotes:
        if not ref.startswith("PMID:"):
            skipped += 1
            continue
        pub = PUBS / f"PMID_{ref.split(':', 1)[1]}.md"
        if not pub.exists():
            problems.append(f"{path}: {ref} has no cached publication at {pub.name}")
            continue
        body = pub.read_text()
        full_text = "full_text_available: true" in body.split("---")[1] if "---" in body else False
        if not full_text and ref not in abstract_only:
            abstract_only.append(ref)
        if norm(txt) not in norm(body):
            problems.append(
                f"{path}: quote NOT a verbatim (normalised) substring of {pub.name}"
                f"{'  [abstract-only cache: the repo validator would only WARN here]' if not full_text else ''}"
                f"\n      {txt[:140]}"
            )
        checked += 1

    return problems, checked, skipped, abstract_only, len(quotes)


def self_test() -> int:
    """Break a quote and confirm detection -- for each cache kind separately.

    The abstract-only case is tested on its own because that is exactly where the
    repo validator weakens to a WARNING, so it is the case this script exists to
    cover and the one whose failure would be least visible.
    """
    doc = yaml.safe_load(REVIEW.read_text())
    problems, *_ = check(doc)
    if problems:
        print("SELF-TEST ABORTED: baseline already has problems:")
        for p in problems:
            print("  -", p)
        return 1

    failures = []
    for label, want_ref in (("full-text source", "PMID:30698747"),
                            ("abstract-only source", "PMID:22923044")):
        import copy
        mutated = copy.deepcopy(doc)
        hits = [t for t in collect(mutated) if t[1] == want_ref]
        if len(hits) < 1:
            failures.append(f"{label}: no quote cites {want_ref}; target drifted")
            continue

        # Mutate the first quote citing that reference, in place.
        target_path = hits[0][0]
        changed = 0

        def walk(node):
            nonlocal changed
            if isinstance(node, dict):
                if (node.get("reference_id") == want_ref
                        and isinstance(node.get("supporting_text"), str)
                        and changed == 0):
                    node["supporting_text"] = (
                        node["supporting_text"] + " and then something nobody wrote."
                    )
                    changed += 1
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(mutated)
        if changed != 1:
            failures.append(f"{label}: expected to mutate exactly 1 quote, did {changed}")
            continue
        probs, *_ = check(mutated)
        hit = [p for p in probs if want_ref.split(":")[1] in p or "NOT a verbatim" in p]
        if hit:
            print(f"  ok  {label} ({want_ref}, {target_path.split('.')[-1]}): detected")
        else:
            failures.append(f"{label}: corrupted quote NOT detected")

    if failures:
        print("\nSELF-TEST FAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print("\nself-test: corrupted quotes detected in both cache kinds")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()

    doc = yaml.safe_load(REVIEW.read_text())
    problems, checked, skipped, abstract_only, n_quotes = check(doc)

    print(f"quotes found           : {n_quotes}")
    print(f"checked (PMID-backed)  : {checked}")
    print(f"skipped (non-PMID refs): {skipped}")
    print(f"abstract-only sources  : {len(abstract_only)} -> {sorted(abstract_only)}")
    print("   (a paraphrase against these would only WARN in `just validate`)")
    print()

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("every quote is a verbatim (normalised) substring of its cached source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
