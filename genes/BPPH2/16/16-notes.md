# Gene Review Notes: Bacillus phage phi29 `16` (`P11014`, `PKG16_BPPH2`)

## Overview
- **Gene symbol**: `16`
- **UniProt ID**: `P11014` (`PKG16_BPPH2`)
- **Protein name**: DNA packaging ATPase gp16
- **Length**: 332 amino acids (38,900 Da)
- **Taxon**: *Bacillus phage phi29* (`NCBITaxon:2884424`)
- **InterPro / Pfam domains** (from `file:BPPH2/16/16-uniprot.txt`):
  - `InterPro:IPR027417` (`P-loop_NTPase`, P-loop containing nucleoside triphosphate hydrolase)
  - `InterPro:IPR008784` (`Podovirus_Gp16`, Podovirus DNA encapsidation protein Gp16)
  - `Pfam:PF05894` (`Podovirus_Gp16`)

## Literature & Bioinformatic Synthesis
- **AAA+ Packaging Motor ATPase and DNA Translocase**: gp16 is the catalytic motor subunit of the *Bacillus phage phi29* DNA packaging machine (`PMID:18674782`; `PMID:23706809`; `file:BPPH2/16/16-uniprot.txt`). It belongs to the P-loop NTPase / AAA+ superfamily, containing canonical Walker A (`G27`), Walker B, arginine finger (`R146`), and sensor motifs in its N-terminal ATPase domain (`PMID:23706809`), linked to a C-terminal vestigial nuclease-like DNA-binding domain (`file:BPPH2/16/16-uniprot.txt`, `PMID:33089330`) that lacks endonuclease activity because phi29 replicates as unit-length terminal-protein (`gp3`)-linked monomers rather than concatemers.
- **pRNA-Dependent Prohead Recruitment (`GO:0003723`)**: Transient assembly of gp16 onto the procapsid portal vertex in the host cell cytoplasm (`GO:0030430`) strictly requires the prohead RNA (`pRNA`) ring anchored to the `gp10` connector (`PMID:18674782`). Ribonuclease footprinting and mutagenesis (`PMID:18674782`) showed that gp16 binds specifically to the A-helix of pRNA, protecting the CCA bulge (residues 18–20).
- **Chemomechanical Coupling (`GO:0016887`, `GO:0015616`, `GO:0019073`)**: Oligomeric gp16 couples ATP hydrolysis (`GO:0016887`, ~1 ATP hydrolyzed per 2 bp of dsDNA translocated) to power translocation of the unit-length viral dsDNA-gp3 complex (`GO:0015616` `DNA translocase activity`) into the procapsid (`GO:0019073` `viral DNA genome packaging`) against high internal pressure, after which gp16 and pRNA dissociate from the filled head (`PMID:18674782`; `PMID:23706809`; `file:BPPH2/16/16-uniprot.txt`).

## Annotation Review Summary
- `GO:0000166` (`nucleotide binding`, IEA, `GO_REF:0000043`): `TOO_GENERAL`. Entailed by `GO:0005524` (`ATP binding`) and `GO:0016887` (`ATP hydrolysis activity`).
- `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043`): `ACCEPT`. gp16 binds viral dsDNA via both its central channel loops and C-terminal domain during packaging (`PMID:23706809`; `file:BPPH2/16/16-uniprot.txt`).
- `GO:0003723` (`RNA binding`, IDA `PMID:18674782`, IEA `GO_REF:0000043`): `ACCEPT` both rows. Directly binds the CCA bulge of the pRNA A-helix (`PMID:18674782`).
- `GO:0005524` (`ATP binding`, IEA, `GO_REF:0000043`): `KEEP_AS_NON_CORE`. Substrate binding step of `GO:0016887` (`ATP hydrolysis activity`).
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043`): `TOO_GENERAL`. Entailed by `GO:0016887` (`ATP hydrolysis activity`).
- `GO:0016887` (`ATP hydrolysis activity`, IDA `PMID:23706809`, IEA `GO_REF:0000116`): `ACCEPT` both rows. Core catalytic activity powering DNA translocation (`PMID:23706809`).
- `GO:0019073` (`viral DNA genome packaging`, IDA, `PMID:18674782`): `ACCEPT`. Core biological process mediated by gp16 (`PMID:18674782`).
