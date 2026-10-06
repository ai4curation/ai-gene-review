"""Verbatim checks for supporting_text that quotes a local source.

``conf/reference_validator_config.yaml`` lists ``file`` and ``Reactome`` under
``skip_prefixes``, so the external reference validator passes every such quote
without looking at it. It cannot simply be un-skipped: the validator has no
Reactome source, and for ``file:`` it writes the file's content into the
``publications/`` cache and reads that copy back on later runs, so an edited
source would be compared against a stale snapshot.

This module checks those quotes against the source as it is on disk now, using
the validator's own matcher (same normalisation, ``...`` elision and
``literal_bracket_patterns``), so a quote passes here exactly when it would pass
against a cached publication. A source is tried in several renderings:

- the raw text;
- for a UniProt flat file, the text with the two-letter line codes removed, so
  a quote of a ``CC`` paragraph may run across the file's line wraps;
- that unwrapped text without ``{ECO:...}`` evidence tags.

Each rendering is also tried with brackets kept literally, because the matcher
strips a bracket such as Rhea's ``[protein]`` as an editorial note.

Quotes that already failed when this check was introduced are listed in
``conf/local_quote_baseline.yaml`` and reported as warnings; any other failure
is an error. Fix a listed quote, then drop it with
``just local-quote-baseline --prune``.
"""

from __future__ import annotations

import hashlib
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple

import yaml

from ai_gene_review.validation.supporting_text import build_supporting_text_validator
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
BASELINE_PATH = PROJECT_ROOT / "conf" / "local_quote_baseline.yaml"
CHECK_TYPE = "local_source_supporting_text"

_UNIPROT_LINE_CODE = re.compile(r"^[A-Z]{2}   ", re.M)
_ECO_TAG = re.compile(r"\s*\{ECO:[^}]*\}")


def local_prefix(reference_id: str) -> Optional[str]:
    """Return ``file`` or ``Reactome`` for a local-source id, else None.

    >>> local_prefix("file:human/TP53/TP53-uniprot.txt")
    'file'
    >>> local_prefix("Reactome:R-HSA-73912")
    'Reactome'
    >>> local_prefix("PMID:123") is None
    True
    """
    prefix = reference_id.split(":", 1)[0].strip().lower()
    if prefix == "file":
        return "file"
    if prefix == "reactome":
        return "Reactome"
    return None


def resolve_local_source(
    reference_id: str, project_root: Path = PROJECT_ROOT
) -> Optional[Path]:
    """Resolve a ``file:`` or ``Reactome:`` id to the file a quote is checked against.

    ``file:`` paths resolve against ``genes/`` first and then the project root,
    as ``validate_file_reference`` does; ``Reactome:`` ids resolve to the cached
    entry under ``reactome/``.

    >>> resolve_local_source("file:human/TP53/TP53-uniprot.txt").name
    'TP53-uniprot.txt'
    >>> resolve_local_source("Reactome:R-HSA-0") is None
    True
    """
    prefix = local_prefix(reference_id)
    identifier = reference_id.split(":", 1)[1].strip() if ":" in reference_id else ""
    if not identifier:
        return None
    if prefix == "file":
        candidates = [project_root / "genes" / identifier, project_root / identifier]
    elif prefix == "Reactome":
        candidates = [project_root / "reactome" / f"{identifier}.md"]
    else:
        return None
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def source_renderings(path: Path, raw: str) -> Tuple[str, ...]:
    """Return the renderings of a source that a quote may match.

    >>> flat = "CC   -!- FUNCTION: Binds\\nCC       DNA {ECO:0000269}. Acts\\n"
    >>> for r in source_renderings(Path("X-uniprot.txt"), flat):
    ...     print(" ".join(r.split()))
    CC -!- FUNCTION: Binds CC DNA {ECO:0000269}. Acts
    -!- FUNCTION: Binds DNA {ECO:0000269}. Acts
    -!- FUNCTION: Binds DNA. Acts
    >>> source_renderings(Path("notes.md"), "text")
    ('text',)
    """
    renderings = [raw]
    if path.name.endswith("-uniprot.txt") or raw.startswith("ID   "):
        unwrapped = _UNIPROT_LINE_CODE.sub("", raw)
        renderings.append(unwrapped)
        renderings.append(_ECO_TAG.sub("", unwrapped))
    return tuple(renderings)


@lru_cache(maxsize=256)
def _normalized_renderings(path: Path, mtime_ns: int, size: int) -> Tuple[str, ...]:
    """Normalised renderings of *path*, keyed on its mtime and size so edits are seen."""
    validator = _validator()
    raw = path.read_text(encoding="utf-8")
    return tuple(validator.normalize_text(r) for r in source_renderings(path, raw))


def _validator():
    validator, _ = build_supporting_text_validator()
    if validator is None:
        raise RuntimeError("linkml_reference_validator is not installed")
    return validator


def quote_matches(quote: str, path: Path) -> bool:
    """True when *quote* is found in any rendering of the source at *path*.

    A quote matches a rendering when every ``...``-separated part, normalised by
    the reference validator, is a substring of it (the validator's own rule), or
    when the whole quote is, with brackets kept literally.
    """
    validator = _validator()
    stat = path.stat()
    renderings = _normalized_renderings(path, stat.st_mtime_ns, stat.st_size)
    parts = [validator.normalize_text(p) for p in validator._split_query(quote)]
    parts = [p for p in parts if p]
    literal = validator.normalize_text(quote)
    for content in renderings:
        if parts and all(p in content for p in parts):
            return True
        if literal and literal in content:
            return True
    return False


def quote_digest(reference_id: str, quote: str) -> str:
    """Stable key for a (reference, quote) pair, insensitive to YAML reflowing.

    >>> quote_digest("file:a.md", "x  y\\nz") == quote_digest("file:a.md", "x y z")
    True
    """
    text = " ".join(quote.split())
    return hashlib.sha256(f"{reference_id.strip()}\n{text}".encode()).hexdigest()[:16]


def iter_local_quotes(data: Any) -> Iterator[Tuple[str, str, str]]:
    """Yield ``(path, reference_id, supporting_text)`` for every local-source quote.

    Covers every ``supported_by`` list in the document and the quotes on
    ``references[].findings[]``, which inherit the parent reference's id.
    """

    def walk(node: Any, path: str) -> Iterator[Tuple[str, str, str]]:
        if isinstance(node, dict):
            supported_by = node.get("supported_by")
            if isinstance(supported_by, list):
                for i, item in enumerate(supported_by):
                    if not isinstance(item, dict):
                        continue
                    yield from _emit(
                        item.get("reference_id"),
                        item,
                        f"{path}.supported_by[{i}]" if path else f"supported_by[{i}]",
                    )
            for key, value in node.items():
                yield from walk(value, f"{path}.{key}" if path else str(key))
        elif isinstance(node, list):
            for i, value in enumerate(node):
                yield from walk(value, f"{path}[{i}]")

    yield from walk(data, "")
    references = data.get("references") if isinstance(data, dict) else None
    for i, reference in enumerate(references or []):
        if not isinstance(reference, dict):
            continue
        for j, finding in enumerate(reference.get("findings") or []):
            if isinstance(finding, dict):
                yield from _emit(
                    reference.get("id"), finding, f"references[{i}].findings[{j}]"
                )


def _emit(reference_id: Any, item: Dict[str, Any], path: str):
    if not isinstance(reference_id, str) or local_prefix(reference_id) is None:
        return
    quote = item.get("supporting_text")
    if not isinstance(quote, str) or not quote.strip():
        return
    yield f"{path}.supporting_text", reference_id.strip(), quote


def find_local_quote_failures(
    data: Any, project_root: Path = PROJECT_ROOT
) -> List[Tuple[str, str, str, str]]:
    """Return ``(path, reference_id, quote, reason)`` for each failing local quote.

    ``reason`` is ``unresolved`` when the source file is missing and
    ``not_found`` when the quote is not in it.
    """
    failures = []
    for path, reference_id, quote in iter_local_quotes(data):
        source = resolve_local_source(reference_id, project_root)
        if source is None:
            failures.append((path, reference_id, quote, "unresolved"))
        elif not quote_matches(quote, source):
            failures.append((path, reference_id, quote, "not_found"))
    return failures


@lru_cache(maxsize=1)
def _baseline(path: Path = BASELINE_PATH) -> Dict[str, Set[str]]:
    if not path.exists():
        return {}
    loaded = yaml.safe_load(path.read_text()) or {}
    entries = loaded.get("entries") or {}
    return {str(k): set(v or []) for k, v in entries.items()}


def baseline_key(yaml_file: Path, project_root: Path = PROJECT_ROOT) -> Optional[str]:
    """Repo-relative POSIX path used to key a review in the baseline."""
    try:
        return yaml_file.resolve().relative_to(project_root).as_posix()
    except ValueError:
        return None


def validate_local_source_quotes(
    data: Any,
    report: ValidationReport,
    yaml_file: Optional[Path] = None,
    project_root: Path = PROJECT_ROOT,
) -> None:
    """Report ``file:`` / ``Reactome:`` quotes that are not in their source."""
    key = baseline_key(yaml_file, project_root) if yaml_file is not None else None
    known = _baseline().get(key, set()) if key else set()
    for path, reference_id, quote, reason in find_local_quote_failures(
        data, project_root
    ):
        listed = quote_digest(reference_id, quote) in known
        if reason == "unresolved":
            message = f"Cannot check supporting text: {reference_id} does not resolve to a file"
            if local_prefix(reference_id) == "Reactome":
                suggestion = (
                    "Cache the Reactome entry: uv run python -c \"from "
                    "ai_gene_review.etl.reactome import cache_reactome_pathway; "
                    f"cache_reactome_pathway('{reference_id}')\""
                )
            else:
                suggestion = "Point reference_id at an existing file under genes/ or the repository root"
        else:
            message = f"Supporting text is not a verbatim substring of {reference_id}"
            suggestion = (
                "Quote the source exactly (use ... between non-contiguous parts); a "
                "summary or placeholder belongs in the review text, not supporting_text"
            )
        if listed:
            message = f"{message} (known failure, listed in conf/local_quote_baseline.yaml)"
        report.add_issue(
            ValidationSeverity.WARNING if listed else ValidationSeverity.ERROR,
            message,
            path=path,
            suggestion=suggestion,
            validation_category="ReferenceValidator",
            check_type=CHECK_TYPE,
        )
