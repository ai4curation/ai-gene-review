# apl2 (O43079) sequence-feature analysis (2026-10-21)

Script: `apl2_motifs.py` (PEP 723; run with `uv run --script apl2_motifs.py`). Raw output: `apl2_motifs.out.txt`.
Input: the local UniProt flat file `apl2-uniprot.txt`.

## Results

- Length: 683 aa.
- Domain cross-references: Adaptin_N trunk (PF01602, IPR002553), AP_beta (IPR026739), AP_complex_bsu_1_2_4
  (IPR016342), PIRSF002291 AP_complex_beta, PANTHER family PTHR11134 with no subfamily assigned.
- No beta-adaptin appendage (ear) domain signature (IPR015151, IPR013037, IPR012295, PF09066, PF02883) is listed in the record.
  The protein therefore consists of the trunk plus a short C-terminal hinge segment; the metazoan
  beta1/beta2 appendage that recruits endocytic accessory proteins is absent.
- One clathrin-box consensus match L[LI][DEN][LF][DE]: LLDLD at 623-627, in the hinge-like region after the trunk.
  This is the same motif class as the hinge clathrin box of mammalian beta-adaptins.

## Interpretation

The trunk domain is what binds the gamma, mu1 and sigma1 subunits, consistent with the pull-down showing
Apm1 binds Apl2 (PMID:19624755). The retained LLDLD clathrin box makes direct clathrin binding by Apl2
plausible, but it is a sequence prediction: no experiment in S. pombe has tested clathrin binding by Apl2.

Phylogenetic placement of apl2 as the fungal AP-1 beta (separate from the AP-2 beta apl1) comes from the
16-taxon MAFFT/NJ tree in `genes/NEUCR/NCU09721/NCU09721-bioinformatics/RESULTS-rereview.md`.

Limitations: motif matching only; no structural modelling and no test of whether LLDLD is accessible.
