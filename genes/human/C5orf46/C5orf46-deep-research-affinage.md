---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/C5orf46
affinage_run_date: 2026-06-09T22:02:45
uniprot_accession: Q6UWT4
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 4
citation_count: 3
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for C5orf46 (human)

## Current model (mechanistic narrative)

C5ORF46 encodes AP-64, a small (64-amino-acid, ~7.2 kDa) anionic, amphiphilic, cysteine-free peptide detectable in human plasma that functions as a secreted antimicrobial peptide [PMID:31308252, PMID:33804835]. AP-64 exerts direct bactericidal activity against multiple Gram-negative bacteria in vitro and reduces E. coli O157:H7 infection in a mouse model [PMID:33804835]. Beyond its antibacterial role, no defined molecular mechanism, receptor, or binding partner has been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** *(none)*
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | Medium | C5ORF46 encodes AP-64, a 64-amino-acid anionic amphiphilic peptide lacking cysteines (MW=7.2 kDa, pI=4.54) that exhibits direct antimicrobial activity against Gram-negative bacteria including E. coli DH5α, E. coli O157:H7, Vibrio cholerae, and Pseudomonas aeruginosa in vitro, and reduces E. coli O157:H7 infection in a mouse model. | PMID:33804835 | Biomolecules |
| 2021 | Low | AP-64 (C5ORF46 protein product) exhibits cytotoxic effects against human T-cell lymphoma Jurkat and B-cell lymphoma Raji cells. | PMID:33804835 | Biomolecules |
| 2019 | Low | C5ORF46 protein is detectable as a previously uncharacterized small protein (2–10 kDa range) in human plasma, identified by mass spectrometry using a small-protein enrichment assay. | PMID:31308252 | Molecular & Cellular Proteomics |
| 2022 | Low | Knockdown of C5ORF46 in renal cancer cell lines reduced cell proliferation and migration and increased apoptosis in vitro; transcriptomic sequencing after knockdown implicated C5ORF46 in regulation of the malignant phenotype and immune microenvironment. | PMID:35504177 | Translational Oncology |

## Citations

- PMID:31308252
- PMID:33804835
- PMID:35504177
