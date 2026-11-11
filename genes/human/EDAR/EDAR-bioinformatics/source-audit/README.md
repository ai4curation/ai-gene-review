# EDAR saved-source replay

This analysis extracts primary assay measurements and database provenance. It makes no annotation decisions and performs no network requests. Inputs contain supplementary data and database records, not article full text.

Requirements: Python 3.9+ and openpyxl 3.1.5. With `uv` installed, run from this directory:

```sh
tar -xzf inputs.tar.gz
uv run --with openpyxl==3.1.5 python replay.py --input-map inputs/input-map.json --output replayed-results.json
```

Alternatively install the stated dependency in an isolated environment and invoke the same Python script. `--input-map` may point to a JSON map of the source keys to other saved paths. Relative paths are resolved against that map's directory. Every complete input hash is checked against `source-manifest.json`; changed bytes cause failure. Source URLs identify the original access routes, but updated remote versions are not silently substituted.

The script recomputes EDAR incident rows and control-normalized ECIA measurements, compares library sequences with official sequences, verifies deposited reference ROGIDs, rebuilds the full PAINT target path and literal family IBDs, selects actual donor annotations and matching ARBA conditions, and traverses Reactome components to the EDAR entity. It includes all four EDAR screen rows, not a hand-selected positive subset, and checks the separate SPR workbook for EDAR records.

`results.json` is the executed saved-input result. [RESULTS.md](RESULTS.md) explains its scope and separates independent biological partner classification from calculated facts. IntAct checksum identity is not proof of every experimental tag, truncation or construct coordinate. Database records and source fields are preserved as data; the current classification decisions remain in the gene review.


The bundled archive contains the 21 exact supplementary and database inputs needed for offline replay;
it does not contain article bodies. The source guide links separately inspected primary text and explains
its access limits. The source manifest binds input identities and hashes. A future source update requires
an explicit manifest update and re-execution; replacing bytes silently is rejected.

Input checks raise explicit `ValueError` exceptions and remain active with `python -O`. The formatted
script retains the original extraction logic. Normal and optimized executions produced byte-identical
results to the committed `results.json`; a deliberately altered input failed its hash check. The archive,
manifest, results and interpretation are unchanged by this readability and integrity-check update.
