---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF39
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N4T4
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF39 (human)

## Current model (mechanistic narrative)

ARHGEF39 (originally C9orf100) is a Dbl-family Rho guanine nucleotide exchange factor that drives cell proliferation, migration, and invasion across multiple epithelial cancers and marks proliferating neural progenitors [PMID:22327280, PMID:35959104]. Despite its predicted catalytic minimal unit (DH-PH domain) [PMID:22327280], direct activation assays establish RHOA as a substrate it activates, with concomitant induction of cell de-adhesion [PMID:35959104], while in lung adenocarcinoma it functions as an essential Rac1-GEF acting non-redundantly with FARP1 and TIAM2 to control membrane ruffle dynamics downstream of EGFR and c-Met activation [PMID:34731623]. Mechanistically, ARHGEF39 signals upstream of the PI3K/Akt and ERK pathways, and its proliferative and pro-motility effects are blunted by PI3K (LY294002) or ERK (PD98059) inhibition [PMID:28871449, PMID:33231603]. ARHGEF39 is a transcriptional target of E2F1, and high expression promotes hepatocellular carcinoma metastasis through enhanced fatty acid metabolism, with upregulation of FASN and EMT markers that is reversed by the FASN inhibitor Orlistat [PMID:39128592]. Its enzymatic regulation, structural basis for the apparent RHOA/Rac1 substrate divergence, and recruitment mechanism downstream of receptor tyrosine kinases remain uncharacterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | Medium | C9orf100 (ARHGEF39) was identified as a member of the Dbl-family GEFs containing a minimal catalytic unit (DH-PH domain). Ectopic expression promoted cell proliferation, colony formation, and migration in HCC cells, while silencing suppressed cell growth; flow cytometry indicated a function at the G2/M phase. | PMID:22327280 | Molecular medicine reports |
| 2017 | Medium | ARHGEF39 overexpression significantly increased phosphorylation of Akt (p-Akt) in gastric cancer cells, and the proliferative effect was attenuated by the PI3K inhibitor LY294002, placing ARHGEF39 upstream of PI3K/Akt signaling in cell proliferation and migration. | PMID:28871449 | Molecular and cellular biochemistry |
| 2020 | Medium | ARHGEF39 promotes viability, migration, and invasion of clear cell renal cell carcinoma cells by activating the AKT/ERK signaling pathway; knockdown reduced AKT and ERK phosphorylation, and pharmacological inhibition of AKT (LY294002) or ERK (PD98059) attenuated ARHGEF39-mediated motility. | PMID:33231603 | Genetics and molecular biology |
| 2021 | High | ARHGEF39 was identified as an essential Rac-GEF responsible for Rac1-mediated lung adenocarcinoma cell migration downstream of EGFR and c-Met activation. It operates non-redundantly with FARP1 and TIAM2 by controlling distinctive aspects of membrane ruffle dynamics. The AXL-Gab1-PI3K axis confers pro-motility traits downstream of EGFR in this context. | PMID:34731623 | Cell reports |
| 2022 | Medium | ARHGEF39 directly activates the Rho GTPase RHOA (not Rac1 as its family context might suggest), and high ARHGEF39 expression causes an increase in detached/de-adhered cells in culture. Single-cell RNA-seq analysis shows ARHGEF39 is a marker of proliferating neural progenitor cells and is co-expressed with cell-division genes, indicating a role in neurogenesis. | PMID:35959104 | Frontiers in molecular neuroscience |
| 2024 | Medium | ARHGEF39 is a transcriptional target of E2F1; E2F1 binding to the ARHGEF39 promoter was validated by ChIP and dual-luciferase reporter assays. High ARHGEF39 expression promotes HCC cell metastasis via enhanced fatty acid metabolism (FAM), as evidenced by increased neutral lipid accumulation, triglycerides, and phospholipids, upregulation of FASN, and EMT markers; the pro-metastatic effect was attenuated by the FASN inhibitor Orlistat. | PMID:39128592 | Clinics and research in hepatology and gastroenterology |

## Citations

- PMID:22327280
- PMID:28871449
- PMID:33231603
- PMID:34731623
- PMID:35959104
- PMID:39128592
