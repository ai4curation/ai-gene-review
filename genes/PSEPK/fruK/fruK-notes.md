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
