---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADIG
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q0VDE8
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ADIG (human)

## Current model (mechanistic narrative)

ADIG (adipogenin/SMAF1) is an adipocyte-enriched ~10 kDa microprotein that functions in lipid droplet biogenesis as a transcriptional output of the adipogenic program and a regulator of fat mass [PMID:26427354, PMID:33691105]. Its expression is tightly coupled to the adipocyte phenotype, induced during adipogenesis, and wholly dependent on PPARγ, which directly binds a functional PPRE in the Adig promoter; ADIG transcription is further modulated by insulin, glucose, and Srebp1c [PMID:26427354, PMID:27766294, PMID:37249025]. ADIG localizes to lipid droplets in adipocytes, and genetic loss of ADIG impairs adipogenesis, produces leaner mice on a high-fat diet and in the ob/ob background, and reduces leptin secretion from adipose tissue [PMID:26427354, PMID:33691105]. Mechanistically, ADIG directly binds seipin and selectively stabilizes its dodecameric oligomer, bridging adjacent subunits to promote seipin assembly and support lipid droplet formation, with bidirectional genetic perturbation altering lipid droplet morphology, fat mass, and thermogenic cold tolerance. PPARγ-driven ADIG expression is not restricted to adipose tissue but is also induced in hepatic steatosis [PMID:37249025].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005811 lipid droplet
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** SEIPIN
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Medium | SMAF1 (ADIG) encodes a novel ~10 kDa protein with adipose tissue-restricted expression; transfection and localization studies of a SMAF1-EGFP fusion construct indicated nuclear localization; expression is closely tied to the adipocyte phenotype and is rapidly lost upon TNFα-mediated dedifferentiation of 3T3-L1 adipocytes. | PMID:15567149 | Biochemical and biophysical research communications |
| 2015 | High | SMAF1/ADIG encodes a bona fide ~10 kDa protein in adipocytes; its expression is rapidly induced during adipogenesis, positively regulated by insulin and glucose, and is wholly dependent on PPARγ (siRNA knockdown of PPARγ abolishes Smaf1 protein). Immunolocalization of HA-tagged Smaf1 reveals enrichment at adipocyte lipid droplets. siRNA-mediated near-abolition of Smaf1 protein did not detectably affect adipocyte triglyceride accumulation, lipolysis, or insulin-stimulated pAkt induction. | PMID:26427354 | Archives of biochemistry and biophysics |
| 2016 | Medium | PPARγ/RXRα directly regulates the Adig/Smaf1 gene promoter; luciferase reporter assays using an ~2 kb fragment of the 5' flanking region of Adig/Smaf1 demonstrated transcriptional activation by PPARγ/RXRα. Srebp1c siRNA knockdown reduces Adig/Smaf1 transcript levels in 3T3-L1 adipocytes, indicating regulation also by Srebp1c. | PMID:27766294 | Data in brief |
| 2016 | Low | Adenovirus-mediated overexpression of ADIG in bovine myosatellite cells upregulates PPARγ expression, increases lipid droplet size (Oil Red O staining), and downregulates key components of the Hedgehog (Hh) signaling pathway; co-treatment with an Hh inhibitor did not further decrease Hh components, suggesting ADIG acts upstream or at the level of Hh signaling suppression. | PMID:27914980 | Gene |
| 2021 | High | Adig deficiency in cultured adipocytes impairs adipogenesis; Adig null mice are leaner than wild-type mice on a high-fat diet and when crossed with ob/ob mice. Additionally, Adig deficiency reduces fat-mass-adjusted plasma leptin levels and impairs leptin secretion from adipose explants, indicating a role in regulating both fat mass accrual and leptin secretion. | PMID:33691105 | Cell reports |
| 2023 | High | Hepatic PPARγ directly binds to a functional PPARγ-responsive element (PPRE) in the Adig promoter and positively regulates hepatic Adig transcription during liver steatosis; this was demonstrated by reporter assays and electrophoretic mobility shift assay (EMSA). Adig is highly expressed in fatty liver models (ob/ob, db/db, alcohol-fed mice) and is markedly reduced in liver-specific Pparg-knockout mice. | PMID:37249025 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2024 | High | Adig directly interacts with seipin to form a rigid complex; cryo-EM at 2.98 Å resolution reveals that seipin can form undecameric or dodecameric oligomers, and Adig selectively binds the dodecameric form. Adig stabilizes and bridges adjacent seipin subunits, promoting seipin assembly. Functionally, Adig is required for lipid droplet formation in adipocytes; inducible overexpression of Adig in mouse adipocytes increases fat mass with enlarged lipid droplets and elevates thermogenesis during cold exposure, whereas inducible adipocyte-specific Adig knockout causes aberrant lipid droplet formation in brown adipose tissue and impaired cold tolerance. | — | bioRxiv |

## Citations

- PMID:15567149
- PMID:26427354
- PMID:27766294
- PMID:27914980
- PMID:33691105
- PMID:37249025
