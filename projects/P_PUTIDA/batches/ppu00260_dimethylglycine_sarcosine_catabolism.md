---
title: "PSEPK dimethylglycine and sarcosine catabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00260: dimethylglycine and sarcosine catabolism

- Module seed: `bacterial_dimethylglycine_sarcosine_catabolism`
- Selected genes: 8
- New gene reviews: `dgcA`, `dgcB`, `PP_0312`, `PP_0313`, `soxA`, `soxB`, `soxD`, `soxG`

## Curated Boundary

- DgcAB converts dimethylglycine to sarcosine and passes reducing equivalents
  through the pathway-associated PP_0312/PP_0313 ETF heterodimer. The terminal
  respiratory-chain acceptor is left unresolved.
- SoxABDG converts sarcosine to glycine, coupled to tetrahydrofolate and oxygen.
- Upstream glycine-betaine conversion and downstream glycine utilization are
  represented by separate modules.

## Required Workflow

- [x] Define a reusable multi-part module with architectural alternatives.
- [x] Fetch selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Start OpenScientist research for every selected gene.
- [x] Complete module-level OpenScientist research.
- [x] Complete module + pathway + PSEPK OpenScientist research.
- [x] Curate all selected gene reviews.
- [x] Consult the annotation reviewer.
- [x] Validate and render module and gene reviews.
- [ ] Open one draft PR for this module.

## Selected Genes

| Done | Gene | Locus | UniProt | Role | Research |
|---|---|---|---|---|---|
| [x] | `dgcA` | PP_0310 | Q88R24 | flavin subunit of DgcAB | no artifact returned |
| [x] | `dgcB` | PP_0311 | Q88R23 | membrane iron-sulfur subunit of DgcAB | no artifact returned |
| [x] | `PP_0312` | PP_0312 | Q88R22 | pathway-associated ETF alpha subunit | no artifact returned |
| [x] | `PP_0313` | PP_0313 | Q88R21 | pathway-associated ETF beta subunit | no artifact returned |
| [x] | `soxB` | PP_0323 | Q88R11 | SoxABDG beta subunit | no artifact returned |
| [x] | `soxD` | PP_0324 | Q88R10 | SoxABDG delta subunit | no artifact returned |
| [x] | `soxA` | PP_0325 | Q88R09 | SoxABDG alpha subunit | complete |
| [x] | `soxG` | PP_0326 | Q88R08 | SoxABDG gamma subunit | no artifact returned |

## Notes

2026-08-13: Corrected the electron-transfer architecture using the characterized
Chromohalobacter system: DgcB is the internal ferredoxin subunit and the adjacent
ETF heterodimer is the next acceptor. The terminal respiratory-chain acceptor
remains outside the boundary. The module includes reviewed single-chain
dimethylglycine dehydrogenase and monomeric sarcosine oxidase alternatives.

The generic module and module + pathway + PSEPK OpenScientist reports completed.
All eight gene jobs were launched, but only the `soxA` job returned an artifact;
the other provider runs exited without files. Gene curation therefore uses the
completed module-level synthesis, primary literature, UniProt/GOA evidence, and
the independent annotation-review pass without claiming missing gene reports.
