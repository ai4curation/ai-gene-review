---
title: "PSEPK ppu00350 Tyrosine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00350: Tyrosine metabolism

- Module seed: `tyrosine_catabolism`
- Candidate genes from membership table: 16
- Primary bucket genes: 6
- Existing review files: 16
- Curated review files: 16
- Existing Asta research files: 16

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
| [x] | `davD` | PP_0213 | Q88RC0 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Glutarate-semialdehyde dehydrogenase (EC 1.2.1.-) |
| [x] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `PP_1709` | PP_1709 | Q88M65 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Fumarylacetoacetate hydrolase family protein |
| [x] | `tyrB` | PP_1972 | Q88LG1 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `sad-I` | PP_2488 | Q88K05 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | NAD+-dependent succinate semialdehyde dehydrogenase (EC 1.2.1.24) |
| [x] | `PP_2552` | PP_2552 | Q88JU5 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | DOPA decarboxylase (EC 4.1.1.28) |
| [x] | `hpd` | PP_3433 | Q88HC7 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 4-hydroxyphenylpyruvate dioxygenase (EC 1.13.11.27) |
| [x] | `peaE` | PP_3463 | Q88H97 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) |
| [x] | `amaC` | PP_3590 | Q88GX7 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |
| [x] | `gabD-II` | PP_4422 | Q88EN2 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Succinate-semialdehyde dehydrogenase (NADP+) (EC 1.2.1.79) |
| [x] | `hmgC` | PP_4619 | Q88E49 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Maleylacetoacetate isomerase (EC 5.2.1.2) |
| [x] | `hmgB` | PP_4620 | Q88E48 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | fumarylacetoacetase (EC 3.7.1.2) |
| [x] | `hmgA` | PP_4621 | Q88E47 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5) (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisica |
| [x] | `PP_4983` | PP_4983 | Q88D45 | kegg:ppu00350 | PRESENT | CURATED | PRESENT | Tryptophan 2-monooxygenase (EC 1.13.12.3) |

## Notes

Generated UTC: 2026-07-07T21:05:27.579756+00:00

2026-07-11 PDT status sync: `modules/tyrosine_catabolism.yaml` is curated and validates with both module validators. All 16 PSEPK review YAMLs in this batch validate with no failures; 14 have only the existing warning that their Asta reports are not cited in annotation-level reviews. The module is treated as the species-neutral homogentisate-route scaffold, with PSEPK ppu00350 side nodes kept as boundary context unless gene-level evidence supports a committed tyrosine-catabolic role.

Real Falcon commands were run:

```bash
just module-deep-research-falcon tyrosine_catabolism
just module-pathway-deep-research-falcon tyrosine_catabolism ppu00350 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/tyrosine_catabolism-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__tyrosine_catabolism__ppu00350-deep-research-falcon.md`
