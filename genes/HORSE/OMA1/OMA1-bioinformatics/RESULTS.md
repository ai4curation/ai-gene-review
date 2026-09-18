# OMA1: horse–human sequence comparison

The horse sequence A0A9L0R9P8 (513 residues) aligns to human Q96E52 (524 residues) with 66.47% identity across 498 paired residues. Paired coverage is 95.04% of the human sequence and 97.08% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human catalytic/cofactor features are in `results.json`. Reproduce with `uv run python genes/HORSE/OMA1/OMA1-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human catalytic/cofactor features

- ACT_SITE: human [328] E → horse [320] E.
- BINDING: human [327] H → horse [319] H.
- BINDING: human [331] H → horse [323] H.
- BINDING: human [392] E → horse [384] E.
