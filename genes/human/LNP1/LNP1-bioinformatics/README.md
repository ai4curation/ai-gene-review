# LNP1 interaction and localization provenance audit

This standard-library Python workflow resolves identifiers and distinguishes
binary physical evidence from AP-MS/co-complex/predicted evidence for human
LNP1 (`A1A4G5`). It explicitly checks the historical collision with lunapark
`LNPK` (`Q9C0E8`) and preserves BioPlex prey isoforms.

Run from this directory with Python 3.9 or newer (tested with Python 3.9.5):

```bash
just run
```

No third-party Python packages are required. Inputs and URLs are declared in
`config.json`; output is written to `results/`. The official BioPlex no-filter
files are roughly 1 GB each, so the workflow uses HTTP byte ranges pinned to the
contiguous LNP1 bait blocks in the dated December 2019 releases. It saves those
source ranges and the server ETag/content-range in `source_manifest.tsv`, and
fails if the expected accessions are no longer recovered.

The large Nature HuRI, Elsevier XL-MS, and Europe PMC phosphoproteome supplement
archives are processed in memory. Only the exact source rows needed for this
audit are retained. HPA, IntAct, BioGRID, hu.MAP3, and Complex Portal responses
are retained under `results/raw/`.

For repository hygiene, saved text snapshots use LF line endings, space-only
indentation, and no trailing horizontal whitespace. `source_manifest.tsv`
records the byte count, SHA-256 digest, and HTTP metadata of each original
fetched response, so the normalization does not obscure source integrity.
