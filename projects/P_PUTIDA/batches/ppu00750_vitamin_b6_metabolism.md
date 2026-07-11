---
title: "PSEPK ppu00750 Vitamin B6 metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00750: Vitamin B6 metabolism

- Module seed: `vitamin_b6_metabolism`
- Candidate genes from membership table: 9
- Primary bucket genes: 9
- Existing review files: 9
- Curated review files: 9
- Existing Asta research files: 9

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
| [x] | `pdxA` | PP_0402 | Q88QT5 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | 4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase) |
| [x] | `PP_0662` | PP_0662 | Q88Q36 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Threonine synthase |
| [x] | `pdxH` | PP_1129 | Q88NS5 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Pyridoxine/pyridoxamine 5'-phosphate oxidase (EC 1.4.3.5) (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5'-phosphate synthase) |
| [x] | `pdxJ` | PP_1436 | Q88MY2 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Pyridoxine 5'-phosphate synthase (PNP synthase) (EC 2.6.99.2) |
| [x] | `thrC` | PP_1471 | Q88MU7 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Threonine synthase (EC 4.2.3.1) |
| [x] | `serC` | PP_1768 | Q88M07 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Phosphoserine aminotransferase (EC 2.6.1.52) (Phosphohydroxythreonine aminotransferase) (PSAT) |
| [x] | `pdxB` | PP_2117 | Q88L20 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290) |
| [x] | `epd` | PP_4964 | Q88D63 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Erythrose-4-phosphate dehydrogenase (EC 1.2.1.72) |
| [x] | `pdxY` | PP_5357 | Q88C26 | kegg:ppu00750 | PRESENT | CURATED | PRESENT | Pyridoxal kinase PdxY (PL kinase) (EC 2.7.1.35) |

## Notes

Generated UTC: 2026-07-07T10:53:03.330712+00:00

Curator update: 2026-07-07 PDT / 2026-07-07 UTC.

- 9 KEGG `ppu00750` membership candidates are fetched, Asta-backed, curated,
  validated, and rendered where changed.
- Species-neutral module created and validated:
  `modules/vitamin_b6_metabolism.yaml`.
- Falcon generic module report complete:
  `modules/vitamin_b6_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway report complete:
  `projects/P_PUTIDA/deep-research/PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon.md`.
- Strict de novo PLP formation is satisfiable in KT2440 through `epd`, `pdxB`,
  `serC`, `pdxA`, `pdxJ`, and `pdxH`.
- `pdxY` covers pyridoxal salvage phosphorylation; no obvious broader PdxK-like
  B6 kinase candidate was found in the local first-pass metadata.
- `thrC` and `PP_0662` are retained as threonine synthase/PLP-enzyme boundary
  context, not committed B6 biosynthetic steps.
- `dxs` supplies the DXP precursor but is shared with thiamine and MEP
  metabolism, so it is tracked as pathway-boundary context rather than a
  dedicated vitamin B6 module member.
- Validation commands run:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/vitamin_b6_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/vitamin_b6_metabolism.yaml
for g in pdxA PP_0662 pdxH pdxJ thrC serC pdxB epd pdxY; do just validate PSEPK "$g"; done
```
