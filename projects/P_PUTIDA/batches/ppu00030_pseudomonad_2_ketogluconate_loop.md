---
title: "PSEPK 2-ketogluconate loop batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [gcd, PP_3382, PP_3383, PP_3384, kguT, kguK, kguE, ptxD]
autolink_gene_symbols: false
---

# PSEPK periplasmic 2-ketogluconate loop

## Workflow

- [x] Fetch or reuse all eight selected gene-review inputs.
- [x] Complete the requested OpenScientist calls and inspect available outputs.
- [x] Reconcile generic module and PSEPK pathway evidence.
- [x] Reconcile Gad architecture, KguE uncertainty, and PP_3376/KguD identity.
- [x] Curate all GOA rows and consult the annotation reviewer.
- [x] Validate and render the scoped genes, module, and batch page.
- [x] Open one draft PR and address automated review feedback.

## Boundary

- The loop runs from periplasmic glucose oxidation through cytoplasmic 6-phosphogluconate.
- The reusable scope is Pseudomonas, not all Pseudomonadota.
- PQQ biosynthesis, porin-mediated entry, PtxS regulation, the alternative GnuK route,
  and the downstream Entner-Doudoroff trunk are excluded.
- KguE is retained as a module-adjacent accessory candidate because its reaction is
  unresolved; it is not used as the terminal reductase.
- PP_3376/Q88HI1 is reviewed under its current `ptxD` symbol but resolved
  conservatively as the KguD candidate from direct KT2440 genetics, locus context,
  and KEGG K00032. No phosphite-dehydrogenase function is claimed.

## Evidence reconciliation

The combined pathway report initially treated PP_3376 as an unrelated phosphonate
dehydrogenase by following its legacy name. That conclusion is superseded by the
primary KT2440 mutant study (PMID:17483213) and the conserved Pseudomonas pathway
order summarized in PMID:29607620. The separately completed phosphite-focused
OpenScientist report was used only to retrieve candidate literature; its transfer
of phosphite activity to Q88HI1 was adjudicated as unsupported target-level evidence.

The seven requested gene-level OpenScientist clients and the generic-module client
were allowed to finish without termination or replacement. They did not leave final
report files in this worktree, so no absent report content was inferred or cited.

The five initially header-only GOA exports were force-refetched from QuickGO and all
12 recovered rows were reviewed: three for PP_3383, one for PP_3384, four for kguT,
three for kguK, and one for kguE. Manual notes record the failed-report provenance.
PMID:39770733 now supplies verbatim primary support for the KguT-KguK-KguD route and
for retaining only a process-level KguE assignment. Reviewed UniProt exemplars
O34213, O34214, and O34215 were verified as the third, flavoprotein, and cytochrome c
Gad subunits, with Q88HH4, Q88HH5, and Q88HH6 as the exact KT2440 implementations.
The exact reviewed UniProt `ID`/`DE` lines are retained in
`modules/pseudomonad_2_ketogluconate_loop-exemplar-verification.md` for offline QA.
GO:0015128 was verified as gluconate-specific and therefore was not reused for
2-dehydro-D-gluconate; GO:0046943 is used as the existing carboxylic-acid transport
intermediate while exact transporter and catabolic-process terms are proposed.

2026-08-13: Started as module 18 of the current 20-module batch.
