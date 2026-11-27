# Bacteriophage P2 Gene N (Major capsid protein gpN; UniProt P25477)

## Overview
Gene **N** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 357-amino-acid major capsid precursor protein gpN (40.2 kDa; `UniProt:P25477`) (`PMID:1837355`, `PMID:1840708`). During procapsid assembly and maturation—directed either by the internal scaffolding/protease protein gpO (forming T=7 icosahedral P2 heads, ~60 nm diameter) or by the satellite phage P4 external scaffolding protein Sid (forming T=4 icosahedral P4 heads, ~45 nm diameter)—gpN undergoes proteolytic maturation with removal of the N-terminal 31 amino acids (yielding the mature 326-aa major capsid protein `gpN*`,residues 32–357) (`PMID:8874520`, `PMID:17931675`). Mutations in the central region of `N` (`sir` mutations, *sid responsiveness*) render gpN unresponsive to size redirection by P4 Sid (`PMID:1840708`).

## Key Literature & Experimental Evidence
- **PMID:1837355** (*Nucleotide sequence of the DNA packaging and capsid synthesis genes of bacteriophage P2.*):
  - Sequenced the P2 morphogenetic operon (`Q-P-O-N-M-L`): `"Polypeptides predicted were: a capsid completion protein, gpL; the major capsid precursor, gpN; the presumed capsid scaffolding protein; gpO; the ATPase and proposed endonuclease subunits of terminase, gpP and gpM, respectively; and a candidate for the portal protein, gpQ."`
- **PMID:1840708** (*Morphopoietic switch mutations of bacteriophage P2.*):
  - Mapped `sir` mutations to gene `N`: `"For eight we could assign their sir mutation to P2 gene N, which encodes the major capsid protein. DNA sequencing indicated an open reading frame of 357 codons for gene N and showed these sir mutations to affect only four codons within a 38-codon segment in the middle of N."`
- **PMID:8874520** (*The N-terminal part of bacteriophage P2 capsid protein is essential for postassembly maturation of P2 and P4 capsids.*):
  - Showed N-terminal cleavage of 31 residues: `"During capsid assembly of bacteriophage P2 and its satellite phage P4, gpN undergoes proteolytic cleavage with the removal of the first 31 amino acids. The truncated protein gpN* is unable to support formation of viable phages in complementation tests."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0039660` (`structural constituent of virion`): **NEW** supported by `PMID:1840708` and `PMID:8874520`.
- **Biological Process**:
  - `GO:0019069` (`viral capsid assembly`): **NEW** supported by `PMID:8874520` and `PMID:1840708`.
- **Cellular Component**:
  - `GO:0019028` (`viral capsid`, IEA): **ACCEPT**
