---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC12
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T9G4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC12 (human)

## Current model (mechanistic narrative)

ARMC12 is a mitochondrial peripheral membrane protein that acts as an adherence factor driving mitochondrial sheath assembly during spermiogenesis [PMID:33536340]. In testicular germ cells it scaffolds mitochondria together by binding VDAC2 and VDAC3 and interacting with MIC60, TBC1D21, and GK2, with TBC1D21 acting as an obligate mediator of the ARMC12–VDAC interaction [PMID:33536340]. Loss of ARMC12 blocks mitochondrial elongation at the interlocking step, producing abnormal mitochondrial coiling along the flagellum, reduced sperm motility, and male sterility [PMID:33536340]; biallelic loss-of-function mutations in humans cause asthenozoospermia with absent mitochondrial sheath and associated midpiece and axonemal defects, establishing a conserved role [PMID:35534203]. Independent of this germline function, ARMC12 has been characterized in neuroblastoma, where it interacts with RBBP4 to promote PRC2-mediated transcriptional repression of tumor suppressor genes [PMID:30026490] and partners with MYC within liquid condensates to upregulate nucleoporin genes (NUP62, NUP93, NUP98) and nuclear pore complex biogenesis, enhancing invasion and metastasis [PMID:41510169].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005739 mitochondrion, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-4839726 Chromatin organization
- **partners:** VDAC2, VDAC3, MIC60, TBC1D21, GK2, RBBP4, MYC
- **complexes:** PRC2

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | ARMC12 is a mitochondrial peripheral membrane protein that functions as an adherence factor between mitochondria. In testicular germ cells, ARMC12 physically interacts with mitochondrial proteins MIC60, VDAC2, and VDAC3, as well as TBC1D21 and GK2, using VDAC2 and VDAC3 as scaffolds to link mitochondria together during mitochondrial sheath formation in spermiogenesis. | PMID:33536340 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | High | TBC1D21 is required for the interaction between ARMC12 and VDAC proteins in vivo; in Tbc1d21-null mice, the ARMC12–VDAC interaction is disrupted, establishing TBC1D21 as an obligate mediator of this scaffold complex. | PMID:33536340 | Proceedings of the National Academy of Sciences of the United States of America |
| 2021 | High | Absence of ARMC12 prevents mitochondrial elongation at the mitochondrial interlocking step during spermiogenesis, causing abnormal mitochondrial coiling along the flagellum, reduced sperm motility, and male sterility. | PMID:33536340 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | Medium | ARMC12 physically interacts with retinoblastoma binding protein 4 (RBBP4) to facilitate the formation and activity of polycomb repressive complex 2 (PRC2), resulting in transcriptional repression of tumor suppressive genes in neuroblastoma cells. | PMID:30026490 | Nature communications |
| 2022 | High | Biallelic loss-of-function mutations in ARMC12 in humans cause asthenozoospermia with multiple midpiece defects including absent mitochondrial sheath, absent central pair, scattered or forked axoneme, and incomplete plasma membrane, confirming the conserved mitochondrial sheath assembly function of ARMC12 in humans. | PMID:35534203 | Journal of medical genetics |
| 2026 | Medium | In a patient with MMAF carrying a homozygous ARMC12 c.686G>A variant, ARMC12 loss causes severe disorganization of mitochondrial sheath structures and loss of axonemal elements; mitochondrial outer membrane proteins COX IV and TOM20 shift from a continuous distribution along the mitochondrial sheath to a discontinuous punctate pattern without significant reduction in total protein levels. | PMID:41971121 | Translational andrology and urology |
| 2026 | Medium | ARMC12 interacts with MYC within liquid condensates in neuroblastoma cells and upregulates nucleoporin-encoding targets (NUP62, NUP93, NUP98), promoting nuclear pore complex biogenesis to facilitate nuclear trafficking of oncogenic effectors and enhance invasion and metastasis. | PMID:41510169 | Theranostics |

## Citations

- PMID:30026490
- PMID:33536340
- PMID:35534203
- PMID:41510169
- PMID:41971121
