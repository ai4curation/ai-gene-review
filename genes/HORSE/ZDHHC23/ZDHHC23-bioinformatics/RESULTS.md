# ZDHHC23: horse–human sequence comparison

The horse sequence A0A9L0T4E4 (448 residues) aligns to human Q8IYP9 (409 residues) with 91.07% identity across 403 paired residues. Paired coverage is 98.53% of the human sequence and 89.96% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/ZDHHC23/ZDHHC23-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [289] C → horse [283] C.
