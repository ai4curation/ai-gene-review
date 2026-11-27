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
- **AI review follow-up.** The InterPro/Ensembl `GO:0003700` row now refines to the Pol II-specific
  transcription-factor activity child `GO:0000981`, while rodent stress-response transfers no longer
  cite the generic JUND AP-1-site sentence as positive support. The core-function prose now
  distinguishes JunD from JUN/JUNB by explicitly including MEN1-dependent restraint of JunD-mediated
  transcription [PMID:9989505, "Menin repressed transcriptional activation mediated by JunD"] while
  keeping direct AP-1 DNA binding and Pol II transcriptional regulation as its molecular core.
- **Chromatin support.** The legacy PMID:1903194 chromatin TAS row is retained as part of JunD's direct
  AP-1 DNA-regulatory mechanism, but its reason now states that the cached abstract supports AP-1-site
  binding and transcriptional activation rather than a separate chromatin assay.
