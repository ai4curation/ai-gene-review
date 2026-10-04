---
title: "Taxon Pathway Variance"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
collections: [HOMOLOGY_PROPAGATION]
species: [worm, DROME, human, DICDI]
genes:
  - sta-1
  - sta-2
  - gei-17
  - PIAS1
  - Su(var)2-10
---

# Taxon Pathway Variance

## Why this project exists

A pathway named after its canonical, usually vertebrate, form does not exist in the
same shape in every lineage. Components get lost, replaced, or rewired, while the
families they belong to persist. When that happens, GO terms that presuppose the
canonical wiring keep flowing into lineages where the wiring is absent: by IBA from a
deep PAINT node, by ortholog projection, or by InterPro2GO. Each such annotation is a
small error, but they share a single cause, and a single fix often blocks all of them:
a **GO taxon constraint** (`never_in_taxon` / `only_in_taxon`) on the term, or an IRD
on the lineage in PAINT.

This project does two things:

1. **Documents lineage-specific pathway variants** — where a pathway runs without a
   component its GO term presupposes, how the lineage does it instead, and which
   modules and gene reviews capture that.
2. **Captures proposed new taxon constraints** in a machine-readable table
   ([proposed_taxon_constraints.tsv](TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.tsv)),
   each with the evidence for the absence and the annotations it would block, ready to
   hand to GO.

It is the pathway-level complement to [IBA_REVIEW](IBA_REVIEW.md) section 14
(lineage-inappropriate transfer), which catalogues the individual bad annotations; this
project asks which constraint would have prevented the whole class.

## What counts as a proposal

A row in the constraints table needs all of:

- **A term that presupposes a component.** The GO definition (or its logical
  definition) must require something the lineage lacks; "receptor signaling pathway
  via JAK-STAT" requires a JAK. A process the lineage merely does differently is not
  enough.
- **Evidence of absence, not absence of evidence.** A primary source stating the
  component is missing from the genome (or a reproducible bioinformatics check in a
  `*-bioinformatics/` folder), with a verbatim quote.
- **A check that GO does not already have the constraint** (OLS term metadata,
  `RO:0002161` never_in_taxon / `RO:0002160` only_in_taxon, and inherited constraints
  from ancestors).
- **The annotations it would block**, so the proposal has a measured payoff, and any
  that it would wrongly block (members of the lineage that do have the component).

Taxon ids and GO ids are verified (OLS / QuickGO / NCBITaxon); none are written from
memory.

## Case study 1: JAK-STAT without JAK in *C. elegans*

*C. elegans* has two STAT paralogs and no JAK.

> "There is no conserved homolog of the JAK kinases in C. elegans" — PMID:28874466

Both worm STATs act in JAK-independent pathways, captured in the module
[c_elegans_jak_independent_stat_signaling](../modules/c_elegans_jak_independent_stat_signaling.yaml):

- **STA-1** represses antiviral genes in the intestine, genetically downstream of the
  ACK-family kinase SID-3 (PMID:28874466).
- **STA-2** drives antimicrobial peptide expression in the epidermis after wounding or
  fungal infection, downstream of hemidesmosome (MUP-4) and PMK-1 signalling with
  SNF-12.

The canonical, JAK-based decomposition is [jak_stat_signaling](../modules/jak_stat_signaling.yaml),
which now carries a pointer to the worm variant.

JAK-presupposing terms nevertheless reach worm genes by IBA from two families:

| Family | Node | Term | Worm gene | Gene review action |
|---|---|---|---|---|
| PIAS (PTHR10782) | PTN000845825 (Eumetazoa) | GO:0046426 negative regulation of receptor signaling pathway via JAK-STAT | gei-17 | REMOVE; family review records a member exception |
| STAT (PTHR11801) | PTN000927860 | GO:0007259 cell surface receptor signaling pathway via JAK-STAT | sta-2 | REMOVE |

The STAT and JAK family reviews (`interpro/panther/PTHR11801/`,
`interpro/panther/PTHR45807/`) and the sta-1 gene review are in progress and will
extend this table.

The PIAS case is also where the repository gained **member exceptions** in family
reviews: PANTHER subfamily PTHR10782:SF94 holds both the fly PIAS (a genuine JAK-STAT
regulator) and worm GEI-17, so no subfamily-level scope can separate them. See
`interpro/panther/PTHR10782/PTHR10782-review.yaml`.

## Proposed taxon constraints

See [proposed_taxon_constraints.tsv](TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.tsv).
Columns: `go_id`, `go_label`, `constraint` (never_in_taxon / only_in_taxon),
`taxon_id`, `taxon_label`, `existing_go_constraint` (what GO already has, if
anything), `evidence` (PMID), `evidence_quote`, `blocks` (annotations it would remove),
`would_wrongly_block`, `status` (PROPOSED / SUBMITTED / ACCEPTED / REJECTED),
`source` (where in this repo the case was found).

## Candidate cases to scope next

- **Dictyostelium STATs** (statA–D): STAT family members in an amoebozoan; the IBA
  project already records JAK-STAT and metazoan defense/proliferation terms
  over-propagated to statA/statC from PTN000927860.
- Other pathways named for a component with a patchy distribution (to be collected as
  they surface in IBA and family reviews).

## Related

- [IBA_REVIEW](IBA_REVIEW.md) — section 14, lineage-inappropriate transfer
- [GENOME_WIDE_VALIDATION](GENOME_WIDE_VALIDATION.md) — reuses GO taxon constraints as
  a consistency check
- [PAINT](PAINT.md) — family reviews and node assessments
