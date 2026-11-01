# Bacteriophage T4 Gene 54 (gp54) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `54` encodes the baseplate tail-tube junction protein gp54 (UniProt `P13341`, 320 amino acids, ~35.0 kDa). Together with gp48, gp54 forms the homohexameric adaptor rings at the top of the baseplate dome that link the central spike/hub complex (`(gp5–gp27)3`) to the major tail tube (`gp19`). Specifically, the gp54 homohexamer forms the second annulus of the tail-tube continuation (directly atop the gp48 first annulus) and directly initiates polymerization of the 24 hexameric rings of gp19 (PubMed 27193680).

## Structural Organization and Role in Tail Morphogenesis
- **Tube Initiation Platform**: During late baseplate morphogenesis, binding of the gp48 hexamer to the top of the baseplate dome is followed by addition of the gp54 hexamer. In association with the hub-anchored tape measure protein gp29, the gp54 hexameric ring exposes a tail-tube-like beta-barrel fold interface that nucleates polymerization of 144 monomers (24 hexameric rings) of gp19 to form the tail tube (PubMed 27193680).
- **Sheath and Tube Contacts**: In addition to binding gp48 below and the first ring of gp19 above, gp54 interacts with the first (proximal) ring of the gp18 contractile tail sheath in the extended tail state.

## Annotation Review Notes
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Directly supported by structural and morphogenesis studies demonstrating that addition of the gp54 hexamer completes the baseplate dome and directly initiates gp19 tail-tube polymerization (`ACCEPT`).
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000043`): Directly supported by atomic cryo-EM reconstructions of the 6-MDa T4 baseplate resolving the gp54 homohexameric ring at the baseplate–tail tube junction (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): Overly general parent term superseded by `GO:0098025` (`virus tail, baseplate`) (`MODIFY` -> `GO:0098025`).
