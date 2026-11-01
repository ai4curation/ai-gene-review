# PMID21533090: target-level plasmodesmal proteomics

The normal Europe PMC supplementary-files endpoint supplied the original XLS tables; `provenance.json` records the URL and archive checksum. `extract_plasmodesmata.py` reproduces target matching with `uv run --with xlrd python genes/ARATH/ABCB1/ABCB1-source-analysis/extract_plasmodesmata.py`. File checksums and one-based Excel rows are recorded in `21533090-target-rows.json`.

The raw identification table (article Table S1, file pone.0018880.s003.xls) includes PIN1 AT1G73590.1 at row1345 with 2 unique peptides and 4.34% coverage; ABCB1 AT2G36910.1 at row2168 with 2 unique peptides and 2.95% coverage; and ABCB4 AT2G47000.1 at row2369 with 4 unique peptides and 4.67% coverage. These are independent mass-spectrometric detections in the plasmodesmata-enriched fraction. They support the existing HDA location claims at the proteomic level without demonstrating exclusive plasmodesmal residence or a transport function across plasmodesmata.

The full article describes cell-wall digestion, differential centrifugation and enrichment controls, but also acknowledges residual contaminants and discusses the need for individual localization confirmation. Only selected other proteins received fluorescent-fusion validation; do not imply that PIN1 or ABCB1/4 did. General contamination concerns do not establish that these particular membrane proteins are contaminants.

Table S2 (file s004) adds classifications and earlier proteomic citations; these are secondary context. Table S3 (file s005) imports GO annotations and is explicitly excluded from the supporting extraction: it is not independent evidence. No source spreadsheet has been edited.
