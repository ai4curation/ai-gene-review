---
title: "Cell Surface and Cell Cortex: What the Annotations Say the Terms Mean"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, rat, DROME, DICDI]
collections: [GO_TRACKER_BACKLOG]
index_group: GO_TRACKER_BACKLOG
---

# Cell Surface and Cell Cortex: What the Annotations Say the Terms Mean

**Bottom line:** Two GO tracker issues ask for better definitions of two
cell-periphery cellular-component terms: GO:0009986 *cell surface* (opened
2018) and GO:0005938 *cell cortex* (opened 2022). Neither has reached a
decision. For cell surface, an editor posted a draft on 2026-10-28 to
redefine the term as the surface-exposed part of the cell (the
"surfaceome"). Nobody has replied. For cell cortex, most respondents prefer
the current broad definition. Both questions turn on usage, and this repo
has a lot of it. Cell surface has 523 rows on 289 reviewed genes, and cell
cortex has 168 rows on 119 genes. Reviews already disagree on the same
patterns the threads raise: cytosolic adaptors on "cell surface", moonlighting
chaperones and enzymes at the surface, kinases transiently at the cortex. A
classification by topology and evidence type is the evidence both
definitions need. Scoped, not started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#14909](https://github.com/geneontology/go-ontology/issues/14909) | 2018-01-23 | improve the definition of GO:0009986 cell surface | 2026-10-28 (unanswered proposal) |
| [go-ontology#23429](https://github.com/geneontology/go-ontology/issues/23429) | 2022-05-31 | improve the definition of GO:0005938 cell cortex | 2026-01-20 |

Thread summaries are as of 2026-11-16, and term states are from a
go-ontology checkout of 2026-11-12. Nothing has been posted to either issue.

## Cell surface (#14909)

**Definition now:** "The external part of the cell wall and/or plasma
membrane." The term is is_a GO:0110165 with no part_of cell periphery, and
GO:0009897 *external side of plasma membrane* is part_of it.

**Positions:**

- A fungal curator wanted a way to group everything outside the cell: "For
  fungi, we need a way to group everything which is on the *outside* of the
  cell." (2018-01-25)
- Another curator held that FACS or non-permeabilized antibody staining
  justifies cell surface even for transmembrane receptors.
- A third wanted the most specific topology term, with a fallback: "If the
  curator cannot tell which term/parent term, to use then they should fall
  back to “plasma membrane” rather than using a term that captures the limits
  of the assay." (2018-03-09)
- The 2026-10-28 draft proposes a surfaceome-style definition, part_of
  GO:0071944 cell periphery, no new fungal grouping term, and obsoleting
  unused children.

That draft lines up with this repo's [SURFACEOME](SURFACEOME.md) project,
which already compares GO cell-surface annotation with an experimental
surfaceome benchmark. It found that GO includes surface-bound secreted
ligands (F2, TF, VEGFA) that the benchmark excludes.

## Cell cortex (#23429)

**Definition now:** "The region of a cell that lies just beneath the plasma
membrane and often, but not always, contains a network of actin filaments and
associated proteins." It is logically defined as cytoplasm part_of cell
periphery.

**Positions:**

- The opening proposal was to make the cortex the membrane-associated actin
  cytoskeleton.
- dictyBase agreed.
- PomBase objected that in fission yeast actin occupies only two cortical
  sites and that cortical ER is part of the cortex.
- WormBase proposed an actomyosin definition.
- TAIR noted plant usage centres on microtubules.

The last comment (2026-01-20) asks: "Is there a pressing need to change it?"
The overlap with GO:0030863 cortical cytoskeleton and GO:0030864 cortical
actin cytoskeleton is unresolved.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0009986 cell surface | 523 | 289 | 345 | 130 | 18 | 5 | 3 | 5 | NEW 11, NOT UNDECIDED 1, PENDING 1, TOO_GENERAL 4 | 72 |
| GO:0009897 external side of plasma membrane | 199 | 138 | 151 | 33 | 0 | 1 | 2 | 2 | NEW 10 | 73 |
| GO:0010339 external side of cell wall | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0005938 cell cortex | 168 | 119 | 98 | 51 | 3 | 4 | 0 | 10 | NEW 2 | 45 |
| GO:0030863 cortical cytoskeleton | 9 | 9 | 5 | 2 | 0 | 0 | 0 | 1 | PENDING 1 | 2 |
| GO:0030864 cortical actin cytoskeleton | 14 | 13 | 6 | 6 | 0 | 1 | 0 | 1 |  | 3 |
| GO:0032541 cortical endoplasmic reticulum | 14 | 11 | 12 | 2 | 0 | 0 | 0 | 0 |  | 3 |

Cell surface genes are mostly human (196 of 289). Cell cortex is more
spread out: 50 human, 23 fly, 8 each for Dictyostelium, worm and rat.

What stands out:

- **Cytosolic proteins on "cell surface".** The MODIFY rows include the TLR
  adaptors MYD88, TIRAP, IRAK1 and IRAK4, and FERMT2. These are cytoplasmic
  proteins recruited to receptors, the "limits of the assay" case.
- **Moonlighting proteins.** Chaperones and enzymes at the surface (HSPD1,
  PDIA4, MYCTU DnaK and GroEL2) are kept as non-core. Enolase (METEA, PSEPK)
  and talin are marked over-annotated. A surfaceome definition has to say
  whether these count.
- **Signaling proteins in the cortex.** Kinases and small GTPases (ARATH MPK3
  and MPK6, AKT1, AKT2, DICDI RasG and Pten, DROME Cdc42) carry the cortex
  term. MPK6, RasG, Pten and Cdc42 are ACCEPT, MPK3 and AKT2 are kept as
  non-core, and AKT1, DROME Akt1, FGFR2, TRAF2 and PSEN1 are UNDECIDED. These are recruitment events, not actin-cortex membership: an
  actin-only definition would exclude them, the current one does not.

## What gene review can and cannot settle

- **Can settle, per gene:** the topology of each annotated product
  (transmembrane, GPI-anchored, peripheral outside, peripheral inside,
  secreted and bound back, cytosolic) and the assay behind the row. Topology
  comes from UniProt features and the cited papers. That gives the
  composition of the term's actual usage, which is the evidence the
  2026-10-28 proposal needs.
- **Can settle, per gene:** for cortex rows, whether the product is an
  actin-cortex component, a cortical ER or patch protein, or a transiently
  recruited signaling protein.
- **Cannot settle:** the definitions themselves. Those are editor decisions,
  and the fungal "everything outside the cell" use case is outside this
  repo's coverage.

## Plan

- [ ] Classify the 289 cell-surface genes by topology, using UniProt
      topology features and signal peptides from the cached records plus
      review text. Reuse the [SURFACEOME](SURFACEOME.md) scripts where they
      fit.
- [ ] Re-check the cytosolic-adaptor MODIFY rows for consistency. What did
      each review replace cell surface with?
- [ ] Classify the 119 cell-cortex genes as actin cortex, other cortical
      structure, or recruited signaling protein.
- [ ] Summarise both breakdowns as a short note for the issue owners.
      Posting it is the project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No analysis started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Both
  threads read in full.
- GO:0005938's term_tracker_item points to
  [go-ontology#26298](https://github.com/geneontology/go-ontology/issues/26298),
  a clathrin-adaptor ticket. The origin of its current logical definition is
  unclear.
