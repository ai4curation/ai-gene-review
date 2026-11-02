---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKHD1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8IWZ3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 16
citation_count: 16
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKHD1 (human)

## Current model (mechanistic narrative)

ANKHD1 is a large multi-domain scaffolding protein that promotes cell proliferation, cell-cycle progression, and tumor cell migration across diverse cancer contexts by coupling protein-protein and RNA-binding activities to growth-control pathways [PMID:24726915, PMID:29695508]. It acts upstream of the Hippo effector YAP1, with silencing reducing YAP1 expression and activation while increasing inhibitory YAP1 phosphorylation, and YAP1 re-expression rescues the loss-of-ANKHD1 phenotype, placing ANKHD1 within a YAP1/AKT signaling axis that controls EMT markers and radioresistance [PMID:24726915, PMID:30555746, PMID:35110552]. ANKHD1 drives the cell cycle through several converging routes: it represses the p21 (CDKN1A) promoter and binds p21 directly while shuttling between cytoplasm and nucleus [PMID:25483783], binds CDK4 to potentiate Cyclin D1/CDK4 activity and retinoblastoma phosphorylation [PMID:40457431], and uses its C-terminal KH domain to bind and suppress tumor-suppressor miRNAs (miR-29a, miR-205, miR-196a), relieving repression of Cyclin D1 [PMID:29695508]. As a chromatin-associated cofactor it partners with the methyltransferase SMYD3 to activate transcription of SLUG and CDK2 in association with active histone marks, promoting migration, invasion, and chemoresistance [PMID:30646949, PMID:33773404], and it interacts with RBM39 to regulate MKI67 pre-mRNA splicing, with its own expression epigenetically induced via p300-mediated H3K27ac [PMID:42061695]. Independently of these growth functions, the ankyrin repeat domain dimerizes and deforms membranes into tubules and vesicles, contributing to negative regulation of early endosome enlargement [PMID:31255983]. Additional reported activities include scaffolding with SHP2, interaction with SIVA to engage the Stathmin 1 pathway, and antiapoptotic regulation of caspases by a KH-domain-deficient splice variant [PMID:16956752, PMID:16098192, PMID:25523139].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding, GO:0060090 molecular adaptor activity, GO:0140110 transcription regulator activity, GO:0008289 lipid binding, GO:0042393 histone binding
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0005886 plasma membrane, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1640170 Cell Cycle, R-HSA-74160 Gene expression (Transcription), R-HSA-8953854 Metabolism of RNA, R-HSA-5653656 Vesicle-mediated transport
- **partners:** SHP2, SIVA, YAP1, CDK4, SMYD3, RBM39, MALAT1, CDKN1A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | Medium | ANKHD1 protein is detected in the cytosolic and membrane fractions of cells and co-immunoprecipitates with SHP2 in K562 and LNCaP cell lines, suggesting a scaffolding role in association with SHP2. | PMID:16956752 | Biochimica et biophysica acta |
| 2005 | Medium | A splice variant of ANKHD1 lacking the KH domain (VBARP) is primarily localized in the cytoplasm and is essential for cell survival through regulation of caspases, acting in an antiapoptotic capacity. | PMID:16098192 | The FEBS journal |
| 2014 | Medium | ANKHD1 binds to SIVA (identified by yeast two-hybrid and confirmed by co-immunoprecipitation), and ANKHD1 silencing leads to Stathmin 1 inactivation and reduced cell migration and proliferation in leukemia cells, likely by inhibiting the SIVA/Stathmin 1 association. | PMID:25523139 | Biochimica et biophysica acta |
| 2014 | Medium | ANKHD1 is a positive regulator of YAP1 in prostate cancer cells; ANKHD1 silencing downregulates YAP1 expression and activation and reduces CCNA2 (Cyclin A) expression, thereby promoting cell cycle progression. | PMID:24726915 | Experimental cell research |
| 2012 | Medium | ANKHD1 silencing in multiple myeloma cells delays S-to-G2M cell cycle progression and upregulates the CDK inhibitor p21, irrespective of p53 status. | PMID:23142581 | FEBS letters |
| 2014 | Medium | ANKHD1 interacts with p21 (confirmed by Co-IP and ChIP) and represses the p21 promoter (demonstrated by luciferase reporter assay); ANKHD1 shuttles between cytoplasm and nucleus as shown by nuclear accumulation upon Leptomycin B treatment. | PMID:25483783 | European journal of cancer |
| 2018 | Medium | ANKHD1 physically interacts via its C-terminal KH domain with tumor-suppressing miRNAs (miR-29a, miR-205, miR-196a) as demonstrated by RNA immunoprecipitation, and drives ccRCC cell mitosis primarily by suppressing miR-29a, leading to upregulation of CCND1. | PMID:29695508 | The Journal of biological chemistry |
| 2019 | Medium | ANKHD1 interacts with SMYD3 (identified by mass spectrometry and confirmed functionally); ANKHD1 interacts with H3K4me3 in SMYD3-overexpressing cells and is required for SMYD3-dependent activation of SLUG gene transcription (associated with H3K4me3, H3K9Ac, H3K14Ac marks), promoting HCC migration and invasion. | PMID:30646949 | Journal of experimental & clinical cancer research |
| 2019 | High | The ankyrin repeat domain (ARD) of ANKHD1 dimerizes and deforms membranes into tubules and vesicles; specifically, the first 15 ANK repeats form a dimer and the latter 10 ANK repeats enable membrane tubulation/vesiculation via an adjacent amphipathic helix and a positively charged curved structure analogous to BAR domains. ANKHD1 knockdown and localization experiments indicate its involvement in negative regulation of early endosome enlargement. | PMID:31255983 | iScience |
| 2018 | Medium | ANKHD1 silencing in colorectal cancer cells reduces YAP1 expression and increases YAP1 phosphorylation, inhibits AKT phosphorylation, and suppresses EMT markers (MMP2, MMP9, vimentin, Snail, ZEB1); YAP1 overexpression reverses the effects of ANKHD1 knockdown, placing ANKHD1 upstream of YAP1 in this pathway. | PMID:30555746 | American journal of cancer research |
| 2020 | Medium | ANKHD1 interacts with SMYD3 as demonstrated by co-immunoprecipitation and immunofluorescence in NSCLC cells; SMYD3-mediated chemoresistance requires ANKHD1 as co-regulator, and SMYD3 transcriptionally regulates CDK2 promoter (by ChIP) in an ANKHD1-dependent manner. | PMID:33773404 | Translational oncology |
| 2020 | Low | ANKHD1 interacts with histone promoter regions (by ChIP) and its silencing downregulates all core histones, implicating ANKHD1 in histone synthesis during S phase; ANKHD1 silencing also reduces PCNA expression and leads to accumulation of γH2AX, indicating a role in DNA repair. | PMID:32562952 | Blood cells, molecules & diseases |
| 2022 | Medium | ANKHD1 and lncRNA MALAT1 interact (demonstrated by RIP and RNA pulldown); this ANKHD1/MALAT1/YAP1 feedback loop promotes YAP1 transcriptional coactivation and enhances radioresistance in CRC via the YAP1/AKT axis. | PMID:35110552 | Cell death & disease |
| 2025 | Medium | ANKHD1 binds to CDK4 and positively controls the Cyclin D1/CDK4 pathway, leading to increased retinoblastoma protein phosphorylation and cell proliferation in a p19-dependent but p21-independent manner; ANKHD1 knockout reduces cystic growth in vitro and in vivo in ADPKD models. | PMID:40457431 | Journal of translational medicine |
| 2025 | Low | ANKHD1 expression in a TauP301S-PS19 mouse model reduces hyperphosphorylated Tau and is associated with promotion of autophagy as a mechanism to mitigate Tau pathology; ANKHD1 expression restores cognitive performance in affected female PS19 mice. | PMID:40806649 | International journal of molecular sciences |
| 2026 | Medium | The acetyltransferase p300 mediates H3K27ac modification at the ANKHD1 promoter to upregulate ANKHD1 expression in response to NNK; ANKHD1 directly interacts with RBM39 to facilitate splicing and expression of MKI67 pre-mRNA, driving CRC cell proliferation and metastasis. | PMID:42061695 | Chemico-biological interactions |

## Citations

- PMID:16098192
- PMID:16956752
- PMID:23142581
- PMID:24726915
- PMID:25483783
- PMID:25523139
- PMID:29695508
- PMID:30555746
- PMID:30646949
- PMID:31255983
- PMID:32562952
- PMID:33773404
- PMID:35110552
- PMID:40457431
- PMID:40806649
- PMID:42061695
