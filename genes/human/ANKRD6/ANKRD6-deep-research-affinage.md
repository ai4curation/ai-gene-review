---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD6
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9Y2G4
self_evaluation_pairwise: tie
faith_pct: 100.0
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

# Affinage mechanistic annotation for ANKRD6 (human)

## Current model (mechanistic narrative)

ANKRD6 (Diversin) is a vertebrate core planar cell polarity (PCP) protein that acts as a molecular switch between Wnt signaling branches, activating non-canonical PCP signaling while suppressing canonical Wnt/β-catenin signaling during development [PMID:25218921, PMID:25200652]. In the mouse inner ear, Ankrd6 protein adopts the asymmetric, planar-polarized junctional localization characteristic of core PCP components, and its loss misorients hair cell bundles while derepressing canonical Wnt reporter activity in knockout fibroblasts; mouse Ankrd6 can rescue Drosophila diego loss-of-function, establishing it as the functional vertebrate Diego ortholog [PMID:25218921]. In the Xenopus neuroectoderm, Diversin is required for apical constriction, neural tube closure, and the polarized localization of endogenous Vangl2, and it acquires planar polarity at junctions in a stage- and position-specific, tension-dependent manner, redistributing toward cells with constricting apical domains [PMID:40719643]. Diversin forms a mechanosensitive complex with ADIP that is distinct from canonical core PCP complexes and is required for wound repair, with Diversin acting upstream of ADIP polarization, which in turn depends on microtubules, F-actin, and nonmuscle myosin II [PMID:40562038, PMID:41601266]. Hypomorphic missense variants in human ANKRD6 that alter its Wnt-switching activity are associated with neural tube defects [PMID:25200652]. In melanoma cells, ANKRD6 acts as a miR-214 target that negatively regulates Wnt/β-catenin signaling and restrains proliferation, migration, and MAPK-inhibitor resistance [PMID:31338875].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060089 molecular transducer activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** ADIP, VANGL2, DVL2
- **complexes:** ADIP-Diversin PCP complex, core PCP complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | Murine Ankrd6 (mAnkrd6) protein is asymmetrically localized in cells of the inner ear sensory organs, characteristic of core PCP complex components. Loss of mAnkrd6 causes PCP defects in inner ear sensory organs (misoriented hair cell bundles). Additionally, canonical Wnt signaling is significantly increased in mouse embryonic fibroblasts from mAnkrd6 knockout mice compared to wild-type controls, demonstrating that mAnkrd6 suppresses canonical Wnt signaling. | PMID:25218921 | Developmental biology |
| 2014 | Medium | Rare missense mutations in ANKRD6 (p.Pro548Leu and p.Arg632His) identified in neural tube defect patients significantly alter DIVERSIN activity in Wnt signaling reporter assays in a hypomorphic manner, consistent with ANKRD6 acting as a molecular switch that activates non-canonical PCP signaling and simultaneously inhibits canonical Wnt/β-catenin signaling during neurulation. | PMID:25200652 | Birth defects research. Part A, Clinical and molecular teratology |
| 2019 | Medium | Knockdown of ANKRD6 in melanoma cells increased cell proliferation and migration and decreased sensitivity to MAPK inhibitors, phenocopying miR-214 overexpression. ANKRD6 was identified as a novel miR-214 target involved in negative regulation of Wnt/β-catenin signaling in melanoma cells. | PMID:31338875 | Molecular carcinogenesis |
| 2025 | Medium | Diversin (ANKRD6) forms a mechanosensitive complex with ADIP (afadin- and α-actinin-interacting protein) that is distinct from known core PCP complexes. This ADIP-Diversin complex is required for wound repair in Xenopus embryos. ADIP puncta relocate in response to pulling forces from neighboring ectoderm cells, and Diversin-containing PCP complexes with Dvl2 show planar polarity in the neural plate and wound edge. | PMID:40562038 | Current biology : CB |
| 2025 | Medium | Depletion of Diversin/Ankrd6 in the Xenopus neuroectoderm inhibited apical domain size and neural tube closure and disrupted the polarized localization of endogenous Vangl2. Diversin puncta acquired planar polarity in the neuroectoderm in a stage- and position-specific manner and accumulated at cell junctions adjacent to apically constricting cells, suggesting mechanosensitive regulation. Diversin cytoplasmic puncta redistributed in the direction of pulling forces from cells with constricting apical domains. | PMID:40719643 | Biology open |
| 2026 | Medium | Depletion of Diversin/Ankrd6 attenuates planar polarization of endogenous ADIP in the Xenopus neuroectoderm, demonstrating that Diversin is required upstream of ADIP polarization during PCP establishment. Pharmacological disruption of microtubules, F-actin, and nonmuscle myosin II eliminates ADIP polarization, placing cytoskeletal machinery downstream of the Diversin-ADIP PCP module. | PMID:41601266 | Biology open |
| 2002 | Medium | Ankrd6 is transcribed as a 5.8-kb mRNA composed of 15 exons encoding a 712 amino acid protein with 6 ankyrin repeats. Ankrd6 is expressed prominently in the developing mouse brain from E12 to maturity, with maximal expression in ventricular zones of neuronal proliferation and intermediate zones of neuronal migration in embryos, and in cortical layer II, dentate gyrus granule cells, olfactory granules, and a subset of Purkinje cells postnatally. | PMID:12203740 | Developmental dynamics : an official publication of the American Association of Anatomists |
| 2005 | Low | Bioinformatic characterization of rat Ankrd6 identified Ser340 (conserved among mammalian Ankrd6 orthologs) as a predicted PKA phosphorylation and 14-3-3 interaction site. The ankyrin repeats are predicted binding domains for Prickle1, Prickle2, Vangl1, and Vangl2. The central coiled-coil region falls within the binding domain for Casein kinase I epsilon (CKIε), and the C-terminal coiled-coil region falls within the binding domain for Axin1 and Axin2. | PMID:15647854 | International journal of molecular medicine |

## Citations

- PMID:12203740
- PMID:15647854
- PMID:25200652
- PMID:25218921
- PMID:31338875
- PMID:40562038
- PMID:40719643
- PMID:41601266
