#!/usr/bin/env python3
"""Print the whitespace-normalised context around a fragment in a cached publication,
so a ``supporting_text`` is copied from the source rather than typed from memory.

Prints the surrounding paragraph deliberately: a quote can be verbatim and TRUE while
the neighbouring sentence disconfirms the claim built on it (campaign brief), and no
automated gate can see that.

Usage:
    uv run python .../quote_finder.py 22547686 "biochemical isolation of SEC-like 2"
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PUBS = REPO / "publications"


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit('usage: quote_finder.py <pmid> "<fragment>" ["<fragment>" ...]')
    pmid = sys.argv[1]
    path = PUBS / f"PMID_{pmid}.md"
    if not path.exists():
        raise SystemExit(f"FATAL: {path} not cached. Run: just fetch-pmid {pmid}")
    flat = " ".join(path.read_text().split())
    missing = []
    for frag in sys.argv[2:]:
        i = flat.find(frag)
        print(f"[{'OK  ' if i >= 0 else 'MISS'}] {frag!r}")
        if i >= 0:
            print("    ..." + flat[max(0, i - 140): i + 420] + "...")
        else:
            missing.append(frag)
        print()
    if missing:
        raise SystemExit(f"{len(missing)} fragment(s) NOT present verbatim: {missing}")


if __name__ == "__main__":
    main()
