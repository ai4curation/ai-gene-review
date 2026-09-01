---
title: "PSEPK ppu00946 Degradation of flavonoids batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [bglX, PP_3195, PP_3197, PP_3198, PP_3199, PP_3204, PP_3205, PP_3206]
autolink_gene_symbols: false
---

# PSEPK ppu00946: Degradation of flavonoids

- Module seed: `bacterial_flavonoid_degradation`
- Candidate genes from membership table: 7, plus PP_3199 recovered from the
  contiguous locus and the FdeD/FdeE reaction assignment
- Primary bucket genes: 6
- Existing review files: 8
- Curated review files: 8
- Existing completed OpenScientist research files: 6

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open [PR #2832](https://github.com/ai4curation/ai-gene-review/pull/2832)
  for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | PRESENT | COMPLETE | FAILED (DNS) | Periplasmic GH3 beta-glucosidase; no evidence for membership in the naringenin core |
| [x] | `PP_3195` | PP_3195 | Q88I07 | kegg:ppu00946 | PRESENT | COMPLETE | PRESENT | Predicted FdeB/R13077 carboxylic ester hydrolase; peptidase transfer removed |
| [x] | `PP_3197` | PP_3197 | Q88I05 | kegg:ppu00946 | PRESENT | COMPLETE | PRESENT | Predicted FdeC-like flavonoid A-ring dioxygenase |
| [x] | `PP_3198` | PP_3198 | Q88I04 | kegg:ppu00946 | PRESENT | COMPLETE | FAILED (DNS) | Predicted FdeD Rieske [2Fe-2S] partner; electron-transfer partner remains unknown |
| [x] | `PP_3199` | PP_3199 | Q88I03 | recovered from locus/KO reaction | PRESENT | COMPLETE | PRESENT | Predicted FdeE-like FAD-dependent flavonoid monooxygenase; 40.4% identity to characterized Hsero_1007 |
| [x] | `PP_3204` | PP_3204 | Q88HZ8 | kegg:ppu00946 | PRESENT | COMPLETE | PRESENT | Predicted FdeH cupin component; independent molecular function unresolved |
| [x] | `PP_3205` | PP_3205 | Q88HZ7 | kegg:ppu00946 | PRESENT | COMPLETE | PRESENT | Predicted FdeI carboxy-lyase; second R13079 activity unresolved |
| [x] | `PP_3206` | PP_3206 | Q88HZ6 | kegg:ppu00946 | PRESENT | COMPLETE | PRESENT | FdeJ-like pathway component; molecular function and R13076 chemistry unresolved |

## Notes

- KEGG defines a five-reaction naringenin route: FdeD/FdeE (R13074),
  FdeC/FdeH (R13075), FdeJ (R13076), FdeB (R13077), and FdeI (R13078).
- The organism-specific gene mapping covers PP_3195, PP_3197, PP_3198,
  PP_3204, PP_3205, and PP_3206 directly. PP_3199 is the adjacent
  monooxygenase candidate for the missing FdeE partner and requires explicit
  orthology/experimental review.
- bglX is a possible glycoside-entry enzyme, not part of the five-reaction
  naringenin-aglycone core. It will remain outside the core module unless the
  species-aware report establishes a connected entry branch.
- The bglX, PP_3198, and module/pathway OpenScientist calls ended with DNS
  connection failures after their full runs and produced no research artifacts.
  Their curation uses fetched database records, primary literature, and
  committed reproducible analyses; provider output was not fabricated.
- `modules/bacterial_flavonoid_degradation.yaml` models six ordered reaction
  parts (R13074-R13079), keeps molecular functions on leaf annotons, uses
  UniProt exemplars without unverified PANTHER/PTN claims, and leaves the FdeH
  and R13079 molecular functions unset where the chemistry is unresolved.
- The completed PP_3205 report recovered K26185/FdeI and explicitly called the
  two assigned reactions provisional. Its unsupported localization, regulatory,
  metal, and active-site claims were not promoted to annotations.
- The completed PP_3204 report recovered K26182/FdeH and confirmed the absence
  of direct target or reaction-level experiments. Its speculative metal,
  localization, and catalytic-class claims were not promoted to annotations.
