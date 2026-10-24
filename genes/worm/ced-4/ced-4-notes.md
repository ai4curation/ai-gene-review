# ced-4 notes

## 2026-09-30 APOPTOSIS manual review

CED-4 is the C. elegans Apaf-1-like adaptor for the canonical EGL-1/CED-9/CED-4/CED-3
apoptotic pathway. Its direct activity is to become an ATP/Mg-bound oligomeric
apoptosome that binds CED-3 and stimulates CED-3 autocatalytic maturation, not
to execute the death program itself [PMID:24065769, "CED-4 forms an octameric
apoptosome, which binds the CED-3 zymogen and facilitates its autocatalytic
maturation"]. Broad `GO:0006915 apoptotic process`, `GO:0043065 positive
regulation of apoptotic process`, `positive regulation of protein processing`,
and generic peptidase-activator rows were therefore narrowed to apoptotic
signaling or apoptotic cysteine-type endopeptidase activator activity.

- ATP/Mg and oligomerization are core CED-4 biochemistry. CED-4 preferentially
  binds ATP [PMID:11779177, "CED-4 exhibited a marked preference for ATP over
  dATP"], is held by CED-9 as an asymmetric dimer, and after EGL-1-dependent
  release further oligomerizes to stimulate CED-3 autoactivation
  [PMID:16208361, "The released CED-4 dimer further dimerizes to form a
  tetramer"].
- CED-3 binding is the informative interaction. Generic `protein binding`
  rows to CED-3 were narrowed to `GO:0089720 caspase binding` using both early
  two-hybrid work [PMID:9109415, "CED-4 was found to interact with CED-3"] and
  the later apoptosome/CED-3 structural study [PMID:24065769, "how CED-4
  recognizes CED-3"].
- CED-9 binding is real but the existing CED-4-side GO term is too generic.
  The structural and reconstitution evidence shows that CED-9 restrains CED-4
  until EGL-1 triggers CED-4 release [PMID:16208361, "This specific interaction
  prevents CED-4 from activating CED-3"], but `GO:0005515 protein binding` does
  not express that mechanism and no precise CED-9-binding MF term was available.
- CED-4 localization changes are part of pathway control. Endogenous CED-4 is
  mitochondrial with CED-9 in wild-type embryos, then becomes perinuclear or
  nuclear-envelope associated in cells induced to die [PMID:10688797,
  "Endogenous CED-9 and CED-4 proteins localized to mitochondria"; PMID:16938876,
  "matefin/SUN-1 is the NE receptor for CED-4"].
- The adenoviral E1B 19K paper supports a real viral BH-domain/CED-4
  interaction and CED-4-dependent FLICE activation in mammalian cells, but this
  is not the core worm function [PMID:9742122, "CED-4 interacts independently
  with two regions of E1B 19K: BH3 and the central conserved region"].
- CED-4 has two full-text-supported non-core outputs that should be kept
  separate from whole-cell apoptosis: a caspase-independent cell-size control
  phenotype in growth-regulator mutants [PMID:18635357, "CED-4 opposes the
  cell size regulatory action of TFG-1"] and a local CED-pathway role in
  eliminating transient presynaptic material in RME neurons [PMID:26074078, "the
  conserved apoptotic cell death (CED) pathway and axonal mitochondria are
  required for the elimination of transiently formed clusters of presynaptic
  components"].
- Several organismal endpoints were intentionally left conservative. Autophagy
  synthetic embryogenesis rows, a DRE-1/CED-9 F-box row, the BET-1/SUMO muscle
  homeostasis row, and the CED-3/miRNA heterochronic row are all biologically
  plausible tails of ced-4 biology, but their cached abstracts do not establish
  the exact CED-4 assertion.

