---
title: "PseudoCAP annotation review: P. aeruginosa seeds of PAINT IBAs"
collections: [HOMOLOGY_PROPAGATION]
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEAE]
genes: [braD, braF, ccmC, estA, fleN, hutH, hutI, lap, PA0692, PA1024, PA3760, PA3891, PA5377, PA5458, phzM, phzS, pilB, pilU, pqsH, pvdE, waaL, wbpD, wbpY, xcpX]
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
| 9 | hutI | PA5092 | imidazolonepropionase activity; L-histidine catabolic process (PTN000505272) | 52 | UNVERIFIABLE: 1967 paper predates genes and never mentions step III | Term right for a LUCA node (reaches human AMDHD1), but its only anchor is weak: re-seed | P |
| 10 | phzS | PA4217 | monooxygenase activity (PTN002492679) | 104 | SOUND claim, wrong reference (a crystallization note) | Sound at family root; one misplaced leaf (Synechocystis ChlP) | P |
| 11 | pilB | PA4526 | ATP hydrolysis activity (PTN001250205) | 90 | SOUND (purified ATPase, PMID:18174131) | Sound | P (x2, other rows: wrong reference / evidence code) |
| 12 | phzM | PA4209 | S-adenosylmethionine-dependent methyltransferase activity (PTN002463933) | 80 | SOUND | Sound at family root | none on seed |
| 13 | braF | PA1071 | L-valine/L-isoleucine import, L-alanine transport (PTN000656921) | 75 | SOUND via reconstitution (PMID:1400443); the growth screen alone is weak | Substrate terms stretch across a node of paralogous ATPases whose binding proteins set specificity | none |
| 14 | wbpD | PA3156 | acetyltransferase activity (PTN001917401); UDP-glucuronate biosynthetic process (PTN001292385) | 67 + 8 | Acetyltransferase SOUND; UDP-glucuronate WRONG (WbpD acetylates UDP-GlcNAc3NA, not in UDP-GlcA synthesis) | Acetyltransferase sound; UDP-glucuronate IBD wrong | P, G |
| 15 | xcpX | PA3097 | T2SS complex; protein secretion by T2SS (PTN000475915) | 35 | SOUND; process row is IDA on a review paper | Sound | P |
| 16 | waaL | PA4999 | polysaccharide biosynthetic process (PTN008076295) | 64 | SOUND; seed term arguably the wrong step | Sound; ligase-activity row removed (WaaL is ATP-independent) | P (x6) |
| 17 | PA3891 | PA3891 | plasma membrane (PTN001953445); ABC-type glycine betaine transporter activity (PTN001953060) | 54 | INDIRECT: "IDA" is cross-species complementation of a P. syringae opuCA mutant; substrate data are the ortholog's | Plausible, but should be re-seeded from the characterised ortholog | P (x2), G (x2) |
| 18 | wbpY | PA5448 | lipopolysaccharide biosynthetic process (PTN000749272) | 51 | SOUND | Sound; its shared glycosyltransferase node should be re-seeded from a 2022 direct assay | P, G |
| 19 | PA0692 | PA0692 | type V secretion process and complex (PTN002160772) | 25 | SOUND; complex row is IMP, which cannot show membership | Sound | P |
| 23 | PA3760 | PA3760 | N-acetylglucosamine transport (PTN000532509) | 43 | SOUND for PA3760 | OVER-SPECIFIC: node is general Enzyme I (PtsI, PtsP, FruB) | G |
| 24 | hutH | PA5098 | histidine ammonia-lyase activity; L-histidine catabolic process (PTN000796665) | 42 | SOUND (direct assay of the partially purified enzyme), coded IMP instead of IDA | Sound; but PAO1 paralog PA5093, which lacks the catalytic Ala-Ser-Gly motif, inherits it | P, G (NOT on PA5093) |
| 27 | PA5377 | PA5377 | carnitine transport and transporter activity; choline transport (PTN000766131) | 39 | Choline/betaine SOUND; carnitine OVER-SPECIFIC (needs the separate binding protein CaiX); amine transporter activity WRONG (quaternary ammonium is not an amine in GO) | Carnitine IBDs on the permease node not supported; amine IBD should be repointed | P (x4), G (x3) |
| 30 | braD | PA1073 | L-isoleucine import, L-alanine transport (PTN000765102) | 36 | SOUND (as braF) | Sound, same caveat; D-alanine transport seed is an indirect phenotype | none |
| 39 | pilU | PA0396 | DNA endonuclease activity, producing 5'-phosphomonoesters (PTN000766390) | ~13 | WRONG: GO:0016888 typed for GO:0016887 ATP hydrolysis (same paper and date as pilB) | Unsupported: remove from node | P, G |

pvdE's review file is still a stub: the research, notes and bioinformatics
are done, but the agent's write of the review YAML was blocked and needs
redoing.

Batch 4 (in progress): mgtE, PA1055, PA1057, pilM, pilD, hom, aruC, gbuA,
nrdJa, cif, dgcB.
Batch 5 (in progress): xcpS, xcpW, xcpV, xcpQ, xcpR, pscC, gltA, PA0920,
PA4079, liuC, PA4503, PA4504, PA4624, dctQ, thiI, cifR, lpxA.

### Patterns emerging

- **Indirect phenotypes as functions** (ccmC, estA): a mutant lacking catalase
  activity because it cannot mature heme proteins was annotated as having
  catalase activity, and PAINT used it as the only seed of a catalase node.
  An esterase whose deletion lowers rhamnolipid output was annotated to
  glycolipid and lipid biosynthesis, and seeds a 960-leaf lipid biosynthesis IBD.
- **Inflated evidence codes** (fleN): IDA on a paper that reports a sequence
  motif.
- **Wrong GO id** (pilU): PseudoCAP entered GO:0016888 DNA endonuclease
  activity, the id after GO:0016887 ATP hydrolysis activity, which it gave PilB
  from the same paper on the same day. PAINT then used it as the only seed of
  a node, so a pilus retraction ATPase clade inherits endonuclease activity.
- **Wrong references** (ccmC, phzS): the cited PMID is a different paper
  (*E. coli* CcmABC biochemistry for ccmC; a crystallization note for phzS).
  The pilB/pilU paper looked like a mis-keyed neighbour of the ccmC paper but
  is correct.
- **Evidence codes that overstate the assay** (fleN, xcpX, PA0692, PA5458,
  PA3891): IDA on a sequence motif, a review, or cross-species
  complementation; IMP for complex membership.
- **Subunit and partner conflation** (PA5377): carnitine transport, which
  needs the separate binding protein CaiX, seeded on the permease node.
- **Old papers that predate the gene** (hutI): a 1967 pathway paper cannot tie
  an activity to PA5092. Here the term is right and the node reaches human
  AMDHD1, but its only anchor needs replacing.
- **Wrong pathway** (wbpD): an acetyltransferase of the UDP-ManNAc3NAcA
  pathway annotated to UDP-glucuronate biosynthesis, seeding an 8-leaf IBD.
- **Cargo annotated as machinery** (lap): a secreted enzyme given secretion
  system process terms.
- **Sound seeds on nodes that are too broad** (pvdE, pqsH, PA5458, PA3760): the
  PseudoCAP row is right, but the node carries the term to proteins that are a
  different kind of thing (soluble ATPase subunits given a transmembrane
  transporter activity), to lineages without the process (LPS biosynthesis on
  Gram-positive peptidoglycan O-acetyltransferases), or rests a large clade on a
  single seed. PA3760's N-acetylglucosamine transport seed sits on a general
  PTS Enzyme I node that also holds PtsI and the nitrogen-PTS PtsP.

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
