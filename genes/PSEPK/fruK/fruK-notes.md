# fruK curation notes

## Boundary and evidence

FruK (Q88PQ4; PP_0794) is the ATP-dependent 1-phosphofructokinase in the
fruBKA operon. The exact UniProt record assigns EC 2.7.1.56 and RHEA:14213 for
conversion of fructose 1-phosphate plus ATP to fructose 1,6-bisphosphate plus
ADP and proton. Primary KT2440 literature describes the same locus as
containing "a third gene needed for F1P phosphorylation, fruK" and identifies
FruK as 1-phosphofructokinase [PMID:27933319].

The generic phosphofructokinase annotation was marked over-annotated because it
can be confused with fructose 6-phosphate kinase activity; GO:0008662 is the
exact molecular function. ATP binding and predicted cytosolic localization were
retained as non-core properties.

The broad carbohydrate-catabolic annotation `GO:0016052` was modified to
`GO:0006001` because FruK is the fructose-specific `fruBKA` step needed for
fructose 1-phosphate phosphorylation
[PMID:27933319 "a third gene needed for F1P phosphorylation, fruK"].


## 2026-11-06 comparative fructose-PTS review

Reviewed all original annotation rows and complete biological scope. Payloads, row order and source bytes are preserved. Broad true terms were refined rather than called over-annotated. No new GO annotation is proposed solely to fill a pathway diagram. Current GO definitions were checked against QuickGO; net phosphohistidine-donor transport and the immediate phosphocysteine step are compatible descriptions of one group-translocation mechanism.

The existing genuine OpenScientist report was consulted and remains unchanged. Its cytosolic placement is an inferred localization consistent with soluble kinase chemistry, not a reported KT2440 localization assay.
