# fz2 (Frizzled 2, Q9VVX3) - manual literature synthesis

No deep-research API was available for this review. This file is a manual synthesis of the cached
publications (`publications/PMID_*.md`) and the UniProt record, written by the reviewer. All claims carry
inline provenance.

## Identity and architecture

- Swiss-Prot entry FRIZ2_DROME (Q9VVX3), 694 aa, FlyBase FBgn0016797, GeneID 40090.
- Class-F seven-transmembrane receptor: signal peptide (1-22), extracellular cysteine-rich FZ domain
  (Wnt-binding CRD), 7 TM helices, C-terminal cytoplasmic tail with the KTxxxW Dishevelled-binding
  motif and a C-terminal PDZ-binding motif (ASHV) [UniProt; PMID:16682643 "DFz2 contains a PDZ-binding
  motif (ASHV) at the C-terminal tail"].
- PANTHER PTHR11309:SF126 (FRIZZLED-2), Pfam PF01392 (Fz) and PF01534 (Frizzled).

## Wingless receptor (core function)

- Dfz2 was the first Frizzled shown to act as a Wnt receptor: S2 cells transfected with Dfz2 respond to
  Wg by elevating Armadillo, and Wg binds to cells expressing Dfz2 [PMID:8717036 "Moreover, Wingless
  binds to Drosophila or human cells expressing Dfz2."].
- In vivo, fz and fz2 are redundant Wg receptors; double mutants phenocopy wg in epidermis, CNS, heart
  and midgut [PMID:10457026 "Frizzled and Dfrizzled2 function as redundant Wingless receptors in multiple
  embryonic tissues"]; Wg transduction is abolished in fz fz2 double mutant cells in embryo and wing disc
  [PMID:10556068].
- Fz2 cooperates with the LRP5/6 co-receptor Arrow; both are required in S2 cells [PMID:12729465 "Wg signal
  transduction in S2 cells depends on the function of both LRPs and DFz2"]; forced proximity of Arrow to
  Fz2 activates signalling [PMID:12636921]; Wnt bridges Frizzled and LRP into hetero-oligomers that
  recruit Dishevelled via the Frizzled tail [PMID:15459103].
- Binding profiles: most Drosophila Wnts bind multiple Frizzleds [PMID:12205098]; Wg acylation at S239
  is needed for efficient dFz2 binding [PMID:22285813].
- The CRD is dispensable for transducing Wg in vivo in some assays [PMID:15514021], but other work shows
  CRD mutants of Fz are compromised, supporting a capture-then-activate model [PMID:16163385].
- Fz2 stimulates Wg internalization; Arrow is needed for lysosomal targeting of Fz2-Wg complexes
  [PMID:16291792; PMID:16530179]. Fz2 overexpression stabilizes extracellular Wg.

## Non-canonical / alternative signalling

- Frizzled Nuclear Import (FNI) pathway at the larval NMJ: postsynaptic DFz2 is endocytosed, its
  C-terminus is cleaved and imported into the muscle nucleus in a Wg-dependent manner [PMID:16311339];
  transport requires the 7-PDZ protein dGRIP, which binds the DFz2 C terminus via PDZ4/5 [PMID:16682643];
  altered in dfmr1 mutants [PMID:24046358].
- DWnt4-Fz2 signalling in ovarian cell migration, distinct from canonical and PCP branches, requiring
  Dsh and PKC [PMID:11970894].

## Developmental contexts (non-core, outputs of receptor activity)

- Wing margin [PMID:9671581], salivary gland migration (Wnt4-Fz/Fz2) [PMID:17507403], retinal axon
  dorsoventral targeting (DWnt4-Fz2) [PMID:16369482], motor neuron target specificity (Wnt4 repulsion via
  Fz2/Drl-2) [PMID:17764943], dorsal cluster neuron axon extension (Wnt5-Fz/Fz2) [PMID:17032066],
  DCN axon branching [PMID:24303071], ovarian escort-cell differentiation niche [PMID:26452202].

## PMID:22530061 (gene-trap olfactory screen)

- Gene-trap line BG01711 was annotated by BDGP to fz2 (76A1), but 3' RACE showed the vector spliced to
  CG8771 (49B12): "For BG01711, the RACE results showed the vector was spliced to the CG8771 gene at
  cytological region 49B12, contradicting the BDGP prediction at 76A1 in the Frizzled 2 gene." The
  olfactory expression and female olfactory-behaviour defect of BG01711 therefore cannot be attributed
  to fz2; the authors list the candidate as "fz2 or CG8771". This paper provides no reliable evidence
  for an fz2 role in olfaction.
