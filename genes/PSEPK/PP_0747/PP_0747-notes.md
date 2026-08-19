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

## 2026-08-19 OpenScientist report screening

The OpenScientist report corroborates that no direct biochemical or structural
study of the KT2440 protein was found [file:PSEPK/PP_0747/PP_0747-deep-research-openscientist.md,
"there is, to date, no published biochemical or structural study of the KT2440
PP_0747 protein itself"].

The report's genome-context argument is incorrect: it calls PP_0747 the sole
6-oxopurine phosphoribosyltransferase and states that KT2440 lacks `xpt`, but
the organism has `xpt`/PP_5265 (Q88CB6), a xanthine
phosphoribosyltransferase [UniProtKB:Q88CB6, "Name=xpt
{ECO:0000255|HAMAP-Rule:MF_01184}; OrderedLocusNames=PP_5265"]. The report's
"sole gateway" and inferred xanthine-specificity claims were therefore not
imported. The dual hypoxanthine/guanine assignment remains grounded in the two
Q88PV1 UniProt/Rhea reactions rather than that faulty genome enumeration.
