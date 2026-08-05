---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD14A
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q9BUJ0
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 5
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABHD14A (human)

## Current model (mechanistic narrative)

ABHD14A is a metabolic serine hydrolase of the α/β-hydrolase superfamily, closely related at the sequence level to ABHD14B, from which it is distinguished by defined sequence determinants [PMID:37974539]. A soluble N-terminally truncated form is an active enzyme that preferentially hydrolyzes short-chain esters, and its p-nitrophenyl-acetate hydrolysis is enhanced by CoA, consistent with a ping-pong type acetyltransferase mechanism analogous to ABHD14B [PMID:bio_10.1101_2025.11.28.691245]. Heterologously expressed full-length protein localizes to the Golgi apparatus, while endogenous protein is undetectable across immortalized cell lines and adult mouse tissues despite transcriptomic predictions [PMID:bio_10.1101_2025.11.28.691245]. At the transcriptional level, ABHD14A (Dorz1) is positively regulated by the zinc-finger transcription factor Zic1 in cerebellar granule neuron precursors [PMID:14667578]. Beyond these findings, the physiological substrates and in vivo role of ABHD14A have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0016740 transferase activity
- **localization:** GO:0005794 Golgi apparatus
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2023 | Medium | ABHD14A is a member of the metabolic serine hydrolase superfamily with high sequence similarity to ABHD14B; bioinformatics coupled with biochemical experiments identified key sequence determinants distinguishing ABHD14A from ABHD14B, enabling better classification of each enzyme. ABHD14A still lacked functional annotation at the time of this study. | PMID:37974539 | Proteins |
| 2025 | Medium | ABHD14A is an active serine hydrolase enzyme that preferentially hydrolyzes short-chain esters, as demonstrated by gel-based activity-based protein profiling (ABPP) and p-nitrophenyl-ester hydrolysis assays using a soluble N-terminally truncated variant. ABHD14A exhibits CoA-dependent enhancement of p-nitrophenyl-acetate hydrolysis, indicative of a ping-pong type acetyltransferase mechanism similar to ABHD14B. | PMID:bio_10.1101_2025.11.28.691245 | bioRxiv |
| 2025 | Medium | Upon heterologous expression in HEK293T cells, full-length ABHD14A localizes specifically to the Golgi apparatus, suggesting a specialized role in secretory pathway biology. Endogenous ABHD14A protein is undetectable across a panel of immortalized mammalian cell lines and adult mouse tissues, contradicting transcriptomic database predictions. | PMID:bio_10.1101_2025.11.28.691245 | bioRxiv |
| 2003 | Medium | Dorz1 (ABHD14A) expression in cerebellar granule neuron precursors is positively regulated by the transcription factor Zic1; Dorz1 was identified as one of the most significantly down-regulated genes in Zic1-deficient cerebellum, and Dorz1 expression was up-regulated in cultured cells overexpressing Zic1. | PMID:14667578 | Brain research. Molecular brain research |
| 2018 | Low | Abhd14a mRNA expression is enzymatically upregulated in some tissues of Bphl knockout mice, indicating that ABHD14A expression can be compensatorily induced in the absence of the related serine hydrolase BPHL. | PMID:30121252 | Biochemical pharmacology |

## Citations

- PMID:14667578
- PMID:30121252
- PMID:37974539
- PMID:bio_10.1101_2025.11.28.691245
