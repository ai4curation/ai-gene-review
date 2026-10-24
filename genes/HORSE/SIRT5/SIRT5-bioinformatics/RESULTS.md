# SIRT5: horse–human sequence comparison

The horse sequence F6S899 (282 residues) aligns to human Q9NXA8 (310 residues) with 67.5% identity across 280 paired residues. Paired coverage is 90.32% of the human sequence and 99.29% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/SIRT5/SIRT5-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [158] H → horse [158] H.
- BINDING: human [102] Y → horse [102] Y.
- BINDING: human [105] R → horse [105] R.
- BINDING: human [140, 141, 142, 143] QNID → horse [140, 141, 142, 143] QNID.
- BINDING: human [166] C → horse [166] C.
- BINDING: human [169] C → horse [169] C.
- BINDING: human [207] C → horse [207] W.
- BINDING: human [212] C → horse [212] W.
- BINDING: human [249, 250, 251] GTS → horse [None, 232, 233] -NS.
- BINDING: human [275, 276, 277] NTE → horse [None, None, None] ---.
- BINDING: human [293] C → horse [265] K.
