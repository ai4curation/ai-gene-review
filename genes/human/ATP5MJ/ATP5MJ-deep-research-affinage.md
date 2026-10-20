---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATP5MJ
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P56378
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for ATP5MJ (human)

## Current model (mechanistic narrative)

ATP5MJ (MLQ/6.8PL) encodes a small mitochondrial proteolipid that post-transcriptionally controls the abundance of the ATP synthase complex [PMID:24330338]. Its knockdown reduces the mitochondrial population of ATP synthase without altering the mRNA levels of ATP synthase α- and β-subunits, and lowers mitochondrial ATP synthesis activity, slows cell growth, and sensitizes cells to glucose deprivation, establishing it as a determinant of assembled ATP synthase levels rather than a transcriptional regulator [PMID:24330338]. The ATP5MJ 3' UTR harbors a functional SECIS element that binds SECISBP2 and supports UGA readthrough for selenocysteine insertion, linking the transcript to selenoprotein synthesis machinery [PMID:41201471]. Beyond these observations, the structural basis of its association with ATP synthase and its mechanism of action have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** ATP synthase

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | MLQ (ATP5MJ/6.8PL) knockdown in HeLa cells reduces the population of ATP synthase in mitochondria without affecting mRNA levels of ATP synthase α- and β-subunits, indicating that MLQ controls ATP synthase abundance post-transcriptionally. Knockdown cells show decreased mitochondrial ATP synthesis activity, slower growth, and increased vulnerability to glucose deprivation. | PMID:24330338 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2014 | Low | The 6.8 kDa mitochondrial proteolipid MLQ (ATP5MJ) was identified as differentially expressed in mitochondria isolated from peripheral blood mononuclear cells of type 2 diabetic patients compared to healthy controls, placing it among ATP synthase-related proteins altered in disease. | PMID:25420343 | European journal of mass spectrometry (Chichester, England) |
| 2025 | Medium | The 3' UTR of ATP5MJ mRNA contains a functional SECIS (selenocysteine insertion sequence) element, as validated by luciferase assays and fusion to known selenoprotein RNAs, indicating that ATP5MJ transcripts can support UGA stop codon readthrough for selenocysteine insertion. | PMID:41201471 | Redox biology |

## Citations

- PMID:24330338
- PMID:25420343
- PMID:41201471
