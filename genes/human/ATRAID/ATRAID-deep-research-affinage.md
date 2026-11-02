---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATRAID
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q6UW56
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

# Affinage mechanistic annotation for ATRAID (human)

## Current model (mechanistic narrative)

ATRAID (APR3) is a glycosylated lysosomal/endosomal membrane protein that controls the cellular delivery and pharmacology of nitrogen-containing bisphosphonates (N-BPs) and acts as a negative regulator of cell proliferation [PMID:29745899, PMID:25839652, PMID:17524364]. It forms a complex with the solute carrier SLC37A3 at the lysosome, and this complex is required to release endocytosed N-BPs from the lysosomal lumen into the cytosol so they can reach farnesyl diphosphate synthase in the mevalonate pathway [PMID:29745899]. Loss of ATRAID blocks N-BP-mediated inhibition of protein prenylation and osteoclast function and renders both cells and mice resistant to alendronate, while patient-derived coding variants alter cellular N-BP sensitivity, establishing ATRAID as a determinant of bisphosphonate therapeutic response in osteoporosis models [PMID:32434850]. Its predominant isoform localizes to cytoplasmic vesicles, the Golgi region, and recycling endosomes marked by LAMP1, LAMP2, and RAB11, consistent with a role in endolysosomal trafficking [PMID:37530719]. Independently, ATRAID restrains the cell cycle: overexpression drives G1/S arrest via marked downregulation of Cyclin D1, an activity that depends on its transmembrane/intracellular domain [PMID:17524364], and it physically binds NELL-1 to suppress osteoblast proliferation and promote osteogenic differentiation and mineralization [PMID:21723284, PMID:31416616]. Transcription of ATRAID is driven from two distinct promoters that are activated by NFAT and repressed by NFκB [PMID:17387583].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140313 molecular sequestering activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005764 lysosome, GO:0005768 endosome, GO:0005886 plasma membrane, GO:0005794 Golgi apparatus, GO:0005635 nuclear envelope, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-1640170 Cell Cycle, R-HSA-1266738 Developmental Biology
- **partners:** SLC37A3, NELL1, NFE2L2
- **complexes:** ATRAID–SLC37A3 lysosomal complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | High | ATRAID forms a protein complex with SLC37A3 (solute carrier family 37 member A3), and both proteins localize to lysosomes. Together, they are required for releasing nitrogen-containing bisphosphonates (N-BPs) that have trafficked to lysosomes via fluid-phase endocytosis into the cytosol, enabling N-BPs to reach their molecular target (farnesyl diphosphate synthase) in the mevalonate pathway. | PMID:29745899 | eLife |
| 2020 | High | ATRAID is required for alendronate-mediated inhibition of protein prenylation and osteoclast function. Loss of ATRAID confers selective resistance to N-BP-mediated cell viability loss. ATRAID-deficient mice have impaired therapeutic responses to alendronate in postmenopausal and senile osteoporosis models. Patient-derived nonsynonymous coding variants in ATRAID confer cellular hypersensitivity to N-BPs. | PMID:32434850 | Science translational medicine |
| 2015 | Medium | APR3 is a lysosomal membrane protein. Western blot of isolated lysosomes demonstrated APR3 is present in the lysosomal membrane fraction but not in the endoplasmic reticulum. Double immunofluorescence confirmed co-localization with lysosomal membrane protein LAMP1 and lysosomal marker Lyso-Tracker Red. | PMID:25839652 | Biochemical and biophysical research communications |
| 2023 | Medium | ATRAID isoform C (Iso C) is the predominantly expressed isoform; it is N-glycosylated and localizes to cytoplasmic vesicles, near the plasma membrane, and in the Golgi area. It co-localizes with endosomal/lysosomal markers LAMP1 and LAMP2, and with RAB11, a GTPase associated with recycling endosomes implicated in vesicular trafficking. Isoform A is rapidly degraded; Isoform B protein was not detected. | PMID:37530719 | FEBS open bio |
| 2007 | Medium | APR3 overexpression causes G1/S cell cycle arrest accompanied by dramatic reduction in Cyclin D1 expression. The truncated form of APR3 (lacking the predicted transmembrane and intracellular domain) antagonizes this effect, indicating the transmembrane/intracellular domain is required for membrane localization and negative regulation of the cell cycle. | PMID:17524364 | Biochemical and biophysical research communications |
| 2007 | Medium | APR3 has two transcripts driven by distinct promoters (not alternative splicing). Constitutively active NFAT enhances both APR3 promoter activities, with functional NFAT binding sites mapped between -96 bp and -47 bp. Constitutively active NFκB inhibits APR3 transcription. | PMID:17387583 | Molecular and cellular biochemistry |
| 2011 | Medium | NELL-1 physically binds to APR3 (identified by biopanning). NELL-1 and APR3 co-localize on the nuclear envelope of human osteoblasts. NELL-1 inhibits osteoblast proliferation in cells co-transfected with APR3 through further downregulation of Cyclin D1. Co-expression of NELL-1 and APR3 enhances osteocalcin and bone sialoprotein expression and mineralization; RNAi of APR3 reduces the differentiation effect of NELL-1. | PMID:21723284 | FEBS letters |
| 2019 | Medium | Endogenous NELL-1 co-immunoprecipitates with APR3 reciprocally in human dental pulp cells. NELL-1 and APR3 co-localize on the nuclear envelope. NELL-1 inhibits proliferation of cells co-infected with APR3 through Cyclin D1 downregulation. The NELL-1/APR3 interaction stimulates alkaline phosphatase activity and promotes expression of DSPP, ALP, OPN, and BSP and mineralization; APR3 shRNA decreases differentiation and mineralization. | PMID:31416616 | Biochemical and biophysical research communications |
| 2018 | Medium | APR3 interacts with NRF2 (nuclear factor erythroid-derived 2-like 2). Knockdown of APR3 promotes NRF2 nuclear translocation and activates phase II enzyme expression, improving redox status and mitochondrial activity. Overexpression of APR3 induces reactive oxygen species production, impairs mitochondrial oxygen consumption and complex activity, reduces ATP content, and causes mitochondrial structural damage, contributing to apoptosis. APR3 overexpression reveals its mitochondrial localization. | PMID:29792731 | FASEB journal |
| 2016 | Low | APR3 overexpression promotes cellular senescence in ARPE-19 cells, characterized by enhanced senescence-associated β-galactosidase activity, reduced proliferation, and increased expression of p53 and p21. Overexpression of a truncated APR3-N (lacking transmembrane/intracellular domain) abrogates APR3-induced senescent phenotypes. | PMID:26934949 | Molecular medicine reports |

## Citations

- PMID:17387583
- PMID:17524364
- PMID:21723284
- PMID:25839652
- PMID:26934949
- PMID:29745899
- PMID:29792731
- PMID:31416616
- PMID:32434850
- PMID:37530719
