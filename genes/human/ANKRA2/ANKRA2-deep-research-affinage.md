---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRA2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9H9E1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRA2 (human)

## Current model (mechanistic narrative)

ANKRA2 is an ankyrin-repeat scaffold protein that functions as a signal-responsive transcriptional corepressor by reading short linear PxLPxI/L motifs in diverse partner proteins [PMID:22649097]. Crystal structures of its ankyrin repeat domain bound to target peptides defined a tumbler-lock recognition mode in which each of the middle three repeats engages one motif residue, and showed that this interface accommodates motifs from HDAC4, HDAC5, HDAC9, megalin, and RFX5 [PMID:22649097]. Through this domain ANKRA2 binds class IIa HDACs (HDAC4, HDAC5) and recruits them as corepressors: it represses CIITA-induced MHC II and HLA-DRA expression in conjunction with the paralog RFXANK [PMID:16236793], and is recruited to the AhR repressor C-terminal domain to repress CYP1A1, an interaction that depends on SUMOylation of AhRR [PMID:17949687, PMID:19251700]. The same ankyrin domain can substitute for RFXANK in MHC II enhanceosome assembly by contacting RFX5, complementing RFXANK-deficient bare lymphocyte syndrome cells [PMID:15655668, PMID:16166641]. Beyond immune gene regulation, ANKRA2 binds the PxLPxL motif of the 3M-syndrome protein CCDC8, linking it to the OBSL1/CUL7 ligase complex [PMID:25752541], and serves as a direct p53 target gene and a high-affinity cofactor of the tumor suppressor transcription factor RFX7, regulating RFX7-overlapping targets such as PDCD4 [PMID:31864703, PMID:39181888]. HDAC4 recruitment is switched off by CaMK-driven phosphorylation of Ser350 within its PxLPxI/L motif, which disrupts ANKRA2 binding and creates a 14-3-3 docking site, coupling complex assembly to calcium signaling [PMID:16236793, PMID:22649097].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-168256 Immune System, R-HSA-4839726 Chromatin organization
- **partners:** HDAC4, HDAC5, RFX5, RFX7, CCDC8, AHRR, RFXANK
- **complexes:** MHC II enhanceosome (RFX complex)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Medium | Class IIa HDACs (HDAC4 and HDAC5) physically associate with the ankyrin repeat domain of ANKRA2, and through association with the paralog RFXANK, repress MHC II promoter activation and endogenous HLA-DRA gene expression induced by CIITA. Phosphorylation of class II HDACs by CaMK results in CRM1-dependent nuclear export of HDAC/RFXANK complexes. | PMID:16236793 | Molecular biology of the cell |
| 2012 | High | The ankyrin repeat domain of ANKRA2 recognizes a PxLPxI/L motif found in HDAC4, HDAC5, HDAC9, megalin, and RFX5, using a tumbler-lock binding mode where each of the middle three ankyrin repeats contacts one residue of the motif. Crystal structures of ANKRA2 ankyrin repeats in complex with binding peptides defined this recognition mechanism. Phosphorylation of Ser350 within the PxLPxI/L motif of HDAC4 impairs ANKRA2 binding while generating a 14-3-3 docking site. | PMID:22649097 | Science signaling |
| 2007 | Medium | ANKRA2 was identified as a binding partner of the AhR repressor (AhRR) C-terminal repression domain via yeast two-hybrid screening. ANKRA2 recruits HDAC4 and HDAC5 as corepressors for AhRR-mediated transcriptional repression of CYP1A1; siRNA knockdown of ANKRA2 reduces AhRR repression activity. | PMID:17949687 | Biochemical and biophysical research communications |
| 2009 | Medium | SUMOylation of AhRR at Lys-542, Lys-583, and Lys-660 is required for the interaction between AhRR and ANKRA2 (as well as HDAC4 and HDAC5); arginine mutation of these residues reduces both SUMOylation and the AhRR–ANKRA2 interaction, impairing transcriptional repression. | PMID:19251700 | The Journal of biological chemistry |
| 2005 | Medium | The ankyrin repeat domain (ARD) of ANKRA2 can substitute for RFXANK in activating MHC II gene expression, as demonstrated by complementation of a bare lymphocyte syndrome cell line deficient in RFX-B (RFXANK). Mouse and Xenopus RFXANK orthologues complement this deficiency but ANKRA2 does so only through its ARD. | PMID:15655668 | Immunogenetics |
| 2005 | Medium | ANKRA2 ankyrin repeat domain mediates interaction with RFX5, and high-resolution mutagenesis of the closely related RFXANK ARD mapped the RFX5 interaction surface; ANKRA2 can substitute for RFXANK in MHC-II enhanceosome assembly through its ARD. | PMID:16166641 | Molecular and cellular biology |
| 2015 | High | The ankyrin repeats of ANKRA2 recognize a PxLPxL motif at the C-terminal region of CCDC8 (a 3M syndrome protein), establishing CCDC8 as a major cellular partner of ANKRA2 but not RFXANK. The N-terminal part of CCDC8 interacts with OBSL1 to form a CUL7 ligase complex, linking ANKRA2 to the 3M syndrome complex. | PMID:25752541 | Structure |
| 2019 | High | Crystal structures of ANKRA2 ankyrin domain bound to an RFX7 fragment revealed that ANKRA2 recognizes the PxLPxL motif of RFX7 and flanking sequences via extensive hydrophobic interactions, with higher binding affinity than RFXANK for RFX7. | PMID:31864703 | Biochemical and biophysical research communications |
| 2024 | Medium | ANKRA2 is a direct transcriptional target of p53, and functions as a critical cofactor of the tumor suppressor transcription factor RFX7. Mass spectrometry identified ANKRA2 binding to the X-box motif of the PDCD4 promoter together with RFX5, RFXAP, RFXANK, and RFX7. Transcriptome analyses showed ANKRA2 regulates a gene set overlapping with RFX7 targets, distinct from RFXANK-regulated genes. | PMID:39181888 | Cell death discovery |

## Citations

- PMID:15655668
- PMID:16166641
- PMID:16236793
- PMID:17949687
- PMID:19251700
- PMID:22649097
- PMID:25752541
- PMID:31864703
- PMID:39181888
