---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB14
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: A6NK59
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

# Affinage mechanistic annotation for ASB14 (human)

## Current model (mechanistic narrative)

ASB14 (Ankyrin Repeat and SOCS Box Containing 14) is an E3 ubiquitin ligase that restrains cardiomyocyte proliferation and cardiac repair by targeting the microtubule-associated protein MAPRE2 for ubiquitination and proteasomal degradation [PMID:38319584]. Loss of ASB14 stabilizes MAPRE2, driving cardiomyocyte nuclear proliferation and enhancing recovery of cardiac function after myocardial infarction [PMID:38319584]. Conversely, ASB14 overexpression in cardiomyocytes promotes apoptosis, suppresses proliferation, and impairs mitochondrial function, acting through downstream effectors including PIP4K2A, AMPK alpha-1, and RRAGC with metabolic reprogramming in linoleic acid and purine pathways [PMID:40417864]. Beyond these cardiomyocyte phenotypes, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-5357801 Programmed Cell Death
- **partners:** MAPRE2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | Medium | ASB14 functions as an E3 ubiquitin ligase that promotes ubiquitination and degradation of MAPRE2 (microtubule-associated protein RP/EB family member 2); loss of ASB14 decreases MAPRE2 protein degradation, which in turn promotes cardiomyocyte nuclear proliferation and enhances cardiac repair after myocardial infarction. | PMID:38319584 | Cell biochemistry and biophysics |
| 2025 | Medium | ASB14 overexpression in AC16 cardiomyocytes promotes apoptosis, inhibits cell proliferation, and inhibits mitochondrial function; proteomics and metabolomics identified downstream effectors including suppression of PIP4K2A, ferritin light chain, AMPK alpha-1, GLB1, ABCC9, and NME7, and upregulation of RRAGC, with enrichment in linoleic acid and purine metabolism pathways. | PMID:40417864 | FASEB journal : official publication of the Federation of American Societies for Experimental Biology |

## Citations

- PMID:38319584
- PMID:40417864
