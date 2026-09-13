# USP8: horse–human sequence comparison

The horse sequence A0A9L0T7K6 (1112 residues) aligns to human P40818 (1118 residues) with 91.82% identity across 1112 paired residues. Paired coverage is 99.46% of the human sequence and 100.0% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/USP8/USP8-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [786] C → horse [785] C.
- ACT_SITE: human [1067] H → horse [1066] H.
