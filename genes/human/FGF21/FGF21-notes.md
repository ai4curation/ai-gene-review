# FGF21 (human, Q9NSA1) curation notes

## Identity
- 209 aa precursor, signal peptide 1-28; beta-trefoil FGF core plus disordered C-terminal tail (UniProt).
- Endocrine FGF19 subfamily (FGF19, FGF21, FGF23). Discovery: [PMID:10858549 "which is a typical signal sequence, and appears to be a secreted protein"]; mainly liver expressed.
- Hepatic, fasting/PPARalpha-induced circulating hormone [PMID:17550778 "Hepatic expression and circulating levels of FGF21 are induced by both KD and fasting"].

## Receptor mechanism (core MF)
- beta-Klotho (KLB) required: [PMID:17452648 "BetaKlotho physically interacts with FGF receptors 1c and 4, thereby increasing the ability of these FGF receptors to bind FGF21 and activate the MAP kinase cascade."]
- Reconstitution: [PMID:18187602 "FGF21 alone does not activate FGFRs and that betaKlotho is required for FGF21 to activate two specific FGFR subtypes: FGFR1c and FGFR3c"]
- Bipartite binding: [PMID:19117008 "the C-terminus is important for betaKlotho interaction whereas the N-terminus likely interacts directly with FGF receptors"]; [PMID:19059246 "FGF21 binds directly to beta-Klotho through its C-terminus."]
- Structure: [PMID:29342135 "In this model, β-Klotho functions as a primary high affinity receptor for FGF21, whereas FGFR1c functions as a catalytic subunit that mediates receptor dimerization and intracellular signaling."]; "FGF21 binds with high affinity, KD = 43.5 nM".
- Tissue selectivity: FGF21 signals in WAT, not liver (FGFR4-dominant) [PMID:17623664 "FGF21, however, activated FGF signaling in white adipose tissue but not in liver"].

## Downstream physiology (non-core)
- Adipocyte glucose uptake via GLUT1 induction, slow and protein-synthesis dependent [PMID:15902306 "the predominant effect of FGF-21 on glucose uptake required at least 4 hours of cell treatment, and it was substantially diminished in the presence of cycloheximide"].
- Non-mitogenic [PMID:15902306 "FGF-21 appears to be mitogenically inactive in vitro when tested on several otherwise FGF-sensitive cell lines and primary cells"] -> basis for REMOVE of IBA proliferation and MODIFY of growth factor activity -> hormone activity (GO:0005179).
- CNS actions [PMID:23933984 "These effects are mediated through β-Klotho expression in the suprachiasmatic nucleus of the hypothalamus and the dorsal vagal complex of the hindbrain."]; [PMID:25130400 "FGF21 stimulates sympathetic nerve activity to brown adipose tissue through a mechanism that depends on the neuropeptide corticotropin-releasing factor."]
- Thermogenesis (mouse) [PMID:22302939 "mice deficient in FGF21 display an impaired ability to adapt to chronic cold exposure, with diminished browning of WAT"].
- LDLR/IDOL in cultured hepatocytes, single study [PMID:22378787 "Experiments using DiI-labeled LDL particles showed that FGF21 increased lipoprotein uptake"]; kept non-core.

## Decisions summary
- ACCEPT: FGFR binding (IBA, IEA), FGFR signaling pathway (IBA, IEA), extracellular region (x4), MAPK (IBA), ERK1/2 (IDA), cell-cell signaling (TAS).
- MODIFY: protein binding with KLB (x3) -> signaling receptor binding GO:0005102; growth factor activity (IBA, IEA) -> hormone activity GO:0005179; signal transduction TAS -> GO:0008543.
- REMOVE: HT Y2H protein binding (x9); cytoplasm IBA; positive regulation of cell population proliferation IBA; neurogenesis IBA; regulation of cell migration IBA. These IBA terms reflect paracrine/intracellular FGF biology from which the endocrine clade has diverged.
- KEEP_AS_NON_CORE: glucose import (IDA, IEA), cold-induced thermogenesis (IEA, ISS), LDL particle clearance (NAS).
- No NEW process terms proposed: metabolic outcomes (glucose homeostasis, lipid metabolism, ketogenesis) are carried out by the target-cell machinery; FGF21's contribution is the ligand activity already captured.

## Module relevance (fgfr_signaling)
- Module's use of GO:0005104 for the endocrine FGF ligand annoton is supported for FGF21; hormone activity (GO:0005179) would be a more informative additional ligand-side MF for the endocrine variant.
