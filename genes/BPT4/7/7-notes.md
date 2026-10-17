# Gene 7 (gp7) Curation Notes — Bacteriophage T4 (P19061)

## Overview
- **Gene symbol**: `7` (encodes baseplate wedge protein gp7)
- **UniProt accession**: `P19061`
- **Organism**: *Tequatrovirus T4* (Bacteriophage T4; `NCBITaxon:10665`)

## Biological Role and Architecture
- **Structural backbone of the baseplate wedge**: gp7 is the largest polypeptide of the baseplate wedge (1032 aa, ~119 kDa), present in 6 copies per virion (one monomer per wedge) (`file:BPT4/7/7-uniprot.txt`; `file:BPT4/7/7-deep-research-falcon.md`).
- **Ordered wedge assembly**: Wedge morphogenesis initiates when a gp7 monomer binds to a gp10 homotrimer (`(gp10)3-gp7`), inducing a conformational stretch in a flexible linker of gp7. This stretched linker is subsequently stabilized by a gp8 homodimer, which allows two copies of gp6 to bind and form the `(gp6)2-gp7` heterotrimeric core module (connected via a triple-helical bundle), followed by incorporation of gp53 and gp25 (`file:BPT4/7/7-uniprot.txt`; `file:BPT4/7/7-deep-research-falcon.md`, PubMed 27193680).
- **Inter-protein disulfide linkage and mechanotransduction**: Uniquely in the T4 baseplate, one subunit of the gp10 trimer is covalently linked via a disulfide bond to gp7 (while the other two gp10 subunits form an intra-trimer disulfide bond), anchoring the peripheral tail-fiber network (gp9, gp10, gp11, gp12) to the inner `gp25-(gp6)2-gp7` sheath-triggering module during the dome-to-star conformational transition (`file:BPT4/7/7-uniprot.txt`; `file:BPT4/7/7-deep-research-falcon.md`, PubMed 27193680).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0098003` (`viral tail assembly`, IEA): Essential wedge initiator and scaffold protein required for sequential assembly of the six baseplate wedges.
  - `GO:0098025` (`virus tail, baseplate`, IEA/IDA): Directly resolved as the multi-domain structural backbone spanning the peripheral and inner regions of each baseplate wedge by cryo-EM (PubMed 27193680).
- **MODIFY**:
  - `GO:0098015` (`virus tail`, IEA) -> `GO:0098025` (`virus tail, baseplate`).
