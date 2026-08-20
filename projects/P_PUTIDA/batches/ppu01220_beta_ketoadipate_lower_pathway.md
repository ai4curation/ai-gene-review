---
title: "PSEPK ppu01220 beta-ketoadipate lower-pathway batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01220: Beta-ketoadipate lower pathway

- Module seed: `beta_ketoadipate_lower_pathway`
- Focused genes: 3
- Existing review files: 3
- Primary pathway source: KEGG `ppu01220`, refined using `ppu00362` membership

## Required Workflow

- [x] Define a species-neutral module from 3-oxoadipate to central metabolites.
- [x] Keep catechol and protocatechuate upper branches outside this module.
- [x] Resolve exact PSEPK genes, loci, and UniProt exemplars.
- [ ] Complete module-level OpenScientist retrieval.
- [ ] Complete PSEPK module/pathway/taxon OpenScientist retrieval.
- [ ] Complete OpenScientist retrieval for each focused gene.
- [x] Complete focused annotation review for all three genes.
- [x] Validate module and gene reviews.
- [x] Render module, project page, and changed gene reviews.

## Candidate Genes

| Done | Gene | Locus | UniProt | Role | Existing review |
|---|---|---|---|---|---|
| [x] | `pcaI` | PP_3951 | Q88FX5 | PcaIJ CoA-transferase alpha subunit | PRESENT |
| [x] | `pcaJ` | PP_3952 | P0A101 | PcaIJ CoA-transferase beta subunit | PRESENT |
| [x] | `pcaF-I` | PP_1377 | Q88N39 | 3-oxoadipyl-CoA thiolase | PRESENT |

## Boundary And Curation Notes

2026-08-11:

- The module starts at 3-oxoadipate, after catechol- and
  protocatechuate-derived branches converge, and ends at acetyl-CoA plus
  succinyl-CoA.
- PcaI and PcaJ form the heteromeric enzyme for the first reaction. Each
  subunit contributes to the complex molecular function; neither is modeled as
  independently enabling the complete activity.
- PcaF-I catalyzes the second, thiolytic-cleavage reaction.
- Exact PSEPK exemplars and UniProt-recorded NCBIfam assignments are used.
  No broader family identifier is asserted without record-level support.
- OpenScientist module, module/pathway/taxon, and three gene-level retrieval
  jobs were launched after local curation; their long-running completion is not
  required for this first-pass module boundary and annotation review.
