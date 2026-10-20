# Gene Review Notes: Bacillus phage phi29 `7` (`P13848`, `SCAF_BPPH2`)

## Overview
- **Gene symbol**: `7`
- **UniProt ID**: `P13848` (`SCAF_BPPH2`)
- **Protein name**: Capsid assembly scaffolding protein gp7
- **Length**: 98 amino acids (11,246 Da)
- **Taxon**: *Bacillus phage phi29* (`NCBITaxon:2884424`)
- **InterPro / Pfam domains** (from `file:BPPH2/7/7-uniprot.txt`):
  - `InterPro:IPR038032` (`Gp7`)
  - `InterPro:IPR024374` (`Phage_phi-29_Gp7`)
  - `Pfam:PF11418` (`Scaffolding_pro`)

## Literature & Bioinformatic Synthesis
- **Role in Prolate Procapsid Assembly**: gp7 is the transient internal scaffolding protein essential for assembling the *T*=3, *Q*=5 prolate icosahedral procapsid (prohead) of phage phi29 [PMID:17198713; file:BPPH2/7/7-uniprot.txt]. Approximately 147–180 copies of gp7 co-assemble with the dodecameric portal protein (`gp10`) and major capsid protein (`gp8`) in the host cell cytoplasm (`GO:0030430`) to form concentric internal shells (`GO:0046806` `viral scaffold`) within the procapsid (`GO:0046729`) [PMID:17198713; file:BPPH2/7/7-uniprot.txt].
- **Structure and Oligomerization**: Crystal structure analysis (`PMID:12778115`, PDB `1NO4`/`1NOH`) revealed that gp7 forms homodimers composed of an N-terminal helix-loop-helix domain that structurally mimics a dsDNA double helix and a C-terminal coiled-coil bundle with an unstructured acidic tail [PMID:17198713; file:BPPH2/7/7-uniprot.txt]. Mutational dissection in an *in vitro* assembly system (`PMID:17198713`) showed that the N-terminal head domain is required for procapsid geometry determination and interaction with the portal (`gp10`), while the C-terminal tail (specifically residues 79–98) is required to bind major capsid protein (`gp8`) monomers and promote polymerization into *T*=3, *Q*=5 shells.
- **Intact Exit During DNA Packaging**: Unlike proteolytic phage scaffolds, gp7 is not cleaved; instead, all gp7 molecules exit intact from the procapsid during ATP-driven viral DNA packaging (`PMID:17198713`; `file:BPPH2/7/7-uniprot.txt`) and are absent from mature virions.

## Annotation Review Summary
- `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`): `KEEP_AS_NON_CORE`. Crystallographic studies (`PMID:12778115`) detected non-specific interactions between gp7 dimers and short nucleic acid segments inside the prohead, but gp7's primary biological role is protein-protein scaffolding of procapsid assembly (`PMID:17198713`).
- `GO:0019068` (`virion assembly`, IDA, `PMID:17198713`): `MODIFY` -> `GO:0019069` (`viral capsid assembly`). `PMID:17198713` specifically demonstrates that gp7 directs procapsid (capsid shell) assembly (`GO:0019069`, a child of `GO:0019068`) rather than whole-virion or tail assembly.
- `GO:0046806` (`viral scaffold`, IDA, `PMID:17198713`): `ACCEPT`. Directly supported by cryo-EM and biochemical evidence showing gp7 forms the internal prohead scaffold (`PMID:17198713`).
