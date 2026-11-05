---
title: "PANTHER/TreeGrafter: a reductase annotated as a dehydrogenase, times 1,387"
---

# PANTHER/TreeGrafter: a reductase annotated as a dehydrogenase, times 1,387

Back to the [project page](../CACAO.md). Reproduce with
`uv run python projects/CACAO/scripts/upstream_checks.py`.

Found while reviewing the CACAO annotations on *Myxococcus xanthus*
[actC](../../genes/MYXXA/actC/actC-ai-review.yaml), whose three CACAO rows were
accepted or refined. The defective row on that gene was not CACAO's: actC
carries `GO:0004029` aldehyde dehydrogenase (NAD+) activity by IEA from
TreeGrafter, and actC has no aldehyde dehydrogenase fold at all.

Tracing it back produced a two-stage error with a single origin.

## Stage 1: the seed annotation states the wrong reaction

`Q12177` (YLL056C, *S. cerevisiae*, "Uncharacterized protein YLL056C") carries:

```
GO:0004029  IDA  PMID:28265724   SGD
GO:0004029  IBA  GO_REF:0000033  GO_Central   WITH/FROM: PTN002449572|SGD:S000003979
GO:0005737  IDA  PMID:28265724   SGD
GO:0005737  IBA  GO_REF:0000033  GO_Central
GO:0008150  ND   GO_REF:0000015  SGD
```

The cited paper is titled "YLL056C from *Saccharomyces cerevisiae* encodes a
novel protein with aldehyde **reductase** activity", and its abstract states:

> Enzyme activity assays showed that Yll056cp is not a quinone or ketone
> reductase but an NADH-dependent aldehyde reductase, which can reduce at least
> seven aldehyde compounds.

`GO:0004029` aldehyde dehydrogenase (NAD+) activity is defined as:

> Catalysis of the reaction: an aldehyde + H2O + NAD+ = a carboxylate + 2 H+ +
> NADH.

These are not two granularities of one claim. The paper's enzyme **reduces** an
aldehyde to an alcohol; `GO:0004029` **oxidises** an aldehyde to a carboxylic
acid. Different direction, different product, different EC class (1.1.1.x
against 1.2.1.3). The paper also places the protein in the *atypical* SDR
group, and `Q12177` carries Pfam `PF01370`, the NAD-dependent
epimerase/dehydratase family — not the ALDH superfamily fold.

The reaction the paper reports, written in GO's oxidative direction, is
`GO:0004022` alcohol dehydrogenase (NAD+) activity ("an alcohol + NAD+ = an
aldehyde or ketone + NADH + H+") or its parent `GO:0018455`. The substrate
range given (glycolaldehyde best by Vmax/Kcat, formaldehyde by Km, plus
furfural, butyraldehyde and propylaldehyde) is broad, so a curator may prefer
the parent.

The `GO:0005737` cytosol/cytoplasm half of the pair is fine — the abstract does
say the protein "localized to the cytoplasm".

## Stage 2: two pipelines amplify it

| Route | Node | Rows |
|---|---|---|
| PAINT (IBA, `GO_REF:0000033`) | `PTN002449572` | 63 |
| TreeGrafter (IEA, `GO_REF:0000118`) | `PTN005180820` | 1,324 (+1,324 cytoplasm) |

**1,387 `GO:0004029` rows across 1,277 taxa trace to that one IDA.**

The recipients are `PTHR48079` — InterPro's integrated name for it is
"NAD(P)-dependent Metabolic Enzyme" (`IPR051783`), its representative structure
is a "putative NAD-dependent epimerase/dehydratase", and its members carry
`PF01370` or `PF13460`. Spot-checking them returns dTDP-glucose 4,6-dehydratase
(rmlB), GDP-fucose synthase (wcaG), GDP-mannose 4,6-dehydratase (gca),
sterol-4alpha-carboxylate 3-dehydrogenase, wbpK, and many copies of *E. coli*
YeeZ. These are extended-SDR Rossmann enzymes. None of them is an aldehyde
dehydrogenase.

The seed sits in subfamily `PTHR48079:SF9` ("PUTATIVE-RELATED"); the recipients
are overwhelmingly `PTHR48079:SF6` ("NAD(P)-BINDING DOMAIN-CONTAINING
PROTEIN-RELATED"). So the assertion is attached at a node ancestral to both
subfamilies and propagates across the family from one member of a different
subfamily.

## Why this is not a donor-count argument

This repository's own
[IBA guidance](../../CLAUDE.md) warns that a short `WITH/FROM` donor list is not
weak support, and that is right: `PTN002449572` having exactly one donor is not
the complaint. A one-donor node seeded by a well-characterised protein can be
entirely sound.

The complaint is about the **content** of the seed. The node's single donor
carries a term that states the wrong reaction, so every annotation inheriting
from the node inherits that error, and no amount of phylogenetic care at the
node could have caught it — the node placement may well be correct for whatever
`Q12177` actually does. Fixing the propagation therefore means fixing the seed
first.

The contrast with the genuine ALDH clades is worth stating because it shows the
system normally works. `PTN000192666` emits 618 IBA rows for `GO:0004029` from
34 donors including ALDH1A1 (`P00352`), ALDH2 (`P05091`) and ALDH1B1
(`P30837`); `PTN008111916` emits 325 from 12 donors. Those sit in `PTHR11699`,
the real ALDH family. Of the 56 proteins in GOA with an experimental
`GO:0004029` annotation, 29 are in `PTHR11699` and exactly one — `Q12177` — is
in `PTHR48079`.

## Requested changes

**To SGD (the origin, and the only fix that matters).** Re-term `Q12177`'s
`GO:0004029` IDA to `GO:0004022` alcohol dehydrogenase (NAD+) activity, or to
`GO:0018455` if the substrate breadth argues for the parent. The cited paper
supports a reduction, not an oxidation, and says so in its title. Leave the
`GO:0005737` IDA alone.

**To GO Central / PAINT.** Once the seed is re-termed, the IBD at
`PTN002449572` needs the same correction, which clears its 63 IBA rows.

**To PANTHER / UniProt's TreeGrafter pipeline.** The GO association behind
`PTN005180820` needs the same correction, which clears 1,324 rows. Worth asking
separately whether a node spanning `SF6` and `SF9` should be emitting a specific
catalytic activity at all, given that the family's own InterPro description
spans "oxidative decarboxylation, reduction, and dehydration reactions" — a
family-level MF this specific is a strong claim for a group that heterogeneous,
independently of whether this particular term is right.

**Note on `IPR051783`'s description.** InterPro's text for the family is
flagged `is_llm: true`, `is_reviewed_llm: false` in the API response. It is
accurate as far as this review can tell, and it is not the source of this error,
but it is unreviewed machine-generated text being served as a family
description, which is worth knowing when citing it.

## A note for this project's taxonomy

This is the inverse of the shape the batch-3 screens were built to find. The
screens looked for a student mis-reading a paper; here a professional curator
read the paper correctly and chose a term whose label matches the paper's words
("aldehyde ... dehydrogenase"-shaped) but whose definition is the opposite
reaction. Then two automatic pipelines multiplied it by roughly 1,400.

It belongs with the InterPro2GO `GO:0019685` case as the same underlying
failure: **a term chosen from its label while its definition says something
else**, and in both cases the amplification, not the original slip, is what
makes it worth reporting. The original slips are one row each.

## Status

- [ ] Report the re-terming to SGD.
- [ ] Report the IBD correction to GO Central, after the seed is fixed.
- [ ] Report the node association to PANTHER, with the family-heterogeneity
      question.
