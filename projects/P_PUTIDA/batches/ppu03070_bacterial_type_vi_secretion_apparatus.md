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

- [x] Resolve the 15-gene structural-operon map from PMID:36748579 Figure 2a, operon text, and exact UniProt family records.
- [x] Define a species-neutral, multi-part apparatus module.
- [x] Curate all existing GO annotations and core functions.
- [x] Complete OpenScientist module + pathway + taxon research.
- [x] Complete and document a Wave130 annotation-reviewer pass for all 16 selected genes.
- [x] Validate and render all Wave130 artifacts.
- [x] Prepare the Wave130 repair for a non-draft PR.

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

## Review Follow-up

The PR review was addressed by adding gene-specific family evidence to the
process assertions, structural molecule activity and GO:0033104 complex
membership to the structural subunits, and a machine-usable negative-regulation
term for TagF1. Family/domain-supported NEW annotations now use ISS, while the
directly mapped TagP1 and TagB1 accessory assignments retain TAS. Figure 2a,
not Table S4, is cited for the locus map; Table S4 is limited to intergenic
distances. The TssM selector uses the discriminating IPR048677 TssM1
helical-region entry with an explicit full-length multi-pass-architecture
caveat because the TagP1-like accessory also matches the broader IPR053156
family.

## Wave130 Annotation-Reviewer Pass

On 2026-09-01, all GOA-derived and proposed annotations for the 16 selected
genes were reassessed against each gene's UniProt record, the cached full text
of PMID:36748579, and the reusable module boundary. No annotation was accepted
from locus membership alone when the gene assignment required separate family
or promoter evidence. The pass retained the existing action set except for
clarifying evidence provenance where noted below.

| Selected gene | Annotation-reviewer decision |
|---|---|
| `PP_3088` (TssA1) | Retain NEW GO:0033103; TssA family evidence and locus position support an assembly role. |
| `PP_3089` (Hcp1/TssD1) | Retain NEW GO:0033103; IPR008514 supports the inner-tube assignment. |
| `PP_3090` (TagP1) | Retain membrane as non-core and NEW GO:0033103; keep outside the conserved apparatus because it is a K1 accessory. |
| `PP_5561` (TagF1) | Retain NEW GO:0050709 as the available broader negative-regulation term; keep outside the structural core. |
| `PP_3091` (TssM1) | Retain NEW GO:0033103; replace the shared IPR053156 quote with the discriminating IPR048677 TssM1 helical-region evidence. |
| `PP_3092` (TssL1) | Retain NEW GO:0033103; DotU/TssL family evidence supports membrane-complex membership. |
| `PP_3093` (TssK1) | Retain NEW GO:0033103; family evidence supports the baseplate-connector role. |
| `PP_3094` (TssJ1) | Retain NEW GO:0033103; lipoprotein and TssJ family evidence support the outer-membrane anchor role. |
| `clpV` (ClpV1/TssH1) | Retain ATP hydrolysis ACCEPT, cytoplasm non-core, broad ATP binding over-annotation, heat-response REMOVE, and NEW GO:0033103; represent ClpV as the sheath-recycling ATPase rather than a structural sheath subunit. |
| `PP_3096` (TssG1) | Retain NEW GO:0033103; IPR010732 supports the baseplate role. |
| `PP_3097` (TssF1) | Retain NEW GO:0033103; family evidence supports the baseplate role. |
| `PP_3098` (TssE1) | Retain NEW GO:0033103; gp25-like/TssE family evidence supports the baseplate role. |
| `puuD` (TssC1) | Retain REMOVE for legacy urate oxidase activity and NEW GO:0033103; multiple TssC-specific families contradict the legacy enzyme name. |
| `PP_3100` (TssB1) | Retain NEW GO:0033103; sheath-family evidence supports the TssB1 role. |
| `PP_5562` (TagB1) | Retain NEW GO:0033103 but correct the rationale: Figure 2a and promoter mapping support TagB1, while UniProt supplies no family/domain assignment. |
| `PP_3106` (VgrG1) | Retain extracellular region as non-core and NEW GO:0033103; IPR006533 and the mapped vgrG operon support the puncturing-tip role. |

The pass also confirmed that all molecular-function terms remain on leaf gene or
module annotons. GO:0005198 is used only for structural subunits, GO:0016887 is
used for ClpV, and no redundant module/step localization pair is asserted.

## OpenScientist Outcome

The commissioned module + `ppu03070` + PSEPK run completed in 1,661.54 seconds
with 15 citations and two rendered artifacts. Its report is stored at
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_type_vi_secretion_apparatus__ppu03070-deep-research-openscientist.md`.

The report independently supports four curation conclusions used here:

- `ppu03070` is a broad multi-secretion-system bucket, so KEGG membership alone
  cannot define the type VI apparatus.
- The K1 locus satisfies the full conserved apparatus boundary.
- PP_3099 is a TssC1 sheath protein rather than a urate oxidase.
- The absence of dedicated ClpV proteins from the K2/K3 loci and the apparent
  K3 TssC gap are follow-up questions, not reasons to alter the reusable core.

The report's PP_3090+PP_3091 split-TssM interpretation was rejected during
manual adjudication. PMID:36748579 Figure 2a identifies PP_3090 as TagP1, while
PP_3091 alone carries the IcmF_C and TssM1-specific helical architecture. The
broad TssM-like hit on PP_3090 is therefore insufficient to override the direct
locus assignment. The generic module remains a reusable single-apparatus
template; this batch records the concrete K1 realization.
