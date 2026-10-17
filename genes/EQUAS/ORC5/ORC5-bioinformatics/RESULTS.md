# ORC5: donkey-human sequence comparison

The donkey sequence A0A9L0JAR4 (440 residues) aligns to human O43913 (435 residues) with 92.87% identity across 435 paired residues. Paired coverage is 100.0% of the human sequence and 98.86% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/ORC5/ORC5-bioinformatics/human_O43913-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/ORC5/ORC5-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- donkey residues 436-440.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- BINDING (): human [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT -> donkey [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT.
