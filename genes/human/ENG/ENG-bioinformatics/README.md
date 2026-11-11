# ENG reproducible source context

Run with Python 3.10 or later; only the standard library is required:

```bash
python reproduce.py --check --output replay-results.json
```

`reproduce.py`, `source_projection.py` and `database_context.py` are visible executable source. `inputs.zip` contains sixteen data-only files, whose exact sizes and hashes are recorded in `input-manifest.json`. The program checks the archive scope, rejects unsafe or duplicate members, extracts into a temporary directory, computes results and optionally compares them with `expected-results.json`. The expected file is never used to compute results.

The inputs comprise authentic frozen QuickGO responses, the normal GOA projection, official human/mouse UniProt records and two product FASTAs, PANTHER tree/MSA responses, the full frozen PAINT IBD GAF, the ARBA rule, HPA XML and the UniProt subcellular-location mapping. All imported source fields are preserved. Source joins include ordinary relation fields only to identify records; biological review decisions are not generated from those relations.

The reconstruction proves the 106 → 105 → 104 raw/TSV/seed correspondence, including retained raw annotation extensions in the two collapse groups. It verifies the two natural-product sequences, all three exact ancestral PAINT assertions, current mouse term/negation joins, the sufficient ARBA condition set and the HPA/SL membrane assertions. The output is a database-context analysis, not a review of original publications, a historical reconstruction of transfer events, or a substitute for human scientific judgment.

No installation, network access, article-body redistribution, figure images, executable archive members or ordinary repository validation are required. Protein-group claims in the source guide are based on separately inspected original tables; this script does not pretend to reproduce an unbundled workbook or raw spectral analysis.
