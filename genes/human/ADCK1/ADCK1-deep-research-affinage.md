---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADCK1
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q86TW2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADCK1 (human)

## Current model (mechanistic narrative)

ADCK1 is a mitochondria-associated kinase that maintains mitochondrial morphology, cristae architecture, and bioenergetic output by acting as an upstream regulator of mitochondrial dynamics [PMID:31125351]. Genetic epistasis in Drosophila and mammalian cells places ADCK1 upstream of YME1L1, which in turn controls OPA1 and IMMT; loss of ADCK1 causes excessive mitochondrial fusion, reduced membrane potential and ATP, and elevated ROS, while its overexpression drives fission, clustering, and cristae destruction, and these overexpression phenotypes are rescued by YME1L1 knockdown [PMID:31125351]. In mammalian cancer cells, ADCK1 is required for mitochondrial membrane potential, ATP production, and suppression of ROS, and its depletion impairs viability, proliferation, and migration while inducing apoptosis [PMID:36371387]. ADCK1 expression is controlled by upstream regulators: mTOR signaling sustains ADCK1 levels [PMID:36371387], and the transcription factor FOXQ1 directly regulates ADCK1 to preserve cristae organization and oxidative phosphorylation in brain endothelial cells [PMID:40884816]. Beyond its mitochondrial role, ADCK1 interacts with TCF4 to activate β-catenin/TCF signaling and promote tumorigenesis in colon cancer cells [PMID:33824271].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** YME1L1, TCF4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | Drosophila ADCK1 (dADCK1) loss-of-function causes premature death, defective locomotor activity, and structural muscle abnormalities with increased mitochondrial fusion, decreased membrane potential, ATP production, and increased ROS and apoptosis. ADCK1 over-expression induces mitochondrial fission, clustering, and cristae destruction. Genetic epistasis in flies and mammalian cells placed ADCK1 upstream of YME1L1, which in turn controls OPA1 and IMMT; knockdown of YME1L1 rescued ADCK1 over-expression phenotypes, establishing a mitochondrial signaling pathway: ADCK1 → YME1L1 → OPA1/IMMT for maintaining mitochondrial morphology and function in muscle. | PMID:31125351 | PLoS genetics |
| 2019 | Medium | Drosophila ADCK1 is necessary and sufficient in the trachea for larval viability; ADCK1 mutants die as second instar larvae with double mouth hooks and tracheal breaks. Tissue-specific genetic rescue confirmed tracheal requirement. Adult tracheal-rescued flies showed reduced lifespan, developmental delay, and reduced body size with normal basic metabolite levels. | PMID:31175694 | Developmental dynamics |
| 2021 | Medium | ADCK1 interacts with TCF4 (T-cell factor 4) to activate the β-catenin/TCF signaling pathway in colon cancer cells. ADCK1 upregulation promoted colony formation, infiltration, and organoid formation, while its downregulation inhibited these processes as well as in vivo tumorigenesis. | PMID:33824271 | Cell death & disease |
| 2022 | Medium | ADCK1 is a mitochondrial protein required for mitochondrial function in osteosarcoma cells; its depletion (shRNA or CRISPR/Cas9 KO) reduces cell viability, proliferation, and migration, induces apoptosis, reduces mitochondrial membrane potential and ATP, and increases ROS. mTOR signaling regulates ADCK1 expression: mTOR inhibitors (rapamycin, AZD2014) and mTOR shRNA decrease ADCK1 levels in osteosarcoma cells. | PMID:36371387 | Cell death & disease |
| 2025 | Medium | FOXQ1 directly regulates ADCK1 expression in brain endothelial cells, and ADCK1-dependent cristae organization is a key mechanism by which FOXQ1 maintains mitochondrial structural integrity. Conditional Foxq1 knockout in endothelial cells disrupts cristae morphology, reduces oxygen consumption, and impairs ATP production. | PMID:40884816 | Advanced science |

## Citations

- PMID:31125351
- PMID:31175694
- PMID:33824271
- PMID:36371387
- PMID:40884816
