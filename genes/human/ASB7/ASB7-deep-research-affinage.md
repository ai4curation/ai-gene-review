---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB7
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9H672
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB7 (human)

## Current model (mechanistic narrative)

ASB7 is the substrate-recognition subunit of a CUL5-based E3 ubiquitin ligase complex that selects specific protein substrates for proteasomal degradation, thereby coordinating mitotic spindle dynamics, heterochromatin homeostasis, and transcriptional control [PMID:27697924, PMID:40440427, PMID:42086529]. It ubiquitinates DDA3 to restrain its activity in spindle regulation; microtubules block the ASB7-DDA3 interaction to stabilize DDA3, and ASB7 loss reduces microtubule polymerization and increases chromosome misalignment in a DDA3-dependent manner [PMID:27697924]. The CUL5-ASB7 complex is recruited to heterochromatin by HP1 and degrades the H3K9 methyltransferase SUV39H1 to act as a negative regulator of H3K9me3, a function that is switched off during mitosis when CDK1 phosphorylates ASB7 and disrupts its binding to SUV39H1, allowing SUV39H1 to accumulate and H3K9me3 to be restored [PMID:40440427]. ASB7 also ubiquitinates ATF2 at lysine 383; loss of ATF2 reduces HDAC6 recruitment to the ITGB2 promoter, derepressing ITGB2 transcription and promoting lung metastasis [PMID:42086529]. Consistent with its spindle role in mitotic cells, ASB7 depletion in mouse oocytes disrupts meiotic spindle assembly and cytoskeletal organization [PMID:33251222].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins, R-HSA-4839726 Chromatin organization, R-HSA-1643685 Disease
- **partners:** CUL5, DDA3, SUV39H1, ATF2, HP1, CDK1
- **complexes:** CUL5-ASB7 E3 ubiquitin ligase

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | ASB7 functions as an E3 ubiquitin ligase in complex with Cullin 5 (CUL5-ASB7) that ubiquitinates DDA3 (a regulator of spindle dynamics) and targets it for proteasomal degradation. The presence of microtubules prevented the ASB7-DDA3 interaction, stabilizing DDA3. Knockdown of ASB7 decreased microtubule polymerization and increased unaligned chromosomes, a phenotype rescued by deletion of DDA3. | PMID:27697924 | The Journal of cell biology |
| 2025 | High | ASB7 forms a CUL5-ASB7 E3 ubiquitin ligase complex that is recruited to heterochromatin by HP1 and promotes SUV39H1 proteasomal degradation, thereby acting as a negative regulator of H3K9me3 homeostasis. During mitosis, CDK1 phosphorylates ASB7, preventing its interaction with SUV39H1, leading to SUV39H1 stabilization and H3K9me3 restoration. | PMID:40440427 | Science (New York, N.Y.) |
| 2020 | Medium | ASB7 knockdown in mouse oocytes disrupts spindle assembly, causes chromosome misalignment, loss of cortical actin cap, impaired kinetochore-microtubule interaction, and activates the spindle assembly checkpoint during meiosis, establishing a role for ASB7 in cytoskeletal organization during oocyte maturation. | PMID:33251222 | Frontiers in cell and developmental biology |
| 2018 | Low | ASB7 expression is upregulated by ER stress in HeLa cells via ERSE regulatory elements, with simultaneous UPR pathway activation. ASB7 knockdown significantly reduced GRP78 and CHOP mRNA levels but did not protect cells from ER stress-induced cell death, and increased pro-inflammatory gene expression (TNF-α, IL-1β) under ER stress. | PMID:29630609 | PloS one |
| 2026 | High | ASB7 forms an E3 ubiquitin ligase complex with CUL5 to ubiquitinate ATF2 at lysine 383 and promote its proteasomal degradation. ATF2 reduction impairs HDAC6 recruitment to the ITGB2 promoter, relieving transcriptional repression of ITGB2, which promotes tumor lung metastasis. | PMID:42086529 | Cell discovery |

## Citations

- PMID:27697924
- PMID:29630609
- PMID:33251222
- PMID:40440427
- PMID:42086529
