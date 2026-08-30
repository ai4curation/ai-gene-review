"""Warm the publications cache with full text via linkml-reference-validator.

This module drives the linkml-reference-validator (>= 0.2.1) full-text provider
chain — PMC, Europe PMC preprints, Unpaywall, OpenAlex by default — over the
repo's own ``publications/PMID_*.md`` cache to upgrade abstract-only records to
full text. It is modeled on the monarch-initiative/dismech
``warm-reference-cache`` workflow and adopts its durable tagging convention:

- A record that gains full text is rewritten with ``full_text_available: true``
  plus provenance tags (``full_text_provider``, ``full_text_extraction_method``,
  ``oa_status``, ``license``, ``full_text_url``) and ``full_text_attempted: true``.
- A record for which the chain concludes cleanly with no usable text is tagged
  ``full_text_attempted: true`` so it is never re-queried on later runs.
- A record whose attempt hit a transient error (download failure, provider
  outage) is left untouched, so a later run retries it.

Because attempts are durable, a bounded ``--limit`` sweep drains the backlog
incrementally and the whole operation is idempotent and resumable.

Unlike dismech, this repo's cache files are in the ai-gene-review format
(``pmid``/``full_text_available`` frontmatter, ``## Abstract`` / ``## Full Text``
sections), not linkml-reference-validator's native cache format, so the sweep
uses LRV's provider/locate/extract primitives but performs its own file rewrites
to preserve the repo format. Only locations LRV classifies as public
(``access_type`` absent or ``"open"``) are merged, mirroring LRV's own policy of
never mixing private-library full text into a shared cache.
"""

import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

from linkml_reference_validator.etl.fulltext.base import FullTextProviderRegistry
from linkml_reference_validator.etl.reference_fetcher import (
    MIN_FULL_TEXT_CHARS,
    ReferenceFetcher,
)
from linkml_reference_validator.models import ReferenceIdentifiers

logger = logging.getLogger(__name__)

FULL_TEXT_HEADER = "## Full Text"


@dataclass
class WarmCandidate:
    """A cached publication that should be attempted for full text."""

    path: Path
    pmid: str
    pmcid: Optional[str] = None
    doi: Optional[str] = None


def parse_publication_file(path: Path) -> Tuple[Dict[str, Any], str]:
    """Split a publication cache file into (frontmatter dict, body text).

    The body is returned verbatim (including its leading newlines) so a
    rewrite that only changes frontmatter is byte-stable for the body.

    Raises:
        ValueError: If the file has no parseable YAML frontmatter.
    """
    content = path.read_text()
    if not content.startswith("---"):
        raise ValueError(f"No frontmatter in {path}")
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Malformed frontmatter in {path}")
    frontmatter = yaml.safe_load(parts[1])
    if not isinstance(frontmatter, dict):
        raise ValueError(f"Frontmatter is not a mapping in {path}")
    return frontmatter, parts[2]


def find_warm_candidates(
    publications_dir: Path = Path("publications"),
) -> List[WarmCandidate]:
    """Find cached publications that need a (first) full-text attempt.

    A candidate lacks full text — ``full_text_available`` false, or no
    ``## Full Text`` section despite the flag — and has never been durably
    attempted (no ``full_text_attempted: true``).
    """
    candidates: List[WarmCandidate] = []
    for md_file in sorted(publications_dir.glob("PMID_*.md")):
        try:
            frontmatter, body = parse_publication_file(md_file)
        except (ValueError, yaml.YAMLError) as exc:
            logger.warning("Skipping unparseable %s: %s", md_file.name, exc)
            continue

        if frontmatter.get("full_text_attempted"):
            continue
        has_full_text = bool(frontmatter.get("full_text_available")) and (
            FULL_TEXT_HEADER in body
        )
        if has_full_text:
            continue

        pmid = str(frontmatter.get("pmid") or md_file.stem.removeprefix("PMID_"))
        candidates.append(
            WarmCandidate(
                path=md_file,
                pmid=pmid,
                pmcid=frontmatter.get("pmcid"),
                doi=frontmatter.get("doi"),
            )
        )
    return candidates


def identifiers_from_frontmatter(frontmatter: Dict[str, Any]) -> ReferenceIdentifiers:
    """Build LRV cross-walked identifiers from repo-format frontmatter.

    The repo stores PMC ids with the ``PMC`` prefix (``PMC84019``) while LRV's
    PMC provider expects the bare numeric id, so the prefix is stripped.
    """
    pmcid = frontmatter.get("pmcid")
    if isinstance(pmcid, str) and pmcid.upper().startswith("PMC"):
        pmcid = pmcid[3:]
    return ReferenceIdentifiers(
        pmid=str(frontmatter["pmid"]) if frontmatter.get("pmid") else None,
        pmcid=str(pmcid) if pmcid else None,
        doi=frontmatter.get("doi") or None,
    )


def _rewrite(path: Path, frontmatter: Dict[str, Any], body: str) -> None:
    """Write frontmatter + body back in the repo's cache format.

    Trailing per-line whitespace is stripped, matching
    ``Publication.to_markdown`` so rewrites stay clean for Git tooling.
    """
    frontmatter_text = yaml.dump(
        frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False
    )
    markdown = f"---\n{frontmatter_text}---{body}"
    markdown = re.sub(r"[ \t]+(?=\r?$)", "", markdown, flags=re.MULTILINE)
    if not markdown.endswith("\n"):
        markdown += "\n"
    path.write_text(markdown)


def mark_attempted(path: Path, frontmatter: Dict[str, Any], body: str) -> None:
    """Durably record that the full-text chain ran cleanly and found nothing."""
    frontmatter["full_text_attempted"] = True
    _rewrite(path, frontmatter, body)


def apply_full_text(
    path: Path,
    frontmatter: Dict[str, Any],
    body: str,
    *,
    text: str,
    extraction_method: str,
    provider: str,
    oa_status: Optional[str] = None,
    license: Optional[str] = None,
    full_text_url: Optional[str] = None,
) -> None:
    """Merge retrieved full text into a cache file with provenance tags."""
    frontmatter["full_text_available"] = True
    frontmatter["full_text_extraction_method"] = extraction_method
    frontmatter["full_text_provider"] = provider
    frontmatter["full_text_attempted"] = True
    if oa_status:
        frontmatter["oa_status"] = oa_status
    if license:
        frontmatter["license"] = license
    if full_text_url:
        frontmatter["full_text_url"] = full_text_url

    # Replace any existing (stale/partial) Full Text section outright.
    section_start = body.find(FULL_TEXT_HEADER)
    if section_start != -1:
        body = body[:section_start].rstrip("\n") + "\n"
    body = body.rstrip("\n") + f"\n\n{FULL_TEXT_HEADER}\n\n{text.strip()}\n"
    _rewrite(path, frontmatter, body)


def warm_publication(
    path: Path,
    fetcher: ReferenceFetcher,
    providers: Optional[List[str]] = None,
) -> str:
    """Attempt full text for one cached publication via the LRV provider chain.

    Mirrors ``ReferenceFetcher._enrich_with_full_text`` semantics: the first
    public location with usable text wins; a clean no-text conclusion is tagged
    durably; a transient error leaves the record retryable.

    Returns:
        ``"full_text"`` — full text merged into the cache file;
        ``"attempted"`` — chain ran cleanly, no usable text, tagged durably;
        ``"transient_error"`` — a provider/download error occurred, not tagged.
    """
    frontmatter, body = parse_publication_file(path)
    ids = identifiers_from_frontmatter(frontmatter)
    provider_names = providers or fetcher.config.full_text_providers
    had_error = False

    for provider_name in provider_names:
        provider = FullTextProviderRegistry.get(provider_name)
        if provider is None:
            logger.debug("Full-text provider not registered: %s", provider_name)
            continue

        try:  # external system boundary: one provider must not abort the chain
            location = provider.locate(ids, fetcher.config)
        except Exception as exc:
            logger.warning(
                "Provider '%s' failed for PMID:%s: %s", provider_name, ids.pmid, exc
            )
            had_error = True
            continue

        if location is None:
            continue
        if location.access_type not in (None, "open"):
            logger.info(
                "Ignoring non-public full text from '%s' for PMID:%s",
                provider_name,
                ids.pmid,
            )
            continue

        # LRV's blessed download/sniff/extract path. `_materialize` is the same
        # routine `ReferenceFetcher.fetch` uses internally; it is not yet public
        # API — public-API request tracked in
        # https://github.com/ai4curation/ai-gene-review/issues/2789 (to be
        # transferred to linkml-reference-validator).
        text, fmt, _pdf_bytes, error = fetcher._materialize(location)
        if error:
            had_error = True
        if not text or len(text.strip()) < MIN_FULL_TEXT_CHARS:
            continue

        apply_full_text(
            path,
            frontmatter,
            body,
            text=text,
            extraction_method=fmt or "text",
            provider=location.provider or provider_name,
            oa_status=location.oa_status,
            license=location.license,
            full_text_url=location.url,
        )
        return "full_text"

    if had_error:
        return "transient_error"
    mark_attempted(path, frontmatter, body)
    return "attempted"


def warm_publications(
    publications_dir: Path = Path("publications"),
    limit: Optional[int] = None,
    delay: float = 0.3,
    providers: Optional[List[str]] = None,
    dry_run: bool = False,
    fetcher: Optional[ReferenceFetcher] = None,
) -> Dict[str, int]:
    """Run a bounded, resumable full-text warm sweep over the cache.

    Args:
        publications_dir: Directory of ``PMID_*.md`` cache files.
        limit: Maximum records to attempt this run (None = all).
        delay: Seconds to sleep between records, on top of LRV's own
            per-request rate limiting.
        providers: Provider-chain override (default: LRV config order).
        dry_run: Report candidates without touching the network or files.
        fetcher: Pre-built ReferenceFetcher (built with defaults if omitted).

    Returns:
        Counts: ``candidates``, ``processed``, ``full_text``, ``attempted``,
        ``transient_error``.
    """
    candidates = find_warm_candidates(publications_dir)
    stats = {
        "candidates": len(candidates),
        "processed": 0,
        "full_text": 0,
        "attempted": 0,
        "transient_error": 0,
    }
    if limit is not None:
        candidates = candidates[:limit]
    if dry_run:
        for candidate in candidates:
            print(
                f"would attempt PMID:{candidate.pmid}"
                f" (pmcid={candidate.pmcid or '-'}, doi={candidate.doi or '-'})"
            )
        return stats

    if fetcher is None:
        from linkml_reference_validator.models import ReferenceValidationConfig

        fetcher = ReferenceFetcher(
            ReferenceValidationConfig(email="ai-gene-review@example.com")
        )

    total = len(candidates)
    for i, candidate in enumerate(candidates):
        outcome = warm_publication(candidate.path, fetcher, providers)
        stats[outcome] += 1
        stats["processed"] += 1
        print(f"[{i + 1}/{total}] PMID:{candidate.pmid} -> {outcome}")
        if delay and i < total - 1:
            time.sleep(delay)
    return stats
