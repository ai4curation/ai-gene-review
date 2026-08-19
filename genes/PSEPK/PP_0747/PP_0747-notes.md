# PP_0747 curation notes

## 2026-08-13 first-pass review

UniProt assigns both EC 2.4.2.8 salvage directions: hypoxanthine plus PRPP to
IMP and guanine plus PRPP to GMP [UniProtKB:Q88PV1,
"PhysiologicalDirection=right-to-left"]. PTHR43340:SF1 and PAINT node
PTN002458265 support the assignment, but Q88PV1 remains an unreviewed entry and
there is no direct KT2440 enzyme assay in the fetched record.

GOA includes hypoxanthine phosphoribosyltransferase activity but omits the
parallel guanine phosphoribosyltransferase activity. The review therefore adds
GO:0052657 as `NEW`, while retaining magnesium binding, localization, and the
broad hypoxanthine metabolic process as non-core context.
