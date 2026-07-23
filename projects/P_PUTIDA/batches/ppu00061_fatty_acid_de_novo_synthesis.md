---
title: "PSEPK type-II fatty-acid synthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK type-II fatty-acid synthesis

This batch models the dissociated bacterial type-II fatty-acid synthase from
malonyl-CoA formation and ACP loading through chain initiation, iterative
elongation, and the cis-unsaturated branch. It is separate from the existing
type-I, mammalian `fatty_acid_de_novo_synthesis` module.

## Workflow

- [x] Fetch the 17 gene records not already present.
- [ ] Run full OpenScientist research for all 18 selected genes.
- [x] Curate all selected gene reviews, including every GOA row.
- [x] Create and validate the species-neutral
  `type_ii_fatty_acid_synthesis` module.
- [x] Run full OpenScientist module research.
- [x] Run full OpenScientist module + `ppu00061` + PSEPK research.
- [x] Render the module and project page.
- [ ] Open one non-draft PR and clear review and CI.

## Selected Genes

| Done | Gene | Locus | UniProt | Pathway role |
|---|---|---|---|---|
| [x] | `accC` | PP_0558 | Q88QD6 | Acetyl-CoA carboxylase biotin carboxylase |
| [ ] | `accB` | PP_0559 | Q88QD5 | Acetyl-CoA carboxylase biotin carrier |
| [x] | `accA` | PP_1607 | Q88MG4 | Acetyl-CoA carboxylase carboxyltransferase alpha |
| [ ] | `accD` | PP_1996 | Q88LD9 | Acetyl-CoA carboxylase carboxyltransferase beta |
| [x] | `fabD` | PP_1913 | Q88LL7 | Malonyl-CoA:ACP transacylase |
| [ ] | `acpP` | PP_1915 | Q88LL5 | Acyl carrier protein |
| [ ] | `PP_4379` | PP_4379 | Q88ES4 | FabH1 short-chain-acyl-CoA initiation |
| [x] | `PP_4545` | PP_4545 | Q88EC1 | FabH2 medium-chain-acyl-CoA initiation |
| [x] | `PP_0262` | PP_0262 | Q88R72 | MadB malonyl-ACP decarboxylase initiation |
| [x] | `fabB` | PP_4175 | Q88FC3 | KAS I condensation and unsaturated branch |
| [ ] | `fabF` | PP_1916 | Q88LL4 | KAS II elongation |
| [x] | `PP_3303` | PP_3303 | Q88HQ0 | Second KAS II candidate |
| [x] | `fabG` | PP_1914 | Q88LL6 | 3-oxoacyl-ACP reduction |
| [ ] | `PP_0581` | PP_0581 | Q88QB3 | Additional 3-oxoacyl-ACP reductase candidate |
| [ ] | `fabA` | PP_4174 | Q88FC4 | Dehydration/isomerization for cis-unsaturated synthesis |
| [ ] | `fabZ` | PP_1602 | Q88MG9 | 3-hydroxyacyl-ACP dehydratase candidate |
| [ ] | `fabV` | PP_4635 | Q88E33 | NADH-dependent enoyl-ACP reductase |
| [ ] | `PP_1852` | PP_1852 | Q88LS6 | NADPH-dependent enoyl-ACP reductase candidate |

## Boundary Decisions

- The four `acc` subunits are one required acetyl-CoA carboxylase complex
  activity; molecular functions will be attached to the complex subunits, not
  to the process module.
- Direct KT2440 genetics and biochemistry expand the KEGG-derived batch with
  `PP_4545` (FabH2) and `PP_0262` (MadB). Initiation is satisfied by
  short-chain-acyl-CoA-selective FabH1 (`PP_4379`),
  medium-chain-acyl-CoA-selective FabH2, or MadB-dependent acetyl-ACP
  formation.
- `PP_0581`, `PP_1852`, and the second KAS-II `PP_3303` remain gene-level
  candidates rather than distinct core module variants because a separate
  physiological pathway role is not established.
- `PP_2540` is a generic SDR protein and `PP_2783` is an aromatic-diol
  dehydrogenase; neither has a supported core FAS-II role.
- `fadD-I` and `fadD-II` activate free fatty acids for downstream metabolism
  and are outside de novo ACP-based synthesis.

The complete 19-gene KEGG source snapshot remains in
`ppu00061_fatty_acid_de_novo_synthesis.tsv`; the two evidence-driven initiation
genes added above are documented separately from that immutable source
snapshot.
