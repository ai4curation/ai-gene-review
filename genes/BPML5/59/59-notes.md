# Curation Notes: Mycobacterium phage L5 Gene 59 (gp59, Q05272)

## Overview
- **UniProt ID:** Q05272 (`VG59_BPML5`)
- **Gene Symbol:** `59`
- **Length:** 164 amino acids (18.6 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome within the replication/recombination gene cluster (`gp56`–`gp69`) [PMID:8459766].

## Domain & Family Architecture
- **InterPro:**
  - `IPR004211` (`Endonuclease_7`, Phage endonuclease VII)
  - `IPR044925` (`His-Me_finger_sf`, His-Me finger endonuclease superfamily)
- **Pfam:** `PF02945` (`Endonuclease_7`, residues 18–112)
- **SUPFAM:** `SSF54104` (`His-Me finger endonucleases`)

## Biological Role & Function
- L5 gp59 is a homolog of bacteriophage T4 endonuclease VII (`PF02945` / `IPR004211`), a His-Me finger (HNH-like beta-beta-alpha-Me) Holliday junction resolvase and branch-specific endodeoxyribonuclease.
- In dsDNA bacteriophages, endonuclease VII resolves Holliday recombination intermediates and branched concatenated DNA structures generated during phage DNA replication and recombination prior to genome packaging.

## GO Annotation Decisions
- Currently no GOA annotations exist for `Q05272`.
- Propose `NEW` annotations based on `IPR004211` (`Endonuclease_7`), `PF02945`, and `IPR044925` (`His-Me_finger_sf`):
  - `GO:0008821` (`crossover junction endodeoxyribonuclease activity`, IEA, `file:BPML5/59/59-uniprot.txt`): specific catalytic activity of phage endonuclease VII Holliday junction resolvases.
  - `GO:0003677` (`DNA binding`, IEA, `file:BPML5/59/59-uniprot.txt`): binds branched and four-way junction DNA substrates.
  - `GO:0006310` (`DNA recombination`, IEA, `file:BPML5/59/59-uniprot.txt`): resolves Holliday junction recombination intermediates.
