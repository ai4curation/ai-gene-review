---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD10
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9NXR5
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 1
citation_count: 1
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD10 (human)

## Current model (mechanistic narrative)

ANKRD10 is regulated at the level of alternative splicing by the RNA-binding protein RBPMS, and its splice isoform ANKRD10-2 functions as a transcriptional co-activator of MYC in bladder cancer [PMID:40044952]. Depletion of RBPMS shifts splicing toward the ANKRD10-2 isoform, which augments MYC transcriptional activity and drives cancer cell migration and invasion [PMID:40044952]. Beyond this RBPMS–ANKRD10-2–MYC axis, no further mechanistic detail for ANKRD10 has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription)
- **partners:** MYC
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2025 | Medium | RBPMS depletion in bladder cancer cells causes alternative splicing of ANKRD10, increasing expression of the ANKRD10-2 isoform, which functions as a transcriptional co-activator of MYC proteins to augment their transcriptional activity and promote cell migration/invasion. | PMID:40044952 | Communications biology |

## Citations

- PMID:40044952
