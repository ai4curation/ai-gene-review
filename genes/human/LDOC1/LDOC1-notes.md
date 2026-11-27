# LDOC1 (Leucine Zipper Down-Regulated In Cancer 1 / SIRH7 / RTL7) — curation notes

SIRH7/RTL7 is a *Mart*/*Sushi-ichi*-derived (Ty3/Gypsy *gag*-like) domesticated
retrotransposon gene. In human it is studied as a nuclear regulatory adapter and
a frequently down-regulated/silenced gene in cancer, not as a capsid-forming Gag
like PEG10/RTL1.

## Function
- Acts as a **nuclear protein-interaction adapter** that binds partner proteins
  and promotes their destabilization; the core activity is captured by
  GO:0030674 protein-macromolecule adaptor activity.
- Negatively regulates canonical NF-κB signaling and promotes apoptosis
  [PMID:27076087 "LDOC1 gene is a known regulator of nuclear factor mediated pathway to apoptosis through inhibition of nuclear factor kappa B"].
- Best-defined mechanism: destabilizes the nucleolar GTPase GNL3L, lowering the
  p65 NF-κB subunit
  [PMID:27764577 "ectopic expression of LDOC1"; "destabilizes endogenous GNL3L levels"].
- Also restrains JAK2/STAT3 signaling (routing phospho-JAK2 for degradation via
  the E3-ligase adaptor LNX1) and modulates histone H2B monoubiquitination.
- An experimentally confirmed NOD2 interactor whose expression is modulated by
  LPS+MDP stimulation, placing it peripherally in the NOD2 innate response
  [PMID:27812135 "Nod2, Vim and Chmp5 were significantly upregulated while Ldoc1 and Trim41 appeared down regulated by a LPS + MDP stimulation"].

## Curation decisions
- Bare GO:0005515 protein-binding rows (large-scale interactome hits) removed
  under the protein-binding policy; the informative MF is the adaptor activity.
- No GeneReviews/Mendelian-disease baseline; LDOC1 is a cancer-associated
  regulator rather than a Mendelian-disease gene.
