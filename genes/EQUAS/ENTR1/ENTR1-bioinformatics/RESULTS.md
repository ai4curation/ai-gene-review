# ENTR1: donkey-human sequence comparison

The donkey sequence A0A8C4MKL2 (356 residues) aligns to human Q96C92 (435 residues) with 81.41% identity across 355 paired residues. Paired coverage is 81.61% of the human sequence and 99.72% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/ENTR1/ENTR1-bioinformatics/human_Q96C92-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/ENTR1/ENTR1-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- human residues 9-85.

## Mapped human site/motif features

- none annotated in the human record.
