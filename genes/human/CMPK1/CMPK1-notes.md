# CMPK1 (P30085, UMP-CMP kinase) curation notes

## Literature search (2026-11-13)

`just deep-research human CMPK1 --provider perplexity` failed (provider not available).
The review uses the cached GOA-cited publications (PMID:10462544, PMID:11912132, PMID:40615,
PMID:23416111; all abstract-only), Reactome R-HSA-73548/R-HSA-75125/R-HSA-499943 and the
curated UniProt record.

- Substrates: UMP and CMP best, dCMP good, dUMP/AMP/dAMP poor [PMID:10462544 "We showed that
  the recombinant UMP-CMP kinase phosphorylated CMP, dCMP, and UMP with highest efficiency and
  dUMP, AMP, and dAMP with lower efficiency."].
- Role: "plays a crucial role in the formation of UDP, CDP, and dCDP, which are required for
  cellular nucleic acid synthesis" [PMID:11912132].
- Localization: predominantly cytoplasmic [PMID:11912132 "UMP/CMPK localized predominantly to
  the cytoplasm."]; GFP fusion in cytosol and nucleus [PMID:10462544].
- The TAS uridine kinase row (PMID:10462544) is the wrong reaction (UCK1/UCK2 make UMP from
  uridine); the derived UMP biosynthetic process IEA (GO_REF:0000108) is removed with it.
- NDP kinase side activity of AK-family enzymes is from PMID:23416111 (in vitro).
- PANTHER: PTHR23359:SF206 (UMP-CMP KINASE); covered by the PTHR23359 family review.
- `just paint-losses human CMPK1`: IRD PTN000599579 on GO:0004017 (AMP kinase activity) applies;
  the review has no AMP kinase row, so it agrees.
