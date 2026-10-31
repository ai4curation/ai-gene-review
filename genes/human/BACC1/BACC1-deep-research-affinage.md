---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BACC1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8IXM2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BACC1 (human)

## Current model (mechanistic narrative)

BAP18 (BACC1/C17orf49) is a chromatin-associated H3K4me3 reader that operates as a context-dependent transcriptional co-regulator, bridging sequence-specific nuclear receptors and transcription factors to histone-modifying and chromatin-remodeling machineries at target promoters and enhancers [PMID:27226492, PMID:32986841]. As a coactivator, BAP18 is recruited to androgen-response elements and estrogen-induced gene promoters where it facilitates recruitment of the MLL1/COMPASS-like complex and AR or ERα, increasing H3K4me3 and H4K16 acetylation to drive transcription and cancer cell growth [PMID:27226492, PMID:32986841]. Its reader activity targets it to H3K4me3-marked promoters of growth and effector genes including CCND1/CCND2, S100A9, and CYP19A1, coupling chromatin engagement to G1-S progression and tumor growth [PMID:32113162, PMID:35484101, PMID:33662476]. BAP18 diversifies its mechanism across complexes and pathways: it recruits the NuA4/TIP60 complex to boost H4 acetylation during PPARα-mediated lipogenic transcription [PMID:38042310], partners with SMARCA1/BPTF to enable CTCF recruitment, enhancer accessibility, eRNA transcription, and enhancer-promoter looping at ERα enhancers [PMID:36828916], and recruits ACTL6A and PAF1 to potentiate β-catenin-driven Wnt target transcription [PMID:40818609]. In an opposing role, BAP18 can act as an AR corepressor by recruiting the SIN3A/HDAC subcomplex to AREs of P21 and PTEN, reducing local H4 acetylation and silencing these genes [PMID:41163225], establishing that BAP18 toggles between activating and repressive outputs depending on the associated complex and cellular context.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0042393 histone binding, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-162582 Signal Transduction, R-HSA-1640170 Cell Cycle
- **partners:** AR, ESR1, PPARA, SMARCA1, BPTF, ACTL6A, PAF1, CTNNB1
- **complexes:** MLL1/COMPASS-like complex, NuA4/TIP60 complex, SIN3A/HDAC complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | BAP18 acts as a coactivator of androgen receptor (AR) in both Drosophila and mammalian cells; it facilitates recruitment of the MLL1 subcomplex and AR to androgen-response elements (AREs) of AR target genes, increasing histone H3K4 trimethylation and H4K16 acetylation. BAP18 knockdown attenuates prostate cancer cell growth and xenograft tumor growth. | PMID:27226492 | Nucleic acids research |
| 2020 | Medium | BAP18 functions as an H3K4me3 reader; it is recruited to promoter regions of CCND1 and CCND2 in oral squamous cell carcinoma cells, facilitating recruitment of MLL1 complex core subunits to increase H3K4me3 levels and activate transcription, thereby promoting G1-S phase transition and cell growth. | PMID:32113162 | EBioMedicine |
| 2020 | High | BAP18 acts as a co-activator of ERα in breast cancer cells; it is recruited to promoter regions of estrogen-induced genes and facilitates recruitment of COMPASS-like core subunits, accompanied by enrichment of H3K4me3, in an E2-dependent manner. BAP18 promotes cell growth and modulates antiestrogen sensitivity. | PMID:32986841 | Nucleic acids research |
| 2022 | Medium | BAP18 is recruited to the H3K4me3-marked promoter of S100A9 in triple-negative breast cancer cells, enhancing its promoter activity and transcription. Knockdown of BAP18 suppresses xenograft tumor growth, an effect partially rescued by S100A9 re-expression, placing S100A9 downstream of BAP18. | PMID:35484101 | Cell death & disease |
| 2023 | High | BAP18 interacts with SMARCA1/BPTF and is required for CTCF recruitment to ERα-enriched enhancers; it facilitates chromatin accessibility within enhancer regions, promotes enhancer RNA transcription, and enhances enhancer-promoter looping. BAP18 depletion increases sensitivity to anti-estrogen and anti-enhancer treatment. | PMID:36828916 | Cell death and differentiation |
| 2021 | Medium | BAP18 interacts with androgen receptor (AR) and enhances AR-mediated transactivation in luteinized granulosa cells; BAP18 and AR co-recruit to AREs of CYP19A1 and FSHR promoters. BAP18 also interacts with Sp1 and co-recruits to the AR gene promoter to activate AR transcription. BAP18 knockdown decreases CYP19A1 expression and impairs androgen-to-estrogen conversion. | PMID:33662476 | Molecular and cellular endocrinology |
| 2023 | Medium | BAP18 co-activates PPARα-mediated transactivation in hepatocellular carcinoma cells and facilitates recruitment of the NuA4/TIP60 complex, thereby increasing histone H4 acetylation at SCD1 loci. BAP18 promotes HCC cell proliferation and lipid accumulation. | PMID:38042310 | Biochimica et biophysica acta. Molecular basis of disease |
| 2025 | Medium | BAP18 recruits ACTL6A and PAF1 to Wnt target gene promoters, enhancing β-catenin-mediated transcription in NSCLC cells. Co-immunoprecipitation confirmed interaction between BAP18, β-catenin, ACTL6A, and PAF1; luciferase reporter assays showed increased β-catenin transcriptional activity. BAP18 knockdown inhibited NSCLC cell proliferation, migration, and xenograft tumor growth. | PMID:40818609 | The Journal of biological chemistry |
| 2025 | Medium | In AR-positive triple-negative breast cancer cells, BAP18 acts as a transcriptional corepressor of AR by associating with AR and the SIN3A/HDAC subcomplex. BAP18 facilitates SIN3A/HDAC recruitment to AREs in promoters of P21 and PTEN, reducing histone H4 acetylation at those sites and suppressing their expression. | PMID:41163225 | Cell & bioscience |
| 2022 | Low | BAP18 knockdown in NSCLC cell lines (A549, H1299) reduces transcriptional levels of CCND1 and CCND2, delays G1-to-S phase transition, and weakens NSCLC cell growth, indicating BAP18 regulates CCND1/2 transcription to promote cell cycle progression. | PMID:35587057 | European review for medical and pharmacological sciences |

## Citations

- PMID:27226492
- PMID:32113162
- PMID:32986841
- PMID:33662476
- PMID:35484101
- PMID:35587057
- PMID:36828916
- PMID:38042310
- PMID:40818609
- PMID:41163225
