---
title: "PSEPK ppu00360 Phenylalanine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00360: Phenylalanine metabolism

- Module seed: `phenylalanine_metabolism`
- Candidate genes from membership table: 28
- Primary bucket genes: 13
- Existing review files: 28
- Curated review files: 28
- Existing Asta research files: 28

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
| [x] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | Aldolase/synthase |
| [x] | `tyrB` | PP_1972 | Q88LG1 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `PP_2552` | PP_2552 | Q88JU5 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | DOPA decarboxylase (EC 4.1.1.28) |
| [x] | `PP_2932` | PP_2932 | Q88IR7 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `paaZ` | PP_3270 | Q88HT3 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase (EC 1.2.1.91, EC 3.3.2.12) |
| [x] | `paaE` | PP_3274 | Q88HS9 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Ring 1,2-phenylacetyl-CoA epoxidase, reductase subunit (EC 1.14.13.149) |
| [x] | `paaD` | PP_3275 | Q88HS8 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Subunit of phenylacetate degradation enzyme |
| [x] | `paaC` | PP_3276 | Q88HS7 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Ring 1,2-phenylacetyl-CoA epoxidase beta subunit (EC 1.14.13.149) |
| [x] | `paaB` | PP_3277 | Q88HS6 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Ring 1,2-phenylacetyl-CoA epoxidase regulatory subunit (EC 1.14.13.149) |
| [x] | `paaA` | PP_3278 | Q88HS5 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit (EC 1.14.13.149) |
| [x] | `paaK` | PP_3279 | Q88HS4 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Phenylacetate-coenzyme A ligase (EC 6.2.1.30) (Phenylacetyl-CoA ligase) |
| [x] | `paaI` | PP_3281 | Q88HS2 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Hydroxyphenylacetyl-CoA thioesterase |
| [x] | `paaH` | PP_3282 | Q88HS1 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) |
| [x] | `paaG` | PP_3283 | Q88HS0 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `hpd` | PP_3433 | Q88HC7 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) |
| [x] | `peaE` | PP_3463 | Q88H97 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) |
| [x] | `amaC` | PP_3590 | Q88GX7 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `katG` | PP_3668 | Q88GQ0 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | Catalase-peroxidase (CP) (EC 1.11.1.21) (Peroxidase/catalase) |
| [x] | `PP_3726` | PP_3726 | Q88GJ6 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase/isomerase family protein |
| [x] | `hbd` | PP_3755 | Q88GG9 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) |
| [x] | `PP_4311` | PP_4311 | Q88EY9 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 2 small subunit (EC 1.4.99.6) |
| [x] | `dadA1` | PP_4434 | Q88EM0 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 1 (EC 1.4.99.-) |
| [x] | `phhA` | PP_4490 | Q88EH3 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |
| [x] | `dadA2` | PP_5270 | Q88CB1 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | D-amino acid dehydrogenase 2 (EC 1.4.99.-) |

## Notes

Generated UTC: 2026-07-07T21:29:20.654931+00:00

2026-07-11 PDT status sync: `modules/phenylalanine_metabolism.yaml` is curated and validates with both module validators. All 28 PSEPK review YAMLs in this batch validate with no failures; 26 have only the existing warning that their Asta reports are not cited in annotation-level reviews. The module separates PhhA hydroxylation of L-phenylalanine into the tyrosine/homogentisate route from the Paa phenylacetate degradation operon, while keeping KEGG ppu00360 aminotransferase, D-amino-acid dehydrogenase, catalase-peroxidase, decarboxylase, and generic CoA-enzyme spillovers as boundary context unless gene-level evidence supports a committed phenylalanine-catabolic role.

Real Falcon commands were run:

```bash
just module-deep-research-falcon phenylalanine_metabolism
just module-pathway-deep-research-falcon phenylalanine_metabolism ppu00360 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/phenylalanine_metabolism-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__phenylalanine_metabolism__ppu00360-deep-research-falcon.md`
