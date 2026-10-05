---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP3S1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q92572
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP3S1 (human)

## Current model (mechanistic narrative)

AP3S1 (CLAPS3) encodes a small clathrin-adaptor chain that functions as a subunit of the AP-3 adaptor complex in intracellular vesicular trafficking, and is expressed ubiquitously across human tissues [PMID:8697810]. Its trafficking role is required for copper homeostasis: partial knockdown in zebrafish sensitized developing melanocytes to hypopigmentation under low-copper conditions, placing AP3S1 in the intracellular trafficking pathway essential for copper loading into cuproproteins [PMID:20713646]. Beyond these established roles, mechanistic detail is limited in the available corpus: AP3S1 has been reported as a host interactor of multiple HPAI H7N9 viral proteins [PMID:38560106] and its knockdown reduces ovarian cancer cell migration and invasion in a manner linked to TGF-β/SMAD signaling [PMID:38609993], but neither the structural basis of cargo recognition nor the biochemical mechanism of these activities has been characterized.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** *(none)*
- **complexes:** AP-3 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1996 | Medium | AP3S1 (CLAPS3) encodes a novel clathrin-adaptor small chain of 193 amino acids (22 kDa) with homology to clathrin-adaptor small chains in rat, mouse, and yeast, and is expressed ubiquitously across human tissues as a 1.35-kb transcript. | PMID:8697810 | Cytogenetics and cell genetics |
| 2010 | Medium | Partial knockdown of Ap3s1 (an intracellular trafficking component, AP-3 complex subunit) in zebrafish sensitized developing melanocytes to hypopigmentation under low-copper conditions, placing AP3S1 in the intracellular trafficking pathway essential for copper loading into cuproproteins. | PMID:20713646 | Disease models & mechanisms |
| 2024 | Low | AP3S1 protein interacts with multiple HPAI H7N9 viral proteins (hemagglutinin, matrix 1, neuraminidase, nucleoprotein, PB1, PB2) as demonstrated by co-immunoprecipitation, identifying AP3S1 as a novel host interactor involved in modulating the viral life cycle. | PMID:38560106 | Heliyon |
| 2024 | Low | AP3S1 knockdown in ovarian cancer cells reduced tumor cell migration and invasion, with mechanistic placement in the TGF-β/SMAD signaling pathway. | PMID:38609993 | European journal of medical research |

## Citations

- PMID:20713646
- PMID:38560106
- PMID:38609993
- PMID:8697810
