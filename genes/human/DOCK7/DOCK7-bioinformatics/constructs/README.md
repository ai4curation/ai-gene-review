# DOCK7 construct audit

This saved-input analysis compares deposited experimental sequences with current official protein sequences. It cannot authenticate the historical laboratory reagent used in every assay. The workbook labels and deposited DNA are reported separately.

`analyze_construct.py` finds the three longest methionine-initiated ORFs in all six frames of the requested workbook sequence and reports exact matching blocks against UniProt and optional FASTA sequences. `compare_embl.py` extracts the literal EMBL CDS translation or reads a supplied FASTA, then reports sequence differences. Both scripts take explicit input paths; neither encodes a biological verdict.

Dependencies are pinned in `pyproject.toml`; run `uv sync` followed by `uv run python ...`. The `justfile` takes source paths rather than assuming an absolute filesystem location. Preserve the reported hashes when downloading the primary sources. The source-manifest records the exact saved files and their URLs.

The ENA `/fasta/AAZ38451.1` response unexpectedly contains nucleotide sequence despite its protein-style header. That raw response is retained as provenance but is **not** the protein analysis input. The translated CDS in the authenticated DQ118679.1 EMBL record is used.

All five exact inputs are bundled under `inputs/`. Run these commands from this directory with Python 3.10+ and uv:

```sh
uv sync --frozen
uv run python analyze_construct.py --workbook inputs/32203420-supplementary-tables.xlsx --sheet "Supplementary Table 1" --gene DOCK7 --uniprot inputs/UniProt-Q96N67.json --output reproduced-DOCK7.json
uv run python analyze_construct.py --workbook inputs/32203420-supplementary-tables.xlsx --sheet "Supplementary Table 1" --gene DOCK6 --uniprot inputs/UniProt-Q96HP0.json --output reproduced-DOCK6.json
uv run python compare_embl.py --embl inputs/DQ118679.1.embl --uniprot inputs/UniProt-Q96N67.json --output reproduced-AAZ38451.json
uv run python compare_embl.py --fasta inputs/Q96HP0.fasta --uniprot inputs/UniProt-Q96HP0.json --output reproduced-control.json
```

The corresponding checked outputs are `DOCK7.json`, `DOCK6-control.json`, `AAZ38451-comparison-v2.json` and `compare-control.json`. Coordinates in sequence matching blocks and opcodes are zero-based, half-open; biological residue ranges in RESULTS are one-based inclusive. The workbook physical row includes its header rows. The inputs and exact outputs are hash-pinned in the final review evidence package.
