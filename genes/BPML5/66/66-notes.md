# Curation Notes: Mycobacterium phage L5 Gene 66 (gp66, Q05280)

## Overview
- **UniProt ID:** Q05280 (`VG66_BPML5`)
- **Gene Symbol:** `66`
- **Length:** 207 amino acids (23.3 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome immediately upstream of the DnaB-like helicase gene (`65`) and downstream of genes `67`–`70` [PMID:8459766].

## Domain & Family Architecture
- **InterPro:**
  - `IPR004843` (`Calcineurin-like_PHP`, Calcineurin-like phosphoesterase domain)
  - `IPR029052` (`Metallo-depent_PP-like`, Metallo-dependent phosphatase-like superfamily)
- **Pfam:** `PF00149` (`Metallophos`, Calcineurin-like phosphoesterase, residues 7–194)
- **SUPFAM:** `SSF56300` (`Metallo-dependent phosphatases`)

## Biological Role & Existing GOA Review
- L5 gp66 contains a calcineurin-like metallophosphoesterase domain (`PF00149` / `IPR004843` / `IPR029052`) spanning almost its entire length (residues 7–194).
- Calcineurin-like metallophosphoesterases coordinate a binuclear divalent metal center (typically Mn2+, Fe2+, Ni2+, or Zn2+) via conserved His/Asp/Asn motifs to catalyze the hydrolysis of phosphoester bonds in nucleotides, nucleic acids, or phosphorylated substrates; in bacteriophages, homologs include lambda Bar/NinI-like protein phosphatases and Mre11/SbcD-like or cyclic nucleotide phosphoesterases.
- Review of existing GOA annotation:
  - `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000002`, `InterPro:IPR004843`): **MODIFY** to `GO:0016788` (`hydrolase activity, acting on ester bonds`). `GO:0016787` is overly broad; because `IPR004843` / `PF00149` is specifically a calcineurin-like metallophosphoesterase domain, the more specific descendant `GO:0016788` (`hydrolase activity, acting on ester bonds`) is supported without over-specifying whether the physiological substrate is a phosphomonoester (`GO:0016791`) or phosphodiester (`GO:0008081`).
- Propose `NEW` annotations:
  - `GO:0016788` (`hydrolase activity, acting on ester bonds`, IEA, `file:BPML5/66/66-uniprot.txt`): replaces the overly general `GO:0016787`.
  - `GO:0046872` (`metal ion binding`, IEA, `file:BPML5/66/66-uniprot.txt`): calcineurin-like metallophosphoesterases require a catalytic binuclear metal center (`IPR029052`, `PF00149`).
