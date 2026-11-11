# Reproduce the DLG3 fragmentomics evidence

[RESULTS.md](RESULTS.md) explains the biological scope and source-mapping limits. This directory contains the original measurement values and an accession/sequence crosswalk, not inferred full-length interactions.

Run from this directory with [uv](https://docs.astral.sh/uv/):

```bash
uv run --script reproduce.py --download --check
```

Alternatively, use the published Supplementary Data 1 workbook already downloaded locally:

```bash
uv run --script reproduce.py --workbook /path/to/41467_2022_33018_MOESM4_ESM.xlsx --check
```

`--check` regenerates the three output files in memory and compares their bytes with the committed tables. Without `--check`, `--output DIRECTORY` writes regenerated outputs. The inline script metadata pins openpyxl 3.1.5 and PyYAML 6.0.2. The equivalent `just check` and `just check-workbook PATH` recipes are included.

Inputs are the original workbook, the adjacent DLG3 review's unmodified source identities, [identity-sequences.fasta](identity-sequences.fasta), and [identity-provenance.tsv](identity-provenance.tsv). The FASTA contains the literal imported partner products reconstructed from the pinned official UniProt records, including alternative-sequence features. Record and sequence digests preserve that version even if the live databases subsequently change. The parser also accepts another gene, review and identity files through its command-line options.
