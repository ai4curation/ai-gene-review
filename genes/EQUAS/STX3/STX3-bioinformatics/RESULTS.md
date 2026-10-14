# STX3: donkey-human sequence comparison

The donkey sequence A0A9L0J901 (289 residues) aligns to human Q13277 (289 residues) with 92.39% identity across 289 paired residues. Paired coverage is 100.0% of the human sequence and 100.0% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/STX3/STX3-bioinformatics/human_Q13277-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/STX3/STX3-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- none annotated in the human record.
