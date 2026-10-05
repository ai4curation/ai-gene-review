# xpt curation notes

## 2026-08-13 first-pass review

The reviewed UniProt entry identifies Xpt as the XMP salvage enzyme that
converts xanthine and PRPP to XMP and diphosphate [UniProtKB:Q88CB6, "Converts
the preformed base xanthine"; Rhea 10800]. This is a HAMAP MF_01184 assignment,
not a direct biochemical assay of the KT2440 protein.

GO:0000310 and GO:0032265 capture the core function and process. The broad
pentosyltransferase annotation is marked over-annotated because the exact
substrate-specific term is already present; cytoplasm and broader metabolic
processes remain non-core. PTHR43864:SF1 plus the exact Q88CB6 exemplar defines
the Xpt branch.

## 2026-10-05 review follow-up

The broad `GO:0016763 pentosyltransferase activity` row is recorded as
`MODIFY`, not `MARK_AS_OVER_ANNOTATED`, because Xpt's InterPro-derived parent
term should be replaced by the exact substrate-specific
`GO:0000310 xanthine phosphoribosyltransferase activity`.
