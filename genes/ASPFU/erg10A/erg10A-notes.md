# A. fumigatus erg10A review notes

## 2026-11-23 review

- Reviewed the new A. fumigatus erg10A stub against Swiss-Prot Q4WLA8,
  PMID:32005728 full text, and the PTHR18919 PAINT snapshot.
- Erg10A is the A. fumigatus PTHR18919:SF156 mitochondrial ACAT1-like
  paralog. Zhang et al. purified residues 36-433, measured activity in both
  reaction directions, solved apo and CoA-bound crystal structures, showed that
  the native-promoter C-terminal GFP fusion colocalizes with MitoTracker, and
  found that erg10A repression is lethal.
- The same paper frames the in-vivo pathway as unknown: "the biological
  function of AfERG10A remains unclear". UniProt's FUNCTION comment records
  the same interpretation, saying Erg10A has no overlapping function with
  Erg10B and seems not to be involved in ergosterol biosynthesis, but its
  PATHWAY comment still places Erg10A in the (R)-mevalonate-from-acetyl-CoA
  pathway. That contradiction is recorded as a UniProt source_defects CHECK.
- The accepted existing mitochondrion rows are left at GO:0005739, matching GOA.
  A new IC row proposes GO:0005759 mitochondrial matrix from the experimentally
  localized mitochondrion, the predicted cleaved N-terminal transit peptide,
  and activity of the recombinant residues 36-433 protein.
- Searches in the 2024-2026 window found no newer direct A. fumigatus erg10A
  biochemical, localization, or pathway-resolution paper.
