# cia30 notes

## 2026-10-01 Re-review after GOA refresh

- Current GOA has only three rows for cia30: mitochondrion (IBA, IEA) and mitochondrial respiratory chain
  complex I assembly (NAS, PMID:9769214). Four previously reviewed rows disappeared from the current
  snapshot and were marked `retired: true` (reviews kept):
  - GO:0006120 mitochondrial electron transport, NADH to ubiquinone (IBA)
  - GO:0010257 NADH dehydrogenase complex assembly (IBA)
  - GO:0051082 unfolded protein binding (IBA) and (IDA, PMID:9769214) - GO:0051082 is obsolete
    (go-ontology#30962).
- Judgment changes:
  - GO:0006120 IBA: ACCEPT -> MARK_AS_OVER_ANNOTATED. CIA30 is an assembly factor absent from the mature
    complex; requirement for building complex I is not participation in electron transport. Also removed
    from core_functions.
  - Dropped the curator-proposed NEW GO:0044183 protein folding chaperone (NAS) and the corresponding
    core_functions molecular_function: autonomous folding of a client was never assayed; "chaperone" in
    PMID:9769214 means assembly factor. Consistent with the human NDUFAF1 review.
  - Added propagation_review to the retired GO:0051082 IBA row; removed curation commentary from description.
