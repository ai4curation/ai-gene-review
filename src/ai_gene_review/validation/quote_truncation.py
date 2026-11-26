"""Find ``supporting_text`` quotes that were cut in the middle of a word.

Quotes are copied out of line-wrapped sources -- cached abstracts, UniProt flat
files, deep-research reports -- and a quote taken across a wrap is easy to stop
at the hyphen the wrap left behind. The result still passes ``validate-quotes``,
because :mod:`ai_gene_review.validation.supporting_text` collapses whitespace
before matching, so the quote genuinely *is* a verbatim substring of its source.
What it is not is a complete one, and the term it loses is usually the term the
quote was adduced for::

    supporting_text: "Catalyzes the NADPH-dependent formation of L-aspartate-"

The product of aspartate-semialdehyde dehydrogenase is L-aspartate-4-semialdehyde.
Cut at the hyphen, the quote reads as though the enzyme made aspartate itself,
which is the one thing it does not do.

This module only *detects and completes* such cuts; it decides nothing about
whether the surrounding claim is right. Two kinds are reported, and they are not
equally strong:

:attr:`CutKind.MID_WORD`
    The source continues with a word character, so a word was broken in half.
    There is no reading on which the quote is complete.

:attr:`CutKind.TOKEN_BOUNDARY`
    The source continues after a space, so the quote ends on a real token --
    ``from both (R)-`` where the source reads ``both (R)- and (S)-isomers``. The
    quote is verbatim and ends where a token ends; whether it is *enough* is a
    judgement about the argument it supports, not a mechanical defect.

A clean result is weak evidence. A quote can be truncated at a comma, a word, or
a sentence boundary and this check will never see it; it finds the one case that
leaves a syntactic trace.

    >>> cut = find_truncation(
    ...     "formation of L-aspartate-",
    ...     "Catalyzes the formation of L-aspartate-4-semialdehyde from L-aspartyl.",
    ... )
    >>> cut.kind is CutKind.MID_WORD
    True
    >>> cut.continuation
    '4-semialdehyde'
    >>> cut.completed
    'formation of L-aspartate-4-semialdehyde'

Quotes that do not end on a hyphen, and quotes their source does not contain,
are not this check's business:

    >>> find_truncation("formation of L-aspartate-4-semialdehyde", "irrelevant") is None
    True
    >>> find_truncation("absent from the source-", "an unrelated sentence") is None
    True
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Sequence

import yaml

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    local_prefix,
    resolve_local_source,
    source_renderings,
)
from ai_gene_review.validation.quote_check import (
    default_files,
    iter_quotes,
    literature_prefix,
)
from ai_gene_review.validation.supporting_text import _cached_text

__all__ = [
    "CutKind",
    "Truncation",
    "Finding",
    "find_truncation",
    "scan_document",
    "source_text",
    "source_renderings_for",
]

#: A word that may itself be hyphenated (``4-semialdehyde``, ``N-acetylglutaminyl``).
#: The trailing group is deliberately not optional-greedy past a final hyphen, so a
#: completion never ends on one.
_TOKEN = re.compile(r"[^\W_][\w]*(?:-[^\W_][\w]*)*")

#: Whitespace between any two tokens of the quote, however the source wraps.
_GAP = r"\s+"

#: Tokens that make a preceding hyphen a suspended hyphen ("CTP- and Mg2+-dependent"),
#: which is correct English rather than a word broken by a line wrap. Keyed on the whole
#: token, so "andro-" does not read as "and".
_SUSPENDING = frozenset({"and", "or", "nor"})

#: Characters folded before matching. Every entry is one character mapped to one
#: character, so an offset into the folded text indexes the original -- which is
#: what lets the continuation be extracted from the source as it is really written.
_FOLD = str.maketrans(
    {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2015": "-",
        "\u2212": "-",
        "\u00ad": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u02bc": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
)


def _fold(text: str) -> str:
    """Fold *text* for matching without changing its length.

    >>> len(_fold("don\u2019t \u2014 L\u2010aspartate")) == len("don\u2019t \u2014 L\u2010aspartate")
    True
    >>> _fold("L\u2010Aspartate\u2014X")
    'l-aspartate-x'
    """
    return text.translate(_FOLD).lower()


class CutKind(str, Enum):
    """How certainly a hyphen-terminal quote is incomplete."""

    MID_WORD = "mid_word"
    """The source continues with a word character: a word broken in half."""

    TOKEN_BOUNDARY = "token_boundary"
    """The source continues after a space: the quote ends on a whole token."""


@dataclass(frozen=True)
class Truncation:
    """A hyphen-terminal quote and the text that completes it.

    Attributes:
        quote: The quote as stored, with surrounding whitespace stripped.
        continuation: The next whole token in the source, which the cut removed.
        kind: Which of the two cases this is; see :class:`CutKind`.
    """

    quote: str
    continuation: str
    kind: CutKind

    @property
    def completed(self) -> str:
        """The quote with its cut word made whole again.

        A mid-word cut is repaired by joining directly; a token-boundary cut needs
        the space the source has::

            >>> Truncation("both (R)-", "and", CutKind.TOKEN_BOUNDARY).completed
            'both (R)- and'
            >>> Truncation("of L-aspartate-", "4-semialdehyde", CutKind.MID_WORD).completed
            'of L-aspartate-4-semialdehyde'

        This is a *proposal*, not a verified quote: it extends to one token, which
        is enough to make the word whole and rarely enough to make the sentence so.
        Re-check any edit with ``just validate-quotes``.
        """
        joiner = "" if self.kind is CutKind.MID_WORD else " "
        return f"{self.quote}{joiner}{self.continuation}"


def find_truncation(quote_text: str, source_text: str) -> Truncation | None:
    """Return the completion of *quote_text* in *source_text*, or ``None``.

    ``None`` means the check has nothing to say: the quote does not end on a
    hyphen, the source does not contain it, or the quote runs to the end of the
    source so there is nothing to complete it with.

    Args:
        quote_text: A ``supporting_text`` value.
        source_text: The raw source, line breaks intact. Breaks are significant --
            they are what distinguishes a wrapped word from two words -- so do not
            pass pre-collapsed text.

    Returns:
        The :class:`Truncation`, or ``None``.
    """
    quote = quote_text.strip()
    if not _fold(quote).endswith("-"):
        return None

    tokens = _fold(quote).split()
    if not tokens:
        return None
    match = re.search(_GAP.join(re.escape(t) for t in tokens), _fold(source_text))
    if match is None:
        return None

    # The fold is length-preserving, so this offset is valid in the original.
    rest = source_text[match.end() :]
    if not rest or not rest.strip():
        return None

    gap = rest[: len(rest) - len(rest.lstrip())]
    # A space (and only a space) makes the hyphen a real token boundary; a line
    # break is how a wrapped word looks, so it stays a mid-word cut.
    kind = (
        CutKind.TOKEN_BOUNDARY
        if gap and "\n" not in gap and "\r" not in gap
        else CutKind.MID_WORD
    )

    token = _TOKEN.match(rest.lstrip())
    if token is None:
        return None
    continuation = token.group(0)
    if _fold(continuation) in _SUSPENDING:
        # A suspended hyphen: real punctuation, so the quote ends on a whole token
        # however the source wraps there.
        kind = CutKind.TOKEN_BOUNDARY
    return Truncation(quote=quote, continuation=continuation, kind=kind)


# --------------------------------------------------------------------------- #
# Corpus scan
# --------------------------------------------------------------------------- #


def source_text(reference_id: str, project_root: Path = PROJECT_ROOT) -> str | None:
    """Raw text of the source *reference_id* names, line breaks intact.

    Handles the two source kinds a quote can be checked against: local files
    (``file:``, ``Reactome:``) and cached literature (``PMID:``, ``DOI:``).
    Returns ``None`` for an id with no readable source, which is the same set
    ``validate-quotes`` reports as unchecked.
    """
    for rendering in source_renderings_for(reference_id, project_root):
        return rendering
    return None


def source_renderings_for(
    reference_id: str, project_root: Path = PROJECT_ROOT
) -> tuple[str, ...]:
    """Every rendering of *reference_id*'s source that a quote may match.

    A UniProt flat file is also offered with its two-letter line codes removed,
    exactly as ``validate-quotes`` offers it. Without that rendering a quote
    wrapped inside a ``CC`` block appears to be completed by the token ``CC``,
    which is the file's left margin rather than anything the record says.
    """
    if local_prefix(reference_id) is not None:
        path = resolve_local_source(reference_id, project_root)
        if path is None or not path.exists():
            return ()
        return source_renderings(path, path.read_text(errors="replace"))
    if literature_prefix(reference_id) is not None:
        text = _cached_text(reference_id, project_root / "publications")
        return (text,) if text is not None else ()
    return ()


@dataclass(frozen=True)
class Finding:
    """One truncated quote, located in the corpus."""

    file: Path
    yaml_path: str
    reference_id: str
    truncation: Truncation


def scan_document(path: Path, project_root: Path = PROJECT_ROOT) -> list[Finding]:
    """Return every truncated quote in the YAML document at *path*."""
    data = yaml.safe_load(path.read_text())
    findings: list[Finding] = []
    for quote in iter_quotes(data):
        if not quote.reference_id or not _fold(quote.text.strip()).endswith("-"):
            continue
        cut = None
        # Most-processed rendering first: for a UniProt flat file the de-prefixed
        # one is the only rendering whose next token is the record's own text.
        for rendering in reversed(
            source_renderings_for(quote.reference_id, project_root)
        ):
            cut = find_truncation(quote.text, rendering)
            if cut is not None:
                break
        if cut is not None:
            findings.append(
                Finding(
                    file=path,
                    yaml_path=quote.path,
                    reference_id=quote.reference_id,
                    truncation=cut,
                )
            )
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    """Report truncated quotes across the corpus.

    Exits 0 whatever it finds: the mid-word cases are defects, but repairing them
    edits curated prose, so this reports rather than gates.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "files", nargs="*", type=Path, help="YAML files (default: the corpus)"
    )
    parser.add_argument(
        "--kind",
        choices=[k.value for k in CutKind],
        help="report only this kind of cut",
    )
    args = parser.parse_args(argv)

    paths = args.files or default_files()
    counts: dict[CutKind, int] = {k: 0 for k in CutKind}
    for path in paths:
        for finding in scan_document(path):
            if args.kind and finding.truncation.kind.value != args.kind:
                continue
            counts[finding.truncation.kind] += 1
            rel = path.relative_to(PROJECT_ROOT) if path.is_absolute() else path
            print(f"{rel}: {finding.yaml_path} [{finding.truncation.kind.value}]")
            print(f"    quote:     ...{finding.truncation.quote[-70:]}")
            print(f"    completed: ...{finding.truncation.completed[-70:]}")
    total = sum(counts.values())
    print(
        f"\n{total} truncated quote(s): "
        f"{counts[CutKind.MID_WORD]} mid-word, {counts[CutKind.TOKEN_BOUNDARY]} at a token boundary"
    )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
