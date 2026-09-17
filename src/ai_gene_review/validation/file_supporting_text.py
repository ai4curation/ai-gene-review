"""Verify ``supporting_text`` attributed to ``file:`` references.

``linkml-reference-validator`` checks ``supporting_text`` only for ``PMID:``
references.  Quotes attributed to ``file:`` references -- deep-research reports,
UniProt records, GOA tables, bioinformatics RESULTS.md -- were never checked, so
paraphrase presented as quotation accumulated there undetected.

The check is deliberately forgiving about *formatting* and strict about *content*:

* UniProt ``.txt`` records carry two-letter line-prefix codes (``DE``, ``CC``,
  ``FT`` ...).  Both the stripped and unstripped forms are searched, because
  curators quote them either way.
* Words hyphenated across a line break are rejoined, and punctuation is reduced
  to whitespace, so ``"light-induced"`` matches a source that wrapped it and a
  quote ending ``.`` matches a source line ending ``;``.
* Unicode punctuation is folded to ASCII, so a curly apostrophe in the quote
  still matches a straight one in the source.
* An ellipsis marks elision: ``"foo ... bar"`` matches if ``foo`` and ``bar``
  both occur, in that order.  This is how curators legitimately shorten a quote.

What survives all of that is a quote whose words are not in the cited file.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

# Narration openers: a "quote" starting this way is the reviewer describing the
# source rather than quoting it, and cannot be verbatim by construction.
_NARRATION = re.compile(
    r"^\s*(falcon|the falcon|deep research|deep-research|this file|the file|"
    r"synthesis|the synthesis|research|the report|report|analysis|the analysis|"
    r"[a-z]+ (?:domain|sequence|structural|phylogenetic) analysis)\b"
    r"[^.]{0,40}?\b(supports?|summari[sz]es?|synthesi[sz]es?|identifies|indicates?|"
    r"shows?|reveals?|describes?|confirms?|suggests?|notes?|reports?|states?|"
    r"establishes?|characteri[sz]es?|frames?|treats?)\b",
    re.I,
)

_PREFIX = re.compile(r"^[A-Z]{2}(?:   |\s{3})")
_WS = re.compile(r"\s+")
_ELLIPSIS = re.compile(r"\s*(?:\.\s*\.\s*\.|\u2026|\[\.\.\.\]|\[\u2026\])\s*")

_PUNCT = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-",
    "—": "-", "―": "-", "−": "-",
    " ": " ", " ": " ", " ": " ", "​": "",
    "ʼ": "'", "´": "'", "`": "'",
}


_HYPHEN_BREAK = re.compile(r"-\s*\n\s*")
_NONWORD = re.compile(r"[^0-9a-z]+")


def _fold(text: str) -> str:
    """Reduce text to lowercase words separated by single spaces.

    Punctuation is discarded rather than normalised.  Curators legitimately end a
    quote with ``.`` where the record has ``;``, or omit a trailing bracket; those
    are transcription conventions, not content differences, and flagging them
    would bury the real fabrications in noise.
    """
    text = unicodedata.normalize("NFKC", text or "")
    text = _HYPHEN_BREAK.sub("-", text)
    text = "".join(_PUNCT.get(ch, ch) for ch in text)
    # Hyphens vanish rather than splitting, so a word wrapped across a line
    # ("light-\ninduced") folds the same as the unwrapped quote ("light-induced").
    text = text.lower().replace("-", "")
    text = _NONWORD.sub(" ", text)
    return _WS.sub(" ", text).strip()


def _source_variants(path: Path) -> list[str]:
    """Folded source text.

    UniProt records are returned twice -- as written and with the two-letter line
    prefixes stripped -- because curators quote them either way.  The variants are
    searched *independently*; concatenating them would let an out-of-order quote
    match across the seam.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")
    variants = [_fold(raw)]
    if path.suffix == ".txt":
        variants.append(
            _fold("\n".join(_PREFIX.sub("", line) for line in raw.splitlines()))
        )
    return variants


def quote_is_present(quote: str, body: str | Iterable[str]) -> bool:
    """True if ``quote`` occurs in any variant of ``body``, ellipsis meaning elision."""
    # Split on ellipsis before folding: folding discards the dots.
    parts = [f for f in (_fold(p) for p in _ELLIPSIS.split(quote or "")) if f]
    if not parts:
        return True
    variants = [body] if isinstance(body, str) else list(body)
    for variant in variants:
        pos = 0
        for part in parts:
            found = variant.find(part, pos)
            if found < 0:
                break
            pos = found + len(part)
        else:
            return True
    return False


def looks_like_narration(quote: str) -> bool:
    """True for text that describes a source instead of quoting it."""
    return bool(_NARRATION.match(quote or ""))


@dataclass
class FileQuoteIssue:
    reference_id: str
    supporting_text: str
    kind: str  # "narration" | "not_verbatim" | "missing_file"
    path: str = ""


@dataclass
class FileQuoteResult:
    checked: int = 0
    issues: list[FileQuoteIssue] = field(default_factory=list)


def _iter_supporting(obj: Any, trail: str = "") -> Iterable[tuple[str, str, str]]:
    if isinstance(obj, dict):
        rid, txt = obj.get("reference_id"), obj.get("supporting_text")
        if isinstance(rid, str) and isinstance(txt, str):
            yield rid, txt, trail
        for key, val in obj.items():
            yield from _iter_supporting(val, f"{trail}.{key}" if trail else str(key))
    elif isinstance(obj, list):
        for i, val in enumerate(obj):
            yield from _iter_supporting(val, f"{trail}[{i}]")


def check_file_supporting_text(
    data: dict, project_root: Path, genes_root: Path | None = None
) -> FileQuoteResult:
    """Check every ``file:`` supporting_text in one review document."""
    result = FileQuoteResult()
    genes_root = genes_root or (project_root / "genes")
    cache: dict[Path, list[str] | None] = {}

    for rid, txt, trail in _iter_supporting(data):
        if not rid.startswith("file:"):
            continue
        result.checked += 1
        rel = rid[5:]
        target = next(
            (p for p in (project_root / rel, genes_root / rel) if p.exists()), None
        )
        if target is None:
            result.issues.append(
                FileQuoteIssue(rid, txt, "missing_file", trail)
            )
            continue
        if looks_like_narration(txt):
            result.issues.append(FileQuoteIssue(rid, txt, "narration", trail))
            continue
        if target not in cache:
            try:
                cache[target] = _source_variants(target)
            except Exception:
                cache[target] = None
        body = cache[target]
        if body is not None and not quote_is_present(txt, body):
            result.issues.append(FileQuoteIssue(rid, txt, "not_verbatim", trail))
    return result
