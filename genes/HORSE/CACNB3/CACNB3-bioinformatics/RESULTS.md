# CACNB3: horse–human sequence comparison

The horse sequence A0A5F5PZM5 (517 residues) aligns to human P54284 (484 residues) with 97.11% identity across 484 paired residues. Paired coverage is 100.0% of the human sequence and 93.62% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/CACNB3/CACNB3-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

