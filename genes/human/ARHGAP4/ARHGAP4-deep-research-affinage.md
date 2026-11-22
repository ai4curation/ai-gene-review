---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P98171
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 13
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGAP4 (human)

## Current model (mechanistic narrative)

ARHGAP4 is a multi-domain Rho GTPase-activating protein that integrates cytoskeletal regulation with the control of cell and axon motility [PMID:12414125, PMID:17804252]. Recombinant ARHGAP4 stimulates the intrinsic GTPase activity of Rac1, Cdc42, and RhoA, establishing it as a functional GAP for multiple Rho-family members [PMID:12414125]. Its modular architecture partitions these activities: the FCH domain directs localization to the leading edges of migrating cells and to axon growth cones, while the GAP domain and C-terminus are required for its inhibition of cell migration and axon outgrowth [PMID:17804252]. Through its RhoGAP and SH3 domains, ARHGAP4 assembles a complex with the septins SEPT2 and SEPT9 that reorganizes focal adhesions and modulates integrin-β1–dependent migration and invasion [PMID:34524873], and it suppresses epithelial-to-mesenchymal transition and focal-adhesion–driven force generation, with Septin9 acting as a negative regulator that promotes EMT via FAK/Src signaling [PMID:32378260]. Beyond its canonical GAP role, ARHGAP4 functions as a scaffolding and regulatory protein in cancer: it promotes ubiquitination of HDAC2 to suppress β-catenin activation and tumor cell invasion [PMID:30958531], binds p53 to repress DRAM1-dependent apoptosis in acute myeloid leukemia [PMID:37443303], and drives colorectal cancer stemness through a MYH9/β-catenin/c-Jun feedback loop [PMID:40817404]. Its expression is suppressed by miR-939-5p [PMID:32021284].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060089 molecular transducer activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005794 Golgi apparatus, GO:0005856 cytoskeleton, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease
- **partners:** SEPT2, SEPT9, HDAC2, TP53, MYH9
- **complexes:** ARHGAP4–SEPT2–SEPT9 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | Recombinant ARHGAP4 stimulates the GTPase activity of Rac1, Cdc42, and RhoA in vitro, establishing it as a functional GAP for multiple Rho family members. | PMID:12414125 | Brain research. Molecular brain research |
| 2002 | Medium | Endogenous ARHGAP4 localizes to the Golgi complex and can redistribute to microtubules during mitosis; it is also detected at the tips of differentiating neurites in PC12 cells. | PMID:12414125 | Brain research. Molecular brain research |
| 2007 | Medium | The FCH domain of ARHGAP4 is required for localizing the protein to the leading edges of migrating NIH/3T3 cells and to axon growth cones, while the GAP domain and C-terminus are necessary for ARHGAP4-mediated inhibition of cell migration and axon outgrowth. | PMID:17804252 | Molecular and cellular neurosciences |
| 2007 | Medium | Overexpression of ARHGAP4 inhibits NIH/3T3 cell migration and hippocampal axon outgrowth, establishing a functional role as an inhibitor of cell and axon motility. | PMID:17804252 | Molecular and cellular neurosciences |
| 2019 | Medium | ARHGAP4 interacts with and promotes ubiquitination of HDAC2, which in turn inhibits β-catenin activation, suppressing MMP2/MMP9 expression and pancreatic cancer cell invasion and migration. | PMID:30958531 | Carcinogenesis |
| 2019 | Medium | ARHGAP4 overexpression inhibits cell viability, glucose uptake, lactate release, PKM2 expression, and mTOR/HIF-1α pathway activation in pancreatic cancer cells; mTOR inhibitor (rapamycin) or HIF-1α inhibitor (YC-1) rescues the morphological changes induced by ARHGAP4 downregulation, placing ARHGAP4 upstream of the mTOR/HIF-1α axis in the Warburg effect. | PMID:31303760 | OncoTargets and therapy |
| 2020 | Medium | miR-939-5p directly targets and suppresses ARHGAP4 expression (validated by luciferase reporter assay), thereby promoting pancreatic cancer cell viability, invasion, and migration; ARHGAP4 overexpression reverses these effects. | PMID:32021284 | OncoTargets and therapy |
| 2020 | Medium | ARHGAP4 suppresses epithelial-to-mesenchymal transition (EMT) in human mammary epithelial cells, regulating epithelial/mesenchymal marker expression, cell proliferation, migration, 3D morphogenesis, and focal adhesion/stress fiber-driven force generation; Septin9 was identified by proteomics as a negative regulator of ARHGAP4 that promotes EMT via FAK/Src signaling. | PMID:32378260 | FASEB journal |
| 2021 | High | ARHGAP4 forms a complex with SEPT2 and SEPT9 via its RhoGAP domain and SH3 domain; silencing ARHGAP4 or overexpressing SEPT2/SEPT9 independently induces reorganization of focal adhesions with upregulation of Integrin Beta 1, enhancing cell migration and invasion in a microenvironment-dependent manner. | PMID:34524873 | Molecular biology of the cell |
| 2023 | Medium | ARHGAP4 binds p53 to inhibit DRAM1 expression in AML cells; ARHGAP4 knockdown activates DRAM1 signaling and induces apoptosis, while DRAM1 knockdown rescues the defects caused by ARHGAP4 deletion, placing ARHGAP4 upstream of p53/DRAM1 in AML leukemogenesis. | PMID:37443303 | Oncogene |
| 2024 | Low | ARHGAP4 knockdown inhibits migration and invasion of colon cancer cells and decreases expression of TGF-β1, p-Smad2, and p-Smad3, while increasing E-cadherin and decreasing N-cadherin/Vimentin, placing ARHGAP4 upstream of the TGF-β/Smad pathway and EMT in colon cancer. | PMID:38805788 | Biochemical and biophysical research communications |
| 2024 | Low | ARHGAP4 promotes apoptosis and inflammation in ovarian granulosa cells via the PI3K-Akt signaling pathway. | PMID:38355537 | Journal of ovarian research |
| 2025 | Medium | ARHGAP4 drives colorectal cancer stemness through a positive feedback loop with MYH9/β-catenin/c-Jun, as demonstrated by co-immunoprecipitation (ARHGAP4-MYH9 interaction), chromatin immunoprecipitation (c-Jun binding), and FRAP. | PMID:40817404 | NPJ precision oncology |

## Citations

- PMID:12414125
- PMID:17804252
- PMID:30958531
- PMID:31303760
- PMID:32021284
- PMID:32378260
- PMID:34524873
- PMID:37443303
- PMID:38355537
- PMID:38805788
- PMID:40817404
