---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASTN1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O14525
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 6
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASTN1 (human)

## Current model (mechanistic narrative)

ASTN1 (astrotactin 1) is a neuronal cell-surface protein that mediates glial-guided neuronal migration in laminar brain structures, accumulating in the forward aspect of the leading process of migrating cerebellar granule cells where new neuron-glial adhesion sites form [PMID:20573900]. Its surface levels are governed by a complex with the paralog ASTN2, which controls how much ASTN1 reaches the plasma membrane during migration [PMID:20573900], and the cyclical release of adhesions to the glial fiber depends on dynamin-dependent endocytosis of the receptor, since dynamin inhibition rapidly and reversibly arrests migration [PMID:20573900]. Bi-allelic loss-of-function variants in ASTN1 cause human neurodevelopmental disorders with defects in radial-glia-guided neuronal migration, and ASTN1 genetically interacts with ASTN2 in this pathway [PMID:41544630]. Beyond its neuronal role, ASTN1 overexpression suppresses migration and invasion of liver cancer cells by inhibiting Wnt/β-catenin signaling, downregulating β-catenin and downstream targets in a manner reversed by the Wnt inhibitor XAV939 [PMID:32945491]. ASTN1 expression is itself subject to post-transcriptional control by miR-sc3, which directly targets Astn1 mRNA for translational suppression [PMID:26786955].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology
- **partners:** ASTN2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | ASTN2 forms a protein complex with ASTN1 and regulates its surface expression, controlling the levels of ASTN1 in the plasma membrane during glial-guided neuronal migration. | PMID:20573900 | The Journal of neuroscience |
| 2010 | Medium | ASTN1-Venus accumulates in the forward aspect of the leading process of migrating cerebellar granule cells, where new sites of neuron-glial adhesion form, indicating directional intracellular trafficking of ASTN1 is coupled to neuronal locomotion. | PMID:20573900 | The Journal of neuroscience |
| 2010 | Medium | Dynamin-dependent endocytosis is required for ASTN1 trafficking and neuronal migration: treatment with Dynasore (a Dynamin inhibitor) rapidly and reversibly arrests glial-guided migration of cerebellar granule cells, implicating receptor endocytosis in the release of neuronal adhesions to the glial fiber. | PMID:20573900 | The Journal of neuroscience |
| 2016 | Medium | miR-sc3 directly targets Astn1 mRNA and causes translational suppression of ASTN1, with an inverse expression relationship between miR-sc3 and Astn1 in injured sciatic nerve after transection. | PMID:26786955 | Cell transplantation |
| 2020 | Medium | ASTN1 overexpression in liver cancer cells reduces their migratory and invasive capacity and downregulates β-catenin, TCF1, TCF4, C-jun, C-myc, COX2, MMP2, MMP9, and VEGF protein levels, indicating suppression of Wnt/β-catenin signaling; Wnt inhibitor XAV939 reversed the ASTN1-mediated inhibition of invasion and migration. | PMID:32945491 | Oncology reports |
| 2026 | Medium | Bi-allelic loss-of-function variants in ASTN1 in humans cause neurodevelopmental disorders with defects in radial-glia-guided neuronal migration, and ASTN1 genetically interacts with ASTN2 (one individual had heterozygous variants in both), placing ASTN1 in the same pathway as ASTN2 for neuronal migration. | PMID:41544630 | American journal of human genetics |

## Citations

- PMID:20573900
- PMID:26786955
- PMID:32945491
- PMID:41544630
