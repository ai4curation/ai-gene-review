"""Shared helpers for validating literature supporting-text snippets."""

from functools import lru_cache
from pathlib import Path
from typing import Optional

import yaml


LITERATURE_PREFIXES = frozenset({"PMID", "DOI"})


@lru_cache(maxsize=None)
def build_supporting_text_validator(publications_dir: Optional[Path] = None):
    """Build the shared deterministic supporting-text validator."""
    if publications_dir is None:
        publications_dir = Path(__file__).resolve().parents[3] / "publications"
    try:
        from linkml_reference_validator.models import ReferenceValidationConfig
        from linkml_reference_validator.validation.supporting_text_validator import (
            SupportingTextValidator,
        )
    except ImportError:
        return None, publications_dir
    config = ReferenceValidationConfig(
        cache_dir=publications_dir,
        fetch_full_text=False,
    )
    return SupportingTextValidator(config), publications_dir


def is_unfetchable(message: str) -> bool:
    """Return whether a validation failure reflects unavailable source text."""
    lowered = message.lower()
    return "could not fetch" in lowered or "no records found" in lowered


@lru_cache(maxsize=None)
def cached_full_text_available(
    reference_id: str,
    publications_dir: Path,
) -> Optional[bool]:
    """Return cached full-text availability, or `None` when not recorded."""
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
    if not path.exists():
        return None
    text = path.read_text()
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
    normalized_content_type = content_type.lower()
    if normalized_content_type in {"abstract_only", "unavailable"}:
        return False
    if normalized_content_type in {"full_text_html", "full_text_pdf"}:
        return True
    return None
