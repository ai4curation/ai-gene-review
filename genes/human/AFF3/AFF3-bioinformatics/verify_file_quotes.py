#!/usr/bin/env python3
"""Independent RAW-BYTE verification of every `file:` supporting_text in the review.

WHY THIS EXISTS SEPARATELY FROM audit_claims.py: `file:` quotes are the one place in the
document that CI does not check at all - the repo's reference validator verifies
supporting_text verbatim only for `PMID:` references - so they are a fabrication surface,
and an agent on another gene in this campaign invented two. audit_claims.py checks them
after whitespace normalisation; this script requires an EXACT byte-level substring match,
which is a different instrument and catches the substitutions normalisation lets through:
hyphen vs en-dash vs em-dash, straight vs curly quotes, and non-breaking spaces.

Fails if it verifies ZERO quotes - a checker that silently finds nothing to check is
reporting coverage it does not have.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/verify_file_quotes.py
    uv run python genes/human/AFF3/AFF3-bioinformatics/verify_file_quotes.py --self-test
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REVIEW = HERE.parent / "AFF3-ai-review.yaml"

SUSPECT_CHARS = {
    "–": "en dash", "—": "em dash", "‘": "left single quote",
    "’": "right single quote", "“": "left double quote",
    "”": "right double quote", " ": "non-breaking space",
}


def walk(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance") and isinstance(v, list):
                for e in v:
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield e.get("reference_id"), e["supporting_text"]
            else:
                yield from walk(v)
    elif isinstance(node, list):
        for e in node:
            yield from walk(e)


def target_for(ref: str) -> Path:
    rel = ref.split(":", 1)[1]
    p = REPO / "genes" / rel
    return p if p.exists() else REPO / rel


def check(doc) -> tuple[int, list[str]]:
    problems: list[str] = []
    n = 0
    for ref, txt in walk(doc):
        if not ref or not ref.startswith("file:"):
            continue
        target = target_for(ref)
        if not target.exists():
            problems.append(f"MISSING FILE {ref} -> {target}")
            continue
        body = target.read_text()
        if txt in body:
            n += 1
            chars = sorted({SUSPECT_CHARS[c] for c in txt if c in SUSPECT_CHARS})
            note = f"   [contains {', '.join(chars)}, matched exactly]" if chars else ""
            print(f"ok    {ref}\n        {txt[:100]}{note}")
        else:
            problems.append(f"NOT AN EXACT SUBSTRING {ref}: {txt!r}")
    return n, problems


def main() -> int:
    doc = yaml.safe_load(REVIEW.read_text())
    if "--self-test" in sys.argv:
        # Assert the mutation changes the document, then that the guard fires.
        import copy
        mutated = copy.deepcopy(doc)
        hits = 0
        for ann in mutated["existing_annotations"]:
            for sb in (ann.get("review") or {}).get("supported_by") or []:
                if str(sb.get("reference_id", "")).startswith("file:"):
                    # Swap an em dash for a hyphen if present, else corrupt a word.
                    old = sb["supporting_text"]
                    sb["supporting_text"] = (old.replace("—", "-") if "—" in old
                                             else old + " XYZZY")
                    assert sb["supporting_text"] != old, "mutation did not change the text"
                    hits += 1
                    break
            if hits:
                break
        assert hits == 1, f"self-test found {hits} file: quotes to mutate, expected 1"
        n, problems = check(mutated)
        if not problems:
            print("FAIL self-test: guard did not fire on a dash-substituted quote")
            return 1
        print(f"\nself-test ok: guard fired -> {problems[0][:140]}")
        return 0

    n, problems = check(doc)
    for p in problems:
        print(f"FAIL  {p}")
    if n == 0:
        print("FATAL: verified ZERO file: quotes - the extractor found nothing, which "
              "is not a pass")
        return 1
    print(f"\nverified {n} file: quote(s) by exact byte-level substring match")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
