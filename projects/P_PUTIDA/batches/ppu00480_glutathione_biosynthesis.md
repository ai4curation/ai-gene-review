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

## 2026-08-13 Follow-up

This ownership pass rechecked every current GOA row and qualifier for `gshA`,
`gshB`, and `PP_3253`; the existing curation decisions remain biologically
appropriate. PMID:40302248 adds direct P. putida KT2440 Tn-seq support for the
identity and an above-threshold copper/cobalt fitness phenotype of `gshA`. No
metal-response BP is proposed because disrupting glutathione synthesis depletes
a broadly protective metabolite: the pooled-mutant fitness result is consistent
with indirect loss of glutathione buffering, not direct GshA involvement in a
specific metal-response or detoxification process. The same study reports a
weaker `gshB` copper phenotype that did not pass its statistical threshold, so
it likewise is not used to infer a response annotation. No organism-specific
result in that paper establishes `PP_3253` as a physiological substitute for
GshA.

All five requested OpenScientist jobs were launched and allowed to finish
without manual termination. The `gshB` gene run completed after 1,001.73
seconds; its report supports the exact glutathione synthase activity and
two-step pathway placement but adds no defensible new GO term. The `gshA` and
`PP_3253` gene runs, generic bacterial-module run, and
module+UPA00142+PSEPK run each exhausted the full 7,200-second provider timeout
without a report. The initial 8,100-second gene-timeout requests were rejected
before launch because OpenScientist caps provider timeouts at 7,200 seconds;
the corrected 7,200-second jobs were then launched and left to complete.

Annotation-reviewer QA confirmed 6/6 `gshA`, 7/7 `gshB`, and 4/4 `PP_3253`
GOA rows are represented once with their original qualifiers. Exact enzyme MFs
and GO:0006750 remain core for canonical GshA and GshB; generic catalytic,
binding, and localization terms remain over-annotated or non-core. PP_3253's
specific ligase and process terms remain undecided, its broad C-N ligase class
is non-core, and no core function is asserted.

## 2026-09-01 Family-evidence repair

Repair PR: [#2862](https://github.com/ai4curation/ai-gene-review/pull/2862).

The bifunctional *Pasteurella multocida* GshAB/GshF exemplar Q9CM00 is assigned
to PANTHER:PTHR38761:SF1 on the basis of its N-terminal glutamate--cysteine
ligase region, even though the same polypeptide also performs the second
glutathione-synthetase reaction. The second module leaf now includes that exact
whole-protein classification only in the exemplar description, not as a family
selector. The same subfamily contains monofunctional GshA proteins, so asserting
it on the second leaf would falsely imply glutathione-synthetase activity for
those proteins. InterPro:IPR040657 identifies the C-terminal ATP-grasp-like
domain and PMID:16339152 directly establishes both activities in the recombinant
fusion. The resulting outside-family advisory for Q9CM00 is intentional and
documents fusion architecture rather than a validation failure.
