# EMILIN1 frozen-data replay

Run with Python 3.10 or newer and only its standard library:

```sh
python reproduce.py --output /tmp/emilin1-replay
```

Choose a new output directory. The script verifies every archived input against the visible manifest, reconstructs the data and compares the resulting JSON hashes with `expected-results.json`. It never downloads data, installs dependencies, modifies the review or evaluates biological actions.

The input-only ZIP contains frozen official database exports, source contexts, product FASTAs, complete saved IBD data, interaction datasets and genuine author workbooks/processed identification output. The code, manifest, expected summary and results narrative are visible beside the archive. Running the code writes full `paint.json`, `database.json`, `interactions.json`, `workbooks.json` and `pride-target.json`; the checked-in expected file is a summary and hashes, not those full outputs.

The XLSX reader uses cached cell values without recalculating formulas. Target rows are literal token matches; adjacent cells, mixed protein groups and alternate searches still require the interpretation in the source guide. The 23658023 extraction restricts itself to Protein Reports, separating human and mouse records. The PRIDE check reads an author-deposited identification table, not raw spectra.

Article XML/HTML/PDF, figure images and provider logs are excluded. Original-body interpretation and the independently inspected 27068509 PDF table remain documented in the source guide, rather than falsely represented as publicly replayed article bodies. Retrieval receipts and byte hashes preserve provenance. Source multiplicity is retained; this script verifies the frozen 115/103/99 counts and does not rerun the repository's evolving normalizer.
