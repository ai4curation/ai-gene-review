
## Completion pass (ImuABC module curation)

- Status set to COMPLETE; all 13 rows now carry vetted quotes from the UniProt record, the
  falcon deep-research report, PMID:33393180 and PMID:21261833.
- Corrected an over-claim: the previous review asserted, as a RESULTS finding of
  PMID:33393180, that RecA*PP "fully cleaves" LexA1. Only the abstract is cached and it does
  not state that; the claim reaches us through the provider report's quotation of the full
  text. The finding is now split, the reference carries full_text_unavailable, and no
  annotation rests on the unverified claim. What the abstract does establish is used instead:
  [PMID:33393180, "sensitive to DNA damage and displays poor homologous recombination efficiencies."]
- Action changes for consistency with the other genes of this cassette and with the term
  relations: GO:0005737 cytoplasm and GO:0005829 cytosol ACCEPT -> KEEP_AS_NON_CORE
  (location is not the core function); GO:0006974 DNA damage response ACCEPT ->
  KEEP_AS_NON_CORE (parent of the GO:0009432 SOS response row that carries the core claim);
  GO:0003684 damaged DNA binding ACCEPT -> KEEP_AS_NON_CORE (a UniRule transfer shared with
  E. coli RecA; the core binding activity is ssDNA binding).
- GO:0009432 treatment across this module's genes, for the record: ACCEPT on recA (it is the
  inducer), KEEP_AS_NON_CORE on imuA/PP_3117 (regulon effector), MARK_AS_OVER_ANNOTATED on
  lexA2 (LexA1, not LexA2, runs the canonical SOS regulon in KT2440).
