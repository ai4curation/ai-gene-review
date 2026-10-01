---
title: Origins of the Neural Crest
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [XENLA, human, CIOIN]
genes: [foxd3-a, sox10, snai2, sox9-a, twist1, ets1-a, myc-a, id3-a, sox8, pax3-a, zic1, MSX1, TFAP2A, hes4-a, gbx2, pou5f1.1, lin28a, snai1]
---
# Project NEURAL_CREST_ORIGINS: the gene regulatory network that made the vertebrate head

**Bottom line (scoping):** the neural crest is the textbook vertebrate novelty.
It is a migratory, multipotent cell population that builds most of the head
skeleton, the peripheral nervous system and the pigment cells. Comparative work
in lamprey, amphioxus and tunicates now explains much of its origin: an ancient
chordate *neural plate border* programme was inherited, and new *neural crest
specifier* circuits were then recruited into it stepwise. A
blastula-stage pluripotency programme was also retained or reactivated. This
project reviews the GO annotations of the genes at each layer of that network.
We start with *Xenopus laevis*, where most of the functional network was
mapped. The aim is a high-quality annotation set that keeps three roles
apart: the border specifiers (ancestral), the crest specifiers (largely
vertebrate innovations) and the pluripotency factors (repurposed). That
separation is what the evolutionary story depends on, and the current GO
annotations blur it.

## Motivation

Gans and Northcutt proposed that the vertebrate "new head" was built from two
embryonic novelties, the neural crest and the cranial placodes
[PMID:17732898 "Neural crest and the origin of vertebrates: a new head"].
Forty years later the question has become one of gene regulation. Which parts
of the neural crest gene regulatory network (GRN) were already present in the
invertebrate chordate ancestor, and which were added at the base of vertebrates?

The evidence so far, from the outgroups:

| Lineage | Key observation | Reference |
|---|---|---|
| Lamprey (jawless vertebrate) | Most of the gnathostome NC GRN is already deployed in lamprey, so the network is at least as old as crown vertebrates | [PMID:17765683 "Ancient evolutionary origin of the neural crest gene regulatory network"], [PMID:19104059] |
| Lamprey | Lamprey cranial NC lacks most of the amniote cranial-specific transcriptional circuit [PMID:27339986] and resembles amniote trunk NC; that circuit was added gradually in gnathostomes, so the ancestral NC was trunk-like | [PMID:31645763 "Evolution of the new head by gradual acquisition of neural crest regulatory circuits"] |
| Lamprey | SoxE paralog duplication and subfunctionalisation in the branchial skeleton | [PMID:21889937] |
| Lamprey | NC and blastula pluripotency networks share regulatory factors as far back as the vertebrate ancestor. Lamprey *pou5* is expressed in animal pole cells but not in NC, yet lamprey and *Xenopus* pou5 both promote NC formation | [PMID:39060477 "Shared features of blastula and neural crest stem cells evolved at the base of vertebrates"] |
| Amphioxus (cephalochordate) | The genome has homologs of most NC GRN genes. Border patterning genes and their BMP responsiveness are conserved, but many NC specifier genes are not expressed at the neural plate border. The AmphiFoxD regulatory region drives mesoderm, not NC, reporter expression in chick | [PMID:18562679 "Insights from the amphioxus genome on the origin of vertebrate neural crest"], [PMID:12397104], [PMID:14651928] |
| Amphioxus / vertebrates | Amphioxus FoxD and vertebrate FoxD3 are both repressors with similar DNA binding, but only FoxD3 induces ectopic NC in chick, through a vertebrate-specific N-terminal motif. Protein evolution, not only *cis*-regulatory change, contributed | [PMID:24252777 "A novel N-terminal motif is responsible for the evolution of neural crest-specific gene-regulatory activity in vertebrate FoxD3"] |
| *Ciona* (tunicate, sister group of vertebrates) | The cephalic melanocyte lineage (a9.49) is a "rudimentary neural crest"; targeted misexpression of Twist (Ci-Twist-like-2) reprograms it into migrating ectomesenchyme | [PMID:23135395 "Identification of a rudimentary neural crest in a non-vertebrate chordate"] |
| *Ciona* | Migratory bipolar tail neurons arise from the neural plate border | [PMID:26524532 "Migratory neuronal progenitors arise from the neural plate borders in tunicates"] |
| *Ciona* | Neural crest and cranial placodes share an evolutionary origin in a border cell population | [PMID:30069052 "Shared evolutionary origin of vertebrate neural crest and cranial placodes"], [PMID:26258298] |
| Lamprey / jawed vertebrates | Neofunctionalisation of the endothelin pathway drove NC diversification into skeletal cell types | [PMID:32939088 "Evolution of the endothelin pathway drove neural crest cell diversification"] |

A second line of work concerns *potency*. Neural crest cells share a regulatory
programme with pluripotent blastula cells (Pou5f3/Oct25, Ventx, Sox2/3, Snail,
Id3, Myc, Lin28). This suggests the crest kept, or reacquired, blastula-stage
potential, and that this may be the true vertebrate innovation
[PMID:25931449 "Shared regulatory programs suggest retention of blastula-stage potential in neural crest cells"],
[PMID:33542111 "Reactivation of the pluripotency program precedes formation of the cranial neural crest"],
[PMID:36182685 "Pluripotency factors are repurposed to shape the epigenomic landscape of neural crest cells"],
[PMID:30144418]. Reviews: [PMID:25903629 "Evolution of vertebrates as viewed from the crest"],
[PMID:25564621 "Establishing neural crest identity: a gene regulatory recipe"],
[PMID:31619682 "A genome-wide assessment of the ancestral neural crest gene regulatory network"].

## Why this is a GO curation problem

GO has a well-populated neural crest process branch:
`GO:0014029` neural crest formation, `GO:0014034` neural crest cell fate
commitment, `GO:0014036` neural crest cell fate specification, `GO:0014033`
neural crest cell differentiation, `GO:0014032` neural crest cell development,
and `GO:0001755` neural crest cell migration. Experimental annotations to it
come mainly from zebrafish, *Xenopus* and mouse knockdown and loss-of-function
work. Expected problems to test, gene by gene:

1. **Layer conflation.** Border specifiers (Pax3, Zic1, Msx1, Tfap2a, Hes4,
   Gbx2) act *upstream* of crest specification. GO has no "neural plate border
   specification/formation" process term; the nearest are neural plate
   pattern/regionalisation terms (`GO:0060896`, `GO:0060897`). So border genes
   may be annotated directly to NC fate specification, and NC specifiers to
   "neural crest formation". Check whether the existing terms are precise
   enough, and whether a border term should be proposed (`proposed_new_terms`).
2. **Annotate the biology, not the experiment.** A GO annotation records our
   synthesised judgement of what the gene product does, reached by biological
   reasoning across several lines of evidence. It is not a transcript of one
   assay. For each gene, the review should bring together:
   - where and when it is expressed (border, premigratory or migratory crest);
   - its molecular activity (DNA binding, activation or repression, partners);
   - its direct targets and enhancer occupancy in the network;
   - gain-of-function sufficiency (ectopic crest, reprogramming);
   - loss-of-function phenotypes;
   - conservation of that role across vertebrates and its state in the
     outgroups.

   From that combined picture, place the gene in the network layer where it
   does its work. A border specifier, a crest specifier and a competence
   factor each warrant a different process term. Where the biology does not
   support a process term, it does not stand just because an experiment is
   attached to it.
3. **Molecular function precision.** Many entries are probably still at
   generic `DNA-binding transcription factor activity` or carry `protein binding`
   IPIs. Where the evidence supports it, prefer RNA polymerase II-specific
   activator/repressor terms. Examples: Snai2 as a repressor; FoxD3 as a
   repressor/pioneer factor; Id3 as a bHLH dimerisation inhibitor, not a DNA
   binder.
4. **Homeolog and paralog splitting.** In *X. laevis* L/S homeologs
   (`foxd3-a`/`-b`, `pax3-a`/`-b`, `sox9-a`/`-b`, `id3-a`/`-b`, `hes4-a`/`-b`),
   experimental annotations may be attached to only one homeolog. Note this in
   the reviews; do not "fix" it by assertion.
5. **Pluripotency factors and the NC.** Can Pou5f3/Oct25, Lin28 or Ventx
   properly be annotated to neural crest processes? Or is the role the
   maintenance of a competence state that the crest inherits? The second would
   argue for a stem cell population maintenance term rather than NC
   specification.

The evolutionary claims belong in gene `description`s and `core_functions` as
biology, and in the project synthesis. GO itself has no "evolutionary novelty"
terms, and we will not invent any.

## Scope and species

- **Primary species: *Xenopus laevis* (`XENLA`, NCBITaxon:8355).** Most of the
  NC GRN was mapped by gain- and loss-of-function in frog. Reviewed (Swiss-Prot)
  entries exist for most network genes and carry *Xenopus*-specific
  experimental GO annotations.
- **Human (`human`)** is used for *MSX1* and *TFAP2A*, which have no reviewed
  *X. laevis* entry. Relevant human reviews that already exist and should be
  cross-checked: SOX9, SOX2, MYC, GBX2, FGF8, KIT, ALX1, AXIN2.
- **Outgroup comparators (stretch goal, `CIOIN` and others).** UniProt coverage
  of lamprey (*Petromyzon marinus*, taxon 7757) and amphioxus is almost all
  unreviewed TrEMBL. Few of these entries have any GO annotation, and some are
  fragments (e.g. amphioxus SoxE `A8QJ82`, 114 aa). *Ciona* Twist-like-2
  (`Q4H2N6`) is the best-supported tunicate candidate, given the Twist
  misexpression result. Outgroup reviews are optional and mostly add `NEW`
  annotations, so the bar in CLAUDE.md applies.

Accessions below were checked against the UniProt REST API on 2026-10-01.

---
# STATUS

Last updated: 2026-10-01

## Tier 1 — Neural crest specifiers (candidates for vertebrate-specific recruitment)

- [x] `XENLA/foxd3-a` (Q9DEN4) — FoxD3; NC specifier (repressor) with a competence face. Reviewed 2026-10-01: 25 GOA rows (14 ACCEPT, 5 non-core, 4 MODIFY, 2 over-annotated) + 1 NEW (GO:0001227). Homeolog `foxd3-b` Q9DEN3
- [x] `XENLA/sox10` (Q8AXX8) — SoxE; NC specifier. Reviewed 2026-10-01: 32 GOA rows (11 ACCEPT, 14 non-core, 6 MODIFY, 1 REMOVE)
- [ ] `XENLA/snai2` (Q91924) — Slug; NC specifier and EMT repressor
- [x] `XENLA/sox9-a` (B7ZR65) — SoxE; NC specifier + crest-derived chondrogenesis. Reviewed 2026-10-01: 45 GOA rows (22 ACCEPT, 16 non-core, 5 MODIFY, 1 REMOVE, 1 over-annotated) + 1 NEW (GO:0001228)
- [ ] `XENLA/twist1` (P13903) — Twist; *Ciona* Twist misexpression makes a9.49 cells migratory
- [x] `XENLA/ets1-a` (P18755) — Ets1; late NC specifier / cranial-identity factor. Reviewed 2026-10-01: 21 GOA rows (12 ACCEPT, 1 MODIFY, 6 non-core, 1 over-annotated) + 4 NEW incl. NC delamination and migration
- [x] `XENLA/myc-a` (P06171) — c-Myc; competence factor carried from the blastula. Reviewed 2026-10-01: 11 GOA rows (10 ACCEPT, 1 non-core) + 1 NEW (GO:0014029, IMP PMID:12791268 — **flagged for curator check**, see notes)
- [x] `XENLA/id3-a` (Q91399) — Id3; NC progenitor maintenance/competence factor (not a specifier). Reviewed 2026-10-01: 28 GOA rows (20 ACCEPT, 5 MODIFY, 2 REMOVE, 1 non-core)
- [ ] `XENLA/sox8` (Q6VVD7) — SoxE

## Tier 2 — Neural plate border specifiers (ancestral chordate layer)

- [ ] `XENLA/pax3-a` (Q645N4) — Pax3/7; border expression conserved in amphioxus
- [ ] `XENLA/zic1` (O73689) — Zic1; border specifier together with Pax3
- [ ] `human/MSX1` (P28360) — Msx (no reviewed *X. laevis* entry)
- [ ] `human/TFAP2A` (P05549) — AP-2; early NPB/NC; amphioxus/lamprey AP-2
- [ ] `XENLA/hes4-a` (Q90Z12) — Hairy2; border maintenance
- [ ] `XENLA/gbx2` (Q91907) — Gbx2; posterior border (cross-check `human/GBX2`)

## Tier 3 — Blastula pluripotency programme retained in the crest

- [ ] `XENLA/pou5f1.1` (Q7T103) — Oct25 (Pou5f3 class)
- [ ] `XENLA/lin28a` (Q8JHC4) — Lin28
- [ ] `XENLA/snai1` (P19382) — Snail1; blastula and NC
- [ ] `XENLA/sox3-a` (P55863) / `XENLA/sox2` (O42569) — SoxB1 to SoxE transition [PMID:30144418]

## Tier 4 — Outgroup comparators (optional)

- [ ] `CIOIN` Ci-Twist-like-2 (Q4H2N6) — the Twist used in the a9.49 reprogramming experiment [PMID:23135395]
- [ ] Lamprey SoxE paralogs (TrEMBL; e.g. soxe2 A0A5P9Q4B1) — decide whether reviewable

## Synthesis deliverables

- [ ] Layer table: for each gene, its GRN layer, the outgroup expression data, and the GO process terms kept after review
- [ ] Decide whether to propose a "neural plate border formation/specification" term
- [ ] Cross-check against GO-CAM (`gocams/index.tsv`) for NC models

# NOTES

## 2026-10-01

- Project created. Pulled experimental (ECO:0000269 descendants) GOA
  annotations to the NC process branch (`GO:0014029`, `GO:0014034`,
  `GO:0014036`, `GO:0014032`, `GO:0014033`, `GO:0001755`). Rows by taxon:
  zebrafish 1420, mouse 335, *X. laevis* 178, human 51, chicken 35,
  *X. tropicalis* 17. The *X. laevis* hits at the fate commitment/specification
  level are dominated by zic1, pax3-a/-b, id3-a, hes4-a/-b, sox9-a, snai1,
  snai2, sox10, foxd3-a and sox8. These set Tiers 1 and 2.
- No GO term for neural plate border formation or specification exists (the
  QuickGO search returns only neural plate terms).
- QuickGO total annotation counts per accession (all evidence): foxd3-a 25,
  sox10 32, snai2 15, sox9-a 45, twist1 12, ets1-a 21, myc-a 11, id3-a 28,
  sox8 19, pax3-a 25, zic1 33, hes4-a 29, gbx2 13, pou5f1.1 52, lin28a 26,
  snai1 21, human MSX1 64, human TFAP2A 116.
- Lamprey and amphioxus proteins are almost all TrEMBL and unannotated, so the
  evolutionary comparison will draw on the literature rather than GO data.

### Tier 1 reviews (in progress)

- **ets1-a.** Placed as a *late* NC specifier and cranial-identity factor. In
  chick it comes on after the border genes, Tfap2b activates it, and it binds
  the cranial Sox10E2 enhancer directly [PMID:27339986, PMID:20139305]. With
  Sox8 and Tfap2b it reprograms trunk crest to a cranial, chondrogenic
  identity. Frog loss of function disrupts delamination and migration but not
  initial foxd3/snai2 [PMID:25691536]. The full text of PMID:27339986 confirms
  that Ets1 is in the chick cranial circuit, which resolves the earlier
  open point. Martik 2019 [PMID:31645763] finds Ets1 absent from lamprey
  premigratory and migratory crest but present in skate, so Ets1 joined the
  crest network in gnathostomes, not at the vertebrate base.
  Open: whether it belongs under NC cell fate specification (chick and frog
  data differ). Frog loss-of-function reagents hit both homeologs.
- **sox10.** NC specifier: it comes on after the border genes, inside the
  crest domain, downstream of Wnt/FGF and Snail [PMID:12885557, PMID:12812785].
  All four `GO:0014029` neural crest formation rows, including three IMP rows,
  were MODIFIED to `GO:0014036` neural crest cell fate specification. Melanocyte
  differentiation was accepted as a core role. `enzyme binding` (an Ubc9 IPI,
  which only shows Sox10 is a SUMOylation substrate) was removed. Sox10 is never
  expressed in blastula cells, which fits SoxE recruitment being a vertebrate
  novelty. Sox10 can replace SoxB1 to keep blastula cells pluripotent, but only
  when overexpressed [PMID:30144418], so this was raised as a question, not
  annotated. Lamprey SoxE paralogs duplicated independently [PMID:21889937], so
  Sox10-specific late roles should not be transferred to lamprey genes.

- **sox9-a.** NC specifier. At the border it comes on after Sox8 and before
  Sox10 [PMID:16943273]. Morphants lose crest progenitors [PMID:11807034]. It
  is needed for specification, not migration, and acts as an activator: an
  engrailed-repressor fusion phenocopies the knockdown [PMID:15464575], so
  `GO:0001228` was added as NEW. Its four `GO:0014029` rows were independently
  narrowed to `GO:0014036`, matching sox10. Chondrogenesis is core
  (crest-derived cranial cartilage); otic placode is a separate,
  non-core deployment. Evolution: the cartilage role is ancestral (lamprey Sox9
  co-expressed with Col2a1), and lamprey SoxE paralogs are not 1:1 orthologs.
  All experimental rows sit on sox9-a, and the abstracts don't say whether the
  reagents also hit sox9-b.

- **foxd3-a.** NC specifier downstream of Zic/Wnt; Zic needs it to induce
  Slug. It is a forkhead *repressor* that recruits Groucho/TLE through an eh1
  motif, so `GO:0001227` was added as NEW and the Grg4 `protein binding` was
  changed to `GO:0001222` transcription corepressor binding. The repression
  process rows were narrowed to `GO:0000122`. `GO:0014034` NC fate commitment
  was accepted as core. Mesoderm and organizer roles are a separate, non-core
  deployment. The neurogenesis regulation terms (opposite signs in two papers)
  were marked over-annotated. FoxD3 is also expressed in blastula cells, and
  mouse Foxd3 maintains epiblast and crest progenitors; that competence role
  is left as a question for frog. Evolution: repressor activity and DNA
  specificity are ancestral, since amphioxus FoxD has both [PMID:24252777].
  New in vertebrates are expression at the border [PMID:18562679] and the
  N-terminal motif that lets FoxD3 induce crest. So both *cis*-regulatory and
  protein changes were involved.

- **id3-a.** Progenitor maintenance and competence factor, not a specifier.
  Losing Id3 causes progenitor cell-cycle arrest and death "rather than a cell
  fate switch", so its five IMP `GO:0014029` rows were *kept* at the broad
  level, which fits the convention below. The IBA corepressor term was
  MODIFIED to `GO:0140416` transcription regulator inhibitor activity, the term
  human/mouse ID1/2/4 carry: Id proteins sequester bHLH partners off DNA. The
  TreeGrafter circadian IEA was removed (an Id2-only function). Evolution: a
  clean co-option case [PMID:14651928]. Amphioxus Id is expressed in
  mesoderm/endoderm, and border expression first appears in lamprey; the
  protein activity is ancestral, so this is a change in *where* it is expressed.
  Open: stem cell population maintenance (`GO:0019827`) for the shared
  Myc–Id3 blastula/NC programme [PMID:25931449] was raised as a question,
  not added.

- **myc-a.** Competence factor carried over from the blastula. Myc is
  expressed in pluripotent blastula cells [PMID:25931449], appears at the
  border before slug, and is needed for crest precursors through Id3
  [PMID:15772131]. The crest requirement does not depend on proliferation
  [PMID:12791268], so the proliferation IBA is non-core. NEW `GO:0014029`
  (IMP, PMID:12791268) was added at the broad level, matching id3-a.
  **Flag:** no Myc ortholog in any species carries a neural crest process
  term. Under CLAUDE.md a systematic absence should be read as a possible
  convention. We judge it a coverage gap: Myc is a DNA-binding transcription
  factor that directly drives Id3 in the crest, so it does part of the work.
  This needs a curator decision. Open: the c-myc I/II naming conflicts
  between Vriz 1989 and UniProt. The morpholino hits both homeologs, so the
  same evidence applies to myc-b (P15171). Evolution: frog uses c-Myc at the
  border, while chick uses N-Myc there and c-Myc later, so the crest needs
  Myc *activity* rather than one specific paralog.

### Project-level decision to confirm: GO:0014029 vs GO:0014036

`GO:0014029` neural crest formation is defined as forming the *region of
ectoderm* between the neural plate and non-neural ectoderm. The chain is
`GO:0014036` fate specification part_of `GO:0014034` fate commitment part_of
`GO:0014029`. The sox10 review narrowed specifier genes from `GO:0014029` to
`GO:0014036`, leaving `GO:0014029` for genes that act on the border region as a
whole. Apply this consistently across Tier 1 (and decide whether border
specifiers in Tier 2 should keep `GO:0014029`). This needs curator sign-off,
because it modifies IMP rows to a more specific child term. Applied so far:
sox10 and sox9-a narrowed to `GO:0014036`; foxd3-a already at `GO:0014034`
(accepted); id3-a deliberately kept at `GO:0014029`, as a non-specifier.
