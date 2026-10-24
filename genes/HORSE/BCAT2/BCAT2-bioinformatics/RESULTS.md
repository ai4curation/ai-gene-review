# BCAT2: horse–human sequence comparison

The horse sequence A0A9L0TSN4 (452 residues) aligns to human O15382 (392 residues) with 83.42% identity across 392 paired residues. Paired coverage is 100.0% of the human sequence and 86.73% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/BCAT2/BCAT2-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- BINDING: human [126] R → horse [186] R.
- BINDING: human [168] Y → horse [228] Y.
- BINDING: human [234] Y → horse [294] Y.
- BINDING: human [296] V → horse [356] V.
- BINDING: human [297] V → horse [357] V.
- BINDING: human [340] T → horse [400] T.
