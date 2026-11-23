# ubiG (PP_1765, Q88M10) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); OpenScientist report
read. Reviewed UniProt entry (HAMAP MF_00472). No KT2440 experiment.

- Both O-methylations: [PMID:10419476 "In addition, E. coli UbiGp was purified and found to
  catalyze both O-methylation steps."]
- GO:0010420 (Coq3 substrate with carboxyl): [PMID:8703953 "UbiG methylates both the derivative
  of the eukaryotic intermediate, 3,4-dihydroxy-5-farnesylbenzoate, as well as that of the E.
  coli intermediate, 2-farnesyl-6-hydroxyphenol."] Real in vitro activity, but the
  carboxylated substrate does not occur in the bacterial pathway (UbiD acts first) ->
  MARK_AS_OVER_ANNOTATED. PAINT has GO:0010420 only at eukaryotic node PTN000566263. For
  yeast/human Coq3 the same term is the physiological activity; the difference is pathway order,
  not sequence.
- Methyltransferase activity (TreeGrafter): MODIFY to both GO:0102208 and GO:0061542.
- Deep research Finding 5 says UbiG serves "aerobic and anaerobic" routes; KT2440 has no
  UbiU/V/T (project pathway report), so the anaerobic part does not apply.

Module agreement: `early_o_methyltransferase_activity` (GO:0102208) and
`late_o_methyltransferase_activity` (GO:0061542). Consistent.
