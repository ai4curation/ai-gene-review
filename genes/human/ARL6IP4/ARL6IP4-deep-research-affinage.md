---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL6IP4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q66PJ3
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

# Affinage mechanistic annotation for ARL6IP4 (human)

## Current model (mechanistic narrative)

ARL6IP4 (SR-25/SRrp37) is a nuclear serine-arginine-related protein that participates in pre-mRNA alternative splicing [PMID:19582790]. It localizes to nucleoli and nuclear speckles, physically interacts with the splicing factor SC35/SRSF2, and modulates alternative 5' and 3' splice-site selection in minigene reporter assays in vivo [PMID:19582790]. ARL6IP4 also physically associates with cyclophilin A (CypA) through the CypA peptidyl-prolyl isomerase domain, and CypA overexpression induces ARL6IP4 expression [PMID:28105234]. Beyond these interactions and its splicing-modulatory activity, the protein's precise catalytic or structural role within the spliceosome has not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding
- **localization:** GO:0005730 nucleolus, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA
- **partners:** SRSF2, PPIA
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | Medium | SRrp37 (ARL6IP4) localizes to nucleoli and nuclear speckles, physically interacts with SC35 (SRSF2) via GST pull-down, and modulates alternative 5' and 3' pre-mRNA splicing in vivo using adenovirus E1A and chimeric calcitonin/dhfr minigene reporters. | PMID:19582790 | Journal of cellular biochemistry |
| 2000 | Low | SR-25 (ARL6IP4) contains a serine-arginine repeat, a serine cluster, and a highly basic cluster with nuclear localization signals; Northern blot showed ubiquitous mRNA expression with relative abundance in testis and thymus, consistent with a nuclear RNA-splicing protein. | PMID:10708573 | Biochemical and biophysical research communications |
| 2016 | Medium | CypA (cyclophilin A) physically associates with SR-25 (ARL6IP4) through its peptidyl-prolyl isomerase (PPIase) domain, as confirmed by yeast two-hybrid screening, binding assays, and co-immunoprecipitation; CypA overexpression induces SR-25 expression in Hep3B cells. | PMID:28105234 | Oncology letters |
| 2007 | Low | SR-25 (ARL6IP4) protein was identified by peptide mass fingerprinting specifically in dominant-negative Rac1N17 melanoma cells, implicating SR-25 as a component of Rac1 signaling pathways that modulate apoptosis sensitivity to paclitaxel. | PMID:17952876 | Proteomics |

## Citations

- PMID:10708573
- PMID:17952876
- PMID:19582790
- PMID:28105234
