"""Minimal Europe PMC search client for litscan jobs."""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Any

import requests

EUROPE_PMC_SEARCH_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


@dataclass
class Publication:
    """A normalized Europe PMC record."""

    pmid: str
    doi: str
    title: str
    journal: str
    publication_date: str
    authors: str
    abstract: str
    source: str
    record_id: str

    @property
    def europe_pmc_url(self) -> str:
        return f"https://europepmc.org/article/{self.source}/{self.record_id}"

    @property
    def pubmed_url(self) -> str:
        return f"https://pubmed.ncbi.nlm.nih.gov/{self.pmid}/" if self.pmid else ""

    @property
    def reference_id(self) -> str:
        """Canonical ``PMID:`` (preferred) or ``DOI:`` reference id, else ''."""
        if self.pmid:
            return f"PMID:{self.pmid}"
        if self.doi:
            return f"DOI:{self.doi.lower()}"
        return ""


def normalize_text(value: Any) -> str:
    """Strip HTML/markup and collapse whitespace.

    >>> normalize_text("Foo &lt;i&gt;bar&lt;/i&gt;   baz")
    'Foo bar baz'
    >>> normalize_text(None)
    ''
    """
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def publication_from_record(record: dict[str, Any]) -> Publication:
    source = normalize_text(record.get("source"))
    record_id = normalize_text(record.get("id"))
    pmid = normalize_text(record.get("pmid"))
    if not pmid and source == "MED" and re.fullmatch(r"\d+", record_id):
        pmid = record_id
    journal = record.get("journalTitle")
    if not journal:
        journal_info = record.get("journalInfo")
        if isinstance(journal_info, dict) and isinstance(
            journal_info.get("journal"), dict
        ):
            journal = journal_info["journal"].get("title")
    return Publication(
        pmid=pmid,
        doi=normalize_text(record.get("doi")),
        title=normalize_text(record.get("title")),
        journal=normalize_text(journal),
        publication_date=normalize_text(record.get("firstPublicationDate")),
        authors=normalize_text(record.get("authorString")),
        abstract=normalize_text(record.get("abstractText")),
        source=source,
        record_id=record_id,
    )


def search(
    query: str,
    *,
    max_records: int = 100,
    page_size: int = 100,
    timeout: float = 30.0,
    sort: str = "P_PDATE_D desc",
) -> tuple[int, list[Publication]]:
    """Run a Europe PMC search, returning ``(hit_count, publications)``.

    ``sort`` defaults to newest-first. Records are de-duplicated by PMID (or
    source:id when no PMID is present).
    """
    publications: list[Publication] = []
    seen: set[str] = set()
    hit_count = 0
    page = 1
    while len(publications) < max_records:
        current_page_size = min(page_size, max_records - len(publications))
        response = requests.get(
            EUROPE_PMC_SEARCH_URL,
            params={
                "query": query,
                "format": "json",
                "pageSize": str(current_page_size),
                "page": str(page),
                "resultType": "core",
                "sort": sort,
            },
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
        if page == 1:
            hit_count = int(payload.get("hitCount") or 0)
        page_records = payload.get("resultList", {}).get("result", [])
        if not page_records:
            break
        for record in page_records:
            pub = publication_from_record(record)
            key = pub.pmid or f"{pub.source}:{pub.record_id}"
            if key in seen:
                continue
            seen.add(key)
            publications.append(pub)
        if len(page_records) < current_page_size:
            break
        page += 1
    return hit_count, publications
