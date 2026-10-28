---
title: "PseudoCAP annotation review: P. aeruginosa seeds of PAINT IBAs"
collections: [HOMOLOGY_PROPAGATION]
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEAE]
genes: [ccmC, estA, pqsH, lap, fleN, pvdE]
---

# PseudoCAP annotation review: P. aeruginosa seeds of PAINT IBAs

**Bottom line:** PseudoCAP, the community annotation group of the
*Pseudomonas* Genome Database, made most of the experimental GO annotations on
*Pseudomonas aeruginosa* PAO1 (1,841 of 2,941 experimental rows in QuickGO).
Some of those rows are used by PAINT curators as seeds for ancestral-node (IBD)
annotations, which then reach thousands of bacterial proteins as IBAs. This
project reviews PseudoCAP annotations, starting with the ones that seed IBDs,
because an error there is copied to every descendant leaf. Of 471 PAO1
proteins that seed an IBD, 398 have a PseudoCAP annotation that supports at
least one of their seedings; those 522 node terms feed 51,455 leaf IBAs. For
139 node terms (109 proteins, 4,772 leaf IBAs) the PAO1 protein is the only
seed, so the IBD rests entirely on the PseudoCAP row. A pilot of six such genes
is under way.

## Why start with IBA seeds

An IBA is a projection of an IBD made at a PANTHER tree node (see
[IBA_REVIEW](IBA_REVIEW.md)). PAINT curators place the IBD after reading the
experimental annotations of the node's descendants, so a seed annotation is
load-bearing in a way an ordinary experimental row is not. Two features of the
PseudoCAP corpus make the seeds worth checking first:

- **Mutant phenotypes as functions.** Half of the PseudoCAP rows that support a
  seeding are IMP (291 IMP, 300 IDA, 15 EXP, 4 IEP). A mutant phenotype can be
  an indirect effect: the clearest case found so far is `ccmC`, a cytochrome c
  maturation heme exporter whose IMP `catalase activity` row (PMID:16824107) is
  the only seed of a catalase IBD propagating to 143 leaves, including back onto
  `ccmC` itself. Overall, 71 molecular-function node terms are supported only
  by IMP or IGI from PAO1 (8,129 leaf IBAs), and 14 of them are sole-seeded.
  Many of these are probably sound (sigma factor, TonB-dependent siderophore
  receptor activity inferred from mutants in well-understood families), but
  each needs a look.
- **Sole seeds.** When the PAO1 protein is the only seed, there is no second
  line of evidence for the curator's node call.

## Data and method

The worklist is built by
[`build_iba_seed_worklist.py`](PSEUDOCAP/build_iba_seed_worklist.py) and
written to [`iba_seed_worklist.yaml`](PSEUDOCAP/iba_seed_worklist.yaml)
(generated 2026-10-28). It downloads, into the git-ignored `.cache/paint/`:

- PANTHER PAINT `IBD.gaf` (node annotations with their seed lists) and the leaf
  IBA file `gene_association.paint_uniprot.gaf.gz`;
- the PAO1 proteome (UniProt, taxon 208964, 5,583 entries);
- all PAO1 experimental annotations from QuickGO (ECO:0000269 and ECO:0000006
  descendants);
- `go-basic.obo` (release 2026-07-26).

A PAO1 protein *seeds* a node term when it is listed in that IBD row's WITH
column. A seeding is *PseudoCAP-supported* when one of the protein's
non-negated experimental annotations, assigned by PseudoCAP, is the node term
or an is_a/part_of descendant of it. Every PAO1 seeding found at least one
supporting experimental annotation, which is a useful check on the join.
Leaf IBAs are counted per node and term from the leaf IBA file.

Ranking: **tier 1** genes are the only seed of at least one node term;
**tier 2** genes share every node with other seeds. Within a tier, genes are
ordered by the leaf IBAs that hang on their sole-seeded nodes, then by total
leaf IBAs.

| | Count |
|---|---:|
| PAO1 proteins seeding an IBD | 471 |
| PAO1 node-term seedings | 663 |
| Proteins with a PseudoCAP-supported seeding | 398 |
| PseudoCAP-supported seedings | 522 |
| of which sole-seeded (tier 1 node terms) | 139 |
| Tier 1 proteins | 109 |
| Tier 2 proteins | 289 |
| Leaf IBAs downstream of PseudoCAP-supported seedings | 51,455 |
| Leaf IBAs downstream of sole-seeded ones | 4,772 |
| Worklist genes already reviewed before this project | 5 (cysH, pqsC, alg8, wzm/Q9HTB8, pvdH) |

## Per-gene review protocol

Each gene gets a full review (all GOA rows, core functions, notes). On top of
that, the notes file carries a `## PseudoCAP IBA-seed assessment` table with,
for every seeding node: the PTN node, node term, number of seeds, leaf IBAs,
the seed annotation, and a verdict:

- `SOUND`: the paper directly shows the node term (or a descendant).
- `OVER-SPECIFIC`: the seed is right but the node term is more specific than
  the clade can carry, or vice versa.
- `INDIRECT-PHENOTYPE`: the seed is a downstream mutant phenotype, not the
  gene's own activity or process.
- `WRONG`: the paper does not support the row.
- `UNVERIFIABLE`: the paper cannot be read (abstract-only, no full text).

Errors in a PseudoCAP row are recorded as `review.source_defects` with
`resource: PSEUDOCAP` (added to `SourceResourceEnum` for this project). When a
wrong seed leaves the IBD unsupported, a second defect with
`resource: GO_CENTRAL` names the PTN node, so `just export-source-defects`
produces one report for PseudoCAP and one for PAINT.

## Pilot batch (tier 1, ranks 1-7)

| Rank | Gene | Locus | Sole-seeded node term | Leaf IBAs | Seed row | Status |
|---:|---|---|---|---:|---|---|
| 1 | estA | PA5112 | lipid biosynthetic process | 960 | IMP PMID:17631636 (glycolipid biosynthetic process; UniProt also IMP) | in progress |
| 2 | pqsH | PA2587 | monooxygenase activity | 297 | IDA PMID:20662781 | in progress |
| 3 | lap | PA2939 | proteolysis | 272 | IDA PMID:11533066 | in progress |
| 4 | fleN | PA1454 | ATP binding | 149 | IDA PMID:10629180 | in progress |
| 6 | ccmC | PA1477 | catalase activity | 143 | IMP PMID:16824107 | in progress |
| 7 | pvdE | PA2397 | ATPase-coupled transmembrane transporter activity | 140 | IMP PMID:19787431 | in progress |

Rank 5 (PA5458) is deferred to the next batch.

## Plan

1. Finish the pilot and record verdicts here.
2. Work through the remaining tier 1 genes (103) in batches, in worklist order.
3. Tier 2, starting with seedings whose only PAO1 support is IMP or IGI.
4. Then the rest of the PseudoCAP corpus (2,069 rows on PAO1 in QuickGO),
   prioritising IMP rows on molecular-function terms.
5. Export source defects for PseudoCAP and PAINT, and summarise the recurring
   patterns for both groups.

Re-run the builder when PAINT or QuickGO data change; it only re-downloads
files missing from `.cache/paint/`, so delete that folder to refresh.
