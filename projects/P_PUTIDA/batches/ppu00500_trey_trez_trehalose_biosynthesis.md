---
title: "PSEPK ppu00500 TreY/TreZ trehalose biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [treY, treZ]
autolink_gene_symbols: false
---

# PSEPK ppu00500: TreY/TreZ trehalose biosynthesis

- Module: `trey_trez_trehalose_biosynthesis`
- Pathway context: KEGG `ppu00500` (starch and sucrose metabolism)
- Focused genes: 2
- Broad membership-table candidates: 18

## Boundary

This batch covers the two-reaction TreY/TreZ route:

1. `treY`: alpha-glucan to maltooligosyltrehalose
2. `treZ`: maltooligosyltrehalose to trehalose plus shortened alpha-glucan

Glycogen synthesis and remodeling supply substrate but are outside this
module. Alternative OtsA/OtsB and TreS trehalose routes, trehalose degradation,
cellulose synthesis, and central hexose metabolism are also separate.

## Status

- [x] Fetch the focused PSEPK genes from UniProt and GOA.
- [x] Curate both first-pass gene reviews.
- [x] Create and semantically validate the species-neutral two-part module.
- [x] Attempt full OpenScientist gene-level research; the corrected `treY` and
  `treZ` requests each exhausted the 7,200-second provider timeout without a
  report.
- [x] Attempt generic module OpenScientist research; the corrected request
  exhausted the 7,200-second provider timeout without a report.
- [x] Complete module + `ppu00500` + PSEPK OpenScientist research.
- [x] Integrate useful research findings without treating provider output as authority.
- [x] Validate and render the module, gene reviews, and batch page.
- [x] Open one non-draft PR for this module:
  [#2244](https://github.com/ai4curation/ai-gene-review/pull/2244).
- [ ] Shepherd the PR through review and CI.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `treY` | PP_4053 | Q88FN6 | maltooligosyltrehalose formation | Exact MF and trehalose-biosynthesis process accepted; target evidence remains sequence-based |
| `treZ` | PP_4051 | Q88FN8 | trehalose release | Exact MF and trehalose-biosynthesis process accepted; broad hydrolase terms demoted |

## Evidence Notes

The TreY and TreZ records map to the specific PTHR10357:SF216 and
PTHR43651:SF11 subfamilies, respectively. Both target assignments remain
inferred rather than directly assayed; the completed OpenScientist review
looked for KT2440 genetics and biochemistry. The broad candidate inventory is
retained in
[`ppu00500_trey_trez_trehalose_biosynthesis.tsv`](ppu00500_trey_trez_trehalose_biosynthesis.tsv).

Ortholog biochemistry independently grounds the reusable module:
PMID:8605217 identifies the adjacent *Arthrobacter* sp. Q36 treY/treZ pair,
PMID:8611744 characterizes purified TreY, and PMID:8611745 characterizes
purified TreZ. These papers support the two reaction definitions and exemplar
accessions without being treated as direct evidence for the KT2440 proteins.

The completed species-aware report judged both reactions present and the
two-step module satisfiable, while correctly retaining weaker evidence for
TreY than TreZ. Its statement that Q88FN6 has no EC number conflicts with the
fetched target record, which contains EMBL-derived EC 5.4.99.15; the exact
record is used for that field, while the absence of target-strain biochemical
evidence remains explicit. The two gene requests and the generic module
request each exhausted the full configured 7,200 seconds with three
iterations.
