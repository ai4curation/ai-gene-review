---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTRT3
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9BYD9
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTRT3 (human)

## Current model (mechanistic narrative)

ACTRT3 (ARPM1) is a testis-enriched actin-related protein that functions as a structural component of the spermatid perinuclear theca (PT) required for acrosome biogenesis and male fertility [PMID:41668650]. It forms a testis-specific complex with profilin III (PFN3), a partnership that is mutually stabilizing: PFN3 is required to maintain ARPM1 in the nuclear fraction, and loss of either partner reduces the level of the other [PMID:18692047, PMID:34869336, PMID:41668650]. Within the PT, ACTRT3 associates with the scaffold proteins ACTRT1, ACTRT2, ACTL7A and SPEM2 and with the sperm-surface protein ZPBP, positioning it as a PT scaffold component that mediates ZPBP localization [PMID:41668650, PMID:bio_10.1101_2025.03.27.645694]. ACTRT3 supports acrosome development by sustaining Golgi trafficking—its loss reduces TGN46 and GOPC, mislocalizes GM130, and impairs autophagic flux (LC3B, CTSB, mTOR)—and it remodels the actin cytoskeleton, interacting with the regulators CFL1 and CNN1 and altering F-actin distribution and cell shape when overexpressed [PMID:41668650]. Loss of ACTRT3 in mice causes subfertility with acrosomal defects beginning at the cap phase [PMID:41668650, PMID:bio_10.1101_2025.03.27.645694].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0008092 cytoskeletal protein binding, GO:0005198 structural molecule activity
- **localization:** GO:0005634 nucleus, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-9612973 Autophagy
- **partners:** PFN3, ACTRT1, ACTRT2, ACTL7A, SPEM2, ZPBP, CFL1, CNN1
- **complexes:** perinuclear theca

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | Medium | Mouse ArpM1 (ACTRT3) is expressed exclusively in the testis in haploid germ cells; it localizes to the nucleus during spermiogenesis and dynamically changes its nuclear localization. Co-immunoprecipitation identified profilin III (PFN3) as an ArpM1-interacting protein, forming a testis-specific complex implicated in sperm nucleus organization. | PMID:18692047 | FEBS letters |
| 2021 | Medium | In Pfn3-knockout mice, ARPM1 (ACTRT3) is absent from the nuclear fraction of testes and sperm, indicating that PFN3 stabilizes ARPM1 and that the PFN3-ARPM1 complex is required for ARPM1 nuclear localization. Loss of PFN3 leads to degradation of ARPM1. | PMID:34869336 | Frontiers in cell and developmental biology |
| 2026 | High | ACTRT3 localizes to the perinuclear theca (PT) of murine spermatids. Actrt3-/- male mice are subfertile with acrosome biogenesis defects beginning at cap phase. Loss of ACTRT3 reduces TGN46 and GOPC protein levels, mislocalizes GM130, and impairs autophagy markers (LC3B, CTSB, mTOR), indicating disrupted Golgi trafficking and autophagic flux required for acrosome development. Co-IP revealed interaction with PT proteins ACTRT1, ACTRT2, ACTL7A, SPEM2, and sperm surface protein ZPBP. Mass spectrometry identified cytoskeletal regulators CFL1 and CNN1 as enriched interactors. Overexpression of Actrt3 in HEK293T cells altered cell shape and F-actin filament distribution, demonstrating a role in cytoskeletal remodeling. PFN3 protein levels were significantly reduced in Actrt3-/- mice. | PMID:41668650 | Development (Cambridge, England) |
| 2025 | Medium | ARPM1/ACTRT3 localizes to the perinuclear theca of round and elongating spermatids. Arpm1-/- male mice are subfertile with acrosomal morphological aberrations from cap phase. Loss of ARPM1 deregulates GM130 and TGN46, indicating defects in cis- and trans-Golgi trafficking. Co-IP confirmed interactions with PT proteins ACTRT1, ACTRT2, ACTL7A, and sperm surface protein ZPBP (in addition to the previously shown PFN3 interaction). ARPM1 is proposed to act as a structural PT scaffold component tethering PFN3 to regulate Golgi-related acrosome development and mediating ZPBP localization for fertilization. | PMID:bio_10.1101_2025.03.27.645694 | bioRxiv |

## Citations

- PMID:18692047
- PMID:34869336
- PMID:41668650
- PMID:bio_10.1101_2025.03.27.645694
