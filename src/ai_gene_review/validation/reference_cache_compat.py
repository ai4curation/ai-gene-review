"""Backport the cache delimiter fix for the pinned LRV 0.2.1 release.

The loader below is adapted from linkml-reference-validator 0.2.1,
Copyright 2025 Chris Mungall, Apache-2.0 (see
``docs/licenses/linkml-reference-validator-Apache-2.0.txt``).
Delimiter detection and malformed-metadata handling are guarded; valid metadata,
extraction and validation retain upstream behavior. Upstream fixed this in commit
https://github.com/linkml/linkml-reference-validator/commit/dd9940dacd34b64a83bc1143414ca9ee4f32f3ee
but that unreleased branch also changes cache refresh semantics.

The dependency has no fetcher-factory argument on its validator or CLI. Repo
validation entry points and reference-cache utilities explicitly install this
version-limited method backport. No installed file or cache is rewritten. Remove it when the pinned
release contains the upstream fix.
"""

from importlib.metadata import version
import logging
import re
from typing import Optional

from ruamel.yaml import YAML
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import ReferenceContent

logger = logging.getLogger(__name__)


def _load_markdown_format_021(
    self, content_text: str, reference_id: str
) -> Optional[ReferenceContent]:
    """Load reference from markdown format with YAML frontmatter.

    Args:
        content_text: File contents
        reference_id: Reference identifier

    Returns:
        ReferenceContent if successful, None otherwise
    """
    parts = re.split(r"(?m)^---[\t ]*\r?$", content_text, maxsplit=2)
    if len(parts) < 3:
        logger.warning(f"Invalid markdown format for {reference_id}")
        return None

    yaml_parser = YAML(typ="safe")
    frontmatter = yaml_parser.load(parts[1])
    if not isinstance(frontmatter, dict):
        logger.warning("Invalid markdown frontmatter mapping for %s", reference_id)
        return None
    body = parts[2].strip()

    content = self._extract_content_from_markdown(body)

    authors = self._as_optional_list(frontmatter.get("authors"))
    keywords = self._as_optional_list(frontmatter.get("keywords"))
    publication_types = self._as_optional_list(frontmatter.get("publication_types"))

    # Parse supplementary files
    supplementary_files = self._parse_supplementary_files(
        frontmatter.get("supplementary_files")
    )

    metadata: dict = {}
    if "extra_fields_captured" in frontmatter:
        metadata["extra_fields_captured"] = frontmatter["extra_fields_captured"]

    return ReferenceContent(
        reference_id=frontmatter.get("reference_id", reference_id),
        title=frontmatter.get("title"),
        content=content,
        content_type=frontmatter.get("content_type", "unknown"),
        authors=authors,
        journal=frontmatter.get("journal"),
        year=str(frontmatter.get("year")) if frontmatter.get("year") else None,
        doi=frontmatter.get("doi"),
        keywords=keywords,
        publication_types=publication_types,
        supplementary_files=supplementary_files,
        metadata=metadata,
        full_text_provider=frontmatter.get("full_text_provider"),
        full_text_url=frontmatter.get("full_text_url"),
        oa_status=frontmatter.get("oa_status"),
        license=frontmatter.get("license"),
        local_pdf_path=frontmatter.get("local_pdf_path"),
        full_text_access_type=frontmatter.get("full_text_access_type"),
        full_text_source_item_id=frontmatter.get("full_text_source_item_id"),
        is_preprint=frontmatter.get("is_preprint"),
        peer_review_status=frontmatter.get("peer_review_status"),
        full_text_attempted=bool(frontmatter.get("full_text_attempted", False)),
    )


def install_reference_cache_compatibility() -> bool:
    """Install only the affected 0.2.1 loader; return whether it is active."""
    installed_version = version("linkml-reference-validator")
    if installed_version != "0.2.1":
        logger.warning(
            "Reference-cache delimiter backport is inactive for LRV %s; "
            "verify upstream delimiter handling before updating the lock.",
            installed_version,
        )
        return False
    if ReferenceFetcher._load_markdown_format is not _load_markdown_format_021:
        ReferenceFetcher._load_markdown_format = _load_markdown_format_021
    return True
