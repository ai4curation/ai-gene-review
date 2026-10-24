# Gene Review Notes: Bacillus phage phi29 `8` (`P13849`, `CAPSD_BPPH2`)

## Overview
- **Gene symbol**: `8`
- **UniProt ID**: `P13849` (`CAPSD_BPPH2`)
- **Protein name**: Major capsid protein gp8
- **Length**: 448 amino acids (49,645 Da)
- **Taxon**: *Bacillus phage phi29* (`NCBITaxon:2884424`)
- **InterPro / Pfam domains** (from `file:BPPH2/8/8-uniprot.txt`):
  - `InterPro:IPR003343` (`Big_2`, Bacterial Ig-like domain 2)
  - `InterPro:IPR058011` (`Phi29_MCP`, Bacteriophage phi29 Major Capsid Protein)
  - `Pfam:PF02368` (`Big_2`)
  - `Pfam:PF25622` (`Phi29_MCP`)

## Literature & Bioinformatic Synthesis
- **Capsid Architecture and Stoichiometry**: gp8 is the major capsid protein of *Bacillus phage phi29*, assembling into a prolate icosahedral shell approximately 54 nm long and 45 nm wide with *T*=3, *Q*=5 elongation symmetry (`file:BPPH2/8/8-uniprot.txt`; `PMID:11562162`; `PMID:17098197`). Each prolate capsid shell comprises exactly 235 monomers of gp8 organized into 11 pentamers (at 11 of the 12 icosahedral vertices, with the 12th occupied by the dodecameric portal `gp10`) and 30 hexamers forming the hemispherical caps and equatorial belt [PMID:11562162; PMID:17098197].
- **Domain Organization**: High-resolution cryo-EM reconstructions (`PMID:17098197`; `PMID:30910995`) show that gp8 consists of an N-terminal canonical HK97-like shell domain (`Pfam:PF25622`) and a C-terminal bacterial immunoglobulin-like (BIG2) domain (`Pfam:PF02368`) that projects outward on the capsid surface and forms the attachment platform for the trimeric head fibers (`gp8.5`) at quasi-3-fold symmetry positions.
- **Role in Procapsid Assembly**: During morphogenesis, gp8 monomers co-assemble with the internal scaffolding protein `gp7`, portal protein `gp10`, and head fiber protein `gp8.5` to form the procapsid (`GO:0046729`) [PMID:22225806]. In the absence of `gp7` or `gp10`, gp8 assembles into smaller isometric *T*=3 or *T*=4 particles (`PMID:17098197`).

## Annotation Review Summary
- `GO:0019028` (`viral capsid`, IEA, `GO_REF:0000043`): `ACCEPT`. Core cellular component location of gp8.
- `GO:0039617` (`T=3 icosahedral viral capsid`, IDA `PMID:11562162`, IDA `PMID:17098197`, IEA `GO_REF:0000043`): `ACCEPT` all three rows. Phage phi29 has a prolate *T*=3, *Q*=5 capsid whose end caps have *T*=3 icosahedral symmetry (`PMID:11562162`; `PMID:17098197`).
- `GO:0046729` (`viral procapsid`, IDA, `PMID:22225806`): `ACCEPT`. gp8 forms the outer shell of the DNA-packaging procapsid (`PMID:22225806`).
- **Core Functions**: `GO:0039660` (`structural constituent of virion`), involved in `GO:0019069` (`viral capsid assembly`), localized to `GO:0019028` (`viral capsid`), `GO:0039617` (`T=3 icosahedral viral capsid`), and `GO:0046729` (`viral procapsid`).
