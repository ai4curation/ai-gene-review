---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AAMDC
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q9H7C9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 4
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AAMDC (human)

## Current model (mechanistic narrative)

AAMDC is an oncogenic signaling regulator amplified in estrogen receptor-positive breast cancer that drives estrogen-independent tumor growth by activating the PI3K-AKT-mTOR axis [PMID:33772001]. Downstream of this signaling, AAMDC controls the translational upregulation of ATF4 and MYC and the transcriptional output of AAMDC-dependent promoters, and ectopic AAMDC expression is sufficient to activate AKT [PMID:33772001]. Through these effectors AAMDC reprograms cellular metabolism, governing the expression of enzymes in the one-carbon folate, methionine, and lipid metabolism pathways [PMID:33772001]. AAMDC physically interacts with the Rab GTPase-activating protein RabGAP1L and colocalizes with RabGAP1L and Rab7a at endolysosomes, forming an assembly platform that links it to the endolysosomal compartment [PMID:33772001]. Beyond these findings, the biochemical activity of AAMDC itself and the structural basis of its signaling and RabGAP1L interaction have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005764 lysosome, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** RABGAP1L, RAB7A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | Medium | AAMDC regulates PI3K-AKT-mTOR signaling, controlling the translational regulation of ATF4 and MYC, and modulating the transcriptional activity of AAMDC-dependent promoters; ectopic AAMDC expression is sufficient to activate AKT signaling, resulting in estrogen-independent tumor growth in estrogen receptor-positive breast cancer models. | PMID:33772001 | Nature communications |
| 2021 | Medium | AAMDC regulates the expression of metabolic enzymes involved in the one-carbon folate and methionine cycles and lipid metabolism in estrogen receptor-positive breast cancer cells. | PMID:33772001 | Nature communications |
| 2021 | Medium | AAMDC physically interacts with the RabGTPase-activating protein RabGAP1L, and AAMDC, RabGAP1L, and Rab7a colocalize in endolysosomes, forming an assembly platform. | PMID:33772001 | Nature communications |
| 2023 | Low | AAMDC promotes autophagy in gastric cancer cells through the AAMDC/MYC/ATF4/Sesn2 signaling pathway; overexpression of AAMDC reversed the inhibitory effect of solanine on autophagy, placing AAMDC upstream of MYC, ATF4, and Sesn2 in this pathway. | PMID:36789094 | Drug design, development and therapy |

## Citations

- PMID:33772001
- PMID:36789094
