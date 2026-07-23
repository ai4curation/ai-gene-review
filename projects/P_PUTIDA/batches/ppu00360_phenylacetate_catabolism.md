---
title: "PSEPK phenylacetate catabolism"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK phenylacetate catabolism

This batch models the aerobic phenylacetyl-CoA pathway from phenylacetate
activation through oxygen-dependent ring epoxidation and ring opening to the
lower beta-oxidation-like reactions. The reusable module exposes the
multisubunit epoxidase as a complex step and keeps each molecular function on
the relevant leaf annoton.

## Workflow

- [x] Fetch all 11 selected gene records.
- [ ] Run full OpenScientist research for each selected gene.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral `phenylacetate_catabolism` module.
- [x] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00360` + PSEPK research.
- [x] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `paaK` | PP_3279 | Q88HS4 | Phenylacetate activation to phenylacetyl-CoA |
| [x] | `paaA` | PP_3278 | Q88HS5 | Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit |
| [ ] | `paaB` | PP_3277 | Q88HS6 | Epoxidase regulatory subunit |
| [x] | `paaC` | PP_3276 | Q88HS7 | Epoxidase beta subunit |
| [x] | `paaD` | PP_3275 | Q88HS8 | Epoxidase-associated accessory factor |
| [ ] | `paaE` | PP_3274 | Q88HS9 | Epoxidase reductase subunit |
| [ ] | `paaG` | PP_3283 | Q88HS0 | 1,2-epoxyphenylacetyl-CoA isomerase |
| [ ] | `paaZ` | PP_3270 | Q88HT3 | Oxepin-CoA hydrolase and semialdehyde dehydrogenase |
| [ ] | `paaF` | PP_3284 | Q88HR9 | Lower-pathway enoyl-CoA hydratase/isomerase |
| [ ] | `paaH` | PP_3282 | Q88HS1 | 3-hydroxyadipyl-CoA dehydrogenase |
| [ ] | `paaJ` | PP_3280 | Q88HS3 | Lower-pathway thiolase |

## Boundary Decisions

- `paaI` and `paaY` encode pathway-associated thioesterases with
  proofreading/detoxification roles. They are relevant accessories but are not
  required transformations in the linear catabolic route.
- `paaX` is the phenylacetyl-CoA-responsive transcriptional repressor and is
  regulatory context rather than a catabolic reaction.
- `PP_3726` and `hbd` are broad-map enoyl-CoA/dehydrogenase candidates outside
  the contiguous `paa` locus; the locus-encoded `paaF` and `paaH` proteins are
  the supported lower-pathway enzymes.
- Aminotransferases, phenylalanine hydroxylase, Hpd, PeaE, amino-acid
  dehydrogenases, and unrelated aromatic enzymes are upstream routes or KEGG
  map spillover.

The complete 28-gene KEGG source snapshot remains in
`ppu00360_phenylacetate_catabolism.tsv`.
