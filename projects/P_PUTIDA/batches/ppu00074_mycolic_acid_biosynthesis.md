---
title: "PSEPK ppu00074 Mycolic acid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00074: Mycolic acid biosynthesis

- Module seed: `mycolic_acid_biosynthesis`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_1183` | PP_1183 | Q88NM4 | kegg:ppu00074 | PRESENT | CURATED | PRESENT | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) |
| [x] | `fabD` | PP_1913 | Q88LL7 | kegg:ppu00074 | PRESENT | CURATED | PRESENT | Malonyl CoA-acyl carrier protein transacylase (EC 2.3.1.39) |

## Pathway Decision

KEGG `ppu00074` is not satisfiable in *Pseudomonas putida* KT2440 and should be
tracked as a boundary/absence case rather than as a real mycolic-acid
biosynthesis pathway. The two mapped candidates are valid genes in other
contexts: `PP_1183` supports EntD-family 4'-phosphopantetheinyltransferase
activity for siderophore/NRPS carrier-protein activation, and `fabD` supports
malonyl-CoA:ACP transacylase activity for FAS-II fatty-acid biosynthesis.

Falcon reports:

- `modules/mycolic_acid_biosynthesis-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon.md`

The diagnostic mycolate machinery is absent/not expected in this target taxon,
including Pks13, FadD32, CmrA, MmpL3, Ag85/Fbp mycolyltransferases, KasA/KasB,
InhA, MabA, HadABC, and meromycolate-modification enzymes.

Validation commands run:

```bash
just validate PSEPK PP_1183
just validate PSEPK fabD
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/mycolic_acid_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/mycolic_acid_biosynthesis.yaml
```

## Notes

Generated UTC: 2026-07-07T06:21:33.101116+00:00
