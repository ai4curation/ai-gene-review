# Bacteriophage P2 Gene M (Terminase, endonuclease subunit gpM; UniProt P25476)

## Overview
Gene **M** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 247-amino-acid terminase endonuclease subunit gpM (26.9 kDa; `UniProt:P25476`, `InterPro:IPR010270` / `PF05944`) (`PMID:1837355`, `file:BPP2/M/M-uniprot.txt`). Unlike phage lambda (which packages concatemeric DNA), bacteriophage P2 packages monomeric circular double-stranded DNA substrates produced by gpA-mediated rolling-circle replication. In complex with the large ATPase subunit gpP (`UniProt:P25479`), gpM binds the phage `cos` packaging site, catalyzes site-specific endonucleolytic cleavage to generate the 19-nt cohesive 5'-overhang ends (linearizing the circular monomer), and translocates the linearized genome into the empty procapsid (`PMID:1837355`, `file:BPP2/M/M-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:1837355** (*Nucleotide sequence of the DNA packaging and capsid synthesis genes of bacteriophage P2.*):
  - `"Each of six open reading frames found in the interval was assigned to one of the essential genes (Q, P, O, N, M and L) by correlating genetic, physical and mutational data with DNA and protein sequence information. Polypeptides predicted were: a capsid completion protein, gpL; the major capsid precursor, gpN; the presumed capsid scaffolding protein; gpO; the ATPase and proposed endonuclease subunits of terminase, gpP and gpM, respectively; and a candidate for the portal protein, gpQ."`
- **UniProtKB P25476 (`file:BPP2/M/M-uniprot.txt`)**:
  - `"The terminase Complex consists of a small subunit (gpM) with endonuclease activity and a large ATPase subunit (gpP). First, the hetero-oligomeric terminase binds to the circular monomeric viral DNA substrate at the packaging initiation site (cos) and gpM introduces two staggered nicks to generate the 19-bp 5'-overhangs of the cohesive ends, thereby linearizing the genome."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0003677` (`DNA binding`, IEA): **ACCEPT**
  - `GO:0004519` (`endonuclease activity`, IEA): **ACCEPT**
  - `GO:0004518` (`nuclease activity`, IEA) and `GO:0016787` (`hydrolase activity`, IEA): **MODIFY** to `GO:0004519` (`endonuclease activity`).
- **Biological Process**:
  - `GO:0019069` (`viral capsid assembly`, IEA): **MODIFY** to `GO:0019073` (`viral DNA genome packaging`) (InterPro `IPR010270` is mapped to `viral capsid assembly`, whereas gpM is the terminase subunit that cleaves `cos` and packages viral DNA into assembled procapsids).
  - `GO:0019073` (`viral DNA genome packaging`): **NEW** supported by `PMID:1837355` and `file:BPP2/M/M-uniprot.txt`.
- **Cellular Component / Complex**:
  - `GO:0043493` (`viral terminase complex`): **NEW** (`part_of`, put in `in_complex` in `core_functions`).
  - `GO:0030430` (`host cell cytoplasm`): **NEW** (`located_in`, put in `locations` in `core_functions`).
