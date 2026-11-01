# Musk (rat, UniProt Q62838) - manual literature synthesis

No deep-research provider was available for this session; this synthesis was written by hand
from the cached publications in `publications/` and the UniProt record `Musk-uniprot.txt`.

## Identity and architecture

- Rat Musk encodes muscle-specific kinase (MuSK), an 868-aa single-pass type I membrane receptor
  tyrosine kinase (UniProt Q62838; RGD:3211; GeneID 81725).
- Ectodomain: three Ig-like domains plus a Frizzled-like cysteine-rich domain; cytoplasmic
  juxtamembrane NPXY motif (Tyr553) and a tyrosine kinase domain with an activation loop
  (Tyr750/754/755) [PMID:20603078 "We showed previously that incubation of MuSK(cyto) with Mg-ATP results in trans-autophosphorylation of Tyr553 (juxtamembrane region) and Tyr750, Tyr754, and Tyr755 (activation loop)"].
- Ig1-2 crystal structure of rat MuSK: I-set Ig domains; a hydrophobic patch on Ig1 is needed for
  agrin-induced activation [PMID:17011580 "residues in this hydrophobic patch are critical for agrin-induced MuSK activation"].

## Catalytic activity and activation

- Kinase activity of the rat cytoplasmic domain measured directly; autophosphorylation relieves
  autoinhibition [PMID:12220490 "Steady-state kinetic analysis demonstrates that autophosphorylation results in a 200-fold increase in k(cat) and a 10-fold decrease in the K(m) for ATP"].
- Dok7 is both a substrate and an activator; Dok7 PH-PTB dimer bound to pTyr553 promotes
  trans-autophosphorylation [PMID:20603078 "Dok7 is not only a substrate of MuSK, but also an activator of MuSK's kinase activity"].
- Agrin does not bind MuSK directly; LRP4 is the agrin receptor and forms a complex with MuSK
  [PMID:18848351 "is a receptor for Agrin, forms a complex with MuSK, and mediates MuSK activation"];
  [PMID:21419809 "Agrin does not bind MuSK directly but interacts with Lrp4, a member of the LDL receptor family [20,21]."].
- CK2 phosphorylates serines in the MuSK kinase insert; needed for AChR clustering
  [PMID:16818610 "We observed CK2-mediated phosphorylation of serine residues within the kinase insert (KI) of MuSK"].
- Wnts bind the MuSK ectodomain (mouse/zebrafish studies) [PMID:22309736 "We provide evidence that Wnt9a and Wnt11 bind directly to the extracellular domain of MuSK"];
  [PMID:22253844 "Wnt4 not only interacts with MuSK ectodomain but also mediates MuSK activation"].

## Biological role

- NMJ formation and maintenance: RNAi of MuSK in rat muscle in vivo blocks NMJ formation and
  disassembles existing NMJs [PMID:14749715 "plasmids that trigger RNAi to MuSK induced the disassembly of existing NMJs"].
- AChR clustering downstream of agrin [PMID:12220490 "agrin released from motor neurons stimulates MuSK autophosphorylation in the kinase activation loop and in the juxtamembrane region, leading to clustering of acetylcholine receptors"].
- Expression: muscle lineage, concentrated at the NMJ in adult muscle, re-induced by denervation
  or paralysis [PMID:7546737 "MuSK expression is dramatically induced throughout the adult myofiber after denervation, block of electrical activity, or physical immobilization"];
  [PMID:9698449 "MuSK is associated with the earliest observable AChR clusters at the developing motor endplate"].
- Brain role (rat hippocampus, antisense knockdown): memory consolidation, LTP, theta oscillation
  [PMID:16870737 "MuSK expression in the hippocampus is required for memory consolidation"].
- Other expression sites: retinal astrocytes [PMID:16899069], inner ear [PMID:18420419].
- Interactors: 14-3-3 gamma (synaptic gene transcription) [PMID:15604144]; Rinl, a Rab5/Rab22 GEF
  that binds the MuSK kinase domain independent of phosphorylation [PMID:21419809 "Rinl interacts with MuSK independent of its phosphorylation and localizes to NMSs."].
