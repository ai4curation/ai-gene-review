# Curation Notes: Mycobacterium phage L5 Gene 57 (gp57, Q05270)

## Overview
- **UniProt ID:** Q05270 (`VG57_BPML5`)
- **Gene Symbol:** `57`
- **Length:** 152 amino acids (17.2 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome immediately downstream of gene `58` (which encodes the N-terminal CHC2 zinc-ribbon DNA-binding domain of DnaG-type primase) and within the early replication module (`gp56`–`gp65`) [PMID:8459766].

## Domain & Family Architecture
- **CDD:** `cd01029` (`TOPRIM_primases`)
- **InterPro:**
  - `IPR034154` (`TOPRIM_DnaG/twinkle`, TOPRIM domain of DnaG-type primases and Twinkle helicase/primases)
  - `IPR006171` (`TOPRIM_dom`, Topoisomerase-primase domain)
- **Pfam:** `PF13155` (`Toprim_2`, residues 6–128)
- **SUPFAM:** `SSF56731` (`DNA primase core`)

## Biological Role & Split Primase Organization
- In mycobacteriophage L5, the DnaG-like DNA primase is split across two adjacent open reading frames transcribed from right to left: `gene 58` (130 aa) encodes the N-terminal CHC2 zinc-finger DNA-binding domain (`IPR036977` / `PF01807`), and `gene 57` (152 aa) encodes the catalytic TOPRIM primase core domain (`cd01029` / `IPR034154` / `PF13155` / `SSF56731`) [PMID:8459766].
- The TOPRIM domain coordinates divalent metal ions (Mg2+) via conserved acidic motifs (E and DXD) to catalyze the synthesis of short oligoribonucleotide primers on single-stranded DNA templates during viral DNA replication.

## GO Annotation Decisions
- Currently no GOA annotations exist for `Q05270`.
- Propose `NEW` annotations based on high-confidence domain architecture (`cd01029`, `IPR034154`, `SSF56731`) and genomic context in the L5 replication cluster:
  - `GO:0003896` (`DNA primase activity`, IEA, `file:BPML5/57/57-uniprot.txt`): gp57 houses the catalytic TOPRIM DNA primase core domain.
  - `GO:0039693` (`viral DNA genome replication`, IEA, `file:BPML5/57/57-uniprot.txt`): DnaG-like primase catalytic core acts in phage DNA genome replication.
