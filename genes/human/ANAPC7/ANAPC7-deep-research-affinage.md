---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC7
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9UJX3
self_evaluation_pairwise: loss
faith_pct: 100.0
n_discoveries: 4
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANAPC7 (human)

## Current model (mechanistic narrative)

ANAPC7 functions as a component of the mitotic machinery, where genetic epistasis places it within the KIF18A-dependent pathway governing mitotic progression: co-depletion of ANAPC7 partially rescues the mitotic arrest caused by KIF18A loss, in direct opposition to ANAPC5, which exacerbates that arrest [PMID:39677807, PMID:40596695]. Beyond this mitotic role, ANAPC7 has been captured in physical-interaction contexts that have not been resolved into a defined mechanism—it binds the cytoplasmic tails of IL-17RA and IL-17RC in a yeast two-hybrid screen, but its knockdown produces no detectable effect on IL-17 signaling [PMID:23922952]. No catalytic activity, structural model, or substrate has been characterized for ANAPC7 in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle
- **partners:** IL17RA, IL17RC, ANAPC5, CD274
- **complexes:** APC/C

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | ANAPC7 (APC7/AnapC7) was identified as a binding partner of both IL-17RA and IL-17RC cytoplasmic tails via yeast 2-hybrid screen. However, siRNA-mediated knockdown of AnapC7 exerted no detectable impact on IL-17 signaling. AnapC5, which associates with AnapC7, also bound IL-17RA and IL-17RC and functioned as a negative regulator of IL-17 signaling, and also associated with A20 (TNFAIP3). | PMID:23922952 | PloS one |
| 2024 | Medium | Genetic epistasis in mouse models and cell lines showed that co-depletion of ANAPC7 partially rescued KIF18A-depletion-induced mitotic arrest, while co-depletion of ANAPC5 exacerbated it. This establishes ANAPC7 as a functional component downstream or in opposition to KIF18A in mitotic progression, with ANAPC5 and ANAPC7 acting in opposing directions in the KIF18A-dependent mitotic pathway. A novel retroviral insertion in Anapc7 was identified that may influence its expression level and sensitivity to KIF18A loss. | PMID:39677807, PMID:40596695 | Scientific reports / bioRxiv |
| 2024 | Low | C-FOS (AP-1 subunit) was shown by ChIP-seq to bind to the promoter of ANAPC7 and regulate its expression during mitotic clonal expansion in early adipogenesis of mesenchymal stem cells. | PMID:38440920 | Journal of cellular biochemistry |
| 2023 | Low | ANAPC7 was experimentally verified as a PD-L1 interactor by co-immunoprecipitation in gastric cancer cells, and ANAPC7 expression was associated with immune escape when NK-92 cells were co-cultured with gastric cancer cells. | PMID:36592213 | Journal of cancer research and clinical oncology |

## Citations

- PMID:23922952
- PMID:36592213
- PMID:38440920
- PMID:39677807
- PMID:40596695
