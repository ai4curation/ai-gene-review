"""PaperBlast API wrapper.

PaperBlast (https://papers.genomics.lbl.gov/) finds papers about a protein or its homologs
using text mining and sequence similarity.

This module provides programmatic access to PaperBlast results, handling the Cloudflare
protection on the website using a headless browser.
"""

import logging
from dataclasses import dataclass
from typing import Optional

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

logger = logging.getLogger(__name__)


@dataclass
class PaperBlastResult:
    """A single result from PaperBlast."""

    title: str
    """Title of the paper or snippet."""

    snippet: Optional[str] = None
    """Text snippet showing relevance."""

    pmid: Optional[str] = None
    """PubMed ID if available."""

    score: Optional[float] = None
    """Relevance score if available."""

    link: Optional[str] = None
    """URL to the paper or source."""


class PaperBlastClient:
    """Client for querying PaperBlast.

    Examples:
        >>> client = PaperBlastClient()
        >>> results = client.search_uniprot("C5B1I4")  # doctest: +SKIP
        >>> for result in results:  # doctest: +SKIP
        ...     print(f"{result.title}: {result.score}")
    """

    BASE_URL = "https://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi"

    def __init__(self, timeout: int = 30000):
        """Initialize the PaperBlast client.

        Args:
            timeout: Timeout in milliseconds for page loads (default: 30000)
        """
        self.timeout = timeout

    def search_uniprot(self, uniprot_id: str) -> list[PaperBlastResult]:
        """Search PaperBlast for papers about a protein by UniProt ID.

        Args:
            uniprot_id: UniProt accession (e.g., "C5B1I4")

        Returns:
            List of PaperBlastResult objects

        Raises:
            ValueError: If the query fails or times out
        """
        url = f"{self.BASE_URL}?query={uniprot_id}&Search=Search"
        return self._fetch_results(url)

    def search_sequence(self, sequence: str) -> list[PaperBlastResult]:
        """Search PaperBlast for papers about a protein by amino acid sequence.

        Args:
            sequence: Amino acid sequence

        Returns:
            List of PaperBlastResult objects

        Raises:
            ValueError: If the query fails or times out
        """
        url = f"{self.BASE_URL}?query={sequence}&Search=Search"
        return self._fetch_results(url)

    def _fetch_results(self, url: str) -> list[PaperBlastResult]:
        """Fetch and parse PaperBlast results using a headless browser.

        Args:
            url: Full URL to fetch

        Returns:
            List of PaperBlastResult objects

        Raises:
            ValueError: If the page fails to load or parsing fails
        """
        logger.info(f"Fetching PaperBlast results from: {url}")

        try:
            with sync_playwright() as p:
                # Launch browser in headless mode
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    # Set a realistic user agent to avoid bot detection
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
                page = context.new_page()

                # Navigate to the URL
                page.goto(url, timeout=self.timeout, wait_until="networkidle")

                # Wait for results to load - look for common result elements
                # Adjust selector based on actual PaperBlast HTML structure
                try:
                    page.wait_for_selector("table, .result, #results", timeout=self.timeout)
                except PlaywrightTimeoutError:
                    logger.warning("Results container not found, proceeding with page content")

                # Get page content
                content = page.content()

                # Close browser
                browser.close()

                # Parse results from HTML
                results = self._parse_html(content)
                logger.info(f"Found {len(results)} results")
                return results

        except PlaywrightTimeoutError as e:
            raise ValueError(f"Timeout loading PaperBlast page: {e}")
        except Exception as e:
            raise ValueError(f"Error fetching PaperBlast results: {e}")

    def _parse_html(self, html: str) -> list[PaperBlastResult]:
        """Parse PaperBlast results from HTML.

        Args:
            html: HTML content from PaperBlast

        Returns:
            List of PaperBlastResult objects

        Note:
            PaperBlast results are in <ul> tags nested under <p> tags.
            Each paper is an <li> with a link to the article and text snippets.
        """
        import re

        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        results = []

        # PaperBlast results are structured as:
        # <p> (protein hit info)
        #   <ul>
        #     <li> (paper link and snippet)
        # We want to extract the papers from the <li> elements

        # Find all list items that contain paper links
        for li in soup.find_all("li"):
            # Look for links to PMC or PubMed
            paper_link = None
            for a in li.find_all("a", href=True):  # type: ignore[union-attr]
                href = a.get("href", "")  # type: ignore[union-attr]
                if "ncbi.nlm.nih.gov/pmc/articles" in href or "pubmed" in href.lower():
                    paper_link = a
                    break

            if not paper_link:
                continue

            # Extract title from the link text
            title = paper_link.get_text(strip=True)
            if not title or len(title) < 5:
                continue

            # Extract PMID/PMCID from URL
            pmid = None
            href = paper_link.get("href", "")  # type: ignore[union-attr]

            # Try to extract PMC ID
            pmc_match = re.search(r"PMC(\d+)", href)
            if pmc_match:
                pmc_match.group(1)

            # Try to extract PMID from URL or text
            pmid_match = re.search(r"pubmed/(\d{7,})", href)
            if pmid_match:
                pmid = pmid_match.group(1)
            else:
                # Look for PMID in surrounding text
                li_text = li.get_text()
                pmid_text_match = re.search(r"PMID[:\s]*(\d{7,})", li_text)
                if pmid_text_match:
                    pmid = pmid_text_match.group(1)

            # Extract snippet - usually in a nested <li> or after the link
            snippet = None
            # Look for text in quotes (common pattern in PaperBlast)
            quote_match = re.search(r'"([^"]{20,})"', li.get_text())
            if quote_match:
                snippet = quote_match.group(1).strip()
            else:
                # Get all text from li, excluding the title
                full_text = li.get_text(strip=True)
                if full_text and len(full_text) > len(title) + 20:
                    # Take text after title as snippet
                    snippet = full_text[len(title) :].strip()
                    # Limit snippet length
                    if len(snippet) > 500:
                        snippet = snippet[:497] + "..."

            # Extract author/journal info from <small> tag
            small_tag = li.find("small")  # type: ignore[union-attr]
            if small_tag:
                citation_info = small_tag.get_text(strip=True)  # type: ignore[union-attr]
                # Append to snippet if we have one
                if snippet:
                    snippet = f"{citation_info} | {snippet}"
                else:
                    snippet = citation_info

            result = PaperBlastResult(
                title=title, snippet=snippet, pmid=pmid, link=href if href.startswith("http") else None
            )

            results.append(result)

        logger.info(f"Parsed {len(results)} paper results from HTML")
        return results


def fetch_paperblast_results(
    query: str, query_type: str = "uniprot", timeout: int = 30000
) -> list[PaperBlastResult]:
    """Fetch PaperBlast results for a protein query.

    Args:
        query: UniProt ID or amino acid sequence
        query_type: Type of query - "uniprot" or "sequence" (default: "uniprot")
        timeout: Timeout in milliseconds (default: 30000)

    Returns:
        List of PaperBlastResult objects

    Examples:
        >>> results = fetch_paperblast_results("C5B1I4")  # doctest: +SKIP
        >>> results = fetch_paperblast_results("MSKGEELFT...", query_type="sequence")  # doctest: +SKIP
    """
    client = PaperBlastClient(timeout=timeout)

    if query_type == "uniprot":
        return client.search_uniprot(query)
    elif query_type == "sequence":
        return client.search_sequence(query)
    else:
        raise ValueError(f"Invalid query_type: {query_type}. Must be 'uniprot' or 'sequence'")
