---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD55
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q3KP44
self_evaluation_pairwise: 
faith_pct: 83.33333333333333
n_discoveries: 9
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD55 (human)

## Current model (mechanistic narrative)

ANKRD55 is an ankyrin repeat protein predominantly expressed in CD4+ T cells that functions as an intrinsic regulator of T cell effector programs through control of both cytoskeletal organization and mitochondrial metabolism [PMID:41090353, PMID:40932625]. At the immune synapse, ANKRD55 binds subunits of the chaperonin-containing TCP1 (CCT) complex and competes with CCT5 for association with TCP1, CCT3, and CCT6, thereby promoting productive CCT assembly, microtubule organization, and TCR activation [PMID:41090353]. Metabolically, ANKRD55 associates with mitochondria and acts upstream of the LKB1 checkpoint: its loss impairs mitochondrial respiration and activates LKB1, suppressing TH17 IL-17 production, a phenotype rescued by concomitant LKB1 deletion [PMID:40932625]. Consistent with these cell-intrinsic roles, T cell-specific Ankrd55 ablation reduces CD4+ T cell proliferation, impairs TH17 differentiation and Th1 polarization, and attenuates EAE severity and neuroinflammation [PMID:41090353]. ANKRD55 protein is induced by inflammatory stimuli and elevated in CNS-infiltrating immune cells in EAE [PMID:27183579]. A broader interactome including cohesins, 14-3-3 proteins, clathrin, and cytoskeletal components, together with nuclear localization in T cells and dendritic cells, points to additional nuclear-associated roles that remain less defined in the available corpus [PMID:31620119, PMID:27183579, PMID:35111166].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005634 nucleus, GO:0005654 nucleoplasm, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-1430728 Metabolism
- **partners:** CCT5, TCP1, CCT3, CCT6, SMC1A, SMC3, VIM, CLTC
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | Medium | ANKRD55 interactome identified by recombinant overexpression in HEK293/HeLa cells and mass spectrometry; 148 interacting proteins found in total protein extracts and 22 in purified nuclear extracts. Validated interactions include RPS3, cohesins SMC1A and SMC3, CLTC, PRKDC, VIM, β-tubulin isoforms, and 14-3-3 isoforms, confirmed by western blot, reverse immunoprecipitation, and confocal microscopy. | PMID:31620119 | Frontiers in immunology |
| 2019 | Low | ANKRD55 harbors three phosphorylation sites, with S436 identified as the highest-scoring likely 14-3-3 binding phosphosite, suggesting regulation by (de)phosphorylation. | PMID:31620119 | Frontiers in immunology |
| 2019 | Low | Bioinformatic and localization analysis indicates ANKRD55 is likely transported into the nucleus via the classical nuclear import pathway and is involved in mitosis, possibly through effects on mitotic spindle dynamics, based on interactome enrichment in nuclear transport terms and interaction with β-tubulin isoforms. | PMID:31620119 | Frontiers in immunology |
| 2016 | Medium | ANKRD55 protein isoforms 005 and 001 are predominantly located in the nucleus of CD4+ T cells and Jurkat and U937 cells, as determined by direct imaging. | PMID:27183579 | Journal of immunology |
| 2016 | Medium | ANKRD55 protein expression is induced by inflammatory stimuli in primary murine hippocampal neurons and microglia, and is elevated in experimental autoimmune encephalomyelitis (EAE) mice, with CD4+ T cells and monocytes expressing ANKRD55 in CNS-infiltrating mononuclear cells. | PMID:27183579 | Journal of immunology |
| 2022 | Medium | ANKRD55 was detected in the nucleus of monocyte-derived dendritic cells (moDC) specifically in nuclear speckles; its expression increases during monocyte-to-moDC differentiation in the presence of IL-4/GM-CSF and is further enhanced by retinoic acid agonist AM580, but downregulated by IFN-γ and LPS-induced maturation. | PMID:35111166 | Frontiers in immunology |
| 2025 | High | ANKRD55 is associated with mitochondria, and its loss (Ankrd55 deletion in mice) impairs mitochondrial respiration and activates the LKB1 pathway in CD4+ T cells, leading to reduced TH17 effector cytokine (IL-17) production. IL-17 production was rescued by additional deletion of LKB1 in Ankrd55-deficient T cells, placing ANKRD55 upstream of LKB1 in a metabolic regulatory axis. | PMID:40932625 | The Journal of experimental medicine |
| 2025 | High | Ankrd55 deficiency in mice reduces CD4+ T cell proliferation and impairs TH17 differentiation and Th1 polarization in a cell-intrinsic manner, demonstrated by T cell-specific Ankrd55 knockout significantly reducing EAE disease severity and neuroinflammation. | PMID:41090353 | The Journal of clinical investigation |
| 2025 | High | ANKRD55 regulates formation of the immune synapse by interacting with subunits of the chaperonin-containing TCP1 (CCT) complex and modulating its activity. Specifically, ANKRD55 competes with CCT5 for binding to TCP1, CCT3, and CCT6, thereby enhancing CCT complex assembly, facilitating proper microtubule organization and T cell receptor (TCR) activation. | PMID:41090353 | The Journal of clinical investigation |

## Citations

- PMID:27183579
- PMID:31620119
- PMID:35111166
- PMID:40932625
- PMID:41090353
