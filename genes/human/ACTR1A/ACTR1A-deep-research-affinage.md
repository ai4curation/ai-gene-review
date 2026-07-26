---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTR1A
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: P61163
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 2
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ACTR1A (human)

## Current model (mechanistic narrative)

ACTR1A (alpha-centractin) is a subunit of the dynactin complex that additionally participates in innate immune signaling and is subject to post-translational regulation [PMID:31221720, PMID:41142317]. ACTR1A physically associates with TLR2 and is required for TLR2-mediated pro-inflammatory cytokine induction, since its knockdown reduces cytokine output downstream of the receptor [PMID:31221720]. ACTR1A is also an in vitro substrate of the SETD3 protein histidine methyltransferase, which methylates recombinant ACTR1A and contacts it in cells, extending SETD3's substrate repertoire beyond beta-actin to this dynactin subunit [PMID:41142317]. Beyond these findings, the structural basis of these interactions, the in-cell methylation site, and the link between ACTR1A modification and dynactin function have not been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** TLR2, SETD3
- **complexes:** dynactin

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | Medium | ACTR1A (alpha-centractin), a subunit of the dynactin complex, physically interacts with TLR2 and functions as a regulator of TLR2-mediated pro-inflammatory cytokine induction. The interaction was identified by cross-linking co-immunoprecipitation proteomics and validated by biochemical methods; RNA interference knockdown of ACTR1A reduced pro-inflammatory cytokine induction downstream of TLR2. | PMID:31221720 | Molecular & Cellular Proteomics |
| 2025 | Medium | ACTR1A (alpha-centractin) is an in vitro substrate of the SETD3 protein histidine methyltransferase. SETD3 was identified as a proximal interactor of ACTR1A by TurboID proximity labeling, and recombinant SETD3 methylated ACTR1A in a radiochemical in vitro methylation assay, extending SETD3's known substrate repertoire beyond β-actin to this dynactin subunit. | PMID:41142317 | PeerJ |

## Citations

- PMID:31221720
- PMID:41142317
