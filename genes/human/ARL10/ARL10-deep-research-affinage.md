---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL10
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N8L6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 3
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARL10 (human)

## Current model (mechanistic narrative)

ARL10 is an ARF-like small GTPase whose subcellular localization and proximal interactor network are distinct from other ARF/ARL family members, as defined by proximity-dependent biotin labeling [PMID:38606629]. Its transcription is directly activated by HIF-1α (but not HIF-2α) binding within an intragenic region in a kidney-cell-specific manner downstream of VHL loss [PMID:41998206]. Beyond this proximity-labeling localization and its HIF-1α-driven regulation, ARL10's biochemical substrates, GTPase activity, and effector mechanisms have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | Medium | BioID proximity-labeling in two cellular models assigned a previously undefined subcellular localization to ARL10 and revealed a distinctive set of proximal interactors for ARL10 compared to other ARF/ARL family members. | PMID:38606629 | Journal of cell science |
| 2023 | Low | BioID proximity-labeling (preprint version) uncovered a previously undefined subcellular localization for ARL10 and demonstrated the distinctiveness of its proximal interactor network relative to other ARF/ARL GTPases. | PMID:36909472 | bioRxiv |
| 2026 | Medium | HIF-1α (but not HIF-2α) directly binds within the intragenic region of ARL10 in a kidney-cell-specific manner, driving ARL10 transcriptional upregulation downstream of VHL loss; demonstrated by ChIP-seq dataset analysis and luciferase reporter assays. | PMID:41998206 | British journal of cancer |

## Citations

- PMID:36909472
- PMID:38606629
- PMID:41998206
