"""Shared helpers for validating literature supporting-text snippets."""

from functools import lru_cache
from pathlib import Path
from typing import Optional

import re

import yaml


LITERATURE_PREFIXES = frozenset({"PMID", "DOI"})


@lru_cache(maxsize=None)
def build_supporting_text_validator(publications_dir: Optional[Path] = None):
    """Build the shared deterministic supporting-text validator.

    The validator is configured from ``conf/reference_validator_config.yaml`` —
    the same file the CLI passes to the external reference validator via
    ``--config`` — so the repo-local ``findings`` path and the CLI/``supported_by``
    path agree. In particular this loads ``literal_bracket_patterns``, which keep
    bracketed chemical notation such as ``[4Fe-4S]`` or ``[Na(+)]`` from being
    stripped as citation markers, and ``skip_prefixes`` / ``unknown_prefix_severity``.
    ``cache_dir`` is taken from ``publications_dir`` and ``fetch_full_text`` is
    forced off regardless of what the config declares.
    """
    project_root = Path(__file__).resolve().parents[3]
    if publications_dir is None:
        publications_dir = project_root / "publications"
    try:
        from linkml_reference_validator.models import ReferenceValidationConfig
        from linkml_reference_validator.validation.supporting_text_validator import (
            SupportingTextValidator,
        )
    except ImportError:
        return None, publications_dir

    config_data: dict = {}
    config_path = project_root / "conf" / "reference_validator_config.yaml"
    if config_path.exists():
        loaded = yaml.safe_load(config_path.read_text())
        if isinstance(loaded, dict):
            config_data = dict(loaded)

    # The caller owns the cache directory; never let the config's relative
    # cache_dir override the resolved absolute path. Resolve reference_base_dir
    # against the project root so file: references still resolve, and force
    # full-text fetching off (the findings path only checks cached text).
    config_data["cache_dir"] = publications_dir
    config_data["fetch_full_text"] = False
    reference_base_dir = config_data.get("reference_base_dir")
    if reference_base_dir is not None and not Path(reference_base_dir).is_absolute():
        config_data["reference_base_dir"] = project_root / reference_base_dir

    config = ReferenceValidationConfig(**config_data)
    return SupportingTextValidator(config), publications_dir


def is_unfetchable(message: str) -> bool:
    """Return whether a validation failure reflects unavailable source text."""
    lowered = message.lower()
    return "could not fetch" in lowered or "no records found" in lowered


def clear_publication_caches() -> None:
    """Drop the memoised reads of the publication cache.

    ``cached_full_text_available``, ``cached_record_has_no_body`` and
    ``cached_text_missing`` are ``lru_cache``d filesystem reads with no invalidation, which
    is fine for a validation run (nothing writes) and a trap for a repair workflow: call
    ``cache_publication(pmid, force=True)`` and re-validate **in the same process** and you
    get the pre-repair answer. Exactly that sequence repaired six stub records in this
    repository; it only escaped the trap because the steps ran as separate processes.

    Call this after any write to ``publications/``.
    """
    cached_full_text_available.cache_clear()
    cached_record_has_no_body.cache_clear()
    cached_text_missing.cache_clear()


#: ``content_type`` values that mean the record carries no full text. A negative list,
#: matching ``etl/publication.py``: any other value (``full_text_xml``, ``full_text_html``,
#: ``full_text_pdf``, ``url``, ...) means full text is present.
NO_FULL_TEXT_CONTENT_TYPES = frozenset({"abstract_only", "unavailable"})


@lru_cache(maxsize=None)
def cached_record_has_no_body(
    reference_id: str,
    publications_dir: Path,
) -> bool:
    """True when the cached record carries no prose worth quoting.

    A record can be cached, report ``full_text_available: false``, and still have nothing in
    it -- six such stubs existed in this repository, each with ``authors: []`` and a body of
    ``"Cached metadata for local validation."``. Telling an author to "quote a verbatim
    substring of the cached abstract" is impossible advice there, and the remedy is different:
    the metadata fetch failed, so the record needs re-fetching rather than a better quote.

    Deliberately conservative: this keys on the stub's literal signature and on an empty
    body, not on a length threshold. A first version used ``len(body) < 80`` and immediately
    misclassified a genuinely short abstract in the test suite as a stub -- short abstracts
    exist, and telling their authors to re-fetch a perfectly good record is the same class of
    impossible advice this function was added to remove.
    """
    prefix, separator, _ = reference_id.partition(":")
    if not separator or prefix.upper() not in {"PMID", "DOI"}:
        return False
    text = _cached_text(reference_id, publications_dir)
    if text is None:
        return False
    body = text.split("---", 2)[-1]
    body = re.sub(r"^#.*$", "", body, flags=re.M)          # drop the title heading
    body = re.sub(r"^##\s*\w[\w \t]*$", "", body, flags=re.M)  # drop section headings
    body = re.sub(r"\s+", " ", body).strip()
    return not body or body == "Cached metadata for local validation."


@lru_cache(maxsize=None)
def cached_text_missing(reference_id: str, publications_dir: Path) -> bool:
    """True when no cached record exists for *reference_id* at all.

    Distinct from ``cached_full_text_available(...) is None``, which means "availability is
    not recorded" and is true of plenty of records that are cached and have a full body.
    Conflating the two is what this predicate exists to prevent.
    """
    return _cached_text(reference_id, publications_dir) is None


def _cached_text(reference_id: str, publications_dir: Path) -> Optional[str]:
    """Raw text of the cached record for *reference_id*, or None."""
    prefix, separator, identifier = reference_id.partition(":")
    if not separator:
        return None
    if prefix.upper() == "PMID":
        filename = f"PMID_{identifier}.md"
    elif prefix.upper() == "DOI":
        filename = f"DOI_{identifier.replace('/', '_')}.md"
    else:
        return None
    path = publications_dir / filename
    return path.read_text() if path.exists() else None


@lru_cache(maxsize=None)
def cached_full_text_available(
    reference_id: str,
    publications_dir: Path,
) -> Optional[bool]:
    """Return cached full-text availability, or `None` when not recorded."""
    text = _cached_text(reference_id, publications_dir)
    if text is None:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    frontmatter = yaml.safe_load(text[3:end])
    if not isinstance(frontmatter, dict):
        return None
    if "full_text_available" in frontmatter:
        return bool(frontmatter["full_text_available"])
    content_type = frontmatter.get("content_type")
    if not isinstance(content_type, str):
        return None
    # Mirror the authoritative mapping in etl/publication.py, which is a NEGATIVE list:
    #   full_text_available = content_type not in ("unavailable", "abstract_only")
    # An earlier positive allow-list here named only full_text_html and full_text_pdf, so
    # every full_text_xml record -- 90 of them, including PMC-sourced green-OA bodies --
    # resolved to None. None here means "not recorded", and a caller that reads it as "not
    # cached" then tells the author to go cache a record that is already there.
    normalized_content_type = content_type.lower()
    if normalized_content_type in NO_FULL_TEXT_CONTENT_TYPES:
        return False
    return True
