# Bacteriophage P2 Gene L (Head completion protein gpL; UniProt P25475)

## Overview
Gene **L** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 169-amino-acid head completion (neck/connector) protein gpL (18.9 kDa; `UniProt:P25475`, `InterPro:IPR009225` / `Pfam:PF05926`) (`PMID:1837355`, `PMID:17931675`, `file:BPP2/L/L-uniprot.txt`). Following terminase-mediated DNA packaging into the procapsid, gpL binds to the portal vertex to seal/stabilize the DNA-filled head and complete head morphogenesis, remaining as a structural component of mature P2 and P4 virions (`PMID:1837355`, `PMID:17931675`, `file:BPP2/L/L-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:1837355** (*Nucleotide sequence of the DNA packaging and capsid synthesis genes of bacteriophage P2.*):
  - `"Polypeptides predicted were: a capsid completion protein, gpL; the major capsid precursor, gpN; the presumed capsid scaffolding protein; gpO; the ATPase and proposed endonuclease subunits of terminase, gpP and gpM, respectively; and a candidate for the portal protein, gpQ."`
- **PMID:17931675** (*Incorporation of scaffolding protein gpO in bacteriophages P2 and P4.*):
  - Identified gpL in mature virions by mass spectrometry: `"Using mass spectrometry, we have also identified the head completion protein gpL in the virions."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0039660` (`structural constituent of virion`): **NEW** supported by `PMID:17931675`.
- **Biological Process**:
  - `GO:0019069` (`viral capsid assembly`, IEA): **ACCEPT** (head completion step of capsid assembly; `PMID:1837355`, `PMID:17931675`).
- **Cellular Component**:
  - `GO:0044423` (`virion component`): **NEW** supported by `PMID:17931675` (`Using mass spectrometry, we have also identified the head completion protein gpL in the virions.`).
