"""Verify every quoted `supporting_text` against its source, including `file:` sources.

The repo's own reference validator only checks quotes attributed to `PMID:` references;
quotes attributed to `file:` paths are unchecked, and fabricated ones have shipped that way
before. This checker covers both, plus the inline `[PMID:... "..."]` quotes in the notes
file, which nothing checks at all.

It deliberately does NOT repair its input. No `\\n` unescaping, no hyphen joining, no
unicode folding beyond the one normalisation the repo validator itself applies
(`re.sub(r"\\s+", " ", ...)`). A checker that repairs the defect it exists to detect always
passes; the only normalisation permitted here is the one the thing being emulated performs.

Usage:
    uv run --no-project python check_quotes.py                 # check review + notes
    uv run --no-project python check_quotes.py --self-test     # prove it can fail
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path(__file__).parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "ARHGEF15-ai-review.yaml"
NOTES = GENE_DIR / "ARHGEF15-notes.md"

# Notes convention enforced here: a quotation is immediately followed by its source in
# square brackets --  "quoted text" [PMID:12345]  or  "quoted text" [file:human/X/Y.md].
# Anything long enough to be a quotation but NOT followed by a bracketed source is reported
# as UNATTRIBUTED rather than silently ignored, because an unattributed quotation is exactly
# the shape a fabricated one takes.
MIN_QUOTE_LEN = 25
# A quotation body may wrap across lines but never across a blank line, and may not itself
# contain a bracketed citation -- without that, an unbalanced inline quote elsewhere in the
# prose pairs up with the next one and manufactures a span that spills over a real citation.
_BODY = r'(?:(?!\n\s*\n)(?!\[(?:PMID:|file:))[^"])'
NOTE_ATTRIBUTED = re.compile(r'"(%s{%d,}?)"\s*\[(PMID:\d+|file:[^\]]+)\]' % (_BODY, MIN_QUOTE_LEN), re.S)
NOTE_ANY_QUOTE = re.compile(
    r'"(%s{%d,}?)"(\s*\[(?:PMID:\d+|file:[^\]]+)\])?' % (_BODY, MIN_QUOTE_LEN), re.S
)

# UniProt flat-file line codes. Columns 1-2 are the code and 3-5 are padding; on CC
# continuation lines the code is repeated. Stripping the code is parsing the SOURCE's own
# record format -- it is not repairing the QUOTE, and a fabricated quote still fails (the
# self-test proves this). Without it, no quotation may cross a UniProt line break at all.
UNIPROT_PREFIX = re.compile(
    r"^(?:ID|AC|DT|DE|GN|OS|OG|OC|OX|OH|RN|RP|RC|RX|RG|RA|RT|RL|CC|DR|PE|KW|FT|SQ)\s{2,}", re.M
)


def norm(text: str) -> str:
    """The repo validator's normalisation, and nothing more."""
    return re.sub(r"\s+", " ", text)


def read_source(path: pathlib.Path) -> str:
    """Source text, with UniProt's line codes removed for `*-uniprot.txt` only."""
    text = path.read_text()
    if path.name.endswith("-uniprot.txt"):
        text = UNIPROT_PREFIX.sub("", text)
    return text


def resolve(reference_id: str) -> pathlib.Path | None:
    if reference_id.startswith("PMID:"):
        return REPO / "publications" / f"PMID_{reference_id.split(':', 1)[1]}.md"
    if reference_id.startswith("file:"):
        return REPO / "genes" / reference_id.split(":", 1)[1]
    return None


def iter_review_quotes(doc: dict):
    """Every supporting_text in the document, wherever it is nested."""

    def walk(node, path):
        if isinstance(node, dict):
            ref = node.get("reference_id")
            txt = node.get("supporting_text")
            if ref and txt:
                yield ref, txt, path
            for k, v in node.items():
                yield from walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                yield from walk(v, f"{path}[{i}]")

    yield from walk(doc, "$")


def notes_items(notes: str) -> tuple[list[tuple[str, str, str]], list[str]]:
    """Attributed quotations, plus complaints about unattributed ones."""
    items = [(ref, quote, "notes.md") for quote, ref in NOTE_ATTRIBUTED.findall(notes)]
    unattributed = [
        q for q, bracket in NOTE_ANY_QUOTE.findall(notes) if not bracket
    ]
    return items, [f"notes.md: UNATTRIBUTED quotation {q[:120]!r}" for q in unattributed]


def check(strict_files: bool = True) -> tuple[int, int, list[str]]:
    problems: list[str] = []
    checked = 0
    skipped = 0

    doc = yaml.safe_load(REVIEW.read_text()) if REVIEW.exists() else {}
    items = list(iter_review_quotes(doc))

    if NOTES.exists():
        note_items, note_problems = notes_items(NOTES.read_text())
        items.extend(note_items)
        problems.extend(note_problems)

    for ref, quote, path in items:
        src = resolve(ref)
        if src is None:
            skipped += 1
            continue
        if not src.exists():
            problems.append(f"{path}: source not found for {ref} -> {src}")
            continue
        if norm(quote) not in norm(read_source(src)):
            problems.append(f"{path}: NOT VERBATIM in {ref}\n      quote: {quote[:180]!r}")
            continue
        checked += 1

    if not strict_files:
        problems = [p for p in problems if "file:" not in p]
    return checked, skipped, problems


def self_test() -> int:
    """Prove the checker reports failure. A checker never observed failing is decoration."""
    failures = []

    def expect(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    checked, skipped, problems = check()
    expect("real corpus is clean", not problems, f"checked={checked} skipped={skipped} " + ("; ".join(problems) if problems else ""))
    expect("something was actually checked (a checker that checks 0 quotes always passes)", checked > 0, f"checked={checked}")

    # A quote that is real but altered must be rejected.
    pub = REPO / "publications" / "PMID_21029865.md"
    real = "We conclude that E5 activates RhoA but not Rac1 or Cdc42"
    expect("a verbatim quote is accepted", norm(real) in norm(pub.read_text()))
    expect(
        "a one-word-altered quote is rejected",
        norm(real.replace("not", "also")) not in norm(pub.read_text()),
    )
    # Whitespace differences must still pass (the validator normalises them)...
    expect(
        "line-wrapped whitespace is tolerated, as the repo validator tolerates it",
        norm(real.replace(" ", "\n  ")) in norm(pub.read_text()),
    )
    # ...but a literal backslash-n must NOT be silently repaired into a newline.
    expect(
        "a literal \\n escape is NOT repaired and therefore fails",
        norm(real.replace(" ", "\\n")) not in norm(pub.read_text()),
    )
    # A quote from the wrong paper must be rejected.
    expect(
        "a quote from a different paper is rejected",
        norm(real) not in norm((REPO / "publications" / "PMID_12775584.md").read_text()),
    )

    # The notes-attribution rule must fire on an unattributed quotation and stay silent on
    # an attributed one. Run the real extractor, not a paraphrase of it.
    good = 'Text around "%s" [PMID:21029865] and more.' % real
    bad = 'Text around "%s" and more.' % real
    g_items, g_problems = notes_items(good)
    b_items, b_problems = notes_items(bad)
    expect("attributed quotation is extracted and not complained about",
           len(g_items) == 1 and not g_problems, f"{len(g_items)} items, {len(g_problems)} problems")
    expect("unattributed quotation is reported",
           len(b_items) == 0 and len(b_problems) == 1, f"{len(b_items)} items, {len(b_problems)} problems")

    # UniProt line-code stripping must let a real multi-line CC quote through WITHOUT
    # letting a fabricated one through. Both halves are required; the first alone is a hole.
    up = GENE_DIR / "ARHGEF15-uniprot.txt"
    real_cc = "Does not activate RAC1 or CDC42"
    expect(
        "a genuine quote spanning a UniProt CC continuation line is accepted",
        norm(real_cc) in norm(read_source(up)),
    )
    expect(
        "...and the same quote fails without the line-code stripping, i.e. the stripping is load-bearing",
        norm(real_cc) not in norm(up.read_text()),
    )
    expect(
        "a fabricated quote is still rejected after stripping",
        norm("Does not activate RHOA or CDC42") not in norm(read_source(up)),
    )
    expect(
        "an inverted quote is still rejected after stripping",
        norm("Does activate RAC1 or CDC42") not in norm(read_source(up)),
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
    checked, skipped, problems = check()
    for p in problems:
        print(f"  {p}")
    print(f"checked={checked} unresolvable_namespace={skipped} problems={len(problems)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
