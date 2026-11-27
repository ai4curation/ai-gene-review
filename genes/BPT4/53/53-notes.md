# Bacteriophage T4 Gene 53 (gp53) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `53` encodes the inner baseplate wedge protein gp53 (UniProt `P16011`, 196 amino acids, ~22.9 kDa). Present in six copies per virion (one per baseplate wedge), gp53 is the fifth protein added in the sequential assembly pathway of the baseplate wedge (`gp10 -> gp7 -> gp8 -> gp6 -> gp53 -> gp25`) and plays a critical structural role as a "bundle clamp" and "sheath platform" that drives wedge circularization around the central hub (PubMed 27193680).

## Structural Organization and Role in Baseplate Assembly and Contraction
- **Wedge Circularization Clamp**: In the atomic structure of the 6-MDa T4 baseplate (PubMed 27193680), gp53 binds at the inter-wedge interface to the helical bundle formed by the two copies of gp6 and one copy of gp7 (`(gp6)2–gp7` heterotrimer), clamping neighboring wedges together to promote their association into a six-fold symmetric ring and recruiting the sheath-initiator subunit gp25.
- **Sheath Platform**: Together with gp25 and gp48/gp54, gp53 forms part of the upper inner baseplate platform near the tail tube that interfaces with the proximal ring of the gp18 contractile sheath and relays the conformational signal from the peripheral wedges during the dome-to-star transition that triggers sheath contraction (PubMed 27193680).

## Annotation Review Notes
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Directly supported by biochemical reconstitution and structural studies showing gp53 is required to clamp `(gp6)2–gp7` wedge bundles, recruit gp25, and circularize the six wedges into the baseplate (`ACCEPT`).
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000043`): Directly supported by atomic-resolution cryo-EM reconstructions of the T4 baseplate resolving six copies of gp53 in the inner baseplate wedge core (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): Overly general parent term superseded by `GO:0098025` (`virus tail, baseplate`) (`MODIFY` -> `GO:0098025`).
