# HNF4A (P41235) — review notes

Deep research: the client timed out, so the review was grounded in UniProt, GOA and cached
abstracts. The provider finished afterwards and `HNF4A-deep-research-falcon.md` is committed; it
was checked against this review on 2026-10-11.

- It agrees on the core annotation: a nuclear, sequence-specific DNA-binding transcription factor
  acting as a homodimer on DR1 elements (two AGGTCA-like half-sites separated by one nucleotide),
  able to activate or repress depending on locus and cell state.
- It qualifies the fatty-acid ligand claim in a way this review should follow. Linoleic acid
  occupancy is real and reversible, and falls on fasting, but ligand-free HNF4A still bound DNA
  and adding linoleic acid did not detectably activate transcription in the tested reporters. So
  HNF4A should not be annotated as requiring a fatty-acid ligand for activation; binding and
  ligand-dependent control are different claims.
- It adds direct structural support for the LBD's allosteric role in DNA binding: a 2.9 A
  structure of a multidomain construct (residues 46-368) as a DNA-bound homodimer, with measured
  DR1 affinity improving from about 6,000 nM for DBD-hinge alone to 82 nM for the multidomain
  construct.
- It stresses the P1/P2 isoform split (P1 giving HNF4alpha1-6, predominant in adult liver; P2
  giving HNF4alpha7-12, important in developing pancreas and intestinal crypt), and that HNF4G can
  compensate for some HNF4A functions, so results from perturbing both paralogs cannot be assigned
  to HNF4A alone.
- It reports that HNF4A restricts accessibility at selected acute-phase loci (HP, SAA1/2, FGG)
  while maintaining it at G6PC1, so it is not purely an activator.

- Orphan nuclear receptor TF, DNA binding as homodimer, constitutive fatty-acid ligand
  [PMID:12193589 "fatty acids are endogenous ligands for HNF4 alpha"]; activates apolipoprotein and hepatic genes
  [PMID:7615825 "dramatically stimulates apoAI gene expression in Caco-2 cells but not in HepG2"].
- Beta cell / HI: [PMID:17407387 "Mice with pancreatic beta-cell deletion of Hnf4a had hyperinsulinaemia in utero and hyperinsulinaemic hypoglycaemia at birth"].
- Core: nuclear receptor activity (GO:0004879) / DNA-binding transcription activator activity, RNA pol II-specific;
  positive regulation of transcription by RNA polymerase II; nucleus.
- regulation of insulin secretion (GO:0050796) kept NON-CORE: HNF4A acts upstream through target-gene transcription,
  so it is not placed in core_functions. dismech nodes bind only GO:0050796 / GO:0030073; they carry no TF MF term.
- signaling receptor binding (PMID:12220494) MODIFY -> transcription coactivator binding (the assay was LBD-coactivator interaction).
- 18 protein-binding IPIs REMOVED (uninformative).
