# ELOVL4 reproducible database evidence

Run from this directory with Python 3.10 or later:

```sh
PYTHONDONTWRITEBYTECODE=1 python reproduce.py
```

Only the Python standard library is required. The visible `reproduce.py`, `derive_paint.py` and `derive_database.py` contain the complete analysis code. `RESULTS.md` explains the findings and limits. `expected-results.json` records hashes of the previously reviewed full projections and their compact summary; these are comparison targets, not substitutes for computation.

`input-evidence.tar.gz` contains 72 fixed input files: official records, raw interaction data, complete PAINT tree/MSA/IBD inputs, typed ontology responses, genuine source TSVs, source objects and their provenance receipts. It contains no executable code, article body, normal publication cache or provider log. `input-manifest.json` identifies every member by size and SHA256. The program authenticates those bytes, rejects unsafe or extra archive entries, extracts into a temporary directory and independently reconstructs the results.

The checks cover every historical/current context against the 37 retained source dictionaries, the exact current TSV projection, all imported HuRI partners, current rule conditions, complete target-path IBD/loss records and the 314-residue target MSA. They also derive the two lateral term relationships from explicit is_a paths. Article interpretation is documented in the adjacent source guide with access limits and locators; it is not represented as an automated result.

The database snapshot is fixed evidence from this review, not a live query. Re-running does not contact APIs, change the review, run its ordinary validators or install dependencies. An input mismatch is an error rather than permission to silently adopt a newer source. The original private projections additionally index publication text; that article-extraction component is deliberately omitted from the public database module.
