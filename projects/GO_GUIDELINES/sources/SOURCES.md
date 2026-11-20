---
title: "GO guidelines: source inventory"
maturity: SCOPING
tags: [PIPELINE]
---

# GO guidelines: source inventory

Part of [GO_GUIDELINES](../../GO_GUIDELINES.md). The guidelines are written from the sources this page inventories.

**Bottom line:** every item in four bodies of Gene Ontology material has a
receipt that scores its relevance to GO annotation best practice (1-5) and says
why in a sentence or two. The four bodies are the GO Consortium shared Google
Drive, the GO wiki, papers and books on GO annotation, and the
`geneontology/go-annotation` repository (its issue tracker and its files). There
are about 22,000 receipts in all. Tallies and the full list of items scored 5 are
in [top-sources.md](top-sources.md). The receipts are
meant as a map for finding guidance, not as the guidance itself.

## Receipt files

One YAML per source, in `receipts/` (local only, not in git; `key-sources.yaml` holds every item scored 4 or 5).
Each receipt in a file is an entry with:

- `id`: `drive:<path>`, `wiki:<page title>`, `PMID:`/`DOI:`, `issue:<n>`, or `file:<path>`
- `title`, `url` (a Drive link, wiki URL, Europe PMC or DOI link, or GitHub link)
- `relevance`: 1-5, or `null` with `assessed: false` when the item was not assessed
- `rationale`: what guidance the item holds, or why it holds none
- `method`: `rule:<name>`, `haiku` or `opus` (see below)
- for the drive, wiki and issues: path or categories, last-modified date, labels, and so on

Entries are sorted with the highest scores first.

| File | Scope |
|---|---|
| `go-drive-receipts.yaml` | every file on the GO shared drive (rclone remote `gdrive-go`, listed 2026-11-14) |
| `go-wiki-receipts.yaml` | every non-redirect page in the Main, GO Wiki, Help and Category namespaces of wiki.geneontology.org (5,236 pages, fetched 2026-11-14) |
| `papers-receipts.yaml` | 995 candidate papers and book chapters from Europe PMC (queries below) |
| `go-annotation-issues-receipts.yaml` | every issue and PR the GitHub API returns for geneontology/go-annotation (6,572) |
| `go-annotation-repo-files-receipts.yaml` | every file on `master` of geneontology/go-annotation (2,821) |

## Rubric

5 states or establishes guidance (a guideline, SOP, policy, consortium decision
or annotation-method paper). 4 is a substantial discussion that settles a general
practice. 3 is case work that carries a reusable lesson. 2 is a case-level item,
or one only tangential to annotation practice. 1 is not relevant. The exact text
is in `scripts/rubric.md`.

## How the receipts were made

Each source got a manifest first. Strategies were then chosen per cluster, by
folder, file type, label, title pattern and a probe of the content:

1. **Rules, written once and applied to whole clusters, each with its stated
   rationale.** Examples:
   - Media and raw data files are not assessed (images, video, GAF/GPAD/OBO dumps, archives).
   - PAINT release statistics and per-release QC output score 1.
   - The 1,102 annotation-review spreadsheets (one per obsoletion ticket) score 2.
   - On the wiki: OBO-Edit and AmiGO manuals score 1, as do meeting minutes with
     no guidance vocabulary and pages under 300 characters.
   - In go-annotation: case-level InterPro2GO, PAINT, ARBA and keyword mapping
     tickets score 2 when neither the body nor the comments use guidance language.
     The auto-generated `reports/` TSVs score 1.
2. **First-pass scoring by Haiku subagents** for everything else, from the
   extracted text: issue body plus comments, wiki text, Drive document text and
   paper abstracts, each up to 3,000 characters. Items in guideline-like folders,
   categories or labels were batched separately and given up to 8-10k characters.
3. **Careful second pass by Opus** for every item the first pass scored 5. These
   receipts keep the Haiku verdict under `first_pass`. The second pass kept 5 only
   for items that themselves state the guidance. Minutes that report a decision
   moved down to 4, and drafts, archived pages and pages since superseded are
   labelled as such. About half of the first-pass 5s were downgraded. The
   go-annotation repository's non-report files were read and scored directly.

The scripts (manifest, bucketing, batching and merge) are in
`scripts/`. They were run from a scratch directory, so
the paths inside them are provenance, not a ready-made pipeline.

## Access notes and known limits

- **GO wiki:** wiki.geneontology.org is behind a Cloudflare challenge, so it was
  read through the MediaWiki API from the user's own browser session and
  downloaded as one wikitext dump.
- **Drive:** Google-native files were exported to text or CSV, and Office and PDF
  files were converted with markitdown (first 20k characters). 195 files could not
  be converted: old `.ppt` files, conversions that timed out, and one dangling
  shortcut. They are receipted as `rule:no-text-extracted` with the title only.
  Files that share an exact name in the same folder could be downloaded only once;
  each extra copy has its own receipt that mirrors the scored one
  (`rule:duplicate-filename`).
- **Papers:** papers were scored on title and abstract only. The candidate set
  came from Europe PMC queries:
  - "Gene Ontology", "GO annotation" or "GO-CAM" in the title
  - abstracts on GO annotation together with guidelines, best practice or curators
  - ECO, PAINT, biocuration and annotation-extension papers
  - the Gene Ontology Handbook chapters (Methods Mol Biol 1446)

  Guidance papers that use none of these words in their title or abstract may be
  missing. Books other than the Handbook were not searched.
- **go-annotation issues:** issue numbers run to 6,658. The API returns 6,572
  issues; the rest are deleted or transferred. Haiku scored thread text up to
  3,000 characters, so a decision made late in a long thread can be missed. The
  Opus pass on 5s and the careful batches read up to 9-14k characters.
- **Haiku scores are a triage, not a verdict.** Scores of 4 and below were not
  re-checked by Opus. Treat them as a ranking for where to look.
