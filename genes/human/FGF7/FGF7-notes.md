# FGF7 (KGF) curation notes — human, UniProt P21781

## Identity
- Fibroblast growth factor 7 / keratinocyte growth factor (KGF); FGF7 subfamily (FGF3, FGF7, FGF10, FGF22).
- UniProt: signal peptide 1-31, mature chain 32-194, N-glycosylation at 45; "SUBCELLULAR LOCATION: Secreted." [file:human/FGF7/FGF7-uniprot.txt]
- Isoform 2 (VSP_055090) truncates residues 96-194; no functional data found.

## Core biology (with provenance)
- Discovered as a stromal/fibroblast-derived epithelial mitogen: "A growth factor specific for epithelial cells was identified in conditioned medium of a human embryonic lung fibroblast cell line." [PMID:2915979]; "Lack of mitogenic activity on either fibroblasts or endothelial cells indicated that KGF possessed a target cell specificity distinct from any previously characterized growth factor." [PMID:2915979]
- Purified by "heparin-Sepharose affinity chromatography" [PMID:2915979] — i.e. the protein itself binds heparin.
- Paracrine: "The KGF transcript was present in stromal cells derived from epithelial tissues." [PMID:2475908]
- Receptor: FGFR2 IIIb splice isoform (KGFR). "Binding assays demonstrated that the KGFR was a high-affinity receptor for both KGF and acidic FGF, while FGFR-2 showed high affinity for basic and acidic FGF but no detectable binding by KGF." [PMID:1309608]; "The KGFR transcript was specific to epithelial cells" [PMID:1309608]
- Receptor-specificity surveys in BaF3 cells [PMID:8663044; PMID:16597617] (abstract only; UniProt cites both for FGFR2 interaction / proliferation).
- FGFBP1 binds FGF7 and enhances low-dose activity: "we demonstrate that FGF-BP interacts with FGF-7, FGF-10, and with the recently identified FGF-22, and enhances the activity of low concentrations of ligand." [PMID:15806171]
- Keratinocyte migration: "KGF induces keratinocyte motility and cytoskeletal rearrangement" and "siRNA-mediated downregulation of cortactin inhibited KGF- and FGF10-induced migration." [PMID:17449030]
- Human embryonic pancreas: "human embryonic pancreatic mesenchyme expresses FGF7 and FGF10 that act on epithelial cells to activate their proliferation" [PMID:15690149]
- Lung: "FGF-10, in contrast to FGF-7, is a modest proliferation factor for the lung epithelium" [PMID:9740653]; fetal lung liquid secretion [PMID:10541313].
- Wound/skin (dominant-negative KGFR; blocks all FGFR2b ligands, not FGF7-specific): "inhibition of KGF receptor signaling reduced the proliferation rate of epidermal keratinocytes at the wound edge, resulting in substantially delayed reepithelialization of the wound." [PMID:7973639]
- Brain (mouse): FGF7 is a target-derived presynaptic organizer for inhibitory synapses in CA3: "in hippocampal neurons, FGF22 and FGF7 are specifically localized at glutamatergic and GABAergic synapses, respectively" and "FGF7KO mice are prone to epileptic seizures" [PMID:20505669]. Source of the Ensembl IEA synapse terms.
- Mouse lung: Elf5 "was induced by FGF7 and FGF10, ligands that primarily bind FGFR2b" [PMID:17394208] — source of the IEA "positive regulation of DNA-templated transcription"; indirect downstream effect.
- Deep research (falcon; reviews, no PMIDs) summarises signalling via FRS2-GRB2-SOS-RAS-ERK, PI3K-AKT, PLCgamma; Fgf7-null lungs are histologically normal (redundancy with FGF10); clinical palifermin (truncated rFGF7) for oral mucositis. [file:human/FGF7/FGF7-deep-research-falcon.md]

## Problem annotations
- GO:0010463 mesenchymal cell proliferation (IDA, UniProt) cites PMID:11023837, an alpha2-macroglobulin/glycodelin (PP14) paper. Neither the abstract nor the Europe PMC MeSH headings mention FGF7/KGF/FGF; the PMC full text could not be retrieved (Europe PMC 500 error; not in BioC OA subset). Likely a wrong PMID but we cannot see what the curator saw. Biologically, FGF7 lacks activity on fibroblasts [PMID:2915979]. -> UNDECIDED, flag for UniProt.
- GO:0005737 cytoplasm IBA (is_active_in) from whole-family node PTN000160075 — driven by intracellular FGFs / non-signal-peptide FGF1/FGF2. FGF7 has a cleaved signal peptide and acts extracellularly. Mouse Fgf7 has no experimental cytoplasm annotation (QuickGO check of P36363). -> REMOVE.
- GO:0022008 neurogenesis IBA (family root) — FGF7's neural role is synapse organization, not generation of neurons. -> MARK_AS_OVER_ANNOTATED.
- GO:0034394 protein localization to cell surface — cortactin membrane translocation downstream of receptor; cortactin is cortical/cytoplasmic, not cell-surface. -> MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding with FGFR2 IIIb (P21802-3) -> MODIFY to GO:0005111 type 2 FGF receptor binding.

## Module relevance (fgfr_signaling)
- Module annoton uses GO:0005104 FGFR binding for the paracrine ligand; for FGF7 the IBA-supported, more specific child GO:0005111 (type 2 FGFR binding) is correct and consistent with the module's "selective for FGFR2 IIIb" description.
- Heparin binding (GO:0008201) is not in human GOA (only rat/mouse ISO); proposed NEW with PMID:2915979 heparin-Sepharose purification evidence.
