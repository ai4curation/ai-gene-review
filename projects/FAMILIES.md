---
title: "Protein Families"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
template: family_index
autolink_gene_symbols: false
---

**Bottom line:** many GO annotations reach a gene through its protein family, by PAINT/IBA propagation from a node in a PANTHER tree or by InterPro2GO mapping of a Pfam domain, so a call about what a family does is copied onto every member below that point. This page is the catalog of our family-level reviews: each one asks whether the family is functionally uniform enough for a term to sit on all of it, and records a scope (family-wide, subfamily-only, residue-determined or unresolved) for each GO term assessed. We did this because per-gene reviews kept tracing over-propagated annotations back to functionally heterogeneous families, and correcting them one gene at a time leaves the source in place. The catalog currently holds 333 entries (324 PANTHER families, 9 Pfam domains), 211 of them marked complete. Of the families with a recorded coherence call, 145 are heterogeneous, 53 mostly coherent and only 28 fully coherent; of 327 term-scope calls, 83 are safe family-wide, 29 only for named subfamilies, 6 depend on a curated residue, and 199 remain unresolved, with 10 not applicable. All 9 Pfam entries were judged not viable for a domain-level GO mapping.

The collections, focused family projects and related mapping reviews below give the detail behind those counts.

## Family review collections

| Collection | Explore |
|------------|---------|
| [ProtNLM benchmark families](PROTNLM_EVALUATION/family-curation/family-index.html) | Family assessments and supporting evidence across the ProtNLM benchmark, with a companion [gene index](PROTNLM_EVALUATION/family-curation/gene-index.html). |
| [PANTHER / IBA family reviews](PANTHER_IBA_REVIEW/README.md) | Family-level review of phylogenetic annotation propagation for a set of fission yeast genes. |

## Focused family projects and reports

| Family | Explore |
|--------|---------|
| [CASP / CASP-like proteins](CASPL_FAMILY.md) | Plant family curation connecting poplar and Arabidopsis gene reviews, PANTHER families, and orthology analyses. |
| [PTHR48034 family review](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR48034/PTHR48034-review.md) | A family-level report examining the splicing annotations inherited by CIRBP. Source report on GitHub. |
| [PM20D1 / M20 family research](https://github.com/ai4curation/ai-gene-review/tree/main/projects/FAMILIES/PM20D1) | Research reports on functional divergence within the M20 family. Source reports on GitHub. |

## Family and domain annotation mappings

- [InterPro mapping reviews](INTERPRO.md) — GO mappings associated with protein domains and family signatures.
- [NCBIFam](NCBIFam.md) — functional-family mappings and GO annotation coverage.
- [PAINT / IBA](IBA_REVIEW.md) — phylogenetic function inheritance and evidence for annotation propagation.
- [TreeGrafter](TREEGRAFTER.md) — automated placement on PANTHER trees and annotation transfer.

[Browse all projects](all-projects.html) · [Browse gene reviews](../../app/index.html)

[Catalog rendering and source links](FAMILIES/README.md)

[Slides](FAMILIES/slides/FAMILIES-slides.html) (Marp source: [FAMILIES-slides.md](FAMILIES/slides/FAMILIES-slides.md)) — AI generated
