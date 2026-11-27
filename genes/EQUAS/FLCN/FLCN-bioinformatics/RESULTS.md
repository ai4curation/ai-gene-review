# FLCN: donkey-human sequence comparison

The donkey sequence A0A8C4MM62 (578 residues) aligns to human Q8NFG4 (579 residues) with 94.64% identity across 578 paired residues. Paired coverage is 99.83% of the human sequence and 100.0% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/FLCN/FLCN-bioinformatics/human_Q8NFG4-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/FLCN/FLCN-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- SITE (Essential for GTPase activation (GAP) activity): human [164] R -> donkey [164] R.
