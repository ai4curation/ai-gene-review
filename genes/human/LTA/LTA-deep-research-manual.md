# LTA manual literature synthesis

Perplexity deep research was unavailable in this workspace, so this file records a manual synthesis from cached primary papers, Reactome events, UniProt, and the existing PTHR11471 family review.

## Core biology

LTA encodes lymphotoxin-alpha, historically TNF-beta, a TNF-superfamily cytokine. Like TNF, soluble LT-alpha homotrimers bind TNFRSF1A/TNFR1 and TNFRSF1B/TNFR2: PMID:3001529 reports that "the binding of labelled TNF-alpha to these cells can be inhibited by both TNF-alpha and TNF-beta but not by gamma-interferon" when characterizing high-affinity human TNF receptors on ME-180 cells.

LTA also contributes the alpha subunit of the membrane lymphotoxin heterotrimer LT-alpha1-beta2. The 2013 LTBR structural paper states that "LTalpha1beta2 possesses two binding sites for LTbetaR with distinct affinities and that dimerization of LTbetaR by LTalpha1beta2 is necessary and sufficient for signal transduction" [PMID:24248355]. This is the key primary evidence for LTA in `GO:0002947` tumor necrosis factor receptor superfamily complex and for the membrane LTBR-binding branch shared with LTB.

Soluble LT-alpha can bind TNFRSF14/HVEM. The LIGHT discovery paper reports that "HVEM binds two cellular ligands, secreted lymphotoxin alpha (LTalpha) and LIGHT" [PMID:9462508].

The existing PTHR11471 family review treats the broad parent TNF-superfamily terms as family-wide but keeps receptor-specific and apoptosis/death-domain signaling terms subfamily-specific. LTA belongs to SF31 and shares TNFR1/TNFR2 signaling with TNF, while LT-alpha1-beta2 signals through LTBR with LTB.

