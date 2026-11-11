# IRF9 (horse, A0A9L0SN53) gene-model comparison

Script: `compare_gene_models.py` (run with `uv run --script compare_gene_models.py`; raw output in `compare_gene_models_output.txt`). Sequences were downloaded from UniProt REST at run time and aligned globally (BLOSUM62, gap open -10, extend -0.5, free end gaps).

## Gene-model context

All five horse IRF9 UniProt entries (A0A9L0SN53, F6Z2B0, A0A9L0TC51, A0A9L0STH9, A0A9L0SUN9) are translations of one Ensembl gene, ENSECAG00000024429. Ensembl marks transcript ENSECAT00000115676 (A0A9L0SN53) as canonical, and the UniProt gene-centric canonical for proteome UP000002281 is also A0A9L0SN53. F6Z2B0 is the model carrying the RefSeq cross-reference XP_005603301.2.

## Findings

- A0A9L0SN53 (529 aa) is identical to F6Z2B0 (445 aa) over all 445 aligned positions, except for an 84-residue insertion after F6Z2B0 residue 349 (GETAPGPEPLSLPFSPRWARLGRTCQPPVLPPAGPPSQPVQSILWSPALSPGSPPSPAKATEDGLQSVTSRGAPSCGSVQSSWE).
- Against human IRF9 (Q00978, 393 aa) A0A9L0SN53 is 83.2% identical over 393 aligned positions. The same 84-residue insertion falls after human residue 330, inside the C-terminal IRF-association domain (IAD), between the conserved segments ...ELFRT(A/T)(Y/H)FCR and DL(V/A)RYFQGLGPPPKF.... Two further horse-specific differences are present in every horse model: a 17-residue insertion after human residue 216 (CADQVDPWGEALVQMAT), N-terminal to the IAD core, and a 33-residue C-terminal extension beyond human residue 393.
- The 84-residue insertion is absent from human IRF9, mouse Irf9 (Q61179) and the donkey IRF9 model A0A9L0I7X9, and from three of the other four horse models; A0A9L0TC51 carries only its first 33 residues. Its position at a splice-variable site is consistent with an alternative exon or retained-intron model rather than a conserved part of IRF9.
- The N-terminal region, including the IRF tryptophan-pentad DNA-binding domain (UniProt PROSITE PS51507 feature, residues 9-116), is identical between A0A9L0SN53 and F6Z2B0 and aligns with the human IRF9 DBD with no gap block of 3 or more residues (the script reports only such blocks; per-domain identity was not computed).

## Interpretation and limits

A0A9L0SN53 is the canonical product in UniProt and Ensembl, but its IAD is interrupted by a Pro-rich insertion that no characterised IRF9 has, and UniProt's own Pfam scan splits the IRF-3 (IAD) domain into two hits (Pfam PF10401 count 2 in A0A9L0SN53 against 1 in F6Z2B0). Whether the IAD of this model still folds and binds STAT2 has not been tested. DNA-binding function rests on the intact DBD; ISGF3 complex membership depends on the IAD and is therefore less certain for this particular model than for the gene. This analysis does not determine which transcript is the dominant one expressed in horse tissues.
