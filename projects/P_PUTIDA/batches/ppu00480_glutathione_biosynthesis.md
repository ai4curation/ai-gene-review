---
title: "PSEPK ppu00480 glutathione biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [gshA, gshB, PP_3253]
autolink_gene_symbols: false
---

# PSEPK ppu00480: glutathione biosynthesis

- Module: `glutathione_biosynthesis`
- Pathway context: KEGG `ppu00480` (glutathione metabolism)
- Focused genes: 3
- Broad membership-table candidates: 31

## Boundary

This batch covers the two conserved biosynthetic reactions:

1. `gshA`: L-glutamate + L-cysteine to gamma-L-glutamyl-L-cysteine
2. `gshB`: gamma-L-glutamyl-L-cysteine + glycine to glutathione

Glutathione reduction, peroxide detoxification, conjugation, degradation, the
gamma-glutamyl cycle, and NADPH-generating reactions are separate modules.
They remain in the broad TSV as pathway-map provenance.

`PP_3253` is included as an organism-specific ambiguity rather than a third
step. It belongs to the type 2/YbdK ligase family and its reviewed UniProt
record states only weak glutamate--cysteine ligase activity. The canonical
type 1 GshA already satisfies step 1.

## Status

- [x] Fetch the focused PSEPK genes from UniProt and GOA.
- [x] Curate all three first-pass gene reviews.
- [x] Create and semantically validate the species-neutral two-part module.
- [x] Attempt full OpenScientist gene-level research; the corrected `gshA`,
  `gshB`, and `PP_3253` requests each exhausted the 7,200-second provider
  timeout without a report.
- [x] Complete generic module OpenScientist research.
- [x] Attempt module + `ppu00480` + PSEPK OpenScientist research; the corrected
  request exhausted the 7,200-second provider timeout without a report.
- [x] Resolve whether `PP_3253` merits a step-1 variant after research.
- [x] Integrate useful research findings without treating provider output as authority.
- [x] Validate and render the module, gene reviews, and batch page.
- [x] Open one non-draft PR for this module:
  [#2240](https://github.com/ai4curation/ai-gene-review/pull/2240).
- [ ] Shepherd the PR through review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `gshA` | PP_0243 | Q88R90 | canonical glutamate--cysteine ligase | Exact MF and glutathione-biosynthesis process accepted |
| `gshB` | PP_4993 | Q88D35 | glutathione synthetase | Exact MF and glutathione-biosynthesis process accepted |
| `PP_3253` | PP_3253 | Q88HV0 | possible type 2 alternative for step 1 | Weak inferred activity and physiological role left undecided |

## Evidence Notes

The exact reviewed UniProt records provide RHEA:13285 for GshA and RHEA:13557
for GshB. Their PANTHER subfamilies are PTHR38761:SF1 and PTHR21621:SF4,
respectively. PP_3253 belongs to PTHR36510:SF1, a distinct type 2/YbdK family.
The generic OpenScientist review confirmed the invariant two-reaction boundary
and identified bifunctional GshAB/GshF proteins as a fused implementation of
the same ordered roles. The reusable module now grounds both activities with
reviewed *Pasteurella multocida* GshAB (UniProtKB:Q9CM00) while retaining
separate reaction parts; PMID:16339152 supplies direct primary evidence for
that fusion. Human GCLC (P48506) and GSS (P48637), together with their exact
PANTHER subfamilies, retain the module's eukaryotic scope. GCLM is documented
as a lineage-specific modifier rather than a third reaction. The report did not
provide organism-specific evidence that `PP_3253` performs the first reaction
in vivo, so it remains outside the module with no asserted core function.

The three gene-level requests and the species-aware module request were each
allowed the full configured 7,200 seconds with three iterations and returned
no report. The module therefore cites the completed generic report and
inspectable exact-record, reaction, family, and gene-review evidence rather
than nonexistent provider files.

The 31-gene KEGG candidate inventory is retained in
[`ppu00480_glutathione_biosynthesis.tsv`](ppu00480_glutathione_biosynthesis.tsv).
