# IRF9: donkey-human sequence comparison

The donkey sequence A0A9L0I7X9 (421 residues) aligns to human Q00978 (393 residues) with 80.41% identity across 388 paired residues. Paired coverage is 98.73% of the human sequence and 92.16% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/IRF9/IRF9-bioinformatics/human_Q00978-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/IRF9/IRF9-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- donkey residues 389-421.

## Human segments not paired with donkey (>=5 residues)

- human residues 193-197.

## Mapped human site/motif features

- none annotated in the human record.
