# MAP2K2: horse–human sequence comparison

The horse sequence A0A9L0SHX8 (390 residues) aligns to human P36507 (400 residues) with 90.26% identity across 390 paired residues. Paired coverage is 97.5% of the human sequence and 100.0% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/MAP2K2/MAP2K2-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [194] D → horse [194] D.
- BINDING: human [101] K → horse [101] K.
