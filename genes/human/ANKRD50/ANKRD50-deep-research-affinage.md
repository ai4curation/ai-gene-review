---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD50
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9ULJ7
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

# Affinage mechanistic annotation for ANKRD50 (human)

## Current model (mechanistic narrative)

ANKRD50 is an essential component of the endosomal SNX27-retromer-WASH supercomplex that supports endosome-to-plasma-membrane recycling of transmembrane cargo [PMID:27909246]. It was first identified as a VPS35-interacting protein, with its depletion causing trafficking defects of retromer-dependent cargo [PMID:25278552]. ANKRD50 simultaneously engages multiple parts of the SNX27-retromer-WASH machinery through direct and cooperative interactions, and its loss phenocopies suppression of SNX27, retromer, or WASH components, impairing cell-surface recycling of transmembrane proteins including the nutrient transporters GLUT1/SLC2A1 and SLC1A4 [PMID:27909246]. The Parkinson's disease-causing VPS35 D620N mutation perturbs retromer's association with ANKRD50 [PMID:27909246]. Beyond these interaction and cargo-recycling findings, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005768 endosome
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization
- **partners:** VPS35, SNX27
- **complexes:** SNX27-retromer-WASH supercomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | ANKRD50 was identified as a novel interacting protein of VPS35, the core retromer component, via quantitative proteomics of the human VPS35 interactome. Depletion of ANKRD50 resulted in trafficking defects of retromer-dependent cargo, indicating a functional role in endosome-to-plasma-membrane sorting. | PMID:25278552 | Journal of cell science |
| 2016 | High | ANKRD50 was established as an essential component of the SNX27-retromer-WASH supercomplex. Mechanistically, ANKRD50 simultaneously engages multiple parts of the SNX27-retromer-WASH machinery through direct and cooperative interactions. Depletion of ANKRD50 in HeLa or U2OS cells phenocopied loss of endosome-to-cell-surface recycling of multiple transmembrane proteins (including GLUT1/SLC2A1 and SLC1A4) seen upon suppression of SNX27, retromer, or WASH complex components. The Parkinson's disease-causing VPS35 D620N mutation also perturbs retromer's association with ANKRD50. | PMID:27909246 | Journal of cell science |

## Citations

- PMID:25278552
- PMID:27909246
