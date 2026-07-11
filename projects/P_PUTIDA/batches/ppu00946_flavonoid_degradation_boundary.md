---
title: "PSEPK ppu00946 Degradation of flavonoids batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00946: Degradation of flavonoids

- Module seed: `flavonoid_degradation_boundary`
- Candidate genes from membership table: 7
- Primary bucket genes: 6
- Existing review files: 7
- Curated review files: 7
- Existing Asta research files: 7

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [x] | `PP_3195` | PP_3195 | Q88I07 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Peptidase S9 prolyl oligopeptidase catalytic domain-containing protein |
| [x] | `PP_3197` | PP_3197 | Q88I05 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Glyoxalase family protein |
| [x] | `PP_3198` | PP_3198 | Q88I04 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Ferredoxin, 2Fe-2S |
| [x] | `PP_3204` | PP_3204 | Q88HZ8 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Cupin type-2 domain-containing protein |
| [x] | `PP_3205` | PP_3205 | Q88HZ7 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | Fumarylacetoacetate hydrolase family protein |
| [x] | `PP_3206` | PP_3206 | Q88HZ6 | kegg:ppu00946 | PRESENT | CURATED | PRESENT | NAD-dependent epimerase/dehydratase domain-containing protein |

## Notes

Generated UTC: 2026-07-08T17:13:31.357546+00:00

2026-07-11 PDT status sync: `modules/flavonoid_degradation_boundary.yaml` is curated and validates with both module validators. The module keeps ppu00946 as an uncertain aromatic-compound boundary: `bglX` is treated as a broad periplasmic beta-glucosidase side node, and the PP_3195-PP_3206 cluster is retained as unresolved hydrolase/redox/cupin/dehydratase-family chemistry rather than a satisfiable flavonoid-degradation route.

Gene validation passed for all seven batch members (`bglX`, `PP_3195`, `PP_3197`, `PP_3198`, `PP_3204`, `PP_3205`, `PP_3206`). `PP_3195`, `PP_3198`, and `PP_3205` have non-blocking warnings that their existing annotation reviews do not cite the available Asta report.

Real Falcon commands were run:

```bash
just module-deep-research-falcon flavonoid_degradation_boundary
just module-pathway-deep-research-falcon flavonoid_degradation_boundary ppu00946 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/flavonoid_degradation_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__flavonoid_degradation_boundary__ppu00946-deep-research-falcon.md`
