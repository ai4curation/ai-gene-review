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

- [ ] `XENLA/foxd3-a` (Q9DEN4) — FoxD3; vertebrate-specific N-terminal motif; no border expression in amphioxus. Homeolog `foxd3-b` Q9DEN3
- [ ] `XENLA/sox10` (Q8AXX8) — SoxE; NC specification, pigment and glia
- [ ] `XENLA/snai2` (Q91924) — Slug; NC specifier and EMT repressor
- [ ] `XENLA/sox9-a` (B7ZR65) — SoxE; cranial NC and chondrogenesis (cross-check `human/SOX9`)
- [ ] `XENLA/twist1` (P13903) — Twist; *Ciona* Twist misexpression makes a9.49 cells migratory
- [ ] `XENLA/ets1-a` (P18755) — Ets1; reported as part of the amniote cranial NC circuit (verify against PMID:27339986 full text during review)
- [ ] `XENLA/myc-a` (P06171) — c-Myc; NC stem-cell pool (cross-check `human/MYC`)
- [ ] `XENLA/id3-a` (Q91399) — Id3; co-opted into the NC (amphioxus/lamprey Id)
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
