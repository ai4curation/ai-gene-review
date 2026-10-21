# TNFRSF1A: donkey-human sequence comparison

The donkey sequence A0A9L0JKX4 (410 residues) aligns to human P19438 (455 residues) with 74.32% identity across 405 paired residues. Paired coverage is 89.01% of the human sequence and 98.78% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/TNFRSF1A/TNFRSF1A-bioinformatics/human_P19438-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/TNFRSF1A/TNFRSF1A-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- human residues 64-106.
- human residues 261-265.

## Mapped human site/motif features

- none annotated in the human record.
