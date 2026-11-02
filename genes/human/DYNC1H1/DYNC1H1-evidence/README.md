# DYNC1H1 source records and measurements

These files expose the records underlying the DYNC1H1 evidence assessment. They are extracts of the cited sources, not an independent experimental study or a substitute for the source-specific reasoning in [the evidence guide](../DYNC1H1-source-evidence.md).

- `source-manifest.yaml` lists public acquisition URLs, exact raw-file SHA-256 hashes, sizes and formats. It includes the original table and database files, not generated narrative.
- `selection.yaml` identifies the 56 imported partner claims, one OpenCell bait/prey pair, 49 selected Reactome paths and nine inherited PAINT claims. Row numbers are zero-based review positions and are locators only; source identifiers remain the stable keys.
- `interactions.yaml` preserves matching IntAct/MINT identifiers, assay methods, participants, species, expansion status, roles, reference-sequence checksums and separately annotated construct features. Separate database records can describe the same experiment. The pooling, array and validation stages of PMID:32814053 are not three independent publications. A checksum matching a current reference sequence does not authenticate the entire experimental insert.
- `measurements.yaml` contains the HeLa RNA-capture row and whole-cell detection, parotid-vesicle measurement, urinary-vesicle database measurement, OpenCell association and the author-thesis RNA-capture row. It preserves literal accession groups and missing values. The OpenCell field named `pval` is retained as supplied, without treating its value as a raw probability.
- `reactome-paths.yaml` verifies each selected edge against the original API response and identifies the terminal human Q14204 entity. These are curated model placements, not 49 independent localization experiments. The granule-lumen placement does not supply a target-specific assay.
- `phylogeny.yaml` reconstructs the target path and exact reference sequence from the official PTHR10676 tree and alignment, then joins the literal IBD records. The dynein-1 branch's separate IRD records are retained. They do not negate the positive terms reviewed here. Donor count and the target's presence among descendant evidence are not failure tests.

Run the extraction with Python dependencies resolved by `uv`:

```sh
uv run reproduce.py --input-map saved-inputs.yaml --output-dir replay
```

`saved-inputs.yaml` maps each manifest key to its authenticated raw-file path, for example `intact: /path/to/intact-Q14204-tab27.tsv`. Every listed source must be supplied. The PDF extraction also needs Poppler's `pdftotext` executable. No API key is required to read saved files.

Alternatively, `uv run reproduce.py --download --cache-dir source-downloads --output-dir replay` requests the manifest's public URLs. Publisher access restrictions and changes in live database responses may prevent a matching download. The script stops on a hash mismatch; it does not silently replace historical evidence or pretend that a challenge page is a paper. The saved-input route reproduces the captured version.

The script searches source rows and derives their fields; it does not contain annotation decisions or substitute expected measurement values. Reactome selection supplies explicit path locators, and the script independently verifies every edge and terminal accession. It does not exhaustively enumerate every possible path or infer absence from unselected paths.

The RNA thesis is Alexander Georg Baltz's *The mRNA-bound Proteome of a human cell-line and in early Drosophila embryogenesis*, an author-deposited thesis containing study-specific supplementary information, not the journal's normal publication cache. Its DYNC1H1 row is in group III on physical PDF page 148; the five numerical columns are retained exactly as printed. The urinary measurement comes from the authors' NHLBI database, whose reference key 2 identifies Gonzales et al. 2009. These source relationships remain explicit.
