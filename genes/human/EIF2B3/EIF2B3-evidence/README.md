# Reproducing EIF2B3 source projections

`reproduce.py` is a Python 3 standard-library program. It parses 16 saved official inputs and reconstructs the target's ancestral path, aligned sequence, literal PAINT records, ARBA condition matches, selected donor annotations, Reactome entity chains and HPA location summary. It does not make biological decisions or retrieve article bodies.

`inputs.json` lists original source URLs, input filenames, byte lengths and SHA-256 hashes. Put those exact responses in a directory, then run:

```sh
python3 reproduce.py --input-dir /path/to/saved-inputs --output reproduced.json
```

Compare the result with `source-projections.json`. The complete PAINT IBD file is required; the selected output rows alone are not used to infer absence of a loss along the path. The source snapshots are intentionally not bundled here, and current downloads may differ from the saved hashes. A newer snapshot should be reviewed separately instead of bypassing the hash checks.

The replay was run with normal and optimized Python, producing identical output. Inputs were supplied through a separate directory, and a changed UniProt input was rejected before output creation. All logical input checks remain active under optimization. The script uses no YAML or third-party parsing packages.

`original-locators.json` records the normal publication-cache hashes and the precise independently assessed original sections. These locators document access; they do not claim that an abstract-only cache contains the separately recovered original. `RESULTS.md` explains the biological interpretation and its limits. The review's zero-quotation policy is preserved.
