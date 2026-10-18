"""Check that every [PMID:N "quote"] in a markdown file is a verbatim substring of publications/PMID_N.md.

Whitespace runs (including the line breaks of hard-wrapped cached abstracts) are
collapsed to single spaces on both sides before matching; nothing else is normalized.

Usage: uv run python projects/DANRE_DUPLICATION/scripts/check_quotes.py FILE.md [...]
Exits non-zero if any quote is missing or not found.
"""

import re
import sys
from pathlib import Path

CITE = re.compile(r'\[PMID:(\d+) "(.+?)"\]')
WS = re.compile(r"\s+")


def norm(text: str) -> str:
    return WS.sub(" ", text).strip()


def main(paths: list[str]) -> int:
    bad = 0
    total = 0
    for p in paths:
        for pmid, quote in CITE.findall(Path(p).read_text()):
            total += 1
            pub = Path(f"publications/PMID_{pmid}.md")
            if not pub.exists():
                print(f"MISSING publication PMID:{pmid}")
                bad += 1
            elif norm(quote) not in norm(pub.read_text()):
                print(f"NOT FOUND PMID:{pmid}: {quote[:90]}")
                bad += 1
    print(f"{total - bad}/{total} quotes verified")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
