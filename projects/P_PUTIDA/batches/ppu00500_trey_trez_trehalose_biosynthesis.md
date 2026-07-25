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
- [ ] Complete OpenScientist gene-level research.
- [ ] Complete generic module OpenScientist research.
- [x] Complete module + `ppu00500` + PSEPK OpenScientist research.
- [ ] Integrate useful research findings without treating provider output as authority.
- [ ] Validate and render the module, gene reviews, and batch page.
- [ ] Open and shepherd one PR for this module.

## Focused Genes

| Gene | Locus | UniProt | Module role | First-pass result |
|---|---|---|---|---|
| `treY` | PP_4053 | Q88FN6 | maltooligosyltrehalose formation | Exact MF and trehalose-biosynthesis process accepted; target evidence remains sequence-based |
| `treZ` | PP_4051 | Q88FN8 | trehalose release | Exact MF and trehalose-biosynthesis process accepted; broad hydrolase terms demoted |

## Evidence Notes

The TreY and TreZ records map to the specific PTHR10357:SF216 and
PTHR43651:SF11 subfamilies, respectively. Both target assignments remain
inferred rather than directly assayed, so OpenScientist research is being used
to look for KT2440 genetics or biochemistry. The broad candidate inventory is
retained in
[`ppu00500_trey_trez_trehalose_biosynthesis.tsv`](ppu00500_trey_trez_trehalose_biosynthesis.tsv).
