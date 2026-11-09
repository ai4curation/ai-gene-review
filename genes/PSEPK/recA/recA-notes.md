
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


## 2026-11-07 — comparative ImuABC annotation audit

Refined broad DNA-binding/process/location claims and synthesized the specific strand-exchange core. Retained conserved ATP-dependent signaling without treating the provider claim of complete LexA1 cleavage as independently verified. PMID33393180 uses EM173 (a prophage-free KT2440 derivative), remains abstract-only, and establishes modest norfloxacin induction. PMID21261833 supplies direct KT2440 recA-dependent formaldehyde survival evidence; PMID37212693 supplies comparative mechanism. The new core term yields an advisory, not a need to manufacture a new row.

The genuine existing provider research was read and preserved unchanged; primary sources control conclusions where reports are stale. PAINT-loss checking completed sequentially, but the target is not a leaf in the available cached family tree: loss status is unavailable, not demonstrated absent. Original ordered annotation payloads and historical NEW actions are preserved; no new row is added. Existing notes above are historical and superseded only where this dated audit explains a correction. All original raw, provider and publication bytes remain unchanged.
