---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKDD1A
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q495B1
self_evaluation_pairwise: 
faith_pct: 66.66666666666667
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

# Affinage mechanistic annotation for ANKDD1A (human)

## Current model (mechanistic narrative)

ANKDD1A functions as a negative regulator of the hypoxic transcriptional response in glioma, acting as a tumor suppressor whose loss favors hypoxic adaptation of tumor cells [PMID:30082910, PMID:21962230]. Mechanistically, ANKDD1A directly binds FIH1 (factor inhibiting HIF-1) and upregulates its activity, which destabilizes HIF1α by shortening its half-life and represses HIF1α-driven transcription; the downstream consequences include reduced glucose uptake and lactate production, inhibition of autophagy, and induction of apoptosis in glioblastoma cells under hypoxia [PMID:30082910]. ANKDD1A expression is suppressed in primary glioma through promoter hypermethylation and altered histone modifications, and can be restored via miR-185-mediated targeting of DNMT1 [PMID:21962230]. Beyond its FIH1/HIF1α axis in glioma, no further molecular detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-8953897 Cellular responses to stimuli
- **partners:** FIH1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | Medium | ANKDD1A directly interacts with FIH1 (factor inhibiting HIF-1) and inhibits the transcriptional activity of HIF1α by upregulating FIH1; ANKDD1A also decreases the half-life of HIF1α through FIH1 upregulation, leading to decreased glucose uptake, reduced lactate production, inhibition of autophagy, and induction of apoptosis in glioblastoma cells under hypoxia. | PMID:30082910 | Oncogene |
| 2011 | Medium | ANKDD1A promoter is hypermethylated in primary glioma relative to normal brain tissue, and its reduced expression is associated with aberrant promoter methylation and altered histone modifications; induction of miR-185 overexpression (which targets DNMT1) restored ANKDD1A expression in glioma cells. | PMID:21962230 | Molecular cancer |

## Citations

- PMID:21962230
- PMID:30082910
