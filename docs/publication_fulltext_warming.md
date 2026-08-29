# Publication full-text warming (LRV provider chain)

`just warm-publications [limit]` upgrades abstract-only records in the
`publications/` cache to full text by driving the
**linkml-reference-validator (LRV ≥ 0.2.1) full-text provider chain**:

1. **pmc** — PMC XML, then PMC HTML (resolves a PMC id from the PMID when the
   cache has none)
2. **epmc_preprint** — Europe PMC preprint body text (fulltextRepo PDF route)
3. **unpaywall** — open-access PDF/HTML located by DOI
4. **openalex** — open-access location located by DOI

This complements the older `just refresh-publications`, which only retried
records that already had a PMC id. The warm sweep also covers **DOI-only
records** (roughly two-thirds of the backlog), which previously were never
retried at all.

## Tagging convention (adopted from monarch-initiative/dismech)

The sweep follows the `warm-reference-cache` workflow from the
[dismech](https://github.com/monarch-initiative/dismech) repo, which drives the
same LRV code path over its `references_cache/`. The key idea is **durable
attempt tagging** in the cache frontmatter:

- **Success** — the record gets `full_text_available: true` plus provenance:
  `full_text_provider`, `full_text_extraction_method` (`xml`/`html`/`pdf`/`text`),
  `oa_status`, `license`, `full_text_url`, and `full_text_attempted: true`.
  The retrieved text is written as the `## Full Text` section.
- **Clean miss** — the chain ran to completion and found no usable open text:
  the record is tagged `full_text_attempted: true` and is **never re-queried**
  by later sweeps.
- **Transient error** — a provider or download raised: the record is left
  untouched so the next sweep retries it.

Because attempts are durable, `just warm-publications 200` run repeatedly
drains the backlog incrementally, is idempotent, and is safe to interrupt —
exactly dismech's resumable bounded-sweep model.

## Access policy

Only locations LRV classifies as public (`access_type` absent or `"open"`) are
merged into the shared cache, mirroring LRV's own rule that private-library
full text (e.g. Zotero) never enters a committed cache. PDFs are not stored;
only extracted text is kept.

## Commands

```bash
just warm-publications-preview 20   # non-network preview of next candidates
just warm-publications 200          # attempt the next 200 un-attempted records
ai-gene-review warm-publications --limit 50 --providers unpaywall,openalex
```

Records that still fail can be handled via manual PMC overrides — see
[pmc_overrides.md](pmc_overrides.md).
