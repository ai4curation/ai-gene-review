# ATG4C: donkey-human sequence comparison

The donkey sequence A0A9L0IIU3 (458 residues) aligns to human Q96DT6 (458 residues) with 94.98% identity across 458 paired residues. Paired coverage is 100.0% of the human sequence and 100.0% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/ATG4C/ATG4C-bioinformatics/human_Q96DT6-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/ATG4C/ATG4C-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- ACT_SITE (Nucleophile): human [111] C -> donkey [111] C.
- ACT_SITE (): human [345] D -> donkey [345] D.
- ACT_SITE (): human [347] H -> donkey [347] H.
