---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD8
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q96I13
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 3
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABHD8 (human)

## Current model (mechanistic narrative)

ABHD8 is an α/β-hydrolase domain-containing protein that functions as a negative regulator of NLRP3 inflammasome activation by controlling NLRP3 protein turnover [PMID:39225180]. ABHD8 interacts physically with NLRP3 and acts as a scaffold that recruits the palmitoyltransferase ZDHHC12 to NLRP3, promoting NLRP3 palmitoylation and its subsequent degradation through the chaperone-mediated autophagy (CMA) pathway; loss of ABHD8 stabilizes NLRP3 and enhances inflammasome activation, whereas overexpression dampens LPS- and alum-triggered activation in vivo [PMID:39225180]. This regulatory axis is a target of viral subversion, as the SARS-CoV-2 nucleocapsid protein disrupts the ABHD8–NLRP3 association, elevating NLRP3 levels and driving excessive inflammasome activation [PMID:39225180]. ABHD8 expression is itself controlled at the 19p13.1 locus, where risk SNPs physically contact the ABHD8 promoter and risk alleles increase its transactivation [PMID:27601076]. Beyond these findings, the catalytic activity of the α/β-hydrolase domain and its direct enzymatic substrates have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-168256 Immune System
- **partners:** NLRP3, ZDHHC12
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | Medium | ABHD8 interacts with NLRP3 and promotes its degradation through the chaperone-mediated autophagy (CMA) pathway; ABHD8 acts as a scaffold to recruit palmitoyltransferase ZDHHC12 to NLRP3, facilitating NLRP3 palmitoylation and subsequent CMA-mediated degradation. ABHD8 deficiency stabilizes NLRP3 protein and promotes inflammasome activation, while ABHD8 overexpression ameliorates LPS- or alum-triggered NLRP3 inflammasome activation in vivo. | PMID:39225180 | Autophagy |
| 2024 | Medium | The SARS-CoV-2 nucleocapsid (N) protein impairs the ABHD8-NLRP3 association, resulting in elevated NLRP3 protein levels and excessive inflammasome activation, placing ABHD8 as a target disrupted by viral infection. | PMID:39225180 | Autophagy |
| 2016 | Medium | Chromosome conformation capture identified physical interactions between four candidate risk SNPs at 19p13 and the ABHD8 locus; luciferase assays showed that six risk alleles increased transactivation of the ABHD8 promoter, and genotype-gene expression associations were identified for ABHD8 (P<2×10⁻³), indicating that multiple SNPs regulate ABHD8 expression. | PMID:27601076 | Nature Communications |

## Citations

- PMID:27601076
- PMID:39225180
