# PLPBP structure and variant placement

Reproducible analysis for human PLPBP / PLPHP (UniProtKB:O94903). It places
disease-associated and population variants on the protein and derives the
PLP-binding site from PLP-bound homolog crystal structures.

- `fetch_data.py` downloads every input (UniProt sequences of the reviewed
  PTHR10146 members, the AlphaFold model, PDB templates, the RefSeq CDS,
  ClinVar and gnomAD v4 records).
- `structure_features.py` computes per-residue features (pLDDT, relative SASA,
  family conservation, distance to the transplanted PLP).
- `map_variants.py` checks each variant's c./p. numbering against the CDS and
  the canonical sequence and annotates it with those features.
- `spatial_tests.py` runs permutation tests and N-terminal descriptors.
- `literature_variants.yaml` is an input: variants transcribed from the cited
  papers (each one is checked by `map_variants.py`).

Run `just all` in this directory (network needed for `fetch` and `control`).
Downloaded inputs go to `data/`, which is not committed; `results/` holds the
annotated variant sets and feature tables from the 2026-11-26 run.
Results and their interpretation are in `RESULTS.md`.
