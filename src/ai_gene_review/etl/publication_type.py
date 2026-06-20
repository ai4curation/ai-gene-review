"""Infer a reference's :class:`PublicationTypeEnum` value.

For PMIDs we infer the publication type from PubMed's publication-type ("PT")
MEDLINE metadata. For non-literature references (GO_REF, Reactome, ``file:``)
we infer it from the identifier scheme.

The PubMed "PT" field is a list (a single article can be both a
"Journal Article" and a "Review"), so :func:`classify_pubmed_publication_type`
applies a priority order, preferring the most specific secondary-literature type
(meta-analysis > systematic review > review > ...) and only falling back to
``PRIMARY_RESEARCH`` for a plain journal article.

Note: PubMed's review tagging is imperfect (some review articles are only tagged
"Journal Article"), so ``PRIMARY_RESEARCH`` here means "not tagged as a review by
PubMed", not a guarantee of primary status.
"""

from __future__ import annotations

import re
import time
from typing import Dict, List, Optional

# Enum values are referenced as plain strings to avoid importing the heavy
# generated datamodel here; they must stay in sync with PublicationTypeEnum.
_PRIMARY_RESEARCH = "PRIMARY_RESEARCH"
_REVIEW = "REVIEW"
_SYSTEMATIC_REVIEW = "SYSTEMATIC_REVIEW"
_META_ANALYSIS = "META_ANALYSIS"
_COMMENT_EDITORIAL = "COMMENT_EDITORIAL"
_CASE_REPORT = "CASE_REPORT"
_PREPRINT = "PREPRINT"
_DATABASE = "DATABASE"
_BIOINFORMATICS = "BIOINFORMATICS"
_DEEP_RESEARCH = "DEEP_RESEARCH"
_OTHER = "OTHER"
_UNKNOWN = "UNKNOWN"

# Mapping from a normalized (lower-cased) PubMed PT string to our enum value,
# in priority order (most specific / most informative first). The first PT in a
# record that matches one of these wins.
_PT_PRIORITY: List[tuple[str, str]] = [
    ("meta-analysis", _META_ANALYSIS),
    ("systematic review", _SYSTEMATIC_REVIEW),
    ("review", _REVIEW),
    ("preprint", _PREPRINT),
    ("case reports", _CASE_REPORT),
    ("editorial", _COMMENT_EDITORIAL),
    ("comment", _COMMENT_EDITORIAL),
    ("letter", _COMMENT_EDITORIAL),
    ("news", _COMMENT_EDITORIAL),
]


def classify_pubmed_publication_type(pt_list: List[str]) -> str:
    """Classify a PubMed PT list into a PublicationTypeEnum value.

    Args:
        pt_list: List of PubMed publication-type strings (the MEDLINE "PT"
            field), e.g. ``["Journal Article", "Review"]``.

    Returns:
        A :class:`PublicationTypeEnum` value (as a string).

    Examples:
        >>> classify_pubmed_publication_type(["Journal Article"])
        'PRIMARY_RESEARCH'
        >>> classify_pubmed_publication_type(["Journal Article", "Review"])
        'REVIEW'
        >>> classify_pubmed_publication_type(["Review"])
        'REVIEW'
        >>> classify_pubmed_publication_type(["Systematic Review", "Review"])
        'SYSTEMATIC_REVIEW'
        >>> classify_pubmed_publication_type(["Meta-Analysis", "Review"])
        'META_ANALYSIS'
        >>> classify_pubmed_publication_type(["Editorial"])
        'COMMENT_EDITORIAL'
        >>> classify_pubmed_publication_type(["Case Reports", "Journal Article"])
        'CASE_REPORT'
        >>> classify_pubmed_publication_type([])
        'UNKNOWN'
        >>> classify_pubmed_publication_type(["Dataset"])
        'OTHER'
    """
    if not pt_list:
        return _UNKNOWN

    normalized = [pt.strip().lower() for pt in pt_list if pt and pt.strip()]
    if not normalized:
        return _UNKNOWN

    # Most-specific secondary type wins, regardless of order in the record.
    for needle, value in _PT_PRIORITY:
        if any(needle in pt for pt in normalized):
            return value

    if any("journal article" in pt for pt in normalized):
        return _PRIMARY_RESEARCH

    return _OTHER


def classify_reference_id(ref_id: str) -> Optional[str]:
    """Infer a publication type from a non-PMID reference identifier.

    Returns ``None`` for PMID references (which require PubMed metadata to
    classify via :func:`classify_pubmed_publication_type`).

    Args:
        ref_id: A reference identifier, e.g. ``GO_REF:0000043``,
            ``Reactome:R-HSA-123``, ``file:human/TP53/...-deep-research-openai.md``.

    Returns:
        A :class:`PublicationTypeEnum` value, or ``None`` if this is a PMID
        (and so should be classified from PubMed metadata).

    Examples:
        >>> classify_reference_id("PMID:12345") is None
        True
        >>> classify_reference_id("GO_REF:0000043")
        'DATABASE'
        >>> classify_reference_id("Reactome:R-HSA-123")
        'DATABASE'
        >>> classify_reference_id("file:human/TP53/TP53-deep-research-openai.md")
        'DEEP_RESEARCH'
        >>> classify_reference_id("file:human/TP53/TP53-bioinformatics/RESULTS.md")
        'BIOINFORMATICS'
        >>> classify_reference_id("DOI:10.1/x")
        'OTHER'
    """
    rid = ref_id.strip()
    lower = rid.lower()

    if lower.startswith("pmid"):
        return None

    if lower.startswith("file:"):
        if "deep-research" in lower or "deep_research" in lower:
            return _DEEP_RESEARCH
        if "bioinformatic" in lower:
            return _BIOINFORMATICS
        # Other local files (notes, manual analyses) are treated as bioinformatics-
        # style ad-hoc sources rather than formal database records.
        return _BIOINFORMATICS

    if lower.startswith(("go_ref", "goref", "reactome", "uniprot", "rhea", "ec:")):
        return _DATABASE

    return _OTHER


def publication_type_for_reference(
    ref_id: str, pubmed_types: Optional[Dict[str, List[str]]] = None
) -> str:
    """Resolve the publication type for any reference identifier.

    Args:
        ref_id: Reference identifier (PMID, GO_REF, Reactome, file:, ...).
        pubmed_types: Optional mapping of bare PMID (no ``PMID:`` prefix) to its
            PubMed PT list, used to classify PMID references. If a PMID is not
            present in this mapping, ``UNKNOWN`` is returned.

    Returns:
        A :class:`PublicationTypeEnum` value.

    Examples:
        >>> publication_type_for_reference("GO_REF:0000043")
        'DATABASE'
        >>> publication_type_for_reference("PMID:1", {"1": ["Journal Article", "Review"]})
        'REVIEW'
        >>> publication_type_for_reference("PMID:99")
        'UNKNOWN'
    """
    by_id = classify_reference_id(ref_id)
    if by_id is not None:
        return by_id

    # PMID path
    bare = re.sub(r"^(PMID|pmid)[:\s]*", "", ref_id.strip())
    if pubmed_types and bare in pubmed_types:
        return classify_pubmed_publication_type(pubmed_types[bare])
    return _UNKNOWN


def parse_medline_publication_types(medline_text: str) -> Dict[str, List[str]]:
    """Parse PMID -> PT list from a MEDLINE-format efetch text block.

    Args:
        medline_text: Text returned by ``efetch(db="pubmed", rettype="medline",
            retmode="text")`` for one or more records.

    Returns:
        Mapping of bare PMID to its list of PT values.

    Examples:
        >>> txt = "PMID- 1\\nPT  - Journal Article\\nPT  - Review\\n\\nPMID- 2\\nPT  - Editorial\\n"
        >>> parse_medline_publication_types(txt)
        {'1': ['Journal Article', 'Review'], '2': ['Editorial']}
    """
    result: Dict[str, List[str]] = {}
    for block in re.split(r"\n\s*\n", medline_text):
        pmid_match = re.search(r"^PMID-\s*(\d+)", block, re.MULTILINE)
        if not pmid_match:
            continue
        pts = re.findall(r"^PT  - (.+)$", block, re.MULTILINE)
        result[pmid_match.group(1)] = [p.strip() for p in pts]
    return result


def fetch_pubmed_publication_types(
    pmids: List[str], batch_size: int = 200, delay: float = 0.34
) -> Dict[str, List[str]]:
    """Fetch PubMed PT lists for many PMIDs, batched.

    This makes network calls to NCBI Entrez. Bare or ``PMID:``-prefixed IDs are
    both accepted; the returned keys are bare PMIDs.

    Args:
        pmids: PMIDs to look up (bare or prefixed).
        batch_size: Number of PMIDs per efetch call (NCBI allows large batches).
        delay: Seconds to sleep between batches (be polite to NCBI; ~3/sec).

    Returns:
        Mapping of bare PMID to its PT list. PMIDs PubMed does not return are
        simply absent from the mapping.
    """
    from Bio import Entrez  # type: ignore[import-untyped]

    Entrez.email = "ai-gene-review@example.com"  # type: ignore[assignment]

    bare = [re.sub(r"^(PMID|pmid)[:\s]*", "", p.strip()) for p in pmids]
    bare = [p for p in bare if p]
    result: Dict[str, List[str]] = {}

    for i in range(0, len(bare), batch_size):
        if i > 0:
            time.sleep(delay)
        chunk = bare[i : i + batch_size]
        handle = Entrez.efetch(
            db="pubmed", id=",".join(chunk), rettype="medline", retmode="text"
        )
        text = handle.read()
        handle.close()
        result.update(parse_medline_publication_types(text))

    return result
