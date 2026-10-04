---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC6
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q6NXE6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 4
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC6 (human)

## Current model (mechanistic narrative)

ARMC6 is an armadillo-repeat protein implicated in telomere biology and gene regulation. In vitro it co-precipitates telomerase activity and interacts with the shelterin component hTRF2 [PMID:29948659], and recombinant ARMC6 preferentially binds G-quadruplex structures formed by telomeric RNA repeats (TERRA) and the promoter sequences of cancer-related genes including EGFR, VEGF, and c-MYC [PMID:39029558]. Consistent with a gene-regulatory role, ARMC6 overexpression in human cell lines alters expression of oncogenic and non-canonical telomerase pathway genes such as VEGF, hTERT, c-MYC, ESM1, and MMP3 [PMID:39029558]. ARMC6 is also a substrate of the histidine methyltransferase METTL9, which generates 1-methylhistidine at its HxH motifs [PMID:40451431]. Beyond these in vitro and overexpression observations, a defined mechanistic function for ARMC6 has not been established in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** TRF2, METTL9
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | Low | Human ARMC6 protein co-precipitates telomerase activity and interacts with hTRF2 (telomeric repeat-binding factor 2) in vitro, suggesting participation in a telomerase interaction network. | PMID:29948659 | Plant molecular biology |
| 2024 | Low | Human ARMC6 binds in vitro to DNA promoter sequences from cancer-related genes (EGFR, VEGF, c-MYC) and to telomeric RNA repeats (TERRA), with preferential recognition of G-quadruplex structures over linear DNA/RNA. | PMID:39029558 | Biochimica et biophysica acta. Gene regulatory mechanisms |
| 2024 | Low | ARMC6 overexpression in human cell lines alters expression of genes connected with oncogenic pathways and non-canonical telomerase pathways (VEGF, hTERT, c-MYC, ESM1, MMP3), consistent with a gene-regulatory role. | PMID:39029558 | Biochimica et biophysica acta. Gene regulatory mechanisms |
| 2025 | Medium | ARMC6 is a substrate of the human protein histidine methyltransferase METTL9, which generates 1-methylhistidine (π-methylhistidine) at HxH motifs; ARMC6 was used as a prototype substrate to demonstrate METTL9 activity across eukaryotic orthologues. | PMID:40451431 | The Journal of biological chemistry |

## Citations

- PMID:29948659
- PMID:39029558
- PMID:40451431
