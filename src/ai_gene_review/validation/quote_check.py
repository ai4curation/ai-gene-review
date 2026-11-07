"""Check every ``supporting_text`` quote in a YAML document, whatever its kind.

Each validator used to decide for itself which quotes to look at, so a gap in any
one of them stayed invisible to the others (issue #6021):

- ``module_validator`` checked only ``source_id`` quotes with a PMID or DOI, so
  ``file:`` / ``Reactome:`` quotes, and every ``reference_id`` / ``findings`` quote,
  passed unread;
- family reviews ran only the external reference validator, which lists ``file``
  and ``Reactome`` under ``skip_prefixes``;
- GO-CAM reviews were schema-validated and nothing else.

This module locates quotes structurally, so one walker serves every document
kind, and sorts each quote into one of three outcomes:

- **verified**: the quote is a verbatim (normalised) substring of its source;
- **failed**: the source does not resolve, is not cached, or does not contain the
  quote -- an error;
- **unchecked**: the source is a kind nothing in the repository can read (a URL,
  a bare database id). Reported, and counted, so that output never implies these
  were verified.

Literature quotes (``PMID:``, ``DOI:``) use the shared ``SupportingTextValidator``
against ``publications/``; ``file:`` and ``Reactome:`` quotes use
``local_source_text``. Both apply the same normaliser, so a quote passes here
exactly when it would pass in a gene review.

Failures that already existed when a document kind was brought under this check
are listed in ``conf/quote_check_baseline.yaml`` (keyed by file and
``quote_digest``, the same scheme gene reviews use in
``conf/local_quote_baseline.yaml``). A listed failure is reported as a warning;
any other failure is an error. The baseline only ever shrinks:

    just validate-quotes                     # check the default scope
    just validate-quotes --prune-baseline    # drop entries that now pass

Gene reviews are not in the default scope: ``validator.py`` already checks their
``file:``/``Reactome:`` quotes (``local_source_text``) and their literature quotes.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Set

import yaml

from ai_gene_review.validation.local_source_text import (
    PROJECT_ROOT,
    baseline_key,
    local_prefix,
    quote_digest,
    quote_matches,
    resolve_local_source,
)
from ai_gene_review.validation.supporting_text import (
    LITERATURE_PREFIXES,
    build_supporting_text_validator,
    is_unfetchable,
)

BASELINE_PATH = PROJECT_ROOT / "conf" / "quote_check_baseline.yaml"

#: Document kinds checked by ``just validate-quotes``: every committed YAML that
#: carries quotes and is not a gene review. Prediction reviews are covered by
#: ``prediction_evidence`` and are listed so the census is complete.
DEFAULT_GLOBS = (
    "modules/**/*.yaml",
    "interpro/*/*/*-review.yaml",
    "gocams/*/*-review.yaml",
    "rules/**/*.yaml",
    "models/**/*.yaml",
    "projects/**/*.yaml",
    "genes/*/*/*-predictions-review.yaml",
)

#: Directories excluded from the default scope: frozen experiment snapshots whose
#: ``file:`` ids were written relative to a copied tree, not to this repository.
EXCLUDED_PARTS = ("recapitulation-experiment",)

#: Keys that name the source of the ``supporting_text`` beside them, in priority order.
REFERENCE_KEYS = ("reference_id", "source_id", "reference")


class Outcome(str, Enum):
    """What happened when a quote was checked."""

    VERIFIED = "verified"
    NOT_FOUND = "not_found"
    UNRESOLVED = "unresolved"
    UNCHECKED = "unchecked"


#: Outcomes that are errors unless baselined.
FAILURES = frozenset({Outcome.NOT_FOUND, Outcome.UNRESOLVED})


@dataclass(frozen=True)
class Quote:
    """One ``supporting_text`` and the source it cites."""

    path: str
    reference_id: Optional[str]
    text: str


@dataclass(frozen=True)
class QuoteResult:
    """A quote and the outcome of checking it."""

    quote: Quote
    outcome: Outcome
    detail: str = ""
    baselined: bool = False

    @property
    def blocking(self) -> bool:
        """True when this result should fail validation."""
        return self.outcome in FAILURES and not self.baselined


def iter_quotes(data: Any) -> Iterator[Quote]:
    """Yield every non-empty ``supporting_text`` in *data* with the id it cites.

    The cited id is the first of ``reference_id`` / ``source_id`` / ``reference``
    on the same mapping. A mapping with none of them inherits the ``id`` of the
    nearest enclosing ``references[]`` entry (``references[].findings[]``); a
    quote with no id at all is yielded with ``reference_id=None``.

    >>> doc = {
    ...   "references": [{"id": "file:x.md", "findings": [{"supporting_text": "a"}]}],
    ...   "evidence": [{"source_id": "PMID:1", "supporting_text": "b"}],
    ...   "gaps": [{"provenance": [{"reference_id": "Reactome:R-1", "supporting_text": "c"}]}],
    ...   "orphan": {"supporting_text": "d"},
    ... }
    >>> [(q.path, q.reference_id, q.text) for q in iter_quotes(doc)]
    ... # doctest: +NORMALIZE_WHITESPACE
    [('references[0].findings[0].supporting_text', 'file:x.md', 'a'),
     ('evidence[0].supporting_text', 'PMID:1', 'b'),
     ('gaps[0].provenance[0].supporting_text', 'Reactome:R-1', 'c'),
     ('orphan.supporting_text', None, 'd')]
    """

    def walk(node: Any, path: str, inherited: Optional[str]) -> Iterator[Quote]:
        if isinstance(node, dict):
            own = next(
                (node[k] for k in REFERENCE_KEYS if isinstance(node.get(k), str)), None
            )
            text = node.get("supporting_text")
            if isinstance(text, str) and text.strip():
                ref = own if own is not None else inherited
                yield Quote(
                    f"{path}.supporting_text" if path else "supporting_text",
                    ref.strip() if ref else None,
                    text,
                )
            for key, value in node.items():
                if key == "references" and isinstance(value, list):
                    for i, ref in enumerate(value):
                        rid = ref.get("id") if isinstance(ref, dict) else None
                        yield from walk(
                            ref,
                            f"{path}.references[{i}]" if path else f"references[{i}]",
                            rid if isinstance(rid, str) else None,
                        )
                    continue
                yield from walk(value, f"{path}.{key}" if path else str(key), inherited)
        elif isinstance(node, list):
            for i, value in enumerate(node):
                yield from walk(value, f"{path}[{i}]", inherited)

    yield from walk(data, "", None)


def literature_prefix(reference_id: str) -> Optional[str]:
    """Return the upper-cased prefix when *reference_id* is a literature id.

    >>> literature_prefix("pmid:123"), literature_prefix("file:x"), literature_prefix("url")
    ('PMID', None, None)
    """
    prefix = reference_id.split(":", 1)[0].strip().upper()
    return prefix if ":" in reference_id and prefix in LITERATURE_PREFIXES else None


def check_quote(
    quote: Quote, project_root: Path = PROJECT_ROOT, validator: Any = None
) -> QuoteResult:
    """Check one quote against its source and return the outcome.

    *validator* is the ``SupportingTextValidator`` for literature quotes; when
    omitted the shared one is built from ``project_root / "publications"``.
    """
    ref = quote.reference_id
    if not ref:
        return QuoteResult(quote, Outcome.UNCHECKED, "no reference id")
    if local_prefix(ref) is not None:
        source = resolve_local_source(ref, project_root)
        if source is None:
            return QuoteResult(quote, Outcome.UNRESOLVED, f"{ref} does not resolve to a file")
        if quote_matches(quote.text, source):
            return QuoteResult(quote, Outcome.VERIFIED)
        return QuoteResult(quote, Outcome.NOT_FOUND, f"not a verbatim substring of {ref}")
    if literature_prefix(ref) is not None:
        if validator is None:
            validator, _ = build_supporting_text_validator(project_root / "publications")
        if validator is None:
            raise RuntimeError("linkml_reference_validator is not installed")
        try:
            result = validator.validate(quote.text, ref)
        except Exception as exc:  # noqa: BLE001 - external publication service
            return QuoteResult(
                quote, Outcome.UNRESOLVED, f"could not check {ref}: {type(exc).__name__}: {exc}"
            )
        if result.is_valid:
            return QuoteResult(quote, Outcome.VERIFIED)
        message = str(getattr(result, "message", "") or "")
        if is_unfetchable(message):
            return QuoteResult(quote, Outcome.UNRESOLVED, f"{ref} is not cached: {message}")
        return QuoteResult(quote, Outcome.NOT_FOUND, f"{ref}: {message}")
    return QuoteResult(
        quote, Outcome.UNCHECKED, f"no checkable source for prefix {ref.split(':', 1)[0]!r}"
    )


#: A baseline: ``{repo-relative file: {outcome: {quote digest, ...}}}``. Entries are
#: split by outcome so a quote that misquotes a readable source (``not_found``,
#: fixable now) stays distinguishable from one whose source is absent
#: (``unresolved``), and a quote cannot move from one class to the other unseen.
Baseline = Dict[str, Dict[str, Set[str]]]

#: The outcome keys a baseline may use.
BASELINE_OUTCOMES = (Outcome.NOT_FOUND.value, Outcome.UNRESOLVED.value)


def load_baseline(path: Optional[Path] = None) -> Baseline:
    """Read the baseline file (a fresh copy, safe to mutate).

    *path* defaults to the module's ``BASELINE_PATH``, looked up at call time so
    that redirecting it (as the tests do) also redirects reads.

    >>> load_baseline(Path("/nonexistent.yaml"))
    {}
    """
    path = BASELINE_PATH if path is None else path
    if not path.exists():
        return {}
    return {k: {o: set(d) for o, d in v.items()} for k, v in _load_baseline(path).items()}


@lru_cache(maxsize=4)
def _load_baseline(path: Path) -> Baseline:
    """Parse the baseline once per process (module validation checks one file at a time)."""
    loaded = yaml.safe_load(path.read_text()) or {}
    baseline: Baseline = {}
    for key, by_outcome in (loaded.get("entries") or {}).items():
        unknown = set(by_outcome or {}) - set(BASELINE_OUTCOMES)
        if unknown:
            raise ValueError(f"{path}: {key}: unknown baseline outcome(s) {sorted(unknown)}")
        baseline[str(key)] = {o: set(d or []) for o, d in (by_outcome or {}).items()}
    return baseline


def check_document(
    data: Any,
    yaml_file: Optional[Path] = None,
    project_root: Path = PROJECT_ROOT,
    validator: Any = None,
    baseline: Optional[Baseline] = None,
) -> List[QuoteResult]:
    """Check every quote in *data*; mark failures listed in the baseline.

    A failure is baselined only under its own outcome: a quote listed as
    ``unresolved`` whose source now exists but does not contain it blocks.
    """
    if baseline is None:
        baseline = _load_baseline(BASELINE_PATH) if BASELINE_PATH.exists() else {}
    key = baseline_key(yaml_file, project_root) if yaml_file is not None else None
    known = baseline.get(key, {}) if key else {}
    results = []
    for quote in iter_quotes(data):
        result = check_quote(quote, project_root, validator)
        if result.outcome in FAILURES and quote.reference_id:
            if quote_digest(quote.reference_id, quote.text) in known.get(result.outcome.value, set()):
                result = QuoteResult(quote, result.outcome, result.detail, baselined=True)
        results.append(result)
    return results


def format_result(path: Path, result: QuoteResult) -> str:
    """One output line for a non-verified result."""
    q = result.quote
    if result.blocking:
        tag = "❌ ERROR"
    elif result.baselined:
        tag = "⚠️  WARN (baselined)"
    else:
        tag = "ℹ️  UNCHECKED"
    return f"{tag} {path}: {q.path} [{q.reference_id}] {result.detail}"


def default_files(project_root: Path = PROJECT_ROOT) -> List[Path]:
    """The files ``just validate-quotes`` checks when none are given."""
    files = {
        path
        for pattern in DEFAULT_GLOBS
        for path in project_root.glob(pattern)
        if not any(part in EXCLUDED_PARTS for part in path.parts)
    }
    return sorted(files)


def write_baseline(entries: Baseline, path: Optional[Path] = None) -> None:
    """Write *entries* to the baseline file (default: ``BASELINE_PATH`` at call time)."""
    path = BASELINE_PATH if path is None else path
    header = (
        "# Known failing supporting_text quotes outside gene reviews.\n"
        "#\n"
        "# Generated by ai_gene_review.validation.quote_check; do not add entries by hand.\n"
        "# Each entry is quote_digest(reference_id, supporting_text) for a quote that\n"
        "# failed when its document kind was brought under the check (issue #6021),\n"
        "# listed under its outcome: not_found (the source exists but does not contain\n"
        "# the quote; fixable now) or unresolved (the source is missing).\n"
        "# Listed quotes are reported as WARNINGs; any other failure is an ERROR.\n"
        "# Fix a quote, then shrink this file with:\n"
        "#   just validate-quotes --prune-baseline\n"
    )
    body = yaml.safe_dump(
        {
            "entries": {
                k: {o: sorted(entries[k][o]) for o in BASELINE_OUTCOMES if entries[k].get(o)}
                for k in sorted(entries)
                if any(entries[k].values())
            }
        },
        sort_keys=False,
        width=100,
    )
    path.write_text(header + body)


def count_entries(baseline: Baseline) -> int:
    """Number of digests in *baseline*.

    >>> count_entries({"a.yaml": {"not_found": {"x", "y"}, "unresolved": {"z"}}})
    3
    """
    return sum(len(d) for v in baseline.values() for d in v.values())


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Check quotes in the given YAML files (default scope if none); exit 1 on failure."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument(
        "--show-unchecked",
        action="store_true",
        help="List each quote whose source cannot be checked (default: count only)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--prune-baseline",
        action="store_true",
        help="Drop baseline entries that now pass (never adds one)",
    )
    mode.add_argument(
        "--init-baseline",
        action="store_true",
        help="Create the baseline from every current failure, over the full default "
        "scope. Refuses when the baseline already exists: once created it only shrinks",
    )
    args = parser.parse_args(argv)
    if args.init_baseline and args.files:
        parser.error("--init-baseline needs the full default scope; pass no files")
    if args.init_baseline and BASELINE_PATH.exists():
        parser.error(
            f"{BASELINE_PATH} already exists and only shrinks; fix failures instead, "
            "or delete the file deliberately in a reviewed change"
        )
    if args.prune_baseline and args.files:
        parser.error("--prune-baseline needs the full default scope; pass no files")
    files = args.files or default_files()

    baseline = load_baseline()
    current: Baseline = {}
    totals: Counter = Counter()
    blocking = 0
    unparseable: List[Path] = []
    for path in files:
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:  # report the file, then keep checking the rest
            print(f"❌ ERROR {path}: not valid YAML, so its quotes cannot be checked: {exc}")
            unparseable.append(path)
            continue
        key = baseline_key(path)
        for result in check_document(data, path, baseline=baseline):
            totals[result.outcome.value] += 1
            if result.outcome in FAILURES and key and result.quote.reference_id:
                current.setdefault(key, {}).setdefault(result.outcome.value, set()).add(
                    quote_digest(result.quote.reference_id, result.quote.text)
                )
            if result.outcome is Outcome.VERIFIED:
                continue
            if result.blocking:
                blocking += 1
            if result.outcome is Outcome.UNCHECKED and not args.show_unchecked:
                continue
            print(format_result(Path(key) if key else path, result))
    print(
        f"Quotes: {totals['verified']} verified; "
        f"{totals['not_found']} not found in their source and "
        f"{totals['unresolved']} with a missing source "
        f"({blocking} blocking, {totals['not_found'] + totals['unresolved'] - blocking} baselined); "
        f"{len(unparseable)} unparseable file{'' if len(unparseable) == 1 else 's'}; "
        f"{totals['unchecked']} unchecked (no readable source); {len(files)} files"
    )
    if args.init_baseline:
        if unparseable:
            # An unreadable file contributes no failures, so the baseline would be incomplete.
            print("Not writing a baseline: fix the unparseable files first")
            return 1
        write_baseline(current)
        print(f"Wrote {count_entries(current)} entries to {BASELINE_PATH}")
        return 0
    if args.prune_baseline:
        if unparseable:
            # An unreadable file contributes no current failures, so pruning would
            # silently drop its baseline entries. Fix the YAML first.
            print("Not pruning: fix the unparseable files first, or their entries would be dropped")
            return 1
        pruned = {
            k: {o: d & current.get(k, {}).get(o, set()) for o, d in v.items()}
            for k, v in baseline.items()
        }
        write_baseline(pruned)
        print(f"Dropped {count_entries(baseline) - count_entries(pruned)} baseline entries that now pass")
    return 1 if blocking or unparseable else 0


if __name__ == "__main__":
    sys.exit(main())
