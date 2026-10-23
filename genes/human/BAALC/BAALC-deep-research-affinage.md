---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BAALC
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXS3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BAALC (human)

## Current model (mechanistic narrative)

BAALC encodes a small, membrane-associated cytoplasmic scaffold/adaptor protein whose stage-restricted expression marks CD34+ hematopoietic progenitors and is downregulated as cells commit to myeloid lineages [PMID:14585369]. In neurons the 1-6-8 isoform is anchored to postsynaptic lipid rafts through N-terminal myristoylation and palmitoylation and binds the regulatory domain of CaMKIIα, establishing a raft-targeted adaptor function [PMID:15659234]. In leukemia, BAALC functions as an oncogenic scaffold: it binds MEKK1 (MAP3K1) and blocks MKP3/DUSP6-mediated ERK dephosphorylation to sustain ERK activity, while simultaneously sequestering the transcription factor KLF4 in the cytoplasm to block monocytic differentiation, together driving cell-cycle progression and chemoresistance [PMID:26050649]. It additionally signals through phosphorylation of MK2a (MAPKAPK2), and its loss selectively halts proliferation and induces differentiation of CN/AML blasts without affecting normal HSPCs [PMID:33894142], and it interacts with the actin-binding protein DBN1 to promote stromal adhesion and microenvironment-mediated chemoresistance [PMID:33453340]. Functionally, BAALC promotes leukemia cell survival and proliferation, as knockdown reduces growth and increases apoptosis [PMID:22549446]. Its transcription is activated by a RUNX1-binding promoter SNP and by an SP1/NF-κB complex, and is shaped by histone modifications consistent with a paused promoter state [PMID:22493267, PMID:24736457, PMID:22197554].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-74160 Gene expression (Transcription)
- **partners:** MAP3K1, KLF4, DBN1, CAMK2A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | Low | BAALC protein localizes to the cytoplasm and in vitro studies suggest a function in the cytoskeleton network. Five protein isoforms are produced from complex splicing of eight transcripts. | PMID:11707601 | Proceedings of the National Academy of Sciences of the United States of America |
| 2003 | Medium | BAALC expression is restricted to CD34+ hematopoietic progenitor cells (including CD34+/CD38-, CD34+/CD33+, and lineage-committed CD34+ fractions) and is downregulated during in vitro differentiation with lineage-specific cytokines (G-CSF, M-CSF, EPO) as early as day 4, indicating stage-specific expression tied to progenitor identity. | PMID:14585369 | Experimental hematology |
| 2005 | High | BAALC 1-6-8 isoform protein is targeted to postsynaptic lipid rafts via N-terminal myristoylation and palmitoylation; both modifications are required for raft targeting. The protein physically interacts with CaMKIIα (but not CaMKIIβ) through its N-terminal 35-amino-acid region binding to the C-terminal regulatory domain of CaMKIIα. The protein localizes to synaptic sites and increases during synaptogenesis. | PMID:15659234 | Journal of neurochemistry |
| 2005 | Low | Baalc protein localizes to the cytoplasm adjacent to the cell membrane in muscle cells and co-localizes with known muscle-associated proteins but not with neural crest or neuronal markers, identifying it as a marker of the mesodermal/muscle lineage in mouse embryos. | PMID:15749074 | Gene expression patterns : GEP |
| 2005 | Low | BAALC expression is induced in astrocytes upon treatment with differentiation inducers (inhibition of proliferation), suggesting a role in the astrocyte differentiation/proliferation balance. | PMID:16376586 | Cell biology international |
| 2011 | Medium | BAALC gene promoter activity is regulated by histone post-translational modifications (H3K9K14 acetylation, H3K4 trimethylation, H3K23 trimethylation), with distinct epigenetic profiles associated with high versus low BAALC expression in leukemia cell lines, consistent with a 'paused' transcriptional state. | PMID:22197554 | Biochemical and biophysical research communications |
| 2012 | Medium | shRNA-mediated knockdown of BAALC in the KG1a AML cell line results in decreased proliferation and enhanced apoptosis, demonstrating a functional role for BAALC in promoting leukemia cell survival and proliferation. | PMID:22549446 | Hematology (Amsterdam, Netherlands) |
| 2012 | High | A SNP (rs62527607[GT]) in the BAALC promoter region creates a binding site for the RUNX1 transcription factor; the T allele drives higher BAALC expression in an allele-specific manner, establishing RUNX1 as a transcriptional activator of BAALC. | PMID:22493267 | Proceedings of the National Academy of Sciences of the United States of America |
| 2014 | Medium | miR-3151, located in intron 1 of BAALC, has its own regulatory element that partly uncouples its expression from the BAALC transcript. Both miR-3151 and BAALC are transcriptionally activated by a SP1/NF-κB complex, whereas BAALC (but not miR-3151) is additionally stimulated by RUNX1. | PMID:24736457 | Science signaling |
| 2015 | High | BAALC physically interacts with the scaffold protein MEKK1 (MAP3K1), inhibiting the interaction between ERK and its phosphatase MKP3/DUSP6, thereby sustaining ERK activity and promoting cell-cycle progression and chemoresistance. Separately, BAALC traps the transcription factor KLF4 in the cytoplasm, preventing nuclear KLF4-mediated monocytic differentiation of AML cells. | PMID:26050649 | Leukemia |
| 2021 | Medium | BAALC physically interacts with DBN1 (Drebrin 1), an actin-binding protein. This interaction promotes cell adhesion to bone marrow stromal cells; DBN1 knockdown impairs adhesion and restores sensitivity to cytarabine, indicating the BAALC-DBN1 interaction contributes to microenvironment-mediated chemoresistance. | PMID:33453340 | Experimental hematology |
| 2021 | High | BAALC upregulation in CN/AML cells results in phosphorylation of MK2a (MAPKAPK2); genetic deletion of BAALC or pharmacological inhibition of MK2a phosphorylation (with CMPD1) blocks proliferation and induces differentiation of CN/AML blasts selectively without affecting normal hematopoietic stem and progenitor cells. | PMID:33894142 | Cell stem cell |
| 2021 | Medium | BAALC overexpression in MCF-7 breast cancer cells increases proliferation, anchorage-independent growth, invasion, and migration; siRNA knockdown in Hs578T cells decreases these properties. The migration and invasion effect is mediated by FAK (focal adhesion kinase)-dependent signaling and is accompanied by increased MMP-9 (but not MMP-2) activity. | PMID:33968759 | Frontiers in oncology |
| 2020 | Medium | NMR backbone resonance assignments (1H, 13C, 15N) were completed for the longest hematopoietic isoform (isoform 1) of human BAALC, providing the first structural characterization of the protein backbone. Comparison with the shortest neuroectodermal isoform (isoform 6) showed only minor chemical shift differences. | PMID:32240523 | Biomolecular NMR assignments |

## Citations

- PMID:11707601
- PMID:14585369
- PMID:15659234
- PMID:15749074
- PMID:16376586
- PMID:22197554
- PMID:22493267
- PMID:22549446
- PMID:24736457
- PMID:26050649
- PMID:32240523
- PMID:33453340
- PMID:33894142
- PMID:33968759
