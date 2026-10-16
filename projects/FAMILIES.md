---
title: "Protein Families"
maturity: IN_PROGRESS
last_reviewed: 2026-10-04
tags: [PIPELINE, EVALUATION]
template: family_index
autolink_gene_symbols: false
manifest:
  slides:
    - href: FAMILIES/slides/FAMILIES-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/3EXdRSggSxqVqzjNGdB2Tx
      title: Project brief
---

**Bottom line:** many GO annotations reach a gene through a reusable family or signature source. PAINT/IBA places a function at an ancestral node in a PANTHER tree and lets descendants inherit it; InterPro2GO attaches a GO term to every protein that matches an InterPro/Pfam signature. This page catalogs reviews of both sources: whether a PANTHER family is functionally uniform enough for a term to descend family-wide, and whether a Pfam-associated InterPro entry is specific enough for a domain-level GO mapping. We did this because per-gene reviews kept tracing over-propagated annotations back to functionally heterogeneous families, and correcting them one gene at a time leaves the source in place. The catalog currently holds 353 entries (344 PANTHER families, 9 Pfam domains), 218 of them marked complete. Among entries with a determinate coherence call, 151 are heterogeneous, 60 mostly coherent and only 33 fully coherent; another 20 are explicitly unknown and 89 have no recorded coherence call yet. Of 391 term-scope calls, 98 are safe family-wide, 61 only for named subfamilies, 7 depend on a curated residue, and 211 remain unresolved, with 14 not applicable. All 9 Pfam entries were judged not viable for a domain-level GO mapping.

The collections, focused family projects and related mapping reviews below give the detail behind those counts.

## Family review collections

| Collection | Explore |
|------------|---------|
| [ProtNLM benchmark families](PROTNLM_EVALUATION/family-curation/family-index.html) | Family assessments and supporting evidence across the ProtNLM benchmark, with a companion [gene index](PROTNLM_EVALUATION/family-curation/gene-index.html). |
| [PANTHER / IBA family reviews](PANTHER_IBA_REVIEW.md) | Family-level review of phylogenetic annotation propagation for a set of fission yeast genes. |

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
