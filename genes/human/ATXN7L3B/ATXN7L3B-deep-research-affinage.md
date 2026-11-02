---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATXN7L3B
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96GX2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATXN7L3B (human)

## Current model (mechanistic narrative)

ATXN7L3B is a cytoplasmic protein that acts as a dominant-negative regulator of the SAGA deubiquitinase (DUB) module by sequestering the shared co-factor ENY2 away from the nucleus [PMID:27601583]. It binds ENY2 but none of the other SAGA components, and in vitro it competes directly with ATXN7L3 for ENY2; a reconstituted USP22-ATXN7L3B-ENY2 complex is catalytically deficient and cannot efficiently deubiquitinate H2Bub1, unlike the ATXN7L3-containing module [PMID:27601583]. Consistent with this antagonism, overexpression of ATXN7L3B raises global H2Bub1 levels while its knockdown destabilizes ENY2 [PMID:27601583]. Through this regulatory role ATXN7L3B influences estrogen receptor target gene expression and breast cancer cell migration [PMID:27601583] and promotes hepatocellular carcinoma stemness, an activity reduced by metformin [PMID:34375763]. Its upregulation also drives osteogenic differentiation of adipose-derived stem cells [PMID:41245170], and a synonymous promoter-proximal SNP (rs590352) modulates its allele-asymmetric expression by disrupting transcription factor binding [PMID:41217722].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization
- **partners:** ENY2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | ATXN7L3B interacts with ENY2 but not with other SAGA complex components; it localizes in the cytoplasm rather than the nucleus. | PMID:27601583 | Molecular and cellular biology |
| 2016 | High | In vitro, ATXN7L3B competes with ATXN7L3 for ENY2 binding; a reconstituted USP22-ATXN7L3B-ENY2 complex cannot efficiently deubiquitinate H2Bub1, in contrast to the ATXN7L3-containing DUB module. | PMID:27601583 | Molecular and cellular biology |
| 2016 | High | Overexpression of ATXN7L3B increases global H2Bub1 levels (opposite to ATXN7L3 overexpression which decreases H2Bub1), and knockdown of ATXN7L3B leads to concomitant loss of ENY2, indicating ATXN7L3B sequesters ENY2 in the cytoplasm to antagonize nuclear SAGA DUB activity. | PMID:27601583 | Molecular and cellular biology |
| 2016 | Medium | Knockdown of ATXN7L3B inhibits migration of breast cancer cells in vitro and limits expression of estrogen receptor (ER) target genes. | PMID:27601583 | Molecular and cellular biology |
| 2021 | Medium | ATXN7L3B promotes hepatocellular carcinoma (HCC) stemness (tumor-initiating ability), and metformin reduces ATXN7L3B levels in HCC cells, with metformin treatment decreasing ATXN7L3B-induced tumor-initiating ability in a HCC mouse model. | PMID:34375763 | Biochemical and biophysical research communications |
| 2025 | Medium | The synonymous SNP rs590352 G→C in exon 1 of ATXN7L3B disrupts binding sites for certain transcription factors (shown by EMSA), reduces reporter gene expression in luciferase assay, and results in lower allele-asymmetric in vivo ATXN7L3B expression for the C allele compared with the G allele. | PMID:41217722 | Biochemical genetics |
| 2025 | Medium | CRISPRa-mediated upregulation of ATXN7L3B in adipose-derived stem cells significantly increases alkaline phosphatase activity and mineralization in monolayer and 3D culture, identifying ATXN7L3B as a novel osteogenic target. | PMID:41245170 | Journal of tissue engineering |
| 2014 | Low | lnc-SCA7 (ATXN7L3B locus; long noncoding RNA product) mediates post-transcriptional cross-talk with ATXN7 mRNA via miR-124, with STAGA required for miR-124 transcription initiation; mutations in ATXN7 disrupt this regulatory loop causing neuron-specific increases in ATXN7 expression. | PMID:25306109 | Nature structural & molecular biology |

## Citations

- PMID:25306109
- PMID:27601583
- PMID:34375763
- PMID:41217722
- PMID:41245170
