# CDK7: horse–human sequence comparison

The horse sequence A0A9L0R074 (415 residues) aligns to human P50613 (346 residues) with 95.38% identity across 346 paired residues. Paired coverage is 100.0% of the human sequence and 83.37% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/CDK7/CDK7-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [137] D → horse [137] D.
- BINDING: human [18] L → horse [18] L.
- BINDING: human [19] G → horse [19] G.
- BINDING: human [20] E → horse [20] E.
- BINDING: human [21] G → horse [21] G.
- BINDING: human [22] Q → horse [22] Q.
- BINDING: human [22] Q → horse [22] Q.
- BINDING: human [23] F → horse [23] F.
- BINDING: human [24] A → horse [24] A.
- BINDING: human [25] T → horse [25] T.
- BINDING: human [26] V → horse [26] V.
- BINDING: human [41] K → horse [41] K.
- BINDING: human [41] K → horse [41] K.
- BINDING: human [47] H → horse [47] H.
- BINDING: human [48] R → horse [48] R.
- BINDING: human [92] D → horse [92] D.
- BINDING: human [94] M → horse [94] M.
- BINDING: human [142] N → horse [142] N.
- BINDING: human [155] D → horse [155] D.
