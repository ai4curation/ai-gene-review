---
title: Origins of the Neural Crest
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [XENLA, human, CIOIN]
genes: [foxd3-a, sox10, snai2, sox9-a, twist1, ets1-a, myc-a, id3-a, sox8, pax3-a, zic1, MSX1, TFAP2A, hes4-a, gbx2, pou5f1.1, lin28a, snai1, sox2, sox3-a, TFAP2B, TFAP2C, PAX7]
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
programme with pluripotent blastula cells (Pou5f3/Oct25/Oct60, Ventx, Sox2/3,
Snail, Id3, Myc, Sox5, FoxD3 [PMID:25931449]; Lin28 is linked to the crest
separately, from chick and lamprey work [PMID:30520734, PMID:39060477]). This suggests the crest kept, or reacquired, blastula-stage
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

## Tier 1 — Neural crest specifiers (candidates for vertebrate-specific recruitment) — COMPLETE 2026-10-01

- [x] `XENLA/foxd3-a` (Q9DEN4) — FoxD3; NC specifier (repressor) with a competence face. Reviewed 2026-10-01: 25 GOA rows (14 ACCEPT, 5 non-core, 4 MODIFY, 2 over-annotated) + 1 NEW (GO:0001227). Homeolog `foxd3-b` Q9DEN3
- [x] `XENLA/sox10` (Q8AXX8) — SoxE; NC specifier. Reviewed 2026-10-01: 32 GOA rows (11 ACCEPT, 14 non-core, 6 MODIFY, 1 REMOVE)
- [x] `XENLA/snai2` (Q91924) — Slug; NC specifier then EMT/migration effector. Reviewed 2026-10-01: 15 GOA rows (13 ACCEPT, 1 MODIFY, 1 REMOVE) + 3 NEW (GO:0001227, GO:0000122, GO:0001222)
- [x] `XENLA/sox9-a` (B7ZR65) — SoxE; NC specifier + crest-derived chondrogenesis. Reviewed 2026-10-01: 45 GOA rows (22 ACCEPT, 16 non-core, 5 MODIFY, 1 REMOVE, 1 over-annotated) + 1 NEW (GO:0001228)
- [x] `XENLA/twist1` (P13903) — Twist; late, head-only NC specifier / ectomesenchyme driver. Reviewed 2026-10-01: 12 GOA rows (9 ACCEPT, 3 MODIFY) + 2 NEW (GO:0140416 Snail2 inhibition, GO:0048701 cranial skeleton morphogenesis)
- [x] `XENLA/ets1-a` (P18755) — Ets1; late NC specifier / cranial-identity factor. Reviewed 2026-10-01: 21 GOA rows (12 ACCEPT, 1 MODIFY, 6 non-core, 1 over-annotated) + 4 NEW incl. NC delamination and migration
- [x] `XENLA/myc-a` (P06171) — c-Myc; competence factor carried from the blastula. Reviewed 2026-10-01: 11 GOA rows (10 ACCEPT, 1 non-core) + 1 NEW (GO:0014029, IMP PMID:12791268; comparator check passed, see notes)
- [x] `XENLA/id3-a` (Q91399) — Id3; NC progenitor maintenance/competence factor (not a specifier). Reviewed 2026-10-01: 28 GOA rows (20 ACCEPT, 5 MODIFY, 2 REMOVE, 1 non-core)
- [x] `XENLA/sox8` (Q6VVD7) — SoxE; first-wave NC specifier. Reviewed 2026-10-01: 19 GOA rows (9 ACCEPT, 8 non-core, 2 MODIFY)

## Tier 2 — Neural plate border specifiers (ancestral chordate layer) — COMPLETE 2026-10-05

- [x] `XENLA/pax3-a` (Q645N4) — Pax3/7; neural plate border specifier. Reviewed 2026-10-05: 25 GOA rows (17 ACCEPT, 3 non-core, 4 over-annotated, 1 MODIFY) + 1 NEW (GO:0001228)
- [x] `XENLA/zic1` (O73689) — Zic1; border specifier (with Pax3), also preplacodal. Reviewed 2026-10-05: 33 GOA rows (25 ACCEPT, 6 non-core, 1 MODIFY, 1 over-annotated) + 2 NEW (GO:0001228, GO:0060788)
- [x] `human/MSX1` (P28360) — Msx1; border specifier upstream of Pax3/Zic. Reviewed 2026-10-05: 64 GOA rows (38 ACCEPT, 17 non-core, 5 over-annotated, 2 REMOVE, 2 UNDECIDED) + 1 NEW (GO:0014029, ISS)
- [x] `human/TFAP2A` (P05549) — AP-2α; spans border and NC layers. Reviewed 2026-10-05: 114 GOA rows (73 ACCEPT, 19 non-core, 10 REMOVE, 6 MODIFY, 6 over-annotated) + 1 NEW (GO:0014029, ISS)
- [x] `XENLA/hes4-a` (Q90Z12) — Hairy2; border / progenitor-maintenance repressor. Reviewed 2026-10-05: 29 GOA rows (20 ACCEPT, 5 non-core, 3 MODIFY, 1 UNDECIDED) + 1 NEW (GO:0001227)
- [x] `XENLA/gbx2` (Q91907) — Gbx2; border specifier, upstream of pax3/msx1. Reviewed 2026-10-05: 13 GOA rows (9 ACCEPT, 2 MODIFY, 2 non-core) + 4 NEW (GO:0014029, GO:0001227, GO:0030917, GO:0043049)

## Tier 3 — Blastula pluripotency programme retained in the crest — COMPLETE 2026-10-07

- [x] `XENLA/pou5f1.1` (Q7T103) — Oct25 (Xenbase pou5f3.2.L); germ-layer timing factor + crest competence factor. Reviewed 2026-10-07: 51 GOA rows (37 ACCEPT, 7 non-core, 5 MODIFY, 2 over-annotated) + 2 NEW (GO:0003714, GO:0014029 — **flagged**, see notes)
- [x] `XENLA/lin28a` (Q8JHC4) — Lin28; general pluripotency/timing RNA-binding factor in frog (crest role shown only in chick). Reviewed 2026-10-07: 26 GOA rows (9 ACCEPT, 12 non-core, 4 MODIFY, 1 over-annotated) + 1 NEW (GO:0070883)
- [x] `XENLA/snai1` (P19382) — Snail1; blastula competence factor, then earliest crest specifier. Reviewed 2026-10-07: 21 GOA rows (15 ACCEPT, 5 MODIFY, 1 REMOVE) + 1 NEW (GO:0001227)
- [x] `XENLA/sox2` (O42569) — SoxB1; blastula pluripotency and neural-progenitor gene, not a crest participant. Reviewed 2026-10-07: 25 GOA rows (17 ACCEPT, 7 non-core, 1 MODIFY) + 2 NEW (GO:0045665, GO:0060041)
- [x] `XENLA/sox3-a` (P55863) — SoxB1; maternal germ-layer patterning, genome activation, neural competence; not a crest participant. Reviewed 2026-10-07: 29 GOA rows (19 ACCEPT, 10 non-core) + 2 NEW (GO:0141064, GO:0021990)

## Tier 4 — Missing module members (from module deep research)

Human entries are used, as for TFAP2A: the key data are from chick, and no
reviewed chicken or frog entries exist (UniProt checked 2026-10-08).

- [x] `human/TFAP2B` (Q92481) — AP-2β; crest specifier (TFAP2A–TFAP2B heterodimer), cranial circuit. Reviewed 2026-10-08: 90 GOA rows (50 ACCEPT, 18 non-core, 11 over-annotated, 7 REMOVE, 4 MODIFY) + 1 NEW (GO:0014036, ISS)
- [ ] `human/TFAP2C` (Q92754) — AP-2γ; partners TFAP2A during border induction (chick)
- [ ] `human/PAX7` (P23759) — Pax7; the Pax3/7 border factor used in chick; FoxD3 NC1/NC2 enhancer input

## Tier 5 — Outgroup comparators (optional)

- [ ] `CIOIN` Ci-Twist-like-2 (Q4H2N6) — the Twist used in the a9.49 reprogramming experiment [PMID:23135395]
- [ ] Lamprey SoxE paralogs (TrEMBL; e.g. soxe2 A0A5P9Q4B1) — decide whether reviewable

## Module

- [x] `modules/neural_crest_gene_regulatory_network.yaml` (2026-10-05) — the
  network as a five-part developmental module: border specification;
  competence maintenance; crest fate specification (with a SoxE paralog
  variant set); delamination and migration; cranial ectomesenchyme. Genes with
  roles in several layers (AP-2α, Snai2, Twist1, Sox9) get one annoton per
  role, so roles that are non-core at gene level become explicit parts. Twist1
  appears twice: restraining Snai2 during specification, and driving cranial
  ectomesenchyme. Regenerate it with
  `uv run python projects/NEURAL_CREST_ORIGINS/build_nc_module.py`; evidence
  quotes are copied from the validated gene reviews.

- [x] Module deep research (falcon, 2026-10-07) integrated. It supports the
  boundary: Wnt/BMP/FGF are upstream inputs, and the border is ancestral while
  the crest assembly is new. It sharpened the edges: Gbx2 → Pax3/Msx1 is
  epistasis only; AP-2α → pax3 is the best-supported direct edge;
  Pax3/Zic1 targets are translation-independent but enhancer occupancy in
  frog is unshown; Twist → Snai2 is stage-specific. Snail1 (specification)
  and Oct25/Pou5f3 (competence) were added from Tier 3. New knowledge gaps:
  unreviewed candidate members (TFAP2A–TFAP2C → TFAP2A–TFAP2B partner switch,
  Hairy2–FGFR4–STAT3, OCT4–SOX2–TFAP2A, Twist1–CHD7/CHD8/WHSC1, chick Pax7)
  and Lin28 (chick-only evidence). Candidate Tier 4 reviews: TFAP2B, TFAP2C,
  PAX7.

## Synthesis deliverables

- [ ] Layer table: for each gene, its GRN layer, the outgroup expression data, and the GO process terms kept after review
- [ ] Decide whether to propose a "neural plate border formation/specification" term (drafted as a `proposed_terms` entry in the module's knowledge gaps)
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
  **Comparator check (corrected 2026-10-02).** The review first said that
  no Myc in any species carries a crest term. That was wrong: zebrafish *mych*
  carries `GO:0014032` neural crest cell development by IMP [PMID:18446220]. So
  this is not a systematic family-wide absence. Mammalian and frog c-Myc simply
  lack curation of the crest papers. The NEW term stands as an ordinary
  coverage gap. Myc is a DNA-binding transcription factor that directly drives
  Id3 in the crest, so it does part of the work. Open: the c-myc I/II naming conflicts
  between Vriz 1989 and UniProt. The morpholino hits both homeologs, so the
  same evidence applies to myc-b (P15171). Evolution: frog uses c-Myc at the
  border, while chick uses N-Myc there and c-Myc later, so the crest needs
  Myc *activity* rather than one specific paralog.

- **sox8.** First-wave NC specifier. It is the earliest SoxE gene at the
  lateral neural plate edge, from mid-gastrula, and Pax3 plus Zic1 activate it
  together with snail1 and myc [PMID:23509273, PMID:24360908]. Knockdown
  *delays* crest induction, and any SoxE gene rescues it. Both `GO:0014029`
  rows were narrowed to `GO:0014036`, consistent with sox9-a and sox10. The
  IMP row also got `GO:0001755` migration. Family transfers from mammalian
  Sox9/10 (PNS, ENS, epithelium) were kept non-core. Evolution: which SoxE
  paralog leads in the crest differs by lineage. Frog uses Sox8, chick and
  mouse Sox9, zebrafish sox9a/b, lamprey SoxE1/2 (duplicated independently
  [PMID:21889937]). The specifier role belongs to the SoxE *group*, split
  among paralogs differently in each lineage, so orthology transfer of
  paralog-specific crest roles is unsafe.

- **twist1.** Late, head-only NC specifier. It comes on at stage 14, after
  snai1/2, sox9 and foxd3, and Pax3 activates it directly without Zic1
  [PMID:24360906]. Knockdown with rescue lowers sox10 and snai2 and widens the
  zic1 border domain. NEW from Lander 2013 [PMID:23443570, full text]:
  - `GO:0140416` transcription regulator inhibitor activity: Twist binds Snail2
    and blocks Snail2-induced ectopic crest, under GSK3β control at S148.
  - `GO:0048701` embryonic cranial skeleton morphogenesis.

  The TAS `GO:0014029` row (source PMID:15242799, an Id2 cardiac-crest paper
  whose abstract never mentions Twist) was narrowed to `GO:0014036` and its
  reference flagged UNVERIFIED. The generic "developmental process" IBA/IEA
  rows were first MODIFIED to `GO:0014036`. On 2026-10-07 they were revised to
  KEEP_AS_NON_CORE: the term is correctly inherited at bHLH family level, and
  Twist1's specific roles now live in its core functions and in two parts of
  the module. Evolution: in *Ciona*, Twist is
  mesoderm-only, and forcing it into a9.49 makes migratory ectomesenchyme
  [PMID:23135395], which supports co-option. The *early* specifier role is
  absent in amniotes (Lander), so the conserved vertebrate role is
  ectomesenchyme, not specification.

- **snai2.** NC specifier that later acts in EMT and migration. It comes on
  after snai1 inside the prospective crest, and knockdown leaves zic1 and pax3
  intact (Tien 2015). It cannot induce crest alone but can with Wnt. Blocking
  it early prevents precursors from forming; blocking it later stops
  migration (LaBonne 2000). NEW: `GO:0001227` repressor activity (engrailed
  fusions; E-cadherin ChIP); `GO:0000122`; `GO:0001222` corepressor binding
  (EZH2, Ajuba LIM proteins via SNAG). The TAS `GO:0014029` row was narrowed to
  `GO:0014036`. Its source, PMID:15242799 (an Id2 paper), is flagged as
  miscited, the same source twist1 found. Elp3 `protein binding` was removed.
  *Withheld* `GO:0036032` delamination: frog cranial crest keep E-cadherin
  while migrating and need it to migrate (Huang 2016). Evolution:
  amphioxus Snail is expressed at the border, so Snail border expression is
  ancestral. Lamprey has one snail gene; Snai1/Snai2 subfunctionalised
  after the gnathostome duplication.

### Tier 1 synthesis (2026-10-01)

| Gene | Layer (review placement) | NC process term kept | Outgroup / evolution |
|---|---|---|---|
| foxd3-a | NC specifier (repressor), with a competence face | `GO:0014034` fate commitment | FoxD repressor activity ancestral; border expression plus N-terminal motif new in vertebrates |
| sox10 | NC specifier | `GO:0014036` | Never in blastula; SoxE recruitment a vertebrate novelty |
| sox9-a | NC specifier, then crest cartilage | `GO:0014036` | Cartilage role ancestral (lamprey Sox9 with Col2a1) |
| sox8 | First-wave NC specifier (frog) | `GO:0014036` | Leading SoxE paralog differs by lineage |
| snai2 | NC specifier, then migration | `GO:0014036`, `GO:0001755` | Snail border expression ancestral (amphioxus) |
| twist1 | Late, head-only specifier; ectomesenchyme | `GO:0014036` | *Ciona* Twist mesoderm-only, sufficient for ectomesenchyme: co-option |
| ets1-a | Late cranial-identity specifier, delamination | `GO:0036032`, `GO:0001755` (NEW) | Absent from lamprey crest, present in skate: a gnathostome addition |
| id3-a | Progenitor maintenance / competence | `GO:0014029` (kept broad) | Border expression from lamprey; a change in where it is expressed |
| myc-a | Competence factor from the blastula | `GO:0014029` (NEW) | Frog c-Myc vs chick N-Myc at the border |

Cross-cutting findings:
- **Three evolutionary modes appear in Tier 1.** (i) Ancestral border
  expression (Snail). (ii) Co-option by a change in where a gene is expressed,
  with protein activity unchanged (Id, SoxE, FoxD *cis*-regulation, Twist).
  (iii) Protein change (FoxD3 N-terminal motif). Ets1 shows the crest network
  kept growing after the vertebrate origin.
- **Molecular function.** Recurring precise terms: `GO:0001227` (FoxD3,
  Snai2), `GO:0001228` (Sox9, Ets1), and `GO:0140416` transcription regulator
  inhibitor activity (Id3; Twist on Snail2). Generic `protein binding` was
  replaced or removed everywhere.
- **PMID:15242799** (an Id2 cardiac-crest paper) is the TAS source for the
  `GO:0014029` rows on both twist1 and snai2, and is miscited for both. Report
  it to the source curators.
- **Homeologs.** In every case, experimental rows sit on one homeolog only
  (foxd3-b, sox9-b, id3-b, myc-b and snai2.S lack them), while knockdown
  reagents typically hit both.
- **Flags for curator review:** the convention below. (The twist1
  "developmental process" rows were resolved on 2026-10-07; see twist1.)

### Tier 2 reviews (in progress)

- **hes4-a (Hairy2a).** Border and progenitor-maintenance repressor, not a
  crest specifier. Notch/Delta1 (downstream of Xiro1), BMP and FGF induce it.
  It represses Bmp4, and early overexpression represses crest markers. With
  Id3 and Stat3 it keeps progenitors dividing and undifferentiated.
  `GO:0014029` was kept at the broad level, as for id3-a and myc-a. NEW
  `GO:0001227`; the comparator was checked in QuickGO (human HES1, HEY1/2 and
  BHLHE40/41 carry it). The BMP signalling row was MODIFIED to `GO:0030514`
  negative regulation. **Conflict for curators:** Q90Z12 carries both positive
  `GO:0014029` rows and a NOT `GO:0014029` row. The NOT comes from Murato 2007,
  a hairy2a-specific knockdown with no crest phenotype, which conflicts with
  Vega-López 2015 [PMID:25997789]; it was marked UNDECIDED. Across the HES/HEY
  family only *Xenopus* hes4 carries any NC term, and Hes4 is absent from
  rodents. No outgroup (amphioxus/lamprey) border data on hairy were found.

- **pax3-a.** Neural plate border specifier. It is expressed at the border
  before foxd3 and slug, and Wnt/FGF induce it via Msx1. With Zic1 it directly
  activates snai1/2, foxd3, twist1 and tfap2b, and the pair is necessary and
  sufficient for crest determination [PMID:23509273]. NEW `GO:0001228`
  activator activity (IDA, PMID:24360906): Pax3 binds the snail2 promoter and
  its own upstream element, and activates both without new protein synthesis.
  Both `GO:0014029` formation and `GO:0014034` commitment were kept as core, and
  `GO:0014036` was not added. That fits the convention: border genes keep the
  broad term, and the specification term goes to the Tier 1 specifiers. The
  FGF and Wnt signalling rows were marked over-annotated: Pax3 is a target of
  these signals, not a transducer [PMID:10433827]. Hatching gland development
  (Pax3 alone, without Zic1) is non-core. The comparator check was verified
  in QuickGO: experimental crest formation/commitment terms sit only on frog
  Pax3, while mouse Pax3 (P24610) carries `GO:0001755` migration by IMP
  [PMID:15384171]. So this is a coverage gap, not a convention. Evolution:
  amphioxus expresses Pax3/7 at the border while most crest specifiers are
  absent there [PMID:18562679]. Pax3 is an ancestral border gene; its link to
  the specifiers is what vertebrates added. The experimental rows sit on
  both homeologs identically, but the reagents did not distinguish them.

- **gbx2.** Border specifier. Wnt activates it directly (ChIP, enhancer
  test). Knockdown removes crest markers and expands the placode domain, with
  rescue. It acts upstream of pax3 and msx1, needs Zic1 to induce crest, and
  represses six1 [PMID:19736322, PMID:22564795]. No *Xenopus* Gbx entry had any
  experimental annotation, so four NEW IMP terms were added from uncurated
  papers: `GO:0014029`, `GO:0001227`, `GO:0030917` (midbrain–hindbrain
  boundary) and `GO:0043049` (otic placode formation). `GO:0014029` rather than
  `GO:0014036`, because Gbx2 alone cannot make crest. The comparator check was
  verified in QuickGO: the border peers pax3-a, zic1 and hes4-a carry
  `GO:0014029` by IMP and none carries `GO:0014036`, and mouse Gbx2 (P48031)
  carries `GO:0001755` migration by IMP from three papers. So the frog gap is
  uncurated literature. Evolution: amphioxus Gbx abuts Otx, so the Gbx/Otx
  positioning machinery is ancestral to chordates. *Ciona* has lost Gbx, and
  lamprey gbx2 shows the frog-like border expression. Gbx2 is an ancestral
  positional gene put to work at the border in vertebrates. Open: *X. laevis*
  has four gbx2 copies, so which one the morpholinos target is unclear.

- **zic1.** Border specifier. It is expressed before foxd3/slug and directly
  activates snail1. With Pax3 it activates snail2, foxd3, twist1, tfap2b and
  sox8. Alone it gives neural or preplacodal tissue, not crest. All five
  `GO:0014029` and three `GO:0014034` rows were accepted, matching pax3-a; the
  `GO:0014033` differentiation row was MODIFIED to `GO:0014034`. NEW:
  - `GO:0001228` activator activity (EMSA on a snail1 element;
    cycloheximide-resistant activation [PMID:24360906]).
  - `GO:0060788` ectodermal placode formation [PMID:17409353, full text].

  The comparator checks were verified in QuickGO: no Zic in any species
  carries `GO:0014036`, while zebrafish foxi1, gata3 and tfap2a and frog tbx1
  carry `GO:0060788` by IMP/IGI. Evolution: amphioxus Zic and Pax3/7 already
  mark the border without the crest specifiers [PMID:18562679], the same
  pattern as pax3-a. Open: PMID:9435279 sources a `GO:0014029` IMP row
  although its abstract does not mention crest (accepted, deferring to the
  curator). Only zic1.S has experimental rows. Zebrafish tfap2a sits at
  `GO:0014036`, which is relevant to the TFAP2A review.

- **TFAP2A (human).** Spans two layers. In frog it is the earliest border
  specifier: Wnt-induced, upstream of pax3, and alone enough to impose a
  border-like pattern [PMID:21169220]. It then acts again in the crest as a
  specifier [PMID:12511599]. In chick it opens chromatin at border enhancers
  with TFAP2C, then at crest enhancers with TFAP2B [PMID:31848212]. Zebrafish
  needs tfap2a and tfap2c together for crest induction [PMID:17258188]. Human
  TFAP2A had no crest term at all, so NEW `GO:0014029` (ISS) was added; adding
  `GO:0014036` as well was judged redundant. The comparator check was verified
  in QuickGO: mouse Tfap2a (P34056) carries `GO:0014032` by IMP [PMID:8622766]
  and zebrafish tfap2a carries `GO:0014036` (IMP). Protein binding rows:
  - CITED2/EP300 rows changed to `GO:0001223` coactivator binding.
  - NPM1 and KCTD1 rows changed to `GO:0001222` corepressor binding.
  - Uninformative rows removed.
  - The MYO6 IPI row (PMID:11447109) was removed as name confusion, verified
    from the cached text: the paper's "AP-2" is the clathrin adaptor complex.

  Hearing, retina, iron-response, ROS and retinoblastoma-overexpression rows
  were marked over-annotated. Evolution: amphioxus AP-2 is expressed in
  non-neural ectoderm only [PMID:12397104]. So, *unlike* Pax3/7 and Zic, AP-2's
  border and crest roles are a vertebrate co-option, probably elaborated by the
  TFAP2 paralog expansion. Open: genes that act in *both* layers, AP-2α the
  clearest case, test whether the convention should let them carry
  `GO:0014036` too.

- **MSX1 (human).** Border specifier, one step above Pax3/Zic1: intermediate
  BMP induces msx1, msx1 induces pax3 and zic, and those induce snail2 and
  foxd3; gbx2 sits upstream. Gain of function induces crest markers
  [PMID:14627721, PMID:15691759]. A dominant negative or Msx1/2 morpholinos
  remove them [PMID:16586351]. Mouse Msx1/2 double mutants still form crest
  but mispattern cranial and cardiac crest [PMID:16221730]. NEW `GO:0014029`
  (ISS) was added. `GO:0014034` was not added, because Msx1 has no shown
  binding at specifier enhancers. Core functions: repressor `GO:0001227`;
  tooth and palate development. The six p53 rows from one overexpression study
  were split between non-core and over-annotated. The inner-ear rows were
  marked UNDECIDED: the source reports malleus (middle ear) defects. The EMT
  IEA was removed because its source studies epithelial–mesenchymal
  *interaction*. Comparator verified in QuickGO: no Msx protein in any species
  carries any crest term; the same-layer peers do by IMP. Evolution: amphioxus
  Msx reaches the neural plate edge and responds to BMP [PMID:18562679], so
  the border role is ancestral. Lamprey msx-A lacks the frog-like border
  dynamics [PMID:39060477].

### Tier 2 synthesis (2026-10-05)

| Gene | Layer | NC terms kept | Outgroup / evolution |
|---|---|---|---|
| gbx2 | Border specifier (posterior; upstream of pax3/msx1) | `GO:0014029` (NEW) | Gbx/Otx positioning ancestral (amphioxus); lost in *Ciona* |
| MSX1 | Border specifier (BMP-responsive; upstream of pax3/zic) | `GO:0014029` (NEW, ISS) | Border expression ancestral (amphioxus) |
| pax3-a | Border specifier; with Zic1, necessary and sufficient for crest | `GO:0014029`, `GO:0014034` | Border expression ancestral (amphioxus) |
| zic1 | Border specifier; also preplacodal | `GO:0014029`, `GO:0014034` | Border expression ancestral (amphioxus) |
| hes4-a | Border / progenitor maintenance | `GO:0014029` (one NOT row UNDECIDED) | No outgroup data found |
| TFAP2A | Spans border and crest | `GO:0014029` (NEW, ISS) | Amphioxus AP-2 is non-neural only: **co-opted** |

Cross-cutting findings:
- **The border layer is ancestral, and the wiring is new.** Pax3/7, Zic, Msx
  and Gbx already mark the chordate neural plate border (amphioxus). What
  vertebrates added is direct activation of the crest specifiers by the
  Pax3/Zic1 pair, plus co-option of AP-2 into the border. This matches Tier 1:
  most specifiers were co-opted by a change in where they are expressed.
- **The convention held up without strain.** Every border gene sits naturally
  at `GO:0014029`, with `GO:0014034` where it directly induces crest fate
  (Pax3, Zic1), and none needed `GO:0014036`. The one tension is TFAP2A,
  which genuinely acts in both layers, and zebrafish tfap2a sits at
  `GO:0014036`.
- **Coverage gaps, not conventions.** Every border gene's comparator check
  (verified in QuickGO) found crest terms on at least one ortholog
  (mouse Pax3, mouse Gbx2, mouse/zebrafish Tfap2a) or on same-layer peers
  (Msx). Uncurated frog papers account for most of the missing annotations:
  gbx2 had no experimental rows at all.
- **The case for a "neural plate border formation" term** is now made by
  six genes. Raise it with GO as a `proposed_new_terms` / NTR. The
  definition should cover the border as a competence territory that gives
  rise to crest, placode and dorsal neural tube.

### Tier 3 reviews (in progress)

- **snai1.** Sits in two layers in sequence. First, a blastula competence
  factor, needed to keep the Oct/Sox/Vent network active [PMID:25931449]. Then
  the earliest crest specifier: it is activated in the first wave with sox8
  and myc [PMID:23509273], Zic1 binds and activates it directly
  [PMID:24360906], and alone it induces all crest markers tested, upstream of
  Slug [PMID:12490555]. Accepted at `GO:0014036` and `GO:0001755`, matching
  snai2. Four Ajuba/LIMD1/WTIP `protein binding` IPIs were changed to
  `GO:0001222` corepressor binding (SNAG-dependent). The TAS `GO:0014029` row
  cites the same miscited Id2 paper, PMID:15242799 (the third gene so
  affected). NEW `GO:0001227`; the comparator was verified in QuickGO (human
  SNAI1 and mouse Snai1 both carry it by IDA). Evolution: Snail border
  expression is ancestral (amphioxus). Lamprey's single snail is flat across
  blastula and crest stages, like frog snai1, while frog snai2 rises like a
  definitive crest factor. That suggests subfunctionalisation after the
  gnathostome duplication. Mouse uses Snail rather than Slug in premigratory
  crest, so which paralog leads is lineage-specific. For the module: add
  Snail1 to the specification and competence parts, with Zic1 → Snail1 →
  Snai2 edges.

- **lin28a.** In frog, a general pluripotency and developmental-timing
  RNA-binding factor. It lets transient blastula cells respond to FGF and
  activin/nodal [PMID:23344711] and times metamorphosis [PMID:28359807]. NEW
  `GO:0070883` pre-miRNA binding (ISS; *X. tropicalis* lin28a binds pre-let-7
  loops [PMID:26447465]). The pre-miRNA processing rows were changed to
  `GO:2000632` *negative* regulation, because Lin28 blocks Dicer processing.
  `GO:0019827` stem cell population maintenance was marked over-annotated: the
  frog data show competence to respond to signals, not a maintained stem cell
  pool. No crest term was added: no frog crest experiment exists. In chick,
  Lin28a is needed for FoxD3/Sox10 [PMID:30520734], and let-7 targets Myc,
  which would put Lin28 in the competence layer. The comparator check
  (QuickGO) found no Lin28 in any species carrying a crest term, so this is an
  uncurated chick paper. `GO:0014029` would belong on chick LIN28A (Q45KJ5),
  not frog lin28a. Module: add only as a knowledge gap or a chick-grounded
  annoton. Correction made: the Motivation section had cited PMID:25931449
  for Lin28, which that paper never mentions; it now cites PMID:30520734 and
  PMID:39060477. Evolution: Lin-28/let-7 are ancient bilaterian timing genes,
  so any crest role is a co-option.

- **pou5f1.1 (Oct25 = pou5f3.2.L).** The best-supported, core role is
  germ-layer timing: a corepressor of VegT, beta-catenin and nodal targets
  that limits the ectoderm's BMP response. NEW `GO:0003714` (IDA,
  PMID:17541407: it still represses when its own binding site is mutated).
  It is also a crest competence factor (module competence part, beside Myc,
  Id3 and Hairy2). York 2024 [PMID:39060477] found it at the border; knocking
  down pou5f3.1 and pou5f3.2 together nearly abolishes snai2 and foxd3,
  pou5f3.2 alone rescues, and gain of function expands pax3, zic1 and snai2.
  NEW `GO:0014029` (IMP, PMID:39060477). **Flag for curators:** I confirmed
  in QuickGO that no POU5 protein in any species carries any crest term. The
  agent judges this curation lag, since the papers date from 2021–2024 and
  same-layer peers such as id3-a and zebrafish mych carry crest terms. But
  this is a systematic absence, and no direct binding to frog crest enhancers
  has been shown. Open: Nicetto 2013 [PMID:23382689] puts Oct25 in the
  notoplate by mid-neurula, which conflicts with York's border expression.
  Oct25 alone was never knocked down. Evolution: pou5 arose in vertebrates
  from a pou3-like ancestor. Lamprey pou5 is absent from the crest yet
  rescues frog crest, so the protein activity predates the crest expression.
  That is the reverse of Id3, where the protein is old and the expression new.

- **sox2.** A blastula pluripotency and neural-plate/neural-progenitor gene,
  *not* a crest participant. Forcing SoxB1 activity at the border lowers foxd3
  and snail2, and Sox2 cannot replace SoxE in crest induction
  [PMID:30144418]. A factor that must be switched off does none of the work,
  so it fails the participation test: no crest term, positive or negative.
  The comparator was checked in QuickGO: no SOX2 or sox3 in any species
  carries a crest term. The Otx2 `protein binding` IPI was changed to
  `GO:0140297` DNA-binding TF binding (Sox2 and Otx2 act together on the Rax
  CNS1 enhancer; mouse Sox2 carries the same term by IPI, verified). NEW:
  `GO:0045665` negative regulation of neuron differentiation and
  `GO:0060041` retina development (both IMP). Module: not a competence member;
  at most an upstream blastula state, or a knowledge gap on the SoxB1 → SoxE
  hand-off. Evolution: lamprey also switches soxB1 off in premigratory crest
  as soxE comes on [PMID:39060477], so the hand-off dates to the vertebrate
  ancestor. Open: blastula evidence comes from combined Sox2+Sox3 knockdown,
  and dominant-negative Sox2 cannot separate the two.

- **sox3-a.** Maternal Sox3 binds and represses the Xnr5 promoter, keeping
  nodal-related genes vegetal (`GO:0001704` accepted). NEW `GO:0141064`
  zygotic genome activation [PMID:37787392]; comparator verified in QuickGO
  (zebrafish pou5f3 and the SoxB1 sox19b carry it by IMP). NEW `GO:0021990`
  neural plate formation: a Sox3 morpholino blocks Noggin-driven neural
  induction and a resistant RNA rescues it [PMID:18992330]. No crest term
  (same reasoning as sox2; verified that no SoxB1 protein in any species
  carries one). Two rows cite papers whose cached abstracts never mention
  Sox3 (PMID:17950579, PMID:17875931); full texts were unavailable, so they
  were kept as non-core rather than removed. P55863 is sox3.S, the exact
  construct used for the chromatin-binding maps.

### Tier 3 synthesis (2026-10-07)

| Gene | Layer | NC term | Module |
|---|---|---|---|
| snai1 | Blastula competence, then earliest crest specifier | `GO:0014036`, `GO:0001755` | Specification part (Zic1 → Snail1 → Snai2) |
| pou5f1.1 (Oct25) | Germ-layer timing (core) + crest competence | `GO:0014029` (NEW, flagged) | Competence part |
| lin28a | General pluripotency/timing RNA-binding factor (frog) | none (chick-only crest evidence) | Knowledge gap only |
| sox2 | Blastula pluripotency, neural progenitor | none | Not a member; SoxB1 → SoxE hand-off gap |
| sox3-a | Maternal germ-layer patterning, genome activation, neural competence | none | Not a member; SoxB1 → SoxE hand-off gap |

Cross-cutting findings:
- **"Shared with the blastula" does not mean "participates in the crest."**
  Of the five pluripotency-programme genes, two keep working inside the
  crest-forming cells (Snail1 as a specifier, Oct25 as a competence factor).
  One has crest evidence only in chick (Lin28). Two must be switched *off*
  for crest to form (Sox2, Sox3). The retained-potential hypothesis is
  really about a subset of the programme, plus a required hand-off.
- **Two evolutionary routes into the competence layer.** Oct25/pou5 is a
  vertebrate-new protein whose crest expression varies by lineage (lamprey
  pou5 is absent from crest but still rescues frog crest). Id3 is an old
  protein whose crest expression is new. The SoxB1 → SoxE hand-off is
  shared with lamprey, so it dates to the vertebrate ancestor.
- **Miscitation pattern.** PMID:15242799 (an Id2 paper) is the cited source
  for TAS crest rows on twist1, snai2 and snai1. Two sox3-a rows cite papers
  about other genes. Report both to the source curators.

### Tier 4 reviews (in progress)

- **TFAP2B (human).** Crest specifier, not a border gene. In chick it comes
  on only at the onset of specification. Knockdown leaves the border intact
  but disrupts specification. It heterodimerises with TFAP2A and recruits it
  to specification enhancers, represses TFAP2C, and brings specification
  forward when introduced early [PMID:31848212, full text]. In frog,
  Pax3/Zic1 activate tfap2b directly [PMID:24360906]. NEW `GO:0014036` (ISS
  from chick). Comparator verified in QuickGO by the agent: no TFAP2B in any
  species carries a crest term, while zebrafish tfap2a/tfap2c (`GO:0014036`)
  and mouse Tfap2a (`GO:0014032`) do; redundancy masks single mutants.
  **Name confusion removal (verified by me from the cached abstract):** the
  two IDA rows from PMID:7559606 were removed. That abstract's "AP-2B" is "a
  dominant-negative inhibitor of AP-2", the alternatively spliced AP-2α
  product [PMID:8321221], not the AP-2β activator. Report this to the source
  curator. Protein binding rows: CITED2 changed to `GO:0001223`, KCTD1 to
  `GO:0001222`, AP-2α self/hetero to `GO:0046982`/`GO:0042803`; UBC9 and
  high-throughput rows removed. Open: mouse Tfap2b is redundant with Tfap2a,
  and Van Otterloo 2022 found no irreplaceable AP-2α/β heterodimer function,
  so necessity rests on chick. Evolution: amphioxus AP-2 is not at the
  border, and lamprey Tfap2 is pan-axial. The A/B/C partner switch looks like
  post-duplication subfunctionalisation, partitioned differently in chick,
  mouse and zebrafish.

### Project-level decision to confirm: GO:0014029 vs GO:0014036

`GO:0014029` neural crest formation is defined as forming the *region of
ectoderm* between the neural plate and non-neural ectoderm. The chain is
`GO:0014036` fate specification part_of `GO:0014034` fate commitment part_of
`GO:0014029`. The sox10 review narrowed specifier genes from `GO:0014029` to
`GO:0014036`, leaving `GO:0014029` for genes that act on the border region as a
whole. Apply this consistently across Tier 1 (and decide whether border
specifiers in Tier 2 should keep `GO:0014029`). This needs curator sign-off,
because it modifies IMP rows to a more specific child term. Applied so far:
sox10, sox9-a and sox8 narrowed to `GO:0014036`; foxd3-a already at `GO:0014034`
(accepted); id3-a deliberately kept at `GO:0014029`, as a non-specifier.
