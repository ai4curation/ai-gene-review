# Gene 25 (Baseplate wedge protein gp25) - Research Notes

## Overview
- **Gene symbol**: `25` (gp25)
- **UniProt ID**: `P09425`
- **Organism**: Bacteriophage T4 (`NCBITaxon:10665`, Tequatrovirus T4)
- **Length**: 132 amino acids (~15.1 kDa monomer)

## Biological Function & Architecture
- **Inner Baseplate Wedge Protein & Contractile Sheath Initiator**: gp25 is the final subunit added during the sequential assembly of the six outer baseplate wedges (`gp10 -> gp7 -> gp8 -> gp6 -> gp53 -> gp25`), present in 6 copies per baseplate (one monomer per wedge, forming a hexameric ring around the gp54/gp19 central tail tube initiator at the baseplate-sheath junction) (PubMed 27193680).Note that although purified recombinant gp25 can form homodimers in solution, within the assembled baseplate six copies of gp25 sit at the inner rim of the six wedges, interacting directly with gp53 and the `(gp6)2-gp7` heterotrimeric trifurcation module.
- **Structural Homology to the Tail Sheath Handshake Domain & Evolutionary Conservation**: Structural and comparative genomic analyses demonstrate that gp25 adopts an alpha/beta fold homologous to domain IV (the C-terminal polymerization/handshake domain) of the contractile tail sheath protein gp18. During tail morphogenesis, the six gp25 subunits accept the N-terminal and C-terminal beta-strand arms from the first ring of six gp18 sheath subunits (alongside beta-strands contributed by gp6), nucleating polymerization of the 24-ring contractile sheath in its high-energy extended conformation and transmitting the baseplate dome-to-star conformational wave that triggers sheath contraction (PubMed 27193680). This gp25-like wedge/sheath-initiator fold (`IPR007048` / `PF04965`) is universally conserved across contractile injection systems, including bacterial Type VI secretion systems (T6SS `TssE` / `HsiF`) and R-type pyocins.

## Annotation Assessment Notes
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000043`): Core cellular component (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): True but overly general relative to `GO:0098025` (`virus tail, baseplate`) (`MODIFY`).
- In `core_functions`, gp25's structural role (`GO:0005198` `structural molecule activity`) in the `GO:0098025` (`virus tail, baseplate`) directly involved in `GO:0098003` (`viral tail assembly`) captures its function as the inner baseplate wedge subunit and contractile sheath assembly initiator.
