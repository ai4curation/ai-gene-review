# CYP71B1 (Cytochrome P450 71B1) — Thlaspi arvense — review notes

UniProt: P49264 · EC 1.14.-.- · Taxon 13288 (*Thlaspi arvense*) · 496 aa
GenEMBL: L24438 · Family: cytochrome P450, CYP71 clan

## State of knowledge: functionally UNCHARACTERIZED
- The only direct evidence for pennycress CYP71B1 is the **1994 cDNA cloning/sequencing
  note** [PMID:8066138 "Cloning and sequencing of a full-length cDNA from Thlaspi arvense
  L. that encodes a cytochrome P-450"] and a 1996 catalog review listing it as a
  full-length cDNA. **No substrate, reaction, pathway, expression, or subcellular
  localization has been experimentally determined.**
  [file:THLAR/CYP71B1/CYP71B1-deep-research-falcon.md]
- Therefore all GO annotations are conservative **InterPro family-level inferences**, and
  function beyond "plant heme-thiolate monooxygenase" is inference only.

## What can be inferred (family-level)
- Plant P450s are **heme-thiolate monooxygenases** (RH + O2 + NADPH -> ROH + H2O + NADP+),
  with a conserved cysteine coordinating heme iron. UniProt annotates the axial heme-iron
  binding residue at position 436 (by similarity). [UniProt P49264 FT BINDING 436]
- The **CYP71 clan** comprises >50% of plant CYPs and is enriched in **specialized
  (defense) metabolism**; characterized Brassicaceae CYP71s (CYP71A13, CYP71A12,
  CYP71B15/PAD3) act in the tryptophan-derived **camalexin** pathway on the ER.
  [file:THLAR/CYP71B1/CYP71B1-deep-research-falcon.md]
- Most plant P450s are **ER-membrane anchored** (cytoplasmic face), but pennycress
  CYP71B1 has no annotated transmembrane segment or experimental localization, so ER
  membrane localization is a hypothesis, not an annotation.

## Symbol-ambiguity caution
- "CYP71B1" is also an Arabidopsis locus (At1g13080), itself listed only as a *putative*
  P450. Do not conflate the pennycress protein with Arabidopsis CYP71B1 or with MAX1
  (CYP711A1). [file:THLAR/CYP71B1/CYP71B1-deep-research-falcon.md]

## Annotation review decisions
All four GOA annotations are well-supported, conservative P450 family-level inferences →
**ACCEPT** all:
- GO:0004497 monooxygenase activity (IEA/InterPro)
- GO:0005506 iron ion binding (IEA/InterPro) — heme iron
- GO:0016705 oxidoreductase activity, acting on paired donors, O2 (IEA/InterPro)
- GO:0020037 heme binding (IEA/InterPro)

No BP or cellular-component annotation can be confidently assigned beyond the family
level; substrate identification is the key open question (see suggested experiments).
