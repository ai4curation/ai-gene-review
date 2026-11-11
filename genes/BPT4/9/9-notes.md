# Gene 9 (gp9) Curation Notes — Bacteriophage T4 (P10927)

## Overview
- **Gene symbol**: `9` (encodes baseplate protein gp9)
- **UniProt accession**: `P10927`
- **Organism**: *Tequatrovirus T4* (Bacteriophage T4; `NCBITaxon:10665`)

## Biological Role and Architecture
- **Long tail fiber socket and mechanotransducer**: gp9 (288 aa, ~31 kDa) forms a homotrimer (6 trimers = 18 copies per baseplate) localized at the upper peripheral rim of the baseplate (`file:BPT4/9/9-uniprot.txt`; `file:BPT4/9/9-deep-research-falcon.md`).
- **Domain organization and interactions**: Each gp9 trimer consists of an N-terminal coiled-coil domain that binds the proximal end (gp34 trimer) of a long tail fiber (LTF), a middle domain, and a C-terminal 8-stranded antiparallel beta-barrel domain that docks onto Domain III of gp7 at the periphery of the baseplate wedge (`file:BPT4/9/9-uniprot.txt`; `file:BPT4/9/9-deep-research-falcon.md`, PubMed 27193680).
- **Role in baseplate stabilization and triggering**: During morphogenesis, gp9 attaches after the छह wedges circularize around the hub and helps stabilize the metastable dome-shaped conformation of the baseplate (`file:BPT4/9/9-deep-research-falcon.md`). Upon reversible binding of the LTFs to host surface receptors, mechanical tension is transmitted through the swiveling gp9 socket to gp7 and the baseplate wedge network, initiating the dome-to-star transition that deploys the short tail fibers and triggers tail sheath contraction (`file:BPT4/9/9-uniprot.txt`; `file:BPT4/9/9-deep-research-falcon.md`, PubMed 27193680).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0098003` (`viral tail assembly`, IEA): Attaches to the assembled baseplate periphery to stabilize the dome-shaped baseplate and anchor the six long tail fibers.
  - `GO:0098025` (`virus tail, baseplate`, IEA/IDA): Directly resolved at the peripheral rim of the baseplate by X-ray crystallography and atomic cryo-EM (PubMed 27193680).
- **MODIFY**:
  - `GO:0098015` (`virus tail`, IEA) -> `GO:0098025` (`virus tail, baseplate`).
- **REMOVE**:
  - `GO:0019076` (`viral release from host cell`, IEA `GO_REF:0000002`): False InterPro2GO mapping. gp9 is a virion baseplate socket protein that anchors the long tail fibers and transmits the host-attachment signal to trigger tail contraction during viral entry, not host cell lysis or viral release.
