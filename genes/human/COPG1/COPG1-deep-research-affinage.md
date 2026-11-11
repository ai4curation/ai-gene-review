---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/COPG1
affinage_run_date: 2026-06-13T19:06:35
uniprot_accession: Q9Y678
self_evaluation_pairwise: win
faith_pct: 
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

# Affinage mechanistic annotation for COPG1 (human)

## Current model (mechanistic narrative)

COPG1 is a subunit of the COPI coatomer complex that supports Golgi-dependent vesicular trafficking and the integrity of the early secretory pathway [PMID:bio_10.1101_2025.08.21.25332476, PMID:bio_10.1101_2024.10.12.618008]. In hepatocytes, COPG1 is required for HDL holoparticle uptake, selective HDL lipid uptake, and apoA-I secretion; its depletion lowers cell-surface abundance of the scavenger receptor SR-BI (via interference with SR-BI glycosylation) and reduces APOA1 expression, while raising surface ABCA1 and ABCA1-mediated cholesterol efflux [PMID:bio_10.1101_2025.08.21.25332476]. The same COPI trafficking machinery is exploited for efficient secretion of the flaviviral non-structural protein NS1, since COPG1 knockdown reduces NS1 secretion from dengue- and West Nile virus-infected cells without affecting infectious virus egress [PMID:bio_10.1101_2024.10.12.618008]. In hepatocellular carcinoma cells, loss of COPG1 disrupts Golgi morphology and triggers ER stress, elevates reactive oxygen species, and suppresses PI3K-AKT signaling, impairing malignant phenotypes and sensitizing cells to sorafenib and doxorubicin [PMID:41751842]. Beyond these trafficking and cancer-cell phenotypes, no further molecular detail of COPG1 has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** *(none)*
- **complexes:** COPI coatomer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2026 | Medium | COPG1 knockdown in hepatocellular carcinoma cells impaired malignant phenotypes and reduced tumorigenicity in vivo. Mechanistically, COPG1 depletion induced Golgi disruption and ER stress, increased reactive oxygen species (ROS) production, and suppressed PI3K-AKT signaling, thereby sensitizing cells to sorafenib and doxorubicin. | PMID:41751842 | International journal of molecular sciences |
| 2025 | Medium | COPG1 (as part of the COPI coatomer complex) is required in hepatocytes for HDL holoparticle uptake, selective HDL lipid uptake, and apoA-I secretion. Knockdown of COPG1 decreased cell-surface abundance of scavenger receptor SR-BI (likely via interference with SR-BI glycosylation) and decreased APOA1 expression, while increasing cell-surface ABCA1 abundance and ABCA1-mediated cholesterol efflux. | PMID:bio_10.1101_2025.08.21.25332476 | bioRxiv |
| 2024 | Medium | COPG1 (a COPI coatomer subunit) is required for efficient secretion of dengue virus non-structural protein 1 (NS1) from infected cells. siRNA knockdown of COPG1 in DENV-infected cells reduced NS1 secretion without affecting infectious virus egress. Similar effects were observed with West Nile virus, indicating a conserved role for COPI machinery in NS1 secretion across orthoflaviviruses. | PMID:bio_10.1101_2024.10.12.618008 | bioRxiv |

## Citations

- PMID:41751842
- PMID:bio_10.1101_2024.10.12.618008
- PMID:bio_10.1101_2025.08.21.25332476
