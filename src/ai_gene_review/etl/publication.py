"""ETL for fetching and caching PubMed/PMC publications.

This module provides comprehensive publication retrieval with multiple fallback strategies
to maximize full text access from PMC (PubMed Central).

## PMC Access Patterns

PMC hosts articles for long-term preservation and web access, but publishers retain
control over programmatic API access:

- **Open Access Journals** (e.g., PLoS ONE): Full XML available via Entrez API with
  complete <body> sections containing article text
- **Publisher-Restricted Journals** (e.g., Cell Reports, Nature): XML API returns only
  metadata with comment "The publisher does not allow downloading of the full text in XML form"
- **HTML Always Available**: All PMC articles provide full text via web interface
  regardless of XML API restrictions

## Retrieval Strategy

The module uses a cascading fallback approach to maximize content retrieval:

1. **XML API First**: Fast, structured access for open access articles
2. **HTML Scraping Fallback**: When XML is restricted, scrape PMC web pages
3. **PDF Extraction Fallback**: For cases where HTML content is insufficient
   (currently limited by PMC's download interstitials)

This approach achieves ~90% success rate for full text retrieval from PMC articles,
dramatically improving content availability compared to XML-only approaches.

## Performance Notes

- XML retrieval: ~1-2 seconds per article
- HTML scraping: ~3-5 seconds per article
- PDF extraction: ~10-15 seconds per article (when accessible)
- Rate limiting: 1-2 second delays between requests to be polite to NCBI servers
"""

import io
import re
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, cast

import requests
import yaml
from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel
import fitz  # type: ignore  # PyMuPDF

# No cycle: validation/supporting_text imports only stdlib and yaml.
from ai_gene_review.validation.supporting_text import (
    NO_FULL_TEXT_CONTENT_TYPES,
    clear_publication_caches,
)
from PyPDF2 import PdfReader
from Bio import Entrez  # type: ignore[import-untyped]

# Set email for NCBI (required for Entrez)
Entrez.email = "ai-gene-review@example.com"  # type: ignore

# Cache for PMC overrides
_PMC_OVERRIDES_CACHE: Optional[Dict[str, Optional[str]]] = None


def load_pmc_overrides() -> Dict[str, Optional[str]]:
    """Load PMC ID overrides from TSV file.
    
    Returns a dictionary mapping PMID to corrected PMCID (or None if no PMC version exists).
    This handles cases where NCBI's database has incorrect PMC linkages.
    
    Returns:
        Dictionary mapping PMID strings to PMCID strings (or None)
        
    Example:
        >>> overrides = load_pmc_overrides()
        >>> # If PMID 2001740 is in overrides with no PMC:
        >>> # overrides.get('2001740') returns None (but key exists)
        >>> # overrides.get('99999999') returns None (key doesn't exist)
    """
    global _PMC_OVERRIDES_CACHE
    
    if _PMC_OVERRIDES_CACHE is not None:
        return _PMC_OVERRIDES_CACHE
    
    overrides: Dict[str, Optional[str]] = {}
    
    # Try to find the overrides file
    override_paths = [
        Path(__file__).parent / "pmc_overrides.tsv",
        Path("src/ai_gene_review/etl/pmc_overrides.tsv"),
        Path("pmc_overrides.tsv"),
    ]
    
    override_file = None
    for path in override_paths:
        if path.exists():
            override_file = path
            break
    
    if not override_file:
        # No overrides file found, return empty dict
        _PMC_OVERRIDES_CACHE = overrides
        return overrides
    
    try:
        with open(override_file, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith('#'):
                    continue
                
                # Split on tab
                parts = line.split('\t')
                if len(parts) >= 1:
                    pmid = parts[0].strip()
                    # PMCID is in second column (may be empty)
                    pmcid = parts[1].strip() if len(parts) >= 2 and parts[1].strip() else None
                    overrides[pmid] = pmcid
    
    except Exception as e:
        print(f"Warning: Could not load PMC overrides: {e}")
    
    _PMC_OVERRIDES_CACHE = overrides
    return overrides


class FullTextResult(BaseModel):
    """Result of full text retrieval attempt.

    This class can be extended in the future to include structured sections,
    images, tables, etc.
    """

    content: Optional[str] = None
    available: bool = False
    extraction_method: Optional[str] = None  # 'xml', 'html', 'pdf', 'abstract_only', etc.
    is_complete: bool = False  # True if we got the full article, False if just abstract


@dataclass
class Publication:
    """Represents a publication with metadata and content.

    Example:
        >>> pub = Publication(
        ...     pmid="12345",
        ...     title="Test Article",
        ...     authors=["Smith J", "Doe J"],
        ...     journal="Test Journal",
        ...     year="2024",
        ...     abstract="This is a test abstract."
        ... )
        >>> frontmatter = pub.to_frontmatter_dict()
        >>> frontmatter['pmid']
        '12345'
        >>> len(pub.to_markdown()) > 0
        True
    """

    pmid: str
    title: str
    authors: List[str]
    journal: str
    year: str
    abstract: str
    full_text: Optional[str] = None
    full_text_available: bool = False
    full_text_extraction_method: Optional[str] = None  # 'xml', 'html', 'pdf', 'abstract_only', None
    pmcid: Optional[str] = None
    doi: Optional[str] = None
    keywords: Optional[List[str]] = None
    pubmed_publication_types: Optional[List[str]] = None  # raw PubMed PT list
    #: Frontmatter keys this dataclass has no field for, preserved verbatim on write.
    #: publication_warm writes full_text_provider, full_text_url, oa_status, license and
    #: full_text_attempted straight into frontmatter, so a rewrite through Publication
    #: silently dropped them -- including `license`, which governs redistribution of the
    #: very text a carry-forward is preserving.
    extra_frontmatter: Optional[Dict[str, Any]] = None

    @property
    def publication_type(self) -> Optional[str]:
        """Classified PublicationTypeEnum value inferred from PubMed PT metadata.

        Returns ``None`` if no PubMed publication-type metadata is available.
        """
        if not self.pubmed_publication_types:
            return None
        from ai_gene_review.etl.publication_type import (
            classify_pubmed_publication_type,
        )

        return classify_pubmed_publication_type(self.pubmed_publication_types)

    def to_frontmatter_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for YAML frontmatter."""
        data = {
            "pmid": self.pmid,
            "title": self.title,
            "authors": self.authors,
            "journal": self.journal,
            "year": self.year,
            "full_text_available": self.full_text_available,
        }
        if self.full_text_extraction_method:
            data["full_text_extraction_method"] = self.full_text_extraction_method
        for key, value in (self.extra_frontmatter or {}).items():
            data.setdefault(key, value)
        if self.pmcid:
            data["pmcid"] = self.pmcid
        if self.doi:
            data["doi"] = self.doi
        if self.keywords:
            data["keywords"] = self.keywords
        if self.pubmed_publication_types:
            data["pubmed_publication_types"] = self.pubmed_publication_types
            data["publication_type"] = self.publication_type
        return data

    def to_markdown(self) -> str:
        """Generate markdown content with frontmatter."""
        # Create frontmatter
        frontmatter = yaml.dump(
            self.to_frontmatter_dict(),
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )

        # Create markdown body
        body_parts = [f"# {self.title}\n"]

        if self.authors:
            body_parts.append(f"**Authors:** {', '.join(self.authors)}\n")

        body_parts.append(f"**Journal:** {self.journal} ({self.year})\n")

        if self.doi:
            body_parts.append(f"**DOI:** [{self.doi}](https://doi.org/{self.doi})\n")

        if self.pmcid:
            body_parts.append(
                f"**PMC:** [{self.pmcid}](https://www.ncbi.nlm.nih.gov/pmc/articles/{self.pmcid}/)\n"
            )

        body_parts.append(f"\n## Abstract\n\n{self.abstract}\n")

        if self.full_text:
            body_parts.append(f"\n## Full Text\n\n{self.full_text}\n")

        markdown = f"---\n{frontmatter}---\n\n{''.join(body_parts)}"
        # PubMed's plain-text records can contain spaces before line breaks.
        # Generated caches intentionally do not preserve Markdown hard-break
        # whitespace; keep their content and indentation clean for Git tooling.
        return re.sub(r"[ \t]+(?=\r?$)", "", markdown, flags=re.MULTILINE)


def extract_pmid(pmid_str: str) -> str:
    """Extract PMID from various formats.

    Examples:
        >>> extract_pmid('12345678')
        '12345678'
        >>> extract_pmid('PMID:12345678')
        '12345678'
        >>> extract_pmid('pmid: 12345678')
        '12345678'
        >>> extract_pmid('PMID12345678')
        '12345678'
        >>> extract_pmid(' PMID: 12345678 ')
        '12345678'
    """
    # Remove PMID prefix and clean up
    pmid = re.sub(r"^(PMID|pmid)[:\s]*", "", pmid_str.strip())
    return pmid.strip()


def doi_to_pmid(doi: str) -> Optional[str]:
    """Resolve a DOI to a PMID using NCBI Entrez API.

    Uses the ESearch API to look up a DOI in PubMed.

    Args:
        doi: DOI string (e.g., "10.1038/s41431-018-0141-z")

    Returns:
        PMID string if found, None otherwise

    Example:
        >>> # Network-dependent example:
        >>> # doi_to_pmid("10.1038/s41431-018-0141-z")
        >>> # '29727692'
    """
    handle = Entrez.esearch(db="pubmed", term=f"{doi}[DOI]", retmax=1)
    record = Entrez.read(handle)
    handle.close()

    id_list = record.get("IdList", [])
    if id_list:
        return str(id_list[0])
    return None


def convert_doi_publication(
    doi_file: Path,
    publications_dir: Path,
    pmid: Optional[str] = None,
) -> bool:
    """Convert a DOI-keyed publication file to PMID-keyed format.

    Reads the legacy DOI file (reference_id/content_type schema), resolves
    the DOI to a PMID if not provided, creates a new PMID-keyed file in
    the standard schema (pmid/full_text_available), and removes the DOI file.

    Args:
        doi_file: Path to the DOI-keyed markdown file
        publications_dir: Directory containing publications
        pmid: Pre-resolved PMID (skips DOI lookup if provided)

    Returns:
        True if conversion succeeded, False otherwise
    """
    content = doi_file.read_text()

    # Parse frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"Warning: Could not parse frontmatter in {doi_file.name}")
        return False

    frontmatter = yaml.safe_load(parts[1])
    doi = frontmatter.get("doi", "")

    # Resolve PMID if not provided
    if pmid is None:
        pmid = doi_to_pmid(doi)
        if pmid is None:
            print(f"Could not resolve DOI {doi} to PMID")
            return False

    # Check if PMID file already exists
    pmid_file = publications_dir / f"PMID_{pmid}.md"
    if pmid_file.exists():
        print(f"PMID file already exists: {pmid_file.name}, skipping conversion")
        return False

    # Build a Publication in the standard schema.
    #
    # An explicit `full_text_available` wins over `content_type`. Deriving it from
    # content_type alone made this a third writer that silently overrides a considered
    # judgement: four cached records were marked `false` by hand because their bodies are
    # openalex landing pages plus RIS citation exports, and two of those are
    # `content_type: full_text_html`, so this converter would have written `true` straight
    # back over them on the next `just convert-doi-publications`.
    #
    # The negative list is imported rather than repeated. It was a literal tuple here while
    # `NO_FULL_TEXT_CONTENT_TYPES` was authoritative elsewhere, which makes the constant
    # authoritative in name only -- a new value would diverge this converter from both the
    # validator and the flag audit.
    declared = frontmatter.get("full_text_available")
    content_type = frontmatter.get("content_type", "unavailable")
    if isinstance(declared, bool):
        full_text_available = declared
    elif isinstance(content_type, str):
        full_text_available = content_type.lower() not in NO_FULL_TEXT_CONTENT_TYPES
    else:
        # Mirror cached_full_text_available, which returns None for a non-string
        # content_type. `str(content_type).lower()` turned an explicit `content_type:`
        # (null) into "none", which is not in the negative list, so the record failed
        # *open* and was recorded as having full text.
        full_text_available = False

    # Extract abstract from body if present
    body = parts[2]
    content = ""
    needed_stripping = False
    if "## Content" in body:
        abstract_section = body.split("## Content", 1)[1].strip()
        # The lift is guarded for the same reason the flag is. `to_markdown` emits this
        # as `## Abstract` with no availability test, and for an abstract-only record the
        # validator tells authors to "quote a verbatim substring of the cached abstract" --
        # so a citation export lifted here becomes quotable text and a quote from its
        # `N2  -` line verifies. Conversion also drops content_type, full_text_provider,
        # full_text_url and oa_status, so `TY  - JOUR` is the only surviving signal that
        # the body is junk; checking it here is the last chance to notice.
        if abstract_section:
            needed_stripping = _carries_stub_marker(abstract_section)
            content = (
                _strip_stub_lines(abstract_section)
                if needed_stripping
                else abstract_section
            )

    # `## Content` is "the text we have"; `content_type` says which kind it is. Routing it
    # always to `abstract` produced a record that claimed full_text_available: true, stored
    # the text under `## Abstract`, and emitted no `## Full Text` -- so
    # cached_full_text_available called it complete while publication_warm's
    # `bool(flag) and FULL_TEXT_HEADER in body` called it a candidate for re-fetching. Two
    # consumers disagreeing about one record. Found by self-audit, not a regression from
    # this PR; fixed here because this PR has already edited this function twice.
    # A section that needed stripping was a landing page, so whatever survived is at best
    # abstract-grade -- on the live records the residue IS the abstract. Promoting it to
    # `full_text` would be bulk without body one writer over.
    #
    # `is_usable_full_text` has three rejection criteria and this converter can only apply
    # the first: the marker list. The other two -- "contained in the already-cached
    # abstract" and "adds less than MIN_FULL_TEXT_CHARS beyond it" -- are exactly what a
    # stripped landing page fails, and there is no separately cached abstract here to
    # compare against. So the conservative reading of a stripped section is the honest one.
    #
    # Gating the revision below on `if not content` alone made it unreachable whenever any
    # prose survived, which is the strip's whole purpose.
    if not content or needed_stripping:
        # An explicit `full_text_available` in the source still wins; only a derived one
        # is revised.
        if not isinstance(declared, bool):
            full_text_available = False

    full_text = content if (content and full_text_available) else None
    abstract = "No abstract available." if (full_text or not content) else content

    pub = Publication(
        pmid=pmid,
        title=frontmatter.get("title", "Unknown title"),
        authors=frontmatter.get("authors", []),
        journal=frontmatter.get("journal", "Unknown journal"),
        year=str(frontmatter.get("year", "Unknown")),
        abstract=abstract,
        doi=doi,
        full_text=full_text,
        full_text_available=full_text_available,
        full_text_extraction_method=(
            content_type.removeprefix("full_text_")
            if isinstance(content_type, str) and full_text
            else None
        ),
    )

    pmid_file.write_text(pub.to_markdown())
    doi_file.unlink()
    clear_publication_caches()
    print(f"Converted {doi_file.name} -> {pmid_file.name}")
    return True


def get_cached_title(
    pmid: str, cache_dir: Path = Path("publications")
) -> Optional[str]:
    """Get just the title from cached publication if available.

    Args:
        pmid: PubMed ID (without PMID prefix)
        cache_dir: Directory containing cached publications

    Returns:
        Title string if cached, None otherwise
    """
    cache_file = cache_dir / f"PMID_{pmid}.md"
    if cache_file.exists():
        # Parse the markdown file to get title
        content = cache_file.read_text()

        # Extract title from first # header
        for line in content.split("\n"):
            if line.startswith("# "):
                return line[2:].strip()

    return None


def get_cached_publication(
    pmid: str, cache_dir: Path = Path("publications")
) -> Optional[Publication]:
    """Get publication from cache if available.

    Args:
        pmid: PubMed ID (without PMID prefix)
        cache_dir: Directory containing cached publications

    Returns:
        Publication object if cached, None otherwise
    """
    # For now, return None to always fetch fresh for full data
    # Could implement full markdown parsing if needed
    return None


def _carries_stub_marker(text: str) -> bool:
    """True when *text* is a paywall stub, landing page or citation export, not prose."""
    from ai_gene_review.etl.publication_warm import FULL_TEXT_STUB_MARKERS

    return any(marker in text for marker in FULL_TEXT_STUB_MARKERS)


def _strip_stub_lines(text: str) -> str:
    """Drop the landing-page and citation-export lines, keep the paper's own prose.

    Rejecting the whole section was all-or-nothing and threw away real content: both DOI
    records this guards carry the paper's genuine abstract alongside the junk --
    `mmbr.00181-23` opens with ~1,500 characters of real SUMMARY before the
    `Research output` header and the RIS block, and `j.str.2024.02.015` has the marker
    first and the abstract after. Keeping the prose is equally safe, since what survives
    is the paper's own words.

    A RIS record is line-oriented (`TY  - JOUR`, `AU  - ...`, `ER  -`), so dropping tagged
    lines and marker lines leaves the prose paragraphs intact.
    """
    from ai_gene_review.etl.publication_warm import FULL_TEXT_STUB_MARKERS

    ris_tag = re.compile(r"^[A-Z][A-Z0-9]\s{2}-\s?")
    kept = [
        line
        for line in text.splitlines()
        if not ris_tag.match(line.strip())
        and not any(marker in line for marker in FULL_TEXT_STUB_MARKERS)
        and line.strip() != "}"
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


PROVENANCE_KEYS = (
    "full_text_provider",
    "full_text_url",
    "oa_status",
    "license",
    "full_text_attempted",
)


def _existing_accepted_full_text(
    path: Path,
) -> tuple[Optional[str], Optional[str], Dict[str, Any]]:
    """The cached record's full text, but only if the record itself vouches for it.

    Returns ``(None, None)`` unless the frontmatter says ``full_text_available: true``.
    Presence of a ``## Full Text`` section is not enough: 888 cached records carry one
    while declaring ``false``, because the body was rejected or is a heading plus the
    abstract (e.g. ``PMID_7262539``).
    """
    # A fourth hand-rolled parse of this format. The duplication is forced, not careless:
    # importing linkml_reference_validator's parser would drag that dependency into this
    # module, and validator.py treats it as optional.
    text = path.read_text()
    if not text.startswith("---"):
        return None, None, {}
    end = text.find("\n---", 3)
    if end == -1:
        return None, None, {}
    frontmatter = yaml.safe_load(text[3:end])
    if not isinstance(frontmatter, dict) or not frontmatter.get("full_text_available"):
        return None, None, {}
    body = text[end + 4 :]
    marker = "\n## Full Text\n"
    if marker not in body:
        return None, None, {}
    section = body.split(marker, 1)[1]
    next_heading = section.find("\n## ")
    if next_heading != -1:
        section = section[:next_heading]
    section = section.strip()
    if not section:
        return None, None, {}
    method = frontmatter.get("full_text_extraction_method")
    provenance = {k: frontmatter[k] for k in PROVENANCE_KEYS if k in frontmatter}
    return section, method if isinstance(method, str) else None, provenance


def accept_full_text(content: str | None, is_complete: bool, abstract: str) -> bool:
    """Whether fetched PMC text may be recorded as ``full_text_available``.

    ``FullTextResult.is_complete`` reports what the provider *claimed*, not what it
    returned. ``fetch_pmc_fulltext``'s HTML and PDF fallbacks can yield a repository
    landing page or a citation export that satisfies it, and this path used to set the
    flag straight from it -- which is how a RIS dump became "full text" for PMID:12534463
    and cost twelve accurate ``full_text_unavailable`` flags across ten reviews. The warm
    sweep already applied a content guard; this writer did not, and it is the path
    ``cache_publication(force=True)`` uses and the validator's error message recommends.

    Split out as a named function rather than left inline so it can be tested without
    faking Entrez. A first attempt monkeypatched a function that does not exist, so the
    stub was inert and the test passed with the guard deleted.
    """
    if not is_complete or not content:
        return False
    from ai_gene_review.etl.publication_warm import is_usable_full_text_for_abstract

    return is_usable_full_text_for_abstract(content, abstract)


def fetch_pubmed_data(
    pmid: str, use_cache: bool = True, cache_dir: Path = Path("publications")
) -> Optional[Publication]:
    """Fetch publication data from PubMed, using cache if available.

    Args:
        pmid: PubMed ID (without PMID prefix)
        use_cache: Whether to use cached data if available
        cache_dir: Directory for caching publications

    Returns:
        Publication object with abstract, or None if not found

    Example:
        >>> # This would require network access
        >>> # pub = fetch_pubmed_data("29727692")
        >>> # if pub:
        >>> #     assert pub.pmid == "29727692"
    """
    # Check cache first
    if use_cache:
        cached = get_cached_publication(pmid, cache_dir)
        if cached:
            return cached

    try:
        # Fetch summary from PubMed
        handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
        summary_records = Entrez.read(handle)
        handle.close()

        if not summary_records or "error" in summary_records[0]:
            return None

        record = summary_records[0]

        # Extract basic metadata (convert Bio.Entrez objects to strings)
        title = str(record.get("Title", "No title"))
        authors = [str(author) for author in record.get("AuthorList", [])]
        journal = str(record.get("Source", "Unknown journal"))
        year = (
            str(record.get("PubDate", "Unknown"))[:4]
            if "PubDate" in record
            else "Unknown"
        )
        doi = str(record.get("DOI", "")) if record.get("DOI") else None

        # PubMed publication types (PT), e.g. ["Journal Article", "Review"].
        pub_types = [str(pt) for pt in record.get("PubTypeList", [])] or None

        # Check for PMC ID with override support
        pmcid = None
        
        # First check if we have an override for this PMID
        overrides = load_pmc_overrides()
        if pmid in overrides:
            # Use the override value (which may be None if no PMC version exists)
            pmcid = overrides[pmid]
            if pmcid is None:
                print(f"PMID {pmid}: Using override - no PMC version available")
            else:
                print(f"PMID {pmid}: Using override PMC ID: {pmcid}")
        else:
            # No override, use normal PMC lookup methods
            # Method 1: Check ArticleIds
            if "ArticleIds" in record:
                article_ids = record["ArticleIds"]
                if isinstance(article_ids, dict):
                    for id_type, id_value in article_ids.items():
                        if "pmc" in str(id_type).lower():
                            pmcid = str(id_value)
                            break

            # Method 2: Use Entrez elink to find PMC ID
            if not pmcid:
                try:
                    handle = Entrez.elink(dbfrom="pubmed", db="pmc", id=pmid)
                    link_records = Entrez.read(handle)
                    handle.close()

                    if link_records and link_records[0].get("LinkSetDb"):
                        for linkset in link_records[0]["LinkSetDb"]:
                            # IMPORTANT: Only use "pubmed_pmc" LinkName (the PMC version of the article)
                            # NOT "pubmed_pmc_refs" (articles that cite this paper)
                            if (linkset.get("DbTo") == "pmc" and 
                                linkset.get("LinkName") == "pubmed_pmc" and 
                                linkset.get("Link")):
                                pmcid = "PMC" + str(linkset["Link"][0]["Id"])
                                break
                except Exception:
                    pass

        # Fetch abstract from PubMed
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
        abstract_text = handle.read()
        handle.close()

        # Clean up abstract
        abstract = abstract_text.strip()
        if not abstract or abstract == "":
            abstract = "No abstract available."

        publication = Publication(
            pmid=pmid,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            abstract=abstract,
            pmcid=pmcid,
            doi=doi,
            pubmed_publication_types=pub_types,
        )

        # Try to fetch full text from PMC if available
        if pmcid:
            full_text_result = fetch_pmc_fulltext(pmcid)
            accepted = accept_full_text(
                full_text_result.content,
                bool(full_text_result.is_complete),
                abstract or "",
            )
            # Judge before writing, as publication_warm.apply_full_text already does.
            # Guarding only the flag left the rejected text in `## Full Text`, which is the
            # body `supporting_text` quotes are matched against -- so the flag would stop
            # lying while the cache file started to. A quote lifted from a landing page
            # would then verify verbatim.
            if accepted:
                publication.full_text = full_text_result.content
                publication.full_text_extraction_method = (
                    full_text_result.extraction_method
                )
            publication.full_text_available = accepted

        # Cache the publication if we fetched it
        if use_cache:
            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = cache_dir / f"PMID_{pmid}.md"
            try:
                cache_file.write_text(publication.to_markdown())
                clear_publication_caches()
            except Exception:
                # Silently fail on cache write errors
                pass

        return publication

    except Exception as e:
        print(f"Error fetching PMID {pmid}: {e}")
        return None


def fetch_pmc_fulltext(pmcid: str) -> FullTextResult:
    """Fetch full text from PMC using cascading fallback strategies.

    Attempts to retrieve full article text via:
    1. Entrez XML API (fast, for open access journals)
    2. HTML scraping fallback (when publishers restrict XML API access)
    3. PDF extraction fallback (when HTML content insufficient)

    Publisher XML restrictions are detected by looking for the comment:
    "The publisher does not allow downloading of the full text in XML form"
    which appears in restricted articles despite PMC hosting the content.

    Args:
        pmcid: PMC ID (with or without PMC prefix)

    Returns:
        FullTextResult object with content and availability status.
        Success rate: ~90% for PMC articles with various access restrictions.
    """
    try:
        # Remove PMC prefix if present
        pmcid = pmcid.replace("PMC", "")

        # Fetch full text XML from PMC
        handle = Entrez.efetch(db="pmc", id=pmcid, rettype="full", retmode="xml")
        xml_data = handle.read()
        handle.close()

        # Convert bytes to string if needed
        if isinstance(xml_data, bytes):
            xml_data = xml_data.decode("utf-8")

        # Check for publisher restrictions
        if "does not allow downloading of the full text" in xml_data:
            print(
                f"PMC{pmcid}: Publisher restricts full text XML access, trying HTML fallback..."
            )
            return fetch_pmc_html_fallback(pmcid)

        # Parse XML to extract text
        root = ET.fromstring(xml_data)

        # Check if there's a body section (actual article content)
        body_elem = root.find(".//body")
        if body_elem is None:
            # No body section - try HTML fallback
            print(f"PMC{pmcid}: No body section found in XML, trying HTML fallback...")
            return fetch_pmc_html_fallback(pmcid)

        # Extract text from body sections
        body_texts = []

        # Look for main content sections
        for elem in body_elem.iter():
            if elem.tag in ["p", "title", "sec"]:
                text = "".join(elem.itertext()).strip()
                if text and len(text) > 10:  # Skip very short snippets
                    # Skip common metadata sections
                    if not any(
                        keyword in text.upper()
                        for keyword in [
                            "AUTHOR CONTRIBUTIONS",
                            "DECLARATION OF INTERESTS",
                            "FUNDING",
                            "ACKNOWLEDGMENTS",
                            "COPYRIGHT",
                        ]
                    ):
                        body_texts.append(text)

        # Also try to extract abstract from front matter if body is empty
        if not body_texts:
            abstract_elem = root.find(".//abstract")
            if abstract_elem is not None:
                abstract_text = "".join(abstract_elem.itertext()).strip()
                if abstract_text:
                    # We only got the abstract, not the full text
                    return FullTextResult(
                        content=abstract_text,
                        available=True,
                        extraction_method="xml_abstract_only",
                        is_complete=False
                    )

        if body_texts:
            # Check if we have substantial content beyond just abstract
            total_text = "\n\n".join(body_texts)
            # If we have more than 3000 chars, likely have full article
            is_complete = len(total_text) > 3000
            return FullTextResult(
                content=total_text,
                available=True,
                extraction_method="xml",
                is_complete=is_complete
            )
        else:
            print(f"PMC{pmcid}: No substantial content found in XML")
            return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)

    except ET.ParseError as e:
        print(f"PMC{pmcid}: XML parsing error - {e}")
        return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)
    except Exception as e:
        print(f"Could not fetch full text for PMC{pmcid}: {e}")
        return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)


_PMC_BOILERPLATE_PREFIXES = (
    "PMCID:",
    "PMID:",
    "DOI:",
    "COPYRIGHT",
    "DOWNLOAD PDF",
    "CITE THIS ARTICLE",
    "SHARE THIS ARTICLE",
    "AUTHOR INFORMATION",
    "FUNDING STATEMENT",
    "ETHICS STATEMENT",
    "DECLARATION OF INTERESTS",
    "DATA AVAILABILITY",
    "AUTHOR CONTRIBUTIONS",
)

_PMC_TERMINAL_HEADINGS = {
    "ACKNOWLEDGMENTS",
    "ACKNOWLEDGEMENTS",
    "CITED BY",
    "REFERENCES",
    "SIMILAR ARTICLES",
    "SUPPLEMENTARY MATERIAL",
}


def _extract_pmc_article_text(html: bytes | str) -> Optional[str]:
    """Extract body headings and paragraphs from current and legacy PMC HTML."""
    soup = BeautifulSoup(html, "html.parser")
    article_content = cast(
        Optional[Tag], soup.select_one("section.body.main-article-body")
    )
    if not article_content:
        article_content = cast(
            Optional[Tag], soup.select_one("section[aria-label='Article content']")
        )
    if not article_content:
        article_content = cast(Optional[Tag], soup.find("article"))
    if not article_content:
        article_content = cast(
            Optional[Tag],
            soup.find("div", class_="article") or soup.find("div", class_="tsec"),
        )
    if not article_content:
        article_content = cast(
            Optional[Tag], soup.find("div", id="article-body") or soup.find("main")
        )
    if not article_content:
        for div in soup.find_all("div"):
            if isinstance(div, Tag) and len(div.find_all("p", recursive=False)) >= 3:
                article_content = div
                break
    if not article_content:
        article_content = cast(Tag, soup)

    parts: List[str] = []
    pending_headings: List[str] = []
    for element in article_content.find_all(["h1", "h2", "h3", "h4", "p"]):
        if not isinstance(element, Tag):
            continue
        if element.find_parent(["figcaption", "table", "nav", "aside", "footer"]):
            continue

        text = element.get_text(separator=" ", strip=True)
        if element.name in ["h1", "h2", "h3", "h4"]:
            normalized_heading = re.sub(r"\s+", " ", text).strip().upper()
            if normalized_heading in _PMC_TERMINAL_HEADINGS:
                break
            if text:
                pending_headings.append(text)
            continue

        upper_text = text.lstrip().upper()
        if len(text) <= 30 or upper_text.startswith(_PMC_BOILERPLATE_PREFIXES):
            continue

        parts.extend(pending_headings)
        pending_headings.clear()
        parts.append(text)

    if not parts:
        return None

    return "\n\n".join(dict.fromkeys(parts))


def _classify_pmc_html_content(content: Optional[str]) -> Optional[FullTextResult]:
    """Classify extracted HTML without inflating headings-only fragments."""
    if content and len(content) > 3000:
        return FullTextResult(
            content=content,
            available=True,
            extraction_method="html",
            is_complete=True,
        )
    if content and len(content) > 500:
        return FullTextResult(
            content=content,
            available=True,
            extraction_method="html_abstract_only",
            is_complete=False,
        )
    return None


def fetch_pmc_html_fallback(pmcid: str) -> FullTextResult:
    """Scrape PMC HTML when XML access is publisher-restricted."""
    try:
        if not pmcid.startswith("PMC"):
            pmcid = f"PMC{pmcid}"

        url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ai-gene-review/1.0; +https://github.com/monarch-initiative/ai-gene-review)"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        content = _extract_pmc_article_text(response.content)
        result = _classify_pmc_html_content(content)
        if result:
            return result

        if content:
            print(
                f"{pmcid}: HTML content too short ({len(content)} chars), trying PDF fallback..."
            )
        else:
            print(f"{pmcid}: No substantial content found in HTML, trying PDF fallback...")
        return fetch_pmc_pdf_fallback(pmcid)

    except requests.RequestException as e:
        print(f"{pmcid}: HTTP request failed - {e}")
        return FullTextResult(
            content=None, available=False, extraction_method=None, is_complete=False
        )
    except Exception as e:
        print(f"{pmcid}: HTML scraping error - {e}")
        return FullTextResult(
            content=None, available=False, extraction_method=None, is_complete=False
        )


def fetch_pmc_pdf_fallback(pmcid: str) -> FullTextResult:
    """Final fallback method to extract text from PMC PDF when HTML is insufficient.

    This method attempts PDF extraction when HTML scraping yields minimal content
    (e.g., just abstracts repeated). Currently limited by PMC's download
    interstitial pages and authentication requirements for PDF access.

    Uses PyMuPDF as primary extraction method with PyPDF2 as fallback for
    maximum compatibility with different PDF formats.

    Args:
        pmcid: PMC ID (with or without PMC prefix)

    Returns:
        FullTextResult object with content from PDF extraction.
        Success rate currently limited by PMC's PDF access restrictions.
    """
    try:
        # Ensure PMC prefix
        if not pmcid.startswith("PMC"):
            pmcid = f"PMC{pmcid}"

        # First, get the PMC page to find the PDF URL
        page_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ai-gene-review/1.0; +https://github.com/monarch-initiative/ai-gene-review)"
        }

        response = requests.get(page_url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Look for PDF download link
        pdf_links = []

        # Method 1: Look for "PDF" link
        for link in soup.find_all("a", href=True):
            if isinstance(link, Tag):
                href = link.get("href")
                if href and isinstance(href, str) and "pdf" in href.lower():
                    pdf_links.append(href)
                elif "PDF" in link.get_text():
                    link_href = link.get("href")
                    if link_href and isinstance(link_href, str):
                        pdf_links.append(link_href)

        # Method 2: Look for typical PMC PDF patterns
        for link in soup.find_all("a", href=True):
            if isinstance(link, Tag):
                href = link.get("href")
                if (
                    href
                    and isinstance(href, str)
                    and ("/pdf/" in href or href.endswith(".pdf"))
                ):
                    pdf_links.append(href)

        if not pdf_links:
            print(f"{pmcid}: No PDF download link found")
            return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)

        # Use the first PDF link found
        pdf_url = pdf_links[0]

        # Make URL absolute if needed
        if isinstance(pdf_url, str):
            if pdf_url.startswith("/"):
                pdf_url = f"https://pmc.ncbi.nlm.nih.gov{pdf_url}"
            elif not pdf_url.startswith("http"):
                pdf_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/{pdf_url}"

        print(f"{pmcid}: Downloading PDF from {pdf_url}")

        # Download the PDF
        if not isinstance(pdf_url, str):
            return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)

        pdf_response = requests.get(pdf_url, headers=headers, timeout=60)
        pdf_response.raise_for_status()

        # Extract text from PDF - try PyMuPDF first, then PyPDF2 as fallback
        text_parts = []

        try:
            # Method 1: PyMuPDF (more robust)
            doc = fitz.open(stream=pdf_response.content, filetype="pdf")
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                if text.strip():
                    # Clean up the text a bit
                    text = text.replace("\n", " ").replace("\r", " ")
                    # Remove excessive whitespace
                    text = " ".join(text.split())
                    if len(text) > 50:  # Only add substantial text
                        text_parts.append(text)
            doc.close()
            print(f"{pmcid}: Extracted text using PyMuPDF")

        except Exception as mupdf_error:
            print(f"{pmcid}: PyMuPDF failed ({mupdf_error}), trying PyPDF2...")

            # Method 2: PyPDF2 fallback
            try:
                pdf_reader = PdfReader(io.BytesIO(pdf_response.content))
                for page_num, page in enumerate(pdf_reader.pages):
                    try:
                        text = page.extract_text()
                        if text.strip():
                            # Clean up the text a bit
                            text = text.replace("\n", " ").replace("\r", " ")
                            # Remove excessive whitespace
                            text = " ".join(text.split())
                            if len(text) > 50:  # Only add substantial text
                                text_parts.append(text)
                    except Exception as e:
                        print(
                            f"{pmcid}: Error extracting text from page {page_num}: {e}"
                        )
                        continue
                print(f"{pmcid}: Extracted text using PyPDF2 fallback")

            except Exception as pypdf2_error:
                print(
                    f"{pmcid}: Both PDF extraction methods failed - PyMuPDF: {mupdf_error}, PyPDF2: {pypdf2_error}"
                )
                return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)

        if text_parts:
            full_text = "\n\n".join(text_parts)
            print(f"{pmcid}: Extracted {len(full_text)} characters from PDF")
            # Check if we got substantial content
            is_complete = len(full_text) > 3000
            return FullTextResult(
                content=full_text,
                available=True,
                extraction_method="pdf" if is_complete else "pdf_partial",
                is_complete=is_complete
            )
        else:
            print(f"{pmcid}: No text extracted from PDF")
            return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)

    except requests.RequestException as e:
        print(f"{pmcid}: HTTP request failed - {e}")
        return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)
    except Exception as e:
        print(f"{pmcid}: PDF extraction error - {e}")
        return FullTextResult(content=None, available=False, extraction_method=None, is_complete=False)


def cache_publication(
    pmid: str, output_dir: Path = Path("publications"), force: bool = False
) -> bool:
    """Cache a single publication to the filesystem.

    Args:
        pmid: PubMed ID (with or without PMID prefix)
        output_dir: Directory to save cached publication
        force: Force re-download even if already cached

    Returns:
        True if successfully cached, False otherwise

    Example:
        >>> # This would require network access
        >>> # success = cache_publication("PMID:29727692", Path("test_publications"))
        >>> # if success:
        >>> #     assert (Path("test_publications") / "PMID_29727692.md").exists()
    """
    # Clean PMID
    pmid = extract_pmid(pmid)

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check if already cached
    output_file = output_dir / f"PMID_{pmid}.md"
    if output_file.exists() and not force:
        print(f"PMID {pmid} already cached (use force=True to re-download)")
        return True

    # Fetch publication data
    print(f"Fetching PMID {pmid}...")
    publication = fetch_pubmed_data(pmid)

    if not publication:
        print(f"Failed to fetch PMID {pmid}")
        return False

    # A forced re-fetch must not destroy good cached full text when the new fetch is
    # rejected -- `force=True` is what the validator's error message recommends. But
    # skipping the whole write was the wrong remedy: it keyed on the *presence* of a
    # `## Full Text` section rather than on whether that text is good, and 888 cached
    # records are `full_text_available: false` while carrying one. For every one of those,
    # a forced re-fetch wrote nothing at all -- not the body, and not a refreshed title,
    # authors, journal, year, pmcid, doi or abstract -- while returning True. That is the
    # `full_text_attempted` trap with a different key.
    #
    # Gate on the existing record's own verdict instead, and carry its body forward rather
    # than declining to write.
    if output_file.exists() and not publication.full_text_available:
        kept_text, kept_method, kept_provenance = _existing_accepted_full_text(
            output_file
        )
        if kept_text:
            print(
                f"PMID {pmid}: re-fetch returned no usable full text; keeping the "
                f"cached body and refreshing the metadata"
            )
            publication.full_text = kept_text
            publication.full_text_available = True
            publication.full_text_extraction_method = kept_method
            # Keep the body's provenance with the body. `license` governs redistribution
            # of the very text being preserved, and the previous skip-the-write behaviour
            # kept it by accident.
            publication.extra_frontmatter = kept_provenance

    # Write to file
    output_file.write_text(publication.to_markdown())
    clear_publication_caches()

    if publication.full_text_available and publication.full_text:
        print(f"Cached PMID {pmid} with full text from PMC")
    elif publication.pmcid:
        print(
            f"Cached PMID {pmid} with abstract only (full text not available from PMC)"
        )
    else:
        print(f"Cached PMID {pmid} with abstract only (no PMC record)")

    return True


def cache_publications(
    pmids: List[str],
    output_dir: Path = Path("publications"),
    force: bool = False,
    delay: float = 0.5,
) -> int:
    """Cache multiple publications.

    Args:
        pmids: List of PubMed IDs
        output_dir: Directory to save cached publications
        force: Force re-download even if already cached
        delay: Delay between requests in seconds (be polite to NCBI)

    Returns:
        Number of successfully cached publications

    Example:
        >>> # This would require network access
        >>> # count = cache_publications(["29727692", "29727693"])
        >>> # assert count >= 0
    """
    success_count = 0

    for i, pmid in enumerate(pmids):
        if i > 0:
            time.sleep(delay)  # Be polite to NCBI servers

        if cache_publication(pmid, output_dir, force):
            success_count += 1

    print(f"Cached {success_count}/{len(pmids)} publications")
    return success_count


def extract_pmids_from_yaml(yaml_file: Path) -> List[str]:
    """Extract PMIDs from a gene review YAML file.

    Args:
        yaml_file: Path to gene review YAML file

    Returns:
        List of PMIDs found in the file

    Example:
        >>> import tempfile
        >>> data = {
        ...     "references": [
        ...         {"id": "PMID:12345"},
        ...         {"id": "PMID:67890"}
        ...     ],
        ...     "existing_annotations": [
        ...         {"original_reference_id": "PMID:11111"}
        ...     ]
        ... }
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        ...     yaml.dump(data, f)
        ...     temp_file = Path(f.name)
        >>> pmids = extract_pmids_from_yaml(temp_file)
        >>> sorted(pmids)
        ['11111', '12345', '67890']
        >>> temp_file.unlink()
    """
    pmids = set()

    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    if not data:
        return []

    # Extract from references
    if "references" in data and data["references"]:
        for ref in data["references"]:
            if isinstance(ref, dict) and "id" in ref:
                ref_id = ref["id"]
                if ref_id and ref_id.startswith("PMID"):
                    pmids.add(extract_pmid(ref_id))

    # Extract from existing_annotations
    if "existing_annotations" in data and data["existing_annotations"]:
        for annotation in data["existing_annotations"]:
            if isinstance(annotation, dict) and "original_reference_id" in annotation:
                ref_id = annotation["original_reference_id"]
                if ref_id and ref_id.startswith("PMID"):
                    pmids.add(extract_pmid(ref_id))

    return list(pmids)
