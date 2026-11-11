# Bacteriophage T4 Gene 48 (gp48) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `48` encodes the baseplate tail-tube junction protein gp48 (UniProt `P13339`, 364 amino acids, ~39.7 kDa). Together with gp54, gp48 forms the structural adaptor and tube-initiation platform at the apex of the baseplate central hub dome, constituting the first hexameric annulus of the tail tube assembly immediately above the `(gp27)3` central hub cylinder (PubMed 27193680).

## Structural Organization and Role in Tail Morphogenesis
- **Tube Initiator Platform**: During baseplate assembly, after the six peripheral wedges circularize around the central `(gp5–gp27)3` hub, six copies of gp48 assemble as a homohexameric ring atop the pseudo-six-fold upper surface of the `(gp27)3` hub cylinder and contact the surrounding inner baseplate proteins gp6, gp25, and gp53 (PubMed 27193680).
- **Coupling to gp54 and gp19**: The gp48 hexamer provides the specific binding surface for the gp54 homohexamer (the second tube annulus), which in turn nucleates polymerization of the 24 hexameric rings of the major tail tube protein gp19 around the tape measure protein gp29. Without gp48 addition, neither gp54 nor gp19 can polymerize onto the baseplate.

## Annotation Review Notes
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Directly supported by structural and classical morphogenesis evidence showing that gp48 forms the first tail-tube initiator ring required for gp54 binding and subsequent gp19 tail tube polymerization (`ACCEPT`).
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000043`): Directly supported by the atomic-resolution cryo-EM structure of the T4 baseplate resolving the gp48 hexameric ring at the baseplate–tail tube junction (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): Overly general parent term superseded by `GO:0098025` (`virus tail, baseplate`) (`MODIFY` -> `GO:0098025`).
