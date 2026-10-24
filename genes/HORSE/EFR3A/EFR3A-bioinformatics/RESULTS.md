# EFR3A: horse–human sequence comparison

The horse sequence A0A9L0S4L8 (796 residues) aligns to human Q14156 (821 residues) with 98.24% identity across 796 paired residues. Paired coverage is 96.95% of the human sequence and 100.0% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/EFR3A/EFR3A-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

