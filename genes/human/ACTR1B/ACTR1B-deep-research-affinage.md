---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTR1B
affinage_run_date: 2026-06-14T20:58:57+00:00
uniprot_accession: P42025
self_evaluation_pairwise: win
faith_pct: 
n_discoveries: 3
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTR1B (human)

## Current model (mechanistic narrative)

ACTR1B (beta-centractin) is an actin-related protein that functions as a stoichiometric minor subunit of the cytosolic 20S dynactin complex [PMID:7696711]. It partitions predominantly to the cytosolic fraction with no detectable free pool, residing within dynactin at a fixed ratio of approximately 1:15 relative to alpha-centractin, which establishes its identity as a constitutive structural component of this complex rather than an independently acting protein [PMID:7696711]. Beyond its membership in dynactin, ACTR1B abundance is modulated in a cell-type-specific manner: it is differentially altered in human platelets upon glycoprotein VI activation [PMID:20107233] and down-regulated in dendritic cells pulsed with high-metastatic-potential hepatocellular carcinoma lysates, where its reduction tracks with diminished CD86 expression and impaired allostimulatory capacity [PMID:17619203, PMID:17925177]. No direct functional dissection of ACTR1B's role within dynactin or in these cellular contexts has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** *(none)*
- **partners:** ACTR1A
- **complexes:** dynactin (20S)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1994 | High | Beta-centractin (ACTR1B) is an actin-related protein that localizes predominantly to the cytosolic fraction as a component of the 20S dynactin complex, with no evidence for a free pool; it exists in a constant ratio of approximately 1:15 (beta:alpha) relative to alpha-centractin within the dynactin complex. | PMID:7696711 | Molecular biology of the cell |
| 2010 | Low | Beta-centractin (ACTR1B) protein abundance is differentially altered in human platelets upon specific activation of glycoprotein VI (GPVI), indicating that GPVI signaling modulates beta-centractin levels and cytoskeletal organization in platelets. | PMID:20107233 | Blood |
| 2007 | Low | Down-regulation of beta-centractin in dendritic cells pulsed with high-metastatic-potential HCC cell lysates is associated with reduced CD86 expression and impaired allostimulatory capacity (mixed lymphocyte reaction), suggesting beta-centractin supports normal DC function. | PMID:17619203, PMID:17925177 | Journal of cancer research and clinical oncology |

## Citations

- PMID:17619203
- PMID:17925177
- PMID:20107233
- PMID:7696711
