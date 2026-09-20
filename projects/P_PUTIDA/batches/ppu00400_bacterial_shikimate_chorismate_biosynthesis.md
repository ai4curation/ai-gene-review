---
title: "PSEPK shikimate and chorismate biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [aroH, aroF-I, aroF-II, aroB, aroQ1, aroQ2, aroQ-III, aroE__Q88RQ5, aroE__Q88K85, aroE__Q88IJ7, PP_3768, PP_2608, aroK, aroA, aroC]
autolink_gene_symbols: false
---

# PSEPK shikimate and chorismate biosynthesis

- Module: `bacterial_shikimate_chorismate_biosynthesis`
- Source bucket: KEGG `ppu00400` (aromatic amino-acid biosynthesis)
- Focused genes: 14 pathway proteins plus one assessed family candidate
- Satisfiability: every pathway step has at least one KT2440 realization; the
  biosynthetic-versus-catabolic assignment of the duplicated middle steps is
  not resolved (see Curation Findings)
- Module research: running
- Gene-level OpenScientist research: running

## Boundary

This batch converts phosphoenolpyruvate and erythrose 4-phosphate to chorismate.
Downstream tryptophan, phenylalanine, tyrosine, folate, and ubiquinone branches
are separate modules. AroA/PP_1770 is a fusion: its EPSP-synthase domain belongs
here, while its prephenate-dehydrogenase activity belongs to the tyrosine branch.

## Functional Parts

| Part | PSEPK realization | Assessment |
|---|---|---|
| DAHP and dehydroquinate formation | AroH Q88LR3, AroF-I Q88KG6, AroF-II Q88IB9, AroB Q88CV2 | Covered |
| Dehydroquinate to shikimate | AroQ1 Q88QD4, AroQ2 Q88K84, AroQ-III Q88IJ6; AroE-family PP_0074 Q88RQ5, PP_2406 Q88K85, PP_3002 Q88IJ7, PP_3768 Q88GF6 | Covered; biosynthetic vs. catabolic roles unresolved |
| Shikimate to EPSP | AroK Q88CV1, AroA Q88M05 | Covered |
| Chorismate formation | AroC Q88LU7 | Covered |

## Curation Findings

Paralogous DAHP synthases, dehydroquinases, and shikimate dehydrogenases are
modeled as alternative implementations of conserved reactions rather than as
duplicate pathway steps. The two unrelated DAHP-synthase families are encoded
as a `variant_sets` block (`axis: enzyme family`, `selection: ONE_OR_MORE`) so
the alternative semantics are machine-readable; the AroQ and AroE paralogs are
alternatives *within* one PANTHER family and stay as a single family selector
carrying several representative members.

KT2440 has five PTHR21089 shikimate-dehydrogenase-family proteins, not four:
PP_0074/Q88RQ5, PP_2406/Q88K85, PP_3002/Q88IJ7, PP_3768/Q88GF6 and
PP_2608/Q88JP1. PP_3768 is now listed in the module and in this batch. PP_2608
was assessed as an AroE-family candidate but is excluded from the module
because direct characterization identifies it as the divergent RifI2
oxidoreductase without an established shikimate-pathway role (PMID:23142411);
because the AroE selector is a FAMILY selector over PTHR21089, of which PP_2608
is a member, that exclusion is normative rather than structurally enforced.

Biosynthetic versus catabolic assignment of the duplicated middle steps is
unresolved. PTHR21272 is named "CATABOLIC 3-DEHYDROQUINASE", and the adjacent
SDH/DHQase gene pairs PP_2406/PP_2407 and PP_3002/PP_3003 have the arrangement
typical of quinate/shikimate catabolism, structurally distinct from the
biosynthetic aroB/aroK locus at PP_5078/PP_5079.

The AroA fusion is split conceptually so its prephenate-dehydrogenase activity
is not conflated with EPSP synthesis.

## Evidence

- `modules/bacterial_shikimate_chorismate_biosynthesis.yaml`
- [PMID:23142411](https://pubmed.ncbi.nlm.nih.gov/23142411/) — RifI2 structural and kinetic characterization (basis for the PP_2608 exclusion)

The OpenScientist module/pathway/taxon report for this batch has not landed yet;
the link will be added when the file exists under `projects/P_PUTIDA/deep-research/`.
