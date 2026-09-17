---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AHNAK2
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q8IVF2
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AHNAK2 (human)

## Current model (mechanistic narrative)

AHNAK2 is a large submembrane scaffold protein that organizes membrane-proximal cytoskeletal architecture in muscle and engages multiple signaling modules to drive tumor cell invasion and survival [PMID:20833135, PMID:38751848]. In skeletal muscle it localizes to the costameric network, co-distributing with vinculin and excluded from the T-tubule system [PMID:20833135], and it binds directly to periaxin, an interaction whose disruption by compound heterozygous AHNAK2 mutations is linked to a Charcot-Marie-Tooth-type peripheral neuropathy/myelination defect in an affected family [PMID:31011849]. AHNAK2 also functions in nonclassical FGF1 secretion: under heat stress it associates with FGF1, translocates with it to the F-actin-rich submembrane cytoskeletal compartment, and is specifically required for stress-induced FGF1 export [PMID:25560297]. In cancer, AHNAK2 acts as a positive regulator of pro-invasive and pro-survival signaling, promoting TGF-β/Smad3-driven EMT [PMID:33363388], post-transcriptionally stabilizing c-MET protein to sustain HGF/c-MET signaling [PMID:38751848], and supporting the AKT/GSK-3β survival axis that confers chemotherapy resistance [PMID:40382757]. It additionally physically interacts with RUVBL1 and is required for G1/S cell cycle progression [PMID:37349884]. Across diverse epithelial cancers AHNAK2 knockdown consistently suppresses proliferation, migration, invasion, and EMT. The biochemical mechanism by which AHNAK2 connects to these signaling cascades has not been resolved in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005886 plasma membrane, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1640170 Cell Cycle
- **partners:** FGF1, PRX, RUVBL1, CTTN, MET
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | Medium | AHNAK2 associates with FGF1 in a heat shock-dependent manner (identified by immunoprecipitation mass spectrometry), and both proteins translocate to the cytoskeletal fraction upon heat stress, co-localizing with F-actin near the plasma membrane. Depletion of AHNAK2 drastically reduces stress-induced FGF1 export but does not affect spontaneous FGF2 export or Notch inhibition-induced FGF1 release, placing AHNAK2 as a specific component of the nonclassical FGF1 secretion pathway. | PMID:25560297 | Journal of cellular biochemistry |
| 2010 | Medium | AHNAK2 localizes to the costameric network in mouse skeletal muscle fibers, as demonstrated by co-localization with vinculin; no AHNAK2 expression was detected in the T-tubule system. | PMID:20833135 | Biochemical and biophysical research communications |
| 2019 | Medium | AHNAK2 binds directly to periaxin (PRX), the protein encoded by the CMT4F-associated PRX gene; compound heterozygous mutations in AHNAK2 in a CMT patient family result in significantly reduced AHNAK2 mRNA and protein levels, suggesting disruption of the AHNAK2-PRX interaction impairs myelination. | PMID:31011849 | Neurogenetics |
| 2020 | Medium | AHNAK2 knockdown in lung adenocarcinoma cells suppresses migration, invasion, and EMT, and inhibits TGF-β1-induced Smad3 phosphorylation. When p-Smad3 is pharmacologically inhibited, AHNAK2 knockdown has no additional effect, placing AHNAK2 upstream of or at the level of Smad3 phosphorylation in the TGF-β/Smad3 pathway. | PMID:33363388 | OncoTargets and therapy |
| 2020 | Low | AHNAK2 knockdown in lung adenocarcinoma A549 cells decreases phosphorylation of MEK, ERK, and p90RSK, and produces effects similar to the MEK inhibitor U0126, placing AHNAK2 as a positive regulator of the MAPK (MEK/ERK) signaling pathway to promote proliferation, migration, and invasion. | PMID:33000678 | Technology in cancer research & treatment |
| 2021 | Low | AHNAK2 knockdown reduces nuclear factor kappa B (NF-κB) pathway activity in thyroid carcinoma cells, as shown by decreased NF-κB signaling markers, inhibiting migration, invasion, and metastasis. | PMID:34627772 | Life sciences |
| 2021 | Low | AHNAK2 knockdown in thyroid carcinoma cells inhibits proliferation, metastasis, and EMT, and reduces β-catenin and cyclin D1 protein levels; AHNAK2 overexpression has the opposite effect. Rescue with LiCl (Wnt activator) or ICG-001 (Wnt inhibitor) counteracts the effects of AHNAK2 knockdown or overexpression, respectively, placing AHNAK2 as a positive regulator of the Wnt/β-catenin pathway. | PMID:34374294 | Neoplasma |
| 2021 | Low | Knockdown of AHNAK2 in ESCC cell lines increases radioresistance, and transcriptome analysis indicates AHNAK2 regulates expression of interleukins, interleukin receptors, and chemokines by inhibiting NF-κB and TNF signaling pathways, suppressing immune response in radioresistant cells. | PMID:33633453 | OncoTargets and therapy |
| 2023 | Medium | AHNAK2 physically interacts with RUVBL1 (identified by co-immunoprecipitation and mass spectrometry); AHNAK2 knockdown causes G1/S phase cell cycle arrest in lung adenocarcinoma cells, and GSEA/RNA-seq implicate AHNAK2 in the mitotic cell cycle, DNA replication, and NF-κB signaling. | PMID:37349884 | Thoracic cancer |
| 2024 | Medium | AHNAK2 promotes pancreatic ductal adenocarcinoma progression by preventing c-MET protein degradation (post-transcriptional stabilization), maintaining persistent HGF/c-MET signaling; AHNAK2 and c-MET show significant positive correlation at the protein level but not mRNA level, and AHNAK2 knockdown reduces c-MET protein in response to HGF treatment. | PMID:38751848 | Cancer management and research |
| 2024 | Low | AHNAK2 knockdown in pancreatic cancer cells decreases phosphorylated p65, phosphorylated IκBα, and MMP-9 expression; NF-κB activation reverses the effects of AHNAK2 knockdown, placing AHNAK2 upstream of the NF-κB/MMP-9 axis in pancreatic cancer progression. | PMID:38864962 | Biochemical genetics |
| 2024 | Low | AHNAK2 promotes differentiated thyroid cancer cell proliferation, migration, and invasion; knockdown reduces phospho-PI3K p85 and phospho-AKT levels, placing AHNAK2 as a positive regulator of the PI3K/AKT signaling pathway. | PMID:36089788 | Current cancer drug targets |
| 2025 | Low | AHNAK2 co-localizes with Cortactin in filopodia in pancreatic cancer cell lines that show diffuse cytoplasmic AHNAK2 distribution; this co-localization increases on fibronectin, collagen substrates, and in hypoxia, and correlates with augmented cancer cell invasion. Cell lines with vesicular AHNAK2 staining do not show these changes. | PMID:39849106 | Scientific reports |
| 2025 | Medium | AHNAK2 knockdown in 5-FU-resistant colorectal cancer cells reduces resistance to 5-FU and suppresses PCNA, CDK4, p-AKT, and p-GSK-3β while increasing cleaved caspase-3 and E-cadherin; AHNAK2 overexpression produces opposite effects both in vitro and in vivo, placing AHNAK2 as an activator of the AKT/GSK-3β survival axis that confers chemotherapy resistance. | PMID:40382757 | Clinical and experimental medicine |
| 2026 | Low | AHNAK2 knockdown in gastric cancer cells reduces proliferation, invasion, and migration while increasing apoptosis; RNA sequencing and western blot analysis confirm that AHNAK2 mediates GC progression through the Wnt/β-catenin signaling pathway. | PMID:41655165 | Discover oncology |

## Citations

- PMID:20833135
- PMID:25560297
- PMID:31011849
- PMID:33000678
- PMID:33363388
- PMID:33633453
- PMID:34374294
- PMID:34627772
- PMID:36089788
- PMID:37349884
- PMID:38751848
- PMID:38864962
- PMID:39849106
- PMID:40382757
- PMID:41655165
