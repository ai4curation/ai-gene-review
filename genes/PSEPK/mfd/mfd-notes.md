# mfd curation notes

## 2026-08-08 pathway pass

The Q88KZ1 HAMAP record says that Mfd recognizes lesion-stalled RNA polymerase,
mediates its ATP-dependent release, and recruits nucleotide-excision-repair
machinery [file:PSEPK/mfd/mfd-uniprot.txt, "recruitment of nucleotide excision
repair machinery to the damaged"]. Direct E. coli structural work independently
shows stalled-RNAP removal and UvrABC recruitment [PMID:33480355,
"Mfd mediates TCR in bacteria by removing the stalled RNAP concealing the lesion
and recruiting Uvr(A)BC."].

Mfd is a duplex-DNA translocase, not a DNA-unwinding helicase. GO:0003678 was
therefore changed to GO:0015616. The PANTHER family also contains RecG-like
proteins, so module selection additionally requires InterPro IPR004576.

## 2026-11-10 completion pass (Claude, AI-assisted)

Provider deep research is not available for this gene; evidence comes from the Q88KZ1
UniProt record (HAMAP MF_00969 TRCF rule, NCBIfam TIGR00580, InterPro IPR004576 family
memberships), the project OpenScientist NER synthesis, and E. coli orthologue papers that
were reviewed in full for `genes/ECOLI/mfd`.

Verdict revisions, made to align with the CLAUDE.md "correct but general is MODIFY" rule
and with the E. coli review for shared terms:

- GO:0000166 nucleotide binding: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0005524 ATP binding.
- GO:0003676 nucleic acid binding: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0003677 DNA
  binding [PMID:7876261 "Weaker binding to single stranded DNA and no binding to single
  stranded RNA were observed."].
- GO:0016787 hydrolase activity: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0016887 ATP
  hydrolysis activity [PMID:33480355 "ATP hydrolysis is required for Mfd loading."].
- GO:0006281 DNA repair: KEEP_AS_NON_CORE -> MODIFY to GO:0006283 transcription-coupled
  nucleotide-excision repair.
- GO:0005737 cytoplasm: KEEP_AS_NON_CORE -> ACCEPT (core-function location; the nucleoid
  lies in the bacterial cytoplasm).
- Unchanged: GO:0000716 ACCEPT; GO:0003677 KEEP_AS_NON_CORE; GO:0003678 MODIFY to
  GO:0015616 (now with a PANTHER/TreeGrafter source defect, supported by the E. coli NOT
  helicase result [PMID:7876262 "We found that TRCF does not have a helicase activity on
  any of the substrates tested."]); GO:0003684 REMOVE (now with an InterPro2GO source
  defect for IPR004576); GO:0005524 and GO:0016887 ACCEPT; GO:0006355 KEEP_AS_NON_CORE.
