---
title: "PSEPK ppu02040 Flagellar assembly batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02040: Flagellar assembly

- Module seed: `bacterial_flagellar_assembly_boundary`
- Candidate genes from membership table: 47
- Primary bucket genes: 47
- Existing review files: 47
- Curated review files: 47
- Existing Asta research files: 47

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
| [x] | `fliY` | PP_0227 | Q88RA6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Periplasmic cystine-binding protein |
| [x] | `rpoD` | PP_0387 | Q88QU7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | RNA polymerase sigma factor RpoD (Sigma-70) |
| [x] | `rpoN` | PP_0952 | P0A171 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | RNA polymerase sigma-54 factor |
| [x] | `PP_1087` | PP_1087 | Q88NW6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Outer membrane protein, OmpA family |
| [x] | `PP_4335` | PP_4335 | Q88EW7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor protein |
| [x] | `PP_4336` | PP_4336 | Q88EW6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor rotation protein |
| [x] | `fliA` | PP_4341 | Q88EW1 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | RNA polymerase sigma factor FliA (RNA polymerase sigma factor for flagellar operon) (Sigma F) (Sigma-28) |
| [x] | `flhA` | PP_4344 | Q88EV8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthesis protein FlhA |
| [x] | `flhB` | PP_4352 | Q88EV1 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthetic protein FlhB |
| [x] | `fliR` | PP_4353 | Q88EV0 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthetic protein FliR |
| [x] | `fliQ` | PP_4354 | Q88EU9 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthetic protein FliQ |
| [x] | `fliP` | PP_4355 | Q88EU8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthetic protein FliP |
| [x] | `fliO` | PP_4356 | Q88EU7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar protein |
| [x] | `fliN` | PP_4357 | Q88EU6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor switch protein FliN |
| [x] | `fliM` | PP_4358 | Q88EU5 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor switch protein FliM |
| [x] | `fliL` | PP_4359 | Q88EU4 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar protein FliL |
| [x] | `fliK` | PP_4361 | Q88EU2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook-length control protein FliK |
| [x] | `fliJ` | PP_4365 | Q88ET8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar FliJ protein |
| [x] | `fliI` | PP_4366 | Q88ET7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellum-specific ATP synthase (EC 7.1.2.2) |
| [x] | `fliH` | PP_4367 | Q88ET6 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar assembly protein FliH |
| [x] | `fliG` | PP_4368 | Q88ET5 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor switch protein FliG |
| [x] | `fliF` | PP_4369 | Q88ET4 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar M-ring protein |
| [x] | `fliE` | PP_4370 | Q88ET3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook-basal body complex protein FliE |
| [x] | `atoC` | PP_4371 | Q88ET2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Two component system AtoC DNA-binding transcriptional activator |
| [x] | `fleQ` | PP_4373 | Q88ET0 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Transcriptional regulator FleQ |
| [x] | `fliT` | PP_4374 | Q88ES9 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar protein FliT |
| [x] | `fliS` | PP_4375 | Q88ES8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar secretion chaperone FliS |
| [x] | `fliD` | PP_4376 | Q88ES7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook-associated protein 2 (HAP2) (Flagellar cap protein) |
| [x] | `fliC` | PP_4378 | Q88ES5 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellin |
| [x] | `flgL` | PP_4380 | Q88ES3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook-associated protein FlgL |
| [x] | `flgK` | PP_4381 | Q88ES2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook-associated protein 1 |
| [x] | `flgJ` | PP_4382 | Q88ES1 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Peptidoglycan hydrolase FlgJ (Muramidase FlgJ) |
| [x] | `flgI` | PP_4383 | Q88ES0 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar P-ring protein (Basal body P-ring protein) |
| [x] | `flgH` | PP_4384 | Q88ER9 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar L-ring protein (Basal body L-ring protein) |
| [x] | `flgG` | PP_4385 | Q88ER8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar basal-body rod protein FlgG (Distal rod protein) |
| [x] | `flgF` | PP_4386 | Q88ER7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar basal-body rod protein FlgF |
| [x] | `flgE` | PP_4388 | Q88ER5 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar hook protein FlgE |
| [x] | `flgD` | PP_4389 | Q88ER4 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Basal-body rod modification protein FlgD |
| [x] | `flgC` | PP_4390 | Q88ER3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar basal-body rod protein FlgC |
| [x] | `flgB` | PP_4391 | Q88ER2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar basal body rod protein FlgB |
| [x] | `flgA` | PP_4394 | Q88EQ9 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagella basal body P-ring formation protein FlgA |
| [x] | `flgM` | PP_4395 | Q88EQ8 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Negative regulator of flagellin synthesis (Anti-sigma-28 factor) |
| [x] | `PP_4396` | PP_4396 | Q88EQ7 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar biosynthesis protein FlgN |
| [x] | `motB` | PP_4904 | Q88DC3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor rotation protein |
| [x] | `motA` | PP_4905 | Q88DC2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar motor rotation protein |
| [x] | `PP_5157` | PP_5157 | Q88CM3 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Solute-binding protein family 3/N-terminal domain-containing protein |
| [x] | `PP_5209` | PP_5209 | Q88CH2 | kegg:ppu02040 | PRESENT | CURATED | PRESENT | Flagellar protein FliL |

## Notes

Generated UTC: 2026-07-09T15:28:28.458185+00:00

2026-07-11 PDT status sync: created and validated
`modules/bacterial_flagellar_assembly_boundary.yaml` as an umbrella/index module
over the completed ppu02040 sub-batches: flagellar regulation, flagellar
export/assembly, basal-body/hook/filament structure, motor/switch/stator, and
nonflagellar transport/envelope spillovers. The parent batch TSV shows 47/47
review files present, 47/47 curated review YAMLs, and 47/47 Asta reports. Module
validation passed with `linkml-validate -C ModuleReview` and the module term-label
validator. Gene review validation passed for all 47 batch review files with `uv
run ai-gene-review validate --verbose --terms --tsv-output
reports/validation-psepk-ppu02040.tsv <47 files from the batch TSV>`. The TSV
contains 23 non-blocking warnings, mostly best-practice warnings that
core-function process, molecular-function, location, or complex terms are not
mirrored in `existing_annotations`, plus seven warnings that available Asta/Falcon
deep-research files are not referenced in annotation reviews.

Falcon status: ran the real module-level command
`just module-deep-research-falcon bacterial_flagellar_assembly_boundary`; it
reached Edison and failed with HTTP 402 Payment Required, so
`modules/bacterial_flagellar_assembly_boundary-deep-research-falcon.md` was not
created. Also ran the real module + pathway + taxon command
`just module-pathway-deep-research-falcon bacterial_flagellar_assembly_boundary ppu02040 PSEPK`;
it reached Edison and failed with the same HTTP 402 Payment Required response, so
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_flagellar_assembly_boundary__ppu02040-deep-research-falcon.md`
was not created. The Falcon workflow boxes remain unchecked.
