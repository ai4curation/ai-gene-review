---
title: "PSEPK methylcitrate-cycle propionate assimilation"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK methylcitrate-cycle propionate assimilation

This batch narrows the broad KEGG `ppu00640` candidate pool to the
2-methylcitrate route that converts propionate-derived propionyl-CoA to
succinate and pyruvate. The reusable module boundary includes four substantive
roles: propionate activation, 2-methylcitrate formation, conversion to
2-methylisocitrate, and carbon-carbon cleavage. It will represent alternative
dehydration/isomerization implementations without treating every KEGG
propanoate-metabolism hit as a module member.

## Workflow

- [x] Fetch the five gene records not already present.
- [ ] Run full OpenScientist research for each selected gene.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral `methylcitrate_cycle` module.
- [ ] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00640` + PSEPK research.
- [x] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `prpE` | PP_2351 | Q88KD9 | Propionate activation to propionyl-CoA |
| [x] | `prpC` | PP_2335 | Q88KF5 | 2-methylcitrate synthase; existing OpenScientist review |
| [x] | `acnA-II` | PP_2336 | Q88KF4 | Cluster-associated aconitase-family pathway candidate |
| [x] | `prpD` | PP_2338 | Q88KF2 | 2-methylcitrate dehydratase |
| [ ] | `prpF` | PP_2337 | Q88KF3 | Methylaconitate isomerase |
| [x] | `acnB` | PP_2339 | Q88KF1 | Bifunctional aconitase/2-methylisocitrate dehydratase; existing OpenScientist review |
| [x] | `prpB` | PP_2334 | Q88KF6 | 2-methylisocitrate lyase producing succinate and pyruvate |

The `acnA-II`/`prpD`/`prpF`/`acnB` cluster is retained for gene-level
adjudication because the pathway may use more than one route between
2-methylcitrate and 2-methylisocitrate. Module membership will follow the
combined biochemical, genomic, and KT2440 fitness evidence rather than gene
proximity alone.

## Excluded Candidate Groups

The remaining 26 KEGG `ppu00640` hits are outside this module boundary:

- Acetyl-CoA carboxylase subunits `accA`, `accB`, `accC`, and `accD` belong to
  fatty-acid synthesis.
- `fadB`, `PP_2213`, `acd`, `PP_2217`, and `paaF` belong to separate acyl-CoA
  activation, fatty-acid, sulfur, or phenylacetate pathways.
- `aceA` belongs to the glyoxylate shunt; `sucC` and `sucD` belong to the TCA
  cycle.
- `PP_0596`, `mmsA-I`, `mmsA-II`, `pta`, `yqhD`, the branched-chain
  dehydrogenase subunits, the lipoamide dehydrogenases, and the acetyl-CoA
  synthetases are broad-map spillover or pathway-boundary metabolism.

The complete 33-gene source snapshot remains in
`ppu00640_methylcitrate_cycle.tsv`.
