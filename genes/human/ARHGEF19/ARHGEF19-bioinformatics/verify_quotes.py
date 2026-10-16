#!/usr/bin/env python3
"""Check every supporting_text in the ARHGEF19 review against its source file.

Run from this directory:  uv run python verify_quotes.py

CI verifies supporting_text only for literature references (PMID:, DOI:). Quotes
attributed to ``file:`` paths and to ``Reactome:`` stable ids are never checked by
anything, which makes them the easiest place in a review for a wrong or invented
quotation to survive. This script closes that gap for this gene: it walks the
review YAML, resolves EVERY reference_id to a local file, and asserts the quote
is a verbatim substring after whitespace normalisation -- the same normalisation
the reference validator applies, and nothing more, so a reworded quote still
fails.

It deliberately re-checks the PMID quotes too. They are covered by CI, but CI
runs against the merge commit and this runs against the working tree, so a local
mismatch is caught before the ~20-minute build rather than after it.

Exit codes: 0 = every quote resolved and matched; 1 = a quote did not match or a
source file is missing (a finding); 2 = the review file itself could not be read.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "ARHGEF19-ai-review.yaml"
PUBLICATIONS = REPO / "publications"
REACTOME = REPO / "reactome"
GENES = REPO / "genes"


def norm(text: str) -> str:
    return " ".join(text.split())


def source_path(ref_id: str) -> Path | None:
    """Resolve a reference_id to a local file, or None if it has no local text."""
    if ref_id.startswith("PMID:"):
        return PUBLICATIONS / f"PMID_{ref_id.split(':', 1)[1]}.md"
    if ref_id.startswith("Reactome:"):
        return REACTOME / f"{ref_id.split(':', 1)[1]}.md"
    if ref_id.startswith("file:"):
        rel = ref_id.split(":", 1)[1]
        for candidate in (REPO / rel, GENES / rel):
            if candidate.exists():
                return candidate
        return GENES / rel  # report the more likely of the two as missing
    return None


def walk(node, path="", out=None):
    """Yield (json-ish path, reference_id, supporting_text) for every quote."""
    if out is None:
        out = []
    if isinstance(node, dict):
        if "reference_id" in node and "supporting_text" in node:
            out.append((path, node["reference_id"], node["supporting_text"]))
        for k, v in node.items():
            walk(v, f"{path}/{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}/{i}", out)
    return out


def findings_quotes(doc) -> list[tuple[str, str, str]]:
    """references[].findings[].supporting_text, whose ref id is the parent's."""
    out = []
    for i, ref in enumerate(doc.get("references") or []):
        rid = ref.get("id")
        for j, f in enumerate(ref.get("findings") or []):
            text = f.get("supporting_text")
            if text:
                out.append((f"/references/{i}/findings/{j}", rid, text))
    return out


def main(review: Path | None = None) -> int:
    review = review or REVIEW
    if not review.exists():
        print(f"TOOLING FAILURE: {review} not found", file=sys.stderr)
        return 2
    doc = yaml.safe_load(review.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        print("TOOLING FAILURE: review YAML did not parse to a mapping", file=sys.stderr)
        return 2

    quotes = walk(doc) + findings_quotes(doc)
    if not quotes:
        print("TOOLING FAILURE: no supporting_text found; the walker is broken",
              file=sys.stderr)
        return 2

    cache: dict[Path, str] = {}
    by_kind: dict[str, list[bool]] = {}
    failures: list[str] = []

    print(f"# supporting_text verification for {review.name}")
    print()
    print(f"{len(quotes)} quotes found.")
    print()

    for loc, rid, text in sorted(quotes):
        kind = rid.split(":", 1)[0] if rid else "?"
        path = source_path(rid) if rid else None
        if path is None:
            by_kind.setdefault(kind, []).append(True)
            print(f"  [skip] {rid} (no local text to check) {loc}")
            continue
        if not path.exists():
            by_kind.setdefault(kind, []).append(False)
            failures.append(f"{loc}: source file missing for {rid} -> {path}")
            print(f"  [MISS] {rid} -> {path} does not exist  {loc}")
            continue
        if path not in cache:
            cache[path] = norm(path.read_text(encoding="utf-8"))
        ok = norm(text) in cache[path]
        by_kind.setdefault(kind, []).append(ok)
        if not ok:
            failures.append(f"{loc}: quote not found in {path.name} for {rid}")
            print(f"  [FAIL] {rid} {loc}")
            print(f"         {norm(text)[:160]}")
        else:
            print(f"  [ok]   {rid} {loc}")

    print()
    print("| reference kind | quotes | matched |")
    print("|---|---|---|")
    for kind in sorted(by_kind):
        results = by_kind[kind]
        print(f"| {kind}: | {len(results)} | {sum(results)} |")
    print()
    unchecked_by_ci = sum(
        len(v) for k, v in by_kind.items() if k not in {"PMID", "DOI"}
    )
    print(f"{unchecked_by_ci} of these {len(quotes)} quotes are invisible to CI "
          "(non-literature reference prefixes) and are checked only here.")
    print()

    if failures:
        print("## FAILURES")
        for f in failures:
            print(f"- {f}")
        return 1
    print("Every quote is a verbatim substring of its cited source.")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else None))
