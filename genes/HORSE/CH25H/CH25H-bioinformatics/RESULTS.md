# CH25H: horse–human sequence comparison

The horse sequence F6T000 (270 residues) aligns to human O95992 (272 residues) with 83.33% identity across 270 paired residues. Paired coverage is 99.26% of the human sequence and 100.0% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/CH25H/CH25H-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

