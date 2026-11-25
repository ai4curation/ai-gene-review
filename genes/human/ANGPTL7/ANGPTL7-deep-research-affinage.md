---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANGPTL7
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: O43827
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANGPTL7 (human)

## Current model (mechanistic narrative)

ANGPTL7 (CDT6) is a secreted glycoprotein that regulates trabecular meshwork extracellular matrix homeostasis and aqueous outflow resistance, with human loss-of-function variants lowering intraocular pressure and protecting against glaucoma [PMID:32369491, PMID:38497513]. In trabecular meshwork cells it remodels the ECM, altering fibronectin, collagens, myocilin, versican, and MMP1 and disrupting fibronectin fibrillar assembly [PMID:21199193], and it executes the cytoskeletal arm of steroid responses by mediating dexamethasone-induced cross-linked actin network formation through RhoA/ROCK signaling [PMID:35136015]. Its own expression in these cells is driven transcriptionally by SP1 [PMID:35136015]. Functionally, ANGPTL7 is required for steroid-induced IOP elevation, since Angptl7-null mice resist dexamethasone-driven pressure increases; recombinant ANGPTL7 lowers hydraulic conductivity while blocking antibodies increase outflow facility and lower IOP across human ex vivo and rabbit in vivo models, establishing it as a secreted, antibody-tractable effector of outflow resistance [PMID:38497513]. Beyond the eye, ANGPTL7 acts in systemic and microenvironmental contexts: it promotes hepatic insulin resistance by upregulating SOCS3 to drive proteasomal IRS1 degradation and suppress Akt phosphorylation [PMID:32786125], supports expansion of hematopoietic stem and progenitor cells upstream of Wnt signaling [PMID:25637050], and serves as an SP1-driven, microenvironment-secreted factor supporting AML cell proliferation [PMID:37319434].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1474244 Extracellular matrix organization, R-HSA-162582 Signal Transduction
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | Medium | Overexpression of ANGPTL7 in primary human trabecular meshwork cells altered expression of extracellular matrix genes/proteins (fibronectin, collagens type I, IV & V, myocilin, versican, MMP1) and interfered with fibrillar assembly of fibronectin; silencing ANGPTL7 during glucocorticoid treatment significantly affected expression of other steroid-responsive proteins, indicating ANGPTL7 modulates trabecular meshwork ECM and steroid response. | PMID:21199193 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2015 | Medium | ANGPTL7 supports expansion and repopulation of human hematopoietic stem and progenitor cells (HSPCs) in vitro and in xenograft models, and activates CXCR4, HOXB4, and Wnt downstream target expression in human HSPCs; chemical inhibition of Wnt signaling diminished ANGPTL7 effects, placing ANGPTL7 upstream of the Wnt pathway in HSPC regulation. | PMID:25637050 | Haematologica |
| 2020 | High | Rare protein-altering (missense and protein-truncating) variants in ANGPTL7 lower intraocular pressure and confer protection against glaucoma in large human cohorts, suggesting the protective mechanism resides in loss of ANGPTL7 function or interaction. | PMID:32369491 | PLoS genetics |
| 2020 | Medium | ANGPTL7 promotes insulin resistance by upregulating SOCS3 expression, leading to IRS1 degradation via the proteasome; ANGPTL7 also inhibits Akt phosphorylation and promotes ERK1/2 phosphorylation in hepatic cells. | PMID:32786125 | FASEB journal : official publication of the Federation of American Societies for Experimental Biology |
| 2022 | Medium | ANGPTL7 expression in trabecular meshwork cells is transcriptionally regulated by SP1 (identified by bioinformatics, dual-luciferase reporter assay, and chromatin immunoprecipitation); ANGPTL7 mediates dexamethasone-induced cross-linked actin network (CLAN) formation via the RhoA/ROCK signaling pathway, and ANGPTL7 knockdown inhibits DEX-induced CLAN formation. | PMID:35136015 | Cell death discovery |
| 2024 | High | Angptl7 knockout mice show elevated IOP; when challenged with dexamethasone, IOP increased in wild-type but not Angptl7 KO mice, demonstrating ANGPTL7 is required for steroid-induced IOP elevation. Recombinant ANGPTL7 decreased hydraulic conductivity in 3D culture of outflow cells, and ANGPTL7-blocking antibodies increased hydraulic conductivity and outflow facility in perfused human donor eyes ex vivo and lowered IOP for 21 days in rabbits after a single intravitreal injection. | PMID:38497513 | Investigative ophthalmology & visual science |
| 2023 | Medium | In the AML bone marrow microenvironment, ID1 interacts with the E3 ubiquitin ligase RNF4 to prevent SP1 ubiquitination/degradation; SP1 then transcriptionally drives Angptl7 expression in mesenchymal stem cells; secreted ANGPTL7 from the microenvironment is the primary factor supporting AML cell proliferation and progression. | PMID:37319434 | Blood |
| 2019 | Low | Overexpression of ANGPTL7 in MC3T3-E1 preosteoblast cells promoted cell proliferation, alkaline phosphatase (ALP) activity, and mineralization, and upregulated BMP2, BMP7, and osteogenic markers (ALP, Runx2, OCN, Col I), indicating ANGPTL7 promotes osteoblast differentiation via BMP pathway regulation. | PMID:31835268 | Medical science monitor : international medical journal of experimental and clinical research |
| 2001 | Medium | The human CDT6 (ANGPTL7) promoter lacks TATA and CAAT boxes near the transcription initiation site; it contains four interferon-stimulated response elements (ISREs), and IFN-alpha stimulates transcriptional activity of the human (but not mouse) CDT6 promoter. Transfection assays revealed positive and negative cis-regulatory elements conferring cell, tissue, and species specificity. | PMID:11687517 | Investigative ophthalmology & visual science |
| 2007 | Low | CDT6 (ANGPTL7) expression in human melanoma cells (BLM) significantly upregulated endostatin, while in mouse melanoma cells (B16-F10) it significantly downregulated endostatin, revealing a species-dependent opposite effect on this angiogenic balance factor. | PMID:17695521 | Anticancer research |

## Citations

- PMID:11687517
- PMID:17695521
- PMID:21199193
- PMID:25637050
- PMID:31835268
- PMID:32369491
- PMID:32786125
- PMID:35136015
- PMID:37319434
- PMID:38497513
