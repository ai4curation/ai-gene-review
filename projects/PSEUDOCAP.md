---
title: "PseudoCAP annotation review: P. aeruginosa seeds of PAINT IBAs"
collections: [HOMOLOGY_PROPAGATION]
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEAE]
genes: [arcA, arcD, aruC, braD, braF, ccmC, cif, cifR, cysB, dctP, dctQ, dgcB, dksA, eddB, estA, fimU, fleN, fliD, fpr, fur, gbuA, gltA, hfq, hom, hutF, hutH, hutI, lap, lasB, lasI, lhpL, liuC, lpxA, mgtE, motB, mucB, mucD, nirJ, nmoA, nrdJa, oprB, oprG, PA0692, PA0906, PA0920, PA1024, PA1054, PA1055, PA1056, PA1057, PA1058, PA1059, PA1340, PA1341, PA1486, PA2280, PA2580, PA3697, PA3760, PA3891, PA4079, PA4503, PA4504, PA4505, PA4521, PA4624, PA5085, PA5208, PA5359, PA5377, PA5458, pchB, pelA, pfeA, phnB, phzC1, phzM, phzS, pilA, pilB, pilD, pilM, pilN, pilT, pilU, pqsC, pqsH, pscC, pslC, ptrB, pvdE, pvdH, Q9HTB8, relA, tgpA, thiI, thrB, waaL, wbpD, wbpY, xcpQ, xcpR, xcpS, xcpV, xcpW, xcpX, znuC]
---

# PseudoCAP annotation review: P. aeruginosa seeds of PAINT IBAs

**Bottom line:** PseudoCAP, the community annotation group of the
*Pseudomonas* Genome Database, made most of the experimental GO annotations on
*Pseudomonas aeruginosa* PAO1 (1,841 of 2,941 experimental rows in QuickGO).
PAINT curators use some of those rows as seeds for ancestral-node (IBD)
annotations, which reach many other proteins as IBAs, so an error in a seed is
copied to every descendant. Of 471 PAO1 proteins that seed an IBD, 398 have a
PseudoCAP annotation supporting at least one seeding; for 139 node terms (109
proteins) the PAO1 protein is the only seed. We reviewed all 109 of those
proteins; three review files (pvdE, pqsA, PA2403) are still to be written. For 21 genes the seed is wrong or
is an indirect mutant phenotype, and the IBD it supports should be withdrawn or
repointed. Examples are catalase activity on a heme exporter (ccmC), lipid
biosynthesis on an esterase (estA), DNA endonuclease activity from a mistyped
GO id (pilU), and signal transduction on a signal synthase (lasI). For 24 the
seed is right for PAO1 but the node carries the term to proteins or lineages it
does not fit. For 25 the claim is true but the PseudoCAP row looks to misstate the
evidence code, qualifier or reference, and 37 are sound. The reviews record 114
defects for PseudoCAP and 74 for PAINT, written up in
[`PSEUDOCAP/defects/`](PSEUDOCAP/defects/PSEUDOCAP.md).

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
Leaf IBAs are counted per node and term from the leaf IBA file. That file
covers only PANTHER's reference proteomes, so the counts are lower bounds:
GOA also projects IBAs onto the rest of UniProtKB. For three nodes checked in
QuickGO on 2026-10-28 (all terms from the node together), the GOA rows were
925 for PTN001247822 (ccmC; 143 catalase IBAs in the reference file), 1,770 for
PTN005219546 (estA; 960 per term) and 369 for PTN002388087 (PA4079; 27).

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

## Results: tier 1 (sole seeds)

All 109 tier 1 proteins have been assessed; the review files for pvdE, pqsA and
PA2403 still need writing (see below). pvdE is classified from its committed
notes and seed assessment. Each gene is classified by the outcome for
its sole-seeded node terms. Leaf IBA counts are the worklist's
reference-proteome counts for those terms, so they are lower bounds.

| Outcome | Genes | Leaf IBAs |
|---|---:|---:|
| Seed wrong or indirect: the IBD should be withdrawn or repointed | 21 | 1,481 |
| Seed right for PAO1, but the node term does not fit its clade | 24 | 804 |
| Claim true, but the seed row's evidence code, qualifier or reference looks wrong | 25 | 887 |
| Sound | 37 | 1,589 |
| Review not yet written (pqsA, PA2403) | 2 | 11 |
| **Total** | **109** | **4,772** |

- **Withdraw or repoint (21):** estA, ccmC, pilU, pilM, pilN, wbpD, PA0920,
  liuC, PA5377, lasI, PA3697, cysB, ptrB, PA5208, PA1340, lhpL, znuC, phnB,
  pslC, motB, nrdJa.
- **Node does not fit the clade (24):** pvdE, PA5458, PA3760, mgtE, aruC, gbuA,
  mucB, pchB, nirJ, fpr, fur, nmoA, tgpA, dctQ, PA4503, PA4504, pqsC, wzm,
  phzC1, thiI, pelA, xcpV, braF, PA5359.
- **Fix the seed row, keep the IBD (25):** fleN, hutI, hutF, hom, thrB, PA3891,
  the six Sha subunits PA1054-PA1059, PA2280, phzS, lpxA, PA0692, dgcB, PA4521,
  pilA, oprB, PA4505, gltA, arcD, PA2580, fliD.
- **Sound (37):** lap, pqsH, PA1024, pilB, phzM, hutH, braD, waaL, wbpY, cif,
  pilD, pscC, relA, hfq, dksA, cifR, PA4079, PA4624, oprG, pilT, fimU, arcA,
  lasB, PA1486, PA5085, PA0906, dctP, PA1341, mucD, pfeA, pvdH, eddB, and the
  type II secretion genes xcpQ, xcpR, xcpS, xcpW and xcpX. Their process rows
  cite a review (PMID:9818381) as IDA; we have only its abstract, which cannot
  show whether the review reports original data, so this is a SUSPECTED check
  rather than an error.

The classification is by the worst outcome among a gene's sole-seeded nodes;
several "sound" genes still have defects on other rows (for example lap and
lasB, which are given secretion-system terms for being secretion cargo).

### Upstream reports

[`export_pseae_defects.py`](PSEUDOCAP/export_pseae_defects.py) collects the
`source_defects` recorded in all PAO1 reviews into one report per resource in
[`PSEUDOCAP/defects/`](PSEUDOCAP/defects/PSEUDOCAP.md): 114 for PseudoCAP (44
wrong term, 42 wrong evidence code, 19 wrong reference, 8 wrong qualifier, 1
wrong gene product), 74 for PAINT/GO Central (44 wrong term, 16 other, 7
missing negation, 6 wrong qualifier, 1 wrong reference), 5 for UniProt and 5
for other resources (InterPro2GO mappings). Most are `CHECK` requests at
SUSPECTED or PROBABLE confidence, because many seed papers could only be read
as abstracts. They include defects from PAO1 reviews made before this project.

### Per-gene verdicts


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
| 15 | xcpX | PA3097 | T2SS complex; protein secretion by T2SS (PTN000475915) | 35 | SOUND; process row cites a review as IDA (abstract only, unverified) | Sound | P (CHECK, SUSPECTED) |
| 16 | waaL | PA4999 | polysaccharide biosynthetic process (PTN008076295) | 64 | SOUND; seed term arguably the wrong step | Sound; ligase-activity row removed (WaaL is ATP-independent) | P (x6) |
| 17 | PA3891 | PA3891 | plasma membrane (PTN001953445); ABC-type glycine betaine transporter activity (PTN001953060) | 54 | INDIRECT: "IDA" is cross-species complementation of a P. syringae opuCA mutant; substrate data are the ortholog's | Plausible, but should be re-seeded from the characterised ortholog | P (x2), G (x2) |
| 18 | wbpY | PA5448 | lipopolysaccharide biosynthetic process (PTN000749272) | 51 | SOUND | Sound; its shared glycosyltransferase node should be re-seeded from a 2022 direct assay | P, G |
| 19 | PA0692 | PA0692 | type V secretion process and complex (PTN002160772) | 25 | SOUND; complex row is IMP, which cannot show membership | Sound | P |
| 20 | mgtE | PA0913 | magnesium ion transport; magnesium ion binding (PTN000227060) | 50 | Transport SOUND; binding INDIRECT (IMP on homology-model sites; binding very likely true by conservation) | 6 of 22 leaves lack the MgtE transmembrane domain yet inherit transport | P, G (x2) |
| 21 | PA1055 | PA1055 | sodium:proton antiporter activity; sodium ion transmembrane transport (PTN002160376) | 48 | INDIRECT: only shaA was deleted; antiporter activity is the whole Sha complex's, so contributes_to | Should be contributes_to; node includes archaeal hydrogenase subunits | P (x2), G |
| 22 | pilM | PA5044 | type IV pilus; type IV pilus-dependent motility (PTN001286216) | 46 | Location WRONG: IMP "no pili" turned into located_in pilus (same row given to pilN/O/P); motility SOUND | Pilus CC IBD unsupported; node also reaches EutJ ethanolamine-utilization proteins | P, G (x2) |
| 23 | PA3760 | PA3760 | N-acetylglucosamine transport (PTN000532509) | 43 | SOUND for PA3760 | OVER-SPECIFIC: node is general Enzyme I (PtsI, PtsP, FruB) | G |
| 24 | hutH | PA5098 | histidine ammonia-lyase activity; L-histidine catabolic process (PTN000796665) | 42 | SOUND (direct assay of the partially purified enzyme), coded IMP instead of IDA | Sound; but PAO1 paralog PA5093, which lacks the catalytic Ala-Ser-Gly motif, inherits it | P, G (NOT on PA5093) |
| 25 | hom | PA3736 | L-threonine biosynthetic process (PTN000752178) | 41 | UNVERIFIABLE: cited paper is about ThrH/ThrB; one PMID applied to all thr genes | Term right for an all-homoserine-dehydrogenase clade; needs a real anchor | P |
| 26 | PA1057 | PA1057 | sodium:proton antiporter activity; sodium ion transmembrane transport (PTN002160407) | 40 | INDIRECT, as PA1055; MrpE is an assembly subunit | Should be contributes_to | P (x2), G |
| 27 | PA5377 | PA5377 | carnitine transport and transporter activity; choline transport (PTN000766131) | 39 | Choline/betaine SOUND; carnitine OVER-SPECIFIC (needs the separate binding protein CaiX); amine transporter activity WRONG (quaternary ammonium is not an amine in GO) | Carnitine IBDs on the permease node not supported; amine IBD should be repointed | P (x4), G (x3) |
| 28 | nrdJa | PA5497 | ribonucleoside-diphosphate reductase activity, thioredoxin as acceptor (PTN000171476) | 39 | OVER-SPECIFIC: purified NrdJ prefers CTP over CDP >60-fold and thioredoxin was never used | Clade mixes NDP- and NTP-specific reductases | P, G |
| 29 | cif | PA2934 | epoxide hydrolase activity (PTN002458043) | 38 | SOUND (structure, kinetics) | Sound; its broad hydrolase node (791 IBAs) also sound | P (reference on another row) |
| 30 | braD | PA1073 | L-isoleucine import, L-alanine transport (PTN000765102) | 36 | SOUND (as braF) | Sound, same caveat; D-alanine transport seed is an indirect phenotype | none |
| 31 | gltA | PA1580 | tricarboxylic acid cycle (PTN002450857) | 36 | SOUND claim; IDA on an enzyme purification (IC would be accurate) | Sound | P |
| 32 | aruC | PA0895 | L-arginine biosynthetic process (PTN000241318) | 35 | SOUND (dual biosynthetic/catabolic aminotransferase; enzyme data only) | Node also passes it to LysJ, diaminobutyrate aminotransferase and AstC leaves | G |
| 33 | gbuA | PA1421 | L-arginine catabolic process (PTN004253691) | 34 | SOUND for GbuA | Over-reaches across a guanidino-acid hydrolase clade (AGMAT, GpuA); separate guanidinopropionase IBA contradicted by assay | G (x2) |
| 34 | pilD | PA4528 | aspartic-type endopeptidase activity (PTN000766410) | 33 | SOUND (purified enzyme) | Sound | P (reference query on a plasma membrane row) |
| 35 | dgcB | PA5399 | oxidoreductase activity (PTN000229983) | 33 | INDIRECT: transposon growth + NMR coded IDA; the chemistry probably belongs to DgcA | Generic node term defensible from domains | P (x2), G |
| 36 | pqsC | PA0998 | secondary metabolite biosynthetic process (PTN002147059) | 30 | SOUND (own transposon mutant loses PQS) | Over-broad: node sits above ordinary fatty-acid FabH enzymes | G |
| 37 | PA0920 | PA0920 | phospholipid homeostasis; aminoacyltransferase; PG alanyltransferase (PTN002162750, PTN005059806) | 28 | Activities SOUND; phospholipid homeostasis WRONG (the gene makes A-PG; homeostasis needs the PA0919 hydrolase) | Homeostasis IBD unsupported, and the node includes fungal ErgS sterol glycyltransferases | P, G, UniProt |
| 38 | PA4079 | PA4079 | NAD(P) CH-OH oxidoreductase (PTN002388087) | 27 | SOUND (direct enzymology) | Sound; generic term suits a cross-kingdom SDR clade | none |
| 39 | pilU | PA0396 | DNA endonuclease activity, producing 5'-phosphomonoesters (PTN000766390) | ~13 | WRONG: GO:0016888 typed for GO:0016887 ATP hydrolysis (same paper and date as pilB) | Unsupported: remove from node | P, G |
| 40 | liuC | PA2013 | terpene catabolic process; methylglutaconyl-CoA hydratase activity (PTN001733227) | 26 | Terpene OVER-SPECIFIC (true for PAO1 only because the terpene pathway feeds leucine catabolism); hydratase UNVERIFIABLE (paper never mentions liuC) | Terpene IBD should go: most leaves lack the pathway; node also covers AtuE and PksH | P, G (x2) |
| 41 | PA4503 | PA4503 | dipeptide transmembrane transporter activity (PTN000765601) | 25 | SOUND claim; operon deletion coded IDA | OVER-SPECIFIC: node holds NikB (nickel) and SapB (putrescine) permeases; binding protein sets substrate | P, G |
| 42 | thiI | PA5118 | thiazole biosynthetic process (PTN001804941) | 25 | WRONG evidence: the paper is a Salmonella genetics study, coded IDA for P. aeruginosa | Node is the family root, mostly short rhodanese-less ThiI that make s4U but not thiazole: re-place at the proteobacterial clade | P, G |
| 43 | pscC | PA1716 | protein secretion by the type III secretion system (PTN009110345) | 25 | SOUND | Sound; node is the T3SS-specific subnode | none |
| 44 | cifR | PA2931 | negative regulation of DNA-templated transcription (PTN002934616) | 25 | SOUND (purified repressor binds mapped operators) | Sound | none |
| 45 | PA4624 | PA4624 | transmembrane protein transporter activity (PTN002160772) | 25 | SOUND (secretion readout of CdrA) | Sound (TpsB subfamily) | P (biofilm row) |
| 46 | xcpS | PA3102 | protein secretion by the T2SS (PTN000768597) | 25 | SOUND term; IDA cites a review (PMID:9818381), abstract only, so the evidence code is unverified | Sound | P (CHECK, SUSPECTED) |
| 47 | xcpW | PA3098 | T2SS process and complex (PTN002446812) | 24 | SOUND terms; process IDA cites a review, complex IDA cites a paper whose abstract shows only membrane fractionation (both abstract only, unverified) | Sound | P (x2, CHECK, SUSPECTED) |
| 48 | wzm | PA5451 | lipopolysaccharide transport (PTN002019107) | 24 | SOUND | Over-broad: reaches teichoic-acid and capsule exporters and Gram-positive/archaeal permeases; polysaccharide transport would fit | G |
| 49 | dctQ | PA5168 | C4-dicarboxylate transport (PTN002169725) | 24 | SOUND for DctQ | OVER-SPECIFIC: YiaM-type clade (E. coli YiaM moves 2,3-diketo-L-gulonate) | G |
| 50 | lpxA | PA3644 | lipopolysaccharide biosynthetic process (PTN000602377) | 24 | SOUND claim; reference is a lipid A structure paper that predates the gene | Sound; lipid A biosynthesis would be sharper | P |
| 51 | xcpV | PA3099 | T2SS process and complex (PTN002446181) | 24 | SOUND terms; same unverified seed queries as xcpW | Node may be too broad: 14 of 49 leaves named PilV/MshD/pilin | P (x2), G (x2) |
| 52 | xcpQ | PA3105 | protein secretion by the T2SS (PTN000768388) | 23 | SOUND term; IDA cites a review, abstract only, evidence code unverified | Sound | P (CHECK, SUSPECTED) |
| 53 | relA | PA0934 | response to starvation (PTN001083175) | 23 | SOUND | Sound; a SpoT hydrolase IBA from the same node was removed from RelA | G |
| 54 | arcA | PA5171 | arginine deiminase activity (PTN005338738) | 23 | SOUND (mutants defined by loss of ADI alone; locus shown to encode it) | Sound; a few short non-ADI leaves (YkgA, archaeal) to check | G |
| 55 | nmoA | PA4202 | nitronate monooxygenase activity (PTN001284536) | 23 | SOUND (purified enzyme, structure) | Over-broad: sibling leaf PA0660 was purified and has no NMO activity (a quinone reductase) | G |
| 56 | pilN | PA5043 | type IV pilus; motility; pilus assembly (PTN002220336) | 21 | Location WRONG (same IMP "no pili" row as pilM, on an inner-membrane protein); motility and assembly SOUND | Pilus CC IBD (added 2026-06-17) should be withdrawn | P, G |
| 57 | lasB | PA3724 | proteolysis (PTN002138658) | 21 | SOUND | Sound | P (x2, cargo-as-machinery rows, as lap) |
| 58 | thrB | PA5495 | L-threonine biosynthetic process; homoserine kinase activity (PTN001464661) | 20 | Process SOUND but evidence is genetic (IGI, not IDA); kinase activity UNVERIFIABLE (no assay visible) | Node includes B. subtilis AmiN, an amicoumacin kinase | P (x2), G |
| 59 | hfq | PA4944 | regulation of RNA stability (PTN002164223) | 20 | SOUND (Hfq stabilises RsmY) | Sound; less certain for Firmicutes leaves | none on seed |
| 60 | pilA | PA4525 | type IV pilus-dependent motility; type IV pilus (PTN002013003) | 20 | SOUND claims; evidence codes wrong (mutant assay as IDA, review as IMP) | Sound | P (x2) |
| 61 | fliD | PA1094 | bacterial-type flagellum filament cap (PTN000767631) | 20 | SOUND claim; cited paper (mucin binding) shows no cap experiment | Sound | UniProt (subunit is hexamer, not pentamer) |
| 62 | PA1059 | PA1059 | sodium:proton antiporter activity (PTN002162936) | 19 | INDIRECT: subunit never mutated (ShaG) | Should be contributes_to; node reaches archaeal hydrogenase subunits MbhC/MbxC | P (x2), G |
| 63 | PA1058 | PA1058 | sodium:proton antiporter activity (PTN002162906) | 19 | INDIRECT: subunit never mutated (ShaF) | Should be contributes_to; node reaches MbhB/MbxB | P (x2), G |
| 64 | tgpA | PA2873 | protein-glutamine gamma-glutamyltransferase activity (PTN002126683) | 17 | OVER-SPECIFIC: kit assay of amine incorporation on an isolated domain, not protein cross-linking | Node of papain-fold domains named by domain only; nearest characterised relative is a deamidase | G |
| 65 | dksA | PA4723 | regulation of DNA-templated transcription (PTN002139169) | 17 | SOUND | Sound | P (wrong reference: paralog DksA2 paper) |
| 66 | pchB | PA4230 | salicylic acid biosynthetic process (PTN002211012) | 17 | SOUND for PchB (isochorismate pyruvate lyase) | OVER-SPECIFIC: node is the AroQ chorismate mutase family root; the other 16 leaves are mutases with no lyase activity | G |
| 67 | arcD | PA5170 | arginine:ornithine antiporter activity (PTN000208945) | 16 | SOUND; PseudoCAP IMP is really a proteoliposome assay (IDA) | Sound; Chlamydia AaxC (arginine:agmatine) under the node | P, G, UniProt |
| 68 | PA1054 | PA1054 | sodium ion transmembrane transport (PTN000511949) | 16 | SOUND: the one subunit actually deleted (ShaAB) | Antiporter activity should be contributes_to | P, G |
| 69 | PA1056 | PA1056 | sodium ion transmembrane transport (PTN001865541) | 16 | SOUND claim; IMP without a PA1056 mutant | Sound; two complex I-derived IEA rows removed | P (x2), G |
| 70 | hutF | PA5106 | L-histidine catabolic process (PTN000138516) | 16 | UNVERIFIABLE (1967 paper, as hutI); activity seed SOUND | Re-anchor on PMID:16475788; three nematode leaves lack HutF signatures | P, G |
| 71 | nirJ | PA0511 | heme biosynthetic process (PTN000132400) | 15 | SOUND for NirJ (heme d1) | OVER-SPECIFIC: archaeal SPASM radical SAM clade; one other leaf is a heme-pathway enzyme | G |
| 72 | xcpR | PA3103 | T2SS process and complex (PTN002016240) | 14 | Complex SOUND; process IDA cites a review, abstract only, evidence code unverified | Sound; node restricted to Gammaproteobacteria, keeping T2SS terms off PilB-type ATPases | P |
| 73 | oprG | PA4067 | transmembrane transport (PTN005107949) | 13 | SOUND (channel in planar bilayers) | Sound | none |
| 74 | fpr | PA3397 | heme catabolic process (PTN002500048) | 13 | SOUND for fpr as heme oxygenase electron donor | OVER-SPECIFIC: a partner-specific role on a family node that includes E. coli and Salmonella Fpr | G |
| 75 | PA4504 | PA4504 | dipeptide transmembrane transporter activity (PTN000766696) | 12 | SOUND claim; operon deletion coded IDA | OVER-SPECIFIC: node holds NikC (nickel) and GsiD (glutathione) | P, G |
| 76 | fur | PA4764 | negative regulation of siderophore biosynthetic process (PTN002112483) | 12 | SOUND for Fur | OVER-SPECIFIC: leaves include Fur of Neisseria, Helicobacter, Coxiella; a sibling secondary-metabolite IBD sits on the whole Fur superfamily (Zur, PerR, Irr) | G (x2) |
| 77 | PA1486 | PA1486 | aminopeptidase activity (PTN002194605) | 12 | SOUND (purified BapF) | Sound | none |
| 78 | pvdH | PA2413 | transaminase activity (PTN002461253) | 11 | SOUND (direct assay) | Sound | none |
| 79 | PA5085 | PA5085 | sequence-specific DNA binding (PTN001576694) | 11 | SOUND (EMSA with purified DguR) | Sound | none |
| 80 | cysB | PA1754 | L-cysteine biosynthetic process (PTN002824317) | 10 | INDIRECT: auxotrophy of a mutant of the pathway's transcriptional activator | Unsupported: all 10 leaves are CysB/Cbl regulators | P, G |
| 81 | oprB | PA3186 | carbohydrate transport (PTN002209977) | 10 | SOUND claim; mutant uptake coded IDA | Sound | P |
| 82 | PA0906 | PA0906 | regulation of DNA-templated transcription (PTN002221379) | 10 | SOUND (ChIP-seq, promoter fusions) | Sound | P (autolysis row) |
| 83 | PA2280 | PA2280 | NAD(P)H quinone oxidoreductase (PTN008682975) | 10 | WRONG reference: the cited paper studies Synechocystis ArsH; activity true from a later P. aeruginosa assay | Sound content; re-cite the seed | P, G |
| 84 | PA2580 | PA2580 | cellular response to oxidative stress (PTN002922793) | 9 | SOUND but weak (overexpression rescues only a katA mutant); quinone reductase row is a purified-enzyme assay coded IMP | Sound; H. pylori ortholog knockout would be a better seed | P |
| 85 | pqsA | PA0996 | secondary metabolite biosynthetic process (PTN002458530) | 9 | Not written (review YAML blocked): agent found the cited paper attributes the PA0996 result to another study | Node is the family root; a child node swaps terms between PqsA and FadD22 | pending |
| 86 | lhpL | PA1255 | 4-hydroxyproline epimerase activity (PTN002433936) | 9 | WRONG: Swiss-Prot records experimentally that it has no 4-hydroxyproline epimerase activity; it is a trans-3-hydroxy-L-proline dehydratase; PAO1's real epimerase is PA1268 | Unsupported: repoint | P, G |
| 87 | motB | PA4953 | bacterial-type flagellum-dependent swarming motility (PTN001251133) | 9 | OVER-SPECIFIC: motAB single mutant swarms normally; only the motAB motCD double fails | Swarming is a lifestyle phenotype, not propagable; repoint to flagellum-dependent motility | P (x2), G |
| 88 | dctP | PA5167 | C4-dicarboxylate transport (PTN002121312) | 9 | SOUND | Sound: unlike the DctQ node this is a binding-protein clade | none |
| 89 | pilT | PA0395 | ATP hydrolysis activity (PTN002020799) | 8 | SOUND (purified enzyme, motif mutants) | Sound | P (a non-seed located_in pilus row) |
| 90 | ptrB | PA0612 | positive regulation of secondary metabolite biosynthetic process (PTN002215317) | 8 | WRONG: full text shows PtrB represses type III secretion; no secondary-metabolite phenotype | Unsupported: delete | P, G |
| 91 | PA1341 | PA1341 | L-glutamate import (PTN004745596) | 7 | SOUND (partial growth defect, corroborated) | Sound | none |
| 92 | znuC | PA5500 | response to zinc ion (PTN001952271) | 7 | INDIRECT: EDTA growth defect of the importer ATPase; zinc sensing is Zur's | Repoint to zinc import (~1,455 GOA rows) | P, G, UniProt |
| 93 | pslC | PA2233 | single-species biofilm formation (PTN002463206) | 7 | INDIRECT: deletion phenotype coded IDA | Unsupported: other leaves are glycosyltransferases for O-antigen, ExoU, flagellin glycans | P, G |
| 94 | PA4521 | PA4521 | response to antibiotic (PTN002214697) | 7 | UNVERIFIABLE (abstract reports only ampD complementation) | AmpE's role contested; E. coli leaf has no AmpR | G |
| 95 | fimU | PA4550 | type IV pilus (PTN008624060) | 7 | SOUND | Sound | none on seed |
| 96 | phnB | PA1002 | phenazine biosynthetic process (PTN000230115) | 7 | INDIRECT: anthranilate feeds PQS, which induces the phz operons; PhzE makes the phenazine anthranilate | Unsupported; a TrpGD fusion artefact also removed | G (x2) |
| 97 | PA5359 | PA5359 | alkane catabolic process (PTN002217427) | 7 | UNVERIFIABLE; paper characterises AlkB/Rub genes and PA5359 is a 151-aa lipoprotein (likely wrong gene, perhaps PA5349) | Node is a lipoprotein-repeat family including a tomato protein | P, G |
| 98 | mucB | PA0764 | regulation of polysaccharide biosynthetic process (PTN002215378) | 7 | SOUND for MucB (alginate via AlgU) | OVER-SPECIFIC: the other 6 leaves are RseB orthologs that regulate sigmaE, not polysaccharides | G |
| 99 | pfeA | PA2688 | enterobactin transport and transporter activity (PTN000763909) | 6 | SOUND | Sound | G (colicin row) |
| 100 | PA1340 | PA1340 | L-glutamine transport (PTN000764525) | 6 | WRONG: the seed paper is a P. putida study; PA1340 was not tested | Node is a GltK glutamate/aspartate clade | P, G |
| 101 | PA4505 | PA4505 | dipeptide transmembrane transporter activity (PTN000656114) | 6 | SOUND claim; operon deletion coded IDA | Sound: node holds only DppD orthologs | P |
| 102 | PA5208 | PA5208 | bacterial-type flagellum-dependent swarming motility (PTN002194937) | 5 | INDIRECT: transposon-screen hit with a growth defect; protein is PhoU-like | Delete: leaves include non-flagellated Haemophilus and Coxiella | P, G |
| 103 | phzC1 | PA4212 | phenazine biosynthetic process (PTN000481936) | 5 | SOUND (phz-operon DAH7P synthase) | Node also holds housekeeping DAH7P synthases (incl. PAO1 PA2843), which now carry phenazine biosynthesis | G |
| 104 | lasI | PA1432 | signal transduction (PTN002217335) | 5 | WRONG: a signal synthase is not part of signal transduction (receiver-side); quorum sensing fits; genetic evidence coded IDA | Repoint node to quorum sensing (all 5 leaves are LuxI-family synthases) | P, G |
| 105 | PA3697 | PA3697 | regulation of nitric oxide metabolic process (PTN002422332) | 5 | INDIRECT: only fhp promoter induction was lost; NO metabolism not measured | Withdraw: ~175 GOA IBA rows cite this node | P, G |
| 106 | mucD | PA0766 | periplasmic space (PTN002342204) | 5 | SOUND | Sound | P (signal transduction row) |
| 107 | eddB | PA3909 | DNA catabolic process (PTN001684760) | 3 | SOUND (secreted DNase) | Sound | none |
| 108 | pelA | PA3064 | deacetylase activity (PTN002441861) | 3 | SOUND (purified protein, active-site mutants) | Other two leaves look too short to contain the deacetylase domain | G |
| 109 | PA2403 | PA2403 | siderophore biosynthetic process | 2 | Not written (agent stopped): gene is FpvG, which releases iron from ferripyoverdine, so pyoverdine biosynthesis looks wrong or indirect | pending | pending |

### Not completed

The review files for pvdE, pqsA and PA2403 were not written: the agent's write
of each review YAML was blocked by a safety classifier (pvdE, pqsA), and the
agent stopped before PA2403. pvdE's notes, seed assessment and node analysis
are committed. The research findings for the other two:

- **pqsA:** the cited paper (PMID:12426334) attributes the PA0996 result to a
  different study; PMID:18728009 shows a pqsA mutant makes no quinolines. The
  seeding node PTN002458530 is the family root, and the child node
  PTN001186225 swaps terms between PqsA and FadD22.
- **PA2403:** the gene is FpvG, which releases iron from ferripyoverdine
  (PMID:28192658, PMID:31924850), so its pyoverdine biosynthesis seed
  (PMID:12207696, an expression-profiling study) looks wrong or indirect.

### Patterns

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
- **Evidence codes that overstate the assay** (fleN, PA0692, PA5458, PA3891,
  PA4503, PA4504, dgcB): IDA on a sequence motif, on cross-species
  complementation or on an operon deletion; IMP for complex membership. The Xcp
  type II secretion process rows all cite one review (PMID:9818381) as IDA.
  That is worth a check, but we have only the abstract, and a review from the
  laboratory that did the work can report original data, so it is recorded as
  SUSPECTED, not as an error.
- **Substrate terms on clades where the binding protein sets the substrate**
  (PA4503, PA4504, braF, dctQ): dipeptide transport seeded on permease nodes
  that also hold NikB/NikC (nickel), SapB (putrescine) and GsiD (glutathione);
  C4-dicarboxylate transport on a YiaM (diketogulonate) clade.
- **Over-specific activity** (nrdJa): a thioredoxin-dependent diphosphate
  reductase term on an enzyme that prefers triphosphates and was never assayed
  with thioredoxin.
- **Subunit and partner conflation** (PA5377, PA1055, PA1057): carnitine
  transport, which needs the separate binding protein CaiX, seeded on the
  permease node; Sha antiporter activity, measured for the whole PA1054-PA1059
  cluster after deleting only PA1054, given as IMP `enables` to each subunit.
- **Consequences as processes** (PA0920): an alanyl-phosphatidylglycerol
  synthase annotated to phospholipid homeostasis.
- **Pathway context that does not travel** (liuC): terpene catabolism is true
  for PAO1 only because its terpene pathway feeds the leucine pathway, but it
  was seeded on a hydratase node whose other members lack it.
- **Phenotypes as locations** (pilM, pilN): IMP "mutant has no pili" recorded
  as `located_in` type IV pilus, and given identically to pilN, pilO and pilP;
  confirmed on pilN.
- **Gene-specific roles on family-root nodes** (pchB, nirJ, fpr, fur): the
  seed is right for the PAO1 gene, but the node is the whole family. Salicylate
  synthesis on the chorismate mutase root, heme d1 synthesis on an archaeal
  radical SAM clade, heme catabolism on ferredoxin reductases that include
  *E. coli* Fpr, and siderophore repression on Fur proteins of bacteria that
  make no siderophores.
- **One citation for a whole operon** (hom): the ThrH/ThrB kinase paper cited
  for hom, thrB and thrH alike.
- **Another organism's paper coded IDA** (thiI): a *Salmonella* genetics study
  given to PA5118 as IDA.
- **Old papers that predate the gene** (hutI, lpxA): a 1967 pathway paper cannot tie
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

1. ~~Review every tier 1 gene.~~ Done except for writing the pqsA, PA2403 and
   pvdE review files.
2. Reconcile small inconsistencies between reviews: xcpX's complex row
   (PMID:9466253) has no reference defect, while the similar xcpW and xcpV rows
   (PMID:8331069) do.
3. Send the PseudoCAP and PAINT reports upstream, starting with the 21
   withdraw-or-repoint cases.
4. Tier 2 (289 proteins that share each node with other seeds), starting with
   seedings whose only PAO1 support is IMP or IGI.
5. The rest of the PseudoCAP corpus (2,069 rows on PAO1 in QuickGO),
   prioritising IMP rows on molecular-function terms.

Re-run the builder when PAINT or QuickGO data change; it only re-downloads
files missing from `.cache/paint/`, so delete that folder to refresh.
