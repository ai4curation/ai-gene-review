---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATG9B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q674R7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATG9B (human)

## Current model (mechanistic narrative)

ATG9B is a tissue-specific functional ortholog of yeast Atg9p that drives autophagosome biogenesis by delivering membrane lipids to the growing phagophore [PMID:15755735, PMID:37938170]. It assembles as a conserved homotrimer that functions as a lipid scramblase, recapitulates the subcellular trafficking and steady-state distribution of ATG9A, can compensate for ATG9A loss in starvation-induced autophagy, and forms a heteromeric complex with the lipid-transfer protein ATG2A [PMID:37938170]. In autophagosome formation it acts upstream of cargo docking, facilitating recruitment of LC3 and p62-associated ubiquitinated proteins to nascent phagophores, such that its loss sensitizes cells to ER stress-induced death through accumulation of ubiquitinated substrates [PMID:28740555]. Beyond canonical autophagy, ATG9B has distinct context-dependent roles: it is stabilized by and trafficked with MYH9 to the cell edge, where it accelerates focal adhesion assembly by promoting integrin β1–Talin-1 interaction and integrin β1 activation to drive cancer invasion in an autophagy-independent manner [PMID:34131310]; it controls actin depolymerization during bacterial internalization under ULK1 kinase control, with its loss causing accumulation of actin filaments and phosphorylated LIM kinase and cofilin [PMID:38706859]; and it localizes to mitochondria via an N-terminal targeting sequence, where its expression collapses mitochondrial membrane potential, promotes mtDNA release, and triggers apoptosis [PMID:41811769]. ATG9B expression is set by multiple transcriptional and post-transcriptional inputs, including suppression by several exosomal miRNAs and activation through ASCL2 and Wnt/β-catenin signaling in cancer stemness and drug resistance [PMID:28740555, PMID:35971776, PMID:35882624, PMID:41495834]. A homozygous frameshift truncating the C-terminal cytosolic domain causes a rare human neurodevelopmental disorder, and the truncated protein is unstable and fails to reach peripheral vesicles, defining the C-terminal domain as required for peripheral trafficking.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0031410 cytoplasmic vesicle, GO:0005739 mitochondrion, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-9612973 Autophagy, R-HSA-5357801 Programmed Cell Death
- **partners:** ATG2A, MYH9, STUB1, ULK1
- **complexes:** ATG9B-ATG2A complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Medium | ATG9B (APG9L2) localizes primarily to the perinuclear region and also as cytosolic dots that partially colocalize with the autophagosome marker LC3 under starvation conditions, and can functionally complement ATG9A (APG9L1) knockdown to restore starvation-induced autophagosome formation in HeLa cells, establishing it as a functional ortholog of yeast Atg9p. | PMID:15755735 | The Journal of biological chemistry |
| 2023 | High | Human ATG9B forms a conserved homotrimeric structure (determined by cryo-EM), functions as a lipid scramblase, displays similar subcellular trafficking and steady-state localization to ATG9A, can compensate for ATG9A absence in starvation-induced autophagy, and forms a heteromeric complex with ATG2A. | PMID:37938170 | Autophagy |
| 2020 | Medium | siRNA knockdown of Atg9b in cardiomyocyte-derived cells reduces autophagosome formation, and Atg9b protein levels are specifically reduced in aged mouse hearts correlating with decreased autophagic activity, demonstrating Atg9b is required for autophagosome biogenesis in cardiac cells. | PMID:32627317 | Aging cell |
| 2017 | Medium | Atg9b-deficient hepatocytes are vulnerable to ER stress-induced cell death due to accumulation of ubiquitinated proteins, and loss of Atg9b blocks recruitment of p62-associated ubiquitinated proteins to autophagosomes; Atg9b-driven phagophores facilitate docking of both LC3 and p62 to initiate autophagy-associated degradation. Additionally, miR-3091-3p from tumor-derived exosomes suppresses Atg9b expression. | PMID:28740555 | Theranostics |
| 2021 | High | ATG9B promotes colorectal cancer invasion in an autophagy-independent manner: MYH9 directly binds to cytoplasmic residues aa368-411 of ATG9B via its head domain; their interaction stabilizes both proteins by reducing binding to the E3 ubiquitin ligase STUB1, preventing ubiquitin-mediated degradation. ATG9B is transported to the cell edge with MYH9 assistance and accelerates focal adhesion assembly by mediating interaction between endocytosed integrin β1 and Talin-1, promoting integrin β1 activation. | PMID:34131310 | Cell death and differentiation |
| 2019 | Medium | HPV16 E7 protein physically interacts with ATG9B (shown by immunoprecipitation), and HPV16 E6 likely transcriptionally regulates ATG9B through the -1750 to -2000 nt region of its promoter (dual-luciferase reporter). Overexpression of ATG9B partially compensates for autophagy blockage caused by 16E6/E7 knockdown. | PMID:31215164 | Cancer medicine |
| 2022 | Medium | miR-7002-5p (from high-glucose macrophage-derived exosomes) directly targets ATG9B, as confirmed by dual-luciferase reporter assay; suppression of ATG9B by miR-7002-5p inhibits autophagy in tubular epithelial cells, inducing dysfunction and inflammation. | PMID:35971776 | FASEB journal |
| 2022 | Medium | ASCL2 transcriptionally regulates ATG9B expression to maintain stemness properties (self-renewal and tumor-propagation potential) in glioma cells; the ASCL2-ATG9B axis is required for autophagic activity and stemness maintenance. | PMID:35882624 | Advanced science |
| 2024 | Medium | ATG9B regulates internalization of various invasive bacteria by controlling actin rearrangement; ATG9B knockdown causes accumulation of actin filaments and phosphorylated LIM kinase and cofilin, indicating ATG9B promotes actin depolymerization. ULK1 kinase activity regulates ATG9B localization and actin remodeling. | PMID:38706859 | iScience |
| 2023 | Medium | ATG9b upregulation by propranolol in hepatic stellate cells enhances P62 recruitment to ATG5-ATG12-LC3 compartments and increases co-localization of P62 with ubiquitinated proteins; the PI3K/AKT/mTOR pathway mediates ATG9b-induced autophagic cell death, while p38/JNK is involved in apoptosis. | PMID:37970991 | Journal of cellular and molecular medicine |
| 2026 | Medium | ATG9B localizes prominently to mitochondria (distinct from ATG9A), where its expression induces aberrant mitochondrial morphology, reduces mitochondrial membrane potential, and promotes mtDNA release and apoptotic cell death. The N-terminal sequence of ATG9B functions as a mitochondrial targeting domain, and expression of this peptide alone is sufficient to induce apoptosis. | PMID:41811769 | Molecular biology of the cell |
| 2024 | Medium | A homozygous 11-nucleotide deletion/frameshift mutation in ATG9B (truncating the C-terminal cytosolic domain) causes a rare neurodevelopmental disorder in humans. The truncated ATG9B protein is unstable in cells and localizes only to perinuclear vesicles but not peripheral vesicles (unlike wild-type ATG9B), indicating the C-terminal domain is required for peripheral vesicle trafficking. | — | bioRxiv (preprint) |
| 2024 | Low | ATG9A and ATG9B show distinct subcellular localizations in uterine epithelial cells: ATG9A distributes in a punctate pattern while ATG9B forms elongated tubular shapes in the cytoplasm, suggesting isoform-specific roles in autophagy. | PMID:38757275 | Clinical and experimental reproductive medicine |
| 2025 | Medium | miR-30c-1-3p directly targets ATG9B (and ATG4B) during M. tuberculosis infection in macrophages; overexpression of ATG9B (alone or with ATG4B) reversed miR-30c-1-3p-mediated autophagy inhibition, demonstrating ATG9B is required for autophagy-mediated antimycobacterial defense. | PMID:40133377 | Scientific reports |
| 2026 | Medium | ATG9B mediates CBX2-induced autophagy and cisplatin resistance in ovarian cancer; CBX2 stabilizes β-catenin via SIAH2-mediated inhibition of ubiquitin-mediated degradation, and ATG9B inhibition rescues the effects of CBX2-mediated autophagy and drug resistance, placing ATG9B downstream of the Wnt/β-catenin pathway in autophagy regulation. | PMID:41495834 | Journal of ovarian research |

## Citations

- PMID:15755735
- PMID:28740555
- PMID:31215164
- PMID:32627317
- PMID:34131310
- PMID:35882624
- PMID:35971776
- PMID:37938170
- PMID:37970991
- PMID:38706859
- PMID:38757275
- PMID:40133377
- PMID:41495834
- PMID:41811769
