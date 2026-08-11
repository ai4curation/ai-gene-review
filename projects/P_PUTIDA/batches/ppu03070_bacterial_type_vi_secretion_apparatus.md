---
title: "PSEPK K1 type VI secretion apparatus"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [PP_3088, PP_3089, PP_3090, PP_5561, PP_3091, PP_3092, PP_3093, PP_3094, clpV, PP_3096, PP_3097, PP_3098, puuD, PP_3100, PP_5562, PP_3106]
autolink_gene_symbols: false
---

# PSEPK K1 type VI secretion apparatus

This batch extracts the conserved type VI structural apparatus from the broad
`ppu03070` secretion-system bucket and grounds it in the experimentally mapped
KT2440 K1-T6SS locus. The reusable module is
`modules/bacterial_type_vi_secretion_apparatus.yaml`.

## Boundary

The reusable core includes the TssJLM membrane complex, TssEFGK baseplate,
TssA/Hcp/TssBC contractile tail, VgrG tip, and ClpV sheath-recycling ATPase.
The K1-specific VgrG adapters, effectors, immunity proteins, and global regulators
are outside the module. TagP1 and TagB1 are recorded as K1 accessory stabilizers;
TagF1 is recorded as a locus-specific post-translational regulator rather than a
conserved structural component.

## Status

- [x] Resolve the 15-gene structural-operon map from PMID:36748579 and Table S4.
- [x] Define a species-neutral, multi-part apparatus module.
- [x] Curate all existing GO annotations and core functions.
- [ ] Complete OpenScientist gene and module + pathway + taxon research.
- [x] Obtain annotation-reviewer subagent sign-off.
- [x] Validate and render all artifacts.
- [ ] Open one draft PR.

## K1 Structural Operon

| Operon order | Gene | Locus | UniProt | Assignment | Module boundary |
|---:|---|---|---|---|---|
| 1 | `tagB1` | PP_5562 | A0A140FWB5 | sheath stabilizer | K1 accessory |
| 2 | `tssB1` | PP_3100 | Q88I99 | sheath subunit | core |
| 3 | `tssC1` | PP_3099 (`puuD`) | Q88IA0 | sheath subunit; not urate oxidase | core |
| 4 | `tssE1` | PP_3098 | Q88IA1 | baseplate subunit | core |
| 5 | `tssF1` | PP_3097 | Q88IA2 | baseplate subunit | core |
| 6 | `tssG1` | PP_3096 | Q88IA3 | baseplate subunit | core |
| 7 | `clpV1/tssH1` | PP_3095 | Q88IA4 | sheath-recycling ATPase | core |
| 8 | `tssJ1` | PP_3094 | Q88IA5 | membrane-complex lipoprotein | core |
| 9 | `tssK1` | PP_3093 | Q88IA6 | baseplate connector | core |
| 10 | `tssL1` | PP_3092 | Q88IA7 | membrane-complex component | core |
| 11 | `tssM1` | PP_3091 | Q88IA8 | membrane-complex component | core |
| 12 | `tagF1` | PP_5561 | A0A140FWB4 | post-translational repressor | K1 regulation |
| 13 | `tagP1` | PP_3090 | Q88IA9 | envelope/sheath stabilizer | K1 accessory |
| 14 | `hcp1/tssD1` | PP_3089 | Q88IB0 | inner tube | core |
| 15 | `tssA1` | PP_3088 | Q88IB1 | assembly coordinator | core |

The adjacent `vgrG1` product PP_3106 (Q88I93) is included as the conserved tip
exemplar, while the surrounding adapter/effector/immunity genes remain excluded.
