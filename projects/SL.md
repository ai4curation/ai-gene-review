---
title: "UniProt Subcellular Locations (SL) Unique Terms Project"
maturity: SCOPING
tags: [PIPELINE]
species: [human, mouse, yeast, SCHPO, worm, DICDI]
---

# UniProt Subcellular Locations (SL) Unique Terms Project

## Overview

The localization counterpart to [SPKW](SPKW.md). Where SPKW reviewed GO annotations derived
solely from UniProt **keywords** (`GO_REF:0000043`), this project reviews annotations derived
solely from UniProt **subcellular locations** (`GO_REF:0000044`) — SL-xxxx identifiers mapped
to GO cellular-component terms, with no corroborating experimental, phylogenetic, or curator
evidence behind them.

Two things make this worth a project of its own rather than a subproject of SPKW.

**It is still running.** GOA retired the SPKW pipeline for cellular organisms around April
2026, which closed that problem at the source. `GO_REF:0000044` is live and is one of the
largest single sources of CC annotation in GOA.

**The source identifier is in the data.** SPKW's methodology had to reverse-map GO terms to
their originating keywords through the external2go `keyword2go` file, because the GAF records
only the GO term. The SL pipeline writes `UniProtKB-SubCell:SL-xxxx` straight into the
WITH/FROM column. The location-level view that took SPKW a separate mapping step is available
for free, per annotation.

## Key finding: the failure is granularity, not truth

Across 1,297 reviewed SL-unique annotations in this corpus (986 gene folders), **40% were
downgraded or worse** and **9% carry a hard issue** (`REMOVE` / `MARK_AS_OVER_ANNOTATED` /
`MODIFY`). But the issue rate is not spread evenly, and the pattern is sharp:

| SL location | Reviewed | Issue rate | | SL location | Reviewed | Issue rate |
|---|---|---|---|---|---|---|
| SL-0171 Mitochondrion membrane | 13 | **31%** | | SL-0097 ER membrane | 36 | **0%** |
| SL-0066 Cilium | 12 | **25%** | | SL-0134 Golgi apparatus membrane | 21 | **0%** |
| SL-0162 Membrane | 61 | **23%** | | SL-0151 Late endosome membrane | 18 | **0%** |
| SL-0147 Endomembrane system | 10 | **20%** | | SL-0071 Clathrin-coated vesicle membrane | 18 | **0%** |
| SL-0090 Cytoskeleton | 59 | **17%** | | SL-0091 Cytosol | 13 | **0%** |
| SL-0132 Golgi apparatus | 23 | **17%** | | SL-0158 Lysosome | 10 | **0%** |
| SL-0243 Secreted | 89 | **15%** | | SL-0182 Nucleus membrane | 10 | **0%** |

The cleanest demonstration is within a single organelle:

| SL location | Reviewed | Issue rate |
|---|---|---|
| SL-0171 Mitochondrion **membrane** | 13 | 31% |
| SL-0168 Mitochondrion **inner** membrane | 19 | 11% |
| SL-0170 Mitochondrion **matrix** | 14 | 7% |

Same organelle, same pipeline, same curators. The under-specified location is three to four
times worse. The pattern repeats for Golgi apparatus (17%) versus Golgi apparatus membrane
(0%), endoplasmic reticulum (10%) versus ER membrane (0%), and bare Membrane (23%) versus
every specific membrane in the table (0%).

**This is a different failure mode from SPKW.** SPKW's problems were semantic — process
conflation, regulatory conflation, expression mistaken for function. The gene was in the wrong
place in a pathway. SL's problem is that an under-specified location maps to a GO term that is
*true but uninformative*, and reviewers then have to adjudicate whether "true but
uninformative" counts as over-annotation. Hence the unusually high `KEEP_AS_NON_CORE` share
(406 of 1,297, 31%) alongside a modest hard-issue rate.

Full tables and the query in [SL-METHODOLOGY.md](SL/SL-METHODOLOGY.md), regenerable from a
committed script.

## Subprojects

| Subproject | SL | Genes | Status |
|---|---|---|---|
| [SL-0221 / phagophore assembly site membrane](CONDENSATES/GO_0034045-annotation-audit.md) | SL-0221 | 11 reviewed, 18 annotations moved | audit complete, feeding GO issue #29437 |

### SL-0221: a third failure mode

`SL-0221 Preautophagosomal structure membrane` → `GO:0034045` is neither a semantic error nor
a granularity error. **The target GO term is logically defective**: it asserts via
`bounding_layer_of` that a membrane bounds the phagophore assembly site, which is a protein
condensate with no bounding bilayer.

This case is documented in full in the
[GO:0034045 corpus slice audit](CONDENSATES/GO_0034045-annotation-audit.md), shared with the
[CONDENSATES](CONDENSATES.md) project. Its lessons for SL generally:

- **UniProt's own hierarchy is not the problem.** SL-0221 is `partOf` the endomembrane system,
  never `partOf` SL-0220 (the PAS itself). The containment that creates the contradiction is
  GO's addition, not UniProt's.
- **The mapping amplifies whatever it is given.** SL-0221 drives ~801 IEAs under
  `GO_REF:0000044`, plus everything derived from it via Ensembl projection
  (`GO_REF:0000107`), ARBA (`GO_REF:0000117`) and TreeGrafter (`GO_REF:0000118`). This corpus
  holds both ends of one such chain: human RAB7A's annotation is a projection of mouse Rab7a's.
- **SL-unique annotations are where the mapping is unchecked.** Every one of the 23 previously
  reviewed GO:0034045/GO:0097632 assertions in this corpus had been `ACCEPT`ed. Re-reviewed
  against the ontology defect, 18 of 29 moved to `MODIFY`.

## Proposed next subprojects

Chosen from the issue-rate table, highest first:

1. **SL-0162 Membrane → GO:0016020** (61 reviewed, 23% issue, 14 flagged). The largest
   under-specified location. Likely to expose whether "membrane" ever adds information over
   the specific compartment terms a gene already carries.
2. **SL-0171 Mitochondrion membrane** (31%) against its specific siblings SL-0168 / SL-0170.
   A controlled test of the granularity hypothesis inside one organelle.
3. **SL-0090 Cytoskeleton → GO:0005856** (59 reviewed, 17%). Suspected to conflate "binds or
   regulates the cytoskeleton" with "is a cytoskeletal component" — the SL analogue of SPKW's
   regulatory conflation, and the one place the two projects' failure modes may meet.
4. **SL-0243 Secreted → GO:0005576** (89 reviewed, 15%). Largest location outside the
   generic ones; worth checking whether signal-peptide-driven predictions dominate.

## Open questions

- Is `KEEP_AS_NON_CORE` the right disposition for a true-but-uninformative location, or should
  the project argue for a distinct verdict? A third of all SL-unique annotations land there.
- Should GOA suppress an SL-derived CC annotation when the gene already carries a more
  specific descendant from any source? That single rule would address most of the granularity
  cases without touching UniProt.
- How many SL locations map to GO terms whose logical axioms do not hold for the structure the
  location names? SL-0221 was found by accident. There is no systematic check.
- Does the issue rate hold outside this corpus? These 986 genes were selected for review for
  other reasons and are not a random sample of GOA.

## Project status

- **Started**: 2026-08-08
- **Corpus scan**: 1,300 SL-unique annotations, 986 gene folders, 1,297 with reviews
- **Genes reviewed under this project**: 11 (all SL-0221)
- **Script**: `projects/SL/scripts/scan_sl_unique.py`
