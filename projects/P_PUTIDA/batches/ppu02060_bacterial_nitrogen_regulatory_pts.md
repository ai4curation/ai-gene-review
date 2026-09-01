---
title: "PSEPK nitrogen-regulatory PTS phosphorelay"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ptsP, ptsH, ptsN]
autolink_gene_symbols: false
---

# PSEPK nitrogen-regulatory PTS phosphorelay

This batch resolves the regulatory branch of KEGG `ppu02060` separately from
the already curated FruB/FruA fructose-uptake PTS. The reusable module is
`modules/bacterial_nitrogen_regulatory_pts.yaml`.

## Boundary

1. PtsP enzyme I(Ntr) accepts phosphate from PEP.
2. NPr, called `ptsH`/PP_0948 by UniProt and `ptsO` in primary KT2440 studies,
   relays phosphate from PtsP.
3. PtsN EIIA(Ntr) receives phosphate and acts as the terminal
   phosphorylation-state-dependent regulator.

The branch has no sugar permease and does not transport or phosphorylate a
carbohydrate. Conditional phosphate input from FruB is documented cross-talk,
not a required part. PHA accumulation, potassium transport, and central-carbon
effects are downstream regulatory outputs.

## Status

- [x] Define a species-neutral three-part PtsP-NPr-PtsN module.
- [x] Fetch and curate the three KT2440 gene reviews.
- [x] Reconcile the `ptsH` versus `ptsO` naming discrepancy.
- [x] Remove propagated sugar-PTS interpretations from the regulatory proteins.
- [x] Complete OpenScientist module + pathway + taxon research with the full
  7,200-second allowance.
- [x] Complete independent annotation-reviewer and module audit.
- [x] Validate and render the repaired module and selected reviews.

The independent audit confirmed the sugar-PTS removals and corrected the PtsN
regulatory-function coverage. PtsP and PtsN retain verified
nitrogen-regulatory PANTHER subfamilies. NPr instead uses a family selector
grounded by experimentally assigned PSEPK and E. coli representatives but no
PANTHER term, because PANTHER:PTHR33705:SF2 also contains canonical sugar-PTS
HPr proteins.

## Wave135 Annotation-Reviewer Pass

Every selected gene received a fresh annotation-reviewer consultation against
its complete fetched GOA table, the cited publication text, UniProt metadata,
and the coherent PtsP-NPr-PtsN pathway boundary. No annotation remains pending.

| Gene | GOA rows reviewed | Annotation-reviewer outcome |
|---|---:|---|
| `ptsP` | 4/4 | Accept cytoplasm and EI(Ntr) phosphotransferase activity; retain the broad phosphorus-transfer parent as non-core; remove sugar-PTS process; retain the literature-supported protein-phosphorylation proposal. |
| `ptsH` | 4/4 | Accept cytoplasm; retain broad transferase activity as non-core; mark generic kinase activity over-annotated; remove sugar-PTS process; retain phosphorus-transfer and protein-phosphorylation proposals for the NPr carrier role. |
| `ptsN` | 3/3 | Remove carbohydrate phosphotransferase activity and sugar-PTS process; modify kinase activator to direction-neutral kinase regulator activity; retain the separately supported signaling, KdpD/potassium, AceE inhibition, and cytoplasmic proposals. |

The module audit treats the KdpD, AceE, PHA, and fructose cross-talk findings as
PSEPK outputs or optional inputs, not conserved relay parts. The reusable core
contains only phosphate entry through PtsP, transfer through NPr, and the
phosphorylation-state-dependent PtsN regulatory readout.

## OpenScientist Research

The [module + pathway + taxon report](../deep-research/PSEPK__bacterial_nitrogen_regulatory_pts__ppu02060-deep-research-openscientist.md)
completed in 1,026.09 seconds with a 7,200-second timeout allowance. It
independently recovered PP_5145, PP_0948, and PP_0950 as the complete KT2440
PTS(Ntr) relay and classified `fruB`, `fruK`, and `fruA` as KEGG-map overlap
rather than module members. It also supported treating FruB as an optional
cross-talk input rather than a fourth core part.

The provider's suggestion to associate PtsP with GO:0009401 was not adopted.
That term is specifically the phosphoenolpyruvate-dependent **sugar**
phosphotransferase system, whereas PMID:18296519 directly describes this branch
as unrelated to sugar traffic. The annotation-reviewer removals therefore take
precedence over that inconsistent automated recommendation.

## Focused Genes

| Gene | Locus | UniProt | Core role |
|---|---|---|---|
| `ptsP` | PP_5145 | Q88CN5 | PEP-dependent enzyme I(Ntr) |
| `ptsH` (`ptsO`/NPr) | PP_0948 | Q88PA2 | Intermediate phosphocarrier |
| `ptsN` | PP_0950 | Q88PA0 | Terminal EIIA(Ntr) regulator of KdpD and AceE |

PMID:18296519 directly establishes the primary in vivo flow as PEP to PtsP to
NPr to PtsN and describes the branch as unrelated to sugar traffic.
PMID:26224366 establishes direct PtsN-KdpD control of `kdpFABC`, while
PMID:21236318 establishes inhibition of pyruvate dehydrogenase through direct
PtsN-AceE interaction.
