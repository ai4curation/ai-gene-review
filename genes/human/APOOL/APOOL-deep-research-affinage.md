---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APOOL
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q6UXV4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 16
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APOOL (human)

## Current model (mechanistic narrative)

APOOL (MIC27) is a non-glycosylated inner mitochondrial membrane protein of the MICOS complex that shapes cristae architecture by coupling cardiolipin binding to assembly of the membrane-sculpting MICOS scaffold [PMID:23704930, PMID:25918844, PMID:37279200]. It faces the intermembrane space, specifically binds cardiolipin but not its precursor phosphatidylglycerol, and physically associates with MICOS/MIB subunits including Mitofilin/MIC60, MINOS1/MIC10, and SAMM50 [PMID:23704930]. Within MICOS it belongs to the MIC10/MIC12/MIC27 subcomplex that assembles independently of the MIC60/MIC19 subcomplex and whose formation depends on cardiolipin and respiratory complexes [PMID:25918844]; its integration requires MIC13/QIL1, whose loss triggers degradation of MIC27 together with MIC10 and MIC26 [PMID:25997101, PMID:27479602]. Mechanistically, MIC27 stabilizes MIC10 oligomers and promotes oligomerization of the F1FO-ATP synthase, thereby supporting crista junction formation and cristae membrane curvature [PMID:26968360, PMID:28845423]. MIC27 and MIC26 reciprocally regulate each other's levels and act antagonistically on MIC10 oligomer stability, and their combined loss cooperatively depletes cardiolipin and destabilizes respiratory chain supercomplexes and ATP synthase, a defect reversed by cardiolipin synthase overexpression [PMID:25764979, PMID:29733859, PMID:32788226]. Loss-of-function mutation in QIL1/MIC13 eliminates the MIC10–MIC26–MIC27–QIL1 subcomplex and produces aberrant cristae and respiratory chain deficiency in patient tissue [PMID:29618761].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0005198 structural molecule activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1852241 Organelle biogenesis and maintenance, R-HSA-1430728 Metabolism
- **partners:** MIC10, MIC26, MIC60, MIC13, SAMM50, MIC19, MIC12
- **complexes:** MICOS complex, MIC10/MIC12/MIC27 subcomplex, MICOS/MIB complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | APOOL (MIC27) is a mitochondrial inner membrane protein facing the intermembrane space that specifically binds cardiolipin in vitro but not its precursor phosphatidylglycerol, and physically interacts with MINOS complex subunits Mitofilin, MINOS1, and SAMM50. | PMID:23704930 | PloS one |
| 2013 | High | Overexpression of APOOL causes mitochondrial fragmentation and reduced basal oxygen consumption rate with altered cristae morphology; downregulation impairs mitochondrial respiration and causes major cristae morphology alterations. | PMID:23704930 | PloS one |
| 2015 | High | APOOL (MIC27) is a component of the Mic27/Mic10/Mic12 MICOS subcomplex, whose assembly is dependent on respiratory complexes and the mitochondrial lipid cardiolipin, forming a subcomplex independent of the Mic60/Mic19 subcomplex. | PMID:25918844 | eLife |
| 2015 | High | Loss of QIL1 (MIC13) results in degradation of MIC27 (APOOL) along with MIC10 and MIC26, while the MIC60-MIC19-MIC25 subcomplex accumulates, placing MIC27 in a QIL1-dependent MICOS subcomplex. | PMID:25997101 | eLife |
| 2015 | Medium | MIC27 (APOOL) is a periphery subunit of the human MICOS/MIB complex whose depletion does not affect cristae morphology or stability of other MICOS components, unlike the core subunits MIC60, MIC19, and SAM50. | PMID:25781180 | PloS one |
| 2015 | High | MIC26 and MIC27 regulate each other's protein levels in an antagonistic manner; MIC26 physically interacts with MIC27 and other MICOS subunits (MIC60, MIC10), and both are positively correlated with MIC10 levels and tafazzin (a cardiolipin remodeling enzyme). | PMID:25764979 | Biochimica et biophysica acta |
| 2016 | High | MIC13 (QIL1) is required for the assembly of MIC27 (APOOL) into the MICOS complex; MIC13 knockout cells show complete loss of crista junctions and loss of MIC27 from the complex, while the MIC60/MIC19/MIC25 subcomplex remains intact. | PMID:27479602 | PloS one |
| 2016 | High | MIC27 (APOOL) promotes stability of MIC10 oligomers within the membrane-sculpting MICOS subcomplex, while MIC12 is required for coupling the two MICOS subcomplexes; loss of MIC27 destabilizes the Mic10-containing subcomplex. | PMID:26968360 | Journal of molecular biology |
| 2017 | High | MIC27 (APOOL) promotes oligomerization of the F1FO-ATP synthase and partially restores crista junction formation in cells lacking MIC60; MIC27 deletion impairs crista junction formation and alters cristae membrane curvature; a chemical crosslink of MIC10 to MIC27 was detected, supporting physical interaction within the MICOS-F1FO-ATP synthase interface. | PMID:28845423 | Microbial cell (Graz, Austria) |
| 2018 | High | MIC27 (APOOL) stabilizes MIC10 oligomers in an antagonistic relationship with MIC26 (which destabilizes MIC10 oligomers); cardiolipin also shows a stabilizing function on MIC10 oligomers, mechanistically linking MIC27's cardiolipin-binding activity to MICOS core scaffold regulation. | PMID:29733859 | Journal of molecular biology |
| 2018 | Medium | In a patient with loss-of-function mutation in QIL1/MIC13, the MIC10-MIC26-MIC27-QIL1 subcomplex is absent, resulting in aberrant cristae structure, loss of cristae junctions, and severely impaired respiratory chain complex activity in liver and muscle. | PMID:29618761 | Journal of human genetics |
| 2019 | Medium | Yeast MIC27 uses the presequence pathway to reach the intermembrane space, establishing its mitochondrial import mechanism as distinct from the TIM40/MIA pathway used by Mic19. | PMID:30718713 | Scientific reports |
| 2020 | High | MIC26 and MIC27 (APOOL) double knockout (DKO) human cells show more severe concentric onion-like cristae with loss of crista junctions than either single KO, indicating overlapping roles; both proteins are dispensable for stability and integration of remaining MICOS subunits, suggesting late assembly into the complex. DKO cells show reduced cardiolipin levels and impaired integrity of respiratory chain supercomplexes and F1Fo-ATP synthase; overexpression of cardiolipin synthase in DKO restores respiratory complex stability. | PMID:32788226 | Life science alliance |
| 2020 | Medium | In Drosophila, the CG5903 gene encoding a MIC26-MIC27 ortholog colocalizes and functions with Mitofilin/MIC60 and QIL1/MIC13 as a MICOS component; knockdown causes loss of crista junctions, reduced mitochondrial membrane potential, fusion/fission imbalances, increased mitophagy, reduced mtDNA content, and muscle dysfunction. | PMID:33268479 | Biology open |
| 2023 | High | MIC27 (APOOL) is exclusively localized in mitochondria as a 30 kDa non-glycosylated protein; predicted glycosylation site mutagenesis and mass spectrometry of candidate bands confirmed no high-molecular-weight glycosylated isoform exists, establishing MIC27 as purely a mitochondrial MICOS subunit. | PMID:37279200 | PloS one |
| 2025 | Medium | Proximity biotinylation (APEX2) fused to MIC27 in MIC27 knockout cells identified 119 common and 50 unique proximal proteins (MINDNet), including OXPHOS subunits, protein translocases, mitochondrial ribosomal proteins, and solute carrier transporters, defining the molecular neighbourhood of MIC27 within the MICOS complex. | PMID:bio_10.1101_2025.05.20.655052 | bioRxiv |

## Citations

- PMID:23704930
- PMID:25764979
- PMID:25781180
- PMID:25918844
- PMID:25997101
- PMID:26968360
- PMID:27479602
- PMID:28845423
- PMID:29618761
- PMID:29733859
- PMID:30718713
- PMID:32788226
- PMID:33268479
- PMID:37279200
- PMID:bio_10.1101_2025.05.20.655052
