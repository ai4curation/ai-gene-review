---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF15
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O94989
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF15 (human)

## Current model (mechanistic narrative)

ARHGEF15 (Vsm-RhoGEF/Ephexin5) is a Rho guanine nucleotide exchange factor that couples receptor signaling to actin cytoskeletal remodeling and is required for vascular development [PMID:12775584, PMID:23029280]. In vascular smooth muscle cells it associates with the EphA4 receptor; ephrin-A1 stimulation drives EphA4-mediated tyrosine phosphorylation of ARHGEF15, enhancing its exchange activity toward RhoA and promoting actin stress fiber assembly [PMID:12775584]. In endothelial cells it acts downstream of VEGF to activate Cdc42 while potentiating inactivation of RhoJ, driving actin polymerization and cell motility; its genetic disruption in mice delays postnatal retinal vascular network extension [PMID:23029280, PMID:24397187], and it operates upstream of STAT3 phosphorylation to promote endothelial migration [PMID:41359253]. Loss-of-function ARHGEF15 mutations produce RhoA/ROCK2 inactivation and F-actin disorganization in vascular cells and impair Wnt/β-catenin signaling in osteoblasts, with a knock-in transgenic mouse recapitulating cerebral small vessel disease and severe osteoporosis [PMID:36929019]. Beyond the vasculature, amyloid-β acutely upregulates Ephexin5 in hippocampal neurons to drive dendritic spine loss and cognitive impairment, effects reversed by genetic or shRNA-mediated Ephexin5 reduction [PMID:28346227], and Sertoli-cell-specific deletion disrupts blood-testis barrier integrity and testicular immune privilege [PMID:36001358].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-1643685 Disease
- **partners:** EPHA4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2003 | High | Vsm-RhoGEF (ARHGEF15) is expressed specifically in vascular smooth muscle cells (VSMCs) and associates with EphA4 receptor in quiescent cells. Upon ephrin-A1 stimulation, EphA4 tyrosine-phosphorylates Vsm-RhoGEF, enhancing its GEF activity toward RhoA. Dominant-negative Vsm-RhoGEF or RNAi depletion blocked ephrin-A1-induced actin stress fiber assembly in VSMCs, establishing an ephrin-A1 → EphA4 → Vsm-RhoGEF → RhoA pathway controlling vascular smooth muscle contractility. | PMID:12775584 | Circulation research |
| 2012 | High | Arhgef15 acts as an endothelial cell-specific RhoGEF that mediates VEGF-induced Cdc42 activation and potentiates RhoJ inactivation, thereby promoting actin polymerization and endothelial cell motility. Genetic disruption of Arhgef15 in mice caused delayed extension of vascular networks and reduced total vessel areas in postnatal retinas. | PMID:23029280 | PloS one |
| 2012 | Medium | Arhgef15 knockout mice display impaired neonatal retinal vascularization, demonstrating a required role for Arhgef15 in endothelial cell-driven vascular development in vivo. | PMID:22535667 | Blood |
| 2013 | Medium | A de novo mutation in ARHGEF15 identified in a child with epileptic encephalopathy reduced the GEF exchange activity of the Ephexin5 protein by approximately 50% in cell-based in vitro assays. | PMID:23647072 | Epilepsia |
| 2013 | Medium | Arhgef15 (an EC-specific RhoGEF) inactivates RhoJ downstream of VEGF signaling in endothelial cells, promoting retinal vascular growth through cytoskeletal rearrangement and cell motility. | PMID:24397187 | Nippon Ganka Gakkai zasshi |
| 2017 | High | Amyloid-β (Aβ) acutely promotes production of Ephexin5 (ARHGEF15) in mature hippocampal neurons. Elevated Ephexin5 drives hippocampal dendritic spine loss and cognitive impairment in hAPP mice (familial AD model). Genetic removal of Ephexin5 eliminated dendritic spine loss and rescued AD-associated behavioral deficits; selective shRNA reduction in the dentate gyrus of presymptomatic hAPP mice was sufficient to prevent cognitive impairment. | PMID:28346227 | The Journal of clinical investigation |
| 2023 | High | Loss-of-function mutations in ARHGEF15 cause RhoA/ROCK2 inactivation leading to F-actin cytoskeleton disorganization in vascular smooth muscle cells and endothelial cells, and inhibit Wnt/β-catenin signaling in osteoblasts. Arhgef15-e(V368M) transgenic mice developed cerebral small vessel disease-like pathological and behavioral phenotypes with severe osteoporosis. | PMID:36929019 | Acta neuropathologica |
| 2022 | High | SC-specific deletion of Arhgef15 in mice disrupted Sertoli cell nuclear localization, impaired blood-testis barrier (BTB) integrity, caused premature germ cell shedding, and led to abnormal sperm morphology (acrosome degeneration, acrosomal vesicle shedding, atrophic nuclei). RNA-seq revealed that differentially expressed genes in Sertoli cells of knockout mice were predominantly immunity-associated, and knockout mice produced antibodies against testicular autoantigens, indicating loss of testicular immune privilege. | PMID:36001358 | Biology of reproduction |
| 2023 | Medium | Constitutive Arhgef15 knockout mice are fertile with complete spermatogenesis; deletion does not affect undifferentiated spermatogonia proliferation or differentiation, but decreases expression of Nanos2, Lin28a, and Ddx4 in the testis. | PMID:36603298 | Reproductive biology |
| 2018 | Low | miR-193a promotes pancreatic cancer metastasis by repressing the TGF-β2/TGF-βRIII/ARHGEF15/ABL2 pathway; ARHGEF15 is placed downstream of TGF-βRIII in a pathway restraining cancer cell metastasis. | PMID:29433538 | Journal of experimental & clinical cancer research |
| 2025 | Medium | ARHGEF15 overexpression promotes HUVEC migration and increases STAT3 phosphorylation; ARHGEF15 knockdown inhibits migration. Inhibition of STAT3 with STATTIC blocks ARHGEF15-overexpression-induced STAT3 phosphorylation and HUVEC migration, placing ARHGEF15 upstream of STAT3 in endothelial cell migration. | PMID:41359253 | Current medical science |

## Citations

- PMID:12775584
- PMID:22535667
- PMID:23029280
- PMID:23647072
- PMID:24397187
- PMID:28346227
- PMID:29433538
- PMID:36001358
- PMID:36603298
- PMID:36929019
- PMID:41359253
