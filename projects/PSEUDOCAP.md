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
seed, so the IBD rests entirely on the PseudoCAP row. Of the first six sole-seeded node terms reviewed, two rest on an indirect
mutant phenotype and are unsupported (estA: lipid biosynthesis on an esterase,
960 leaf IBAs; ccmC: catalase activity on a heme exporter, 143), one rests on a
sequence motif coded as IDA (fleN), and three seeds are sound, two of them on
nodes that are too broad or too dependent on them (pvdE, pqsH).

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

## Results so far

Verdicts on the PseudoCAP seed and on the IBD it feeds. "Defects" are the
`source_defects` recorded in the review (P = PseudoCAP, G = GO_CENTRAL/PAINT).

| Rank | Gene | Locus | Sole-seeded node term (PTN) | Leaf IBAs | Seed verdict | IBD verdict | Defects |
|---:|---|---|---|---:|---|---|---|
| 1 | estA | PA5112 | lipid biosynthetic process (PTN005219546) | 960 | INDIRECT-PHENOTYPE: a deletion makes less rhamnolipid; EstA is an outer-membrane esterase, the synthesis steps are RhlA/B/C | Unsupported: withdraw this IBD (the node's esterase IBD is sound) | P (x3), G, UniProt |
| 2 | pqsH | PA2587 | monooxygenase activity (PTN008173107) | 297 | SOUND, under-specific (should be GO:0102164 HHQ monooxygenase) | Sound at family root; ~294 plant leaves rest on this one bacterial seed | P |
| 3 | lap | PA2939 | proteolysis (PTN000254534) | 272 | SOUND (purified enzyme) | Sound | none on seed; 2 P on T2SS/Sec cargo rows |
| 4 | fleN | PA1454 | ATP binding (PTN000344128) | 149 | WRONG evidence code: IDA for a sequence motif | Term true (later structures), needs a real seed | P, G |
| 5 | PA5458 | PA5458 | lipopolysaccharide biosynthetic process (PTN000546841); polysaccharide biosynthetic process (PTN000546715) | 31 + 113 | SOUND but general (O-antigen modification; one row IDA without an assay) | Both wrong for clade: 15/31 leaves in non-LPS organisms (OatA peptidoglycan O-acetyltransferases); 109/113 leaves eukaryotic | P, G (x2) |
| 6 | ccmC | PA1477 | catalase activity (PTN001247822) | 143 | INDIRECT-PHENOTYPE, and cites an *E. coli* paper | Unsupported: drop catalase from the node | P (x7), G |
| 7 | pvdE | PA2397 | ATPase-coupled transmembrane transporter activity (PTN000656738) | 140 | SOUND | Node too deep: 126 of 140 leaves are NBD-only proteins | G (planned) |
| 8 | PA1024 | PA1024 | oxidoreductase activity (PTN002844975) | 122 | SOUND (purified enzyme) | Sound; generic term right for a clade with one characterised member | none on seed; InterPro2GO NMO mapping removed |

pvdE's review file is still a stub: the research, notes and bioinformatics
are done, but the agent's write of the review YAML was blocked and needs
redoing.

Batch 2 (in progress): hutI, hutH, phzS, phzM, pilB, pilU.
Batch 3 (in progress): braF, braD, PA3760, wbpD, wbpY, waaL, xcpX, PA0692,
PA3891, PA5377.

### Patterns emerging

- **Indirect phenotypes as functions** (ccmC, estA): a mutant lacking catalase
  activity because it cannot mature heme proteins was annotated as having
  catalase activity, and PAINT used it as the only seed of a catalase node.
  An esterase whose deletion lowers rhamnolipid output was annotated to
  glycolipid and lipid biosynthesis, and seeds a 960-leaf lipid biosynthesis IBD.
- **Inflated evidence codes** (fleN): IDA on a paper that reports a sequence
  motif.
- **Mis-keyed references** (ccmC; pilB and pilU are being checked): the cited
  PMID is a different paper from the one the phenotypes come from.
- **Cargo annotated as machinery** (lap): a secreted enzyme given secretion
  system process terms.
- **Sound seeds on nodes that are too broad** (pvdE, pqsH, PA5458): the
  PseudoCAP row is right, but the node carries the term to proteins that are a
  different kind of thing (soluble ATPase subunits given a transmembrane
  transporter activity), to lineages without the process (LPS biosynthesis on
  Gram-positive peptidoglycan O-acetyltransferases), or rests a large clade on a
  single seed.

These are catalogued for PAINT as pattern 16 of [IBA_REVIEW](IBA_REVIEW.md).

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
