# DLG4 PDZ interaction measurements

This reproducible extraction links the DLG4 rows of the original PMID:36115835 supplementary workbook to the exact GOA partner accessions and saved official protein sequences. It reports measurements and sequence matches; it does not assign GO actions.

Run `uv run reproduce.py --download --check` from this directory after the review is installed, or supply the original workbook with `--workbook /path/to/41467_2022_33018_MOESM4_ESM.xlsx`. The script checks its SHA-256 digest. To regenerate into a separate directory, omit `--check` and use `--output /path/to/output`. For a different review location, pass `--review /path/to/DLG4-ai-review.yaml`.

Python and package requirements are pinned in the script metadata. The input FASTA and provenance table record the exact identifiers, sequence digests and official source URLs. The downloaded workbook is read without modification. No live UniProt changes are silently adopted during replay.

See [RESULTS.md](RESULTS.md) for interpretation, counts and source limits. All 39 original worksheet fields, including independent assay measurements and peptide modifications, are retained in `measurements.tsv`; `source-row-crosswalk.tsv` distinguishes accession candidates from sequence-supported selections.
