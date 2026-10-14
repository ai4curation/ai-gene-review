# NDEL1: donkey-human sequence comparison

The donkey sequence A0A9L0IJ72 (481 residues) aligns to human Q9GZM8 (345 residues) with 97.1% identity across 345 paired residues. Paired coverage is 100.0% of the human sequence and 71.73% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/human/NDEL1/NDEL1-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/NDEL1/NDEL1-bioinformatics/compare_pair.py genes/human/NDEL1/NDEL1-uniprot.txt`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- donkey residues 339-474.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- none annotated in the human record.
