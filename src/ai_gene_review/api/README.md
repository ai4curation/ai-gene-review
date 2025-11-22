# API Wrappers

This directory contains Python wrappers for external bioinformatics APIs and services.

## PaperBlast

PaperBlast (https://papers.genomics.lbl.gov/) finds papers about a protein or its homologs using text mining and sequence similarity.

### Features

- Query by UniProt ID or amino acid sequence
- Bypasses Cloudflare protection using headless browser (Playwright)
- Parses results including paper titles, PMIDs, snippets, and links
- Returns structured `PaperBlastResult` objects

### Usage

#### Python API

```python
from ai_gene_review.api.paperblast import fetch_paperblast_results

# Search by UniProt ID
results = fetch_paperblast_results("C5B1I4", query_type="uniprot")

# Search by sequence
results = fetch_paperblast_results("MSKGEELFT...", query_type="sequence")

# Process results
for result in results:
    print(f"Title: {result.title}")
    print(f"PMID: {result.pmid}")
    print(f"Link: {result.link}")
    print(f"Snippet: {result.snippet}")
```

#### Command Line

```bash
# Fetch results for a UniProt ID
uv run python scripts/fetch_paperblast.py C5B1I4

# Fetch results for a sequence
uv run python scripts/fetch_paperblast.py "MSKGEELFT..." --sequence
```

### Requirements

- `playwright` - For headless browser automation
- `beautifulsoup4` - For HTML parsing

The wrapper automatically handles:
- Cloudflare bot protection
- JavaScript rendering
- Result parsing and extraction

### Implementation Notes

**Why headless browser?**

The PaperBlast website is protected by Cloudflare's bot detection, which blocks simple HTTP requests (like `curl` or `requests`). The site requires JavaScript execution to pass the Cloudflare challenge.

Our implementation uses Playwright with Chromium to:
1. Load the page with a realistic user agent
2. Wait for JavaScript to execute
3. Wait for results to load
4. Extract the rendered HTML
5. Parse results using BeautifulSoup

**Alternative approaches considered:**

1. ❌ **Direct HTTP requests** - Blocked by Cloudflare (403 Forbidden)
2. ❌ **Local installation** - Would require downloading large databases
3. ✅ **Headless browser** - Works reliably, minimal setup

### Performance

- First query: ~5-10 seconds (includes browser startup)
- Subsequent queries: ~3-5 seconds
- Timeout: 30 seconds (configurable)

### Future Improvements

- [ ] Add caching to avoid repeated queries
- [ ] Add support for batch queries
- [ ] Extract sequence similarity scores from results
- [ ] Parse protein homolog information
- [ ] Add integration with gene review workflow
