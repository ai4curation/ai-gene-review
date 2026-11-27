# JUND notes

- **Deep research.** Perplexity deep research was unavailable in this worktree during the JUN-family
  review. Continue the review from UniProt, GOA, the PTHR11462 PAINT table, Reactome caches, and cached
  primary literature.
- **Core AP-1 function.** JunD has the same conserved PTHR11462 AP-1 DNA-binding and transcriptional
  activation rows as JUN and JUNB. The JUND UniProt record describes AP-1-site binding, FOS-family
  heterodimerization, and AP-1 complex membership; broad DNA-binding, AP-1-complex ancestor, and
  transcription-regulation rows were refined to the specific AP-1/Pol II terms.
- **MEN1/MAPK10 regulation.** The structural menin paper shows that JunD residues 27-47 form the
  menin-binding motif and that menin binds JunD and blocks JNK-induced phosphorylation
  [PMID:22327296, "Menin also interacts with JunD by directly binding to its N-terminus"]. MEN1 protein
  binding was therefore refined to `GO:0001221` transcription coregulator binding, MAPK10 binding was
  refined to `GO:0051019`, and the row asserting JUND itself has RNA polymerase II repressor activity
  was removed.
- **Over-propagated rodent context.** Multiple GO_REF:0000107 rows are transferred from rodent JunD
  response terms such as circadian rhythm, cold, water deprivation, fatty-acid response and cardiac
  hypertrophy. These were marked over-annotated because they propagate contextual transcriptional
  outputs onto human JUND rather than the direct AP-1 mechanism.
