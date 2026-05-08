# Wsc1 (S. pombe) - Research Notes

## Gene Overview

- UniProt: P87179
- Gene: wsc1 (SPBC30B4.01c)
- Organism: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
- Full name: Cell wall integrity and stress response component 1
- 374 AA, single-pass type I transmembrane protein with N-terminal signal peptide

## Domain Architecture

- **WSC domain** (aa 31-119): Cysteine-rich extracellular carbohydrate-binding domain. Binds cell wall polysaccharides and mediates mechanosensing [PMID:34666001 "Wsc1 accumulates to sites of enhanced mechanical stress through reduced lateral diffusivity, mediated by the binding of its extracellular WSC domain to CW polysaccharides"]
- **Ser/Thr-rich region** (aa ~132-236): Heavily O-mannosylated, disordered region that likely functions as a rigid rod-like spacer in the periplasm [PMID:15948957, O-mannosylation confirmed]
- **Transmembrane helix** (aa 293-313): Single-pass membrane anchor
- **Cytoplasmic tail** (aa 314-374): Short cytoplasmic domain; contains phosphoserine at Ser354 [PMID:18257517]
- InterPro: IPR002889 (WSC carbohydrate-binding domain), IPR051836 (Kremen receptor family)
- PANTHER: PTHR24269:SF16 (Protein SLG1 subfamily)

## Key Literature Findings

### PMID:23907979 - Cruz et al. 2013 (MicrobiologyOpen)
"The fission yeast cell wall stress sensor-like proteins Mtl2 and Wsc1 act by turning on the GTPase Rho1p but act independently of the cell wall integrity pathway."

Key findings for Wsc1:
1. Wsc1p-GFP localizes to patches at cell tips [PMID:23907979 "Wsc1p-GFP was concentrated in patches at the cell tips"]
2. Wsc1p interacts with Rho-GEF Rgf2p [PMID:23907979 "it interacted with the Rho-GEF Rgf2p"]
3. Overexpression activates cell wall biosynthesis [PMID:23907979 "its overexpression activated cell wall biosynthesis"]
4. Single deletion (wsc1-delta) is viable but double deletion with mtl2 is lethal [PMID:23907979 "Each gene could be deleted individually without affecting viability, but the deletion of both was lethal"]
5. Rescued by overexpression of Rho1 or its GEFs [PMID:23907979 "this phenotype was rescued by overexpression of the genes encoding either Rho1p or its GDP/GTP exchange factors (GEFs)"]
6. wsc1-delta shows low Rho1p-GTP under cell wall stress [PMID:23907979 "wsc1-delta and mtl2-delta cells showed a low level of Rho1p-GTP under cell wall stress"]
7. Two separate signaling branches: Wsc1->Rgf2->Rho1->glucan synthase (GS); Mtl2->Rho1->Pck1 [PMID:23907979 "signaling from Wsc1p and Rgf2p through Rho1p to activate glucan synthase (GS)"]
8. CRITICAL: MAPK Pmk1p pathway remains active in wsc1-delta, meaning Wsc1 acts INDEPENDENTLY of the canonical CWI MAPK pathway [PMID:23907979 "signaling through the mitogen-activated protein kinase (MAPK) Pmk1p remained active in mtl2-delta and wsc1-delta disruptants exposed to cell wall stress"]

### PMID:34666001 - Neeli-Venkata et al. 2021 (Dev Cell)
"Detection of surface forces by the cell-wall mechanosensor Wsc1 in yeast."

Key findings:
1. Wsc1 forms micrometer-sized clusters at sites of force application on cell wall [PMID:34666001 "we uncovered the formation of micrometer-sized clusters at sites of force application onto the CW"]
2. Clusters assemble within minutes of CW compression in dose-dependence with mechanical stress [PMID:34666001 "Clusters assembled within minutes of CW compression, in dose dependence with mechanical stress"]
3. Clusters disassemble upon relaxation [PMID:34666001 "disassembled upon relaxation"]
4. Clustering mechanism: reduced lateral diffusivity via WSC domain binding to CW polysaccharides [PMID:34666001 "Wsc1 accumulates to sites of enhanced mechanical stress through reduced lateral diffusivity, mediated by the binding of its extracellular WSC domain to CW polysaccharides"]
5. Clustering is independent of canonical polarity, trafficking, and downstream CW regulatory pathways [PMID:34666001 "independent of canonical polarity, trafficking, and downstream CW regulatory pathways"]
6. Wsc1 functions as an autonomous mechanosensing module [PMID:34666001 "Wsc1 may represent an autonomous module to detect and transduce local surface forces onto the CW"]

### PMID:29689193 - Davi et al. 2018 (Dev Cell)
"Mechanosensation Dynamically Coordinates Polar Growth and Cell Wall Assembly to Promote Cell Survival."

Key findings:
1. CW thickness at growing tips fluctuates with homeostatic feedback [PMID:29689193 "Thickness at growing tips exhibited a fluctuating behavior with thickening phases followed by thinning phases, indicative of a delayed feedback promoting thickness homeostasis"]
2. This feedback is mediated by mechanosensing through the CWI pathway [PMID:29689193 "This feedback was mediated by mechanosensing through the CW integrity pathway, which probes strain in the wall to adjust synthase localization and activity to surface growth"]
3. wsc1-delta mutants defective in thickness homeostasis lyse by wall rupture [PMID:29689193 "Mutants defective in thickness homeostasis lysed by rupturing the wall"]

### PMID:21832151 - Kashiwazaki et al. 2011 (Mol Biol Cell)
"Endocytosis is essential for dynamic translocation of a syntaxin 1 orthologue during fission yeast meiosis."

This is not a Wsc1-focused paper. Wsc1 (SPBC30B4.01c) appears in Table 3 as one of many PM proteins surveyed for their localization during meiosis. The paper confirmed Wsc1 plasma membrane localization during vegetative growth via GFP-tagging.

### PMID:15948957 - Willer et al. 2005 (Mol Microbiol)
"Protein O-mannosylation is crucial for cell wall integrity, septation and viability in fission yeast."

This paper first describes SpWsc1p as an O-mannosylated protein, supporting the structural model that O-mannosylation of the Ser/Thr-rich region contributes to the rod-like rigidity of the ectodomain.

### PMID:18257517 - Wilson-Grady et al. 2008 (J Proteome Res)
"Phosphoproteome analysis of fission yeast."

Large-scale phosphoproteome study; identifies phosphoserine at Ser-354 in the cytoplasmic tail of Wsc1. This is potentially important for signal transduction.

## Signaling Pathway Summary

Based on all literature, the Wsc1 signaling pathway in S. pombe:

1. Wsc1 WSC domain binds cell wall polysaccharides
2. Under mechanical stress (wall compression/stretching), Wsc1 lateral diffusion is reduced, leading to clustering
3. Clustered Wsc1 recruits/activates the Rho-GEF Rgf2p at the cytoplasmic tail
4. Rgf2p activates Rho1p (GDP->GTP exchange)
5. Active Rho1p-GTP directly activates beta-1,3-glucan synthase (Bgs complex)
6. This promotes cell wall synthesis and repair

IMPORTANT: Unlike S. cerevisiae Wsc1, S. pombe Wsc1 acts INDEPENDENTLY of the MAPK (Pmk1) cell wall integrity pathway. The BioReason model incorrectly describes signaling through "PKC-like 2 -> MAPKK Skh1/Pek1" as part of the Wsc1 pathway. This is the Mtl2 branch or the general CWI MAPK pathway, not the Wsc1-specific branch.

## Notes on BioReason Predictions

1. GO:0004888 (transmembrane signaling receptor activity) - reasonable inference from domain architecture, but the existing curated term GO:0140897 (mechanoreceptor activity) is more specific and experimentally validated
2. GO:0060547 (negative regulation of necrotic cell death) - this GO term is OBSOLETE; moreover, there is no direct evidence that Wsc1 regulates necrotic cell death. This appears to be an unsupported extrapolation.
3. GO:0016021 (integral component of membrane) - reasonable structural inference but redundant with the more specific GO:0005886 (plasma membrane) and GO:0031520 (plasma membrane of cell tip)
4. BioReason correctly identifies the Rho1-centered signaling but incorrectly merges the Wsc1 and Mtl2 branches and adds the PKC->MAPK cascade that is NOT part of Wsc1 signaling in S. pombe
5. BioReason mentions "uncharacterized aminotransferase C6B12.04c" as an interaction partner - this is not validated in the literature
