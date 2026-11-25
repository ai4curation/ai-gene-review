# Reproduce the EIF2B4 source joins

Run with Python 3.10 or later; the script uses only the standard library:

```sh
python reproduce.py --output replay.json --check records.json
python -O reproduce.py --output replay-optimized.json --check records.json
```

The script verifies the archive SHA256 and every member hash before reading any input. It reconstructs the literal interaction joins, reference-sequence ROGIDs, partner sequence comparisons, PAINT target path and IBD joins, rat donor references, ARBA conditions and Reactome component chain. It compares the complete result when `--check` is supplied. A changed input raises an explicit error, including under optimized Python.

`source-inputs.zip` contains 41 saved database/source files, approximately 2 MB compressed. It includes the complete 159-record IntAct response, full family tree/MSA and IBD snapshot, complete rat query, official sequence/term/rule/entity records, three official product FASTAs, and both raw GOA versions. It contains no recovered article bodies. `source-manifest.json` gives source URLs, retrieval metadata where available, sizes and hashes. Reused inputs are identified as reused; no new retrieval is claimed.

For independently saved inputs, put the exact manifest filenames in one directory and use:

```sh
python reproduce.py --saved-dir /path/to/saved-inputs --output replay.json --check records.json
```

All listed inputs are required. The script does not download current database releases, infer missing records or silently substitute changed files. The source snapshots are version-specific; current web resources can legitimately differ.

`original-locators.json` records publication cache hashes, original URLs and the actual inspected section/window scope. It is a provenance index, not copied article text or an independent experiment. Biological interpretations remain in the review and [source guide](../EIF2B4-source-guide.md); the script produces identities and joins, not annotation decisions.
