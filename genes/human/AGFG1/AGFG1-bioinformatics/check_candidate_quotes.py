"""Pre-check candidate supporting_text quotes before they go into the review YAML.

Mirrors the whitespace-normalised substring test that checkquotes.py and
linkml-reference-validator apply, so a bad quote is caught here rather than in CI.
Deliberately stricter than the CI validator: it does NOT strip punctuation, so a
hyphen/en-dash or straight/curly-quote mismatch fails here even though CI would
normalise it away.

Usage: uv run python check_candidate_quotes.py candidate_quotes.tsv
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve()
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def source_text(ref_id: str) -> tuple[Path, str] | None:
    if ref_id.startswith("PMID:"):
        p = REPO / "publications" / f"PMID_{ref_id.split(':', 1)[1]}.md"
    elif ref_id.startswith("file:"):
        rel = ref_id.split(":", 1)[1]
        p = REPO / "genes" / rel
        if not p.exists():
            p = REPO / rel
    else:
        return None
    return p, (p.read_text() if p.exists() else "")


def main() -> int:
    path = Path(sys.argv[1])
    bad = 0
    checked = 0
    with path.open() as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if not row or row[0].startswith("#"):
                continue
            assert len(row) == 2, f"expected 2 columns, got {len(row)}: {row!r}"
            ref, quote = row
            got = source_text(ref)
            if got is None:
                print(f"SKIP (not text-checkable) {ref}")
                continue
            p, text = got
            if not text:
                print(f"MISSING SOURCE {ref} -> {p}")
                bad += 1
                continue
            checked += 1
            if norm(quote) not in norm(text):
                bad += 1
                print(f"NOT FOUND in {p.name}:\n    {quote}")
    assert checked > 0, "checked zero quotes - a vacuous pass"
    print(f"\n{checked} quotes checked, {bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
