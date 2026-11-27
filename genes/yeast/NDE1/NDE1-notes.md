# NDE1 (YMR145C, UniProt P40215) notes

Module: `oxphos` (external NDH-2, ndh2_external_activity). Absent from YeastCyc PWY3O-188 gene list.

## Evidence journal
- Major external NADH dehydrogenase: nde1 3-fold lower mitochondrial NADH oxidation; nde1 nde2 abolishes it [PMID:9733747 "NADH-dependent mitochondrial respiration was completely abolished in an nde1Delta nde2Delta double mutant."].
- Same conclusion with gene named NDH1 [PMID:9696750 "Thus, Ndh1p appears to be a mitochondrial dehydrogenase capable of using exogenous NADH."]; nde1 slows growth on non-fermentable carbon incl. ethanol.
- Location: IMS [UniProt:P40215]; part of a supercomplex of IMS-facing dehydrogenases [PMID:11502169 "two external NADH-dehydrogenases Nde1p and Nde2p"].
- Second topomer spans outer membrane, cytosol-exposed, triggers death [PMID:31668496 "The surface-exposed topomer triggers cell death in response to pro-apoptotic stimuli."].
- nde1 nde2 chemostat glucose metabolism remains respiratory [PMID:9733747 "Glucose metabolism in aerobic, glucose-limited chemostat cultures (D = 0.10 h-1) of an nde1Delta nde2Delta mutant was essentially respiratory."] -> "pyruvate fermentation to ethanol" IMP rows are indirect; MARK_AS_OVER_ANNOTATED.

## Curation decisions
- Core MF GO:0120555, BP GO:0006120 (added as NEW, IMP PMID:9733747; GOA has it for NDI1 only), CC inner membrane (IMS face).
- Apoptosis regulation kept as non-core (topomer-specific moonlighting).
