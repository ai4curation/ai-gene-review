---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTL8
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9H568
self_evaluation_pairwise: 
faith_pct: 85.71428571428571
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTL8 (human)

## Current model (mechanistic narrative)

ACTL8 (CT57) is a cancer-testis antigen that functions as an oncogenic driver across multiple epithelial cancers, where it promotes proliferation, migration, invasion, and cell cycle progression while restraining apoptosis [PMID:33883901, PMID:31962007]. Loss-of-function studies in triple-negative breast cancer, gastric cancer, oral squamous cell carcinoma, lung adenocarcinoma, and endometrial cancer consistently show that ACTL8 silencing suppresses tumor cell growth and motility, an effect reproduced in nude-mouse xenografts [PMID:33883901, PMID:35051678, PMID:31962007, PMID:32125225]. Mechanistically, ACTL8 acts upstream of PI3K/AKT/mTOR signaling: knockdown reduces pathway phosphorylation and pharmacological pathway modulators reverse or mimic the ACTL8 phenotype in both breast and gastric cancer models [PMID:33883901, PMID:39322809]. ACTL8 sustains a cell-cycle and proliferation transcriptional program, supporting expression of FOXM1, STMN1, PLK1, BIRC5, CDK1, cyclin B2, cyclin E1, and c-Myc, while its loss derepresses p21 and shifts EMT markers toward an epithelial state [PMID:35051678, PMID:35116946, PMID:32125225]. ACTL8 additionally drives MYC-dependent glutamine metabolism through SLC1A5 and GLS1, maintaining redox homeostasis; MYC re-expression rescues the metabolic phenotype but not p-AKT, placing ACTL8 above both axes [PMID:41621692]. The small molecule Momordin Ic binds ACTL8 directly and destabilizes it via ubiquitin-proteasome degradation, establishing ACTL8 as a druggable target [PMID:41621692]. ACTL8 protein is detected in the cytoplasm of tumor cells [PMID:41129177].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1640170 Cell Cycle, R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | Medium | ACTL8 knockdown in TNBC cells (MDA-MB-231 and BT-549) suppressed proliferation, migration, and invasion, and promoted apoptosis. Western blot showed that silencing ACTL8 inhibited phosphorylation of PI3K/AKT/mTOR pathway components. PI3K/AKT/mTOR pathway inhibitor (Wortmannin) enhanced these effects, while pathway activator (740Y-P) reversed them, placing ACTL8 upstream of PI3K/AKT/mTOR signaling. | PMID:33883901 | OncoTargets and therapy |
| 2024 | Medium | ACTL8 overexpression in gastric cancer (GC) cells increased phosphorylation of PI3K/AKT/mTOR signaling proteins, while ACTL8 knockdown reduced GC cell proliferation, migration, and invasion. PI3K/AKT/mTOR pathway inhibitors reversed the effects of ACTL8 overexpression, confirming ACTL8 acts upstream of this pathway in GC. | PMID:39322809 | Digestive diseases and sciences |
| 2021 | Medium | Knockdown of ACTL8 in oral squamous cell carcinoma (OSCC) cells inhibited growth and mobility, arrested the cell cycle, and promoted apoptosis. Western blot confirmed downregulation of cell cycle signaling proteins CDK1, cyclin E1, cyclin B2, and c-Myc, placing ACTL8 as a positive regulator of the cell cycle signaling pathway in OSCC. | PMID:35051678 | Tissue & cell |
| 2019 | Medium | Knockdown of ACTL8 in lung adenocarcinoma A549 cells inhibited cell proliferation and altered expression of 504 differentially expressed genes. qRT-PCR and Western blot confirmed downregulation of FOXM1, STMN1, PLK1, and BIRC5, and pathway analysis revealed inhibition of cyclin/cell cycle regulation pathways and activation of cell death pathways, identifying these as downstream effectors of ACTL8. | PMID:35116946 | Translational cancer research |
| 2020 | Medium | ACTL8 knockdown in lung adenocarcinoma cells (A549 and NCI-H1975) inhibited proliferation, colony formation, cell cycle progression, migration, invasion, and increased apoptosis in vitro, and inhibited tumor growth in nude mouse xenografts in vivo, demonstrating an oncogenic role for ACTL8 in LUAD. | PMID:31962007 | Thoracic cancer |
| 2020 | Low | Silencing ACTL8 in endometrial cancer cell lines (KLE and Ishikawa) reduced proliferation, migration, and invasion. Mechanistically, ACTL8 knockdown upregulated the cell cycle inhibitor p21 and epithelial marker E-cadherin, and downregulated cyclin A, MMP-9, and N-cadherin, indicating ACTL8 regulates cell cycle progression and epithelial-mesenchymal transition markers. | PMID:32125225 | Bioscience, biotechnology, and biochemistry |
| 2026 | Medium | ACTL8 knockdown (shRNA) in breast cancer cells reduced MYC expression and its downstream targets SLC1A5 and GLS1, suppressing glutamine metabolism and impairing redox homeostasis (reduced GSH/GSSG and NADPH/NADP+ ratios). MYC overexpression restored metabolic enzymes and phenotypes but failed to rescue p-AKT levels, placing ACTL8 upstream of PI3K/AKT/mTOR and upstream of MYC-driven glutamine metabolism. Surface plasmon resonance (SPR) and thermal shift assay (TSA) confirmed direct high-affinity binding of small molecule Momordin Ic to ACTL8, which destabilized ACTL8 and promoted its ubiquitin-proteasome degradation. | PMID:41621692 | Biochemical pharmacology |
| 2025 | Low | Immunohistochemistry on HNSCC tumor tissue confirmed ACTL8 protein expression (moderate focal cytoplasmic staining) in tumor cells, validating transcriptional upregulation at the protein level and supporting cytoplasmic localization of ACTL8 in cancer cells. | PMID:41129177 | JAMA otolaryngology-- head & neck surgery |

## Citations

- PMID:31962007
- PMID:32125225
- PMID:33883901
- PMID:35051678
- PMID:35116946
- PMID:39322809
- PMID:41129177
- PMID:41621692
