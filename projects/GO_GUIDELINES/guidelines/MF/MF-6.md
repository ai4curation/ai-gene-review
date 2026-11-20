---
id: MF-6
title: Use class-level binding children; name the specific partner in `has_input`
status: proposed
topic: MF
provenance: GOC
aspects:
- F
evidence_codes:
- IPI
go_terms:
- term_id: GO:0019901
  label: protein kinase binding
- term_id: GO:0030971
  label: receptor tyrosine kinase binding
- term_id: GO:0005515
  label: protein binding
- term_id: GO:0051015
  label: actin filament binding
sources:
- kind: wiki
  title: Guidelines for new Binding terms
  url: https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms
- kind: wiki
  title: Proposal to obsolete children of "transcription factor binding"
  url: https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22
- kind: wiki
  title: Annotating binding
  url: https://wiki.geneontology.org/index.php/Annotating_binding
date: '2026-11-15'
---

# MF-6. Use class-level binding children; name the specific partner in `has_input`

## Decision

When a binding term is warranted, choose the child that names the class of partner
(`GO:0019901` protein kinase binding, `GO:0030971` receptor tyrosine kinase binding).
Put the specific physiological partner in `has_input`; put the partner actually used in
the experiment in With/From. Do not request binding terms for individual proteins.

## Context

Subclasses of GO:0005515 "should represent general classes of proteins, not
specific proteins"
([wiki: Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)).
GO obsoleted the per-partner children of transcription factor binding for the same
reason ([wiki: Proposal to obsolete children of "transcription factor binding"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)).
With/From supports the evidence; the extension modifies the term. A mouse receptor shown
to bind a human ligand is annotated with the human ligand in With/From and the
orthologous mouse ligand in `has_input`
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

## Application

Worked example. C. elegans UNC-115 binds filaments made from rabbit skeletal muscle
actin: `GO:0051015` actin filament binding, IPI, rabbit actin in With/From. Actin,
tubulin and histone binding are exceptions to the `has_input` recommendation because
many identical copies exist and the copy used is rarely known
([wiki: Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| Evidence codes | IPI |
| GO terms | `GO:0019901` protein kinase binding; `GO:0030971` receptor tyrosine kinase binding; `GO:0005515` protein binding; `GO:0051015` actin filament binding |

## Sources

- wiki: [Guidelines for new Binding terms](https://wiki.geneontology.org/index.php/Guidelines_for_new_Binding_terms)
- wiki: [Proposal to obsolete children of "transcription factor binding"](https://wiki.geneontology.org/index.php/Proposal_to_obsolete_children_of_%22transcription_factor_binding%22)
- wiki: [Annotating binding](https://wiki.geneontology.org/index.php/Annotating_binding)

<!-- END GENERATED -->
