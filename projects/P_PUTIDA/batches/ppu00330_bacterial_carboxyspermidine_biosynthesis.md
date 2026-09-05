---
title: "PSEPK carboxyspermidine biosynthesis"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [speA, speB, PP_2928, nspC]
autolink_gene_symbols: false
---

# PSEPK carboxyspermidine biosynthesis

This batch narrows the broad KEGG `ppu00330` arginine/proline map to the
arginine-to-spermidine carboxyspermidine route.

## Boundary

1. PP_2928 CASDH is strongly inferred to condense putrescine and aspartate semialdehyde to
   carboxyspermidine using NADPH.
2. NspC is strongly inferred to decarboxylate carboxyspermidine to spermidine.

SpeA/SpeB-mediated putrescine supply remains relevant batch context, but it is
not inflated into the reusable two-reaction module. Asd-dependent
aspartate-semialdehyde supply, alternative SpeC putrescine supply, polyamine
catabolism, and the classical SpeD/SpeE route are likewise outside the required
core. `PP_3146` is a generic oxidoreductase and is explicitly excluded.

## Gap Resolution

The initial metadata made CASDH appear absent. Species-aware OpenScientist
research identified `PP_2928/Q88IS1`, immediately adjacent to `nspC`, as a
strong CASDH candidate based on PTHR43796 membership, domain architecture,
protein length, synteny, and sequence similarity to characterized CANSDH. The
exact current label of GO:0102143 is "carboxynorspermidine dehydrogenase
activity"; in this pathway the putrescine substrate yields carboxyspermidine,
so the activity is described mechanistically as CASDH. PP_2928 and NspC roles
are strong comparative/synteny inferences, not direct KT2440 experiments.

## Status

- [x] Resolve the apparent CASDH gap and exclude PP_3146.
- [x] Define a reusable two-reaction module with exact KT2440 exemplars.
- [x] Curate the four KT2440 gene reviews.
- [x] Complete module + pathway + taxon OpenScientist research.
- [x] Complete the generic-module OpenScientist job and link its report from the module.
- [x] Obtain annotation-reviewer subagent sign-off.
- [x] Validate and render all artifacts.
- [x] Open one draft PR (PR #2533).

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `speA` | PP_0567 | Q88QC7 | Upstream agmatine supply context |
| `speB` | PP_2196 | Q88KU3 | Upstream putrescine supply context |
| `PP_2928` | PP_2928 | Q88IS1 | Inferred CASDH carboxyspermidine formation |
| `nspC` | PP_2929 | Q88IS0 | Inferred terminal carboxyspermidine decarboxylation |
