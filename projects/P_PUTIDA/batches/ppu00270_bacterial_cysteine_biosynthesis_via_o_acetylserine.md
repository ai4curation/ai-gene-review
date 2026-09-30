---
title: "PSEPK ppu00270 bacterial cysteine biosynthesis via O-acetylserine"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [cysE, cysK, cysM]
autolink_gene_symbols: false
---

# PSEPK ppu00270: bacterial cysteine biosynthesis via O-acetylserine

- Module: `bacterial_cysteine_biosynthesis_via_o_acetylserine`
- Pathway context: KEGG `ppu00270` (cysteine and methionine metabolism)
- Focused genes: 3
- Broad `ppu00270` membership-table candidates retained in TSV: 46

## Boundary

This batch covers the two reactions that convert L-serine to L-cysteine:

1. `cysE`/Q88PL0 transfers acetyl from acetyl-CoA to L-serine, producing
   O-acetyl-L-serine.
2. `cysK`/Q88E95 or `cysM`/Q88MC0 incorporates sulfide into
   O-acetyl-L-serine, producing L-cysteine and acetate.

Sulfate uptake and APS-dependent reduction to sulfide are upstream input supply
and remain in `aps_dependent_assimilatory_sulfate_reduction`. Methionine
biosynthesis, transsulfuration, cysteine utilization, glutathione synthesis,
and other broad KEGG `ppu00270` members are separate modules.

The terminal alternatives are not treated as interchangeable labels. Exact
PSEPK records support the same sulfide-dependent GO:0004124 reaction for both
proteins, while InterPro distinguishes CysK/OASS-A (IPR005859) from CysM/OASS-B
(IPR005858). Work in P. aeruginosa indicates that CysK is sulfide-optimized and
CysM can specialize toward thiosulfate-dependent S-sulfocysteine formation.
That substrate preference is recorded as a hypothesis for Q88MC0, not imported
as a new KT2440 annotation.

## Workflow

- [x] Fetch `cysE`, `cysK`, and `cysM` from current UniProt and GOA.
- [x] Curate all three first-pass gene reviews and notes.
- [x] Create a reusable two-part module with exact UniProt leaves.
- [x] Complete OpenScientist research for `cysK`; `cysE` and `cysM` remain active provider jobs and are not required for this evidence-complete first pass.
- [ ] Complete generic module OpenScientist research.
- [ ] Complete module + `ppu00270` + PSEPK OpenScientist research.
- [x] Integrate useful CysK research findings without treating provider output as authority.
- [ ] Run final gene, module, render, test, and diff/cache checks.
- [ ] Open one draft PR for this module/pathway.
- [ ] Shepherd automated review and CI feedback.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `cysE` | PP_0840 | Q88PL0 | serine O-acetylation | Exact EC 2.3.1.30 reaction accepted; broad O-acetyltransferase retained as non-core |
| `cysK` | PP_4571 | Q88E95 | sulfide incorporation, CysK/OASS-A variant | Exact EC 2.5.1.47 reaction accepted; PLP binding proposed from mapped cofactor sites |
| `cysM` | PP_1654 | Q88MC0 | sulfide incorporation, CysM/OASS-B variant | Exact EC 2.5.1.47 reaction accepted; thiosulfate specialization remains untested in KT2440 |

## Satisfiability

The KT2440 instance is covered at both required steps: Q88PL0 supplies
O-acetyl-L-serine and either Q88E95 or Q88MC0 can satisfy the exact
sulfide-incorporation reaction. P. putida S-313 cell extracts provide direct
organism-level evidence for O-acetylserine sulfhydrylase activity
(PMID:10482527), although that study predates KT2440 locus assignments.

Three additional CysE-family records, PP_0228/Q88RA5, PP_1110/Q88NU4, and
PP_3136/Q88I65, remain candidate alternatives rather than required leaves.
Their electronic annotations and atypical architectures do not establish that
they replace or supplement Q88PL0 physiologically. This is a focused knowledge
gap for future gene-level review.

## Ontology Note

GO:0006535 is the live, route-specific term for L-cysteine biosynthesis from
L-serine. The three broad GO:0019344 annotations remain correct, while authored
core functions and the module concept use GO:0006535 for greater precision.

Generated UTC: 2026-08-11

## Research qualification

The completed CysK report suggested a stable CysE-CysK cysteine-synthase
complex. That claim is not adopted for this reusable bacterial module. Direct
work in P. aeruginosa found no detectable binding between CysK and the
endogenous CysE1 C-terminal peptide (PMID:41676964), and no interaction has been
tested in KT2440. The two enzymes are therefore modeled as sequential pathway
steps; any direct physical complex remains an experimental question.
