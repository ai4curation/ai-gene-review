# rpr notes

## 2026-09-30

- Reviewed Drosophila `rpr` as the Reaper/RHG IAP-antagonist comparator for
  APOPTOSIS from UniProt, the 43-row GOA seed, and the cached primary
  literature.
- Centered the review on Reaper's direct DIAP1 antagonism: binding DIAP1
  through the IAP-binding motif, relieving DIAP1-mediated DrICE inhibition,
  stimulating UbcD1-dependent DIAP1 autoubiquitination and turnover, and
  inhibiting DIAP1-mediated DTRAF1 degradation in a contextual JNK branch.
- Kept the GH3/phospholipid mitochondrial outer-membrane rows as part of the
  core mechanism because GH3-dependent membrane association and Reaper
  self-association make DIAP1 degradation and apoptotic signaling efficient.
- Modified broad `GO:0006915 apoptotic process` rows to
  `GO:0097190 apoptotic signaling pathway` where the source supported direct
  Reaper IAP-antagonist activity upstream of caspase activation.
- Treated salivary-gland, midgut, neuroblast, ecdysone, and DNA-damage rows as
  non-core developmental or stress deployments of the same IAP-antagonist
  module.
- Narrowed the generic Reaper-DIAP2 protein-binding row to ubiquitin protein
  ligase binding as a contextual IAP interaction, and removed the dBruce
  ubiquitin-conjugating-enzyme-binding row because dBruce physically binds
  Reaper to ubiquitinate and restrain it, making Reaper the substrate rather
  than the actor in that anti-apoptotic ubiquitination event.
- Left abstract-only or source-mismatched rows unresolved for Sickle,
  DmIKKepsilon, dOmi, larval optic-neuropil, and larval-CNS-remodeling papers
  when the cached text did not verify a Reaper-specific assay.

## Follow-up on UniProt FUNCTION (Dredd)

- UniProt's only FUNCTION sentence says Reaper "acts on the effector Dredd". The support is induction of dredd RNA and Dredd processing,
  plus genetic modulation [PMID:9740659 "Heterozygosity at the dredd locus suppressed apoptosis in transgenic models of reaper- and grim-induced cell killing"].
  This is indirect; Dredd is now known mainly as the Imd-pathway caspase [PMID:11269502]. Recorded as a MISSING_STATEMENT on the
  UniProt reference (FUNCTION omits DIAP1 antagonism). No annotation change.
