# DYSF source audit

This analysis reconstructs the PAINT path and sequence, interaction-record joins, reference-sequence checksums and selected original supplementary-table rows underlying the DYSF review. It does not assign annotation actions or infer biological function from a match count.

Run from this directory:

```sh
just replay
```

Or run the two commands directly:

```sh
uv run --frozen python replay.py --check results.json
uv run --frozen python replay.py --accession Q6DN12 --paint-only --check comparison-MCTP2.json
```

Python 3.10 or later and `xlrd==2.0.2` are required; `uv.lock` fixes the dependency. The replay reads saved inputs and makes no network requests. Initial dependency installation may require access to PyPI. `just regenerate` writes the generated outputs. The `--input-dir`, `--accession`, `--paint-only`, `--output` and `--check` options permit reuse without editing the script.

Each file in `inputs/` is a lossless gzip encoding of an authenticated source response. `sources.json` records the original and compressed SHA-256 hashes, byte counts, exact source URL, and available acquisition metadata. Decompression must reproduce the original bytes. The whole IBD snapshot was reused from an earlier genuine normal download; no new acquisition date is claimed. The publication supplement is the genuine Europe PMC archive, not an article-body excerpt. No whole article is republished here.

The script:

1. Verifies every compressed and decompressed input, then reads the complete saved QuickGO page.
2. Traverses the PANTHER tree to the exact accession, removes alignment gaps and compares the sequence with UniProt. It joins each imported IBA node/term to literal IBD rows and reports the complete target path. It also exposes the differing UniProt and PANTHER geneinfo family pointers.
3. Joins the target's binding annotations to IntAct using both publication and partner accession. It preserves bait/prey roles, taxon, detection method, construct-feature strings and record identifiers. Sequence checks reconstruct each available ROGID from the saved reference sequence and taxon. A matching reference ROGID does not authenticate the entire experimental insert.
4. Opens the original PMID:23414517 supplement archive and selects target/partner rows using the actual workbook columns. It preserves the source's filename/worksheet-name mismatch and one-based Excel row numbers. Bait information is selected by the official gene symbol.

The input QuickGO page is DYSF-specific. The MCTP2 run tests the reusable tree/sequence component on a second input; its zero source-annotation count is not an assertion that MCTP2 has no GO annotations. Empty IntAct joins likewise mean that this saved query returned no matching records, not that an association is absent.

`results.json` and `comparison-MCTP2.json` are machine output. `RESULTS.md` supplies the biological interpretation and independent partner-class source links. Neither the script nor its outputs establishes native binding geometry, a unique natural isoform, or activity of an interacting partner by DYSF.
