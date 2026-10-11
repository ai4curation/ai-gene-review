# HNF4A (P41235) — review notes

Deep research: falcon timed out. Review grounded in UniProt, GOA and cached abstracts.

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
