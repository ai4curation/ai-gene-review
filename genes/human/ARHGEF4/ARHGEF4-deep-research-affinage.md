---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NR80
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 23
citation_count: 23
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF4 (human)

## Current model (mechanistic narrative)

ARHGEF4 (Asef) is a guanine nucleotide exchange factor that links the APC tumor suppressor to Rho-family GTPase signaling, thereby controlling actin cytoskeletal remodeling, cell-cell adhesion, and directed migration [PMID:10947987, PMID:12598901]. The enzyme is held inactive by an intramolecular interaction between its SH3 domain and the catalytic DH/PH module that blocks GTPase binding; engagement of the APC armadillo repeats by Asef's APC-binding region (ABR/CAB motif) relieves this autoinhibition, and crystallographic analysis shows APC recognition drives a conformational change that sterically frees the DH domain to catalyze nucleotide exchange [PMID:17704816, PMID:21788986]. In purified systems Asef acts as a CDC42-specific exchange factor whose activity is enhanced by the PH domain, and chemical-probe disruption of the APC-Asef interface confirmed CDC42 as the operative GTPase in APC-stimulated activation within colorectal cancer cells [PMID:17214551, PMID:28759015]. Asef activity is further gated by upstream signals: Src-family kinases phosphorylate Tyr94 in the APC-binding region downstream of EGF, the PH domain binds PtdIns(3,4,5)P3 for PI3K-dependent membrane and junctional targeting, and growth-factor-driven, microtubule-dependent recruitment positions Asef at the cell periphery [PMID:17292853, PMID:18653540, PMID:19525225, PMID:25101856]. Through these inputs Asef weakens E-cadherin-mediated adhesion to promote colorectal tumor cell migration, and genetic loss reduces adenoma burden in Apc(Min/+) mice via JNK-mediated MMP9 transactivation and supports tumor angiogenesis [PMID:12598901, PMID:19893577, PMID:19897489]. In endothelium Asef nucleates an IQGAP1-cortactin/Arp3 cortical actin module downstream of HGF to enhance Rac1 activity and barrier function and to mediate anti-inflammatory protection [PMID:25492863, PMID:25518936, PMID:25539852]. Distinct roles include CNS astrocyte differentiation and blood-brain barrier integrity [PMID:27881777] and a neuronal function in which Asef negatively regulates Staufen-dependent PSD-95 synaptic localization and excitatory transmission [PMID:30125942, PMID:33154196].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005886 plasma membrane, GO:0005829 cytosol, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease, R-HSA-112316 Neuronal System
- **partners:** APC, CDC42, RAC1, IQGAP1, STAUFEN1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2000 | High | ARHGEF4/Asef binds to the armadillo repeat domain of APC tumor suppressor protein, and this interaction enhances Asef's GEF activity, stimulating cell flattening, membrane ruffling, and lamellipodia formation. Asef was initially characterized as a Rac-specific GEF. | PMID:10947987 | Science |
| 2000 | Medium | ARHGEF4 (Asef) is expressed in brain and encodes a protein with a DH domain showing homology to collybistin, mapping to chromosome 2q22. | PMID:10873612 | Biochemical and biophysical research communications |
| 2003 | High | Overexpression of Asef decreases E-cadherin-mediated cell-cell adhesion and promotes epithelial cell migration; both activities are stimulated by truncated APC proteins found in colorectal tumor cells. RNAi and dominant-negative experiments show both Asef and mutated APC are required for colorectal tumor cell migration. | PMID:12598901 | Nature cell biology |
| 2007 | High | Asef is autoinhibited through an intramolecular interaction between its SH3 domain and the catalytic DH/PH domains that blocks CDC42 binding. Binding of the APC armadillo repeats to the 'core APC-binding' (CAB) motif of Asef, or truncation of the SH3 domain, relieves this autoinhibition and allows specific activation of CDC42. Full-length (but not truncated) APC activates CDC42 in an Asef-dependent manner to suppress anchorage-independent growth in colorectal cancer cell lines. | PMID:17704816 | Nature structural & molecular biology |
| 2007 | High | In vitro GEF activity assays show Asef has negligible activity toward Rac1, Rac2, Rac3, RhoA, or TC10, but catalyzes nucleotide exchange on CDC42. The PH domain enhances the CDC42-GEF activity of the DH domain and also contributes to autoinhibition. | PMID:17214551 | Biological chemistry |
| 2007 | Medium | The PH domain of Asef binds phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3) and targets Asef to cell-cell adhesion sites in MDCK II cells. Overexpression of Asef increases E-cadherin and actin filaments at cell-cell contact sites. | PMID:17292853 | Biochemical and biophysical research communications |
| 2008 | High | EGF stimulation induces phosphorylation of Tyr94 within the APC-binding region of Asef via Src-family tyrosine kinases, and this phosphorylation is required for EGF-induced Rac1 activation. A Tyr94Phe mutant of Asef fails to restore EGF-induced Rac1 activation in Asef siRNA-treated cells. | PMID:18653540 | Journal of cell science |
| 2009 | High | Asef deficiency (Asef-/- mice) significantly reduces the number and size of adenomas in Apc(Min/+) mice. The APC-Asef complex induces c-Jun N-terminal kinase (JNK)-mediated transactivation of matrix metalloproteinase 9 (MMP9), required for invasive activity of colorectal tumor cells. Asef is also required for tumor angiogenesis. | PMID:19893577 | EMBO reports |
| 2009 | High | Asef is required for basic fibroblast growth factor (bFGF)- and vascular endothelial growth factor (VEGF)-induced endothelial cell migration and microvessel formation in vitro, and tumor growth and vascularity are markedly impaired in subcutaneous tumor implantation in Asef-/- mice. | PMID:19897489 | The Journal of biological chemistry |
| 2009 | High | HGF, bFGF, and EGF induce accumulation and colocalization of APC and Asef in membrane ruffles and lamellipodia. Both APC and Asef are required for HGF-induced cell migration. These effects are mediated by PI3-kinase activation and require the PH domain of Asef, placing Asef downstream of growth factor receptors and PI3K. | PMID:19525225 | The Journal of biological chemistry |
| 2011 | High | Crystal structure of the human APC armadillo repeat domain/Asef complex reveals that APC uses a conserved surface groove to recognize the APC-binding region (ABR) of Asef, with large conformational changes in ABR upon binding. Structural superimposition suggests APC binding creates steric clash with the DH domain to stimulate GEF activity. Key interface residues on APC and Asef were mutated and shown to abrogate binding and GEF activity. | PMID:21788986 | Cell research |
| 2013 | Medium | In non-motile confluent cells, Asef colocalizes with wild-type APC at cell-cell adhesion sites (apical and junctional levels). In colorectal tumor cells with truncated APC, Asef and mutant APC are localized mainly in the cytoplasm, suggesting aberrant subcellular localization contributes to abnormal adhesion and migration. | PMID:23910005 | Cancer science |
| 2014 | High | HGF induces formation of an Asef-IQGAP1 protein complex that colocalizes at the cell cortical area. Asef knockdown attenuates HGF-induced Rac activation, IQGAP1 accumulation at the cortex, and IQGAP1 interaction with cortactin and Arp3. The IQGAP1 C-terminal domain is essential for HGF-induced IQGAP1/Asef interaction. Active (not inactive) Asef is required for IQGAP1 interaction, establishing a positive feedback mechanism for cortical cytoskeletal remodeling. | PMID:25492863 | The Journal of biological chemistry |
| 2014 | High | Asef knockdown attenuates HGF-induced Rac1 activation, peripheral actin enhancement, lamellipodia formation, VE-cadherin adherens junctions, and protection against thrombin-induced RhoA activation and EC permeability. HGF-induced membrane translocation of Asef stimulates its Rac1-specific nucleotide exchange activity. Asef-/- mice fail to respond to HGF protection against lung injury. | PMID:25518936 | Molecular biology of the cell |
| 2014 | High | Asef knockdown attenuates HGF protective effects against LPS-induced EC barrier failure, NF-κB signaling, adhesion molecule expression (ICAM-1, VCAM-1), and IL-8 production. Asef-/- mice show diminished HGF protection against LPS-induced lung inflammation and vascular leak, demonstrating Asef is required for HGF anti-inflammatory barrier protection. | PMID:25539852 | American journal of physiology. Lung cellular and molecular physiology |
| 2014 | Medium | HGF activates Asef through an APC- and microtubule-dependent pathway distinct from Tiam1 activation. Asef associates with microtubule fraction upon HGF stimulation. Low-dose nocodazole inhibiting peripheral microtubule dynamics attenuates HGF-induced Asef peripheral translocation and EC barrier enhancement, without affecting Tiam1. | PMID:25101856 | Cellular signalling |
| 2016 | Medium | Mice lacking Asef exhibit impaired astrocyte differentiation during spinal cord development and impaired repair after white matter injury, coupled with compromised blood-brain barrier integrity in adult CNS. | PMID:27881777 | The Journal of neuroscience |
| 2017 | High | Peptidomimetic inhibitors disrupting the APC-Asef interface block colorectal cancer cell migration. Using the peptidomimetic as a chemical probe established that CDC42 (not Rac1) is the downstream GTPase involved in APC-stimulated Asef activation in colorectal cancer cells. Crystal structures confirmed the inhibitors bind in the APC pocket at the Asef interface. | PMID:28759015 | Nature chemical biology |
| 2018 | Medium | Full-length APC is autoinhibited through intramolecular interaction between its armadillo repeats and APC residues 1362–1540 (APC-2,3 repeats), which competes off and inhibits Asef. Deletion of these APC repeats permits Asef activation, leading to Golgi fragmentation via Asef-ROCK-MLC2 signaling. Truncated APC disrupts protein trafficking and SREBP2-dependent cholesterol homeostasis in a Golgi fragmentation-dependent manner. | PMID:29866653 | Molecular and cellular biology |
| 2018 | Medium | Asef1 (ARHGEF4) negatively regulates synaptic localization of PSD-95 in excitatory synapses by inhibiting Staufen-mediated synaptic localization of PSD-95, thereby impairing synaptic transmission in hippocampal neurons. Neuronal activity facilitates PI3K-dependent dissociation of Asef1 from Staufen. | PMID:30125942 | Journal of neurochemistry |
| 2019 | Medium | ARHGEF4 (Asef) plays a role in actin cytoskeleton reorganization, migration, and podosome-related gene expression in hepatic stellate cells cultured in 3D floating collagen matrices, acting as a Rac1-specific GEF in this context. | PMID:30871422 | Cell adhesion & migration |
| 2020 | Medium | Arhgef4 knockout mice display enlarged PSD-95 clusters in hippocampal neurons and enhanced spatial memory and object recognition memory, confirming Arhgef4 acts as a negative regulator of excitatory synaptic function at the behavioral level. | PMID:33154196 | Experimental neurobiology |
| 2021 | Medium | Staufen1 overexpression blocks the GEF activity of Arhgef4 and inhibits Arhgef4-induced increase in dendritic protrusions in cultured neurons. Arhgef4 can simultaneously bind both APC and Staufen1, suggesting Staufen1 modulates Arhgef4 GEF activity independently of APC binding. | PMID:34022264 | Neuroscience letters |

## Citations

- PMID:10873612
- PMID:10947987
- PMID:12598901
- PMID:17214551
- PMID:17292853
- PMID:17704816
- PMID:18653540
- PMID:19525225
- PMID:19893577
- PMID:19897489
- PMID:21788986
- PMID:23910005
- PMID:25101856
- PMID:25492863
- PMID:25518936
- PMID:25539852
- PMID:27881777
- PMID:28759015
- PMID:29866653
- PMID:30125942
- PMID:30871422
- PMID:33154196
- PMID:34022264
