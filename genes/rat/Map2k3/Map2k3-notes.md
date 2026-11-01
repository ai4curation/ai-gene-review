# Map2k3 (rat) review notes

## 2026-10-28 session

- Task named B1H230; `just fetch-gene rat Map2k3` resolved F7EXM7 instead. Both are TrEMBL
  entries with gene name Map2k3 and RGD:1306620; the GOA file (37 rows, incl. RGD IDA/IEP)
  is keyed to F7EXM7. B1H230 still exists but carries only ~10 electronic GOA rows.
  Reviewed F7EXM7. F7EXM7 = B1H230 + 87-aa N-terminal extension (residues 88-434 of F7EXM7
  are identical to B1H230), so residue numbers in this review are F7EXM7 numbers; human
  Ser218/Thr222 = rat S305/T309.
- Key rat paper PMID:20550965 (full text): immune-complex kinase assay of endogenous MKK3
  from perfused rat hearts with GST-p38 + GST-ATF2; MKK3 activated by ischaemia (high basal,
  sustained) and by sorbitol (positive control). Supports MAPKK activity directly for rat
  -> wanted a NEW IDA MF row, but validation forbids NEW for a term already in GOA; the rat evidence is cited on the accepted MAPKK rows instead [PMID:20550965 "1 μg GST-p38 and 4 μg GST-ATF2 for MKK3 and MKK6"].
- PMID:14670949 (LPS in astrocytes) and PMID:9779826 (postnatal heart expression) are
  abstract-only.
- Mouse ISO donors (MGI:1346868) read: PMID:10097111 (full text), PMID:10202148,
  PMID:15767678 (full text), PMID:11593045, PMID:18948261.
- Decisions kept consistent with the human MAP2K3 review: generic kinase / Ser / Tyr / Ser-Thr
  kinase rows MODIFY to MAP kinase kinase activity (GO:0004708; note GO:0004708 is_a
  GO:0004712, not a descendant of GO:0004713/GO:0106310/GO:0004674 - checked with OAK);
  hippo, VEGF, endothelial migration rows non-core; DNA-templated transcription
  over-annotated; protein kinase binding non-core.
- GO:0038066 p38MAPK cascade is_a GO:0000165 MAPK cascade (OAK), so MAPK cascade rows are
  MODIFY -> GO:0038066. GO:0031098 SAPK cascade is not an ancestor of GO:0038066 (OAK), so it
  is accepted as its own correct grouping.
- positive regulation of MAPK cascade rows: MKK3 is a member of the cascade, not a regulator;
  MODIFY -> GO:0038066 and source_defects recorded. [Corrected 2026-10-28: superseded; these rows now MODIFY -> GO:1900745 and the source_defects are withdrawn, see the dated section below.]
- Comparator check for NEW: none of the process terms proposed; only one NEW MF row.
- No CC rows in GOA; no rat localization data, so no NEW CC row (human evidence is TAS only).

## 2026-10-28: positive regulation of MAPK cascade rows (PR #5678 follow-up)

The two GO:0043410 rows (ARBA IEA, ISO from mouse) were first MODIFYed laterally to GO:0038066 p38MAPK cascade, with SUSPECTED WRONG_TERM defects, on the view that a cascade kinase should not carry a regulation term. The rat Map2k7 and Map3k5 reviews (PR #5679) settled on the GO convention that cascade kinases also carry the positive-regulation term. [Corrected 2026-10-28: overstated. Curators give cascade kinases the positive-regulation term in some cases (human MAP3K5 by IMP, PMID:23000344; rat Map2k7 by RGD IDA from PMID:10051439, PMID:11849756 and PMID:17064355), but not consistently at the MAP2K tier.] To match, both rows now MODIFY to the descendant GO:1900745 positive regulation of p38MAPK cascade, and the two source defects are withdrawn. p38MAPK cascade remains the core process.
