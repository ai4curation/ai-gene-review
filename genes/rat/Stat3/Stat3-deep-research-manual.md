# Stat3 (rat, UniProt P52631): manual literature synthesis

No deep-research provider was run for this gene (no API keys in this session). This file
is a manual synthesis written from the cached publications in `publications/` and the
UniProt record (`Stat3-uniprot.txt`). Every claim carries inline provenance.

## Identity and family

- Rat Stat3 (P52631; RGD:3772; GeneID 25125) is a 770-aa member of the STAT transcription
  factor family, with N-terminal, coiled-coil, DNA-binding (p53-like fold), linker, SH2 and
  transactivation domains (InterPro IPR001217 STAT; IPR035855 STAT3_SH2)
  [file:rat/Stat3/Stat3-uniprot.txt "Belongs to the transcription factor STAT family."].
- Rat Stat3 was first purified from acute-phase rat liver nuclei by DNA-affinity
  chromatography on the IL-6 response element of the alpha2-macroglobulin gene
  [PMID:8530402 "Amino acid sequence analysis identified the 86- and 91-kDa species as two forms of the transcription factor Stat3"].

## Core molecular mechanism (cytokine-activated, sequence-specific transcription activator)

- Canonical activation: receptor-associated JAKs phosphorylate STATs on a tyrosine, STATs
  dimerise and translocate to the nucleus to bind promoter elements
  [PMID:19450559 "This association causes JAKs to phosphorylate STATs at distinct tyrosine residues, allowing the bound STATs to be released from the receptor and undergo homo- or heterodimersation"].
- UniProt function summary [file:rat/Stat3/Stat3-uniprot.txt "Signal transducer and transcription activator that mediates cellular responses to interleukins, KITLG/SCF, LEP and other growth factors."]
  and IL-6/gp130 acute-phase target genes [file:rat/Stat3/Stat3-uniprot.txt "Upon activation of IL6ST/gp130 signaling by interleukin-6 (IL6), binds to the IL6-responsive elements identified in the promoters of various acute-phase protein genes."].
- In rat cardiomyocytes, Stat3 forms a promoter-binding complex with NFAT and binds the
  alphaBE4 element of the CryAB gene [PMID:19538478 "the transcription factors NFAT, Nished and STAT3 form a dynamic ternary complex and interact with the alphaBE4 promoter element of the CryAB gene"].
- In rat hippocampal CA1, Stat3 occupies target promoters (survivin, Bcl-xL, Mn-SOD) after
  ischemia and drives STAT3-dependent transcription [PMID:23884942 "Ischemia promotes activation of STAT3 signaling, association of STAT3 with the promoters of target genes, and STAT3-dependent mRNA and protein expression of prosurvival proteins in the selectively vulnerable CA1."].
- Tyr705 is required: a Y705F dominant-negative Stat3 enhances cell death in rat neonatal
  ventricular myocytes [PMID:19450559 "This data provides further evidence that a fully transcriptionally active STAT3 that requiring the 705 tyrosine phosphorylation site is necessary for its cytoprotective properties."].

## Interactions recorded for the rat protein

- Glucocorticoid receptor interacts with Stat3 at the haptoglobin HRE during the acute phase
  [PMID:20155810 "Coimmunoprecipitation experiments showed that activated GR established de novo interaction with STAT3 isoforms"].
- STAT5B associates with Stat3 in thrombin-stimulated VSMC [PMID:16527988 "An increased association of STAT-5B with STAT-3 occurred in response to thrombin"].
- Co-association with CCR1/CCR2/CCR5 in arthritic joints [PMID:14674010 "The association of STAT-1 and STAT-3 with CCR5 on days 18 and 21 correlated with JAK-1 phosphorylation and binding on day 18."].
- Association with ephrinB1 [PMID:17954917 "signal transducer and activator of transcription 3 (STAT3) can interact with ephrinB1 in a phosphorylation-dependent manner"] and with Rac1 [PMID:16055727 "Upon SIRPα activation, we observed the presence of STAT3 in immunoprecipitates of Rac1."].

## Non-nuclear pools

- Mitochondria: STAT3 is imported into mitochondria in a GRIM-19-dependent manner and
  resides in the inner membrane [PMID:23271731 "In this report we show that mitochondrial-localized STAT3 resides in the inner mitochondrial membrane."].
- Pharmacological STAT3 inhibition (Stattic) in rat heart mitochondria increases ROS, lowers
  ATP production and sensitises the permeability transition pore [PMID:23590160 "inhibition of mitochondrial STAT3 by Stattic impacts on mitochondrial ATP production and MPTP opening through enhanced ROS formation"].
  Caveat: Stattic is a small-molecule inhibitor and these are pharmacological, not genetic, data.
- Postsynaptic density: Stat3 is found in the rat PSD [PMID:10891587 "The occurrence of Stat3 in the synaptic site, especially in the PSD, was confirmed by immunoelectron microscopic examination."].
  In rat hippocampal slices, STAT3 inhibition or knockdown blocks NMDAR-dependent LTD
  [PMID:22284190 "Thus, pharmacological inhibition or knockdown of STAT3 also blocks the induction of NMDAR-LTD."]
  by a non-nuclear, transcription-independent mechanism [PMID:22284190 "These data collectively suggest that NMDAR-LTD can be readily induced and expressed for at least 3 hr, without the need for gene transcription and that the effects of inhibition of STAT3 are independent of an action within the nucleus."].

## Physiological contexts in rat (mostly perturbation / expression evidence)

- Acute-phase response in liver [PMID:8530402].
- Cytoprotection of cardiomyocytes against ischemia/reperfusion [PMID:19450559 "Overexpression of STAT3 in primary neonatal rat ventricular myocytes (NRVM) protects against I/R-induced cell death."];
  IL-6-activated Stat3 prevents cardiomyocyte apoptosis in haemorrhagic shock [PMID:18270592 "Pre-treatment of rats with a selective inhibitor of Stat3, T40214, reduced the IL-6-mediated increase in cardiac Stat3 activity"].
- Estradiol neuroprotection after global ischemia via Stat3-dependent survivin
  transcription [PMID:23884942].
- IL-6-stimulated satellite-cell proliferation via JAK2/STAT3/cyclin D1 [PMID:23869758 "IL-6 induced dose-dependent increase in satellite cell proliferation by activating the JAK2/STAT3/cyclin D1 pathway."];
  ghrelin-stimulated hippocampal neural stem cell proliferation [PMID:23608221 "pretreatment of cells with specific inhibitors of MEK/ERK1/2, phosphatidylinositol-3-kinase (PI3K)/Akt, mTOR, and Jak2/STAT3 attenuated ghrelin-induced cell proliferation"].
- Prolactin-induced SERCA2 expression in islets [PMID:17911393 "The upregulation of SERCA2 by PRL was abolished after STAT3 knockdown."].
- TNF-induced IL-6 release from brain pericytes via NF-kB and JAK-STAT3 [PMID:29702085].
- Hypoxia/SuHx pulmonary hypertension: phospho-STAT3 in CD4+ cells [PMID:38602915 "Phosphorylation of STAT3 in CD4+ cells was also observed around the vascular lesions in the lungs of the SuHx rat"].

## Inferences

Rat Stat3 is ~99% identical to mouse and human STAT3, so the extensive mouse/human
literature (leptin signalling in hypothalamus, Th17 differentiation, gp130-family cytokine
signalling, autophagy repression via PKR, mitochondrial respiration) is transferred by ISO
annotations. These are plausible, but most of the organismal processes (feeding behaviour,
temperature homeostasis, glucose homeostasis) are downstream physiological consequences of
its transcriptional role in particular cell types rather than distinct activities.
