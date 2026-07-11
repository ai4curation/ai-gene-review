---
title: "PSEPK ppu00220 Arginine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00220: Arginine biosynthesis

- Module seed: `arginine_biosynthesis`
- Candidate genes from membership table plus promoted module-gap genes: 32
- Primary bucket genes: 17
- Existing review files: 32
- Curated review files: 32
- Existing Asta research files: 32

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `argH` | PP_0184 | P59618 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) |
| [x] | `aruC` | PP_0372 | Q88QW2 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Acetylornithine aminotransferase 2 (EC 2.6.1.11, EC 2.6.1.13) |
| [x] | `argC1` | PP_0432 | Q88QQ6 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | N-acetyl-gamma-glutamyl-phosphate reductase 1 (AGPR 1) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 1) ( |
| [x] | `gdhA` | PP_0675 | Q88Q23 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate dehydrogenase |
| [x] | `arcC` | PP_0999 | Q88P54 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Carbamate kinase |
| [x] | `arcB` | PP_1000 | Q88P53 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Ornithine carbamoyltransferase, catabolic (OTCase) (EC 2.1.3.3) |
| [x] | `arcA` | PP_1001 | Q88P52 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Arginine deiminase (ADI) (EC 3.5.3.6) (Arginine dihydrolase) (AD) |
| [x] | `argF` | PP_1079 | Q88NX4 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Ornithine carbamoyltransferase (OTCase) (EC 2.1.3.3) |
| [x] | `argG` | PP_1088 | P59604 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase) |
| [x] | `argJ` | PP_1346 | P59612 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Arginine biosynthesis bifunctional protein ArgJ [Cleaved into: Arginine biosynthesis bifunctional protein ArgJ alpha cha |
| [x] | `alaA` | PP_1872 | Q88LQ7 | kegg:ppu00290 | PRESENT | CURATED | PRESENT | Glutamate-pyruvate aminotransferase AlaA (EC 2.6.1.2) |
| [x] | `gdhB` | PP_2080 | Q88L55 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) |
| [x] | `puuA-I` | PP_2178 | Q88KW1 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |
| [x] | `ansB` | PP_2453 | Q88K39 | kegg:ppu00470 | PRESENT | CURATED | PRESENT | Glutaminase-asparaginase (EC 3.5.1.38) (L-ASNase/L-GLNase) (L-asparagine/L-glutamine amidohydrolase) |
| [x] | `ureA` | PP_2843 | Q88J06 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit gamma (EC 3.5.1.5) (Urea amidohydrolase subunit gamma) |
| [x] | `ureB` | PP_2844 | Q88J05 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit beta (EC 3.5.1.5) (Urea amidohydrolase subunit beta) |
| [x] | `ureC` | PP_2845 | Q88J04 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Urease subunit alpha (EC 3.5.1.5) (Urea amidohydrolase subunit alpha) |
| [x] | `PP_3148` | PP_3148 | Q88I53 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `PP_3571` | PP_3571 | Q88GZ4 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Acetylornithine deacetylase |
| [x] | `argC2` | PP_3633 | P59308 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | N-acetyl-gamma-glutamyl-phosphate reductase 2 (AGPR 2) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase 2) ( |
| [x] | `PP_4399` | PP_4399 | Q88EQ4 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `argD` | PP_4481 | P59319 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Acetylornithine aminotransferase (ACOAT) (EC 2.6.1.11) |
| [x] | `PP_4547` | PP_4547 | Q88EB9 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase |
| [x] | `carB` | PP_4723 | Q88DU6 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain) |
| [x] | `carA` | PP_4724 | Q88DU5 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain) |
| [x] | `glnA` | PP_5046 | Q88CY3 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamine synthetase (EC 6.3.1.2) |
| [x] | `spuB` | PP_5183 | Q88CJ7 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `spuI` | PP_5184 | Q88CJ6 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamylpolyamine synthetase |
| [x] | `argA` | PP_5185 | P0A0Z9 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Amino-acid acetyltransferase (EC 2.3.1.1) (N-acetylglutamate synthase) (AGS) (NAGS) |
| [x] | `argE` | PP_5186 | Q88CJ5 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Acetylornithine deacetylase (EC 3.5.1.16) |
| [x] | `argB` | PP_5289 | P59300 | kegg:ppu00220 | PRESENT | CURATED | PRESENT | Acetylglutamate kinase (EC 2.7.2.8) (N-acetyl-L-glutamate 5-phosphotransferase) (NAG kinase) (NAGK) |
| [x] | `puuA-II` | PP_5299 | Q88C84 | kegg:ppu00910 | PRESENT | CURATED | PRESENT | Glutamate-putrescine ligase (EC 6.3.1.11) |

## Notes

Generated UTC: 2026-07-07T15:28:35.398045+00:00

## Workflow Notes

- Created and validated `modules/arginine_biosynthesis.yaml`.
- Added `--extra-gene` support to `projects/P_PUTIDA/extract_pathway_batch.py`
  and used `--extra-gene argD=UniPathway:UPA00068` so the strict
  acetylornithine aminotransferase step is represented.
- Ran `just module-deep-research-falcon arginine_biosynthesis` and
  `just module-pathway-deep-research-falcon arginine_biosynthesis ppu00220
  PSEPK`. Both reached Edison and failed at task creation with HTTP 402 Payment
  Required, so `modules/arginine_biosynthesis-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_biosynthesis__ppu00220-deep-research-falcon.md`
  were not created.
- Asta succeeded for all 32 candidates after one retry for `argC1`, `alaA`, and
  `argE`.
- All 32 candidate gene reviews validate. Remaining warnings are expected
  first-pass Asta context notices.

## Curation Notes

- Strict bacterial L-arginine biosynthesis is represented by CarAB,
  ArgA/ArgJ, ArgB, ArgC1/ArgC2, promoted ArgD, ArgE/PP_3571/ArgJ, ArgF, ArgG,
  and ArgH.
- `argD` is not in the KEGG ppu00220 membership extract but is
  UniPathway-supported for UPA00068 and was promoted as a module-gap gene.
- `arcA`, `arcB`, and `arcC` are the arginine deiminase/carbamate side branch,
  not strict arginine biosynthesis. `arcB` now has a `NEW` L-arginine catabolic
  process suggestion and its electronic L-arginine biosynthetic process transfer
  is removed.
- `ureA`, `ureB`, and `ureC` are urease/urea-catabolism side nodes; the
  glutamate/glutamine/polyamine genes are retained as precursor or boundary
  context rather than committed ppu00220 steps.
