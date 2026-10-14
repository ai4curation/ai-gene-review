---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB13
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXK3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 4
citation_count: 1
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB13 (human)

## Current model (mechanistic narrative)

ASB13 is an E3 ubiquitin ligase that acts as a suppressor of breast cancer cell migration and metastasis by controlling the stability of the transcription factor SNAI2 [PMID:32943576]. Identified in a genome-wide E3 ligase siRNA screen, ASB13 directly ubiquitinates SNAI2 and targets it for proteasomal degradation [PMID:32943576]. By depleting SNAI2, ASB13 relieves SNAI2-mediated transcriptional repression of YAP, so that ASB13 loss reduces YAP expression in a SNAI2-dependent manner, placing ASB13 upstream of a SNAI2–YAP regulatory axis [PMID:32943576]. Functionally, ASB13 knockout in breast cancer cells promotes migration and decreases F-actin polymerization, whereas ASB13 overexpression suppresses lung metastasis in vivo, and the downstream effector YAP itself restrains tumorsphere formation, anchorage-independent growth, migration, and metastasis [PMID:32943576]. Beyond this SNAI2–YAP axis in breast cancer, no further mechanistic detail for ASB13 has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-1643685 Disease
- **partners:** SNAI2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | High | ASB13 functions as an E3 ubiquitin ligase that targets SNAI2 for ubiquitination and proteasomal degradation, identified through a dual-luciferase-based genome-wide E3 ligase siRNA library screen. | PMID:32943576 | Genes & development |
| 2020 | High | ASB13 knockout in breast cancer cells promotes cell migration and decreases F-actin polymerization, while ASB13 overexpression suppresses lung metastasis in vivo, establishing ASB13 as a suppressor of breast cancer metastasis. | PMID:32943576 | Genes & development |
| 2020 | High | ASB13-mediated degradation of SNAI2 relieves SNAI2's transcriptional repression of YAP; ASB13 knockout decreases YAP expression in a SNAI2-dependent manner, placing ASB13 upstream of the SNAI2–YAP axis. | PMID:32943576 | Genes & development |
| 2020 | Medium | YAP suppresses tumor progression in breast cancer: YAP knockout increases tumorsphere formation, anchorage-independent colony formation, cell migration in vitro, and lung metastasis in vivo, confirming YAP as a downstream effector of the ASB13–SNAI2 axis. | PMID:32943576 | Genes & development |

## Citations

- PMID:32943576
