# DNMT1 source-record extraction

This small analysis reproduces the literal DNMT1 records used from the MitoCoP supplementary workbook (PMID:34800366) and OpenCell interaction CSV (PMID:35271311). It selects by gene-name fields, preserves all target-row fields and accession groups, and performs no GO inference. The output is [source-extract.json](source-extract.json); interpretation is in [RESULTS.md](RESULTS.md).

Python 3 with its standard library is sufficient. Supply the original files locally:

```bash
python3 reproduce.py --mitocop /path/to/34800366-mmc2.xlsx --opencell /path/to/OpenCell-protein-interactions.csv --output /tmp/DNMT1-source-extract.json
```

Alternatively download the published original sources without credentials:

```bash
python3 reproduce.py --download /tmp/DNMT1-originals --output /tmp/DNMT1-source-extract.json
```

The MitoCoP download is the complete supplementary archive (about 135 MB); the script extracts its one `mmc2.xlsx` member. Both archive and input checksums are verified. A changed upstream file or an HTML challenge stops extraction rather than silently accepting different evidence. The local-input route is the audited reproduction; network availability is not guaranteed. Use `--gene DNAJC19` or another literal gene to inspect a different selection; results and counts are derived from the data.

[Source manifest](source-manifest.yaml) gives public URLs, fixed hashes and access dates. The published output includes all 413 target workbook cells, their original headers, and one complete OpenCell record. Spreadsheet row numbers are one-based Excel rows. CSV line numbers include the header; zero-based data indices are also recorded. No raw workbook or complete interaction network is duplicated here.
