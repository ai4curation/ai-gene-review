# Bacteriophage P2 Gene A (Replication endonuclease /gpA; UniProt Q06419)

## Overview
Gene **A** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 761-amino-acid replication endonuclease gpA (86.3 kDa; `UniProt:Q06419`). gpA is an essential early protein that initiates rolling-circle (modified rolling-circle) viral DNA replication by introducing a site-specific, strand-specific single-strand nick at the origin of replication (`ori`), which lies within the `A` coding sequence itself (`PMID:8510152`). Following cleavage, gpA becomes covalently linked to the 5' phosphate end of the cleaved strand via its catalytic tyrosine residue (`Tyr-454`), generating a free 3'-OH terminus that serves as a primer for host DNA polymerase III extension (`file:BPP2/A/A-uniprot.txt`).

## Key Literature & Experimental Evidence
- **PMID:8510152** (*Studies of bacteriophage P2 DNA replication. The DNA sequence of the cis-acting gene A and ori region and construction of a P2 mini-chromosome.*):
  - Sequenced the P2 `A` gene and `ori` region: `"The sequenced region contained gene A, which predicts a 761 amino acid residue polypeptide known to induce a single-strand cut at or near ori, and ori, which has been located by electron microscopy to about 89% from the left end of the phage genome."`
  - Demonstrated host lethality upon overexpression: `"The products of orf-80, orf-82 and gene A were found to be lethal to the host when overexpressed."`
- **UniProtKB Q06419 (`file:BPP2/A/A-uniprot.txt`)**:
  - Documents function: `"Replicates the viral genome by introducing a nick at the viral origin of replication, located inside the A gene. Remains covalently attached to the 5' phosphate endpoint, which allows the freed 3'-OH end to serve as primer for host polymerase to synthesize a new copy of the viral genome. Works in cis."`
  - Identifies active site at `Tyr-454` (`MOD_RES 454; /note="O-(5'-phospho-DNA)-tyrosine"`).
  - Contains the Phage_GPA replication protein domain (`InterPro:IPR008766` / `PF05840`).

## Curation Decisions
- **Molecular Function**:
  - `GO:0004519` (`endonuclease activity`, IEA): **ACCEPT** as the core catalytic activity (site-specific nicking endonuclease at `ori`).
  - `GO:0004518` (`nuclease activity`, IEA) and `GO:0016787` (`hydrolase activity`, IEA): **MODIFY** to `GO:0004519` (`endonuclease activity`).
  - `GO:0003688` (`DNA replication origin binding`): **NEW** supported by `PMID:8510152` and `file:BPP2/A/A-uniprot.txt`, as gpA specifically recognizes and cleaves the P2 replication origin (`ori`).
- **Biological Process**:
  - `GO:0039693` (`viral DNA genome replication`, IEA): **ACCEPT** as the core biological process.
  - `GO:0006260` (`DNA replication`, IEA): **MODIFY** to `GO:0039693` (`viral DNA genome replication`).
- **Cellular Component**:
  - `GO:0030430` (`host cell cytoplasm`): **NEW** based on replication of P2 DNA inside the *E. coli* host cytoplasm (`PMID:8510152`).
