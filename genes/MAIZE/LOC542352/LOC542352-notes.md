# LOC542352 notes

## 2026-10-28 initial review

- fetch-gene resolved A0A804Q7E0 (GeneID 542352, Zm00001eb299370) as requested; GOA has one
  row: extracellular region (IEA, InterPro2GO from IPR018244).
- Protein: acidic PR-1 type CAP-domain protein, signal peptide 1-23, no experimental
  characterization of this gene product. See LOC542352-deep-research-manual.md.
- PMID:23113982 (named by the task as key experimental paper) was read in full: it concerns
  the pr1 (red aleurone1) flavonoid 3'-hydroxylase locus, not this PR-1 protein. Symbol
  collision between alias "PR1" and locus "pr1" [PMID:23113982 "The maize (Zea mays) red
  aleurone1 (pr1) encodes a CYP450-dependent flavonoid 3'-hydroxylase (ZmF3'H1)"].
  NCBI Gene's gene2pubmed/GeneRIF also links the related pr1 paper PMID:21385724 to GeneID
  542352: an upstream NCBI defect (no GO row carries it, so it cannot be put in an
  annotation's source_defects; recorded in reference_review and suggested_questions).
- Extracellular region accepted: signal peptide + PR-1 family secretion to the apoplast.
- No NEW rows: sterol binding (GO:0032934) and defense-response processes are family-level
  inferences / expression-marker evidence only, so left as hypotheses.
