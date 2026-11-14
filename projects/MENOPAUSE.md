---
title: "Menopause and reproductive ageing: the KNDy, gonadotropin and estrogen-receptor genes"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, worm]
genes: [TACR3, TAC3, KISS1R, KISS1, FSHR, ESR2, Tacr3, Tac2, Kiss1r, Kiss1, fshr-1]
---

# Menopause and reproductive ageing: the KNDy, gonadotropin and estrogen-receptor genes

**Bottom line:** the menopausal transition is a normal life stage, not a disease, and GO
treats it that way: `GO:0042697` menopause and its parent `GO:1990636` reproductive
senescence are phase terms that GO says must not be used for direct annotation, and
QuickGO shows no annotations to either. This project therefore curates the gene
products whose activities the transition changes, starting with the hypothalamic
circuit that generates GnRH pulses and, after estrogen withdrawal, drives hot flushes:
neurokinin B (TAC3) acting on NK3R (TACR3) and kisspeptin (KISS1) acting on KISS1R, in
arcuate kisspeptin / neurokinin B / dynorphin (KNDy) neurons, together with the FSH
receptor and estrogen receptor beta. Wave 1 covers six human genes, their four mouse
orthologs, the seven production GO-CAMs that contain them, five PANTHER families, and a
module for the KNDy pulse generator.

## Scope rules

- Never annotate `GO:0042697` or `GO:1990636`. A menopausal context belongs in a
  review's description, or as an annotation extension (`happens_during`), not as a
  biological process term.
- Association with age at natural menopause, or with bone density in postmenopausal
  women, is genetic association, not function. On its own it supports no process term
  (the KL review applies the same rule to a bone-density association in its existing
  annotations).
- Ligand and receptor terms stay on the right side of each pair: hormone or receptor
  ligand activity on TAC3 and KISS1, receptor activity on TACR3, KISS1R and FSHR.
- Thermoregulation: GO's heat-dissipation terms (`GO:0031653`, `GO:0031654`,
  `GO:0031656`) carry no annotations in any species, so the hot-flush role is
  annotated to `GO:0001659` temperature homeostasis. In human this rests on drug and
  infusion studies (NK3R antagonist trials in postmenopausal women; NKB infusion in
  premenopausal women), and in mouse on a selective NK3R agonist plus manipulation of the
  kisspeptin and NK3R neuron populations.

## Wave 1 status

| Artifact | Items | State |
|---|---|---|
| Human gene reviews | TACR3, TAC3, KISS1R, KISS1, FSHR, ESR2 | done |
| Mouse ortholog reviews | Tacr3, Tac2, Kiss1r, Kiss1 | done |
| Ortholog revisit | worm fshr-1 (hormone-receptor rows reinstated) | done |
| GO-CAM reviews | 68d5ebd600000043, 68d5ebd600000736, 68d5ebd600001111, 68d5ebd600001504, 59dc728000000351, 69b3372b00003343, 6606056e00000678 | done |
| PANTHER family reviews | PTHR46925, PTHR15536, PTHR45695, PTHR16955, PTHR24372 | done |
| Module | `kndy_gnrh_pulse_generator` | draft |

## The KNDy module

`modules/kndy_gnrh_pulse_generator.yaml` models the arcuate oscillator as five parts:
estradiol negative feedback through ESR1 (linked to the `estrogen_receptor_signaling`
module); neurokinin B autoexcitation (TAC3, NK3R, Gq); dynorphin termination of each
burst (PDYN, KOR); kisspeptin output onto GnRH neurons (KISS1, KISS1R, Gq, a TRPC
channel), with direct arcuate and relayed rostral routes as alternatives; and GnRH
release. The pituitary steps (GnRH receptor, gonadotropin secretion) and the median
preoptic thermoregulatory output are outside its boundary: the second uses the same
NKB–NK3R pair on a different neuron population and is a candidate for its own module.
The feedback loop is left open, because estradiol comes from the gonad, which is also
outside the boundary. ESR1, OPRK1, GNRH1 and TRPC4 have no gene reviews yet, and the
module proposes GO terms for GnRH secretion, its regulation, and kisspeptin receptor
activity.

## Findings for upstream resources

Each finding is recorded in a structured field (`source_defects`, `proposed_action`,
`proposed_new_terms` or an ontology-change request) in the file named.

### PAINT and PANTHER

- **PTHR24372 (LGR family).** The root IBD for `GO:0008528` G protein-coupled peptide
  receptor activity is too deep: peptide ligands are ancestral only to the type C
  (relaxin) receptors, and GO files the glycoprotein-hormone receptor activities under
  `GO:0016500`. Proposed: replace it with `GO:0004930` at the root. The LGR6 clade
  lacks the IRDs that prune cAMP and hormone signalling from LGR4 and LGR5. Human LGR6
  and mouse and rat Lgr4 sit in the SLIT tree (PTHR45836), so mouse and rat Lgr4
  inherit axon-guidance terms.
- **PTHR45695.** Only 19 of the 58 reviewed entries InterPro assigns to this family are
  in PANTHER's own tree for it. KISS1R itself sits in PTHR24230, and 11 of the 13 PAINT
  nodes in the slice belong to other trees. In PTHR24230, peptide-receptor terms at the
  root reach the leukotriene receptors, and galanin receptor activity is placed one node
  too deep. `just paint-losses` reports "no loss" for proteins that are absent from the
  tree it searched, so its silence for KISS1R was not a check.
- **PTHR15536.** The blood-pressure IBD rests on one rat seed from central agonist
  pharmacology; proposed for removal.
- **PTHR46925.** NK3R's own `GO:0016498` has no IBD at its subfamily node, although
  the NK1R and NK2R terms are placed at theirs.

### GO-CAM

- The Gs/cAMP NKB model (68d5ebd600000043) has no human evidence for NK3R coupling to
  Gs; its edge rests on one introduction sentence in a rat cell-line paper.
- The kisspeptin bone model (68d5ebd600001504) uses `RO:0002413` (provides input for)
  where the step is direct positive regulation, lists active SRC as the receptor's
  input, and declares no cell type for an osteoclast-specific claim.
- Both FSH models cite PMID:27889227, a GPCR-trafficking review that never mentions
  FSH. The generic FSH model (59dc728000000351) also uses the XLalphas entry instead of
  Gs-alpha, cites PMID:123 (a 1975 gastric-surgery paper) for an edge, and draws the
  direct receptor-to-Gs step as indirect. The granulosa model (69b3372b00003343) has two
  edges citing unrelated papers, a malformed `GO_REF:000024`, and a process nested
  inside itself.
- In the UBR5/ESR1 model (6606056e00000678), the cited paper shows the coactivator
  competition for the retinoic acid receptor only, and does not assay ESR1
  ubiquitination.

### GO ontology

- No term exists for GnRH secretion or its regulation (only response to GnRH and
  gonadotropin secretion), nor for kisspeptin receptor activity; the KISS1 review
  proposes "kisspeptin receptor signaling pathway".
- `GO:0004963` follicle-stimulating hormone receptor activity is not under
  `GO:0004930`, unlike its sibling receptor activities, and `GO:0042699` FSH signalling
  is `part_of` ovarian follicle development, although FSH also signals in Sertoli
  cells. Both are recorded as change requests in the FSHR review.

### UniProt and GOA

- Mouse Kiss1 (Q6Y4S4) supports its function statement with an experimental-evidence
  code on a paper whose abstract describes immature female rats (PMID:15486019).
- Three ISO rows on mouse and rat Tac3 cite human TAC3 annotations that human TAC3 no
  longer carries.
- PMID:16174717 circulates as "Dhillo 2005 kisspeptin"; it is a thyroid-cancer paper.
  The human kisspeptin-54 infusion study is PMID:16174713.

## Wave 2 plan

- ESR1 (about 330 GOA rows), and the estrogen-receptor family PTHR48092; bring the
  DRAFT `estrogen_receptor_signaling` module up to review standard.
- The remaining GnRH-axis genes: GNRH1, GNRHR, LHB, LHCGR, OPRK1 (dynorphin's receptor
  in KNDy neurons; PDYN is already reviewed).
- Premature ovarian insufficiency genes: MCM8, MCM9, FOXL2, BMP15, GDF9, NOBOX, FIGLA,
  EIF4ENIF1.
- A family review of PTHR24230, the PANTHER tree that actually holds KISS1R, where the
  PAINT fixes found under PTHR45695 belong.
- Rat orthologs, where rat pharmacology is the source of many of the transferred rows.
