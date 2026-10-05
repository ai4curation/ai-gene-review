---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC8
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8IUR7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC8 (human)

## Current model (mechanistic narrative)

ARMC8 is an evolutionarily ancestral armadillo-repeat protein that regulates the cadherin/catenin cell-adhesion apparatus and Wnt/β-catenin signaling to control epithelial-mesenchymal transition (EMT), invasion, and proliferation in cancer cells [PMID:30482882, PMID:26944057, PMID:27712595]. Through its ARM repeats it binds specifically to αE-catenin (but not αN- or αT-catenin) and to the δ-catenin family plakophilins-1, -2, -3 and p0071 [PMID:30482882]. Functionally, ARMC8 promotes degradation of α-catenin and disruption of the E-cadherin/catenin complex: its depletion in hepatocellular carcinoma cells upregulates α-catenin, β-catenin and E-cadherin and restores E-cadherin to the membrane [PMID:26944057]. ARMC8 acts upstream of Wnt/β-catenin signaling, modulating β-catenin, c-Myc and cyclin D1 levels and the invasion-associated factors MMP7, Snail and p120ctn [PMID:26081621, PMID:27712595], and it mediates TGF-β1-induced EMT through this pathway [PMID:28081738]. Its net effect is context-dependent, behaving as an invasion/proliferation driver in colon, ovarian, osteosarcoma and bladder cells [PMID:26081621, PMID:26232863, PMID:27712595, PMID:28081738] but as a tumor suppressor in cutaneous squamous cell carcinoma [PMID:34016486]; in several contexts ARMC8 is a direct downstream target of repressive microRNAs miR-664 and miR-455-3p [PMID:34016486, PMID:37400847]. Phylogenetic analysis establishes ARMC8 as a highly conserved metazoan armadillo protein that is not the ortholog of yeast Gid5/Vid28 [PMID:30482882].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008092 cytoskeletal protein binding, GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1500931 Cell-Cell communication
- **partners:** CTNNA1, PKP1, PKP2, PKP3, PKP4
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | Medium | ARMC8 interacts specifically with δ-catenins (plakophilins-1, -2, -3 and p0071) as shown by yeast two-hybrid and confirmed by co-immunoprecipitation and co-localization; ARMC8 also interacts specifically with αE-catenin but not with αN-catenin or αT-catenin. | PMID:30482882 | Bioscience reports |
| 2019 | Medium | Phylogenetic analysis established that ARMC8 is NOT the human ortholog of yeast Gid5/Vid28; it is a highly ancestral armadillo protein present in metazoans but absent in yeast. | PMID:30482882 | Bioscience reports |
| 2016 | Medium | Knockdown of ARMC8 in HepG2 hepatocellular carcinoma cells significantly upregulated α-catenin, β-catenin, and E-cadherin expression and restored E-cadherin to the cell membrane, indicating ARMC8 promotes degradation of α-catenin and disruption of the E-cadherin/catenin complex. | PMID:26944057 | Tumour biology |
| 2015 | Medium | Overexpression of ARMC8 in colon cancer cells upregulated MMP7 and Snail while downregulating p120ctn and α-catenin; siRNA-mediated knockdown had the reverse effect, placing ARMC8 upstream of these invasion-associated factors. | PMID:26081621 | Tumour biology |
| 2015 | Medium | Overexpression of ARMC8 in ovarian cancer cells enhanced invasion/migration and upregulated MMP7 and Snail while downregulating α-catenin, p120ctn, and E-cadherin; siRNA knockdown had the reverse effects. | PMID:26232863 | Human pathology |
| 2016 | Medium | Knockdown of ARMC8 in osteosarcoma MG-63 cells inhibited proliferation in vitro and xenograft tumor growth in vivo, suppressed EMT, and reduced expression of β-catenin, c-Myc, and cyclin D1, placing ARMC8 upstream of the Wnt/β-catenin pathway. | PMID:27712595 | Oncology research |
| 2017 | Medium | Silencing of ARMC8 in bladder carcinoma UMUC3 cells inhibited TGF-β1-induced migration, invasion, and EMT, and suppressed TGF-β1-induced expression of β-catenin, cyclin D1, and c-Myc, establishing ARMC8 as a mediator of TGF-β1-induced EMT through modulation of the Wnt/β-catenin signaling pathway. | PMID:28081738 | Oncology research |
| 2021 | Medium | In cutaneous squamous cell carcinoma cells, ARMC8 functions as a tumor suppressor: knockdown promoted proliferation, migration, and invasion via activation of Wnt/β-catenin signaling and EMT, while overexpression inhibited these processes. ARMC8 was identified as a direct downstream target of miR-664. | PMID:34016486 | Journal of dermatological science |
| 2023 | Medium | ARMC8 was confirmed as a direct downstream target of miR-455-3p by luciferase reporter assay; miR-455-3p repressed Wnt/β-catenin signaling through binding to ARMC8, and ARMC8 overexpression partially reversed the tumor-suppressive effects of miR-455-3p in gastric cancer cells. | PMID:37400847 | BMC medical genomics |
| 2013 | Low | Yeast Vid28p (proposed ortholog, but phylogenetically refuted as the true ortholog of human ARMC8 by a later study) contains an Armadillo (ARM) domain required for FBPase degradation; deletion of VID28 or mutation of the ARM domain caused Vid vesicles to fail to co-localize with actin patches, and Vid vesicle proteins appeared in the extracellular fraction. Vid28p distributed to Vid vesicles and interacted with other Vid vesicle proteins. | PMID:23393132 | The Journal of biological chemistry |

## Citations

- PMID:23393132
- PMID:26081621
- PMID:26232863
- PMID:26944057
- PMID:27712595
- PMID:28081738
- PMID:30482882
- PMID:34016486
- PMID:37400847
