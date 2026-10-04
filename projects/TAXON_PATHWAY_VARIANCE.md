---
title: "Taxon Pathway Variance"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
collections: [HOMOLOGY_PROPAGATION]
species: [worm, DROME, human, DICDI]
genes:
  - sta-1
  - sta-2
  - gei-17
  - PIAS1
  - Su(var)2-10
  - statA
  - statC
  - JAK1
manifest:
  artifacts:
    - href: https://claude.ai/artifact/4MLfbbbWWnLchDvspwdPuM
      title: Brief for GO and PAINT
      description: AI generated
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
2. **Captures proposed new taxon constraints** in a machine-readable YAML file
   ([proposed_taxon_constraints.yaml](TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.yaml)),
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
| STAT (PTHR11801) | PTN000927860 | GO:0007259 cell surface receptor signaling pathway via JAK-STAT | sta-1 | REMOVE |

The same STAT node also carries `GO:0006952` defense response, which reaches STA-1
with the wrong sign: STA-1 represses antiviral genes (IBA_REVIEW section 9).

### What the family reviews show

The two family reviews explain *why* every one of these annotations arrives, and
why a taxon constraint rather than a PAINT edit is the durable fix:

- **JAK (PTHR45807)** is an animal-only family. PANTHER roots it at Eumetazoa, and
  the tree has no nematode, amoebozoan, fungal or plant leaf. No JAK-STAT term
  reaches a JAK-less organism from this family.
- **STAT (PTHR11801)** is much older. Its JAK-STAT, defense response and
  proliferation IBDs sit on **PTN000927860, the Unikonts node**, which spans the
  Dictyostelium STATs as well as all animals. The family review rates the
  JAK-STAT row `TOO_DEEP`: the seeds support only Bilateria (PTN000210449).
- So the term is placed where the *STAT* family arose, while the pathway it names
  arose with the *JAK* family, much later. Any lineage that kept STATs but never had
  JAKs inherits it. That mismatch is structural, which is why it recurs across worms
  and slime moulds and why a constraint on the term catches all of it at once.

The STAT review also found the reverse case at the family root: plant STAT-like
proteins (Arabidopsis SHA/SHB) lack the STAT DNA-binding domain yet inherit the
root's DNA-binding transcription factor IBDs; they are recorded there as member
exceptions.

## Case study 2: STAT without JAK in *Dictyostelium*

*Dictyostelium* has four STATs (dstA–D) and no JAK; STATc is tyrosine phosphorylated
by the TKL kinase Pyk2 instead.

> "There are no orthologs of the animal tyrosine kinases" — PMID:22699506

The statA and statC reviews already MODIFY the inherited `GO:0007259` IBA to
`GO:0097696` cell surface receptor signaling pathway via STAT, which presupposes no
JAK and is the right term for both the slime-mould and the worm STATs.

The PIAS case is also where the repository gained **member exceptions** in family
reviews: PANTHER subfamily PTHR10782:SF94 holds both the fly PIAS (a genuine JAK-STAT
regulator) and worm GEI-17, so no subfamily-level scope can separate them. See
`interpro/panther/PTHR10782/PTHR10782-review.yaml`.

## Proposed taxon constraints

See [proposed_taxon_constraints.yaml](TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.yaml).
Each proposal records the GO term, the constraint (`never_in_taxon` / `only_in_taxon`),
the taxon, any constraint GO already has, verbatim evidence, the annotations it would
block, any it would wrongly block, a status (PROPOSED / SUBMITTED / ACCEPTED /
REJECTED), and where in this repo the case was found.

### Current proposals

| ID | Term | Constraint | Taxon | Blocks | Caveat |
|---|---|---|---|---|---|
| TPV-001 | GO:0007259 cell surface receptor signaling pathway via JAK-STAT | never_in_taxon | Nematoda (fallback *Caenorhabditis*) | worm STAT IBAs from PTN000927860 | direct evidence is for *C. elegans* |
| TPV-002 | GO:0046425 regulation of receptor signaling pathway via JAK-STAT | never_in_taxon | Nematoda (fallback *Caenorhabditis*) | gei-17 and nematode PIAS/PTPN2 IBAs, ~100 IEAs | stated separately in case constraints do not propagate over regulates |
| TPV-003 | GO:0007259 cell surface receptor signaling pathway via JAK-STAT | only_in_taxon | Metazoa (fallback: never in Dictyostelia) | Dictyostelium STAT IBAs; non-animal IEAs | ontology prerequisite (see YAML) |

GO has no taxon constraint on any of these terms today (checked in QuickGO and OLS).

TPV-003 has an ontology prerequisite (re-parenting GO:0007260), recorded in its
`prerequisites` entry in the YAML; not yet requested.

## Candidate cases to scope next

- **TYK2 IRD.** PAINT records TYK2 as having *lost* JAK-STAT signaling (a negated IRD
  on PTN002910252); the JAK family review rates this `WRONG_NODE`, contradicted by
  TYK2's own experimental annotations. Not a taxon question, but the same
  machinery misfiring in the opposite direction.
- Other pathways named for a component with a patchy distribution, collected as they
  surface in IBA and family reviews.

## Key literature

Reviews that frame the JAK-STAT case:

- Liongue et al. 2013, *Evolution of the JAK-STAT pathway* (PMID:24058787). Where
  JAKs and STATs arose; the main source for TPV-003.
- Wang & Levy 2012, *Comparative evolutionary genomics of the STAT family of
  transcription factors* (PMID:24058748). STATs across eukaryotes, including amoebae
  and nematodes.
- Kawata 2011, *STAT signaling in Dictyostelium development* (PMID:21534947). STAT
  activation in a lineage without JAK.
- Taffoni & Pujol 2015, *Mechanisms of innate immunity in C. elegans epidermis*
  (PMID:26716073). Context for the STA-2 pathway.

Primary evidence of JAK absence: Tanguy et al. 2017 (PMID:28874466) for *C. elegans*;
Goldberg et al. 2006 (PMID:16596165) and Araki et al. 2012 (PMID:22699506) for
*Dictyostelium*.

## Related

- [IBA_REVIEW](IBA_REVIEW.md) — section 14, lineage-inappropriate transfer
- [GENOME_WIDE_VALIDATION](GENOME_WIDE_VALIDATION.md) — reuses GO taxon constraints as
  a consistency check
- [PAINT](PAINT.md) — family reviews and node assessments
