# Curation Notes: Mycobacterium phage L5 Gene 69 (gp69, Q05283)

## Overview
- **UniProt ID:** Q05283 (`VG69_BPML5`)
- **Gene Symbol:** `69`
- **Length:** 290 amino acids (32.7 kDa)
- **Genomic Context:** Encoded on the leftwards-transcribed right arm of the Mycobacterium phage L5 genome between gene `68` and gene `70`, just downstream of the prophage repressor gene `71` [PMID:8459766, PMID:9636706].

## Domain & Family Architecture
- **InterPro:**
  - `IPR038726` (`PDDEXK_AddAB-type`, AddAB-type PD-(D/E)XK nuclease domain)
  - `IPR011604` (`PDDEXK-like_dom_sf`, PD-(D/E)XK nuclease superfamily)
  - `IPR011335` (`Restrct_endonuc-II-like`, Restriction endonuclease type II-like superfamily)
- **Pfam:** `PF12705` (`PDDEXK_1`, PD-(D/E)XK nuclease superfamily, residues 99–282)
- **SUPFAM:** `SSF52980` (`Restriction endonuclease-like`)

## Biological Role & GO Annotation Decisions
- L5 gp69 is a 290-amino-acid nuclease containing a C-terminal AddAB-type PD-(D/E)XK nuclease domain (`PF12705` / `IPR038726` / `IPR011604`, residues 99–282) belonging to the restriction endonuclease type II-like structural superfamily (`IPR011335` / `SSF52980`).
- In bacteriophages, PD-(D/E)XK family nucleases (such as phage RecE/Cas4/AddB-like exonucleases) catalyze metal-dependent phosphodiester cleavage of DNA during recombination, replication, or host DNA degradation.
- Currently no GO annotations exist in GOA (`69-goa.tsv`).
- Propose `NEW` annotations supported by `IPR038726` (`PDDEXK_AddAB-type`), `IPR011604` (`PDDEXK-like_dom_sf`), and `PF12705` (`PDDEXK_1`):
  - `GO:0004518` (`nuclease activity`, IEA, `file:BPML5/69/69-uniprot.txt`): supported by the PD-(D/E)XK nuclease domain (`PF12705`, `IPR038726`, `IPR011604`), without over-specifying endo- vs. exonuclease polarity in the absence of biochemical assays.
  - `GO:0003677` (`DNA binding`, IEA, `file:BPML5/69/69-uniprot.txt`): AddAB-type PD-(D/E)XK nucleases bind DNA substrates.
