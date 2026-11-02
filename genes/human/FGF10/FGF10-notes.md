# FGF10 (KGF-2) curation notes: human, UniProt O15520

## Identity
- Fibroblast growth factor 10 / keratinocyte growth factor 2; FGF7 subfamily (FGF3, FGF7, FGF10, FGF22). PANTHER PTHR11486.
- UniProt: signal peptide 1-37, chain 38-208, predicted N-glycosylation at 51 and 196; "SUBCELLULAR LOCATION: Secreted" [file:human/FGF10/FGF10-uniprot.txt]
- UniProt function: "normal branching morphogenesis. May play a role in wound healing." Subunit: "Interacts with FGFR1 and FGFR2. Interacts with FGFBP1." [file:human/FGF10/FGF10-uniprot.txt]
- Disease: ALSG (MIM 180920) and LADD3 (MIM 620193), both from heterozygous loss-of-function variants [file:human/FGF10/FGF10-uniprot.txt].

## Core biology (with provenance)
- Receptor specificity: "FGF7 and FGF10 activate only the b isoform of FGFR2 (FGFR2b)." Crystal structure FGF10-FGFR2b; "Structure-based mutagenesis of FGF10 confirms the importance of the observed contacts for FGF10 biological activity." [PMID:12591959]
- FGFR1b as well: UniProt lists FGFR1 as partner (citing PMID:16597617, BaF3 mitogenesis survey; cached abstract does not state FGF10 specifics). Deep research: "FGF10 signals predominantly through FGFR2b, the epithelial IgIIIb splice isoform of fibroblast growth factor receptor 2" [file:human/FGF10/FGF10-deep-research-falcon.md].
- Paracrine, fibroblast-derived: "fibroblasts of the human lamina propria were the cell type that synthesized FGF-10 RNA"; "Recombinant (r) preparations of human FGF-10 were found to induce proliferation of human urothelial cells in vitro"; signalling "begins with the heparin-dependent phosphorylation of tyrosine residues of surface transmembrane receptors" [PMID:11923311]
- "Synthesis of FGF-10 was restricted to mesenchymal fibroblasts, and secreted FGF-10 exhibited paracrine transport to two proximal sites" [PMID:16597614]
- Heparan sulfate: "surface plasmon resonance (SPR) analysis showed that FGF10 and the FGF10-FGFR2b complex bound to purified perlecan HS"; "heparanase releases FGF10 from perlecan HS in the basement membrane, increasing MAPK signaling, epithelial clefting, and lateral branch formation" [PMID:17959718]
- Dermatan sulfate potentiates FGF10 on FGFR2IIIb cells and keratinocyte migration [PMID:19152659]; FGFBP1: "FGF-BP interacts with FGF-7, FGF-10, and with the recently identified FGF-22, and enhances the activity of low concentrations of ligand" [PMID:15806171]
- Lung chemoattractant: "FGF-10 exerts a powerful chemoattractant effect on the distal but not on proximal lung epithelium." "Epithelial buds grow toward an FGF-10 source within 24 h" [PMID:9740653]
- Pancreas: "human embryonic pancreatic mesenchyme expresses FGF7 and FGF10 that act on epithelial cells to activate their proliferation" [PMID:15690149]
- MAPK: "FGF-10 upregulates (short-term) the Na,K-ATPase activity in AEC via the Grb2-SOS/Ras/MAPK pathway" [PMID:12804770]; ERK via Grb2-SOS/Ras/RAF-1 [PMID:14975937]
- Human genetics: ALSG missense "R80S and G138E" [PMID:17213838]; "changed FGF10 signaling due to haploinsufficiency during development results in ALSG" [PMID:19102732]
- Lung saccular stage: "(FGF-10) is required for saccular lung development"; TLR2/4 activation "inhibited FGF-10 expression" [PMID:17071719]

## Decisions / problem annotations
- Cytoplasm IBA (PTN000160075, family root): REMOVE, as for FGF7; signal-peptide-bearing secreted ligand. Added propagation_review.
- Nucleus IDA x3 (Bassuk lab; recombinant FGF10 in urothelial cells [PMID:11923311, PMID:16597614, PMID:17471512]): experimental, kept as NON_CORE (not removed). Authors note FGF10 "has been identified inside urothelial cells, despite its acknowledged role as an extracellular signaling ligand" [PMID:17471512].
- Plasma membrane IDA -> MODIFY to cell surface (ligand is bound on outer face via FGFR2b/HSPG).
- protein binding: FGFR2 structure paper -> MODIFY to GO:0005111; PLA screen and HuRI Y2H (SREK1IP1, THAP1) -> REMOVE (uninformative).
- "epithelial cell proliferation" / "urothelial cell proliferation" (process itself) -> MODIFY to positive regulation terms; ERK1/2 cascade -> MODIFY to positive regulation of ERK1/2 cascade (GO:0070374).
- Positive regulation of lymphocyte proliferation (PMID:19152659): abstract says "proliferation of cell lines expressing FGF receptor-2-IIIb" - likely BaF3 reporter cells, but full text (PMC2721336) could not be fetched (Europe PMC 500, NCBI 429) -> UNDECIDED.
- Tear secretion / regulation of saliva secretion (IMP, ALSG): secondary to gland aplasia -> MARK_AS_OVER_ANNOTATED; salivary and lacrimal gland development ACCEPT.
- Positive regulation of DNA repair: authors only "suggesting a role for DNA repair" [PMID:14975937] -> MARK_AS_OVER_ANNOTATED.
- Response to estradiol / LPS (rat IEA), angiogenesis (rat IEA), mesonephros (IEP), transcription (mouse IEA): MARK_AS_OVER_ANNOTATED.
- Radial glial differentiation (ISS/IEA from mouse) and neurogenesis IBA: KEEP_AS_NON_CORE (mouse Fgf10 cortical role; not verified in human, no PMID cached).
- No NEW annotations proposed. Heparin binding already present (IDA). Type 1 FGFR binding (FGFR1b) raised as a question only.

## Module relevance (fgfr_signaling)
- Module uses GO:0005104 for the paracrine ligand; FGF10 carries GO:0005104 (IDA, accepted) and the more specific GO:0005111 (IBA + IPI + structure). GO:0005111 chosen as core MF, consistent with FGF7.
- FGF10 also activates FGFR1b, so GO:0005104 remains correct at the module's level of generality.
