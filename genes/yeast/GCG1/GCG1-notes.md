# GCG1 (YER163C, UniProt P32656) notes

- ChaC-family glutathione-specific gamma-glutamylcyclotransferase. "the ChaC family of proteins function as γ-glutamyl cyclotransferases acting specifically to degrade glutathione but not other γ-glutamyl peptides" [PMID:23070364]. Cached paper is abstract-only; yeast-specific data (GCG1 = YER163C) are summarised in UniProt.
- UniProt: "Catalyzes the cleavage of glutathione into 5-oxo-L-proline"; "Acts specifically on glutathione, but not on other gamma-glutamyl peptides."; Reaction "glutathione = L-cysteinylglycine + 5-oxo-L-proline" EC 4.3.2.7; KM 1.52 mM for glutathione [UniProt:P32656].
- Overexpression (not E>Q mutants) "led to glutathione depletion and enhanced apoptosis in yeast" [PMID:23070364].
- Localization: "SUBCELLULAR LOCATION: Cytoplasm ... Nucleus" (Huh GFP) [UniProt:P32656].

## Pathway
- Module glutathione_synthesis_gamma_glutamyl_cycle: GCG1 exemplar for GO:0061928 in cytosol. Agrees.
- YeastCyc: PWY3O-114 / PWYQT-4432 (glutathione degradation) list only ECM38 (GGT) and DUG1; neither GCG1 (ChaC route) nor the Dug2/Dug3 route nor OXP1 are attached to reactions. YeastCyc comment still states gamma-glutamyl cyclotransferase and 5-oxoprolinase are "still in question" - outdated since 2010/2012 (PMID:20402795, PMID:23070364).
- GO:0003839 (generic GGCT acting on gamma-glutamyl amino acids) IDA annotation conflicts with the reported specificity; GO:0061928 is correct.
