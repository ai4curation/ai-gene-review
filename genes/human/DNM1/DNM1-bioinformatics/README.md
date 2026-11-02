# DNM1 primary interaction-data extraction

This offline analysis extracts the source-specific DNM1 partner subset from two genuine primary datasets. It preserves endpoint direction, complete node/edge attributes and every selected CSV field. It makes no annotation verdict, isoform assignment or claim of direct binding.

## Reproduce

Python 3.9 or newer is sufficient; there are no third-party dependencies. Place the exact source snapshots named in `source-manifest.json` in a directory. The manifest supplies the public URLs, byte counts and SHA-256 digests. The analysis rejects changed bytes rather than silently treating a newer live dataset as the recorded snapshot.

```sh
python3 extract.py --inputs-dir /path/to/saved/inputs
python3 extract.py --inputs-dir /path/to/saved/inputs --check
```

The first command writes `RESULTS.json`. `--check` recomputes from the raw files and compares exact output bytes without writing. `--manifest`, `--selection` and `--output` accept alternate paths. The script performs no network calls. If obtaining the inputs afresh, use the URLs in the manifest and confirm their hashes; a currently served dataset may differ from this historical snapshot. The original raw datasets are not rewritten or replaced with projections.

`selection.json` specifies the target and partner symbols. These are the requested source boundary, not measured outputs. Edge IDs, counts, node attributes, CSV indices and measurement values are never hardcoded in the script. The analysis also reports all incident target records so that selection is visible.

## Source selection and direction

The [primary NDEx network](https://public.ndexbio.org/v2/network/95bc75d5-d1d1-11ee-8a40-005056ae23aa) is identified within its CX metadata as the U2OS AP-MS network associated with [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/). Exact symbol matching identifies the DNM1 node. Five edges touch that node; the source-specific SNX9, DNM2 and GRB2 partner filter selects three. The source node and target node are retained without reorienting them. Their literal `bait` attributes indicate the three partners as baits and DNM1 as prey. Nodes that lack an accession are not assigned an invented one.

The [OpenCell primary CSV](https://opencell.czbiohub.org/data/datasets/opencell-protein-interactions.csv) contains five DNM1-involving rows; the DNM2 partner filter selects two reciprocal observations. The [dataset column descriptions](https://opencell.czbiohub.org/data/datasets/opencell-protein-interactions-readme.csv) identify `target_gene_name` as pull-down bait and `interactor_gene_name` as prey. All accession groups are retained as one original field. Neither a group of protein identifiers nor an Ensembl gene match establishes which natural splice product was assayed.

OpenCell indices are explicit: `data_index_zero_based` counts parsed data records, excluding the header; `csv_line_start_one_based_including_header` and `csv_line_end_one_based_including_header` count physical CSV lines. The selected records are data indices 7578 and 7582, physical lines 7580 and 7584. The implementation uses the CSV parser's line counter, so it does not assume that each future record occupies one line.

## Interpretation limits

Omitted partners are outside the requested source subset, not negative interactions. AP-MS association does not establish purified binary contact or native functional stoichiometry. Original measurement labels and numeric strings are preserved; this script applies no significance cutoff and does not reinterpret the `pval` field as a newly computed probability. The abundance-derived columns do not assign a fixed complex stoichiometry. No mitochondrial, neuronal or isoform-specific role is inferred from these records.

The checked projections are independent quality-control comparisons only; they are not inputs to `extract.py`. The human-readable report is in `RESULTS.md` and the complete computed records in `RESULTS.json`.

## RNA-capture table

`extract_rna.py` is a separate offline extraction of the DNM1 measurement row in the original-author thesis associated with PMID:22681889. It requires Python 3 and the `pdftotext` executable from Poppler. The input PDF URL and required SHA-256 are recorded in both the script and `rna-extract.json`. It rejects a changed PDF, reads the actual text, identifies the literal class/DNM1 row and derives its page and fields. No annotation action is produced.

```sh
python3 extract_rna.py --pdf /path/to/Dissertation_Baltz.pdf --output rna-extract.json
```

The executed output is PDF page 147, class III, L1/H1 unavailable, L2 −2.38, mean 2.38, iBAQ 3.94. Values are strings to preserve source notation. The remaining literal columns and original row are retained rather than interpreted as extra activity evidence. The gene's evidence guide explains the single qualifying labeling experiment and absence from the individual PAR-CLIP validation panel. This table result does not establish a distinct physiological RNA-regulatory function.
