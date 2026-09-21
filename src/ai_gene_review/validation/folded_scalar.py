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
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

#: Matches the opening line of a folded scalar, e.g. ``  reason: >-``.
BLOCK_HEAD = re.compile(r"^(\s*)[\w-]+:\s*>-?\s*$")

#: Words that make a trailing hyphen a **suspended** hyphen rather than a broken compound.
#: "betaB2- and betaA3-crystallins" is correct English and must not be flagged; the space
#: after the hyphen is intended there. Without this, the check fires on real prose and a
#: check that cries wolf gets switched off.
SUSPENDED_HYPHEN_FOLLOWERS = frozenset({"and", "or", "nor", "but", "to", "through", "versus", "vs"})


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

    A real split needs an alphanumeric immediately before the trailing hyphen and a
    lowercase word after it -- that combination is a broken compound rather than a list
    dash or a deliberate trailing hyphen:

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
        following = lines[i + 1].strip() if i + 1 < len(lines) else ""
        first = following.split()[0] if following.split() else ""
        if first.rstrip(",;:").lower() in SUSPENDED_HYPHEN_FOLLOWERS:
            continue
        # The alphanumeric test is what excludes em-dashes: any tail ending in "--" has
        # "-" in that position, so "an aside -- continues" can never be reported. An
        # explicit endswith("--") guard was removed as dead code once a mutation test
        # showed deleting it changed no behaviour.
        if len(tail) > 1 and tail[-2].isalnum() and first[:1].islower():
            yield FoldedHyphenSplit(line=i + 1, tail=tail, next_word=first)


def check_folded_scalar_hyphens(yaml_file: Path, report) -> None:
    """Add a warning for each mid-compound fold in *yaml_file*.

    Reported as a warning rather than an error: the repository carries a large
    pre-existing backlog of these, and blocking on them would fail every run of
    ``validate-all`` before any of them could be fixed.
    """
    from ai_gene_review.validation.validation_report import ValidationSeverity

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
