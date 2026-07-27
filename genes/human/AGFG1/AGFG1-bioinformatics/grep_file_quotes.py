"""Byte-exact verification of every `file:` supporting_text in the AGFG1 review,
by invoking `grep -F` on the target file.

Why this exists separately from checkquotes.py: the repo's reference validator
SKIPS `file:` references entirely, so those quotes are the one place in the
document where an invented or subtly-normalised quotation survives every
automated gate. checkquotes.py does check them but collapses whitespace and
lowercases; this script does neither, so it also catches hyphen vs en/em-dash,
straight vs curly quotes and non-breaking spaces - the characters a copy-paste
silently rewrites.

Fails loudly if it finds zero quotes to check, so it cannot report a vacuous pass.

Usage: uv run python grep_file_quotes.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
REPO = HERE
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent


def file_quotes(node, out: list[tuple[str, str]]) -> None:
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                for e in v:
                    if isinstance(e, dict) and e.get("supporting_text"):
                        rid = e.get("reference_id") or node.get("id")
                        if isinstance(rid, str) and rid.startswith("file:"):
                            out.append((rid[len("file:"):], e["supporting_text"]))
            else:
                file_quotes(v, out)
    elif isinstance(node, list):
        for e in node:
            file_quotes(e, out)


def resolve(rel: str) -> pathlib.Path:
    p = REPO / "genes" / rel
    return p if p.exists() else REPO / rel


def main() -> int:
    quotes: list[tuple[str, str]] = []
    file_quotes(yaml.safe_load(REVIEW.read_text()), quotes)
    assert quotes, "found zero file: quotes - refusing to report a vacuous pass"

    bad = 0
    for rel, quote in quotes:
        path = resolve(rel)
        if not path.exists():
            print(f"MISSING FILE: {rel}")
            bad += 1
            continue
        # YAML folds long scalars onto one line with single spaces; the target file
        # may wrap. Only single-line quotes can be grep -F'd verbatim, which is the
        # discipline the campaign brief requires for file: quotes.
        r = subprocess.run(
            ["grep", "-qF", "--", quote, str(path)], capture_output=True
        )
        if r.returncode != 0:
            print(f"NOT BYTE-EXACT in {rel}:\n    {quote}")
            bad += 1
    print(f"{len(quotes)} file: quotes checked with grep -F, {bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
