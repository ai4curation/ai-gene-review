# LNPEP: donkey-human sequence comparison

The donkey sequence A0A9L0JGC2 (1026 residues) aligns to human Q9UIQ6 (1025 residues) with 91.02% identity across 1025 paired residues. Paired coverage is 100.0% of the human sequence and 99.9% of the donkey sequence.

Global alignment uses Biopython PairwiseAligner, match 2, mismatch -1, gap open -10, gap extension -0.5. Inputs are UniProt flat files (human reference: `genes/EQUAS/LNPEP/LNPEP-bioinformatics/human_Q9UIQ6-uniprot.txt`); sequence hashes and mapped human site features are in `results.json`. Reproduce with `uv run python genes/EQUAS/LNPEP/LNPEP-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology. Functional transfer must also consider family placement, mapped residues and experimental human evidence.

## Donkey segments not paired with human (>=5 residues)

- none.

## Human segments not paired with donkey (>=5 residues)

- none.

## Mapped human site/motif features

- MOTIF (Dileucine internalization motif): human [53, 54] LL -> donkey [53, 54] LL.
- MOTIF (Dileucine internalization motif): human [76, 77] LL -> donkey [76, 77] LL.
- ACT_SITE (Proton acceptor): human [465] E -> donkey [465] E.
- BINDING (): human [295] E -> donkey [295] E.
- BINDING (): human [428, 429, 430, 431, 432] GAMEN -> donkey [428, 429, 430, 431, 432] GAMEN.
- BINDING (): human [464] H -> donkey [464] H.
- BINDING (): human [468] H -> donkey [468] H.
- BINDING (): human [487] E -> donkey [487] E.
- SITE (Cleavage; to produce pregnancy serum form): human [154, 155] FA -> donkey [154, 155] LA.
- SITE (Transition state stabilizer): human [549] Y -> donkey [550] Y.
