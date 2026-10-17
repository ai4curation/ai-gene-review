# BICDL1: donkey-human sequence comparison

The donkey sequence A0A9L0JLY3 (573 residues) aligns to human Q6ZP65 (573 residues) with 95.99% identity across 524 paired residues. Paired coverage is 91.45% of the human sequence and 91.45% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/BICDL1/BICDL1-bioinformatics/human_Q6ZP65-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/BICDL1/BICDL1-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- donkey residues 389-436.

## Human segments not paired with donkey (>=5 residues)

- human residues 255-303.

## Mapped human site/motif features

- MOTIF (CC1 box): human [113, 114, 115, 116, 117] AARLG -> donkey [114, 115, 116, 117, 118] AARLG.
