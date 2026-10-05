---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD33
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q7Z3H0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD33 (human)

## Current model (mechanistic narrative)

ANKRD33 (PANKY) is a photoreceptor-specific ankyrin repeat protein that acts as a transcriptional cofactor in the retinal gene regulatory network [PMID:20026326]. Its expression is directly induced by the CRX homeodomain transcription factor, and ANKRD33 in turn suppresses CRX-activated photoreceptor genes by inhibiting CRX DNA-binding activity, as demonstrated by electrophoretic mobility shift assay, thereby forming a negative-feedback loop on CRX-driven transcription [PMID:20026326]. The PANKY-A isoform localizes to both the nucleus and the cytoplasm, consistent with a role bridging transcriptional regulation and a cytoplasmic function [PMID:20026326]. Beyond this CRX feedback role, the mechanistic detail of ANKRD33 has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** *(none)*
- **partners:** CRX
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | Medium | PANKY/ANKRD33 is a photoreceptor-specific ankyrin repeat protein that acts as a transcriptional cofactor suppressing CRX-activated photoreceptor genes; PANKY-A localizes to both nucleus and cytoplasm, its expression is directly upregulated by the CRX transcription factor, and it inhibits the DNA-binding activity of CRX as shown by electrophoretic mobility shift assay. | PMID:20026326 | FEBS letters |
| 2012 | Low | Ankrd33 expression in retinal photoreceptors is downstream of NeuroD1 transcription factor; Ankrd33 mRNA is significantly down-regulated in NeuroD1 conditional knockout retinas, and the ANKRD33 protein product is selectively expressed in photoreceptor outer segments. | PMID:22784109 | Journal of neurochemistry |

## Citations

- PMID:20026326
- PMID:22784109
