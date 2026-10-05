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
records that already had a PMC id. The warm sweep also covers **PMID records
without a PMC id** (roughly two-thirds of the backlog), which previously were
never retried at all — their DOI lets Unpaywall/OpenAlex locate open text.
Note the sweep targets `PMID_*.md` records only; the small number of
`DOI_*.md`-keyed records in the cache are not candidates.

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
exactly dismech's resumable bounded-sweep model. If the provider chain or the
acceptance guards improve, `--retry-attempted` re-targets records a previous
sweep already concluded on.

## Acceptance guards

Length alone does not make text "full text". Before a record is upgraded, the
retrieved text must pass content-quality guards (`is_usable_full_text`):

- **No paywall/stub markers** — publisher subscription previews ("This is a
  preview of subscription content", "Subscribe to this journal") and PMC
  scanned-PDF stub pages ("The Full Text of this article is available as a
  PDF") are boilerplate around an abstract, not body text.
- **Substantially more than the cached abstract** — text that merely re-emits
  the abstract with a keywords line or courtesy footer is rejected.

Rejected text counts as a clean miss: the record is tagged
`full_text_attempted: true` with `full_text_available` left `false`. This
matters because `full_text_available:` is the field gene reviews consult to
decide whether the reviewer can see what a curator saw (see CLAUDE.md).

## Access and licensing policy

Only locations LRV classifies as public (`access_type` absent or `"open"`) are
merged into the shared cache, mirroring LRV's own rule that private-library
full text (e.g. Zotero) never enters a committed cache. **Bronze** OA (free to
read on the publisher's site but with no open license) is additionally
excluded unless the location carries an explicit license, since committing
that text would redistribute it without redistribution rights; any license the
provider reports is persisted in the `license` frontmatter field. PDFs are not
stored; only extracted text is kept.

## Commands

```bash
just warm-publications-preview 20   # non-network preview of next candidates
just warm-publications 200          # attempt the next 200 un-attempted records
ai-gene-review warm-publications --limit 50 --providers unpaywall,openalex
```

Records that still fail can be handled via manual PMC overrides — see
[pmc_overrides.md](pmc_overrides.md).
