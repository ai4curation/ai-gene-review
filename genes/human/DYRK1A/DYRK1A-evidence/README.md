# DYRK1A saved-source extraction

This package reproduces records from four authenticated source snapshots. It extracts data and does not assign annotation actions, biological functions, direct-contact claims or natural isoforms. No network request is made by the scripts.

## Run from saved inputs

Python 3.9 or later is sufficient; all code uses the standard library. Keep the two Python files together. Copy `local-inputs.example.json` to a local mapping and replace its values with the saved paths. Relative paths resolve beside that mapping.

```sh
python3 -B extract.py --inputs-map local-inputs.json --check
```

Alternatively, place the four manifest-named source files in one directory:

```sh
python3 -B extract.py --inputs-dir /path/to/saved/inputs --check
```

Omit `--check` and supply `--output extracted.json` to write a fresh result. `--check` recomputes every reported record and compares exact output with `RESULTS.json`, writing nothing. Changed input hashes or sizes are rejected before extraction. Both original supplementary ZIP hashes and the selected embedded workbook hashes are checked. The two standalone extracted workbooks are not required.

## Sources

These are authentic recorded source URLs, not new retrieval claims. Save the exact snapshots below; a later repackaged archive or updated dataset will intentionally fail the pinned hash check. Full digests, sizes and retrieval provenance are in `source-manifest.json`. No large source ZIP is redistributed by this package.

| Input | Recorded source | Embedded workbook |
|---|---|---|
| apms | [40205054-apms-network.json](https://public.ndexbio.org/v2/network/95bc75d5-d1d1-11ee-8a40-005056ae23aa) | Not applicable |
| opencell | [OpenCell-protein-interactions.csv](https://opencell.czbiohub.org/data/datasets/opencell-protein-interactions.csv) | Not applicable |
| table_35914814 | [35914814-supplementary.zip](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9348576/supplementaryFiles) | LSA-2021-01205_TableS3.xlsx |
| table_36950384 | [36950384-supplementary.zip](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10025425/supplementaryFiles) | mmc4.xlsx |

## Selection and coordinates

`selection.json` states the target and partner filters. Values, row numbers, node identifiers, edge identifiers, counts and results are derived from source files rather than prescribed by those filters.

- Table S3 selects the target accession in either participant accession column, retaining every literal cell and all three distinct bait labels. It preserves binding-site coordinates exactly as supplied; it does not reinterpret their units or authenticate complete experimental inserts. Rows 1–3 are retained as headers. The workbook information sheet is not a target measurement table and is not projected.
- The mmc4 replay retains all target-index or target-interactor rows in four measurement/summary sheets. The Overview sheet is explanatory and is not projected. Selected partners form a reporting subset, not a score threshold. Summary, list, frequency and annotation views are distinct views of the data; repeated rows across them or the DYRK1A_Broad/DYRK1A dataset labels must not be counted as independent experiments.
- XLSX worksheet rows and column headers are one-based and reproduced in full. Empty cells remain JSON null. The standard-library reader preserves text, numeric and Boolean literal values and cached formula values without evaluating formulae; the selected source sheets have no formula cells. It does not interpret Excel formatting as biology.
- The AP-MS graph preserves endpoint direction, full selected edges and all supplied node/edge attributes. Every target-incident edge is listed separately, with a flag for the requested partner subset.
- OpenCell retains the full accession group and every source field as text. Data indices are zero-based; physical CSV line positions include the header and are one-based. The field named pval is reproduced without numerical or statistical reinterpretation. The selected accession group contains multiple products and DYRK1B entries as well as DYRK1A; it is not unique natural-isoform evidence.

Unselected incident records remain visible. Their omission from the selected subset is not a negative interaction claim. No purified binding, physiological context or orthogonal retest is inferred by this extraction. The owner review remains responsible for assay and functional interpretation.

`graph_csv.py` is byte-identical to the previously executed DNM1 portable graph/CSV extractor. `extract.py` adds hash-checked archive-member extraction and worksheet parsing. `RESULTS.md` summarizes the actual execution; `RESULTS.json` contains full selected fields and incident context.
