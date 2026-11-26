# INM1 (YHR046C, P38710) notes

- Inositol monophosphatase, Li+/Na+-sensitive [PMID:10096091 "The two recombinant purified proteins were shown to catalyse inositol-1-phosphate hydrolysis sensitive to lithium and sodium."]; [PMID:10844654 "The purified protein has inositol monophosphatase activity that is inhibited by the antibipolar drug lithium, but not valproate."].
- Redundant with INM2 [PMID:10096091 "A double gene disruption had no apparent growth defect and was not auxotroph for inositol."]; [PMID:10844654 "In the inm1Delta:URA3 null mutant, inositol monophosphatase activity was reduced but not eliminated."].
- Double mutant raises IP1, lowers IP3 [PMID:12593845 "a double null mutation imp1 imp2 causes increased levels of inositol monophosphates and reduced level of inositol 1,4,5-trisphosphate"].
- Pathway: step 2/2 of myo-inositol synthesis from G6P [UniProt:P38710 "PATHWAY: Polyol metabolism; myo-inositol biosynthesis"]. Physiological substrate from INO1 is 1D-myo-inositol 3-phosphate; experiments used inositol-1-phosphate. Core MF chosen as generic GO:0052834 (EC 3.1.3.25) to cover both.
- Cytoplasm + nucleus (GFP) [UniProt:P38710 "SUBCELLULAR LOCATION: Cytoplasm ... Nucleus"].

## Curation decisions
- "phosphatidylinositol dephosphorylation" IEA from InterPro IPR020550 REMOVED (IMPase acts on soluble IP1, not lipids). Same for INM2.
- "signal transduction" IBA (human IMPA1 donor) marked over-annotated.
