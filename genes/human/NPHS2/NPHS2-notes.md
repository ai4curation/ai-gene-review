# NPHS2 notes

## 2026-11-05 ORGANELLES ER batch 3 (endoplasmic reticulum rows)

- Row: GO:0005783 IEA (GO_REF:0000044, SL-0095); stays KEEP_AS_NON_CORE; reason rewritten; source_defects entry added.
- UniProt: [file:human/NPHS2/NPHS2-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Endoplasmic reticulum {ECO:0000269|PubMed:23648087}."]; isoform 1 is "Cell membrane {ECO:0000305}".
- Source fetched (PMID:23648087, full text): [PMID:23648087 "Here we show that the short isoform is expressed in human kidneys and localizes to the endoplasmic reticulum"]; [PMID:23648087 "Overexpression in HeLa cells and subsequent immunofluorescence staining revealed that the short isoform was retained in the endoplasmic reticulum and did not traffic to the plasma membrane"]. Mouse delta-exon5 follow-up repeats it in HeLa (PMID:38114895).
- Call: real isoform-restricted retention pool of a natural splice form (ATP7A, ABCA7 precedents) -> KEEP_AS_NON_CORE. Close call with MARK_AS_OVER_ANNOTATED because the ER retention is shown only for overexpressed tagged constructs; stated in the reason.
- The GOA row has no isoform, but the source restricts ER to Q9NP85-2 -> source_defects (UNIPROT, Gene_Product_Form_ID, ADD Q9NP85-2), as for ABCA7.
- No GO:0005789: canonical podocin (intramembrane hairpin 103-123, both termini cytoplasmic) only transits the ER; the retained short isoform's topology is unresolved (partly N-glycosylated near the C-terminus).
