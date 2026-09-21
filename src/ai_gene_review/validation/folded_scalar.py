"""Detect hyphenated compounds split across a line break inside a YAML folded scalar.

A ``>-`` folded scalar turns a single newline into a **space**. So::

    reason: >-
      the loss-of-
      function phenotype

renders as ``the loss-of- function phenotype`` -- a word the author never wrote. Both
forms are valid YAML and parse without error, so schema validation cannot see it; the
damage only appears once the text is rendered, and by then it is on the published page.

This was found after a 95-column reflow of the AKAP12 review split ``A-kinase-anchoring``
across lines and shipped ``A-kinase- anchoring`` to the site. The reflow had been
justified as whitespace-only, which is exactly why nobody re-read the prose.

A line ending in ``--`` is an em-dash and folds correctly, so it is excluded.

**Scope.** Only ``>``-style folded scalars are scanned. Plain and double-quoted multi-line
scalars fold newlines to spaces identically, so the same defect is invisible here -- but
detecting it means tracking implicit-scalar continuation, which is a different parse
problem and is left out deliberately rather than overlooked.

Continuations that begin with ``(`` or ``[`` are also left out, because the class is
genuinely mixed: ``3-`` / ``(methylsulfanyl)propylamine`` is a split, while ``alpha-`` /
``(Tay-Sachs) or beta- (Sandhoff)`` is deliberate suspended-hyphen style where the space is
wanted. Reporting both would make the check untrustworthy for the sake of a few true hits.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity

#: Matches the opening line of a folded scalar, e.g. ``  reason: >-``.
BLOCK_HEAD = re.compile(r"^(\s*(?:-\s+)?)[\w-]+:\s*>[-+]?\s*$")

#: Words that make a trailing hyphen a **suspended** hyphen rather than a broken compound.
#: "betaB2- and betaA3-crystallins" is correct English and must not be flagged; the space
#: after the hyphen is intended there. Without this, the check fires on real prose and a
#: check that cries wolf gets switched off.
SUSPENDED_HYPHEN_FOLLOWERS = frozenset({"and", "or", "nor", "but", "to", "through", "versus", "vs"})


#: Closing punctuation that can end a compound's first half, alongside alphanumerics:
#: ``(Rab GTPase)-dependent``, ``24(S)-hydroxylation``, ``5-fluoro-2\'-deoxyuridine``.
CLOSING_PUNCTUATION = ")]}'\u2019"


def can_precede_hyphen(ch: str) -> bool:
    """True when *ch* can legitimately end the first half of a split compound.

    A hyphen is excluded, which is what keeps em-dashes out -- any tail ending ``--`` has
    a hyphen in this position.

    >>> [can_precede_hyphen(c) for c in "a4)'-"]
    [True, True, True, True, False]
    """
    return ch.isalnum() or ch in CLOSING_PUNCTUATION


@dataclass(frozen=True)
class FoldedHyphenSplit:
    """One hyphenated compound broken across a folded-scalar line break."""

    line: int
    tail: str
    next_word: str

    @property
    def rendered(self) -> str:
        """What the folded scalar actually produces (with the spurious space).

        >>> FoldedHyphenSplit(12, "loss-of-", "function").rendered
        'loss-of- function'
        """
        return f"{self.tail} {self.next_word}"

    @property
    def intended(self) -> str:
        """What the author almost certainly meant.

        >>> FoldedHyphenSplit(12, "loss-of-", "function").intended
        'loss-of-function'
        """
        return f"{self.tail}{self.next_word}"


def find_folded_hyphen_splits(text: str) -> Iterator[FoldedHyphenSplit]:
    """Yield every mid-compound fold in *text*.

    A real split needs a word character or closing punctuation immediately before the
    trailing hyphen, and an alphanumeric continuation after it -- that combination is a
    broken compound rather than a list dash or a deliberate trailing hyphen. The
    continuation is deliberately *not* required to be lowercase: ``ER-to-`` / ``Golgi``
    and ``interleukin-`` / ``6`` are both real splits.

        >>> list(find_folded_hyphen_splits("a: >-\\n  the loss-of-\\n  function bit\\n"))
        [FoldedHyphenSplit(line=2, tail='loss-of-', next_word='function')]

    An em-dash folds correctly and is not reported:

        >>> list(find_folded_hyphen_splits("a: >-\\n  an aside --\\n  continues\\n"))
        []

    Nor is ordinary text:

        >>> list(find_folded_hyphen_splits("a: >-\\n  nothing wrong\\n  at all\\n"))
        []

    A **suspended** hyphen is correct English and must not be flagged -- the space after
    the hyphen is intended:

        >>> list(find_folded_hyphen_splits("a: >-\\n  betaB2-\\n  and betaA3-crystallins\\n"))
        []
    """
    lines = text.splitlines()
    in_block = False
    indent = 0
    for i, line in enumerate(lines):
        head = BLOCK_HEAD.match(line)
        if head:
            in_block, indent = True, len(head.group(1))
            continue
        if not in_block or not line.strip():
            continue
        if len(line) - len(line.lstrip()) <= indent:
            in_block = False
            continue
        stripped = line.rstrip()
        if not stripped.endswith("-"):
            continue
        tail = stripped.split()[-1]
        # The continuation must still be inside this block. Without the indent test the
        # lookahead reads the next dedented key and reports nonsense like "oyl- action:".
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if not nxt.strip() or len(nxt) - len(nxt.lstrip()) <= indent:
            continue
        following = nxt.strip()
        first = following.split()[0] if following.split() else ""
        if first.rstrip(",;:").lower() in SUSPENDED_HYPHEN_FOLLOWERS:
            continue
        # What must NOT precede the hyphen is another hyphen: any tail ending "--" is an
        # em-dash, which folds correctly. An explicit endswith("--") guard was removed as
        # dead code once a mutation test showed deleting it changed nothing.
        #
        # Alphanumeric alone was too narrow and silently dropped a live class: compounds
        # ending in a bracket or apostrophe -- "(Rab GTPase)-dependent", "24(S)-hydroxylation",
        # "5-fluoro-2'-deoxyuridine" -- 16 sites in this corpus, rendering with the
        # spurious space today.
        if len(tail) > 1 and can_precede_hyphen(tail[-2]) and first[:1].isalnum():
            yield FoldedHyphenSplit(line=i + 1, tail=tail, next_word=first)


def check_folded_scalar_hyphens(yaml_file: Path, report: ValidationReport) -> None:
    """Add a warning for each mid-compound fold in *yaml_file*.

    Reported as a warning rather than an error: the repository carries a large
    pre-existing backlog of these, and blocking on them would fail every run of
    ``validate-all`` before any of them could be fixed.
    """
    try:
        text = yaml_file.read_text(errors="replace")
    except OSError:
        return
    for split in find_folded_hyphen_splits(text):
        report.add_issue(
            ValidationSeverity.WARNING,
            (
                f"Folded scalar splits a hyphenated compound: renders as "
                f"{split.rendered!r}, almost certainly meant {split.intended!r}"
            ),
            path=f"line {split.line}",
            suggestion=(
                "Rewrap without breaking on hyphens (textwrap.fill(..., "
                "break_on_hyphens=False)); a folded newline renders as a space"
            ),
            validation_category="BestPractices",
            check_type="folded_scalar_hyphen",
        )
