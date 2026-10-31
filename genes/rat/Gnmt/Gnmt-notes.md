# Gnmt (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Gnmt` resolved P13255 (GNMT_RAT, RGD:2719, GeneID 25134); 53 GOA rows.
- PMID:19239903 cached and read (full text): liver cytosol proteomics, GNMT
  upregulated by betaine in ethanol-fed rats; expression evidence only, no GO row
  derives from it [PMID:19239903 "resulted in the identification of this protein as glycine N-methyltransferase (GNMT) using MALDI-TOF MS and LC-MS/MS"].
- No deep-research keys; manual synthesis in `Gnmt-deep-research-manual.md`.
- Most experimental papers are abstract-only in the cache (10756111, 12054489,
  12859184, 15340920, 17158459, 3838667, 6587377, 8278367); 18501206, 22037183
  and 19239903 have full text.

## Decisions

- Core: glycine N-methyltransferase activity (ACCEPT all 11 rows), folic acid
  binding (5-methyltetrahydrofolate; ACCEPT, no more specific GO term found in
  OLS), cytosol (ACCEPT), SAM catabolic process and L-methionine cycle (ACCEPT).
- S-adenosylmethionine metabolic process (6 rows) -> MODIFY to GO:0050843 and
  GO:0033353, both already on the gene (OLS: both are is_a GO:0046500).
- L-methionine metabolic process ISO -> MODIFY to L-methionine cycle.
- Cytoplasm (EXP, IEA) -> MODIFY to cytosol.
- Glycine catabolic process (IMP, PMID:18501206): full text reports kinetics and
  folate inhibition only; sarcosine is recycled to glycine by SARDH, so the
  GNMT/SARDH loop is SAM disposal rather than glycine catabolism ->
  MARK_AS_OVER_ANNOTATED (expert flag).
- Regulation of gluconeogenesis (IBA, ISO) and glycogen metabolic process (ISO)
  derive from Gnmt-null mouse phenotypes -> MARK_AS_OVER_ANNOTATED (indirect).
  The human GNMT review kept the gluconeogenesis IBA as non-core; this review is
  stricter.
- Selenol Se-methyltransferase (Reactome TAS): GO definition is use of AdoSeMet
  as methyl donor, matching Reactome's claim -> KEEP_AS_NON_CORE (side activity).
- Binding (glycine, SAM, identical protein), homotetramerization and
  methyltransferase complex -> KEEP_AS_NON_CORE.
- No NEW terms proposed. Nuclear pool (PMID:8278367) left as a question rather
  than a NEW row (single line of evidence).

## 2026-10-28 review-fix pass

- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
  (The removed Gnmt quote, about N-acetylation and folate inhibition, also did not bear on glycine catabolism.)
