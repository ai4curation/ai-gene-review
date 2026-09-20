---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP23
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9P227
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

# Affinage mechanistic annotation for ARHGAP23 (human)

## Current model (mechanistic narrative)

ARHGAP23 is a multidomain RhoGAP-family protein that functions as a cytoplasmic suppressor of RhoA activity at cell-cell junctions [PMID:38970683]. At adherens junctions in keratinocytes, association of plakophilin 4 (PKP4) with ARHGAP23 reduces its binding to RhoA, thereby restraining cytoplasmic RhoA activation and stress fiber formation; this PKP4 scaffolding spatially restricts where ARHGAP23 acts on RhoA [PMID:38970683]. ARHGAP23 is also a component of the core VE-cadherin interactome in endothelial cells, binding VE-cadherin independently of intracellular-domain tyrosine phosphorylation [PMID:42006337]. Beyond these junction-associated roles, the enzymatic GAP activity and domain functions of ARHGAP23 have not been experimentally characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** PKP4, RHOA, CDH5
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | Low | ARHGAP23 (KIAA1501) was identified as a RhoGAP-domain-containing protein with a domain structure consisting of PDZ, Pleckstrin homology (PH), and RhoGAP domains, shared with ARHGAP21 and Xenopus rGAP. Two protein isoforms (1491-aa isoform 1 and 1144-aa isoform 2) arise from alternative splicing involving a 23-bp exon 23 that causes a frameshift and C-terminal truncation in isoform 2. | PMID:15254754 | International journal of oncology |
| 2024 | Medium | ARHGAP23 acts as a Rho suppressor at adherens junctions: association of PKP4 (plakophilin 4) with ARHGAP23 reduced ARHGAP23 binding to RhoA, thereby preventing RhoA activation in the cytoplasm and stress fiber formation. This places ARHGAP23 as a cytoplasmic inhibitor of RhoA activity whose function is spatially regulated by PKP4 scaffolding. | PMID:38970683 | Cellular and molecular life sciences : CMLS |
| 2026 | Low | ARHGAP23 was identified as a component of the core VE-cadherin interactome in endothelial cells, binding VE-cadherin even when its intracellular domain is not tyrosine-phosphorylated, as detected by mass spectrometry-based proteomics. | PMID:42006337 | iScience |

## Citations

- PMID:15254754
- PMID:38970683
- PMID:42006337
