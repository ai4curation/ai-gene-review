# DOCK8 deposited construct comparison

This analysis identifies the coding body in the library DNA deposited with [PMID:32203420](https://doi.org/10.1038/s41556-020-0488-x). It compares all three forward translations with all four retrieved human DOCK8 product FASTAs. A DOCK6 insert is processed as an independent control.

Run `just reproduce` from this directory. Python 3.12 or later, `uv`, and `just` are required; the Python analysis uses only the standard library. Alternatively, run the two commands in `justfile` directly. The exact input files are included, so reproduction does not require network access. Outputs are deterministic JSON and extracted DNA FASTA files.

`source-manifest.json` records the original URLs, acquisition times and SHA-256 hashes. To test recovery into a separate directory, use `uv run --frozen python fetch_inputs.py --manifest source-manifest.json --output-dir recovered`. A changed remote record fails the hash check rather than silently replacing the fixed input. No input or output identities are hardcoded in `analyze.py`; the named workbook sheet is the documented table format. The gene, workbook, comparison sequences and output paths are command-line parameters.

The method extracts the unique long A/C/G/T cell from the matching Supplementary Table 1 row, translates it using the standard genetic code, and requires an exact complete FASTA-sequence match. It reports translation frame, offset and flanks separately. It is a sequence-identity analysis, not a test of biological activity or an assertion that the deposited record proves the contents of every physical assay vial. See [RESULTS.md](RESULTS.md).
