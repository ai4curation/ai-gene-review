# Enterobacteria phage PRD1 gene XXXI (Penton protein P31, P27384)

## Summary
Gene `XXXI` (synonym `C`) encodes the penton base protein P31 (126 aa, ~14 kDa; UniProt `P27384`, `VP31_BPPRD`) of Enterobacteria phage PRD1. P31 folds into a single eight-stranded viral jelly-roll beta-barrel (`PDB:1W8X`) and assembles as a homopentamer at the 5-fold vertices of the pseudo `T=25` icosahedral capsid [PMID:17416681, file:BPPRD/XXXI/XXXI-uniprot.txt]. At each receptor-binding vertex, the P31 penton interlocks laterally with peripentonal major capsid protein P3 (`III`) trimers and beneath with the integral inner-membrane vertex protein P16 (`XVI`), while anchoring the homotrimeric spike protein P5 (`V`) and monomeric receptor-binding adsorption protein P2 (`II`) [PMID:17416681, file:BPPRD/XXXI/XXXI-uniprot.txt].

## Domain Architecture & Structural Features
- **Length**: 126 aa (chain residues 1–126) [file:BPPRD/XXXI/XXXI-uniprot.txt].
- **InterPro / Pfam**:
  - `InterPro:IPR015043` (`Phage_PRD1_P5_spike_N`) / `Pfam:PF08948` (`PRD1_P5_spike_N`, residues 1–126) [file:BPPRD/XXXI/XXXI-uniprot.txt].
- **Subunit & Vertex Interactions**:
  - Forms homopentamers in solution and in the virion (`PDB:1W8X`) [PMID:17416681].
  - Shares 38% sequence identity with the N-terminal jelly-roll domain of the spike protein P5 (`V`), enabling P31 and the N-terminal base of P5 to form an integrated vertex complex [PMID:17416681].
  - Mutants lacking P31 assemble P3/P30 capsid shells that lack pentons, P5 spikes, and P2 adsorption proteins at the five-fold vertices, rendering the particles non-infectious [PMID:17416681].

## Literature & Annotation Review
- **`GO:0019028` (`viral capsid`, IDA, `PMID:11697904`)**:
  - Action: `MODIFY` to `GO:0019030` (`icosahedral viral capsid`). P31 forms the pentameric vertex capsomers (pentons) at the 5-fold axes of the PRD1 icosahedral viral capsid [PMID:17416681, file:BPPRD/XXXI/XXXI-uniprot.txt].
- **Core Function**:
  - `GO:0039660` (`structural constituent of virion`), directly involved in `GO:0019069` (`viral capsid assembly`).
