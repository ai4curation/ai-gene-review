# DOCK7 primary interaction records

This Python 3.9+ standard-library analysis extracts the original graph/CSV fields supporting the four DOCK7–LRCH assertions from PMID:35271311 and PMID:40205054. It preserves complete accession groups and bait direction. It does not assign experimental isoforms, interpret omitted partners as negatives, or infer a purified direct interface.

The exact upstream snapshots are identified by URL and SHA-256 in `source-manifest.json`. The large primary datasets are not duplicated here. Obtain the files using the executable downloader, or supply previously downloaded files with those exact hashes:

```sh
python fetch_inputs.py --output-dir inputs
python extract.py --inputs-dir inputs --manifest source-manifest.json --selection selection.json --output RESULTS.json --check
```

`fetch_inputs.py` performs real public HTTP requests and refuses changed bytes. A future upstream change is an explicit reproducibility limitation, not permission to substitute a different snapshot. The saved-input extractor was actually replayed against the original datasets. `RESULTS.json` contains all incident records plus the selected source-assertion subset. The selection file names the gene and the two partners; it contains no measurement values.

CSV coordinates distinguish zero-based data-row index (excluding header) and physical line (including header). Graph edge IDs are literal NDEx IDs. These are record locators, not biological ranks.
