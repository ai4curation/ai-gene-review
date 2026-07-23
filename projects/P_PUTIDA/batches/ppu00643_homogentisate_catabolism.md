---
title: "PSEPK homogentisate catabolism"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK homogentisate catabolism

This batch models the conserved lower homogentisate pathway from homogentisate
to fumarate and acetoacetate. The reusable boundary contains three required
reactions: aromatic-ring cleavage, maleylacetoacetate isomerization, and
fumarylacetoacetate hydrolysis.

## Workflow

- [x] Fetch the two gene records not already present.
- [ ] Run full OpenScientist research for all three selected genes.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral `homogentisate_catabolism` module.
- [x] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00643` + PSEPK research.
- [x] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [ ] | `hmgA` | PP_4621 | Q88E47 | Homogentisate 1,2-dioxygenase |
| [ ] | `hmgC` | PP_4619 | Q88E49 | Maleylacetoacetate isomerase |
| [ ] | `hmgB` | PP_4620 | Q88E48 | Fumarylacetoacetase |

## Excluded Candidates

- `peaE` encodes phenylacetaldehyde dehydrogenase and supplies aromatic-acid
  pathways upstream of homogentisate; it is not a lower-pathway step.
- `PP_2932` is an amidase-family protein without a supported role in the
  `hmgABC` reaction sequence.

The complete five-gene KEGG source snapshot remains in
`ppu00643_homogentisate_catabolism.tsv`.
