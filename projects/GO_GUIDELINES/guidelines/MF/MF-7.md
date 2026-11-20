---
id: MF-7
title: For small molecules, annotate the physiological ligand; never the drug or probe
status: proposed
topic: MF
provenance: GOC
aspects:
- F
go_terms:
- term_id: GO:0005488
  label: binding
- term_id: GO:0051378
  label: serotonin binding
- term_id: GO:0016594
  label: glycine binding
- term_id: GO:0003755
  label: peptidyl-prolyl cis-trans isomerase activity
- term_id: GO:0005528
  label: FK506 binding
open_questions:
- '**Drug-named binding terms.** `GO:0005528` FK506 binding names an exogenous compound. Should such terms
  be reviewed under the 2020 drug-binding rules?'
sources:
- kind: wiki
  title: Annotation Conf. Call 2020-02-04
  url: https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04
- kind: issue
  title: go-annotation#3166
  url: https://github.com/geneontology/go-annotation/issues/3166
date: '2026-11-15'
---

# MF-7. For small molecules, annotate the physiological ligand; never the drug or probe

## Decision

Annotate small-molecule binding as `GO:0005488` binding (or an existing specific
binding term) with `has_input` a ChEBI entity, rather than requesting a new
pre-composed term. When a compound was used as a proxy for a natural ligand, annotate
binding of the natural ligand. Make no binding annotation for a drug interaction that
is a gain of function outside the protein's normal role.

## Context

The 2020 ontology editors' decision asks curators to use binding plus
`has_input` ChEBI for chemical binding
([wiki: Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)).
The obsoletion of "drug binding" set the three-way rule for compounds
([go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166)):
proxy for a natural ligand, annotate the natural ligand; pathway inhibitor, annotate the
pathway BP only for products that normally act in it; gain-of-function drug binding,
annotate nothing.

## Application

Worked examples. LSD binding to a serotonin receptor supports `GO:0051378` serotonin
binding (LSD in With/From where allowed); strychnine binding supports `GO:0016594`
glycine binding. FKBP1A (FKBP12) inhibits TORC1 only when bound to rapamycin, which is
not part of its normal role, so its drug binding rows were deleted and no TORC1
signaling annotation is made for it. Its own enzymatic activity,
`GO:0003755` peptidyl-prolyl cis-trans isomerase activity, is the informative MF.
(`GO:0005528` FK506 binding is itself a drug-named term worth questioning; see Open
questions.)

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC] |
| Date | 2026-11-15 |
| GO terms | `GO:0005488` binding; `GO:0051378` serotonin binding; `GO:0016594` glycine binding; `GO:0003755` peptidyl-prolyl cis-trans isomerase activity; `GO:0005528` FK506 binding |

## Open questions

1. **Drug-named binding terms.** `GO:0005528` FK506 binding names an exogenous compound. Should such terms be reviewed under the 2020 drug-binding rules?

## Sources

- wiki: [Annotation Conf. Call 2020-02-04](https://wiki.geneontology.org/index.php/Annotation_Conf._Call_2020-02-04)
- issue: [go-annotation#3166](https://github.com/geneontology/go-annotation/issues/3166)

<!-- END GENERATED -->
