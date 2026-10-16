---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMOTL1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8IY63
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 14
citation_count: 13
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMOTL1 (human)

## Current model (mechanistic narrative)

AMOTL1 is a peripheral membrane scaffold protein of tight junctions that acts as a central regulator of Hippo/YAP signaling, coupling junctional integrity to the cytoplasmic-to-nuclear shuttling of the transcriptional co-activator YAP1 [PMID:11733531, PMID:32313226]. First identified as a tight-junction protein of exocrine epithelia containing a coiled-coil domain and a C-terminal PDZ-binding motif [PMID:11733531], it is anchored at junctions through interactions with the multi-PDZ scaffolds MUPP1 and Patj [PMID:17397395]. Mechanistically, AMOTL1 binds YAP1 in the cytoplasm, mutually protecting each protein from ubiquitin-mediated degradation, and promotes YAP1 nuclear translocation to drive transcription of targets such as CTGF, thereby supporting proliferation, migration, and oncogenic properties [PMID:32313226]. AMOTL1 abundance is tightly controlled by competing ubiquitin-pathway inputs: NEDD4-1 engages three AMOTL1 PPxY motifs cooperatively through its WW domains to promote degradation, while KIBRA binds the C-terminal PPxY motif to protect AMOTL1 [PMID:41580069]; the tumor suppressor Merlin drives AMOTL1 degradation via NEDD family ligases [PMID:26806348]; HECW2 stabilizes AMOTL1 through K63-linked ubiquitination, and its loss relieves junctional integrity and triggers YAP nuclear translocation and angiogenic sprouting [PMID:27498087]; and Tankyrase-mediated PARylation marks AMOTL1 for RNF146-dependent proteasomal degradation [PMID:42012498]. AMOTL1 output is further tuned upstream by Fat4, which sequesters AMOTL1 out of the nucleus to restrict cardiomyocyte proliferation [PMID:28239148], and by SRSF3-directed alternative splicing that generates a long isoform with enhanced intracellular YAP1-translocating activity [PMID:37558679]. Patient-derived hotspot mutations R157C and P160L in the Tankyrase-binding motif abolish Tankyrase/RNF146 binding, prevent AMOTL1 turnover, and cause cytoplasmic accumulation that disrupts cell junctions and focal adhesions, impairs migration, and produces craniofacial, cardiac, and skeletal muscle defects in zebrafish [PMID:42012498].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-392499 Metabolism of proteins
- **partners:** YAP1, NEDD4-1, KIBRA, HECW2, MUPP1, PATJ, NF2, TNKS
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | Medium | AMOTL1 (JEAP) was identified as a novel peripheral membrane protein localized at tight junctions (TJs) specifically in exocrine cells (pancreas, submandibular gland, lacrimal gland, parotid gland, sublingual gland), but not at TJs of intestinal epithelial or endothelial cells. It contains a coiled-coil domain and a C-terminal PDZ-binding motif. | PMID:11733531 | The Journal of biological chemistry |
| 2007 | Medium | AMOTL1 (JEAP) physically interacts with the multi-PDZ scaffold proteins MUPP1 and Patj via its C-terminal PDZ-binding motif (PDZ3 of MUPP1 responsible for JEAP interaction). AMOTL1 co-localizes with MUPP1 at tight junctions and apical membranes in epithelial cells and behaves as a peripheral (not transmembrane) membrane protein. The PDZ-binding motif is not strictly required for TJ localization, indicating MUPP1/Patj interaction is not solely responsible for AMOTL1's TJ targeting. | PMID:17397395 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2014 | Medium | miR-124 represses AMOTL1 expression by directly targeting its 3′UTR, thereby suppressing vasculogenic mimicry, migration, invasion, and EMT in cervical cancer cells. | PMID:25218344 | Cancer letters |
| 2016 | High | The E3 ubiquitin ligase HECW2 physically interacts with AMOTL1 and stabilizes it via K63-linked ubiquitination in endothelial cells. HECW2 depletion reduces AMOTL1 stability, loosens cell-to-cell junctions, and causes nuclear translocation of YAP, leading to increased angiogenic sprouting. | PMID:27498087 | Cellular signalling |
| 2016 | Medium | The tumor suppressor Merlin directly interacts with AMOTL1 and triggers its proteasomal degradation via NEDD family ubiquitin ligases. YAP activity conversely stimulates AMOTL1 expression. AMOTL1 expression is sufficient to trigger tumor cell migration and stimulates proliferation by activating c-Src. | PMID:26806348 | Neoplasia (New York, N.Y.) |
| 2017 | High | In the mouse heart, Fat4 sequesters AMOTL1 out of the nucleus; loss of Fat4 allows nuclear translocation of AMOTL1 together with YAP1, promoting cardiomyocyte proliferation and heart overgrowth. AMOTL1 acts as a mammalian intermediate for non-canonical Hippo signaling downstream of Fat4, restricting heart growth at birth. | PMID:28239148 | Nature communications |
| 2020 | Medium | AMOTL1 physically interacts with YAP1 in the cytoplasm, protecting each other from ubiquitin-mediated degradation. AMOTL1 promotes YAP1 translocation into the nucleus to activate downstream targets such as CTGF. Knockdown of AMOTL1 impairs gastric oncogenic properties. | PMID:32313226 | Oncogene |
| 2023 | Medium | The splicing factor SRSF3 directly binds exon 12 of AMOTL1 via its RRM domain to promote inclusion of exon 12, generating a long isoform (AMOTL1-L). AMOTL1-L preferentially localizes intracellularly rather than at the cell membrane and more robustly interacts with YAP1, promoting its nuclear translocation and NPC cell proliferation and migration; the short isoform AMOTL1-S lacks these properties. | PMID:37558679 | Cell death & disease |
| 2024 | High | N-acetyltransferase 10 (Nat10) mediates N4-acetylcytidine (ac4C) modification of Amotl1 mRNA, increasing its stability and translation in cardiac fibroblasts. This leads to increased Amotl1–Yap interaction and Yap nuclear translocation, promoting cardiac fibroblast proliferation and differentiation into myofibroblasts, contributing to cardiac fibrosis after myocardial infarction. | PMID:38839936 | Acta pharmacologica Sinica |
| 2026 | High | AMOTL1 contains three PPxY motifs that engage NEDD4-1 and KIBRA through distinct cooperative binding mechanisms. NEDD4-1 binds all three PPxY motifs cooperatively (using three of its four WW domains), yielding ~10-fold enhanced affinity and promoting AMOTL1 degradation. KIBRA binds primarily through the C-terminal PPxY motif with high affinity and protects AMOTL1 from degradation; secondary KIBRA interactions at other PPxY sites do not enhance overall affinity. | PMID:41580069 | Journal of molecular biology |
| 2026 | High | Patient-derived hotspot mutations R157C and P160L in the Tankyrase-binding motif (TBM) of AMOTL1 abolish interaction with Tankyrase 1/2 and RNF146, preventing poly-ADP-ribosylation, ubiquitination, and proteasomal degradation of AMOTL1. The stabilized mutants accumulate in the cytoplasm, disrupt cell junctions and focal adhesions, inhibit cell migration velocity and persistence, and cause craniofacial malformations and cardiac/skeletal muscle defects in zebrafish. | PMID:42012498 | Bioscience reports |
| 2026 | Medium | PFKP directly binds AMOTL1 and inhibits its ubiquitin-mediated degradation. PFKP-driven aerobic glycolysis and EMT in head and neck cancer cells are dependent on AMOTL1. PFKP promotes YAP nuclear translocation via AMOTL1, suppressing Hippo pathway activity. | PMID:41727965 | Journal of translational internal medicine |
| 2025 | Low | Tankyrase (TNKS1/2) targets AMOTL1 as a direct substrate; pharmacological TNKS inhibition with OM-153 stabilizes AMOTL1 protein in lung fibroblasts, suppresses YAP signaling, and reduces pro-fibrotic ECM expression in multiple preclinical IPF models. | — | bioRxiv |
| 2024 | Low | AMOTL1 interacts with the androgen receptor (AR) in prostate cancer cells, and this interaction is pivotal for modulating sensitivity to AR antagonists. | PMID:39643184 | International journal of biological macromolecules |

## Citations

- PMID:11733531
- PMID:17397395
- PMID:25218344
- PMID:26806348
- PMID:27498087
- PMID:28239148
- PMID:32313226
- PMID:37558679
- PMID:38839936
- PMID:39643184
- PMID:41580069
- PMID:41727965
- PMID:42012498
