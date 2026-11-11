# Gene 10 (Baseplate wedge protein gp10) - Research Notes

## Overview
- **Gene symbol**: `10` (gp10)
- **UniProt ID**: `P10928`
- **Organism**: Bacteriophage T4 (`NCBITaxon:10665`, Tequatrovirus T4)
- **Length**: 602 amino acids (~66.2 kDa monomer)

## Biological Function & Architecture
- **Peripheral Baseplate Pin and Mechanical Lever**: gp10 is the first protein incorporated into the sequential assembly pathway of the six outer baseplate wedges (`gp10 -> gp7 -> gp8 -> gp6 -> gp53 -> gp25`), followed by attachment of gp11 and gp12. Six homotrimers of gp10 (18 copies per virion) form the peripheral pins at the vertices of the baseplate dome.
- **Four-Domain Non-Collinear Homotrimer**: Structural analyses (PubMed 16554069; PubMed 27193680) show that gp10 is organized into four distinct domains (domains I–IV), each forming a local homotrimer whose symmetry axes are non-collinear. It is stabilized by Unusual inter- and intra-complex disulfide bonds: one gp10 protomer forms an inter-chain disulfide bond (`Cys444` of gp10 to `Cys479` of gp7), while the remaining two gp10 protomers form an inter-chain disulfide bond with each other (`Cys444`–`Cys444`) (PubMed 19896486; PubMed 27193680).
- **Coupling Baseplate Reconfiguration to Short Tail Fiber Deployment**: In the pre-attachment dome-shaped baseplate, gp10 binds the N-terminal attachment region of the gp12 short tail fiber (STF) trimer (via domain IV) and binds the gp11 adaptor trimer (via domain III), holding the STFs folded beneath the baseplate. Upon host recognition by the long tail fibers, gp10 rotates by ~100° about its long axis (with domain IV rotating ~60°), acting as a mechanical lever that unfolds the gp12 short tail fibers downward to bind irreversibly to host cell surface lipopolysaccharide (LPS) during the dome-to-star transition.

## Annotation Assessment Notes
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from ARBA `GO_REF:0000120`): Core localization (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): True but overly broad compared to `GO:0098025` (`virus tail, baseplate`) (`MODIFY`).
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Core biological process (`ACCEPT`), as gp10 initiates assembly of the baseplate outer wedge and recruits gp7, gp11, and gp12.
- `GO:0019076` (`viral release from host cell`, IEA from `GO_REF:0000002` via InterPro `IPR008987` `Baseplate_struct_prot_Gp9/10_N`): False positive automated mapping (`REMOVE`). gp10 is a virion baseplate structural protein that functions in tail assembly and host attachment/entry conformational switching, not in host cell lysis or viral egress.
