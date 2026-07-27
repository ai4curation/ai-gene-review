---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTRT2
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q8TDY3
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTRT2 (human)

## Current model (mechanistic narrative)

ACTRT2 (Arp-T2) is a testis-specific actin-related protein that serves as a structural component of the sperm head perinuclear theca, the cytoskeletal calyx that resists high ionic strength and detergent extraction, where it is a major acidic constituent expressed late in spermatid differentiation [PMID:12243744]. Within the subacrosomal region of developing spermatids, ACTRT2 assembles into a multimeric perinuclear theca complex with ACTRT1, ACTL7A, ACTL9, and ACTRT3 that anchors the developing acrosome to the sperm nucleus during spermiogenesis; loss of complex integrity produces acrosomal detachment [PMID:35616329, PMID:41668650]. In human spermatozoa it localizes to the post-acrosomal region and middle piece, and its expression is reduced in obesity-associated asthenozoospermia [PMID:25293813]. Beyond its structural role, ACTRT2 protects spermatogonia against ferroptosis: its loss drives intracellular iron overload, mitochondrial damage, and a shift in ferroptosis regulators (upregulation of ACSL4 and ALOX15 with downregulation of SLC7A11 and GPX4) that sensitizes cells to busulfan-induced death [PMID:40811009].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-5357801 Programmed Cell Death
- **partners:** ACTRT1, ACTL7A, ACTL9, ACTRT3
- **complexes:** perinuclear theca (sperm calyx) cytoskeletal complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | Medium | ACTRT2 (Arp-T2) is a novel actin-related protein that localizes specifically to the cytoskeletal calyx of the mammalian sperm head (perinuclear theca), is expressed specifically in the testis late in spermatid differentiation, and is a major acidic component of the calyx structure characterized by resistance to high ionic strength and detergents. | PMID:12243744 | Experimental cell research |
| 2022 | High | ACTRT2 interacts with ACTRT1, ACTL7A, and ACTL9 to form a multimeric complex that localizes to the subacrosomal region of spermatids and is required for anchoring the developing acrosome to the nucleus; this complex mediates the acrosome-nucleus connection during spermiogenesis. | PMID:35616329 | Development (Cambridge, England) |
| 2014 | Medium | ACTRT2 localizes to the post-acrosomal region and middle piece of human spermatozoa, and its expression is decreased in obesity-associated asthenozoospermia. | PMID:25293813 | Andrology |
| 2025 | Medium | ACTRT2 deficiency in spermatogonia increases vulnerability to ferroptosis: loss of ACTRT2 leads to intracellular iron overload (upregulation of SLC11A2, IREB2, TFRC), mitochondrial damage, upregulation of pro-ferroptotic ACSL4 and ALOX15, and downregulation of anti-ferroptotic SLC7A11 and GPX4, resulting in increased cell death upon busulfan treatment. | PMID:40811009 | Molecular human reproduction |
| 2026 | Medium | ACTRT2 physically interacts with ACTRT3 (ARPM1/ACTRT3) as part of a perinuclear theca protein complex in spermatids, as demonstrated by co-immunoprecipitation in the context of ACTRT3 characterization. | PMID:41668650 | Development (Cambridge, England) |
| 2025 | Low | ACTRT2 interacts with ACTRT1 and ACTL7A (and ARPM1/ACTRT3) as part of the perinuclear theca cytoskeletal complex, corroborating its role as a structural component linking acrosome to nucleus. | PMID:bio_10.1101_2025.03.27.645694 | bioRxiv |

## Citations

- PMID:12243744
- PMID:25293813
- PMID:35616329
- PMID:40811009
- PMID:41668650
- PMID:bio_10.1101_2025.03.27.645694
